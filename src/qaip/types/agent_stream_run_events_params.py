# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentStreamRunEventsParams"]


class AgentStreamRunEventsParams(TypedDict, total=False):
    after: int
    """Last persisted event index received by the client.

    Takes precedence over Last-Event-ID.
    """

    principal_id: str
    """Scope by principal.

    If omitted, only a run with no principal (principal_id is null) is addressed; a
    run whose principal differs yields 404.
    """

    last_event_id: Annotated[str, PropertyInfo(alias="Last-Event-ID")]
