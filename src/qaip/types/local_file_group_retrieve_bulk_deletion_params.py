# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LocalFileGroupRetrieveBulkDeletionParams"]


class LocalFileGroupRetrieveBulkDeletionParams(TypedDict, total=False):
    after: str
    """Return remaining_source_group_ids strictly greater than this ID.

    Use the remaining_cursor from the previous response to page through a long
    remainder.
    """
