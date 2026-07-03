from __future__ import annotations

import json
from unittest.mock import patch

import httpx
import pytest

from qaip import Qaip
from qaip.cli._cli import main, _build_parser
from qaip.cli._errors import CLIError
from qaip.cli._api._common import filter_fields


class TestParserBuild:
    def test_build_parser(self) -> None:
        parser = _build_parser()
        assert parser is not None
        assert parser.prog == "qaip"

    def test_version(self) -> None:
        parser = _build_parser()
        with pytest.raises(SystemExit) as exc_info:
            parser.parse_args(["--version"])
        assert exc_info.value.code == 0

    def test_no_subcommand_prints_help_without_error(self, capsys: pytest.CaptureFixture[str]) -> None:
        # サブコマンド未指定時のデフォルトハンドラが TypeError を起こさず
        # ヘルプを表示すること。
        with patch("sys.argv", ["qaip"]):
            rc = main()
        assert rc == 0
        captured = capsys.readouterr()
        assert "usage:" in captured.out


class TestSchemaCommand:
    def test_schema_list_all(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(["schema"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert "sources" in data
        assert "crawls" in data
        assert "agent" in data
        assert "completion" in data
        assert "search" in data

    def test_schema_specific_resource(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(["schema", "sources"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert "description" in data
        assert "methods" in data
        assert "retrieve" in data["methods"]
        assert "list" in data["methods"]

    def test_schema_unknown_resource(self) -> None:
        parser = _build_parser()
        args = parser.parse_args(["schema", "nonexistent"])
        with pytest.raises(CLIError) as exc_info:
            args.func(args)
        assert exc_info.value.code == "invalid_argument"


class TestDryRun:
    def test_search_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "search.create", "--query", "test", "--dry-run"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "POST"
        assert data["path"] == "/search"
        assert data["body"]["query"] == "test"

    def test_completion_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        messages = json.dumps([{"role": "user", "content": "hello"}])
        args = parser.parse_args(["api", "completion.create", "--messages", messages, "--dry-run"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "POST"
        assert data["path"] == "/completions"
        assert data["body"]["messages"][0]["content"] == "hello"

    def test_content_retrieve_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "content.retrieve", "--id", "abc123", "--dry-run"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "GET"
        assert data["path"] == "/contents/abc123"

    def test_tags_list_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "tags.list", "--dry-run"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "GET"
        assert data["path"] == "/tags"

    def test_tags_create_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "tags.create",
            "--name", "important",
            "--description", "重要タグ",
            "--dry-run",
        ])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "POST"
        assert data["path"] == "/tags"
        assert data["body"] == {"name": "important", "description": "重要タグ"}

    def test_tags_update_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "tags.update",
            "--id", "tag-1",
            "--name", "renamed",
            "--dry-run",
        ])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "PUT"
        assert data["path"] == "/tags/tag-1"
        assert data["body"] == {"name": "renamed"}

    def test_tags_delete_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "tags.delete", "--id", "tag-1", "--dry-run"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "DELETE"
        assert data["path"] == "/tags/tag-1"

    def test_sources_retrieve_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "sources.retrieve", "--id", "src-1", "--dry-run"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "GET"
        assert data["path"] == "/sources/src-1"

    def test_sources_list_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "sources.list", "--limit", "10", "--dry-run"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "GET"
        assert data["body"]["limit"] == 10

    def test_source_groups_list_with_source_type(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "source-groups.list",
                "--limit",
                "5",
                "--source-type",
                "crawl",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "GET"
        assert data["path"] == "/source-groups"
        assert data["body"]["source_type"] == "crawl"

    def test_secrets_create_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "secrets.create",
                "--name",
                "my-secret",
                "--secret",
                "val",
                "--type",
                "github_pat",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "POST"
        assert data["path"] == "/secrets"
        assert data["body"]["name"] == "my-secret"

    def test_secrets_delete_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "secrets.delete", "--id", "sec-1", "--dry-run"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "DELETE"
        assert data["path"] == "/secrets/sec-1"

    def test_crawls_create_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "crawls.create",
                "--name",
                "test-crawl",
                "--start-url",
                "https://example.com",
                "--max-depth",
                "3",
                "--max-num-files",
                "100",
                "--file-extensions",
                ".pdf,.docx",
                "--rrule",
                "FREQ=DAILY",
                "--html-only",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "POST"
        assert data["path"] == "/crawls"
        assert data["body"]["start_url"] == "https://example.com"
        assert data["body"]["max_depth"] == 3
        assert data["body"]["file_extensions"] == [".pdf", ".docx"]
        assert data["body"]["rrule"] == "FREQ=DAILY"
        assert data["body"]["html_only"] is True

    def test_crawls_create_url_list_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "crawls.create_url_list",
                "--name",
                "url-list",
                "--urls",
                "https://a.example.com,https://b.example.com",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "POST"
        assert data["path"] == "/crawl-url-lists"
        assert data["body"]["name"] == "url-list"
        assert data["body"]["target_urls"] == ["https://a.example.com", "https://b.example.com"]

    def test_agent_run_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        messages = json.dumps([{"role": "user", "content": "hi"}])
        args = parser.parse_args(
            [
                "api",
                "agent.run",
                "--messages",
                messages,
                "--run-id",
                "run-x",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "POST"
        assert data["path"] == "/agent/run"
        assert data["body"]["messages"][0]["content"] == "hi"
        assert data["body"]["run_id"] == "run-x"

    def test_agent_create_run_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        messages = json.dumps([{"role": "user", "content": "hi"}])
        args = parser.parse_args(
            [
                "api",
                "agent.create_run",
                "--messages",
                messages,
                "--thread-id",
                "t-1",
                "--idempotency-key",
                "abc",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "POST"
        assert data["path"] == "/agent/runs"
        assert data["body"]["input"]["messages"][0]["content"] == "hi"
        assert data["body"]["input"]["thread_id"] == "t-1"
        assert data["body"]["idempotency_key"] == "abc"

    def test_agent_retrieve_run_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "agent.retrieve_run", "--id", "run-1", "--dry-run"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "GET"
        assert data["path"] == "/agent/runs/run-1"

    def test_agent_list_run_events_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "agent.list_run_events",
                "--id",
                "run-1",
                "--limit",
                "5",
                "--after",
                "42",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "GET"
        assert data["path"] == "/agent/runs/run-1/events"
        assert data["body"]["limit"] == 5
        assert data["body"]["after"] == 42

    def test_githubs_create_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "githubs.create",
                "--name",
                "gh-1",
                "--repository",
                "octocat/Hello-World",
                "--reference",
                "main",
                "--reference-type",
                "branch",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "POST"
        assert data["path"] == "/githubs"
        assert data["body"]["repository"] == "octocat/Hello-World"
        assert data["body"]["reference_param"] == "main"
        assert data["body"]["reference_type"] == "branch"

    def test_google_drives_create_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "google-drives.create",
                "--name",
                "gd-1",
                "--folder-url",
                "https://drive.google.com/drive/folders/abc",
                "--secret-id",
                "sec-1",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "POST"
        assert data["path"] == "/google-drives"
        assert data["body"]["folder_url"] == "https://drive.google.com/drive/folders/abc"
        assert data["body"]["secret_id"] == "sec-1"

    def test_notions_create_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "notions.create",
                "--name",
                "notion-1",
                "--page-id",
                "22cf90c7c8aa80098050fa40c6ebab1e",
                "--notion-token",
                "secret_xxx",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "POST"
        assert data["path"] == "/notions"
        assert data["body"]["page_id"] == "22cf90c7c8aa80098050fa40c6ebab1e"
        # notion_token は dry-run 出力でマスクされる。
        assert data["body"]["notion_token"] == "***"

    def test_google_drives_list_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "google-drives.list", "--dry-run"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "GET"
        assert data["path"] == "/google-drives"

    def test_githubs_list_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "githubs.list", "--dry-run"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "GET"
        assert data["path"] == "/githubs"

    def test_notions_list_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "notions.list", "--dry-run"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "GET"
        assert data["path"] == "/notions"

    def test_local_file_groups_list_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "local-file-groups.list", "--dry-run"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "GET"
        assert data["path"] == "/local-file-groups"

    def test_local_file_groups_create_dry_run(
        self, capsys: pytest.CaptureFixture[str], tmp_path: pytest.TempPathFactory
    ) -> None:
        from pathlib import Path

        assert isinstance(tmp_path, Path)
        f1 = tmp_path / "a.txt"
        f1.write_text("hello")
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "local-file-groups.create",
                "--name",
                "lfg",
                "--file",
                str(f1),
                "--last-modified",
                "1775000000000",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "POST"
        assert data["path"] == "/local-file-groups"
        assert data["body"]["files"] == ["a.txt"]
        assert data["body"]["last_modified"] == [1775000000000]

    def test_tag_source_groups_create_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "tag-source-groups.create",
                "--tag-id",
                "tag-1",
                "--source-group-id",
                "sg-1",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "POST"
        assert data["path"] == "/tag-source-groups"
        assert data["body"]["tag_id"] == "tag-1"


class TestJsonInput:
    def test_json_body_direct(self, capsys: pytest.CaptureFixture[str]) -> None:
        body = json.dumps({"query": "from json", "limit": 5})
        parser = _build_parser()
        args = parser.parse_args(["api", "search.create", "--json", body, "--dry-run"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["body"]["query"] == "from json"
        assert data["body"]["limit"] == 5

    def test_json_body_overrides_flags(self, capsys: pytest.CaptureFixture[str]) -> None:
        body = json.dumps({"query": "from json"})
        parser = _build_parser()
        args = parser.parse_args(["api", "search.create", "--json", body, "--query", "from flag", "--dry-run"])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        # --json 内の値が優先される
        assert data["body"]["query"] == "from json"


class TestFilterFields:
    def test_filter_fields(self) -> None:
        data = {"id": "1", "name": "test", "status": "active", "extra": "val"}
        result = filter_fields(data, "id,name")
        assert result == {"id": "1", "name": "test"}

    def test_filter_fields_none(self) -> None:
        data = {"id": "1", "name": "test"}
        result = filter_fields(data, None)
        assert result == data


class TestValidation:
    def test_missing_required_field(self) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "search.create", "--dry-run"])
        with pytest.raises(CLIError, match="--query"):
            args.func(args)

    def test_secrets_create_missing_fields(self) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "secrets.create", "--name", "test", "--dry-run"])
        with pytest.raises(CLIError, match="--secret"):
            args.func(args)

    def test_invalid_json_body(self) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "search.create", "--json", "not-json", "--dry-run"])
        with pytest.raises(CLIError, match="Invalid JSON"):
            args.func(args)

    def test_githubs_create_missing_repository(self) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "githubs.create", "--name", "gh", "--dry-run"])
        with pytest.raises(CLIError, match="--repository"):
            args.func(args)

    def test_notions_create_missing_page_id(self) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "notions.create", "--name", "n", "--dry-run"])
        with pytest.raises(CLIError, match="--page-id"):
            args.func(args)

    def test_google_drives_create_missing_folder_url(self) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "google-drives.create", "--name", "gd", "--dry-run"])
        with pytest.raises(CLIError, match="--folder-url"):
            args.func(args)

    def test_crawls_create_url_list_missing_urls(self) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "crawls.create_url_list", "--name", "x", "--dry-run"])
        with pytest.raises(CLIError, match="--urls"):
            args.func(args)

    def test_tags_create_missing_name(self) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "tags.create", "--description", "d", "--dry-run"])
        with pytest.raises(CLIError, match="--name"):
            args.func(args)

    def test_tags_update_requires_a_field(self) -> None:
        parser = _build_parser()
        args = parser.parse_args(["api", "tags.update", "--id", "tag-1", "--dry-run"])
        with pytest.raises(CLIError, match="at least one"):
            args.func(args)


