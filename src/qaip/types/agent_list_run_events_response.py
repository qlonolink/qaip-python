# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .agent_run import AgentRun
from .agent_run_event import AgentRunEvent

__all__ = ["AgentListRunEventsResponse"]


class AgentListRunEventsResponse(BaseModel):
    events: List[AgentRunEvent]

    next_index: int

    run: AgentRun
