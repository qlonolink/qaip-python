# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["Display"]


class Display(BaseModel):
    id: str
    """Canonical lowercase nonzero UUID."""

    created_at: datetime

    file_id: str
    """Canonical lowercase nonzero UUID."""

    page_count: int

    revision_id: str
    """Canonical lowercase nonzero UUID."""
