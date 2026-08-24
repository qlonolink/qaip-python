# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .external_query_state import ExternalQueryState

__all__ = ["ExternalQueryStateOnlyResponse"]


class ExternalQueryStateOnlyResponse(BaseModel):
    request_id: str

    response_type: Literal["state_only"]

    state: ExternalQueryState

    terminal: bool

    failure_class: Optional[
        Literal[
            "invalid_request",
            "unauthorized",
            "snapshot_unavailable",
            "capacity",
            "build_timeout",
            "query_timeout",
            "rate_limited",
            "internal",
        ]
    ] = None

    retry_after_seconds: Optional[int] = None
