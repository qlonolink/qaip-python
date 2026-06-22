# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.user_keyword_snapshot import UserKeywordSnapshot

__all__ = ["UserKeywordSnapshotsResource", "AsyncUserKeywordSnapshotsResource"]


class UserKeywordSnapshotsResource(SyncAPIResource):
    """User keyword snapshot management"""

    @cached_property
    def with_raw_response(self) -> UserKeywordSnapshotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return UserKeywordSnapshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserKeywordSnapshotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return UserKeywordSnapshotsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserKeywordSnapshot:
        """
        Snapshots the authenticated user's current keywords and triggers re-indexing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user-keyword-snapshots",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserKeywordSnapshot,
        )


class AsyncUserKeywordSnapshotsResource(AsyncAPIResource):
    """User keyword snapshot management"""

    @cached_property
    def with_raw_response(self) -> AsyncUserKeywordSnapshotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserKeywordSnapshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserKeywordSnapshotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncUserKeywordSnapshotsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserKeywordSnapshot:
        """
        Snapshots the authenticated user's current keywords and triggers re-indexing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user-keyword-snapshots",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserKeywordSnapshot,
        )


class UserKeywordSnapshotsResourceWithRawResponse:
    def __init__(self, user_keyword_snapshots: UserKeywordSnapshotsResource) -> None:
        self._user_keyword_snapshots = user_keyword_snapshots

        self.create = to_raw_response_wrapper(
            user_keyword_snapshots.create,
        )


class AsyncUserKeywordSnapshotsResourceWithRawResponse:
    def __init__(self, user_keyword_snapshots: AsyncUserKeywordSnapshotsResource) -> None:
        self._user_keyword_snapshots = user_keyword_snapshots

        self.create = async_to_raw_response_wrapper(
            user_keyword_snapshots.create,
        )


class UserKeywordSnapshotsResourceWithStreamingResponse:
    def __init__(self, user_keyword_snapshots: UserKeywordSnapshotsResource) -> None:
        self._user_keyword_snapshots = user_keyword_snapshots

        self.create = to_streamed_response_wrapper(
            user_keyword_snapshots.create,
        )


class AsyncUserKeywordSnapshotsResourceWithStreamingResponse:
    def __init__(self, user_keyword_snapshots: AsyncUserKeywordSnapshotsResource) -> None:
        self._user_keyword_snapshots = user_keyword_snapshots

        self.create = async_to_streamed_response_wrapper(
            user_keyword_snapshots.create,
        )
