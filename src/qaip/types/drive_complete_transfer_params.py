# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .complete_transfer_request_param import CompleteTransferRequestParam

__all__ = ["DriveCompleteTransferParams"]


class DriveCompleteTransferParams(TypedDict, total=False):
    complete_transfer_request: Required[CompleteTransferRequestParam]
