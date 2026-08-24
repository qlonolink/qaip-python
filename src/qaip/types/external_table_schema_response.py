# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .external_table_schema import ExternalTableSchema

__all__ = ["ExternalTableSchemaResponse"]


class ExternalTableSchemaResponse(BaseModel):
    tables: List[ExternalTableSchema]
