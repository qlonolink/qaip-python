# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .source_group import SourceGroup
from .shared.pagination import Pagination

__all__ = ["SourceGroupListResponse"]


class SourceGroupListResponse(BaseModel):
    pagination: Pagination

    source_groups: List[SourceGroup]
