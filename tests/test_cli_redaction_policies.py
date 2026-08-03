from __future__ import annotations

import io
import sys
import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from qaip.cli._api import redaction_policies
from qaip.cli._cli import EXIT_AUTH, EXIT_VALIDATION, main, _build_parser
from qaip.cli._errors import CLIError

POLICY_BODY = {
    "name": "internal-contracts",
    "description": "表示説明",
    "businessConfidential": {
        "definition": "未公開の契約情報",
        "include": [{"text": "契約金額", "mode": "value_clause"}],
        "exclude": [],
        "examples": ["A社との年間契約額は3,200万円"],
    },
}


def _run(argv: list[str]) -> None:
    parser = _build_parser()
    args = parser.parse_args(argv)
    args.func(args)


def test_schema_lists_all_ten_methods(capsys: pytest.CaptureFixture[str]) -> None:
    _run(["schema", "redaction-policies"])

    schema = json.loads(capsys.readouterr().out)

    expected_parameters = {
        "validate": (["name", "business_confidential"], ["description"]),
        "create": (["name", "business_confidential"], ["description"]),
        "list": ([], []),
        "retrieve": (["name"], []),
        "create-version": (["name", "business_confidential"], ["description"]),
        "list-versions": (["name"], ["before_version", "limit"]),
        "retrieve-version": (["name", "version"], []),
        "activate-version": (["name", "version", "expected_active_version"], []),
        "archive": (["name", "expected_active_version"], []),
        "delete-version": (["name", "version"], []),
    }
    assert set(schema["methods"]) == set(expected_parameters)
    for method, (required, optional) in expected_parameters.items():
        assert schema["methods"][method]["required_params"] == required
        assert schema["methods"][method]["optional_params"] == optional


