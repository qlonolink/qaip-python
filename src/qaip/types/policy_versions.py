# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .policy_version import PolicyVersion

__all__ = ["PolicyVersions", "Pagination"]


class Pagination(BaseModel):
    next_before_version: Optional[str] = FieldInfo(alias="nextBeforeVersion", default=None)


class PolicyVersions(BaseModel):
    pagination: Pagination

    versions: List[PolicyVersion]
