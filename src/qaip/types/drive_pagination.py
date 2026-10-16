# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DrivePagination"]


class DrivePagination(BaseModel):
    has_more: bool

    next_id: Optional[str] = None
    """Server-provided cursor; null on the last page."""
