# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .google_drive import GoogleDrive
from .shared.pagination import Pagination

__all__ = ["GoogleDriveListResponse"]


class GoogleDriveListResponse(BaseModel):
    google_drives: List[GoogleDrive]

    pagination: Pagination
