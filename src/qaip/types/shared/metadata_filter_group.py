# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from .metadata_filter import MetadataFilter
from .logical_operator import LogicalOperator

__all__ = ["MetadataFilterGroup"]


class MetadataFilterGroup(BaseModel):
    """(reserved for future use) Filter group with nested structure.

    Supports combining filters with AND/OR logic.
    """

    filters: Optional[List[MetadataFilter]] = None
    """Filters within this group (combined using the logic operator)"""

    groups: Optional[List["MetadataFilterGroup"]] = None
    """Nested subgroups"""

    logic: Optional[LogicalOperator] = None
    """Logical operator for combining filter conditions"""
