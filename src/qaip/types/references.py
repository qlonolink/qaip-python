# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .reference_entry import ReferenceEntry

__all__ = ["References"]


class References(BaseModel):
    file_id: str
    """Canonical lowercase nonzero UUID."""

    recorded: bool

    references: List[ReferenceEntry]

    revision_id: str
    """Canonical lowercase nonzero UUID."""
