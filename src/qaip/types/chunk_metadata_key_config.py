# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .shared.metadata_type import MetadataType

__all__ = ["ChunkMetadataKeyConfig"]


class ChunkMetadataKeyConfig(BaseModel):
    key: str
    """Metadata key name"""

    type: MetadataType
    """Data type of the metadata value"""
