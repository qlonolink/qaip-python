# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes, SequenceNotStr

__all__ = ["LocalFileGroupCreateParams"]


class LocalFileGroupCreateParams(TypedDict, total=False):
    files: Required[SequenceNotStr[FileTypes]]
    """Files to upload"""

    last_modified: Required[SequenceNotStr[str]]
    """
    Last modified timestamps in Unix epoch milliseconds (integer) for each file
    (same order and count as files). For example, 1709971200000 represents
    2024-03-09T12:00:00Z.
    """

    name: Required[str]
    """Name of the local file group"""

    chunk_metadata_keys: str
    """JSON array of chunk metadata key configurations.

    Each element is an object with "key" (string) and "type" (one of "string",
    "integer", "float", "date", "datetime"). Example:
    [{"key":"author","type":"string"},{"key":"page_number","type":"integer"}]
    """
