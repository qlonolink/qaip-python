# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentRetrieveThreadParams"]


class AgentRetrieveThreadParams(TypedDict, total=False):
    principal_id: str
    """Scope by principal.

    If omitted, only a thread with no principal (principal_id is null) is returned;
    a thread whose principal differs yields 404.
    """
