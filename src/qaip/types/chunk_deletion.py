# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.job_status import JobStatus

__all__ = ["ChunkDeletion"]


class ChunkDeletion(BaseModel):
    id: str
    """The id of the chunk deletion job"""

    deleted_count: int
    """Number of chunk rows deleted.

    Always present; meaningful only once the job has succeeded (status = success).
    Before then it is 0 (not yet determined), so callers must gate on status rather
    than treating 0 as "no chunks deleted".
    """

    source_group_id: str
    """The ID of the source group whose chunks are being deleted"""

    status: JobStatus
    """Job status"""

    text_contains: List[str]
    """The substrings used to match chunk rows for deletion"""

    creation_time: Optional[int] = None
    """Unix timestamp when the job was created"""

    end_time: Optional[int] = None
    """Unix timestamp when the job finished"""

    start_time: Optional[int] = None
    """Unix timestamp when the job started"""
