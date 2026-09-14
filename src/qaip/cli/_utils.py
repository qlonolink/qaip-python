from __future__ import annotations

import os
import re
import argparse
from typing import Any

import qaip

from ._errors import CLIError

_HEADER_NAME_RE = re.compile(r"^[!#$%&'*+\-.^_`|~0-9A-Za-z]+$")
_BLOCKED_HEADER_NAMES = frozenset(
    {
        "authorization",
        "connection",
        "content-length",
        "content-type",
        "expect",
        "host",
        "proxy-authorization",
        "te",
        "trailer",
        "transfer-encoding",
        "upgrade",
        "x-api-key",
    }
)
_BLOCKED_HEADER_PREFIXES = ("x-stainless-",)


def _has_invalid_header_value_char(value: str) -> bool:
    return any((ord(char) < 32 and char != "\t") or ord(char) >= 127 for char in value)


def parse_headers(raw: list[str] | None) -> dict[str, str]:
    """`-H/--header` で渡された 'Name: Value' 形式の文字列を dict に変換する。

    区切りは最初の ':'。名前が空、または ':' を含まない要素は入力エラーとする。
    非公開ヘッダー（社内限定機能の伝送路など）を任意に付与するための汎用口。
    """
    headers: dict[str, str] = {}
    for item in raw or []:
        name, sep, value = item.partition(":")
        name = name.strip()
        if not sep or not name:
            raise CLIError(
                "invalid header: expected 'Name: Value'",
                code="invalid_argument",
            )
        normalized_name = name.lower()
        if not _HEADER_NAME_RE.fullmatch(name):
            raise CLIError(
                "invalid header name: expected RFC 7230 token",
                code="invalid_argument",
            )
        if normalized_name in _BLOCKED_HEADER_NAMES or normalized_name.startswith(_BLOCKED_HEADER_PREFIXES):
            raise CLIError(
                "invalid header: header is managed by the CLI/SDK",
                code="invalid_argument",
            )
        if _has_invalid_header_value_char(value):
            raise CLIError(
                "invalid header value: contains unsupported control characters",
                code="invalid_argument",
            )
        value = value.strip(" \t")
        headers[name] = value
    return headers


def get_client(args: argparse.Namespace | None = None) -> qaip.Qaip:
    """CLI の共通引数から Qaip クライアントを生成する。

    --api-key / --base-url が指定されていれば優先し、未指定ならSDKの
    デフォルト（環境変数など）に委ねる。--header は default_headers として
    全リクエストに付与する。

    認証情報が一切無い状態（`--api-key` 未指定 かつ `QAIP_API_KEY` env も無し）
    では、API コール時点まで待たず CLI 段で `missing_credentials` として
    早期失敗する（agent-friendly setup check）。
    """
    api_key: str | None = getattr(args, "api_key", None) if args is not None else None
    base_url: str | None = getattr(args, "base_url", None) if args is not None else None
    headers = parse_headers(getattr(args, "headers", None) if args is not None else None)

    if not api_key and not os.environ.get("QAIP_API_KEY"):
        raise CLIError(
            "API key is required",
            code="missing_credentials",
            hint="Set QAIP_API_KEY env var, or pass --api-key. `qaip schema` and `--dry-run` work without credentials.",
        )

    kwargs: dict[str, Any] = {}
    if api_key:
        kwargs["api_key"] = api_key
    if base_url:
        kwargs["base_url"] = base_url
    if headers:
        kwargs["default_headers"] = headers
    return qaip.Qaip(**kwargs)
