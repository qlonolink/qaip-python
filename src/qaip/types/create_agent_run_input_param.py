# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CreateAgentRunInputParam"]


class CreateAgentRunInputParam(TypedDict, total=False):
    context: Iterable[Dict[str, object]]

    forwarded_props: Annotated[Dict[str, object], PropertyInfo(alias="forwardedProps")]
    """AG-UI extension properties forwarded to the run.

    This remains a free-form object because AG-UI clients and server-side
    integrations may add extension keys. Known QAIP keys include `filters`,
    `authz_policy`, `principal_id`, `grounding`, and `retrieval_mode`; their values
    are validated by the run service before use.

    `retrieval_mode` controls only the built-in QAIP knowledge-base `search` tool.
    Its accepted values are `required` (the default when omitted) and `disabled`. In
    `disabled` mode the tool and its retrieval/citation system instructions are both
    omitted. It does not disable explicitly configured external-table tools or
    Google grounding.
    """

    messages: Iterable[Dict[str, object]]

    parent_run_id: Annotated[str, PropertyInfo(alias="parentRunId")]
    """Server-issued run ID to branch from.

    Its thread must match threadId when both are supplied.
    """

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
    - used on a deployment whose AgentCore runtime has no redactor wired up:
      `422 AGENTCORE_REDACTION_UNSUPPORTED`. Where the wiring is in place, the
      AgentCore execution mode applies the same redaction as the local mode
    - redactor unavailable / timeout / failure: `503 REDACTION_UNAVAILABLE` before
      the run starts, or a `RUN_ERROR` with code `REDACTION_FAILED` during the run.
      The request is never forwarded unmasked as a fallback.
    - concurrent redaction runs saturated in the AgentCore execution mode:
      `503 REDACTION_CAPACITY_EXCEEDED` before the run starts. Each run executes in
      its own microVM, so the per-process concurrency limit cannot bound the load on
      the shared redactor; the number of concurrent policy-bearing runs is capped
      instead. Retrying later succeeds.

    A parent run's policy is not inherited: a child run is redacted only when it
    specifies `redactionPolicyId` itself.
    """

    resume: Optional[Iterable[Dict[str, object]]]

    state: Optional[Dict[str, object]]
    """AG-UI state supplied to the run."""

    thread_id: Annotated[str, PropertyInfo(alias="threadId")]
    """Server-issued thread ID to continue. Omit to create a new thread."""

    tools: Iterable[Dict[str, object]]
