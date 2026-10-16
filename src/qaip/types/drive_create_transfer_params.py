# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .reference_source_param import ReferenceSourceParam

__all__ = ["DriveCreateTransferParams"]


class DriveCreateTransferParams(TypedDict, total=False):
    folder_id: Required[str]
    """Canonical lowercase nonzero UUID."""

    idempotency_key: Required[str]
    """Canonical lowercase nonzero UUID."""

    media_type: Required[str]
    """Valid MIME media type without parameters."""

    name: Required[str]
    """Nonblank file or folder name; no slash, backslash, control characters, .

    or .. .
    """

    sha256: Required[str]

    size_bytes: Required[int]

    references: Iterable[ReferenceSourceParam]
    """Optional agent-declared sources.

    Omitted and empty references are equivalent. Sources require current read
    authorization as well as source scope. All tuples are validated before transfer
    creation and before publication. Removing references permits saving an
    unrecorded output.
    """
