# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PolicyDefinition", "BusinessConfidential", "BusinessConfidentialInclude"]


class BusinessConfidentialInclude(BaseModel):
    mode: Literal["exact", "value_clause", "exact_or_value_clause"]

    text: str


class BusinessConfidential(BaseModel):
    definition: str

    examples: List[str]

    exclude: List[str]

    include: List[BusinessConfidentialInclude]


class PolicyDefinition(BaseModel):
    business_confidential: Optional[BusinessConfidential] = FieldInfo(alias="businessConfidential", default=None)

    enabled_categories: List[Literal["N", "T", "E", "A", "I", "C", "P", "K", "B"]] = FieldInfo(
        alias="enabledCategories"
    )
