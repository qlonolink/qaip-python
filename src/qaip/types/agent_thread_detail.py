# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .agent_run_node import AgentRunNode

__all__ = ["AgentThreadDetail"]


class AgentThreadDetail(BaseModel):
    runs: List[AgentRunNode]

    thread_id: str
