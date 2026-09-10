# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentListThreadsParams"]


class AgentListThreadsParams(TypedDict, total=False):
    all_principals: bool
    """If true, return threads across all principals in the tenant.

    Mutually exclusive with principal_id (400 if both are set).
    """

    limit: int

    offset: int

    principal_id: str
    """Filter by principal.

    If omitted, only threads with no principal (principal_id is null) are returned.
    Mutually exclusive with all_principals=true (400 if both are set).
    """
