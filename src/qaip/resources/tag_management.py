# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import tag_management_create_params, tag_management_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.shared.tag import Tag

__all__ = ["TagManagementResource", "AsyncTagManagementResource"]


class TagManagementResource(SyncAPIResource):
    """List available tags"""

    @cached_property
    def with_raw_response(self) -> TagManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return TagManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return TagManagementResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tag:
        """<p> Creates a new tag.

        </p> <p> Required scope: `knowledge:write` </p>

        Args:
          name: Tag name

          description: Tag description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tags",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                tag_management_create_params.TagManagementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )

    def update(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tag:
        """<p> Updates an existing tag's name or description.

        This is a partial update: only fields provided with a non-empty value are changed; fields that are omitted or sent as an empty string are left unchanged. The tag color is managed in the dashboard and is always preserved. </p> <p> Required scope: `knowledge:write` </p>

        Args:
          description: New tag description. Omit or send an empty string to leave unchanged.

          name: New tag name. Omit or send an empty string to leave unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/tags/{id}", id=id),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                tag_management_update_params.TagManagementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tag:
        """<p> Deletes a tag.

        Associated tag-source-group links are also removed. </p> <p> Required scope: `knowledge:write` </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/tags/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )


class AsyncTagManagementResource(AsyncAPIResource):
    """List available tags"""

    @cached_property
    def with_raw_response(self) -> AsyncTagManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTagManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncTagManagementResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tag:
        """<p> Creates a new tag.

        </p> <p> Required scope: `knowledge:write` </p>

        Args:
          name: Tag name

          description: Tag description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tags",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                tag_management_create_params.TagManagementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )

    async def update(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tag:
        """<p> Updates an existing tag's name or description.

        This is a partial update: only fields provided with a non-empty value are changed; fields that are omitted or sent as an empty string are left unchanged. The tag color is managed in the dashboard and is always preserved. </p> <p> Required scope: `knowledge:write` </p>

        Args:
          description: New tag description. Omit or send an empty string to leave unchanged.

          name: New tag name. Omit or send an empty string to leave unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/tags/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                tag_management_update_params.TagManagementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tag:
        """<p> Deletes a tag.

        Associated tag-source-group links are also removed. </p> <p> Required scope: `knowledge:write` </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/tags/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )


class TagManagementResourceWithRawResponse:
    def __init__(self, tag_management: TagManagementResource) -> None:
        self._tag_management = tag_management

        self.create = to_raw_response_wrapper(
            tag_management.create,
        )
        self.update = to_raw_response_wrapper(
            tag_management.update,
        )
        self.delete = to_raw_response_wrapper(
            tag_management.delete,
        )


class AsyncTagManagementResourceWithRawResponse:
    def __init__(self, tag_management: AsyncTagManagementResource) -> None:
        self._tag_management = tag_management

        self.create = async_to_raw_response_wrapper(
            tag_management.create,
        )
        self.update = async_to_raw_response_wrapper(
            tag_management.update,
        )
        self.delete = async_to_raw_response_wrapper(
            tag_management.delete,
        )


class TagManagementResourceWithStreamingResponse:
    def __init__(self, tag_management: TagManagementResource) -> None:
        self._tag_management = tag_management

        self.create = to_streamed_response_wrapper(
            tag_management.create,
        )
        self.update = to_streamed_response_wrapper(
            tag_management.update,
        )
        self.delete = to_streamed_response_wrapper(
            tag_management.delete,
        )


class AsyncTagManagementResourceWithStreamingResponse:
    def __init__(self, tag_management: AsyncTagManagementResource) -> None:
        self._tag_management = tag_management

        self.create = async_to_streamed_response_wrapper(
            tag_management.create,
        )
        self.update = async_to_streamed_response_wrapper(
            tag_management.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            tag_management.delete,
        )
