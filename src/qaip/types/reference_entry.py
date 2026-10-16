# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .available_reference_source import AvailableReferenceSource

__all__ = ["ReferenceEntry"]


class ReferenceEntry(BaseModel):
    """
    source is present only when status=available; unavailable does not disclose source identity.
    """

    ordinal: int

    status: Literal["available", "unavailable"]

    source: Optional[AvailableReferenceSource] = None
