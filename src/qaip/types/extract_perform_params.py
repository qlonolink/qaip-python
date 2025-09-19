# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .file_type import FileType
from .source_type import SourceType

__all__ = ["ExtractPerformParams"]


class ExtractPerformParams(TypedDict, total=False):
    schema: Required[object]
    """JSON Schema for the data to be extracted."""

    date_from: int
    """Start date for content search (Unix timestamp in seconds)"""

    date_to: int
    """End date for content search (Unix timestamp in seconds)"""

    domains: SequenceNotStr[str]

    file_types: List[FileType]

    limit: int

    llm_model: str
    """LLM model to use (e.g., gpt-4.1, defaults to gpt-4.1 if not specified)."""

    offset: int

    prompt: str
    """
    Additional prompt for the LLM (optional, if not specified, a default prompt in
    Japanese will be used).
    """

    source_types: List[SourceType]

    tag_ids: SequenceNotStr[str]
