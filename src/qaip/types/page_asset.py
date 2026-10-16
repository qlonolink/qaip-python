# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PageAsset"]


class PageAsset(BaseModel):
    sha256: str

    size_bytes: int
