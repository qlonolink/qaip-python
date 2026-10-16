# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AvailableReferenceSource"]


class AvailableReferenceSource(BaseModel):
    file_id: str
    """Canonical lowercase nonzero UUID."""

    name: str

    revision_id: str
    """Canonical lowercase nonzero UUID."""

    display_revision_id: Optional[str] = None
    """Canonical lowercase nonzero UUID."""

    page_id: Optional[str] = None
    """Canonical lowercase nonzero UUID."""
