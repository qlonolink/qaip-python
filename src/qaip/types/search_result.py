# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .search_evidence import SearchEvidence

__all__ = ["SearchResult"]


class SearchResult(BaseModel):
    analysis_generation_id: str

    display_revision_id: str

    evidence: List[SearchEvidence]

    file_id: str

    name: str

    reason: str

    revision_id: str
