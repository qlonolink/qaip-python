# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MetadataFilter"]


class MetadataFilter(TypedDict, total=False):
    """Metadata filter for filtering search results by key/value pairs"""

    key: Required[str]
    """Metadata key"""

    operator: Required[Literal["eq", "ne", "gt", "gte", "lt", "lte", "between"]]
    """Comparison operator"""

    type: Required[Literal["string", "integer", "float", "date", "datetime"]]
    """Data type of the metadata value"""

    max: object
    """Maximum value for range queries (string or number)"""

    min: object
    """Minimum value for range queries (string or number)"""

    val: object
    """Metadata value (string or number).

    This is optional since min/max can be used for range queries.
    """
