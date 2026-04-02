# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GoogleDriveSetting"]


class GoogleDriveSetting(BaseModel):
    id: str
    """Google Drive ingestion setting ID"""

    folder_url: str
    """Google Drive folder URL"""

    name: str
    """Name of the Google Drive ingestion setting"""

    rrule: Optional[str] = None
    """Recurrence rule (RFC 5545 RRULE)"""

    secret_id: Optional[str] = None
    """ID of the associated secret"""
