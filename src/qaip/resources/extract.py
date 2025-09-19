# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import extract_perform_params
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
from ..types.extract_perform_response import ExtractPerformResponse

__all__ = ["ExtractResource", "AsyncExtractResource"]


class ExtractResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/qaip-python#accessing-raw-response-data-eg-headers
        """
        return ExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/qaip-python#with_streaming_response
        """
        return ExtractResourceWithStreamingResponse(self)

    def perform(
        self,
        *,
        schema: object,
        date_from: int | Omit = omit,
        date_to: int | Omit = omit,
        domains: SequenceNotStr[str] | Omit = omit,
        file_types: List[FileType] | Omit = omit,
        limit: int | Omit = omit,
        llm_model: str | Omit = omit,
        offset: int | Omit = omit,
        prompt: str | Omit = omit,
        source_types: List[SourceType] | Omit = omit,
        tag_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractPerformResponse:
        """
        Performs data extraction using LLM based on the specified data source, filter
        conditions, and JSON schema. Retrieves chunked data from LanceDB and uses the
        schema to extract and return the result as JSON via LLM.

        Args:
          schema: JSON Schema for the data to be extracted.

          date_from: Start date for content search (Unix timestamp in seconds)

          date_to: End date for content search (Unix timestamp in seconds)

          llm_model: LLM model to use (e.g., gpt-4.1, defaults to gpt-4.1 if not specified).

          prompt: Additional prompt for the LLM (optional, if not specified, a default prompt in
              Japanese will be used).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/extract",
            body=maybe_transform(
                {
                    "schema": schema,
                    "date_from": date_from,
                    "date_to": date_to,
                    "domains": domains,
                    "file_types": file_types,
                    "limit": limit,
                    "llm_model": llm_model,
                    "offset": offset,
                    "prompt": prompt,
                    "source_types": source_types,
                    "tag_ids": tag_ids,
                },
                extract_perform_params.ExtractPerformParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractPerformResponse,
        )


class AsyncExtractResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/qaip-python#with_streaming_response
        """
        return AsyncExtractResourceWithStreamingResponse(self)

    async def perform(
        self,
        *,
        schema: object,
        date_from: int | Omit = omit,
        date_to: int | Omit = omit,
        domains: SequenceNotStr[str] | Omit = omit,
        file_types: List[FileType] | Omit = omit,
        limit: int | Omit = omit,
        llm_model: str | Omit = omit,
        offset: int | Omit = omit,
        prompt: str | Omit = omit,
        source_types: List[SourceType] | Omit = omit,
        tag_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractPerformResponse:
        """
        Performs data extraction using LLM based on the specified data source, filter
        conditions, and JSON schema. Retrieves chunked data from LanceDB and uses the
        schema to extract and return the result as JSON via LLM.

        Args:
          schema: JSON Schema for the data to be extracted.

          date_from: Start date for content search (Unix timestamp in seconds)

          date_to: End date for content search (Unix timestamp in seconds)

          llm_model: LLM model to use (e.g., gpt-4.1, defaults to gpt-4.1 if not specified).

          prompt: Additional prompt for the LLM (optional, if not specified, a default prompt in
              Japanese will be used).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/extract",
            body=await async_maybe_transform(
                {
                    "schema": schema,
                    "date_from": date_from,
                    "date_to": date_to,
                    "domains": domains,
                    "file_types": file_types,
                    "limit": limit,
                    "llm_model": llm_model,
                    "offset": offset,
                    "prompt": prompt,
                    "source_types": source_types,
                    "tag_ids": tag_ids,
                },
                extract_perform_params.ExtractPerformParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractPerformResponse,
        )


class ExtractResourceWithRawResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.perform = to_raw_response_wrapper(
            extract.perform,
        )


class AsyncExtractResourceWithRawResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.perform = async_to_raw_response_wrapper(
            extract.perform,
        )


class ExtractResourceWithStreamingResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.perform = to_streamed_response_wrapper(
            extract.perform,
        )


class AsyncExtractResourceWithStreamingResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.perform = async_to_streamed_response_wrapper(
            extract.perform,
        )
