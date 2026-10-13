# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .external_table_schema import ExternalTableSchema

__all__ = ["ExternalTableSchemaResponse", "Lineage"]


class Lineage(BaseModel):
    """認可と実行で選択したdatasetの版。内部保存先や提供元publication IDは含まない。"""

    dataset_id: str

    logical_schema: str

    synced_at: datetime

    version_id: str
    """qdev で公開した dataset version の UUID。"""


class ExternalTableSchemaResponse(BaseModel):
    tables: List[ExternalTableSchema]

    lineage: Optional[List[Lineage]] = None
    """この schema 応答に含まれる認可済み dataset 版の一覧。"""
