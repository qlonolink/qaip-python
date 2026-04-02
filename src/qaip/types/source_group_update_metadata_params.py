# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.metadata import Metadata

__all__ = ["SourceGroupUpdateMetadataParams"]


class SourceGroupUpdateMetadataParams(TypedDict, total=False):
    metadata: Required[Metadata]
