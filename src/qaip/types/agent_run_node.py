# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .agent_run_status import AgentRunStatus

__all__ = ["AgentRunNode"]


class AgentRunNode(BaseModel):
    run_id: str

    status: AgentRunStatus

    created_at: Optional[datetime] = None

    parent_run_id: Optional[str] = None

    title: Optional[str] = None
