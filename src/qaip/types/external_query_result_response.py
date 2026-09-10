# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal

from .._models import BaseModel
from .external_query_column import ExternalQueryColumn

__all__ = ["ExternalQueryResultResponse"]


class ExternalQueryResultResponse(BaseModel):
    columns: List[ExternalQueryColumn]

    request_id: str

    response_type: Literal["result"]

    row_count: int

    rows: List[Dict[str, object]]

    state: Literal["SUCCEEDED"]

    truncated: bool
