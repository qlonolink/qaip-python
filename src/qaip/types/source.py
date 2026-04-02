# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.metadata import Metadata
from .shared.file_type import FileType

__all__ = ["Source"]


class Source(BaseModel):
    id: str
    """Source ID (file ID)"""

    name: str
    """Name of the source (file name)"""

    source_group_id: str
    """Parent source group ID"""

    file_size: Optional[int] = None
    """File size in bytes"""

    file_type: Optional[FileType] = None
    """The type of the source file"""

    metadata: Optional[Metadata] = None
