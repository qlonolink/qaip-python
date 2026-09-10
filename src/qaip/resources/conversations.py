# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    conversation_list_params,
    conversation_delete_params,
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return ConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return ConversationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        conversation_id: str,
        *,
        leaf_id: str | Omit = omit,
        principal_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationDetail:
        """
        <p> Get a conversation's active path (the messages from a leaf back to the root) plus a lightweight tree of all nodes (id/parent_id/role) for branch navigation. Pass leaf_id to preview a specific branch without changing the persisted current leaf. </p> <p> Required scope: `inference:run` </p>

        Args:
          leaf_id: Leaf node to build active_path from. When set, returns that branch's path
              without mutating current_leaf_id (non-destructive preview). When omitted, uses
              the conversation's current_leaf_id. Must belong to the conversation.

          principal_id: Scope the target by principal. If omitted, only a conversation with no principal
              (principal_id is null) is addressed; a conversation whose principal differs
              yields 404.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
                    {
                        "leaf_id": leaf_id,
                        "principal_id": principal_id,
                    },
                    conversation_retrieve_params.ConversationRetrieveParams,
                ),
            ),
            cast_to=ConversationDetail,
        )

    def update(
        self,
        conversation_id: str,
        *,
        principal_id: str | Omit = omit,
        current_leaf_id: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Conversation:
        """
        <p> Update a conversation's title and/or switch the active branch by setting current_leaf_id to another node in the same conversation. </p> <p> Required scope: `inference:run` </p>

        Args:
          principal_id: Scope the target by principal. If omitted, only a conversation with no principal
              (principal_id is null) is addressed; a conversation whose principal differs
              yields 404.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._patch(
            path_template("/conversations/{conversation_id}", conversation_id=conversation_id),
            body=maybe_transform(
                {
                    "current_leaf_id": current_leaf_id,
                    "title": title,
                },
                conversation_update_params.ConversationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"principal_id": principal_id}, conversation_update_params.ConversationUpdateParams
                ),
            ),
            cast_to=Conversation,
        )

    def list(
        self,
        *,
        all_principals: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        principal_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationListResponse:
        """
        <p> List the caller's conversations (most recently updated first, excluding deleted ones). </p> <p> Required scope: `inference:run` </p>

        Args:
          all_principals: If true, return conversations across all principals in the tenant. Mutually
              exclusive with principal_id (400 if both are set).

          principal_id: Filter by principal. If set, only conversations belonging to this principal are
              returned. If omitted, only conversations with no principal (principal_id is
              null) are returned. Mutually exclusive with all_principals=true (400 if both are
              set).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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

    def delete(
        self,
        conversation_id: str,
        *,
        principal_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """<p> Delete a conversation.

        Afterwards it no longer appears in the list or can be retrieved. </p> <p> Required scope: `inference:run` </p>

        Args:
          principal_id: Scope the target by principal. If omitted, only a conversation with no principal
              (principal_id is null) is addressed; a conversation whose principal differs
              yields 404.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
                    {"principal_id": principal_id}, conversation_delete_params.ConversationDeleteParams
                ),
            ),
            cast_to=NoneType,
        )


class AsyncConversationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncConversationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        conversation_id: str,
        *,
        leaf_id: str | Omit = omit,
        principal_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationDetail:
        """
        <p> Get a conversation's active path (the messages from a leaf back to the root) plus a lightweight tree of all nodes (id/parent_id/role) for branch navigation. Pass leaf_id to preview a specific branch without changing the persisted current leaf. </p> <p> Required scope: `inference:run` </p>

        Args:
          leaf_id: Leaf node to build active_path from. When set, returns that branch's path
              without mutating current_leaf_id (non-destructive preview). When omitted, uses
              the conversation's current_leaf_id. Must belong to the conversation.

          principal_id: Scope the target by principal. If omitted, only a conversation with no principal
              (principal_id is null) is addressed; a conversation whose principal differs
              yields 404.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
                    {
                        "leaf_id": leaf_id,
                        "principal_id": principal_id,
                    },
                    conversation_retrieve_params.ConversationRetrieveParams,
                ),
            ),
            cast_to=ConversationDetail,
        )

    async def update(
        self,
        conversation_id: str,
        *,
        principal_id: str | Omit = omit,
        current_leaf_id: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Conversation:
        """
        <p> Update a conversation's title and/or switch the active branch by setting current_leaf_id to another node in the same conversation. </p> <p> Required scope: `inference:run` </p>

        Args:
          principal_id: Scope the target by principal. If omitted, only a conversation with no principal
              (principal_id is null) is addressed; a conversation whose principal differs
              yields 404.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._patch(
            path_template("/conversations/{conversation_id}", conversation_id=conversation_id),
            body=await async_maybe_transform(
                {
                    "current_leaf_id": current_leaf_id,
                    "title": title,
                },
                conversation_update_params.ConversationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"principal_id": principal_id}, conversation_update_params.ConversationUpdateParams
                ),
            ),
            cast_to=Conversation,
        )

    async def list(
        self,
        *,
        all_principals: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        principal_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationListResponse:
        """
        <p> List the caller's conversations (most recently updated first, excluding deleted ones). </p> <p> Required scope: `inference:run` </p>

        Args:
          all_principals: If true, return conversations across all principals in the tenant. Mutually
              exclusive with principal_id (400 if both are set).

          principal_id: Filter by principal. If set, only conversations belonging to this principal are
              returned. If omitted, only conversations with no principal (principal_id is
              null) are returned. Mutually exclusive with all_principals=true (400 if both are
              set).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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

    async def delete(
        self,
        conversation_id: str,
        *,
        principal_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """<p> Delete a conversation.

        Afterwards it no longer appears in the list or can be retrieved. </p> <p> Required scope: `inference:run` </p>

        Args:
          principal_id: Scope the target by principal. If omitted, only a conversation with no principal
              (principal_id is null) is addressed; a conversation whose principal differs
              yields 404.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
                    {"principal_id": principal_id}, conversation_delete_params.ConversationDeleteParams
                ),
            ),
            cast_to=NoneType,
        )


class ConversationsResourceWithRawResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.retrieve = to_raw_response_wrapper(
            conversations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            conversations.update,
        )
        self.list = to_raw_response_wrapper(
            conversations.list,
        )
        self.delete = to_raw_response_wrapper(
            conversations.delete,
        )


class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.retrieve = async_to_raw_response_wrapper(
            conversations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            conversations.update,
        )
        self.list = async_to_raw_response_wrapper(
            conversations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            conversations.delete,
        )


class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.retrieve = to_streamed_response_wrapper(
            conversations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            conversations.update,
        )
        self.list = to_streamed_response_wrapper(
            conversations.list,
        )
        self.delete = to_streamed_response_wrapper(
            conversations.delete,
        )


class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.retrieve = async_to_streamed_response_wrapper(
            conversations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            conversations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            conversations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            conversations.delete,
        )
