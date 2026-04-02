# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .shared.file_type import FileType
from .shared.source_type import SourceType
from .shared.logical_operator import LogicalOperator

__all__ = ["AgentFiltersParam"]


class AgentFiltersParam(TypedDict, total=False):
    """Filters for agent search and completion"""

    chunk_metadata: "MetadataFilterGroup"
    """Filter by chunk-level metadata from chunk_metadatas table"""

    citation: bool
    """Whether to include citations in the response"""

    date_from: int
    """Start date for content search (Unix timestamp in seconds)"""

    date_to: int
    """End date for content search (Unix timestamp in seconds)"""

    domains: SequenceNotStr[str]
    """Array of domains to search within (supports partial matching)"""

    file_types: List[FileType]

    metadata: "MetadataFilterGroup"
    """(reserved for future use) Filter group with nested structure.

    Supports combining filters with AND/OR logic.
    """

    source_metadata: "MetadataFilterGroup"
    """Filter by individual source/file metadata from source_metadatas table"""

    source_types: List[SourceType]

    tag_filter_logic: LogicalOperator
    """Logical operator for combining filter conditions"""

    tag_ids: SequenceNotStr[str]
    """target tag IDs to be obtained"""

    tags: SequenceNotStr[str]
    """target tag names to be obtained"""


from .shared_params.metadata_filter_group import MetadataFilterGroup
