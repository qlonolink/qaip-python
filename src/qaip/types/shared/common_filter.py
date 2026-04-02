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

    source_metadata: Optional["MetadataFilterGroup"] = None
    """Filter by individual source/file metadata from source_metadatas table"""

    source_types: Optional[List[SourceType]] = None

    tag_filter_logic: Optional[LogicalOperator] = None
    """Logical operator for combining filter conditions"""

    tag_ids: Optional[List[str]] = None

    tags: Optional[List[str]] = None


from .metadata_filter_group import MetadataFilterGroup
