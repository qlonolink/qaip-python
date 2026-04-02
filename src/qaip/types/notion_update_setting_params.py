# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NotionUpdateSettingParams"]


class NotionUpdateSettingParams(TypedDict, total=False):
    name: Required[str]
    """Name of the Notion data source"""

    rrule: str
    """Recurrence rule (RFC 5545 RRULE).

    Empty string or omission removes the existing schedule.
    """
