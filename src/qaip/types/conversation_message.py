# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.content import Content

__all__ = ["ConversationMessage"]


class ConversationMessage(BaseModel):
    id: str

    content: str

    role: str
    """user | assistant"""

    assistant_metadata: Optional[Dict[str, object]] = None
    """
    Non-streaming assistant extras captured verbatim (finish_reason, grounding
    web_citations / search_suggestion / web_search_queries, etc.). When the turn was
    requested with `include_retrieved: true`, `retrieved` holds every knowledge-base
    chunk passed to the model (same shape as `citations`), for both streaming and
    non-streaming turns.
    """

    citations: Optional[List[Content]] = None

    created_at: Optional[datetime] = None

    filter_snapshot: Optional[Dict[str, object]] = None
    """Retrieval/filter snapshot for this turn (user messages)."""

    parent_id: Optional[str] = None
