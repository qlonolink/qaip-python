# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["IssuableApiKeyScope"]

IssuableApiKeyScope: TypeAlias = Literal[
    "inference:run",
    "knowledge:read",
    "knowledge:write",
    "ingestion:manage",
    "secrets:read",
    "secrets:write",
    "policy:redaction:manage",
    "policy:authz:manage",
    "authz:grant",
]
