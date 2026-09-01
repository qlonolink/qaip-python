# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SourceDownloadRawParams"]


class SourceDownloadRawParams(TypedDict, total=False):
    crawl_id: str
    """Parent crawl ID.

    When supplied, the raw file is resolved through the crawl manifest without
    scanning the global crawled_files table. Omission uses the deprecated fallback.
    """
