# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ..types import external_query_create_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.external_query_create_response import ExternalQueryCreateResponse
from ..types.external_table_schema_response import ExternalTableSchemaResponse
from ..types.external_query_state_only_response import ExternalQueryStateOnlyResponse

__all__ = ["ExternalQueriesResource", "AsyncExternalQueriesResource"]


class ExternalQueriesResource(SyncAPIResource):
    """Query materialized external tables"""

    @cached_property
    def with_raw_response(self) -> ExternalQueriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return ExternalQueriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalQueriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return ExternalQueriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        sql: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalQueryCreateResponse:
        """
        Executes one read-only SELECT against the authenticated tenant's materialized
        external tables. Call /query/schema first to discover logical table and column
        names. Authorization is tenant-wide in Phase 1; principal-level row
        authorization is not applied. Required scope: `external_data:query`

        Args:
          sql: A single read-only SELECT using logical table names

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ExternalQueryCreateResponse,
            self._post(
                "/query",
                body=maybe_transform({"sql": sql}, external_query_create_params.ExternalQueryCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ExternalQueryCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalQueryStateOnlyResponse:
        """
        Returns retained state without dispatching build or SQL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._get(
            path_template("/query/{request_id}", request_id=request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalQueryStateOnlyResponse,
        )

    def cancel(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalQueryStateOnlyResponse:
        """
        Stops an active canary query and retains only its terminal state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._delete(
            path_template("/query/{request_id}", request_id=request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalQueryStateOnlyResponse,
        )

    def retrieve_schema(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalTableSchemaResponse:
        """
        Lists active logical tables and their columns for the authenticated tenant.
        Storage paths, setting IDs, and credentials are never returned. Required scope:
        `external_data:query`
        """
        return self._get(
            "/query/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalTableSchemaResponse,
        )


class AsyncExternalQueriesResource(AsyncAPIResource):
    """Query materialized external tables"""

    @cached_property
    def with_raw_response(self) -> AsyncExternalQueriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalQueriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalQueriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncExternalQueriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        sql: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalQueryCreateResponse:
        """
        Executes one read-only SELECT against the authenticated tenant's materialized
        external tables. Call /query/schema first to discover logical table and column
        names. Authorization is tenant-wide in Phase 1; principal-level row
        authorization is not applied. Required scope: `external_data:query`

        Args:
          sql: A single read-only SELECT using logical table names

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ExternalQueryCreateResponse,
            await self._post(
                "/query",
                body=await async_maybe_transform({"sql": sql}, external_query_create_params.ExternalQueryCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ExternalQueryCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalQueryStateOnlyResponse:
        """
        Returns retained state without dispatching build or SQL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._get(
            path_template("/query/{request_id}", request_id=request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalQueryStateOnlyResponse,
        )

    async def cancel(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalQueryStateOnlyResponse:
        """
        Stops an active canary query and retains only its terminal state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._delete(
            path_template("/query/{request_id}", request_id=request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalQueryStateOnlyResponse,
        )

    async def retrieve_schema(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalTableSchemaResponse:
        """
        Lists active logical tables and their columns for the authenticated tenant.
        Storage paths, setting IDs, and credentials are never returned. Required scope:
        `external_data:query`
        """
        return await self._get(
            "/query/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalTableSchemaResponse,
        )


class ExternalQueriesResourceWithRawResponse:
    def __init__(self, external_queries: ExternalQueriesResource) -> None:
        self._external_queries = external_queries

        self.create = to_raw_response_wrapper(
            external_queries.create,
        )
        self.retrieve = to_raw_response_wrapper(
            external_queries.retrieve,
        )
        self.cancel = to_raw_response_wrapper(
            external_queries.cancel,
        )
        self.retrieve_schema = to_raw_response_wrapper(
            external_queries.retrieve_schema,
        )


class AsyncExternalQueriesResourceWithRawResponse:
    def __init__(self, external_queries: AsyncExternalQueriesResource) -> None:
        self._external_queries = external_queries

        self.create = async_to_raw_response_wrapper(
            external_queries.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            external_queries.retrieve,
        )
        self.cancel = async_to_raw_response_wrapper(
            external_queries.cancel,
        )
        self.retrieve_schema = async_to_raw_response_wrapper(
            external_queries.retrieve_schema,
        )


class ExternalQueriesResourceWithStreamingResponse:
    def __init__(self, external_queries: ExternalQueriesResource) -> None:
        self._external_queries = external_queries

        self.create = to_streamed_response_wrapper(
            external_queries.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            external_queries.retrieve,
        )
        self.cancel = to_streamed_response_wrapper(
            external_queries.cancel,
        )
        self.retrieve_schema = to_streamed_response_wrapper(
            external_queries.retrieve_schema,
        )


class AsyncExternalQueriesResourceWithStreamingResponse:
    def __init__(self, external_queries: AsyncExternalQueriesResource) -> None:
        self._external_queries = external_queries

        self.create = async_to_streamed_response_wrapper(
            external_queries.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            external_queries.retrieve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            external_queries.cancel,
        )
        self.retrieve_schema = async_to_streamed_response_wrapper(
            external_queries.retrieve_schema,
        )
