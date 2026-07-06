# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .shared.file_type import FileType
from .shared.source_type import SourceType
from .shared.message_role import MessageRole
from .shared.logical_operator import LogicalOperator

__all__ = ["ClientCompletionParams", "Message"]


class ClientCompletionParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """The messages to generate completion for"""

    authz_policy: str
    """
    (reserved for future use) Name of the registered authz policy to evaluate when
    retrieving context. Defaults to the reserved "default" policy when omitted.
    Ignored when authz is disabled.
    """

    chunk_metadata: "MetadataFilterGroup"
    """Filter by chunk-level metadata from chunk_metadatas table"""

    citation: bool
    """Whether to include citations in the response"""

    conversation_id: str
    """Conversation to append this turn to.

    When omitted, a new conversation is created server-side and its id is returned
    (response body for JSON, the X-Conversation-Id header for streaming). Pass it
    back on subsequent turns so the answer is persisted into the same conversation
    history tree. When set, the past conversation is rebuilt server-side from the
    stored tree, so only the latest user message in `messages` is used as the new
    input (earlier `messages` entries are ignored). Retrieval uses that latest
    question.
    """

    date_from: int
    """Start date for content search (Unix timestamp in seconds)"""

    date_to: int
    """End date for content search (Unix timestamp in seconds)"""

    domains: SequenceNotStr[str]
    """Array of domains to search within (supports partial matching)"""

    file_types: List[FileType]

    grounding: bool
    """Whether to enable Gemini's Google Search grounding during answer generation.

    Only effective when the completion model is a Gemini model and the
    `gemini_grounding` feature is enabled on the server; otherwise this flag is
    ignored.
    """

    limit: int
    """Maximum number of chunks to retrieve as context for completion"""

    metadata: "MetadataFilterGroup"
    """(reserved for future use) Filter group with nested structure.

    Supports combining filters with AND/OR logic.
    """

    parent_message_id: str
    """
    Id of the message node to branch this turn from (the parent of the new user
    message). When omitted, the turn continues from the conversation's current
    active leaf. Set it to fork a branch (e.g. editing an earlier question). Must
    belong to conversation_id.
    """

    principal_id: str
    """Identifier of the end-user (principal) on whose behalf this request is made.

    Used to look up the principal's authz subject attributes for policy evaluation.
    When omitted, subject attributes are empty (most restrictive). Ignored when
    authz is disabled.
    """

    regenerate: bool
    """
    When true, the latest user message is NOT persisted again; instead a new
    assistant answer is created as a sibling under parent_message_id (which must
    reference an existing user message). Used to regenerate an answer.
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

    truncation: Literal["auto", "disabled"]
    """
    How to handle a reconstructed conversation that exceeds the model's context
    budget (only relevant when conversation_id is set, i.e. history is rebuilt
    server-side). "auto": drop the oldest turns until it fits (the latest question
    is always kept). "disabled": return 400 if it does not fit.
    """

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
