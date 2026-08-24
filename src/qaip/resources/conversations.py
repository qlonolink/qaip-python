# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    conversation_list_params,
    conversation_scope_params,
    conversation_update_params,
    conversation_retrieve_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.conversation import Conversation
from ..types.conversation_detail import ConversationDetail
from ..types.conversation_list_response import ConversationListResponse

__all__ = ["ConversationsResource", "AsyncConversationsResource"]


class ConversationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConversationsResourceWithRawResponse:
        return ConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationsResourceWithStreamingResponse:
        return ConversationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        all_principals: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        principal_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationListResponse:
        return self._get(
            "/conversations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "all_principals": all_principals,
                        "limit": limit,
                        "offset": offset,
                        "principal_id": principal_id,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=ConversationListResponse,
        )

    def retrieve(
        self,
        conversation_id: str,
        *,
        leaf_id: str | Omit = omit,
        principal_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationDetail:
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get(
            path_template("/conversations/{conversation_id}", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"leaf_id": leaf_id, "principal_id": principal_id},
                    conversation_retrieve_params.ConversationRetrieveParams,
                ),
            ),
            cast_to=ConversationDetail,
        )

    def update(
        self,
        conversation_id: str,
        *,
        current_leaf_id: str | Omit = omit,
        title: str | Omit = omit,
        principal_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Conversation:
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._patch(
            path_template("/conversations/{conversation_id}", conversation_id=conversation_id),
            body=maybe_transform(
                {"current_leaf_id": current_leaf_id, "title": title},
                conversation_update_params.ConversationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"principal_id": principal_id}, conversation_scope_params.ConversationScopeParams
                ),
            ),
            cast_to=Conversation,
        )

    def delete(
        self,
        conversation_id: str,
        *,
        principal_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/conversations/{conversation_id}", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"principal_id": principal_id}, conversation_scope_params.ConversationScopeParams
                ),
            ),
            cast_to=NoneType,
        )


class AsyncConversationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConversationsResourceWithRawResponse:
        return AsyncConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationsResourceWithStreamingResponse:
        return AsyncConversationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        all_principals: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        principal_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationListResponse:
        return await self._get(
            "/conversations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "all_principals": all_principals,
                        "limit": limit,
                        "offset": offset,
                        "principal_id": principal_id,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=ConversationListResponse,
        )

    async def retrieve(
        self,
        conversation_id: str,
        *,
        leaf_id: str | Omit = omit,
        principal_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationDetail:
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._get(
            path_template("/conversations/{conversation_id}", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"leaf_id": leaf_id, "principal_id": principal_id},
                    conversation_retrieve_params.ConversationRetrieveParams,
                ),
            ),
            cast_to=ConversationDetail,
        )

    async def update(
        self,
        conversation_id: str,
        *,
        current_leaf_id: str | Omit = omit,
        title: str | Omit = omit,
        principal_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Conversation:
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._patch(
            path_template("/conversations/{conversation_id}", conversation_id=conversation_id),
            body=await async_maybe_transform(
                {"current_leaf_id": current_leaf_id, "title": title},
                conversation_update_params.ConversationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"principal_id": principal_id}, conversation_scope_params.ConversationScopeParams
                ),
            ),
            cast_to=Conversation,
        )

    async def delete(
        self,
        conversation_id: str,
        *,
        principal_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/conversations/{conversation_id}", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"principal_id": principal_id}, conversation_scope_params.ConversationScopeParams
                ),
            ),
            cast_to=NoneType,
        )


class ConversationsResourceWithRawResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self.list = to_raw_response_wrapper(conversations.list)
        self.retrieve = to_raw_response_wrapper(conversations.retrieve)
        self.update = to_raw_response_wrapper(conversations.update)
        self.delete = to_raw_response_wrapper(conversations.delete)


class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self.list = async_to_raw_response_wrapper(conversations.list)
        self.retrieve = async_to_raw_response_wrapper(conversations.retrieve)
        self.update = async_to_raw_response_wrapper(conversations.update)
        self.delete = async_to_raw_response_wrapper(conversations.delete)


class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self.list = to_streamed_response_wrapper(conversations.list)
        self.retrieve = to_streamed_response_wrapper(conversations.retrieve)
        self.update = to_streamed_response_wrapper(conversations.update)
        self.delete = to_streamed_response_wrapper(conversations.delete)


class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self.list = async_to_streamed_response_wrapper(conversations.list)
        self.retrieve = async_to_streamed_response_wrapper(conversations.retrieve)
        self.update = async_to_streamed_response_wrapper(conversations.update)
        self.delete = async_to_streamed_response_wrapper(conversations.delete)
