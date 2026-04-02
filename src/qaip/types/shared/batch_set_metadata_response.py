# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BatchSetMetadataResponse", "Result"]


class Result(BaseModel):
    id: Optional[str] = None
    """Source or source group ID"""

    error: Optional[str] = None
    """Error message if operation failed"""

    success: Optional[bool] = None
    """Whether the operation succeeded"""


class BatchSetMetadataResponse(BaseModel):
    results: List[Result]

    success_count: int
    """Number of successfully processed items"""
