# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RedactionPolicyActivateVersionParams"]


class RedactionPolicyActivateVersionParams(TypedDict, total=False):
    name: Required[str]

    expected_active_version: Required[Annotated[Optional[str], PropertyInfo(alias="expectedActiveVersion")]]
    """null requires that no ACTIVE version currently exists."""
