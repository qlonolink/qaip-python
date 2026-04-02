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


class ForwardedProps(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Forwarded properties for the run (AG-UI standard)"""

    filters: "AgentFiltersParam"
    """Filters for agent search and completion"""


from .agent_filters_param import AgentFiltersParam
