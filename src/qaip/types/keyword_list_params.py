# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["KeywordListParams"]


class KeywordListParams(TypedDict, total=False):
    offset: int
    """Number of records to skip"""

    page_size: int
    """Maximum number of results to return"""

    sort_field: str
    """Field to sort by"""

    sort_order: str
    """Sort order (e.g. "asc" or "desc")"""
