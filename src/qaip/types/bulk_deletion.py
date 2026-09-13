# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.job_status import JobStatus

__all__ = ["BulkDeletion"]


class BulkDeletion(BaseModel):
    id: str
    """The id of the bulk deletion job"""

    deleted_count: int
    """Number of source groups deleted so far.

    Meaningful only once the job has reached a terminal status, so callers must gate
    on status rather than treating a low value as a failure.
    """

    remaining_source_group_ids: List[str]
    """
    Source groups that have not been deleted: skipped because another job held the
    group's lock, or failed part-way. Deletion is idempotent, so a caller can
    resubmit this list as-is once the job is terminal.
    """

    remaining_truncated: bool
    """True when remaining_source_group_ids was cut off because too many groups remain.

    Fetch the rest by passing remaining_cursor as the after query parameter.
    """

    status: JobStatus
    """Job status"""

    total_count: int
    """Number of source groups the job was started with"""

    creation_time: Optional[int] = None
    """Unix timestamp when the job was created"""

    end_time: Optional[int] = None
    """Unix timestamp when the job finished"""

    remaining_cursor: Optional[str] = None
    """The last ID in remaining_source_group_ids.

    Present only when remaining_truncated is true; pass it as the after query
    parameter to get the next page.
    """

    start_time: Optional[int] = None
    """Unix timestamp when the job started"""
