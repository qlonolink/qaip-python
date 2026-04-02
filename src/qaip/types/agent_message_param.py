# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypedDict

from .shared.message_role import MessageRole
from .agent_message_content_param import AgentMessageContentParam

__all__ = ["AgentMessageParam"]


class AgentMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[AgentMessageContentParam]]]

    role: Required[MessageRole]
    """The role of the message sender"""
