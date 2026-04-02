# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CrawlSetting"]


class CrawlSetting(BaseModel):
    id: str
    """Web crawl ingestion setting ID"""

    html_only: bool
    """When true, only HTML files will be downloaded"""

    max_depth: int
    """Maximum crawl depth"""

    name: str
    """Name of the web crawl ingestion setting"""

    start_url: str
    """Start URL of the web crawl"""

    use_browser: bool
    """Whether to use a headless browser for crawling"""

    content_pattern: Optional[List[str]] = None
    """Content patterns for filtering"""

    file_extensions: Optional[List[str]] = None
    """File extensions to include (e.g. ".pdf", ".docx")"""

    max_num_files: Optional[int] = None
    """Maximum number of files to crawl"""

    path_filters: Optional[List[str]] = None
    """Path filters for crawling"""

    rrule: Optional[str] = None
    """Recurrence rule (RFC 5545 RRULE)"""
