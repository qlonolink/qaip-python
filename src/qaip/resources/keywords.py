# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import keyword_list_params, keyword_create_params, keyword_update_params
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
from ..types.keyword import Keyword
from ..types.keyword_list_response import KeywordListResponse

__all__ = ["KeywordsResource", "AsyncKeywordsResource"]


class KeywordsResource(SyncAPIResource):
    """Keyword management"""

    @cached_property
    def with_raw_response(self) -> KeywordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return KeywordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeywordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return KeywordsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        meaning: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Keyword:
        """
        Creates a new keyword for the authenticated user.

        Args:
          name: Name of the keyword

          meaning: Meaning of the keyword

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/keywords",
            body=maybe_transform(
                {
                    "name": name,
                    "meaning": meaning,
                },
                keyword_create_params.KeywordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Keyword,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Keyword:
        """
        Gets a specific keyword by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/keywords/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Keyword,
        )

    def update(
        self,
        id: str,
        *,
        name: str,
        meaning: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Keyword:
        """
        Updates an existing keyword.

        Args:
          name: Name of the keyword

          meaning: Meaning of the keyword

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/keywords/{id}", id=id),
            body=maybe_transform(
                {
                    "name": name,
                    "meaning": meaning,
                },
                keyword_update_params.KeywordUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Keyword,
        )

    def list(
        self,
        *,
        offset: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_field: str | Omit = omit,
        sort_order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeywordListResponse:
        """
        Lists the authenticated user's keywords.

        Args:
          offset: Number of records to skip

          page_size: Maximum number of results to return

          sort_field: Field to sort by

          sort_order: Sort order (e.g. "asc" or "desc")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/keywords",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "offset": offset,
                        "page_size": page_size,
                        "sort_field": sort_field,
                        "sort_order": sort_order,
                    },
                    keyword_list_params.KeywordListParams,
                ),
            ),
            cast_to=KeywordListResponse,
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
    ) -> Keyword:
        """
        Deletes an existing keyword.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/keywords/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Keyword,
        )


class AsyncKeywordsResource(AsyncAPIResource):
    """Keyword management"""

    @cached_property
    def with_raw_response(self) -> AsyncKeywordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeywordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeywordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncKeywordsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        meaning: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Keyword:
        """
        Creates a new keyword for the authenticated user.

        Args:
          name: Name of the keyword

          meaning: Meaning of the keyword

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/keywords",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "meaning": meaning,
                },
                keyword_create_params.KeywordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Keyword,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Keyword:
        """
        Gets a specific keyword by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/keywords/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Keyword,
        )

    async def update(
        self,
        id: str,
        *,
        name: str,
        meaning: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Keyword:
        """
        Updates an existing keyword.

        Args:
          name: Name of the keyword

          meaning: Meaning of the keyword

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/keywords/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "meaning": meaning,
                },
                keyword_update_params.KeywordUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Keyword,
        )

    async def list(
        self,
        *,
        offset: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_field: str | Omit = omit,
        sort_order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeywordListResponse:
        """
        Lists the authenticated user's keywords.

        Args:
          offset: Number of records to skip

          page_size: Maximum number of results to return

          sort_field: Field to sort by

          sort_order: Sort order (e.g. "asc" or "desc")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/keywords",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "offset": offset,
                        "page_size": page_size,
                        "sort_field": sort_field,
                        "sort_order": sort_order,
                    },
                    keyword_list_params.KeywordListParams,
                ),
            ),
            cast_to=KeywordListResponse,
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
    ) -> Keyword:
        """
        Deletes an existing keyword.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/keywords/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Keyword,
        )


class KeywordsResourceWithRawResponse:
    def __init__(self, keywords: KeywordsResource) -> None:
        self._keywords = keywords

        self.create = to_raw_response_wrapper(
            keywords.create,
        )
        self.retrieve = to_raw_response_wrapper(
            keywords.retrieve,
        )
        self.update = to_raw_response_wrapper(
            keywords.update,
        )
        self.list = to_raw_response_wrapper(
            keywords.list,
        )
        self.delete = to_raw_response_wrapper(
            keywords.delete,
        )


class AsyncKeywordsResourceWithRawResponse:
    def __init__(self, keywords: AsyncKeywordsResource) -> None:
        self._keywords = keywords

        self.create = async_to_raw_response_wrapper(
            keywords.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            keywords.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            keywords.update,
        )
        self.list = async_to_raw_response_wrapper(
            keywords.list,
        )
        self.delete = async_to_raw_response_wrapper(
            keywords.delete,
        )


class KeywordsResourceWithStreamingResponse:
    def __init__(self, keywords: KeywordsResource) -> None:
        self._keywords = keywords

        self.create = to_streamed_response_wrapper(
            keywords.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            keywords.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            keywords.update,
        )
        self.list = to_streamed_response_wrapper(
            keywords.list,
        )
        self.delete = to_streamed_response_wrapper(
            keywords.delete,
        )


class AsyncKeywordsResourceWithStreamingResponse:
    def __init__(self, keywords: AsyncKeywordsResource) -> None:
        self._keywords = keywords

        self.create = async_to_streamed_response_wrapper(
            keywords.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            keywords.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            keywords.update,
        )
        self.list = async_to_streamed_response_wrapper(
            keywords.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            keywords.delete,
        )
