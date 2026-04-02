# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .notion import Notion
from .._models import BaseModel
from .shared.pagination import Pagination

__all__ = ["NotionListResponse"]


class NotionListResponse(BaseModel):
    notions: List[Notion]

    pagination: Pagination
