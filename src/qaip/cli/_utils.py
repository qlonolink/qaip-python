from __future__ import annotations

import os
import argparse
from typing import Any

import qaip

from ._errors import CLIError


def get_client(args: argparse.Namespace | None = None) -> qaip.Qaip:
    """CLI の共通引数から Qaip クライアントを生成する。

    --api-key / --base-url が指定されていれば優先し、未指定ならSDKの
    デフォルト（環境変数など）に委ねる。

    認証情報が一切無い状態（`--api-key` 未指定 かつ `QAIP_API_KEY` env も無し）
    では、API コール時点まで待たず CLI 段で `missing_credentials` として
    早期失敗する（agent-friendly setup check）。
    """
    api_key: str | None = getattr(args, "api_key", None) if args is not None else None
    base_url: str | None = getattr(args, "base_url", None) if args is not None else None

    if not api_key and not os.environ.get("QAIP_API_KEY"):
        raise CLIError(
            "API key is required",
            code="missing_credentials",
            hint="Set QAIP_API_KEY env var, or pass --api-key. `qaip schema` and "
            "`--dry-run` work without credentials.",
        )

    kwargs: dict[str, Any] = {}
    if api_key:
        kwargs["api_key"] = api_key
    if base_url:
        kwargs["base_url"] = base_url
    return qaip.Qaip(**kwargs)
