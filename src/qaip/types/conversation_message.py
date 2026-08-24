# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.content import Content

__all__ = ["ConversationMessage"]


class ConversationMessage(BaseModel):
    content: str

    id: str

    role: str

    assistant_metadata: Optional[Dict[str, object]] = None

    citations: Optional[List[Content]] = None

    created_at: Optional[datetime] = None

    filter_snapshot: Optional[Dict[str, object]] = None

    parent_id: Optional[str] = None
