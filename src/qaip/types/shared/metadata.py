# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .metadata_record import MetadataRecord

__all__ = ["Metadata"]


class Metadata(BaseModel):
    records: Optional[List[MetadataRecord]] = None
    """List of metadata records.

    A patch may contain up to 40 items; the merged result is capped at 20.
    """
