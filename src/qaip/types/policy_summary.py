# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .policy_source import PolicySource

__all__ = ["PolicySummary"]


class PolicySummary(BaseModel):
    active_version: Optional[str] = FieldInfo(alias="activeVersion", default=None)

    content_digest: Optional[str] = FieldInfo(alias="contentDigest", default=None)

    description: Optional[str] = None

    draft_version: Optional[str] = FieldInfo(alias="draftVersion", default=None)

    name: str

    source: PolicySource
