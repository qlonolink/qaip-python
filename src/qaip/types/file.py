# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    id: str
    """Canonical lowercase nonzero UUID."""

    current_revision_id: Optional[str] = None
    """Canonical lowercase nonzero UUID."""

    folder_id: Optional[str] = None
    """Canonical lowercase nonzero UUID."""

    generation: int

    media_type: str

    name: str
    """Nonblank file or folder name; no slash, backslash, control characters, .

    or .. .
    """

    restore_until: Optional[datetime] = None

    sha256: str

    size_bytes: int

    trashed_at: Optional[datetime] = None

    updated_at: datetime
