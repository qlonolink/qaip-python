# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["IssuableAPIKeyScope", "IssuableApiKeyScope"]

IssuableAPIKeyScope: TypeAlias = Literal[
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


# 公開済みの型名を維持する。
IssuableApiKeyScope = IssuableAPIKeyScope
