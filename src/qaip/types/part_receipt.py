# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PartReceipt"]


class PartReceipt(BaseModel):
    number: int

    sha256: str

    size_bytes: int
