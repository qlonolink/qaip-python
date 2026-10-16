# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Folder"]


class Folder(BaseModel):
    id: str
    """Canonical lowercase nonzero UUID."""

    created_at: datetime

    generation: int

    name: str
    """Nonblank file or folder name; no slash, backslash, control characters, .

    or .. .
    """

    parent_id: Optional[str] = None
    """Canonical lowercase nonzero UUID."""
