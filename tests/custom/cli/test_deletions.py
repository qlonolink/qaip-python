from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import httpx
import pytest

from qaip import Qaip
from qaip.cli._cli import main, _build_parser

GROUP = "00000000-0000-4000-8000-000000000001"
JOB = "00000000-0000-4000-8000-000000000002"


def invoke(*args: str) -> int:
    with patch("sys.argv", ["qaip", "--error-format", "json", *args]):
        return main()


def test_schema_contains_all_deletion_methods(capsys: pytest.CaptureFixture[str]) -> None:
    assert invoke("schema", "local-file-groups") == 0
    methods = json.loads(capsys.readouterr().out)["methods"]
    assert methods["start_bulk_deletion"]["required_params"] == ["source_group_ids"]
    assert methods["start_chunk_deletion"]["required_params"] == ["id", "text_contains"]
    assert methods["retrieve_bulk_deletion"]["optional_params"] == ["after"]
    assert methods["retrieve_chunk_deletion"]["required_params"] == ["id", "chunk_deletion_id"]


@pytest.mark.parametrize(
    ("args", "method", "path", "body", "response"),
    [
        (
            ["start_bulk_deletion", "--source-group-id", GROUP, "--yes"],
            "POST",
            "/local-file-groups/bulk-deletions",
            {"source_group_ids": [GROUP]},
            {"id": JOB, "accepted_count": 1, "rejected": []},
        ),
        (
            ["start_chunk_deletion", "--id", GROUP, "--text-contains", "a,b", "--text-contains", "日本語", "--yes"],
            "POST",
            f"/local-file-groups/{GROUP}/chunk-deletions",
            {"text_contains": ["a,b", "日本語"]},
            {"id": JOB, "source_group_id": GROUP},
        ),
        (
            ["retrieve_chunk_deletion", "--id", GROUP, "--chunk-deletion-id", JOB],
            "GET",
            f"/local-file-groups/{GROUP}/chunk-deletions/{JOB}",
            None,
            {"id": JOB, "source_group_id": GROUP, "deleted_count": 1, "status": "success", "text_contains": ["test"]},
        ),
        (
            ["retrieve_bulk_deletion", "--bulk-deletion-id", JOB, "--after", GROUP],
            "GET",
            f"/local-file-groups/bulk-deletions/{JOB}",
            None,
            {
                "id": JOB,
                "deleted_count": 1,
                "total_count": 1,
                "status": "success",
                "remaining_source_group_ids": [],
                "remaining_truncated": False,
            },
        ),
    ],
)
def test_requests_match_dry_run(
    args: list[str],
    method: str,
    path: str,
    body: object,
    response: dict[str, object],
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    command = f"local-file-groups.{args[0]}"
    assert invoke("api", command, *args[1:], "--dry-run") == 0
    dry = json.loads(capsys.readouterr().out)
    assert dry["method"] == method
    assert dry["path"] == path
    assert dry.get("body") == body
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        assert request.method == method
        assert request.url.path == "/api/v1" + path
        assert (json.loads(request.content) if request.content else None) == body
        assert dict(request.url.params) == dry.get("query", {})
        return httpx.Response(200, json=response)

    with Qaip(
        api_key="test",
        base_url="https://test.invalid/api/v1",
        _strict_response_validation=True,
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    ) as client:

        def fake_get_client(_: object) -> Qaip:
            return client

        monkeypatch.setattr("qaip.cli._api.local_file_groups.get_client", fake_get_client)
        assert invoke("api", command, *args[1:]) == 0
    actual = json.loads(capsys.readouterr().out)
    for key, value in response.items():
        assert actual[key] == value
    assert len(seen) == 1


@pytest.mark.parametrize(
    "args",
    [
        ["start_bulk_deletion", "--source-group-id", GROUP],
        ["start_chunk_deletion", "--id", GROUP, "--text-contains", "test"],
    ],
)
def test_deletion_requires_yes_before_creating_client(args: list[str], capsys: pytest.CaptureFixture[str]) -> None:
    with patch("qaip.cli._api.local_file_groups.get_client") as client:
        assert invoke("api", f"local-file-groups.{args[0]}", *args[1:]) == 4
        client.assert_not_called()
    assert json.loads(capsys.readouterr().err)["error"]["code"] == "confirmation_required"


@pytest.mark.parametrize(
    ("method", "body"),
    [
        ("start_bulk_deletion", {"source_group_ids": []}),
        ("start_bulk_deletion", {"source_group_ids": "all"}),
        ("start_bulk_deletion", {"source_group_ids": [None]}),
        ("start_bulk_deletion", {"source_group_ids": [GROUP], "extra_body": {"source_group_ids": [JOB]}}),
        ("start_chunk_deletion", {"text_contains": []}),
        ("start_chunk_deletion", {"text_contains": [""]}),
        ("start_chunk_deletion", {"text_contains": [False]}),
        ("start_chunk_deletion", {"text_contains": ["test"], "extra_headers": {"X-API-Key": "other"}}),
    ],
)
def test_invalid_json_rejected_in_dry_run(method: str, body: object, capsys: pytest.CaptureFixture[str]) -> None:
    extra = ["--id", GROUP] if method == "start_chunk_deletion" else []
    assert invoke("api", f"local-file-groups.{method}", *extra, "--json", json.dumps(body), "--dry-run") == 4
    assert json.loads(capsys.readouterr().err)["error"]["code"] == "invalid_argument"


@pytest.mark.parametrize("method", ["start_bulk_deletion", "start_chunk_deletion"])
def test_json_file_and_stdin_override_named_flags(
    method: str,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import io

    key = "source_group_ids" if method == "start_bulk_deletion" else "text_contains"
    flag = "--source-group-id" if method == "start_bulk_deletion" else "--text-contains"
    extra = [] if method == "start_bulk_deletion" else ["--id", GROUP]
    body = {key: [GROUP]}
    payload = tmp_path / "request.json"
    payload.write_text(json.dumps(body))
    for source in [f"@{payload}", "-"]:
        monkeypatch.setattr("sys.stdin", io.StringIO(json.dumps(body)))
        assert invoke("api", f"local-file-groups.{method}", *extra, flag, "ignored", "--json", source, "--dry-run") == 0
        assert json.loads(capsys.readouterr().out)["body"] == body


@pytest.mark.parametrize(
    "args",
    [
        ["start_bulk_deletion", "--source-group-id", "../other", "--yes"],
        ["start_chunk_deletion", "--id", "../other", "--text-contains", "test", "--yes"],
        ["retrieve_chunk_deletion", "--id", GROUP, "--chunk-deletion-id", "../other"],
        ["retrieve_bulk_deletion", "--bulk-deletion-id", JOB, "--after", "../other"],
    ],
)
def test_invalid_ids_cannot_make_requests(args: list[str], capsys: pytest.CaptureFixture[str]) -> None:
    with patch("qaip.cli._api.local_file_groups.get_client") as client:
        assert invoke("api", f"local-file-groups.{args[0]}", *args[1:]) == 4
        client.assert_not_called()
    assert json.loads(capsys.readouterr().err)["error"]["code"] == "invalid_id"


def test_start_does_not_retry_or_poll(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(500, json={"message": "unavailable"})

    with Qaip(api_key="test", http_client=httpx.Client(transport=httpx.MockTransport(handler))) as client:

        def fake_get_client(_: object) -> Qaip:
            return client

        monkeypatch.setattr("qaip.cli._api.local_file_groups.get_client", fake_get_client)
        assert invoke("api", "local-file-groups.start_bulk_deletion", "--source-group-id", GROUP, "--yes") == 5
    assert len(seen) == 1
    capsys.readouterr()


def test_no_json_for_job_retrieval() -> None:
    with pytest.raises(SystemExit) as exc:
        _build_parser().parse_args(
            ["api", "local-file-groups.retrieve_bulk_deletion", "--bulk-deletion-id", JOB, "--json", "{}"]
        )
    assert exc.value.code == 2


def test_all_rejected_returns_without_polling(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        assert request.method == "POST"
        return httpx.Response(
            200, json={"accepted_count": 0, "rejected": [{"source_group_id": GROUP, "reason": "not_found"}]}
        )

    with Qaip(
        api_key="test",
        _strict_response_validation=True,
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    ) as client:

        def fake_get_client(_: object) -> Qaip:
            return client

        monkeypatch.setattr("qaip.cli._api.local_file_groups.get_client", fake_get_client)
        assert invoke("api", "local-file-groups.start_bulk_deletion", "--source-group-id", GROUP, "--yes") == 0
    result = json.loads(capsys.readouterr().out)
    assert result["accepted_count"] == 0
    assert result["id"] is None
    assert result["rejected"] == [{"source_group_id": GROUP, "reason": "not_found"}]
    assert len(seen) == 1


def test_conversation_deletion_returns_json_null(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "DELETE"
        return httpx.Response(204)

    with Qaip(api_key="test", http_client=httpx.Client(transport=httpx.MockTransport(handler))) as client:

        def fake_get_client(_: object) -> Qaip:
            return client

        monkeypatch.setattr("qaip.cli._api.conversations.get_client", fake_get_client)
        assert invoke("api", "conversations.delete", "--id", "conversation-1", "--yes") == 0
    assert json.loads(capsys.readouterr().out) is None
