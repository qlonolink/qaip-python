# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .content import Content
from .._models import BaseModel

__all__ = ["SearchQueryResponse"]


class SearchQueryResponse(BaseModel):
    id: str
    """A unique identifier for the search request"""

    created: int
    """The Unix timestamp (in seconds) of when the search was performed"""

    results: List[Content]
    """Array of search results"""
