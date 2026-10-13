# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .chunk_bulk_deletion_entry_param import ChunkBulkDeletionEntryParam

__all__ = ["LocalFileGroupStartChunkBulkDeletionParams"]


class LocalFileGroupStartChunkBulkDeletionParams(TypedDict, total=False):
    deletions: Required[Iterable[ChunkBulkDeletionEntryParam]]
    """Groups and the substrings to delete from each.

    Entries for the same source group are merged.
    """
