# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["CrawlDownloadRawArchiveParams"]


class CrawlDownloadRawArchiveParams(TypedDict, total=False):
    source_ids: SequenceNotStr[str]
    """Source IDs to include.

    Omit to include every source in the crawl; an empty array is invalid.
    """
