# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import search_query_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.file_type import FileType
from ..types.source_type import SourceType
from ..types.search_query_response import SearchQueryResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/qaip-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/qaip-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def query(
        self,
        *,
        query: str,
        date_from: int | Omit = omit,
        date_to: int | Omit = omit,
        domains: SequenceNotStr[str] | Omit = omit,
        file_types: List[FileType] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        source_types: List[SourceType] | Omit = omit,
        tag_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchQueryResponse:
        """
        Searches through indexed content using query

        Args:
          query: Search query string

          date_from: Start date for content search (Unix timestamp in seconds)

          date_to: End date for content search (Unix timestamp in seconds)

          domains: Array of domains to search within (supports partial matching)

          limit: Maximum number of results to return

          offset: Number of results to skip

          tag_ids: target tag IDs to be obtained

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/search",
            body=maybe_transform(
                {
                    "query": query,
                    "date_from": date_from,
                    "date_to": date_to,
                    "domains": domains,
                    "file_types": file_types,
                    "limit": limit,
                    "offset": offset,
                    "source_types": source_types,
                    "tag_ids": tag_ids,
                },
                search_query_params.SearchQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchQueryResponse,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/qaip-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def query(
        self,
        *,
        query: str,
        date_from: int | Omit = omit,
        date_to: int | Omit = omit,
        domains: SequenceNotStr[str] | Omit = omit,
        file_types: List[FileType] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        source_types: List[SourceType] | Omit = omit,
        tag_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchQueryResponse:
        """
        Searches through indexed content using query

        Args:
          query: Search query string

          date_from: Start date for content search (Unix timestamp in seconds)

          date_to: End date for content search (Unix timestamp in seconds)

          domains: Array of domains to search within (supports partial matching)

          limit: Maximum number of results to return

          offset: Number of results to skip

          tag_ids: target tag IDs to be obtained

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "date_from": date_from,
                    "date_to": date_to,
                    "domains": domains,
                    "file_types": file_types,
                    "limit": limit,
                    "offset": offset,
                    "source_types": source_types,
                    "tag_ids": tag_ids,
                },
                search_query_params.SearchQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchQueryResponse,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.query = to_raw_response_wrapper(
            search.query,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.query = async_to_raw_response_wrapper(
            search.query,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.query = to_streamed_response_wrapper(
            search.query,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.query = async_to_streamed_response_wrapper(
            search.query,
        )
