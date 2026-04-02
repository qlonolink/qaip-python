# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.metadata import Metadata

__all__ = ["NotionCreateParams"]


class NotionCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the Notion data source"""

    page_id: Required[str]
    """Notion page ID"""

    metadata: Metadata
    """(reserved for future use) Additional metadata for the Notion data source"""

    notion_token: str
    """One-time Notion integration token (mutually exclusive with secret_id)"""

    rrule: str
    """Recurrence rule (RFC 5545 RRULE). Requires secret_id (not one-time token)."""

    secret_id: str
    """ID of a stored secret to use (mutually exclusive with notion_token)"""
