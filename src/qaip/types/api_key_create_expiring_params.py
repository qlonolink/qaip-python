# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .api_key_kind import APIKeyKind
from .issuable_api_key_scope import IssuableAPIKeyScope

__all__ = ["APIKeyCreateExpiringParams"]


class APIKeyCreateExpiringParams(TypedDict, total=False):
    key_kind: Required[APIKeyKind]
    """Principal binding of the issued API key."""

    name: Required[str]
    """Name of the API key"""

    scopes: Required[List[IssuableAPIKeyScope]]
    """Scopes granted to the issued key. Must be a subset of the caller's scopes."""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    description: str
    """Description of the API key"""

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Absolute expiration time. Mutually exclusive with `ttl`."""

    ttl: int
    """Lifetime in seconds. Mutually exclusive with `expires_at`."""
