# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.metadata import Metadata
from .shared.job_error import JobError
from .shared.job_status import JobStatus

__all__ = ["GoogleDrive"]


class GoogleDrive(BaseModel):
    id: str
    """Google Drive data source ID"""

    folder_url: str
    """Google Drive folder URL"""

    name: str
    """Name of the Google Drive ingestion setting"""

    status: JobStatus
    """Job status"""

    creation_time: Optional[int] = None
    """Creation time (Unix timestamp in seconds)"""

    end_time: Optional[int] = None
    """Job end time (Unix timestamp in seconds)"""

    error: Optional[JobError] = None

    ingestion_setting_id: Optional[str] = None
    """Google Drive ingestion setting ID"""

    metadata: Optional[Metadata] = None
    """(reserved for future use) Additional metadata for the Google Drive data source"""

    start_time: Optional[int] = None
    """Job start time (Unix timestamp in seconds)"""
