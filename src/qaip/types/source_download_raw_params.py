# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SourceDownloadRawParams"]


class SourceDownloadRawParams(TypedDict, total=False):
    crawl_id: str
    """Parent crawl ID used to resolve the file without a global table scan"""
