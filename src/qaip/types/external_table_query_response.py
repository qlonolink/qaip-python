# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ExternalTableQueryResponse", "Lineage"]


class Lineage(BaseModel):
    """認可と実行で選択したdatasetの版。内部保存先や提供元publication IDは含まない。"""

    dataset_id: str

    logical_schema: str

    synced_at: datetime

    version_id: str
    """qdev で公開した dataset version の UUID。"""


class ExternalTableQueryResponse(BaseModel):
    columns: List[str]

    row_count: int

    rows: List[Dict[str, object]]

    truncated: bool

    lineage: Optional[List[Lineage]] = None
    """
    実際に選択した dataset 版の一覧。旧 server で省略された場合は版情報なしとして扱
    う。
    """
