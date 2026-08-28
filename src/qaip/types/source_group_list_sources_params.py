# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SourceGroupListSourcesParams"]


class SourceGroupListSourcesParams(TypedDict, total=False):
    after_id: str
    """Fetch sources after this source ID"""

    limit: int
    """Maximum number of results to return.

    Omit to return all sources for backward compatibility.
    """
