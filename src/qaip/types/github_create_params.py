# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .github_reference_type import GitHubReferenceType
from .shared_params.metadata import Metadata

__all__ = ["GitHubCreateParams"]


class GitHubCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the GitHub data source"""

    repository: Required[str]
    """GitHub repository in owner/repo format (e.g. "octocat/Hello-World")"""

    github_token: str
    """One-time GitHub personal access token (mutually exclusive with secret_id)"""

    metadata: Metadata
    """(reserved for future use) Additional metadata for the GitHub data source"""

    path_filters: SequenceNotStr[str]
    """Path filters patterns.

    The total number of characters across all elements in the array must be 2000 or
    fewer.
    """

    reference_param: str
    """Reference parameter (branch name, tag name, or commit hash)"""

    reference_type: GitHubReferenceType
    """Git reference type"""

    rrule: str
    """Recurrence rule (RFC 5545 RRULE). Requires secret_id (not one-time token)."""

    secret_id: str
    """ID of a stored secret to use (mutually exclusive with github_token)"""
