# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .agent_provider import AgentProvider
from .agent_run_status import AgentRunStatus
from .agent_execution_mode import AgentExecutionMode

__all__ = ["AgentRun"]


class AgentRun(BaseModel):
    execution_mode: AgentExecutionMode

    provider: AgentProvider

    run_id: str

    status: AgentRunStatus
    """Agent run status. Values are QUEUED, RUNNING, SUCCEEDED, FAILED, or CANCELLED."""

    workflow_type: str

    created_at: Optional[datetime] = None

    error: Optional[Dict[str, object]] = None

    finished_at: Optional[datetime] = None

    idempotency_key: Optional[str] = None

    input: Optional[Dict[str, object]] = None
    """Original RunAgentInput. Used to reconstruct a thread's transcript on restore."""

    mcp_session_id: Optional[str] = None

    parent_run_id: Optional[str] = None
    """Run this run branched from within the thread (null for the thread root)."""

    result: Optional[Dict[str, object]] = None

    runtime_arn: Optional[str] = None

    runtime_session_id: Optional[str] = None

    started_at: Optional[datetime] = None

    thread_id: Optional[str] = None

    trace_id: Optional[str] = None
