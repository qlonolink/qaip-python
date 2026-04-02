# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import tag_source_group_create_params, tag_source_group_delete_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared.tag_source_group import TagSourceGroup

__all__ = ["TagSourceGroupsResource", "AsyncTagSourceGroupsResource"]


class TagSourceGroupsResource(SyncAPIResource):
    """Tag and source group associations"""

    @cached_property
    def with_raw_response(self) -> TagSourceGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return TagSourceGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagSourceGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return TagSourceGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        source_group_id: str,
        tag_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagSourceGroup:
        """<p> Creates a new tag source group association.

        A source group is a collection of files ingested by a single job. </p> <p> Required roles: All </p>

        Args:
          source_group_id: Source group ID. The source group ID corresponds to the job ID for each data
              source.

          tag_id: Tag ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tag-source-groups",
            body=maybe_transform(
                {
                    "source_group_id": source_group_id,
                    "tag_id": tag_id,
                },
                tag_source_group_create_params.TagSourceGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagSourceGroup,
        )

    def delete(
        self,
        *,
        source_group_id: str,
        tag_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagSourceGroup:
        """<p> Deletes a tag source group association.

        </p> <p> Required roles: All </p>

        Args:
          source_group_id: Source group ID. The source group ID corresponds to the job ID for each data
              source.

          tag_id: Tag ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/tag-source-groups",
            body=maybe_transform(
                {
                    "source_group_id": source_group_id,
                    "tag_id": tag_id,
                },
                tag_source_group_delete_params.TagSourceGroupDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagSourceGroup,
        )


class AsyncTagSourceGroupsResource(AsyncAPIResource):
    """Tag and source group associations"""

    @cached_property
    def with_raw_response(self) -> AsyncTagSourceGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTagSourceGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagSourceGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncTagSourceGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        source_group_id: str,
        tag_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagSourceGroup:
        """<p> Creates a new tag source group association.

        A source group is a collection of files ingested by a single job. </p> <p> Required roles: All </p>

        Args:
          source_group_id: Source group ID. The source group ID corresponds to the job ID for each data
              source.

          tag_id: Tag ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tag-source-groups",
            body=await async_maybe_transform(
                {
                    "source_group_id": source_group_id,
                    "tag_id": tag_id,
                },
                tag_source_group_create_params.TagSourceGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagSourceGroup,
        )

    async def delete(
        self,
        *,
        source_group_id: str,
        tag_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagSourceGroup:
        """<p> Deletes a tag source group association.

        </p> <p> Required roles: All </p>

        Args:
          source_group_id: Source group ID. The source group ID corresponds to the job ID for each data
              source.

          tag_id: Tag ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/tag-source-groups",
            body=await async_maybe_transform(
                {
                    "source_group_id": source_group_id,
                    "tag_id": tag_id,
                },
                tag_source_group_delete_params.TagSourceGroupDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagSourceGroup,
        )


class TagSourceGroupsResourceWithRawResponse:
    def __init__(self, tag_source_groups: TagSourceGroupsResource) -> None:
        self._tag_source_groups = tag_source_groups

        self.create = to_raw_response_wrapper(
            tag_source_groups.create,
        )
        self.delete = to_raw_response_wrapper(
            tag_source_groups.delete,
        )


class AsyncTagSourceGroupsResourceWithRawResponse:
    def __init__(self, tag_source_groups: AsyncTagSourceGroupsResource) -> None:
        self._tag_source_groups = tag_source_groups

        self.create = async_to_raw_response_wrapper(
            tag_source_groups.create,
        )
        self.delete = async_to_raw_response_wrapper(
            tag_source_groups.delete,
        )


class TagSourceGroupsResourceWithStreamingResponse:
    def __init__(self, tag_source_groups: TagSourceGroupsResource) -> None:
        self._tag_source_groups = tag_source_groups

        self.create = to_streamed_response_wrapper(
            tag_source_groups.create,
        )
        self.delete = to_streamed_response_wrapper(
            tag_source_groups.delete,
        )


class AsyncTagSourceGroupsResourceWithStreamingResponse:
    def __init__(self, tag_source_groups: AsyncTagSourceGroupsResource) -> None:
        self._tag_source_groups = tag_source_groups

        self.create = async_to_streamed_response_wrapper(
            tag_source_groups.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            tag_source_groups.delete,
        )
