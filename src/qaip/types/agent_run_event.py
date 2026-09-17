# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AgentRunEvent"]


class AgentRunEvent(BaseModel):
    """Durable AG-UI event.

    Newly finalized RUN_ERROR payloads include code, message, request_id, object-valued details, and retryable=false. The request_id identifies the original run creation, not the request fetching or replaying events; it is null when the original correlation ID is unknown. Error details are empty and upstream correlation/retry metadata is not trusted. Previously stored events are replayed unchanged and may not contain these fields. Clients must not automatically repeat a failed run because partial output or side effects may already exist.
    """

    index: int

    payload: str

    created_at: Optional[datetime] = None

    event_type: Optional[str] = None
