# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AgentRunEvent"]


class AgentRunEvent(BaseModel):
    index: int

    payload: str

    created_at: Optional[datetime] = None

    event_type: Optional[str] = None
