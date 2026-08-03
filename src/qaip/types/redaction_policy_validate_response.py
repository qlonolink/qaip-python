# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .policy_definition import PolicyDefinition

__all__ = ["RedactionPolicyValidateResponse"]


class RedactionPolicyValidateResponse(BaseModel):
    content_digest: str = FieldInfo(alias="contentDigest")

    definition: PolicyDefinition

    name: str

    schema_version: Literal[1] = FieldInfo(alias="schemaVersion")
