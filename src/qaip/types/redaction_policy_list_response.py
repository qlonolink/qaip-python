# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .policy_summary import PolicySummary

__all__ = ["RedactionPolicyListResponse"]


class RedactionPolicyListResponse(BaseModel):
    policies: List[PolicySummary]
