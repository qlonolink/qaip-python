# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .local_file_group import LocalFileGroup
from .shared.pagination import Pagination

__all__ = ["LocalFileGroupListResponse"]


class LocalFileGroupListResponse(BaseModel):
    local_file_groups: List[LocalFileGroup]

    pagination: Pagination
