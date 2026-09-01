# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .create_agent_run_input_param import CreateAgentRunInputParam

__all__ = ["AgentCreateRunParams"]


class AgentCreateRunParams(TypedDict, total=False):
    input: Required[CreateAgentRunInputParam]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
