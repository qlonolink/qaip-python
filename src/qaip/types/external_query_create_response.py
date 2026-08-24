# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .external_table_query_response import ExternalTableQueryResponse
from .external_query_result_response import ExternalQueryResultResponse
from .external_query_preparing_response import ExternalQueryPreparingResponse
from .external_query_state_only_response import ExternalQueryStateOnlyResponse

__all__ = ["ExternalQueryCreateResponse"]

ExternalQueryCreateResponse: TypeAlias = Union[
    ExternalQueryResultResponse,
    ExternalQueryPreparingResponse,
    ExternalQueryStateOnlyResponse,
    ExternalTableQueryResponse,
]
