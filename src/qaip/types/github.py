# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.metadata import Metadata
from .shared.job_error import JobError
from .shared.job_status import JobStatus
from .github_reference_type import GitHubReferenceType

__all__ = ["GitHub"]


class GitHub(BaseModel):
    id: str
    """GitHub data source ID"""

    ingestion_setting_id: str
    """GitHub ingestion setting ID"""

    name: str
    """Name of the GitHub ingestion setting"""

    reference_type: GitHubReferenceType
    """Git reference type"""

    repository: str
    """GitHub repository in owner/repo format (e.g. "octocat/Hello-World")"""

    status: JobStatus
    """Job status"""

    creation_time: Optional[int] = None
    """Creation time (Unix timestamp in seconds)"""

    end_time: Optional[int] = None
    """Job end time (Unix timestamp in seconds)"""

    error: Optional[JobError] = None

    metadata: Optional[Metadata] = None
    """(reserved for future use) Additional metadata for the GitHub data source"""

    path_filters: Optional[List[str]] = None
    """Path filter patterns"""

    reference_param: Optional[str] = None
    """Reference parameter (branch name, tag name, or commit hash)"""

    start_time: Optional[int] = None
    """Job start time (Unix timestamp in seconds)"""
