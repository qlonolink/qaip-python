# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .part_receipt import PartReceipt

__all__ = ["Transfer"]


class Transfer(BaseModel):
    id: str
    """Canonical lowercase nonzero UUID."""

    error_code: Optional[str] = None

    expires_at: datetime

    file_id: str
    """Canonical lowercase nonzero UUID."""

    part_size: int

    parts: List[PartReceipt]

    revision_id: Optional[str] = None
    """Canonical lowercase nonzero UUID."""

    size_bytes: int

    state: Literal[
        "creating",
        "uploading",
        "completing",
        "verifying",
        "committed",
        "aborting",
        "aborted",
        "expired",
        "conflict",
        "failed",
    ]
