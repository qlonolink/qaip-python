# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DriveListDisplaysParams"]


class DriveListDisplaysParams(TypedDict, total=False):
    revision_id: Required[str]
    """Canonical lowercase nonzero UUID."""

    after_id: str
    """Exclusive last returned ID.

    Results are in ascending UUID order; an empty page ends the scan.
    """

    limit: int
