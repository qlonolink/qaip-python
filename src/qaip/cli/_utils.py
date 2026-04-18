from __future__ import annotations

import argparse
from typing import Any

import qaip


def get_client(args: argparse.Namespace | None = None) -> qaip.Qaip:
    """CLI の共通引数から Qaip クライアントを生成する。

    --api-key / --base-url が指定されていれば優先し、未指定ならSDKの
    デフォルト（環境変数など）に委ねる。
    """
    api_key: str | None = getattr(args, "api_key", None) if args is not None else None
    base_url: str | None = getattr(args, "base_url", None) if args is not None else None
    kwargs: dict[str, Any] = {}
    if api_key:
        kwargs["api_key"] = api_key
    if base_url:
        kwargs["base_url"] = base_url
    return qaip.Qaip(**kwargs)
