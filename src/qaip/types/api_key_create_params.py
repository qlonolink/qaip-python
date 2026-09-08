# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .issuable_api_key_scope import IssuableAPIKeyScope

__all__ = ["APIKeyCreateParams", "ApiKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the API key"""

    scopes: Required[List[IssuableAPIKeyScope]]
    """Scopes granted to the issued key. Must be a subset of the caller's scopes."""

    description: str
    """Description of the API key"""


# 公開済みの型名を維持する。
ApiKeyCreateParams = APIKeyCreateParams
