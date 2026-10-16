# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .search_source import SearchSource

__all__ = ["SearchEvidence"]


class SearchEvidence(BaseModel):
    evidence_id: str

    excerpt: str
    """A UTF-8 prefix of verified chunk text, bounded to 2048 encoded bytes."""

    excerpt_truncated: bool

    page_order: int

    source: SearchSource
    """Fixed reference tuple accepted by create_transfer.references.

    Display and page are always present here.
    """
