# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ChunkBulkDeletionEntryParam"]


class ChunkBulkDeletionEntryParam(TypedDict, total=False):
    source_group_id: Required[str]
    """The ID of the local file group whose chunk rows are deleted"""

    text_contains: Required[SequenceNotStr[str]]
    """OR list of substrings for this group.

    Chunk rows whose text contains any of these substrings (literal match) are
    deleted. The text is the JSONL line without the reserved qaip_metadata object,
    which ingestion separates from the row, so a substring that occurs only inside
    qaip_metadata matches nothing. Empty strings are rejected because they would
    match every row.
    """
