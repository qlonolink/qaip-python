# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .agent_message_param import AgentMessageParam

__all__ = ["AgentRunParams", "ForwardedProps"]


class AgentRunParams(TypedDict, total=False):
    forwarded_props: Annotated[ForwardedProps, PropertyInfo(alias="forwardedProps")]
    """Forwarded properties for the run (AG-UI standard)"""

    messages: Iterable[AgentMessageParam]

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
