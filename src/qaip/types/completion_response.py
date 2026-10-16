# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.content import Content

__all__ = [
    "CompletionResponse",
    "Choice",
    "ChoiceMessage",
    "ChoiceWebCitation",
    "RedactedInput",
    "RedactedInputMessage",
]


class ChoiceMessage(BaseModel):
    content: str
    """The content of the message"""

    role: Literal["assistant"]
    """The role of the message sender"""


class ChoiceWebCitation(BaseModel):
    """A web source returned by Gemini's Google Search grounding.

    Distinct from Content (internal knowledge base citations); surfaced separately so clients can render web references apart from internal document citations.
    """

    title: str
    """Title of the grounded web source"""

    url: str
    """URL of the grounded web source"""


class Choice(BaseModel):
    finish_reason: str
    """The reason why the model stopped generating tokens"""

    index: int
    """The index of this completion choice"""

    message: ChoiceMessage

    citations: Optional[List[Content]] = None
    """Array of search results"""

    search_suggestion: Optional[str] = None
    """
    Google Search Suggestions HTML (searchEntryPoint.renderedContent) from Gemini
    grounding. Per Google's "Grounding with Google Search" terms, clients MUST
    display this content as provided whenever it is present. Present only when
    grounding produced search suggestions.
    """

    web_citations: Optional[List[ChoiceWebCitation]] = None
    """
    Web sources from Gemini's Google Search grounding, returned separately from
    `citations`. Present only when grounding was enabled and the model used web
    results.
    """

    web_search_queries: Optional[List[str]] = None
    """The Google Search queries Gemini issued for grounding.

    Present only when grounding was used.
    """


class RedactedInputMessage(BaseModel):
    """The redacted message. Omitted or `null` when `status` is `skipped`."""

    index: int
    """Position of the message in the conversation passed to the model.

    For a `POST /completions` continuation the server rebuilds the earlier turns
    from the stored history, so this counts those turns too.
    """

    id: Optional[str] = None
    """Message id. Omitted or `null` for `POST /completions`."""

    content: Optional[str] = None
    """The redacted message text.

    For an Agent run with content parts, the text parts are joined. Omitted when the
    redacted text is too large to carry in one event (over 256 KiB encoded);
    `masked_counts` is still returned then.
    """


class RedactedInput(BaseModel):
    """How the end-user's latest message was redacted under the redaction policy.

    It is the
    redaction result, not a record of what was sent out. Only the latest `user` message is covered; earlier turns were returned with
    their own responses. Retrieved chunks and other boundaries are never included, and
    the unredacted text is not returned, since the caller already has it.
    """

    boundary: Literal[
        "initial_input",
        "initial_input_system",
        "initial_input_assistant",
        "rag_query",
        "rag_result",
        "google_query",
        "google_result",
        "tool_result",
        "external_table_result",
        "x_query",
        "xai_query",
        "chartmetric_query",
        "chartmetric_result",
        "completions_messages",
        "completions_messages_system",
        "completions_messages_assistant",
        "completions_query",
        "completions_docs",
    ]
    """A point where data leaves QAIP for an external provider.

    `initial_input`, `initial_input_system`, `initial_input_assistant`, `rag_query`,
    `rag_result`, `google_query`, `google_result`, `tool_result`,
    `external_table_result`, `x_query`, `xai_query`, `chartmetric_query` and
    `chartmetric_result` belong to Agent runs; `completions_messages`,
    `completions_messages_system`, `completions_messages_assistant`,
    `completions_query` and `completions_docs` belong to `POST /completions`. The
    conversation history is split by role: `*_system` covers `system` messages,
    `*_assistant` covers `assistant` messages (including their tool call arguments),
    and `initial_input` / `completions_messages` cover every other role.
    """

    status: Literal["succeeded", "skipped"]
    """`succeeded` means the message was redacted.

    `skipped` means the policy excludes this boundary (`skippedBoundaries`), so the
    message itself was not redacted; neither `masked_counts` nor `message` is
    returned then. Other boundaries, such as `completions_query` for the retrieval
    query, follow their own policy setting and are not reported here.
    """

    masked_counts: Optional[Dict[str, int]] = None
    """
    Number of masks applied to the message text per category code (`N` name, `T`
    phone number, `E` email address, `A` address, `I` ID, `C` card number, `P`
    personal information, `K` credential, `B` business confidential). One mask
    counts once. Omitted or `null` when `status` is `skipped`.
    """

    message: Optional[RedactedInputMessage] = None
    """The redacted message. Omitted or `null` when `status` is `skipped`."""


class CompletionResponse(BaseModel):
    choices: List[Choice]
    """The completion choices generated by the model"""

    created: int
    """The Unix timestamp (in seconds) of when the completion was created"""

    assistant_message_id: Optional[str] = None
    """Id of the persisted assistant message node (the new active leaf).

    Null when no assistant node was persisted.
    """

    conversation_id: Optional[str] = None
    """Target conversation id.

    For an existing conversation (conversation_id was supplied) it is always
    returned, even if this turn's answer was not persisted. For a new conversation
    it is null when nothing was persisted (e.g. no answer generated, or the history
    write failed).
    """

    redacted_input: Optional[RedactedInput] = None
    """How the end-user's latest message was redacted under the redaction policy.

    It is the redaction result, not a record of what was sent out. Only the latest
    `user` message is covered; earlier turns were returned with their own responses.
    Retrieved chunks and other boundaries are never included, and the unredacted
    text is not returned, since the caller already has it.
    """

    retrieved: Optional[List[Content]] = None
    """
    Every knowledge-base chunk retrieved for this request and passed to the model as
    context (after authorization filtering), in retrieval order, whether or not the
    answer cited it. Null unless the request set `include_retrieved: true`; an empty
    array means nothing was retrieved.
    """

    user_message_id: Optional[str] = None
    """Id of the persisted user message node for this turn.

    Null when the turn was not persisted.
    """
