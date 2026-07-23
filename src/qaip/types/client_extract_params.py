# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .shared.file_type import FileType
from .shared.source_type import SourceType
from .shared.logical_operator import LogicalOperator
from .shared_params.common_filter import CommonFilter

__all__ = ["ClientExtractParams", "RelatedFilter"]


class ClientExtractParams(TypedDict, total=False):
    schema: Required[object]
    """JSON Schema for the data to be extracted."""

    authz_policy: str
    """
    (reserved for future use) Name of the registered authz policy to evaluate when
    retrieving content. Defaults to the reserved "default" policy when omitted.
    Ignored when authz is disabled.
    """

    chunk_metadata: "MetadataFilterGroup"
    """Filter by chunk-level metadata from chunk_metadatas table"""

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

    metadata_filter: "MetadataFilterGroup"
    """
    Filter by declared metadata columns (see /metadata_columns) pushed down directly
    to LanceDB (no PostgreSQL round-trip). Targets string/integer typed columns.
    Keys must be declared via /metadata_columns or the request is rejected (400).
    """

    offset: int

    principal_id: str
    """Identifier of the end-user (principal) on whose behalf this request is made.

    Used to look up the principal's authz subject attributes for policy evaluation.
    When omitted, subject attributes are empty (most restrictive). Ignored when
    authz is disabled.
    """

    prompt: str
    """
    Additional prompt for the LLM (optional, if not specified, a default prompt in
    Japanese will be used).
    """

    related_filter: RelatedFilter

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

    use_related: bool
    """Whether to search for and use related content"""


class RelatedFilter(CommonFilter, total=False):
    limit: int

    offset: int


from .shared_params.metadata_filter_group import MetadataFilterGroup
