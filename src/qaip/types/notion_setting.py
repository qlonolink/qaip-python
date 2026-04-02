# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["NotionSetting"]


class NotionSetting(BaseModel):
    id: str
    """Notion ingestion setting ID"""

    name: str
    """Name of the Notion ingestion setting"""

    page_id: str
    """Notion page ID"""

    rrule: Optional[str] = None
    """Recurrence rule (RFC 5545 RRULE)"""

    secret_id: Optional[str] = None
    """ID of the associated secret"""
