# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ReferenceSourceParam"]


class ReferenceSourceParam(TypedDict, total=False):
    """Fixed source tuple.

    page_id requires display_revision_id. Every ID must exist and correspond within the current source scope. Invalid, unknown or inaccessible tuples return the same reference_validation_failed error.
    """

    file_id: Required[str]
    """Canonical lowercase nonzero UUID."""

    revision_id: Required[str]
    """Canonical lowercase nonzero UUID."""

    display_revision_id: str
    """Canonical lowercase nonzero UUID."""

    page_id: str
    """Canonical lowercase nonzero UUID."""