class TestSensitiveMasking:
    def test_secrets_create_dry_run_masks_secret(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "secrets.create",
                "--name",
                "s",
                "--secret",
                "SHOULD_NOT_APPEAR",
                "--type",
                "github_pat",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        assert "SHOULD_NOT_APPEAR" not in captured.out
        data = json.loads(captured.out)
        assert data["body"]["secret"] == "***"

    def test_secrets_update_dry_run_masks_secret(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "secrets.update",
                "--id",
                "sec-1",
                "--name",
                "s",
                "--json",
                json.dumps({"secret": "ROT_SHOULD_NOT_APPEAR"}),
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        assert "ROT_SHOULD_NOT_APPEAR" not in captured.out
        data = json.loads(captured.out)
        assert data["body"]["secret"] == "***"

    def test_githubs_create_dry_run_masks_token(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "githubs.create",
                "--name",
                "g",
                "--repository",
                "o/r",
                "--github-token",
                "GHP_SHOULD_NOT_APPEAR",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        assert "GHP_SHOULD_NOT_APPEAR" not in captured.out
        data = json.loads(captured.out)
        assert data["body"]["github_token"] == "***"

    def test_google_drives_create_dry_run_masks_service_account_key(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "google-drives.create",
                "--name",
                "gd",
                "--folder-url",
                "https://drive.google.com/drive/folders/x",
                "--service-account-key",
                "KEY_SHOULD_NOT_APPEAR",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        assert "KEY_SHOULD_NOT_APPEAR" not in captured.out
        data = json.loads(captured.out)
        assert data["body"]["service_account_key"] == "***"


class TestClientCredentials:
    """CLI 引数の --api-key / --base-url が Qaip() に渡ることを確認する。"""

    def test_get_client_uses_cli_args(self) -> None:
        from argparse import Namespace
        from unittest.mock import patch as _patch

        from qaip.cli._utils import get_client

        with _patch("qaip.cli._utils.qaip.Qaip") as mock_qaip:
            get_client(Namespace(api_key="AK", base_url="https://example.com"))
            mock_qaip.assert_called_once_with(api_key="AK", base_url="https://example.com")

    def test_get_client_uses_env_api_key(self, monkeypatch: pytest.MonkeyPatch) -> None:
        from unittest.mock import patch as _patch

        from qaip.cli._utils import get_client

        monkeypatch.setenv("QAIP_API_KEY", "env-key")
        with _patch("qaip.cli._utils.qaip.Qaip") as mock_qaip:
            get_client()
            mock_qaip.assert_called_once_with()

    def test_get_client_missing_credentials_raises(self, monkeypatch: pytest.MonkeyPatch) -> None:
        from qaip.cli._utils import get_client

        monkeypatch.delenv("QAIP_API_KEY", raising=False)
        with pytest.raises(CLIError) as exc_info:
            get_client()
        assert exc_info.value.code == "missing_credentials"


class TestHeaderOption:
    """グローバル -H/--header が default_headers として全リクエストに乗ることを確認する。"""

    def test_get_client_passes_default_headers(self) -> None:
        from argparse import Namespace
        from unittest.mock import patch as _patch

        from qaip.cli._utils import get_client

        with _patch("qaip.cli._utils.qaip.Qaip") as mock_qaip:
            get_client(
                Namespace(
                    api_key="AK",
                    base_url=None,
                    headers=["X-Request-Id: req-123", "X-Foo:bar"],
                )
            )
            mock_qaip.assert_called_once_with(
                api_key="AK",
                default_headers={"X-Request-Id": "req-123", "X-Foo": "bar"},
            )

    def test_get_client_no_headers_omits_default_headers(self) -> None:
        from argparse import Namespace
        from unittest.mock import patch as _patch

        from qaip.cli._utils import get_client

        with _patch("qaip.cli._utils.qaip.Qaip") as mock_qaip:
            get_client(Namespace(api_key="AK", base_url=None, headers=None))
            mock_qaip.assert_called_once_with(api_key="AK")

    def test_parse_headers_invalid_raises(self) -> None:
        from qaip.cli._utils import parse_headers

        with pytest.raises(CLIError) as exc_info:
            parse_headers(["NoColonHere"])
        assert exc_info.value.code == "invalid_argument"
        assert "NoColonHere" not in str(exc_info.value)

        with pytest.raises(CLIError) as exc_info:
            parse_headers([": SECRET_SHOULD_NOT_APPEAR"])
        assert exc_info.value.code == "invalid_argument"
        assert "SECRET_SHOULD_NOT_APPEAR" not in str(exc_info.value)

    @pytest.mark.parametrize(
        "header",
        [
            "X-Api-Key: SECRET_SHOULD_NOT_APPEAR",
            "Authorization: SECRET_SHOULD_NOT_APPEAR",
            "Content-Type: application/json",
            "Host: example.com",
            "X-Stainless-Raw-Response: raw",
        ],
    )
    def test_parse_headers_rejects_managed_headers(self, header: str) -> None:
        from qaip.cli._utils import parse_headers

        with pytest.raises(CLIError) as exc_info:
            parse_headers([header])
        assert exc_info.value.code == "invalid_argument"
        assert "SECRET_SHOULD_NOT_APPEAR" not in str(exc_info.value)

    @pytest.mark.parametrize(
        "header",
        [
            "Bad Header: value",
            "X-Test: \nok",
            "X-Test: ok\nbad",
            "X-Test: ok\rbad",
            "X-Test: ok\r",
            "X-Test: ok\x7fbad",
            "X-Test: ok\x7f",
            "X-Test: あ",
        ],
    )
    def test_parse_headers_rejects_invalid_name_or_value(self, header: str) -> None:
        from qaip.cli._utils import parse_headers

        with pytest.raises(CLIError) as exc_info:
            parse_headers([header])
        assert exc_info.value.code == "invalid_argument"

    def test_header_reaches_request(self) -> None:
        # -H で渡したヘッダーが実際の HTTP リクエストに乗ることを MockTransport で確認する。
        seen: dict[str, str] = {}

        def handler(request: httpx.Request) -> httpx.Response:
            seen.update(request.headers)
            return httpx.Response(
                200,
                json={
                    "id": _VALID_UUID,
                    "name": "t",
                    "start_url": "https://example.com/",
                    "status": 0,
                },
            )

        transport = httpx.MockTransport(handler)
        client = Qaip(api_key="test-key", http_client=httpx.Client(transport=transport))
        # CLI 引数の -H が default_headers→クライアントへ流れる経路を模し、
        # with_options で同じ default_headers を適用する。
        client = client.with_options(default_headers={"X-Request-Id": "req-123"})

        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "crawls.create",
                "--name",
                "t",
                "--start-url",
                "https://example.com/",
                "--max-depth",
                "1",
                "--max-num-files",
                "1",
            ]
        )
        with patch("qaip.cli._api.crawls.get_client", return_value=client):
            args.func(args)

        assert seen.get("x-request-id") == "req-123"
        assert seen.get("x-api-key") == "test-key"


class TestInvalidJsonArgs:
    def test_completion_invalid_messages_json(self) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "completion.create",
                "--messages",
                "not-json",
                "--dry-run",
            ]
        )
        with pytest.raises(CLIError, match="Invalid JSON for --messages"):
            args.func(args)

    def test_extract_invalid_schema_json(self) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "extract.create",
                "--schema",
                "not-json",
                "--dry-run",
            ]
        )
        with pytest.raises(CLIError, match="Invalid JSON for --schema"):
            args.func(args)

    def test_agent_run_invalid_forwarded_props_json(self) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "agent.run",
                "--forwarded-props",
                "not-json",
                "--dry-run",
            ]
        )
        with pytest.raises(CLIError, match="Invalid JSON for --forwarded-props"):
            args.func(args)


