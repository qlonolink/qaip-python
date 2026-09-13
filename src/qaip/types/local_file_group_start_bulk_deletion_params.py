# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["LocalFileGroupStartBulkDeletionParams"]


class LocalFileGroupStartBulkDeletionParams(TypedDict, total=False):
    source_group_ids: Required[SequenceNotStr[str]]
    """IDs of the local file groups to delete.

    Duplicates are ignored. IDs that cannot be accepted are reported in the response
    rather than failing the whole request.
    """
