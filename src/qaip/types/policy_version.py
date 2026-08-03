# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .policy_source import PolicySource
from .policy_status import PolicyStatus
from .policy_definition import PolicyDefinition

__all__ = ["PolicyVersion"]


class PolicyVersion(BaseModel):
    activated_at: Optional[datetime] = FieldInfo(alias="activatedAt", default=None)

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)

    content_digest: str = FieldInfo(alias="contentDigest")

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    definition: Optional[PolicyDefinition] = None
    """null in version-list responses; populated by detail and version reads."""

    description: Optional[str] = None

    name: str

    schema_version: int = FieldInfo(alias="schemaVersion")

    source: PolicySource

    status: PolicyStatus

    version: str
