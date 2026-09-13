# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["LocalFileGroupStartChunkDeletionParams"]


class LocalFileGroupStartChunkDeletionParams(TypedDict, total=False):
    text_contains: Required[SequenceNotStr[str]]
    """OR list of substrings.

    Chunk rows whose text (raw JSONL line) contains any of these substrings (literal
    match) are deleted. Raw SQL is not accepted.
    """
