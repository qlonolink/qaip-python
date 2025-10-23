# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TagsResponse", "Tag"]


class Tag(BaseModel):
    id: str
    """Tag ID"""

    description: str
    """Tag description"""

    name: str
    """Tag name"""


class TagsResponse(BaseModel):
    tags: Optional[List[Tag]] = None
