from __future__ import annotations

import sys
import json
import argparse
from typing import Any, cast

from .._errors import CLIError


def add_json_param(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--json",
        dest="json_body",
        help="JSON request body (pass raw JSON or @filename to read from file, or - for stdin)",
    )


def add_dry_run(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Validate and print the request without executing it",
    )


def add_fields(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--fields",
        help="Comma-separated list of fields to include in the output (e.g. 'id,name,status')",
    )


def parse_json_arg(raw: str, *, label: str) -> Any:  # noqa: ANN401
    """CLI 引数として渡された JSON 文字列をパースする。

    失敗時は traceback ではなくユーザー向けの CLIError にラップする。
    """
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        raise CLIError(f"Invalid JSON for {label}: {e}") from e


def parse_json_body(args: argparse.Namespace) -> dict[str, Any] | None:
    raw = getattr(args, "json_body", None)
    if raw is None:
        return None

    if raw == "-":
        raw = sys.stdin.read()
    elif raw.startswith("@"):
        filepath = raw[1:]
        try:
            with open(filepath) as f:
                raw = f.read()
        except FileNotFoundError as err:
            raise CLIError(f"File not found: {filepath}") from err

    data = parse_json_arg(raw, label="--json")

    if not isinstance(data, dict):
        raise CLIError("JSON body must be an object")

    return cast(dict[str, Any], data)


def filter_fields(data: Any, fields: str | None) -> Any:  # noqa: ANN401
    if fields is None or not isinstance(data, dict):
        return data

    field_list = [f.strip() for f in fields.split(",")]
    filtered: dict[str, Any] = {k: v for k, v in cast(dict[str, Any], data).items() if k in field_list}
    return filtered


def print_result(data: Any, args: argparse.Namespace) -> None:  # noqa: ANN401
    fields: str | None = getattr(args, "fields", None)
    filtered: Any
    if isinstance(data, list):
        filtered = [filter_fields(item, fields) for item in cast(list[Any], data)]
    else:
        filtered = filter_fields(data, fields)
    sys.stdout.write(json.dumps(filtered, indent=2, ensure_ascii=False, default=str) + "\n")


SENSITIVE_MASK = "***"


def print_dry_run(
    method: str,
    path: str,
    body: dict[str, Any] | None = None,
    *,
    sensitive_keys: tuple[str, ...] = (),
) -> None:
    """dry-run のリクエスト内容を標準出力に表示する。

    sensitive_keys に指定されたフィールドは値を `***` にマスクする。CI のログに
    平文のシークレットが残ることを防ぐ。
    """
    result: dict[str, Any] = {"method": method, "path": path}
    if body is not None:
        if sensitive_keys:
            masked = dict(body)
            for key in sensitive_keys:
                if key in masked:
                    masked[key] = SENSITIVE_MASK
            result["body"] = masked
        else:
            result["body"] = body
    sys.stdout.write(json.dumps(result, indent=2, ensure_ascii=False, default=str) + "\n")
