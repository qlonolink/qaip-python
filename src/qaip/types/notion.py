# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.metadata import Metadata
from .shared.job_error import JobError
from .shared.job_status import JobStatus

__all__ = ["Notion"]


class Notion(BaseModel):
    id: str
    """Notion data source ID"""

    name: str
    """Name of the Notion ingestion setting"""

    page_id: str
    """Notion page ID"""

    status: JobStatus
    """Job status"""

    creation_time: Optional[int] = None
    """Creation time (Unix timestamp in seconds)"""

    end_time: Optional[int] = None
    """Job end time (Unix timestamp in seconds)"""

    error: Optional[JobError] = None

    ingestion_setting_id: Optional[str] = None
    """Notion ingestion setting ID"""

    metadata: Optional[Metadata] = None
    """(reserved for future use) Additional metadata for the Notion data source"""

    start_time: Optional[int] = None
    """Job start time (Unix timestamp in seconds)"""
