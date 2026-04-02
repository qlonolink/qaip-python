# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TagSourceGroupDeleteParams"]


class TagSourceGroupDeleteParams(TypedDict, total=False):
    source_group_id: Required[str]
    """Source group ID.

    The source group ID corresponds to the job ID for each data source.
    """

    tag_id: Required[str]
    """Tag ID"""
