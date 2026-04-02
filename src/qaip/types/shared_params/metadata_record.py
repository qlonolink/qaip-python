# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..shared.metadata_type import MetadataType

__all__ = ["MetadataRecord"]


class MetadataRecord(TypedDict, total=False):
    key: Required[str]
    """Metadata key (max 20 characters)"""

    val: Required[object]
    """Metadata value (string max 50 characters, or number).

    Pass null to delete this key.
    """

    type: MetadataType
    """Data type of the metadata value. Required when val is not null."""
