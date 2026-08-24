# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .agent_run_status import AgentRunStatus

__all__ = ["AgentThread"]


class AgentThread(BaseModel):
    latest_run_id: str

    status: AgentRunStatus

    thread_id: str

    principal_id: Optional[str] = None

    run_count: Optional[int] = None

    title: Optional[str] = None

    updated_at: Optional[datetime] = None
