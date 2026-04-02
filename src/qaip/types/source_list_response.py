# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .source import Source
from .._models import BaseModel
from .shared.pagination import Pagination

__all__ = ["SourceListResponse"]


class SourceListResponse(BaseModel):
    pagination: Pagination

    sources: List[Source]
