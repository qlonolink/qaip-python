# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .shared.file_type import FileType
from .shared.source_type import SourceType
from .shared.message_role import MessageRole
from .shared.logical_operator import LogicalOperator

__all__ = ["ClientCompletionParams", "Message"]


class ClientCompletionParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """The messages to generate completion for"""

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

    limit: int
    """Maximum number of chunks to retrieve as context for completion"""

    metadata: "MetadataFilterGroup"
    """(reserved for future use) Filter group with nested structure.

    Supports combining filters with AND/OR logic.
    """

    source_metadata: "MetadataFilterGroup"
    """Filter by individual source/file metadata from source_metadatas table"""

    source_types: List[SourceType]

    stream: bool
    """Whether to stream the response.

    If true, the response is sent as a stream using the 'text/plain' content type.
    """

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


class Message(TypedDict, total=False):
    content: Required[str]
    """The content of the message"""

    role: Required[MessageRole]
    """The role of the message sender"""


from .shared_params.metadata_filter_group import MetadataFilterGroup
