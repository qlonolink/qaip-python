from __future__ import annotations

import sys
import argparse
from typing import Any

import pydantic

from ._api import register_commands
from ._errors import CLIError, display_error
from .._version import __version__
from .._exceptions import APIError


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


def main() -> int:
    try:
        _main()
    except (APIError, CLIError, pydantic.ValidationError) as err:
        display_error(err)
        return 1
    except TypeError as err:
        # --json で SDK メソッドのシグネチャに合わない引数が渡されたケース
        # （例: `unexpected keyword argument 'foo'`）はユーザー向けエラーに変換する。
        # 内部バグ由来の TypeError は握り潰さず再送出する。
        msg = str(err)
        if "unexpected keyword argument" in msg or "got multiple values for" in msg:
            display_error(CLIError(f"Invalid argument: {err}"))
            return 1
        raise
    except KeyboardInterrupt:
        sys.stderr.write("\n")
        return 1
    return 0


def _main() -> None:
    parser = _build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    sys.exit(main())
