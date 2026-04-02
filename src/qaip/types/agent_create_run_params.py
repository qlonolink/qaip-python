# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .agent_message_param import AgentMessageParam

__all__ = ["AgentCreateRunParams", "Input", "InputForwardedProps"]


class AgentCreateRunParams(TypedDict, total=False):
    input: Required[Input]

    idempotency_key: str
    """Optional idempotency key for reusing an existing asynchronous run."""


class InputForwardedProps(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Forwarded properties for the run (AG-UI standard)"""

    filters: "AgentFiltersParam"
    """Filters for agent search and completion"""


class Input(TypedDict, total=False):
    forwarded_props: Annotated[InputForwardedProps, PropertyInfo(alias="forwardedProps")]
    """Forwarded properties for the run (AG-UI standard)"""

    messages: Iterable[AgentMessageParam]

    run_id: str
    """Optional ID for the run"""

    thread_id: str
    """Optional ID for the thread"""


from .agent_filters_param import AgentFiltersParam
