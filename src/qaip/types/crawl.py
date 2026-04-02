# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.metadata import Metadata
from .shared.job_error import JobError
from .shared.job_status import JobStatus

__all__ = ["Crawl"]


class Crawl(BaseModel):
    id: str
    """Web crawl data source ID"""

    name: str
    """Name of the web crawl ingestion setting"""

    start_url: str
    """Start URL of the web crawl"""

    status: JobStatus
    """Job status"""

    creation_time: Optional[int] = None
    """Creation time (Unix timestamp in seconds)"""

    end_time: Optional[int] = None
    """Job end time (Unix timestamp in seconds)"""

    error: Optional[JobError] = None

    ingestion_setting_id: Optional[str] = None
    """Web crawl ingestion setting ID"""

    metadata: Optional[Metadata] = None
    """(reserved for future use) Additional metadata for the web crawl data source"""

    start_time: Optional[int] = None
    """Job start time (Unix timestamp in seconds)"""
