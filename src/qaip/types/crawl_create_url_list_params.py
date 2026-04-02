# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .shared_params.metadata import Metadata

__all__ = ["CrawlCreateURLListParams"]


class CrawlCreateURLListParams(TypedDict, total=False):
    name: Required[str]
    """Name of the web crawl data source"""

    target_urls: Required[SequenceNotStr[str]]
    """List of URLs to download directly. Each URL must use http or https scheme."""

    max_num_files: int
    """Maximum number of files to download.

    Defaults to the number of target URLs if omitted.
    """

    metadata: Metadata
    """(reserved for future use) Additional metadata for the web crawl data source"""

    rrule: str
    """Recurrence rule (RFC 5545 RRULE)"""
