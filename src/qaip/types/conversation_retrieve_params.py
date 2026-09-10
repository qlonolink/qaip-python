# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConversationRetrieveParams"]


class ConversationRetrieveParams(TypedDict, total=False):
    leaf_id: str
    """Leaf node to build active_path from.

    When set, returns that branch's path without mutating current_leaf_id
    (non-destructive preview). When omitted, uses the conversation's
    current_leaf_id. Must belong to the conversation.
    """

    principal_id: str
    """Scope the target by principal.

    If omitted, only a conversation with no principal (principal_id is null) is
    addressed; a conversation whose principal differs yields 404.
    """
