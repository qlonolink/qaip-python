# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["TagSourceGroup"]


class TagSourceGroup(BaseModel):
    source_group_id: str
    """Source group ID.

    The source group ID corresponds to the job ID for each data source.
    """

    tag_id: str
    """Tag ID"""
