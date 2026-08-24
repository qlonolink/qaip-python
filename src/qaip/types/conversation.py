# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Conversation"]


class Conversation(BaseModel):
    id: str

    created_at: Optional[datetime] = None

    current_leaf_id: Optional[str] = None

    principal_id: Optional[str] = None

    title: Optional[str] = None

    updated_at: Optional[datetime] = None
