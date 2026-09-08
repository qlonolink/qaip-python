# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .api_key_kind import APIKeyKind
from .issuable_api_key_scope import IssuableAPIKeyScope

__all__ = ["CreatedExpiringAPIKey"]


class CreatedExpiringAPIKey(BaseModel):
    id: str
    """API key ID"""

    creation_time: datetime
    """API key creation time"""

    expires_at: datetime
    """API key expiration time"""

    key: str
    """Plaintext API key. Returned only for the first successful request."""

    key_kind: APIKeyKind
    """Principal binding of the issued API key."""

    name: str
    """Name of the API key"""

    scopes: List[IssuableAPIKeyScope]
    """Scopes granted to this key"""

    description: Optional[str] = None
    """Description of the API key"""
