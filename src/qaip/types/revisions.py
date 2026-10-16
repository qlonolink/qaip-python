# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .revision import Revision
from .drive_pagination import DrivePagination

__all__ = ["Revisions"]


class Revisions(BaseModel):
    pagination: DrivePagination

    revisions: List[Revision]
