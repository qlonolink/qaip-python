# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .issuable_api_key_scope import IssuableApiKeyScope

__all__ = ["CreatedApiKey"]


class CreatedApiKey(BaseModel):
    id: str
    """API key ID"""

    creation_time: int
    """Creation time (Unix timestamp in seconds)"""

    key: str
    """Plaintext API key. Returned only at creation time."""

    name: str
    """Name of the API key"""

    scopes: List[IssuableApiKeyScope]
    """Scopes granted to this key"""

    description: Optional[str] = None
    """Description of the API key"""
