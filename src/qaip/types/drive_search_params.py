# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DriveSearchParams"]


class DriveSearchParams(TypedDict, total=False):
    query: Required[str]
    """Natural-language information need. Whitespace-only queries are rejected."""

    limit: int

    offset: int
    """Use pagination.next_offset from the preceding response."""
