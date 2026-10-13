# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["CrawlUpdateSettingParams"]


class CrawlUpdateSettingParams(TypedDict, total=False):
    name: Required[str]
    """Name of the web crawl data source"""

    load_more_enabled: bool
    """
    Omission preserves the saved value; false disables clicking without clearing
    selectors or the limit. Null is invalid.
    """

    load_more_max_clicks: int
    """Maximum click attempts per page.

    Omission preserves the saved value, or 10 for legacy settings. Null is invalid.
    """

    load_more_selectors: SequenceNotStr[str]
    """Ordered CSS selectors.

    Omission preserves them; an empty array clears them and uses built-in controls.
    Null is invalid.
    """

    rrule: str
    """Recurrence rule (RFC 5545 RRULE).

    Empty string or omission removes the existing schedule.
    """
