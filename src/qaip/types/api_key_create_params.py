# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .issuable_api_key_scope import IssuableApiKeyScope

__all__ = ["ApiKeyCreateParams"]


class ApiKeyCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the API key"""

    scopes: Required[List[IssuableApiKeyScope]]
    """Scopes granted to the issued key. Must be a subset of the caller's scopes."""

    description: str
    """Description of the API key"""
