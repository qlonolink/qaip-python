# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.tag import Tag

__all__ = ["TagsResponse"]


class TagsResponse(BaseModel):
    tags: Optional[List[Tag]] = None
