# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .create_agent_run_input_param import CreateAgentRunInputParam

__all__ = ["AgentCreateRunParams"]


class AgentCreateRunParams(TypedDict, total=False):
    input: Required[CreateAgentRunInputParam]
    """Agent run input.

    `legacy_full` accepts a complete AG-UI history; `delta_v1` accepts only the
    newest user turn and lets the server rebuild a bounded rolling context.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
