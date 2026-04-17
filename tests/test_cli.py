from __future__ import annotations

import json
from unittest.mock import patch

import pytest

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
        with pytest.raises(SystemExit):
            args.func(args)


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
        args = parser.parse_args([
            "api", "source-groups.list",
            "--limit", "5",
            "--source-type", "crawl",
            "--dry-run",
        ])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "GET"
        assert data["path"] == "/source-groups"
        assert data["body"]["source_type"] == "crawl"

    def test_secrets_create_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "secrets.create",
            "--name", "my-secret",
            "--secret", "val",
            "--type", "github_pat",
            "--dry-run",
        ])
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
        args = parser.parse_args([
            "api", "crawls.create",
            "--name", "test-crawl",
            "--start-url", "https://example.com",
            "--max-depth", "3",
            "--max-num-files", "100",
            "--file-extensions", ".pdf,.docx",
            "--rrule", "FREQ=DAILY",
            "--html-only",
            "--dry-run",
        ])
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
        args = parser.parse_args([
            "api", "crawls.create_url_list",
            "--name", "url-list",
            "--urls", "https://a.example.com,https://b.example.com",
            "--dry-run",
        ])
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
        args = parser.parse_args([
            "api", "agent.run",
            "--messages", messages,
            "--run-id", "run-x",
            "--dry-run",
        ])
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
        args = parser.parse_args([
            "api", "agent.create_run",
            "--messages", messages,
            "--thread-id", "t-1",
            "--idempotency-key", "abc",
            "--dry-run",
        ])
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
        args = parser.parse_args([
            "api", "agent.list_run_events",
            "--id", "run-1",
            "--limit", "5",
            "--after", "42",
            "--dry-run",
        ])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "GET"
        assert data["path"] == "/agent/runs/run-1/events"
        assert data["body"]["limit"] == 5
        assert data["body"]["after"] == 42

    def test_githubs_create_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "githubs.create",
            "--name", "gh-1",
            "--repository", "octocat/Hello-World",
            "--reference", "main",
            "--reference-type", "branch",
            "--dry-run",
        ])
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
        args = parser.parse_args([
            "api", "google-drives.create",
            "--name", "gd-1",
            "--folder-url", "https://drive.google.com/drive/folders/abc",
            "--secret-id", "sec-1",
            "--dry-run",
        ])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "POST"
        assert data["path"] == "/google-drives"
        assert data["body"]["folder_url"] == "https://drive.google.com/drive/folders/abc"
        assert data["body"]["secret_id"] == "sec-1"

    def test_notions_create_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "notions.create",
            "--name", "notion-1",
            "--page-id", "22cf90c7c8aa80098050fa40c6ebab1e",
            "--notion-token", "secret_xxx",
            "--dry-run",
        ])
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
        args = parser.parse_args([
            "api", "local-file-groups.create",
            "--name", "lfg",
            "--file", str(f1),
            "--last-modified", "1775000000000",
            "--dry-run",
        ])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data["method"] == "POST"
        assert data["path"] == "/local-file-groups"
        assert data["body"]["files"] == ["a.txt"]
        assert data["body"]["last_modified"] == [1775000000000]

    def test_tag_source_groups_create_dry_run(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "tag-source-groups.create",
            "--tag-id", "tag-1",
            "--source-group-id", "sg-1",
            "--dry-run",
        ])
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


