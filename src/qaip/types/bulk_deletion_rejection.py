# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BulkDeletionRejection"]


class BulkDeletionRejection(BaseModel):
    reason: Literal["not_found"]
    """Why the ID was not accepted.

    `not_found`: absent or owned by another user. Groups with another job in flight
    are not rejected here; they are skipped by the job and reported in the status's
    `remaining_source_group_ids`.
    """

    source_group_id: str
    """The ID that was not accepted"""
