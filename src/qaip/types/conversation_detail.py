# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .conversation_message import ConversationMessage
from .conversation_tree_node import ConversationTreeNode

__all__ = ["ConversationDetail"]


class ConversationDetail(BaseModel):
    id: str

    active_path: List[ConversationMessage]
    """
    Messages (with content/citations) from the leaf back to the root, in display
    order.
    """

    created_at: Optional[datetime] = None

    current_leaf_id: Optional[str] = None

    principal_id: Optional[str] = None
    """Authorization principal this conversation belongs to (null if not set)."""

    title: Optional[str] = None

    tree: Optional[List[ConversationTreeNode]] = None
    """
    All nodes as a lightweight structure (id/parent_id/role/created_at, no
    content/citations). Use to detect sibling branches and pick a leaf to preview
    via the leaf_id query parameter.
    """

    updated_at: Optional[datetime] = None
