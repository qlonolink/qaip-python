from __future__ import annotations

import io
import sys
import json
import builtins
from typing import Any, cast
from pathlib import Path
from unittest.mock import patch
from collections.abc import Iterator
from typing_extensions import override

import httpx
import pytest

from qaip import Qaip
from qaip.cli._cli import main

GROUP = "00000000-0000-4000-8000-000000000001"


def invoke(*args: str) -> int:
    with patch.object(sys, "argv", ["qaip", "--error-format", "json", "api", *args]):
        return main()


@pytest.mark.parametrize(
    ("command", "args", "body"),
    [
        ("secrets.update", ["--id", GROUP], {"name": "n"}),
        ("secrets.create", [], {"name": "n", "secret": "test-secret", "type": "github"}),
        ("githubs.create", [], {"name": "n", "repository": "test/repo"}),
        ("search.create", [], {"query": "test"}),
    ],
)
@pytest.mark.parametrize("control", ["extra_body", "extra_headers", "extra_query", "timeout"])
@pytest.mark.parametrize("dry_run", [False, True])
def test_sdk_controls_never_reach_client_or_output(
    command: str,
    args: list[str],
    body: dict[str, object],
    control: str,
    dry_run: bool,
    capsys: pytest.CaptureFixture[str],
) -> None:
    injected = {**body, control: {"secret": "unapproved-value", "X-API-Key": "replacement-key"}}
    with patch("qaip.cli._utils.qaip.Qaip") as factory:
        assert invoke(command, *args, "--json", json.dumps(injected), *(["--dry-run"] if dry_run else [])) == 4
        factory.assert_not_called()
    captured = capsys.readouterr()
    assert captured.out == ""
    assert json.loads(captured.err)["error"]["code"] == "invalid_argument"
    assert "unapproved-value" not in captured.err and "replacement-key" not in captured.err


@pytest.mark.parametrize("failure", ["status", "lost_response"])
def test_api_key_issuance_sends_only_one_request(
    failure: str, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        assert request.method == "POST" and request.url.path == "/api-keys"
        if failure == "lost_response":
            raise httpx.ReadTimeout("response was lost", request=request)
        return httpx.Response(503, json={"error": {"message": "temporarily unavailable"}})

    with Qaip(
        api_key="test",
        base_url="https://test.invalid",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    ) as client:

        def fake_client(_: object) -> Qaip:
            return client

        monkeypatch.setattr("qaip.cli._api.api_keys.get_client", fake_client)
        with pytest.warns(DeprecationWarning, match="deprecated"):
            assert invoke("api-keys.create", "--name", "test", "--scopes", "knowledge:read") == 5
    assert len(requests) == 1
    assert json.loads(capsys.readouterr().err)["error"]["retryable"] is False


@pytest.mark.parametrize("command", ["agent.run", "agent.stream_run_events"])
def test_agent_emits_json_from_real_sse_decoder(
    command: str, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    events = [
        {"type": "RUN_STARTED", "runId": "run-test"},
        {"type": "TEXT_MESSAGE_CONTENT", "delta": "日本語の応答"},
        {"type": "RUN_FINISHED", "runId": "run-test"},
    ]
    requests: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request.method)
        if request.method == "POST":
            return httpx.Response(202, json={"run_id": "run-test"})
        assert request.url.path == "/agent/runs/run-test/events/stream"
        content = ": keepalive\n\n" + "".join("data: " + json.dumps(event) + "\n\n" for event in events)
        return httpx.Response(200, headers={"content-type": "text/event-stream"}, content=content)

    with Qaip(
        api_key="test",
        base_url="https://test.invalid",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    ) as client:

        def fake_client(_: object) -> Qaip:
            return client

        monkeypatch.setattr("qaip.cli._api.agent.get_client", fake_client)
        args = ["--messages", '[{"role":"user","content":"hello"}]'] if command == "agent.run" else ["--id", "run-test"]
        assert invoke(command, *args) == 0
    captured = capsys.readouterr()
    assert not captured.err
    assert [json.loads(line) for line in captured.out.splitlines()] == events
    assert requests == (["POST", "GET"] if command == "agent.run" else ["GET"])


@pytest.mark.parametrize("command", ["sources.download_raw", "crawls.download_raw_archive"])
@pytest.mark.parametrize("force", [False, True])
def test_download_checks_overwrite_when_committing_file(
    command: str, force: bool, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    output = tmp_path / "download.bin"

    class Download(httpx.SyncByteStream):
        @override
        def __iter__(self) -> Iterator[bytes]:
            output.write_bytes(b"created-by-another-process")
            yield b"downloaded-bytes"

    def handler(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, headers={"content-type": "application/octet-stream"}, stream=Download())

    with Qaip(
        api_key="test",
        base_url="https://test.invalid",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    ) as client:
        module = "sources" if command.startswith("sources") else "crawls"

        def fake_client(_: object) -> Qaip:
            return client

        monkeypatch.setattr(f"qaip.cli._api.{module}.get_client", fake_client)
        code = invoke(command, "--id", GROUP, "--output", str(output), *(["--force"] if force else []))
    assert code == (0 if force else 4)
    assert output.read_bytes() == (b"downloaded-bytes" if force else b"created-by-another-process")
    assert list(tmp_path.iterdir()) == [output]
    if not force:
        assert json.loads(capsys.readouterr().err)["error"]["code"] == "confirmation_required"


def test_json_file_uses_utf8_under_non_utf8_locale(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    path = tmp_path / "body.json"
    body = {"text_contains": ["削除対象,日本語"]}
    path.write_bytes(json.dumps(body, ensure_ascii=False).encode("utf-8"))
    real_open = builtins.open

    def locale_open(file: Any, *args: Any, **kwargs: Any) -> Any:  # noqa: ANN401
        if file == str(path) and "encoding" not in kwargs:
            kwargs["encoding"] = "latin-1"
        return cast(Any, real_open(file, *args, **kwargs))

    monkeypatch.setattr(builtins, "open", locale_open)
    assert invoke("local-file-groups.start_chunk_deletion", "--id", GROUP, "--json", "@" + str(path), "--dry-run") == 0
    assert json.loads(capsys.readouterr().out)["body"] == body


def test_non_utf8_json_file_is_rejected(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    path = tmp_path / "body.json"
    path.write_bytes(b'{"text_contains":["\xff"]}')
    assert invoke("local-file-groups.start_chunk_deletion", "--id", GROUP, "--json", "@" + str(path), "--dry-run") == 4
    captured = capsys.readouterr()
    assert not captured.out
    assert json.loads(captured.err)["error"]["code"] == "invalid_argument"


def test_json_stdin_uses_utf8_under_non_utf8_locale(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    body = {"text_contains": ["削除対象,日本語"]}
    stdin = io.TextIOWrapper(io.BytesIO(json.dumps(body, ensure_ascii=False).encode("utf-8")), encoding="latin-1")
    monkeypatch.setattr(sys, "stdin", stdin)
    assert invoke("local-file-groups.start_chunk_deletion", "--id", GROUP, "--json", "-", "--dry-run") == 0
    assert json.loads(capsys.readouterr().out)["body"] == body


def test_non_utf8_json_stdin_is_rejected(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setattr(sys, "stdin", io.TextIOWrapper(io.BytesIO(b'{"text_contains":["\xff"]}'), encoding="latin-1"))
    assert invoke("local-file-groups.start_chunk_deletion", "--id", GROUP, "--json", "-", "--dry-run") == 4
    captured = capsys.readouterr()
    assert not captured.out
    assert json.loads(captured.err)["error"]["code"] == "invalid_argument"
