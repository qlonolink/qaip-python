# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["AgentRunStatus"]

AgentRunStatus: TypeAlias = Literal["QUEUED", "RUNNING", "CANCELLING", "SUCCEEDED", "FAILED", "CANCELLED"]