class TestSensitiveMasking:
    def test_secrets_create_dry_run_masks_secret(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "secrets.create",
            "--name", "s",
            "--secret", "SHOULD_NOT_APPEAR",
            "--type", "github_pat",
            "--dry-run",
        ])
        args.func(args)
        captured = capsys.readouterr()
        assert "SHOULD_NOT_APPEAR" not in captured.out
        data = json.loads(captured.out)
        assert data["body"]["secret"] == "***"

    def test_secrets_update_dry_run_masks_secret(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "secrets.update",
            "--id", "sec-1",
            "--name", "s",
            "--json", json.dumps({"secret": "ROT_SHOULD_NOT_APPEAR"}),
            "--dry-run",
        ])
        args.func(args)
        captured = capsys.readouterr()
        assert "ROT_SHOULD_NOT_APPEAR" not in captured.out
        data = json.loads(captured.out)
        assert data["body"]["secret"] == "***"

    def test_githubs_create_dry_run_masks_token(self, capsys: pytest.CaptureFixture[str]) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "githubs.create",
            "--name", "g",
            "--repository", "o/r",
            "--github-token", "GHP_SHOULD_NOT_APPEAR",
            "--dry-run",
        ])
        args.func(args)
        captured = capsys.readouterr()
        assert "GHP_SHOULD_NOT_APPEAR" not in captured.out
        data = json.loads(captured.out)
        assert data["body"]["github_token"] == "***"

    def test_google_drives_create_dry_run_masks_service_account_key(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "google-drives.create",
            "--name", "gd",
            "--folder-url", "https://drive.google.com/drive/folders/x",
            "--service-account-key", "KEY_SHOULD_NOT_APPEAR",
            "--dry-run",
        ])
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

    def test_get_client_without_args(self) -> None:
        from unittest.mock import patch as _patch

        from qaip.cli._utils import get_client

        with _patch("qaip.cli._utils.qaip.Qaip") as mock_qaip:
            get_client()
            mock_qaip.assert_called_once_with()


class TestInvalidJsonArgs:
    def test_completion_invalid_messages_json(self) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "completion.create",
            "--messages", "not-json",
            "--dry-run",
        ])
        with pytest.raises(CLIError, match="Invalid JSON for --messages"):
            args.func(args)

    def test_extract_invalid_schema_json(self) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "extract.create",
            "--schema", "not-json",
            "--dry-run",
        ])
        with pytest.raises(CLIError, match="Invalid JSON for --schema"):
            args.func(args)

    def test_agent_run_invalid_forwarded_props_json(self) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "agent.run",
            "--forwarded-props", "not-json",
            "--dry-run",
        ])
        with pytest.raises(CLIError, match="Invalid JSON for --forwarded-props"):
            args.func(args)


class TestSecretsListDryRunKeyName:
    def test_secrets_list_dry_run_uses_secret_type_key(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "secrets.list",
            "--type", "github",
            "--dry-run",
        ])
        args.func(args)
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        # SDK とスキーマに合わせて secret_type キーで出力される
        assert data["body"]["secret_type"] == "github"
        assert "type" not in data["body"]


class TestLocalFileGroupsMissingFile:
    def test_missing_file_raises_cli_error(self) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "local-file-groups.create",
            "--name", "lfg",
            "--file", "/nonexistent/path/does-not-exist.txt",
            "--dry-run",
        ])
        with pytest.raises(CLIError, match="File not found"):
            args.func(args)


class TestMainTypeErrorHandling:
    def test_main_converts_unexpected_kwarg_typeerror(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """SDK 呼び出しで unexpected keyword argument の TypeError が発生した場合、
        スタックトレースではなくユーザー向けエラーに変換される。
        """
        from unittest.mock import MagicMock, patch as _patch

        mock_client = MagicMock()
        mock_client.content.side_effect = TypeError(
            "content() got an unexpected keyword argument 'foo'"
        )
        with _patch("qaip.cli._utils.qaip.Qaip", return_value=mock_client):
            with patch("sys.argv", ["qaip", "api", "content.retrieve", "--id", "abc"]):
                rc = main()
        assert rc == 1
        captured = capsys.readouterr()
        assert "Invalid argument" in captured.err

    def test_main_reraises_unrelated_typeerror(self) -> None:
        """SDK 呼び出し起因ではない TypeError は握り潰さない。"""
        from unittest.mock import MagicMock, patch as _patch

        mock_client = MagicMock()
        mock_client.content.side_effect = TypeError("not an sdk arg error")
        with _patch("qaip.cli._utils.qaip.Qaip", return_value=mock_client):
            with patch("sys.argv", ["qaip", "api", "content.retrieve", "--id", "abc"]):
                with pytest.raises(TypeError, match="not an sdk arg error"):
                    main()


class TestSecretsUpdateValidation:
    def test_secrets_update_requires_name(self) -> None:
        parser = _build_parser()
        args = parser.parse_args([
            "api", "secrets.update",
            "--id", "sec-1",
            "--dry-run",
        ])
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
