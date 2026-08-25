# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .secret_type import SecretType

__all__ = ["SecretCreateParams", "ChartmetricConsent"]


class SecretCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the secret"""

    secret: Required[str]
    """The secret value"""

    type: Required[SecretType]
    """The type of the secret"""

    chartmetric_consent: Optional[ChartmetricConsent]
    """Explicit consent for the Chartmetric plan and build-embedded data-use profile.

    This object is required only when creating a Chartmetric secret.
    """

    description: str
    """Description of the secret"""


class ChartmetricConsent(TypedDict, total=False):
    """Explicit consent for the Chartmetric plan and build-embedded data-use profile.

    This object is required only when creating a Chartmetric secret.
    """

    accept_history_storage: Required[Literal[True]]

    accept_llm_processing: Required[Literal[True]]

    accept_quota_rate_cost: Required[Literal[True]]

    accept_retention_deletion: Required[Literal[True]]

    data_use_profile: Required[str]

    enable_for_all_agents: Required[Literal[True]]

    plan_profile: Required[str]
