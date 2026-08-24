# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ExternalQueryState"]

ExternalQueryState: TypeAlias = Literal[
    "RECEIVED",
    "PREPARING",
    "CACHE_READY",
    "RUNNING",
    "CANCELLING",
    "CANCELLED",
    "SUCCEEDED",
    "FAILED",
    "UNKNOWN",
]
