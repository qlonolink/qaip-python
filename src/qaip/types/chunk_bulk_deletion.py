# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.job_status import JobStatus
from .chunk_bulk_deletion_source_group import ChunkBulkDeletionSourceGroup

__all__ = ["ChunkBulkDeletion"]


class ChunkBulkDeletion(BaseModel):
    id: str
    """The id of the chunk bulk deletion job"""

    source_groups: List[ChunkBulkDeletionSourceGroup]
    """Every source group of the job in ascending ID order"""

    status: JobStatus
    """Job status"""

    creation_time: Optional[int] = None
    """Unix timestamp when the job was created"""

    end_time: Optional[int] = None
    """Unix timestamp when the job finished"""

    start_time: Optional[int] = None
    """Unix timestamp when the job started"""
