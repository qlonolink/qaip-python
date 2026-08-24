from __future__ import annotations

import re
import sys
import json
import argparse
from typing import Any, cast

from .._errors import CLIError

_UUID_RE = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")

# `validate_loose_id` の許容文字。空白（タブ・改行・unicode 空白すべて）/ path 区切り
# (`/` `\\`) / URL エンコード文字 (`%`) / ASCII 制御文字 (`\x00`-`\x1f`, DEL) を弾く
# ホワイトリスト方針。dot-segment (`.` / `..`) は別チェック。
_LOOSE_ID_RE = re.compile(r"^[^\s/\\%\x00-\x1f\x7f]+$")


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


def add_yes(parser: argparse.ArgumentParser) -> None:
    """destructive コマンドの確認フラグを追加する。"""
    parser.add_argument(
        "--yes",
        action="store_true",
        default=False,
        help="Confirm execution of a destructive operation (required unless --dry-run)",
    )


def require_yes(args: argparse.Namespace, *, action: str) -> None:
    """destructive 本実行で `--yes` が無い場合に拒否する。

    `--dry-run` 経由ではこの関数の呼び出し自体が起きない前提（各サブコマンドで
    `if args.dry_run` で先に return しておくこと）。
    """
    if getattr(args, "yes", False):
        return
    raise CLIError(
        f"Refusing to execute destructive operation ({action}) without --yes",
        code="confirmation_required",
        hint="Re-run with --dry-run to inspect the request, then add --yes to apply.",
    )


def validate_id(value: str, *, label: str = "id") -> str:
    """ID 引数を hex 8-4-4-4-12 形式（UUID 文字列レイアウト）に限定する。

    エージェントの暴走で URL / path traversal / 制御文字が ID に混入しても
    CLI 段で弾くための防衛線。サーバ側 400 を待たず早期失敗させる。
    `--dry-run` 経由では呼ばれない（テンプレ確認用途のため緩和）。

    なお RFC 4122 の variant / version bit は検証しない（サーバ側の仕様に
    委ねる）。caller 発行 ID を許容するエンドポイント（agent run_id 等）
    では本関数の代わりに `validate_loose_id` を使うこと。
    """
    if not _UUID_RE.match(value):
        raise CLIError(
            f"Invalid {label}: {value!r} is not a UUID",
            code="invalid_id",
            hint=f"{label} must be a UUID like '00000000-0000-0000-0000-000000000000'.",
        )
    return value


def validate_loose_id(value: str, *, label: str = "id") -> str:
    """caller 発行 ID（agent run_id 等、UUID を強制できないもの）の最低限のサニティ。

    SDK 側の `path_template` は `.`/`..`/empty 以外のあやしい文字を percent-encode
    してそのまま送るため、エージェントが意図せず混入させた path 区切り (`/` `\\`)・
    URL エンコード文字 (`%`)・空白・ASCII 制御文字・dot-segment をサーバに届ける
    前に CLI で弾く。`--id ''` で SDK が `ValueError` を投げる経路（main で
    catch されず traceback が露出する）に対する構造化エラー保証も兼ねる。
    """
    if value in (".", ".."):
        raise CLIError(
            f"Invalid {label}: dot-segment {value!r} is not allowed",
            code="invalid_id",
        )
    if not _LOOSE_ID_RE.match(value):
        raise CLIError(
            f"Invalid {label}: must be a non-empty path-safe token "
            "(no whitespace, slashes, percent, or control characters)",
            code="invalid_id",
            hint=f"{label} must match /^[^\\s/\\\\%\\x00-\\x1f\\x7f]+$/.",
        )
    return value


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


def validate_json_body_fields(body: dict[str, Any], *, allowed: frozenset[str]) -> None:
    """SDK の制御引数を request body として受け付けないようフィールドを限定する。"""
    unknown = sorted(set(body) - allowed)
    if unknown:
        raise CLIError(f"unsupported field(s) in --json: {', '.join(unknown)}")


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
    headers: dict[str, Any] | None = None,
    query: dict[str, Any] | None = None,
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
    if headers is not None:
        result["headers"] = headers
    if query is not None:
        result["query"] = query
    sys.stdout.write(json.dumps(result, indent=2, ensure_ascii=False, default=str) + "\n")
