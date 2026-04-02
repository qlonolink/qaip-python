# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.tag import Tag
from .shared.metadata import Metadata
from .shared.job_status import JobStatus
from .shared.source_type import SourceType

__all__ = ["SourceGroup"]


class SourceGroup(BaseModel):
    id: str
    """Source group ID (job ID)"""

    creation_time: int
    """Unix timestamp when the source group was created"""

    name: str
    """Name of the source group"""

    source_type: SourceType
    """The type of the source"""

    status: JobStatus
    """Job status"""

    metadata: Optional[Metadata] = None

    tags: Optional[List[Tag]] = None
    """List of tags associated with the source group"""
