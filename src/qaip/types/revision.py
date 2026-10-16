# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Revision"]


class Revision(BaseModel):
    id: str
    """Canonical lowercase nonzero UUID."""

    created_at: datetime

    file_id: str
    """Canonical lowercase nonzero UUID."""

    media_type: str
    """Valid MIME media type without parameters."""

    restored_from_id: Optional[str] = None
    """Canonical lowercase nonzero UUID."""

    sha256: str

    size_bytes: int
