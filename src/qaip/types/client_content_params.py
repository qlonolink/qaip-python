# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ClientContentParams"]


class ClientContentParams(TypedDict, total=False):
    authz_policy: str
    """
    (reserved for future use) Name of the registered authz policy to evaluate when
    fetching the content. Defaults to the reserved "default" policy when omitted.
    Ignored when authz is disabled.
    """

    principal_id: str
    """
    Identifier of the end-user (principal) on whose behalf the content is fetched.
    Used to look up authz subject attributes. Empty subject when omitted. Ignored
    when authz disabled.
    """
