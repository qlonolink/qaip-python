from __future__ import annotations

import sys
import argparse
from typing import Any

import pydantic

from ._api import register_commands
from ._errors import CLIError, SilentCLIError, display_error
from .._version import __version__
from .._exceptions import APIError, QaipError, APIStatusError

# 終了コードはエラー種別ごとに分化させる。argparse 自身の usage error は
# SystemExit(2) を投げるため、`2` はそちらに譲る。
EXIT_OK = 0
EXIT_GENERIC = 1
EXIT_USAGE = 2
EXIT_AUTH = 3
EXIT_VALIDATION = 4
EXIT_API = 5


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Qaip API command-line client",
        prog="qaip",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version="%(prog)s " + __version__,
    )
    parser.add_argument(
        "-k",
        "--api-key",
        help="API key (defaults to QAIP_API_KEY env var)",
    )
    parser.add_argument(
        "-b",
        "--base-url",
        help="API base URL (defaults to QAIP_BASE_URL env var)",
    )
    parser.add_argument(
        "--error-format",
        choices=("text", "json"),
        default=None,
        help="Format for error output written to stderr "
        "(default: text; or set QAIP_ERROR_FORMAT=json)",
    )
    def show_help(_: argparse.Namespace) -> None:
        parser.print_help()

    parser.set_defaults(func=show_help)

    subparsers = parser.add_subparsers(title="commands")

    sub_api = subparsers.add_parser("api", help="Direct API calls")
    register_commands(sub_api)

    _register_schema_command(subparsers)

    return parser


def _register_schema_command(subparsers: Any) -> None:  # noqa: ANN401
    sub = subparsers.add_parser(
        "schema",
        help="Show API schema for a resource or method (agent-friendly introspection)",
    )
    sub.add_argument(
        "resource",
        nargs="?",
        help="Resource name (e.g. sources, crawls, agent). Omit to list all resources.",
    )
    sub.set_defaults(func=_schema_command)


def _schema_command(args: argparse.Namespace) -> None:
    from ._schema import show_schema

    show_schema(args.resource)


def _cli_error_exit_code(err: CLIError) -> int:
    if err.code == "missing_credentials":
        return EXIT_AUTH
    if err.code in ("invalid_id", "invalid_argument", "validation_error"):
        return EXIT_VALIDATION
    if err.code == "confirmation_required":
        return EXIT_VALIDATION
    return EXIT_GENERIC


def main() -> int:
    error_format: str | None = None
    try:
        parser = _build_parser()
        args = parser.parse_args()
        error_format = getattr(args, "error_format", None)
        args.func(args)
    except SilentCLIError:
        return EXIT_GENERIC
    except CLIError as err:
        display_error(err, error_format=error_format)
        return _cli_error_exit_code(err)
    except APIStatusError as err:
        display_error(err, error_format=error_format)
        if err.status_code in (401, 403):
            return EXIT_AUTH
        # 400/422 は agent 視点で「入力を直す」案件なので validation 側へ
        if err.status_code in (400, 422):
            return EXIT_VALIDATION
        return EXIT_API
    except APIError as err:
        display_error(err, error_format=error_format)
        return EXIT_API
    except pydantic.ValidationError as err:
        display_error(
            CLIError(str(err), code="validation_error"),
            error_format=error_format,
        )
        return EXIT_VALIDATION
    except QaipError as err:
        # SDK の自前例外を構造化エラーに正規化する防御的フォールバック。
        # 認証欠如は `_utils.get_client` の早期 check で CLIError として処理
        # されるため、ここに到達するのは想定外のクライアント側エラー。
        display_error(CLIError(str(err)), error_format=error_format)
        return EXIT_GENERIC
    except TypeError as err:
        # --json で SDK メソッドのシグネチャに合わない引数が渡されたケース
        # （例: `unexpected keyword argument 'foo'`）はユーザー向けエラーに変換する。
        # 内部バグ由来の TypeError は握り潰さず再送出する。
        msg = str(err)
        if "unexpected keyword argument" in msg or "got multiple values for" in msg:
            display_error(
                CLIError(f"Invalid argument: {err}", code="invalid_argument"),
                error_format=error_format,
            )
            return EXIT_VALIDATION
        raise
    except KeyboardInterrupt:
        sys.stderr.write("\n")
        return EXIT_GENERIC
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
