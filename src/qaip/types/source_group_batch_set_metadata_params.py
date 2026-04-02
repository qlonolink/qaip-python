# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .shared_params.metadata import Metadata

__all__ = ["SourceGroupBatchSetMetadataParams", "Item"]


class SourceGroupBatchSetMetadataParams(TypedDict, total=False):
    items: Required[Iterable[Item]]
    """List of source group metadata items (max 50)"""


class Item(TypedDict, total=False):
    metadata: Required[Metadata]

    source_group_id: Required[str]
    """Source group ID"""
