# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .external_table_column import ExternalTableColumn

__all__ = ["ExternalTableSchema"]


class ExternalTableSchema(BaseModel):
    columns: List[ExternalTableColumn]

    logical_table: str

    synced_at: datetime
