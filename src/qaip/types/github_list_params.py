# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GitHubListParams"]


class GitHubListParams(TypedDict, total=False):
    after_id: str
    """Fetch records after this ID"""

    limit: int
    """Maximum number of results to return"""
