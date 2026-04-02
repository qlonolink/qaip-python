# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Pagination"]


class Pagination(BaseModel):
    has_more: bool
    """Whether there are more items after this page"""

    limit: int
    """Maximum number of items per page"""

    next_id: Optional[str] = None
    """ID to pass as after_id for next page (null if has_more=false)"""

    total: Optional[int] = None
    """Total number of items"""
