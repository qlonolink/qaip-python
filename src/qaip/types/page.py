# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .page_asset import PageAsset

__all__ = ["Page"]


class Page(BaseModel):
    id: str
    """Canonical lowercase nonzero UUID."""

    height: float

    ordinal: int

    png: PageAsset

    svg: PageAsset

    warnings: List[str]

    width: float