class TestSecretsListDryRunKeyName:
    def test_secrets_list_dry_run_uses_secret_type_key(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "secrets.list",
                "--type",
                "github",
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        # SDK とスキーマに合わせて secret_type キーで出力される
        assert data["body"]["secret_type"] == "github"
        assert "type" not in data["body"]


class TestLocalFileGroupsMissingFile:
    def test_missing_file_raises_cli_error(self) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "local-file-groups.create",
                "--name",
                "lfg",
                "--file",
                "/nonexistent/path/does-not-exist.txt",
                "--dry-run",
            ]
        )
        with pytest.raises(CLIError, match="File not found"):
            args.func(args)

    def test_create_sends_file_as_files_multipart_field(
        self,
        capsys: pytest.CaptureFixture[str],
        tmp_path: pytest.TempPathFactory,
    ) -> None:
        from pathlib import Path

        assert isinstance(tmp_path, Path)
        file_path = tmp_path / "etl.md"
        file_path.write_text("hello")
        captured_bodies: list[bytes] = []

        def handler(request: httpx.Request) -> httpx.Response:
            captured_bodies.append(request.read())
            return httpx.Response(200, json={"source_group_id": "019ede24-8c8a-7b95-a5c6-36fff2574cbe"})

        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "local-file-groups.create",
                "--name",
                "lfg",
                "--file",
                str(file_path),
                "--last-modified",
                "1000",
            ]
        )

        transport = httpx.MockTransport(handler)
        with Qaip(
            base_url="http://test.local",
            api_key="test-key",
            http_client=httpx.Client(transport=transport),
        ) as client:
            with patch("qaip.cli._api.local_file_groups.get_client", return_value=client):
                args.func(args)

        captured = capsys.readouterr()
        assert json.loads(captured.out) == {"source_group_id": "019ede24-8c8a-7b95-a5c6-36fff2574cbe"}
        assert len(captured_bodies) == 1
        body = captured_bodies[0]
        assert b'name="files[]"' not in body
        assert b'name="files"; filename="etl.md"' in body
        assert b'name="last_modified[]"' not in body
        assert b'name="last_modified"\r\n\r\n1000' in body


