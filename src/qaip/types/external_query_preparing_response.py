# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExternalQueryPreparingResponse"]


class ExternalQueryPreparingResponse(BaseModel):
    request_id: str

    response_type: Literal["preparing"]

    state: Literal["PREPARING"]

    status_url: str
