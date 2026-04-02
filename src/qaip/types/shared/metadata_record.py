# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .metadata_type import MetadataType

__all__ = ["MetadataRecord"]


class MetadataRecord(BaseModel):
    key: str
    """Metadata key (max 20 characters)"""

    val: object
    """Metadata value (string max 50 characters, or number).

    Pass null to delete this key.
    """

    type: Optional[MetadataType] = None
    """Data type of the metadata value. Required when val is not null."""
