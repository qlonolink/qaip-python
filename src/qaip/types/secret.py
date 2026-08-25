# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .secret_type import SecretType

__all__ = ["Secret", "ChartmetricConsent"]


class ChartmetricConsent(BaseModel):
    accepted_at: int
    """Consent acceptance time (Unix timestamp in seconds)"""

    data_use_profile: str

    plan_profile: str


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

    chartmetric_consent: Optional[ChartmetricConsent] = None

    chartmetric_lifecycle_state: Optional[Literal["pending_create", "active", "pending_update", "pending_delete"]] = (
        None
    )
    """Persistent lifecycle state of a Chartmetric credential"""

    description: Optional[str] = None
    """Description of the secret"""
