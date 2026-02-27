# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .shared.file_type import FileType
from .shared.source_type import SourceType

__all__ = ["ClientExtractParams"]


class ClientExtractParams(TypedDict, total=False):
    schema: Required[object]
    """JSON Schema for the data to be extracted."""

    date_from: int
    """Start date for content search (Unix timestamp in seconds)"""

    date_to: int
    """End date for content search (Unix timestamp in seconds)"""

    domains: SequenceNotStr[str]

    file_types: List[FileType]

    limit: int

    metadata: "MetadataFilterGroup"
    """(reserved for future use) Filter group with nested structure.

    Supports combining filters with AND/OR logic.
    """

    offset: int

    prompt: str
    """
    Additional prompt for the LLM (optional, if not specified, a default prompt in
    Japanese will be used).
    """

    source_metadata: "MetadataFilterGroup"
    """Filter by individual source/file metadata from source_metadatas table"""

    source_types: List[SourceType]

    tag_filter_logic: Literal["AND", "OR"]
    """Logical operator for combining filter conditions"""

    tag_ids: SequenceNotStr[str]

    tags: SequenceNotStr[str]


from .shared_params.metadata_filter_group import MetadataFilterGroup
