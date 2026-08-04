# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .agent_message_param import AgentMessageParam

__all__ = ["AgentRunParams", "ForwardedProps"]


class AgentRunParams(TypedDict, total=False):
    forwarded_props: Annotated[ForwardedProps, PropertyInfo(alias="forwardedProps")]
    """Forwarded properties for the run (AG-UI standard)"""

    messages: Iterable[AgentMessageParam]

    redaction_policy_id: Annotated[Optional[str], PropertyInfo(alias="redactionPolicyId")]
    """
    ID of a versioned redaction policy to apply before sending the conversation to
    the external model / embedding provider.

    When omitted or `null` (the default), **no redaction is performed and the input
    is sent to the external provider as-is**. This is an explicit API contract, not
    a fail-open behavior: omitting the field never silently sanitizes the input.

    When a known ID is given, the conversation history (all roles, string/array/dict
    content, tool call arguments, string metadata and source URLs), RAG search query
    and results, Google web search query and results, external table results, and
    all other tool results are masked with that policy before they reach the
    corresponding external model or embedding provider. The original text is still
    stored in `agent_runs.input` and emitted in `RUN_STARTED` for UI display; only
    the copy sent to the external provider is masked. Restoration mappings are never
    stored.

    Errors:

    - unknown ID or an empty string: `422` (never interpreted as "no redaction")
    - combined with the AgentCore execution mode:
      `422 AGENTCORE_REDACTION_UNSUPPORTED`
    - redactor unavailable / timeout / failure: `503 REDACTION_UNAVAILABLE` before
      the run starts, or a `RUN_ERROR` with code `REDACTION_FAILED` during the run.
      The request is never forwarded unmasked as a fallback.

    A parent run's policy is not inherited: a child run is redacted only when it
    specifies `redactionPolicyId` itself.
    """

    run_id: str
    """Optional ID for the run"""

    thread_id: str
    """Optional ID for the thread"""


class ForwardedProps(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """Forwarded properties for the run (AG-UI standard)"""

    authz_policy: str
    """
    (reserved for future use) Name of the registered authz policy to evaluate when
    the agent retrieves context. Defaults to the reserved "default" policy when
    omitted. Ignored when authz is disabled.
    """

    filters: "AgentFiltersParam"
    """Filters for agent search and completion"""

    grounding: bool
    """Whether to enable Gemini's Google Search grounding during the agent run.

    Only effective when the agent model is a Gemini model and the `gemini_grounding`
    feature is enabled on the server; otherwise this flag is ignored. Mirrors the
    `/completions` `grounding` parameter.
    """

    principal_id: str
    """Identifier of the end-user (principal) on whose behalf this request is made.

    Used to look up the principal's authz subject attributes for policy evaluation.
    When omitted, subject attributes are empty (most restrictive). Ignored when
    authz is disabled.
    """


from .agent_filters_param import AgentFiltersParam
