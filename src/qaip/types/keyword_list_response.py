# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .keyword import Keyword
from .._models import BaseModel

__all__ = ["KeywordListResponse"]


class KeywordListResponse(BaseModel):
    keywords: List[Keyword]
    """The list of keywords"""

    total: int
    """Total number of keywords"""
