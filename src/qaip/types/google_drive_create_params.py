# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.metadata import Metadata

__all__ = ["GoogleDriveCreateParams"]


class GoogleDriveCreateParams(TypedDict, total=False):
    folder_url: Required[str]
    """Google Drive folder URL"""

    name: Required[str]
    """Name of the Google Drive data source"""

    metadata: Metadata
    """(reserved for future use) Additional metadata for the Google Drive data source"""

    rrule: str
    """Recurrence rule (RFC 5545 RRULE). Requires secret_id (not one-time key)."""

    secret_id: str
    """ID of a stored secret to use (mutually exclusive with service_account_key)"""

    service_account_key: str
    """One-time service account key JSON (mutually exclusive with secret_id)"""
