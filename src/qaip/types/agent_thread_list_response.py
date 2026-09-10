# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .agent_thread import AgentThread

__all__ = ["AgentThreadListResponse"]


class AgentThreadListResponse(BaseModel):
    threads: List[AgentThread]
