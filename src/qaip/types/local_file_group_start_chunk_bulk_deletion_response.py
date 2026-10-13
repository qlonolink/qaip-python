# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .bulk_deletion_rejection import BulkDeletionRejection

__all__ = ["LocalFileGroupStartChunkBulkDeletionResponse"]


class LocalFileGroupStartChunkBulkDeletionResponse(BaseModel):
    accepted_count: int
    """Number of source groups handed to the job.

    The job may still skip some of them; the authoritative outcome is each group's
    state in the job status.
    """

    rejected: List[BulkDeletionRejection]
    """Source groups that were not accepted, with the reason for each"""

    id: Optional[str] = None
    """The id of the started job, used to poll its status.

    Absent when accepted_count is 0, in which case no job was started.
    """
