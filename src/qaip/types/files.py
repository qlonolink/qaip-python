# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .file import File
from .._models import BaseModel
from .drive_pagination import DrivePagination

__all__ = ["Files"]


class Files(BaseModel):
    files: List[File]

    pagination: DrivePagination
