# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .conversation_message import ConversationMessage
from .conversation_tree_node import ConversationTreeNode

__all__ = ["ConversationDetail"]


class ConversationDetail(BaseModel):
    active_path: List[ConversationMessage]

    id: str

    created_at: Optional[datetime] = None

    current_leaf_id: Optional[str] = None

    principal_id: Optional[str] = None

    title: Optional[str] = None

    tree: Optional[List[ConversationTreeNode]] = None

    updated_at: Optional[datetime] = None
