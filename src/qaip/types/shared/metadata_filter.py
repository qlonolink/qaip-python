# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MetadataFilter"]


class MetadataFilter(BaseModel):
    """Metadata filter for filtering search results by key/value pairs"""

    key: str
    """Metadata key"""

    operator: Literal["eq", "ne", "gt", "gte", "lt", "lte", "between", "contains"]
    """Comparison operator.

    contains tests array membership and is valid only for string_list / integer_list
    columns in metadata_filter; conversely those array types accept only contains.
    """

    type: Literal["string", "integer", "float", "date", "datetime", "string_list", "integer_list"]
    """Data type of the metadata value.

    string_list / integer_list are valid only for metadata_filter (declared LanceDB
    array columns); the PostgreSQL-backed metadata / source_metadata /
    chunk_metadata filters reject them.
    """

    max: Optional[object] = None
    """Maximum value for range queries (string or number)"""

    min: Optional[object] = None
    """Minimum value for range queries (string or number)"""

    val: Optional[object] = None
    """Metadata value (string or number).

    This is optional since min/max can be used for range queries.
    """
