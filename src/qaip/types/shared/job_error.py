# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["JobError"]


class JobError(BaseModel):
    message: Optional[str] = None
    """Error message"""

    title: Optional[str] = None
    """Error title"""
