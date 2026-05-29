# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from ..._types import SequenceNotStr
from ..shared.file_type import FileType
from ..shared.source_type import SourceType
from ..shared.logical_operator import LogicalOperator

__all__ = ["CommonFilter"]


class CommonFilter(TypedDict, total=False):
    chunk_metadata: "MetadataFilterGroup"
    """Filter by chunk-level metadata from chunk_metadatas table"""

    date_from: int
    """Start date for content search (Unix timestamp in seconds)"""

    date_to: int
    """End date for content search (Unix timestamp in seconds)"""

    domains: SequenceNotStr[str]

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

    tags: SequenceNotStr[str]

    use_postfilter: bool
    """
    Whether to bypass LanceDB prefilter and apply WHERE after the vector search
    (IVF_PQ) returns top-K. Significantly faster for broad filters that cover most
    of the table, but may return fewer than `limit` results when the hit rate is
    low.
    """


from .metadata_filter_group import MetadataFilterGroup
