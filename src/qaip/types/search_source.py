# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SearchSource"]


class SearchSource(BaseModel):
    """Fixed reference tuple accepted by create_transfer.references.

    Display and page are always present here.
    """

    display_revision_id: str

    file_id: str

    page_id: str

    revision_id: str
