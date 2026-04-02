# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .secret_type import SecretType

__all__ = ["SecretListParams"]


class SecretListParams(TypedDict, total=False):
    after_id: str
    """Fetch records after this ID"""

    limit: int
    """Maximum number of results to return"""

    secret_type: SecretType
    """Filter by secret type"""
