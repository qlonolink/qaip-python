# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .agent_run import AgentRun

__all__ = ["AgentRetrieveRunResultResponse"]


class AgentRetrieveRunResultResponse(BaseModel):
    run: AgentRun

    error: Optional[Dict[str, object]] = None

    result: Optional[Dict[str, object]] = None
