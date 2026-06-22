# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["UserKeywordSnapshot"]


class UserKeywordSnapshot(BaseModel):
    snapshot: List[object]
    """The user's keyword snapshot as a list of keyword entries"""

    user_id: str
    """The ID of the user the snapshot belongs to"""
