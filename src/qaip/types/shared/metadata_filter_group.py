# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MetadataFilterGroup", "Filter"]


class Filter(BaseModel):
    """Metadata filter for filtering search results by key/value pairs"""

    key: str
    """Metadata key"""

    operator: Literal["eq", "ne", "gt", "gte", "lt", "lte", "between"]
    """Comparison operator"""

    type: Literal["string", "integer", "float", "date"]
    """Data type of the metadata value"""

    max: Optional[object] = None
    """Maximum value for range queries (string or number)"""

    min: Optional[object] = None
    """Minimum value for range queries (string or number)"""

    val: Optional[object] = None
    """Metadata value (string or number).

    This is optional since min/max can be used for range queries.
    """


class MetadataFilterGroup(BaseModel):
    """(reserved for future use) Filter group with nested structure.

    Supports combining filters with AND/OR logic.
    """

    filters: Optional[List[Filter]] = None
    """Filters within this group (combined using the logic operator)"""

    groups: Optional[List["MetadataFilterGroup"]] = None
    """Nested subgroups"""

    logic: Optional[Literal["AND", "OR"]] = None
    """Logical operator for combining filter conditions"""
