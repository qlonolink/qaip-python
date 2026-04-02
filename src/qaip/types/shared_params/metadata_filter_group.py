# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .metadata_filter import MetadataFilter
from ..shared.logical_operator import LogicalOperator

__all__ = ["MetadataFilterGroup"]


class MetadataFilterGroup(TypedDict, total=False):
    """(reserved for future use) Filter group with nested structure.

    Supports combining filters with AND/OR logic.
    """

    filters: Iterable[MetadataFilter]
    """Filters within this group (combined using the logic operator)"""

    groups: Iterable["MetadataFilterGroup"]
    """Nested subgroups"""

    logic: LogicalOperator
    """Logical operator for combining filter conditions"""
