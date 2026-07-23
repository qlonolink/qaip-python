# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from .file_type import FileType
from .source_type import SourceType
from .logical_operator import LogicalOperator

__all__ = ["CommonFilter"]


class CommonFilter(BaseModel):
    chunk_metadata: Optional["MetadataFilterGroup"] = None
    """Filter by chunk-level metadata from chunk_metadatas table"""

    date_from: Optional[int] = None
    """Start date for content search (Unix timestamp in seconds)"""

    date_to: Optional[int] = None
    """End date for content search (Unix timestamp in seconds)"""

    domains: Optional[List[str]] = None

    file_types: Optional[List[FileType]] = None

    metadata: Optional["MetadataFilterGroup"] = None
    """(reserved for future use) Filter group with nested structure.

    Supports combining filters with AND/OR logic.
    """

    metadata_filter: Optional["MetadataFilterGroup"] = None
    """
    Filter by declared metadata columns (see /metadata_columns) pushed down directly
    to LanceDB (no PostgreSQL round-trip). Targets string/integer typed columns.
    Keys must be declared via /metadata_columns or the request is rejected (400).
    """

    source_metadata: Optional["MetadataFilterGroup"] = None
    """Filter by individual source/file metadata from source_metadatas table"""

    source_types: Optional[List[SourceType]] = None

    tag_filter_logic: Optional[LogicalOperator] = None
    """Logical operator for combining filter conditions"""

    tag_ids: Optional[List[str]] = None

    tags: Optional[List[str]] = None

    use_postfilter: Optional[bool] = None
    """
    Whether to bypass LanceDB prefilter and apply WHERE after the vector search
    (IVF_PQ) returns top-K. Significantly faster for broad filters that cover most
    of the table, but may return fewer than `limit` results when the hit rate is
    low.
    """


from .metadata_filter_group import MetadataFilterGroup
