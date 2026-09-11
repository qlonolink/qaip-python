# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConversationDeleteParams"]


class ConversationDeleteParams(TypedDict, total=False):
    principal_id: str
    """Scope the target by principal.

    If omitted, only a conversation with no principal (principal_id is null) is
    addressed; a conversation whose principal differs yields 404.
    """
