# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .display import Display
from .._models import BaseModel
from .drive_pagination import DrivePagination

__all__ = ["Displays"]


class Displays(BaseModel):
    displays: List[Display]

    pagination: DrivePagination
