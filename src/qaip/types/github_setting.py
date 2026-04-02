# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .github_reference_type import GitHubReferenceType

__all__ = ["GitHubSetting"]


class GitHubSetting(BaseModel):
    id: str
    """GitHub ingestion setting ID"""

    name: str
    """Name of the GitHub ingestion setting"""

    repository: str
    """GitHub repository in owner/repo format (e.g. "octocat/Hello-World")"""

    path_filters: Optional[List[str]] = None

    reference_param: Optional[str] = None
    """Reference parameter (branch name, tag name, or commit hash)"""

    reference_type: Optional[GitHubReferenceType] = None
    """Git reference type"""

    rrule: Optional[str] = None
    """Recurrence rule (RFC 5545 RRULE)"""

    secret_id: Optional[str] = None
    """ID of the associated secret"""
