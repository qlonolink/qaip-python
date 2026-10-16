# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .folder import Folder
from .._models import BaseModel
from .drive_pagination import DrivePagination

__all__ = ["Folders"]


class Folders(BaseModel):
    folders: List[Folder]

    pagination: DrivePagination
