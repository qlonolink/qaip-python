# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .policy_source import PolicySource
from .policy_version import PolicyVersion

__all__ = ["PolicyDetail"]


class PolicyDetail(BaseModel):
    active_version: Optional[PolicyVersion] = FieldInfo(alias="activeVersion", default=None)

    description: Optional[str] = None

    draft_version: Optional[PolicyVersion] = FieldInfo(alias="draftVersion", default=None)

    name: str

    source: PolicySource
