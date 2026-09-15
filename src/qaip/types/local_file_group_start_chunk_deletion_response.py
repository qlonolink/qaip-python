# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["LocalFileGroupStartChunkDeletionResponse"]


class LocalFileGroupStartChunkDeletionResponse(BaseModel):
    id: str
    """The id of the started chunk deletion job, used to poll its status"""

    source_group_id: str
    """The ID of the source group whose chunks are being deleted"""
