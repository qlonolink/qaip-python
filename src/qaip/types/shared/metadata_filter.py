# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MetadataFilter"]


class MetadataFilter(BaseModel):
    """Metadata filter for filtering search results by key/value pairs"""

    key: str
    """Metadata key"""

    operator: Literal["eq", "ne", "gt", "gte", "lt", "lte", "between"]
    """Comparison operator"""

    type: Literal["string", "integer", "float", "date", "datetime"]
    """Data type of the metadata value"""

    max: Optional[object] = None
    """Maximum value for range queries (string or number)"""

    min: Optional[object] = None
    """Minimum value for range queries (string or number)"""

    val: Optional[object] = None
    """Metadata value (string or number).

    This is optional since min/max can be used for range queries.
    """
