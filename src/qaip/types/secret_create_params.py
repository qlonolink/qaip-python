# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .secret_type import SecretType

__all__ = ["SecretCreateParams"]


class SecretCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the secret"""

    secret: Required[str]
    """The secret value"""

    type: Required[SecretType]
    """The type of the secret"""

    description: str
    """Description of the secret"""
