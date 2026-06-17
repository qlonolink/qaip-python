# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .shared.file_type import FileType
from .shared.source_type import SourceType
from .shared.logical_operator import LogicalOperator

__all__ = ["ClientSearchParams"]


class ClientSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search query string"""

    authz_policy: str
    """
    (reserved for future use) Name of the registered authz policy to evaluate for
    this request. Defaults to the reserved "default" policy when omitted. Ignored
    when authz is disabled. An unknown or malformed name returns 400.
    """

    chunk_metadata: "MetadataFilterGroup"
    """Filter by chunk-level metadata from chunk_metadatas table"""

    date_from: int
    """Start date for content search (Unix timestamp in seconds)"""

    date_to: int
    """End date for content search (Unix timestamp in seconds)"""

    domains: SequenceNotStr[str]
    """Array of domains to search within (supports partial matching)"""

    file_types: List[FileType]

    limit: int
    """Maximum number of results to return"""

    metadata: "MetadataFilterGroup"
    """(reserved for future use) Filter group with nested structure.

    Supports combining filters with AND/OR logic.
    """

    metadata_filter: "MetadataFilterGroup"
    """
    Filter by declared metadata columns (see /metadata_columns) pushed down directly
    to LanceDB (no PostgreSQL round-trip). Targets string/integer typed columns.
    Keys must be declared via /metadata_columns or the request is rejected (400).
    """

    offset: int
    """Number of results to skip"""

    principal_id: str
    """Identifier of the end-user (principal) on whose behalf this request is made.

    Used to look up the principal's authz subject attributes for policy evaluation.
    When omitted, subject attributes are empty (most restrictive). Ignored when
    authz is disabled.
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

    use_postfilter: bool
    """
    Whether to bypass LanceDB prefilter and apply WHERE after the vector search
    (IVF_PQ) returns top-K. Significantly faster for broad filters that cover most
    of the table, but may return fewer than `limit` results when the hit rate is
    low.
    """


from .shared_params.metadata_filter_group import MetadataFilterGroup
