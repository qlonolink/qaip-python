# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TagManagementUpdateParams"]


class TagManagementUpdateParams(TypedDict, total=False):
    description: str
    """New tag description. Omit or send an empty string to leave unchanged."""

    name: str
    """New tag name. Omit or send an empty string to leave unchanged."""
