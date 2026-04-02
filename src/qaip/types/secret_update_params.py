# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SecretUpdateParams"]


class SecretUpdateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the secret"""

    description: str
    """Description of the secret"""

    secret: str
    """The secret value (omit to keep unchanged)"""
