# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .github import GitHub
from .._models import BaseModel
from .shared.pagination import Pagination

__all__ = ["GitHubListResponse"]


class GitHubListResponse(BaseModel):
    githubs: List[GitHub]

    pagination: Pagination
