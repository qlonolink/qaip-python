# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DriveDownloadOriginalParams"]


class DriveDownloadOriginalParams(TypedDict, total=False):
    revision_id: Required[str]
    """Fixed original revision ID returned by an allowed file lookup.

    A mismatched or unavailable revision is denied.
    """

    range: Annotated[str, PropertyInfo(alias="Range")]
