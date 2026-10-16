# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .search_result import SearchResult
from .search_pagination import SearchPagination

__all__ = ["SearchResponse"]


class SearchResponse(BaseModel):
    pagination: SearchPagination

    pending_analysis_count: int
    """
    Accessible current originals without a published analysis; includes unsupported
    or failed analyses.
    """

    results: List[SearchResult]

    search_truncated: bool
    """True when 1000 ranked chunks were examined.

    Narrow the query to examine other candidates.
    """
