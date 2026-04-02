# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .shared_params.metadata import Metadata

__all__ = ["CrawlCreateParams"]


class CrawlCreateParams(TypedDict, total=False):
    max_depth: Required[int]
    """Maximum crawl depth"""

    max_num_files: Required[int]
    """Maximum number of files to crawl"""

    name: Required[str]
    """Name of the web crawl data source"""

    start_url: Required[str]
    """Start URL of the web crawl"""

    content_pattern: SequenceNotStr[str]
    """Content patterns for filtering.

    The total number of characters across all elements in the array must be 2000 or
    fewer.
    """

    file_extensions: SequenceNotStr[str]
    """File extensions to include (e.g.

    ".pdf", ".docx"). For supported file extensions, please refer to
    https://developer.qaip.com/docs/datasources#%E5%AF%BE%E5%BF%9C%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%BD%A2%E5%BC%8F
    """

    html_only: bool
    """When true, only HTML files will be downloaded"""

    metadata: Metadata
    """(reserved for future use) Additional metadata for the web crawl data source"""

    path_filters: SequenceNotStr[str]
    """Path filters for crawling.

    The total number of characters across all elements in the array must be 2000 or
    fewer.
    """

    rrule: str
    """Recurrence rule (RFC 5545 RRULE)"""

    use_browser: bool
    """Whether to use a headless browser for crawling"""
