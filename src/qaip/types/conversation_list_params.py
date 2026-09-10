# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConversationListParams"]


class ConversationListParams(TypedDict, total=False):
    all_principals: bool
    """If true, return conversations across all principals in the tenant.

    Mutually exclusive with principal_id (400 if both are set).
    """

    limit: int

    offset: int

    principal_id: str
    """Filter by principal.

    If set, only conversations belonging to this principal are returned. If omitted,
    only conversations with no principal (principal_id is null) are returned.
    Mutually exclusive with all_principals=true (400 if both are set).
    """
