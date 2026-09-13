# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .bulk_deletion_rejection import BulkDeletionRejection

__all__ = ["LocalFileGroupStartBulkDeletionResponse"]


class LocalFileGroupStartBulkDeletionResponse(BaseModel):
    accepted_count: int
    """Number of source groups handed to the job.

    The job may still skip some of them (another job holds the group's lock); the
    authoritative outcome is the status's `remaining_source_group_ids`.
    """

    rejected: List[BulkDeletionRejection]
    """IDs that were not accepted, with the reason for each"""

    id: Optional[str] = None
    """The id of the started bulk deletion job, used to poll its status.

    Absent when accepted_count is 0, in which case no job was started.
    """
