# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DriveUploadPartParams"]


class DriveUploadPartParams(TypedDict, total=False):
    transfer_id: Required[str]
    """Canonical lowercase nonzero UUID."""

    x_drive_sha256: Required[Annotated[str, PropertyInfo(alias="X-Drive-SHA256")]]
