# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .page import Page
from .._models import BaseModel

__all__ = ["DisplayManifest"]


class DisplayManifest(BaseModel):
    id: str
    """Canonical lowercase nonzero UUID."""

    file_id: str
    """Canonical lowercase nonzero UUID."""

    font_sha256: str

    pages: List[Page]

    renderer_version: str

    revision_id: str
    """Canonical lowercase nonzero UUID."""

    settings_sha256: str

    sha256: str
