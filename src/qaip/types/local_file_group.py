# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.metadata import Metadata
from .shared.job_error import JobError
from .shared.job_status import JobStatus
from .chunk_metadata_key_config import ChunkMetadataKeyConfig

__all__ = ["LocalFileGroup"]


class LocalFileGroup(BaseModel):
    id: str
    """Local file group ID"""

    name: str
    """Local file group name"""

    status: JobStatus
    """Job status"""

    chunk_metadata_keys: Optional[List[ChunkMetadataKeyConfig]] = None
    """Chunk metadata key configurations"""

    chunk_metadatas_count: Optional[int] = None
    """Number of chunk metadata records extracted for this local file group"""

    creation_time: Optional[int] = None
    """Creation time (Unix timestamp in seconds)"""

    end_time: Optional[int] = None
    """End time (Unix timestamp in seconds)"""

    error: Optional[JobError] = None

    metadata: Optional[Metadata] = None
    """(reserved for future use) Additional metadata for the local file group"""

    start_time: Optional[int] = None
    """Start time (Unix timestamp in seconds)"""

    upload_time: Optional[int] = None
    """Upload time (Unix timestamp in seconds)"""
