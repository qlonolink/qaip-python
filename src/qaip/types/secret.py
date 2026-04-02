# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .secret_type import SecretType

__all__ = ["Secret"]


class Secret(BaseModel):
    id: str
    """Secret ID"""

    creation_time: int
    """Creation time (Unix timestamp in seconds)"""

    last_update_time: int
    """Last updated time (Unix timestamp in seconds)"""

    name: str
    """Name of the secret"""

    type: SecretType
    """The type of the secret"""

    description: Optional[str] = None
    """Description of the secret"""
