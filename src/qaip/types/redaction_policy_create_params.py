# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["RedactionPolicyCreateParams", "BusinessConfidential", "BusinessConfidentialInclude"]


class RedactionPolicyCreateParams(TypedDict, total=False):
    business_confidential: Required[Annotated[BusinessConfidential, PropertyInfo(alias="businessConfidential")]]

    name: Required[str]

    description: Optional[str]


class BusinessConfidentialInclude(TypedDict, total=False):
    mode: Required[Literal["exact", "value_clause", "exact_or_value_clause"]]

    text: Required[str]


class BusinessConfidential(TypedDict, total=False):
    definition: Required[str]

    examples: Required[SequenceNotStr[str]]

    exclude: Required[SequenceNotStr[str]]

    include: Required[Iterable[BusinessConfidentialInclude]]
