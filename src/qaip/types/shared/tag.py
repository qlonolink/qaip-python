# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Tag"]


class Tag(BaseModel):
    id: str
    """Tag ID"""

    description: str
    """Tag description"""

    name: str
    """Tag name"""
