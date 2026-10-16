# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DriveListFoldersParams"]


class DriveListFoldersParams(TypedDict, total=False):
    after_id: str
    """Exclusive last returned ID.

    Results are in ascending UUID order; an empty page ends the scan.
    """

    limit: int

    parent_id: str
    """Canonical lowercase nonzero UUID."""
