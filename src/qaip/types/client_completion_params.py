# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
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

    include_redacted_input: bool
    """
    Whether to return how the latest user message was redacted (see
    `RedactedInput`), e.g. to show the end-user their question in redacted form. The
    messages are redacted first, and both the retrieval query and the LLM prompt are
    built from the redacted text. Only effective with `redaction_policy_id`. The
    JSON response carries it in the top-level `redacted_input`; the SSE stream emits
    one CUSTOM event named `redaction_applied` as soon as the messages are redacted,
    before the search and the answer text. The text/plain stream cannot carry it,
    and it is not stored in the conversation history.
    """

    include_retrieved: bool
    """
    Whether to return, separately from `citations`, every knowledge-base chunk that
    was retrieved for this request and passed to the model as context (after
    authorization filtering), whether or not the answer cited it. When true, the
    JSON response carries them in the top-level `retrieved` array, the SSE stream
    emits one or more CUSTOM events named `retrieved` before RUN_FINISHED (split by
    encoded size; concatenate their values in order to get the full list), and the
    persisted assistant message keeps them in `assistant_metadata.retrieved` (see
    GET /conversations). The text/plain stream cannot carry them in the body, so it
    only persists them. Intended for callers that audit what the end-user was shown;
    off by default so the response size and stored history of existing clients do
    not change.
    """

    limit: int
    """Maximum number of chunks to retrieve as context for completion"""

    metadata: "MetadataFilterGroup"
    """(reserved for future use) Filter group with nested structure.

    Supports combining filters with AND/OR logic.
    """

    metadata_filter: "MetadataFilterGroup"
    """
    Filter by declared metadata columns (see /metadata_columns) pushed down directly
    to LanceDB (no PostgreSQL round-trip). Targets string/integer/string_list
    /integer_list typed columns. Keys must be declared via /metadata_columns or the
    request is rejected (400).
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

    redaction_policy_id: Optional[str]
    """
    ID of a versioned redaction policy (built-in, or a tenant policy name) to apply
    before anything leaves QAIP for an external provider: the retrieval query sent
    to the embedding API, the retrieved knowledge-base chunks (title / URL / text)
    and the conversation `messages` sent to the LLM. The redaction boundaries are
    `completions_query`, `completions_docs`, `completions_messages`,
    `completions_messages_system` (the `system` role messages) and
    `completions_messages_assistant` (the `assistant` role messages); a policy can
    exclude some of them via `skippedBoundaries`. The `messages` are redacted first
    and the retrieval query is built from the redacted user messages, so
    `completions_query` only applies when the policy excludes
    `completions_messages`.

    When omitted or `null` (the default), **no redaction is performed and the input
    is sent to the external provider as-is**. This is an explicit API contract, not
    a fail-open behavior. Unknown IDs return `422 UNKNOWN_REDACTION_POLICY`; an
    unavailable redactor returns `503 REDACTION_UNAVAILABLE` and a redaction failure
    during generation returns `503 REDACTION_FAILED` (or `RUN_ERROR` with that code
    on the SSE stream). The request is never forwarded unmasked.

    Redacted chunks are also what `citations` and `retrieved` return, so citation
    links can break when the URL itself contains masked values. `grounding: true`
    may be combined with a policy: Gemini derives its search queries from the
    redacted messages, but QAIP cannot intercept the built-in grounding search
    itself, so the guarantee is weaker than the Agent run's explicit `google_query`
    / `google_result` boundaries.
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

    If true, the response is streamed as 'text/plain' by default, or as an ag-ui
    Server-Sent Events stream ('text/event-stream') when the request sends the
    header 'Accept: text/event-stream'.
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