_VALID_UUID = "11111111-1111-1111-1111-111111111111"


class TestMainTypeErrorHandling:
    def test_main_converts_unexpected_kwarg_typeerror(
        self, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """SDK 呼び出しで unexpected keyword argument の TypeError が発生した場合、
        スタックトレースではなくユーザー向けエラーに変換される。
        """
        from unittest.mock import MagicMock, patch as _patch

        monkeypatch.setenv("QAIP_API_KEY", "fake")
        mock_client = MagicMock()
        mock_client.content.side_effect = TypeError("content() got an unexpected keyword argument 'foo'")
        with _patch("qaip.cli._utils.qaip.Qaip", return_value=mock_client):
            with patch("sys.argv", ["qaip", "api", "content.retrieve", "--id", _VALID_UUID]):
                rc = main()
        # invalid_argument は validation エラーとして exit code 4 を返す
        assert rc == 4
        captured = capsys.readouterr()
        assert "Invalid argument" in captured.err

    def test_main_reraises_unrelated_typeerror(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """SDK 呼び出し起因ではない TypeError は握り潰さない。"""
        from unittest.mock import MagicMock, patch as _patch

        monkeypatch.setenv("QAIP_API_KEY", "fake")
        mock_client = MagicMock()
        mock_client.content.side_effect = TypeError("not an sdk arg error")
        with _patch("qaip.cli._utils.qaip.Qaip", return_value=mock_client):
            with patch("sys.argv", ["qaip", "api", "content.retrieve", "--id", _VALID_UUID]):
                with pytest.raises(TypeError, match="not an sdk arg error"):
                    main()


class TestSecretsUpdateValidation:
    def test_secrets_update_requires_name(self) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "secrets.update",
                "--id",
                "sec-1",
                "--dry-run",
            ]
        )
        with pytest.raises(CLIError, match="--name"):
            args.func(args)


