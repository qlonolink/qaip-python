# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .external_query_column import ExternalQueryColumn

__all__ = ["ExternalQueryResultResponse", "Lineage"]


class Lineage(BaseModel):
    """認可と実行で選択したdatasetの版。内部保存先や提供元publication IDは含まない。"""

    dataset_id: str

    logical_schema: str

    synced_at: datetime

    version_id: str
    """qdev で公開した dataset version の UUID。"""


class ExternalQueryResultResponse(BaseModel):
    columns: List[ExternalQueryColumn]

    request_id: str

    response_type: Literal["result"]

    row_count: int

    rows: List[Dict[str, object]]

    state: Literal["SUCCEEDED"]

    truncated: bool

    lineage: Optional[List[Lineage]] = None
    """worker が実際に開いた dataset 版の一覧。旧 server では省略される。"""
