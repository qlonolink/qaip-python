# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExternalQueryCreateParams"]


class ExternalQueryCreateParams(TypedDict, total=False):
    sql: Required[str]
    """A single read-only SELECT using logical table names."""
