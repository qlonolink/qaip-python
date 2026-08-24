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
    @cached_property
    def with_raw_response(self) -> ExternalQueriesResourceWithRawResponse:
        return ExternalQueriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalQueriesResourceWithStreamingResponse:
        return ExternalQueriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        sql: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalQueryCreateResponse:
        options = make_request_options(
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        # 公開 API は呼び出しごとに request_id を採番するため、応答喪失時の
        # POST 再送で別の query を起動しないよう、この操作だけ自動再試行を切る。
        options["max_retries"] = 0
        return cast(
            ExternalQueryCreateResponse,
            self._post(
                "/query",
                body=maybe_transform({"sql": sql}, external_query_create_params.ExternalQueryCreateParams),
                options=options,
                cast_to=cast(Any, ExternalQueryCreateResponse),
            ),
        )

    def retrieve_schema(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalTableSchemaResponse:
        return self._get(
            "/query/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalTableSchemaResponse,
        )

    def retrieve(
        self,
        request_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalQueryStateOnlyResponse:
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalQueryStateOnlyResponse:
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._delete(
            path_template("/query/{request_id}", request_id=request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalQueryStateOnlyResponse,
        )


class AsyncExternalQueriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExternalQueriesResourceWithRawResponse:
        return AsyncExternalQueriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalQueriesResourceWithStreamingResponse:
        return AsyncExternalQueriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        sql: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalQueryCreateResponse:
        options = make_request_options(
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        # 同期側と同じ理由で、非冪等な query 作成は自動再試行しない。
        options["max_retries"] = 0
        return cast(
            ExternalQueryCreateResponse,
            await self._post(
                "/query",
                body=await async_maybe_transform({"sql": sql}, external_query_create_params.ExternalQueryCreateParams),
                options=options,
                cast_to=cast(Any, ExternalQueryCreateResponse),
            ),
        )

    async def retrieve_schema(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalTableSchemaResponse:
        return await self._get(
            "/query/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalTableSchemaResponse,
        )

    async def retrieve(
        self,
        request_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalQueryStateOnlyResponse:
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalQueryStateOnlyResponse:
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._delete(
            path_template("/query/{request_id}", request_id=request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalQueryStateOnlyResponse,
        )


class ExternalQueriesResourceWithRawResponse:
    def __init__(self, external_queries: ExternalQueriesResource) -> None:
        self.create = to_raw_response_wrapper(external_queries.create)
        self.retrieve_schema = to_raw_response_wrapper(external_queries.retrieve_schema)
        self.retrieve = to_raw_response_wrapper(external_queries.retrieve)
        self.cancel = to_raw_response_wrapper(external_queries.cancel)


class AsyncExternalQueriesResourceWithRawResponse:
    def __init__(self, external_queries: AsyncExternalQueriesResource) -> None:
        self.create = async_to_raw_response_wrapper(external_queries.create)
        self.retrieve_schema = async_to_raw_response_wrapper(external_queries.retrieve_schema)
        self.retrieve = async_to_raw_response_wrapper(external_queries.retrieve)
        self.cancel = async_to_raw_response_wrapper(external_queries.cancel)


class ExternalQueriesResourceWithStreamingResponse:
    def __init__(self, external_queries: ExternalQueriesResource) -> None:
        self.create = to_streamed_response_wrapper(external_queries.create)
        self.retrieve_schema = to_streamed_response_wrapper(external_queries.retrieve_schema)
        self.retrieve = to_streamed_response_wrapper(external_queries.retrieve)
        self.cancel = to_streamed_response_wrapper(external_queries.cancel)


class AsyncExternalQueriesResourceWithStreamingResponse:
    def __init__(self, external_queries: AsyncExternalQueriesResource) -> None:
        self.create = async_to_streamed_response_wrapper(external_queries.create)
        self.retrieve_schema = async_to_streamed_response_wrapper(external_queries.retrieve_schema)
        self.retrieve = async_to_streamed_response_wrapper(external_queries.retrieve)
        self.cancel = async_to_streamed_response_wrapper(external_queries.cancel)
