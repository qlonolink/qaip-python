# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .metadata_record import MetadataRecord

__all__ = ["Metadata"]


class Metadata(TypedDict, total=False):
    records: Iterable[MetadataRecord]
    """List of metadata records.

    A patch may contain up to 40 items; the merged result is capped at 20.
    """
