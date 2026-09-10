# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .agent_run_status import AgentRunStatus

__all__ = ["AgentThread"]


class AgentThread(BaseModel):
    agent_id: Optional[str] = None
    """Agent that owns the thread. Legacy rows may return null."""

    current_run_id: Optional[str] = None
    """Authoritative continuation cursor for `delta_v1`.

    Send this value as `baseRunId`; legacy rows that have not been classified may
    return null.
    """

    latest_run_id: str
    """Most recently created run; not an authoritative continuation cursor."""

    status: AgentRunStatus
    """Agent run lifecycle state."""

    thread_id: str

    principal_id: Optional[str] = None
    """Authorization principal this thread belongs to (null if not set)."""

    run_count: Optional[int] = None

    title: Optional[str] = None

    updated_at: Optional[datetime] = None