def test_create_dry_run_reads_json_file_and_uses_wire_names(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    path = tmp_path / "policy.json"
    path.write_text(json.dumps(POLICY_BODY, ensure_ascii=False), encoding="utf-8")

    with patch.object(redaction_policies, "get_client") as get_client:
        _run(["api", "redaction-policies.create", "--json", f"@{path}", "--dry-run"])

    output = json.loads(capsys.readouterr().out)
    assert output == {"method": "POST", "path": "/redaction/policies", "body": POLICY_BODY}
    get_client.assert_not_called()


def test_validate_reads_json_from_stdin(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(sys, "stdin", io.StringIO(json.dumps(POLICY_BODY)))

    _run(["api", "redaction-policies.validate", "--json", "-", "--dry-run"])

    output = json.loads(capsys.readouterr().out)
    assert output["path"] == "/redaction/policies/validate"
    assert output["body"] == POLICY_BODY


def test_json_scalars_take_precedence_over_named_flags(capsys: pytest.CaptureFixture[str]) -> None:
    body = {**POLICY_BODY, "name": "json-name", "description": "json-description"}

    _run(
        [
            "api",
            "redaction-policies.create",
            "--json",
            json.dumps(body),
            "--name",
            "flag-name",
            "--description",
            "flag-description",
            "--dry-run",
        ]
    )

    output = json.loads(capsys.readouterr().out)
    assert output["body"]["name"] == "json-name"
    assert output["body"]["description"] == "json-description"


@pytest.mark.parametrize(
    ("argv", "method", "path", "body"),
    [
        (
            ["redaction-policies.create", "--json", json.dumps(POLICY_BODY)],
            "POST",
            "/redaction/policies",
            POLICY_BODY,
        ),
        (
            [
                "redaction-policies.create-version",
                "--name",
                "internal-contracts",
                "--json",
                json.dumps({key: value for key, value in POLICY_BODY.items() if key != "name"}),
            ],
            "POST",
            "/redaction/policies/internal-contracts/versions",
            {key: value for key, value in POLICY_BODY.items() if key != "name"},
        ),
        (
            [
                "redaction-policies.activate-version",
                "--name",
                "internal-contracts",
                "--version",
                "1",
                "--json",
                '{"expectedActiveVersion":null}',
            ],
            "POST",
            "/redaction/policies/internal-contracts/versions/1/activate",
            {"expectedActiveVersion": None},
        ),
        (
            [
                "redaction-policies.archive",
                "--name",
                "internal-contracts",
                "--expected-active-version",
                "1",
            ],
            "POST",
            "/redaction/policies/internal-contracts/archive",
            {"expectedActiveVersion": "1"},
        ),
        (
            ["redaction-policies.delete-version", "--name", "internal-contracts", "--version", "1"],
            "DELETE",
            "/redaction/policies/internal-contracts/versions/1",
            None,
        ),
    ],
)
def test_all_mutations_have_network_free_dry_run(
    argv: list[str],
    method: str,
    path: str,
    body: dict[str, object] | None,
    capsys: pytest.CaptureFixture[str],
) -> None:
    with patch.object(redaction_policies, "get_client") as get_client:
        _run(["api", *argv, "--dry-run"])

    output = json.loads(capsys.readouterr().out)
    assert output["method"] == method
    assert output["path"] == path
    assert output.get("body") == body
    get_client.assert_not_called()


@pytest.mark.parametrize(
    "argv",
    [
        [
            "redaction-policies.activate-version",
            "--name",
            "internal-contracts",
            "--version",
            "1",
            "--expected-active-version",
            "null",
        ],
        ["redaction-policies.archive", "--name", "internal-contracts", "--expected-active-version", "1"],
        ["redaction-policies.delete-version", "--name", "internal-contracts", "--version", "1"],
    ],
)
def test_lifecycle_mutations_require_yes(argv: list[str]) -> None:
    with patch.object(redaction_policies, "get_client") as get_client:
        with pytest.raises(CLIError) as caught:
            _run(["api", *argv])

    assert caught.value.code == "confirmation_required"
    get_client.assert_not_called()


def test_yes_allows_activate_and_preserves_explicit_null(capsys: pytest.CaptureFixture[str]) -> None:
    client = MagicMock()
    client.redaction_policies.activate_version.return_value.model_dump.return_value = {"version": "1"}

    with patch.object(redaction_policies, "get_client", return_value=client):
        _run(
            [
                "api",
                "redaction-policies.activate-version",
                "--name",
                "internal-contracts",
                "--version",
                "1",
                "--expected-active-version",
                "null",
                "--yes",
            ]
        )

    client.redaction_policies.activate_version.assert_called_once_with(
        "internal-contracts",
        "1",
        expected_active_version=None,
    )
    assert json.loads(capsys.readouterr().out) == {"version": "1"}


def test_list_versions_dry_run_validates_cursor_and_limit(capsys: pytest.CaptureFixture[str]) -> None:
    _run(
        [
            "api",
            "redaction-policies.list-versions",
            "--name",
            "internal-contracts",
            "--limit",
            "50",
            "--before-version",
            "52",
            "--dry-run",
        ]
    )
    output = json.loads(capsys.readouterr().out)
    assert output["body"] == {"limit": 50, "beforeVersion": "52"}

    with pytest.raises(CLIError, match="--limit"):
        _run(
            [
                "api",
                "redaction-policies.list-versions",
                "--name",
                "internal-contracts",
                "--limit",
                "101",
                "--dry-run",
            ]
        )


def test_list_and_retrieve_fields_filter_the_response_wrapper(
    capsys: pytest.CaptureFixture[str],
) -> None:
    client = MagicMock()
    client.redaction_policies.list.return_value.model_dump.return_value = {
        "policies": [{"name": "internal-contracts", "source": "TENANT"}],
        "ignored": "value",
    }
    client.redaction_policies.retrieve.return_value.model_dump.return_value = {
        "name": "internal-contracts",
        "source": "TENANT",
        "description": "表示説明",
    }

    with patch.object(redaction_policies, "get_client", return_value=client):
        _run(["api", "redaction-policies.list", "--fields", "policies"])
        listed = json.loads(capsys.readouterr().out)
        _run(
            [
                "api",
                "redaction-policies.retrieve",
                "--name",
                "internal-contracts",
                "--fields",
                "name,source",
            ]
        )
        retrieved = json.loads(capsys.readouterr().out)

    assert listed == {"policies": [{"name": "internal-contracts", "source": "TENANT"}]}
    assert retrieved == {"name": "internal-contracts", "source": "TENANT"}


def test_confirmation_error_is_structured_and_exits_four(capsys: pytest.CaptureFixture[str]) -> None:
    argv = [
        "qaip",
        "--error-format",
        "json",
        "api",
        "redaction-policies.activate-version",
        "--name",
        "internal-contracts",
        "--version",
        "1",
        "--expected-active-version",
        "null",
    ]

    with patch.object(redaction_policies, "get_client") as get_client, patch("sys.argv", argv):
        assert main() == EXIT_VALIDATION

    payload = json.loads(capsys.readouterr().err)
    assert payload["error"]["code"] == "confirmation_required"
    assert payload["error"]["retryable"] is False
    get_client.assert_not_called()


def test_unknown_body_field_is_rejected_before_network() -> None:
    body = {**POLICY_BODY, "enabledCategories": ["B"]}
    with patch.object(redaction_policies, "get_client") as get_client:
        with pytest.raises(CLIError) as caught:
            _run(["api", "redaction-policies.create", "--json", json.dumps(body), "--dry-run"])

    assert caught.value.code == "invalid_argument"
    get_client.assert_not_called()


def test_actual_call_without_credentials_exits_three(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("QAIP_API_KEY", raising=False)
    with patch("sys.argv", ["qaip", "api", "redaction-policies.list"]):
        assert main() == EXIT_AUTH
