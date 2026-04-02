# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["LocalFileGroupDeleteResponse"]


class LocalFileGroupDeleteResponse(BaseModel):
    source_group_id: str
    """The ID of the deleted source group"""
