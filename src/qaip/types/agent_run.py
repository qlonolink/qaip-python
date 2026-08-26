# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .agent_provider import AgentProvider
from .agent_run_status import AgentRunStatus
from .agent_execution_mode import AgentExecutionMode

__all__ = ["AgentRun"]


class AgentRun(BaseModel):
    context_start_run_id: Optional[str] = None
    """
    Oldest run included in the reconstructed rolling context, or null when none was
    needed.
    """

    context_truncated: bool
    """Whether older turns were omitted to stay within the server context budget."""

    execution_mode: AgentExecutionMode

    input_history_mode: Literal["legacy_full", "delta_v1"]
    """How the request supplied conversation history for this run."""

    provider: AgentProvider

    run_id: str

    status: AgentRunStatus
    """Agent run lifecycle state."""

    thread_id: str

    workflow_type: str

    created_at: Optional[datetime] = None

    error: Optional[Dict[str, object]] = None

    finished_at: Optional[datetime] = None

    idempotency_key: Optional[str] = None

    input: Optional[Dict[str, object]] = None
    """Server-enriched agent input used to reconstruct the thread transcript."""

    mcp_session_id: Optional[str] = None

    parent_run_id: Optional[str] = None
    """Run this run branched from within the thread (null for the thread root)."""

    result: Optional[Dict[str, object]] = None

    runtime_arn: Optional[str] = None

    started_at: Optional[datetime] = None

    trace_id: Optional[str] = None
    """
    保存済み W3C trace context から導出した lowercase OpenTelemetry trace ID。移行前
    の行は null。
    """
