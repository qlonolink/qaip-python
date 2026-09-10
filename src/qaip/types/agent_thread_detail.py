# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .agent_run_node import AgentRunNode

__all__ = ["AgentThreadDetail"]


class AgentThreadDetail(BaseModel):
    runs: List[AgentRunNode]
    """All runs in the thread as a tree (via parent_run_id)."""

    thread_id: str
