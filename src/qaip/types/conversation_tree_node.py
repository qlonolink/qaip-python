# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ConversationTreeNode"]


class ConversationTreeNode(BaseModel):
    id: str

    role: str

    created_at: Optional[datetime] = None

    parent_id: Optional[str] = None