class TestMainEntrypoint:
    def test_main_returns_zero_on_success(self) -> None:
        with patch("sys.argv", ["qaip", "schema"]):
            result = main()
            assert result == 0

    def test_main_returns_one_on_error(self) -> None:
        with patch("sys.argv", ["qaip", "api", "search.create"]):
            result = main()
            assert result == 1


class TestStartupAuthCheck:
    """`qaip api ...` を未認証で叩くと API コール前に missing_credentials で死ぬ。

    `qaip schema` / `--dry-run` は資格情報なしでも動くべきなので、その path
    では auth check が走らないことも確認する。
    """

    def test_missing_credentials_exits_with_auth_code(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        monkeypatch.delenv("QAIP_API_KEY", raising=False)
        with patch("sys.argv", ["qaip", "api", "tags.list"]):
            rc = main()
        assert rc == 3  # EXIT_AUTH
        captured = capsys.readouterr()
        assert "API key is required" in captured.err

    def test_missing_credentials_in_json_format(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        monkeypatch.delenv("QAIP_API_KEY", raising=False)
        with patch("sys.argv", ["qaip", "--error-format", "json", "api", "tags.list"]):
            rc = main()
        assert rc == 3
        captured = capsys.readouterr()
        payload = json.loads(captured.err)
        assert payload["error"]["code"] == "missing_credentials"
        assert payload["error"]["retryable"] is False
        assert "hint" in payload["error"]

    def test_schema_works_without_credentials(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("QAIP_API_KEY", raising=False)
        with patch("sys.argv", ["qaip", "schema"]):
            rc = main()
        assert rc == 0

    def test_dry_run_works_without_credentials(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("QAIP_API_KEY", raising=False)
        with patch("sys.argv", ["qaip", "api", "search.create", "--query", "x", "--dry-run"]):
            rc = main()
        assert rc == 0


class TestStructuredErrorOutput:
    """`--error-format json` および QAIP_ERROR_FORMAT=json で stderr が
    `{error:{code,message,retryable,...}}` の JSON になる。"""

    def test_json_error_for_missing_required_arg(self, capsys: pytest.CaptureFixture[str]) -> None:
        with patch("sys.argv", ["qaip", "--error-format", "json", "api", "search.create"]):
            rc = main()
        assert rc == 1  # generic CLIError (code=cli_error)
        captured = capsys.readouterr()
        payload = json.loads(captured.err)
        assert payload["error"]["code"] == "cli_error"
        assert "--query" in payload["error"]["message"]

    def test_json_error_for_invalid_id(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        monkeypatch.setenv("QAIP_API_KEY", "fake")
        with patch(
            "sys.argv",
            ["qaip", "--error-format", "json", "api", "content.retrieve", "--id", "not-uuid"],
        ):
            rc = main()
        assert rc == 4  # EXIT_VALIDATION
        captured = capsys.readouterr()
        payload = json.loads(captured.err)
        assert payload["error"]["code"] == "invalid_id"
        assert "UUID" in payload["error"]["message"]

    def test_env_var_selects_json_format(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        monkeypatch.setenv("QAIP_ERROR_FORMAT", "json")
        with patch("sys.argv", ["qaip", "api", "search.create"]):
            rc = main()
        assert rc == 1
        captured = capsys.readouterr()
        # JSON として読めること
        json.loads(captured.err)


class TestIdValidation:
    """ID 引数は本実行時のみ UUID 形式に限定される。dry-run では緩和される。"""

    def test_invalid_id_rejected_at_real_call(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("QAIP_API_KEY", "fake")
        parser = _build_parser()
        args = parser.parse_args(["api", "content.retrieve", "--id", "https://x.example/foo"])
        with pytest.raises(CLIError) as exc_info:
            args.func(args)
        assert exc_info.value.code == "invalid_id"

    def test_path_traversal_rejected(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("QAIP_API_KEY", "fake")
        parser = _build_parser()
        args = parser.parse_args(["api", "sources.retrieve", "--id", "../../etc/passwd"])
        with pytest.raises(CLIError) as exc_info:
            args.func(args)
        assert exc_info.value.code == "invalid_id"

    def test_uuid_passes(self, monkeypatch: pytest.MonkeyPatch) -> None:
        from unittest.mock import MagicMock, patch as _patch

        monkeypatch.setenv("QAIP_API_KEY", "fake")
        mock_client = MagicMock()
        mock_client.content.return_value.model_dump.return_value = {"id": _VALID_UUID}
        with _patch("qaip.cli._utils.qaip.Qaip", return_value=mock_client):
            parser = _build_parser()
            args = parser.parse_args(
                [
                    "--error-format",
                    "json",
                    "api",
                    "content.retrieve",
                    "--id",
                    _VALID_UUID,
                ]
            )
            args.func(args)  # 例外が出なければ OK

    def test_dry_run_does_not_validate_id(self) -> None:
        # dry-run はテンプレ確認なので非UUIDでも素通し（既存テストとの互換性も担保）
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "content.retrieve",
                "--id",
                "abc",
                "--dry-run",
            ]
        )
        args.func(args)  # 例外が出なければ OK


class TestDestructiveYesGuard:
    """destructive コマンドは `--yes` 必須。`--dry-run` 経由は不要。"""

    def test_secrets_delete_without_yes_blocks(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("QAIP_API_KEY", "fake")
        parser = _build_parser()
        args = parser.parse_args(["api", "secrets.delete", "--id", _VALID_UUID])
        with pytest.raises(CLIError) as exc_info:
            args.func(args)
        assert exc_info.value.code == "confirmation_required"

    def test_crawls_delete_without_yes_blocks(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("QAIP_API_KEY", "fake")
        parser = _build_parser()
        args = parser.parse_args(["api", "crawls.delete", "--id", _VALID_UUID])
        with pytest.raises(CLIError) as exc_info:
            args.func(args)
        assert exc_info.value.code == "confirmation_required"

    def test_dry_run_does_not_require_yes(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "secrets.delete",
                "--id",
                _VALID_UUID,
                "--dry-run",
            ]
        )
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "DELETE"

    def test_yes_flag_allows_execution(self, monkeypatch: pytest.MonkeyPatch) -> None:
        from unittest.mock import MagicMock, patch as _patch

        monkeypatch.setenv("QAIP_API_KEY", "fake")
        mock_client = MagicMock()
        mock_client.secrets.delete.return_value.model_dump.return_value = {"id": _VALID_UUID}
        with _patch("qaip.cli._utils.qaip.Qaip", return_value=mock_client):
            parser = _build_parser()
            args = parser.parse_args(
                [
                    "api",
                    "secrets.delete",
                    "--id",
                    _VALID_UUID,
                    "--yes",
                ]
            )
            args.func(args)
        mock_client.secrets.delete.assert_called_once_with(_VALID_UUID)

    def test_tags_delete_without_yes_blocks(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("QAIP_API_KEY", "fake")
        parser = _build_parser()
        args = parser.parse_args(["api", "tags.delete", "--id", _VALID_UUID])
        with pytest.raises(CLIError) as exc_info:
            args.func(args)
        assert exc_info.value.code == "confirmation_required"

    def test_tag_source_groups_delete_without_yes_blocks(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("QAIP_API_KEY", "fake")
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "tag-source-groups.delete",
                "--tag-id",
                _VALID_UUID,
                "--source-group-id",
                _VALID_UUID,
            ]
        )
        with pytest.raises(CLIError) as exc_info:
            args.func(args)
        assert exc_info.value.code == "confirmation_required"

    def test_tag_source_groups_delete_invalid_id_before_yes(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """validate_id が require_yes より先に走り、不正 ID の場合は破壊操作の
        確認を求める前に invalid_id で弾く。"""
        monkeypatch.setenv("QAIP_API_KEY", "fake")
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "tag-source-groups.delete",
                "--tag-id",
                "not-a-uuid",
                "--source-group-id",
                _VALID_UUID,
            ]
        )
        with pytest.raises(CLIError) as exc_info:
            args.func(args)
        assert exc_info.value.code == "invalid_id"

    @pytest.mark.parametrize(
        "argv",
        [
            ["api", "secrets.delete", "--id", "not-a-uuid"],
            ["api", "crawls.delete", "--id", "not-a-uuid"],
            ["api", "githubs.delete", "--id", "not-a-uuid"],
            ["api", "google-drives.delete", "--id", "not-a-uuid"],
            ["api", "notions.delete", "--id", "not-a-uuid"],
            ["api", "local-file-groups.delete", "--id", "not-a-uuid"],
            ["api", "sources.delete_metadata", "--id", "not-a-uuid"],
            ["api", "source-groups.delete_metadata", "--id", "not-a-uuid"],
            ["api", "tags.delete", "--id", "not-a-uuid"],
        ],
    )
    def test_destructive_invalid_id_rejected_before_yes(self, argv: list[str], monkeypatch: pytest.MonkeyPatch) -> None:
        """全 destructive コマンドで `validate_id → require_yes` の順序を保証する。
        不正 ID と `--yes` 抜きを同時に渡したとき、確認要求ではなく invalid_id が先に出る。"""
        monkeypatch.setenv("QAIP_API_KEY", "fake")
        parser = _build_parser()
        args = parser.parse_args(argv)
        with pytest.raises(CLIError) as exc_info:
            args.func(args)
        assert exc_info.value.code == "invalid_id"


class TestTagsExecution:
    """tags.create / update / delete は低レベル HTTP メソッド経由で実行される。"""

    def test_create_executes_post(self, monkeypatch: pytest.MonkeyPatch) -> None:
        from unittest.mock import MagicMock, patch as _patch

        monkeypatch.setenv("QAIP_API_KEY", "fake")
        mock_client = MagicMock()
        mock_client.post.return_value.model_dump.return_value = {"id": _VALID_UUID}
        with _patch("qaip.cli._utils.qaip.Qaip", return_value=mock_client):
            parser = _build_parser()
            args = parser.parse_args([
                "api", "tags.create", "--name", "important", "--description", "d",
            ])
            args.func(args)
        path, kwargs = mock_client.post.call_args[0], mock_client.post.call_args[1]
        assert path == ("/tags",)
        assert kwargs["body"] == {"name": "important", "description": "d"}

    def test_update_executes_put(self, monkeypatch: pytest.MonkeyPatch) -> None:
        from unittest.mock import MagicMock, patch as _patch

        monkeypatch.setenv("QAIP_API_KEY", "fake")
        mock_client = MagicMock()
        mock_client.put.return_value.model_dump.return_value = {"id": _VALID_UUID}
        with _patch("qaip.cli._utils.qaip.Qaip", return_value=mock_client):
            parser = _build_parser()
            args = parser.parse_args([
                "api", "tags.update", "--id", _VALID_UUID, "--name", "renamed",
            ])
            args.func(args)
        assert mock_client.put.call_args[0] == (f"/tags/{_VALID_UUID}",)
        assert mock_client.put.call_args[1]["body"] == {"name": "renamed"}

    def test_delete_executes_delete_with_yes(self, monkeypatch: pytest.MonkeyPatch) -> None:
        from unittest.mock import MagicMock, patch as _patch

        monkeypatch.setenv("QAIP_API_KEY", "fake")
        mock_client = MagicMock()
        mock_client.delete.return_value.model_dump.return_value = {"id": _VALID_UUID}
        with _patch("qaip.cli._utils.qaip.Qaip", return_value=mock_client):
            parser = _build_parser()
            args = parser.parse_args([
                "api", "tags.delete", "--id", _VALID_UUID, "--yes",
            ])
            args.func(args)
        assert mock_client.delete.call_args[0] == (f"/tags/{_VALID_UUID}",)


class TestAgentRunIdAcceptsCustomString:
    """agent.* の retrieve/cancel/result/events は caller 発行 ID を許容する。

    `agent.create_run` は input.run_id に任意の文字列を渡せる仕様のため、
    follow-up コマンドで UUID 強制すると regression になる。
    """

    def test_retrieve_run_accepts_non_uuid_id(self, monkeypatch: pytest.MonkeyPatch) -> None:
        from unittest.mock import MagicMock, patch as _patch

        monkeypatch.setenv("QAIP_API_KEY", "fake")
        mock_client = MagicMock()
        mock_client.agent.retrieve_run.return_value.model_dump.return_value = {"id": "my-run-1"}
        with _patch("qaip.cli._utils.qaip.Qaip", return_value=mock_client):
            parser = _build_parser()
            args = parser.parse_args(["api", "agent.retrieve_run", "--id", "my-run-1"])
            args.func(args)
        mock_client.agent.retrieve_run.assert_called_once_with("my-run-1")

    def test_cancel_run_accepts_non_uuid_id(self, monkeypatch: pytest.MonkeyPatch) -> None:
        from unittest.mock import MagicMock, patch as _patch

        monkeypatch.setenv("QAIP_API_KEY", "fake")
        mock_client = MagicMock()
        mock_client.agent.cancel_run.return_value.model_dump.return_value = {}
        with _patch("qaip.cli._utils.qaip.Qaip", return_value=mock_client):
            parser = _build_parser()
            args = parser.parse_args(["api", "agent.cancel_run", "--id", "user-supplied-run"])
            args.func(args)
        mock_client.agent.cancel_run.assert_called_once_with("user-supplied-run")

    def test_list_run_events_accepts_non_uuid_id(self, monkeypatch: pytest.MonkeyPatch) -> None:
        from unittest.mock import MagicMock, patch as _patch

        monkeypatch.setenv("QAIP_API_KEY", "fake")
        mock_client = MagicMock()
        mock_client.agent.list_run_events.return_value.model_dump.return_value = {"events": []}
        with _patch("qaip.cli._utils.qaip.Qaip", return_value=mock_client):
            parser = _build_parser()
            args = parser.parse_args(["api", "agent.list_run_events", "--id", "run-x"])
            args.func(args)
        # run_id が SDK にそのまま渡っていることを位置引数で確認する。
        assert mock_client.agent.list_run_events.call_args.args == ("run-x",)

    @pytest.mark.parametrize(
        "subcommand",
        [
            "agent.retrieve_run",
            "agent.cancel_run",
            "agent.retrieve_run_result",
            "agent.list_run_events",
        ],
    )
    @pytest.mark.parametrize(
        "bad_id",
        ["", "  ", ".", "..", "../etc", "foo/bar", "foo\\bar", "foo%2e", "\x07ctl"],
    )
    def test_followup_commands_reject_invalid_run_id(
        self,
        subcommand: str,
        bad_id: str,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """4 つの follow-up コマンドが揃って不正 run_id を弾くことを保証する。
        将来 validate_loose_id 呼び出しがどれか 1 つから消えても気付ける。"""
        monkeypatch.setenv("QAIP_API_KEY", "fake")
        parser = _build_parser()
        args = parser.parse_args(["api", subcommand, "--id", bad_id])
        with pytest.raises(CLIError) as exc_info:
            args.func(args)
        assert exc_info.value.code == "invalid_id"

    def test_create_run_rejects_invalid_run_id(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """creation 側でも同じ loose_id 検証をかけないと、create で受け付けた
        run_id が follow-up で拒否される非対称が起きる。"""
        monkeypatch.setenv("QAIP_API_KEY", "fake")
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "agent.create_run",
                "--messages",
                json.dumps([{"role": "user", "content": "hi"}]),
                "--run-id",
                "../etc",
                "--dry-run",
            ]
        )
        with pytest.raises(CLIError) as exc_info:
            args.func(args)
        assert exc_info.value.code == "invalid_id"

    def test_run_rejects_invalid_thread_id(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("QAIP_API_KEY", "fake")
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "agent.run",
                "--messages",
                json.dumps([{"role": "user", "content": "hi"}]),
                "--thread-id",
                "../etc",
                "--dry-run",
            ]
        )
        with pytest.raises(CLIError) as exc_info:
            args.func(args)
        assert exc_info.value.code == "invalid_id"

    def test_main_returns_validation_exit_for_empty_run_id(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """`--id ''` が SDK の ValueError として露出せず、構造化エラーになる。"""
        monkeypatch.setenv("QAIP_API_KEY", "fake")
        with patch(
            "sys.argv",
            ["qaip", "--error-format", "json", "api", "agent.retrieve_run", "--id", ""],
        ):
            rc = main()
        assert rc == 4
        captured = capsys.readouterr()
        payload = json.loads(captured.err)
        assert payload["error"]["code"] == "invalid_id"


class TestApiErrorExitCodeMapping:
    """APIStatusError の status_code に応じた exit code 分化。"""

    def _run_with_api_error(
        self,
        status_code: int,
        monkeypatch: pytest.MonkeyPatch,
    ) -> int:
        from unittest.mock import MagicMock, patch as _patch

        import httpx

        from qaip._exceptions import APIStatusError

        monkeypatch.setenv("QAIP_API_KEY", "fake")
        request = httpx.Request("GET", "https://example.com/")
        response = httpx.Response(status_code, request=request)

        class _Err(APIStatusError):
            pass

        err = _Err(f"status {status_code}", response=response, body=None)

        mock_client = MagicMock()
        mock_client.tags.side_effect = err

        with _patch("qaip.cli._utils.qaip.Qaip", return_value=mock_client):
            with patch("sys.argv", ["qaip", "api", "tags.list"]):
                return main()

    def test_400_maps_to_validation(self, monkeypatch: pytest.MonkeyPatch) -> None:
        rc = self._run_with_api_error(400, monkeypatch)
        assert rc == 4

    def test_422_maps_to_validation(self, monkeypatch: pytest.MonkeyPatch) -> None:
        rc = self._run_with_api_error(422, monkeypatch)
        assert rc == 4

    def test_500_maps_to_api(self, monkeypatch: pytest.MonkeyPatch) -> None:
        rc = self._run_with_api_error(500, monkeypatch)
        assert rc == 5

    def test_401_maps_to_auth(self, monkeypatch: pytest.MonkeyPatch) -> None:
        rc = self._run_with_api_error(401, monkeypatch)
        assert rc == 3


class TestSchemaUnknownStructured:
    """schema 失敗が --error-format json で構造化エラーになる。"""

    def test_unknown_resource_is_structured(self, capsys: pytest.CaptureFixture[str]) -> None:
        with patch(
            "sys.argv",
            ["qaip", "--error-format", "json", "schema", "nonexistent"],
        ):
            rc = main()
        assert rc == 4  # invalid_argument → EXIT_VALIDATION
        captured = capsys.readouterr()
        payload = json.loads(captured.err)
        assert payload["error"]["code"] == "invalid_argument"
        assert "nonexistent" in payload["error"]["message"]
        assert "hint" in payload["error"]


class TestSecretsUpdateSecretValueGuard:
    """secrets.update で secret キーが body にある場合のみ --yes 必須。"""

    def test_update_secret_value_without_yes_blocks(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("QAIP_API_KEY", "fake")
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "secrets.update",
                "--id",
                _VALID_UUID,
                "--name",
                "n",
                "--json",
                json.dumps({"secret": "rotated"}),
            ]
        )
        with pytest.raises(CLIError) as exc_info:
            args.func(args)
        assert exc_info.value.code == "confirmation_required"

    def test_update_name_only_does_not_require_yes(self, monkeypatch: pytest.MonkeyPatch) -> None:
        from unittest.mock import MagicMock, patch as _patch

        monkeypatch.setenv("QAIP_API_KEY", "fake")
        mock_client = MagicMock()
        mock_client.secrets.update.return_value.model_dump.return_value = {"id": _VALID_UUID}
        with _patch("qaip.cli._utils.qaip.Qaip", return_value=mock_client):
            parser = _build_parser()
            args = parser.parse_args(
                [
                    "api",
                    "secrets.update",
                    "--id",
                    _VALID_UUID,
                    "--name",
                    "renamed",
                ]
            )
            args.func(args)
        mock_client.secrets.update.assert_called_once()

    def test_update_invalid_id_before_yes(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """validate_id が require_yes より先。不正な secret_id の場合は破壊操作の
        確認を求める前に invalid_id で弾く。"""
        monkeypatch.setenv("QAIP_API_KEY", "fake")
        parser = _build_parser()
        args = parser.parse_args(
            [
                "api",
                "secrets.update",
                "--id",
                "not-a-uuid",
                "--name",
                "n",
                "--json",
                json.dumps({"secret": "rotated"}),
            ]
        )
        with pytest.raises(CLIError) as exc_info:
            args.func(args)
        assert exc_info.value.code == "invalid_id"

    def test_update_secret_value_with_yes_passes(self, monkeypatch: pytest.MonkeyPatch) -> None:
        from unittest.mock import MagicMock, patch as _patch

        monkeypatch.setenv("QAIP_API_KEY", "fake")
        mock_client = MagicMock()
        mock_client.secrets.update.return_value.model_dump.return_value = {"id": _VALID_UUID}
        with _patch("qaip.cli._utils.qaip.Qaip", return_value=mock_client):
            parser = _build_parser()
            args = parser.parse_args(
                [
                    "api",
                    "secrets.update",
                    "--id",
                    _VALID_UUID,
                    "--name",
                    "n",
                    "--yes",
                    "--json",
                    json.dumps({"secret": "rotated"}),
                ]
            )
            args.func(args)
        mock_client.secrets.update.assert_called_once()
