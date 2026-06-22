# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Keyword"]


class Keyword(BaseModel):
    id: str
    """Keyword ID"""

    name: str
    """Name of the keyword"""

    meaning: Optional[str] = None
    """Meaning of the keyword"""
