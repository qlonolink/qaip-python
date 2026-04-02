# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .secret import Secret
from .._models import BaseModel
from .shared.pagination import Pagination

__all__ = ["SecretListResponse"]


class SecretListResponse(BaseModel):
    pagination: Pagination

    secrets: List[Secret]
