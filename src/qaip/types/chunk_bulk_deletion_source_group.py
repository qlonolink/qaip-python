# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChunkBulkDeletionSourceGroup"]


class ChunkBulkDeletionSourceGroup(BaseModel):
    deleted_count: int
    """Number of chunk rows deleted from this group.

    Meaningful only when state is deleted. A resubmission of rows that are already
    gone reports 0.
    """

    source_group_id: str
    """The ID of the local file group"""

    state: Literal["pending", "claimed", "deleted", "failed", "skipped_busy"]
    """`pending`: not processed yet.

    `claimed`: being processed. `deleted`: the matching rows are gone. `failed`: the
    job failed part-way. `skipped_busy`: another job held the group, or its
    ingestion had not finished. Groups not in `deleted` once the job is terminal can
    be resubmitted.
    """
