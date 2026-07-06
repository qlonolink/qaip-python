# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import source_list_params, source_update_metadata_params, source_batch_set_metadata_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.source import Source
from ..types.shared.metadata import Metadata as SharedMetadata
from ..types.source_list_response import SourceListResponse
from ..types.shared_params.metadata import Metadata as SharedParamsMetadata
from ..types.source_delete_metadata_response import SourceDeleteMetadataResponse
from ..types.shared.batch_set_metadata_response import BatchSetMetadataResponse

__all__ = ["SourcesResource", "AsyncSourcesResource"]


class SourcesResource(SyncAPIResource):
    """Sources management and metadata"""

    @cached_property
    def with_raw_response(self) -> SourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return SourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return SourcesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Source:
        """<p> Gets detailed information about a specific source.

        This endpoint currently supports local_file source IDs. Crawl source IDs returned by /search or GET /contents/{id} are separate IDs and are not accepted here; use GET /sources/{source_id}/raw to download the stored crawl file content. </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._get(
            path_template("/sources/{source_id}", source_id=source_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Source,
        )

    def list(
        self,
        *,
        after_id: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceListResponse:
        """<p> Lists sources that have metadata records.

        Currently only local_file sources are returned by this endpoint. Crawl source IDs appear in search results and can be used with GET /sources/{source_id}/raw instead. </p> <p> Required roles: All, App </p>

        Args:
          after_id: Fetch records after this ID

          limit: Maximum number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_id": after_id,
                        "limit": limit,
                    },
                    source_list_params.SourceListParams,
                ),
            ),
            cast_to=SourceListResponse,
        )

    def batch_set_metadata(
        self,
        *,
        items: Iterable[source_batch_set_metadata_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchSetMetadataResponse:
        """<p> Updates metadata for multiple sources in a single request.

        Merges with existing metadata by key. Send val: null to delete a key. Maximum 50 items per request. </p> <p> Required roles: All </p>

        Args:
          items: List of source metadata items (max 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sources/metadata/batch",
            body=maybe_transform({"items": items}, source_batch_set_metadata_params.SourceBatchSetMetadataParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchSetMetadataResponse,
        )

    def download_raw(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> bytes:
        """<p> Downloads the original file fetched by crawl.

        Only crawl source IDs returned as content.source_id from /search,
        GET /contents/{id}, or POST /completions citations are valid. Local file
        source IDs accepted by GET /sources/{source_id} return 404 here. </p>
        <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._get(
            path_template("/sources/{source_id}/raw", source_id=source_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=bytes,
        )

    def delete_metadata(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceDeleteMetadataResponse:
        """<p> Deletes metadata for a specific source.

        </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._delete(
            path_template("/sources/{source_id}/metadata", source_id=source_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceDeleteMetadataResponse,
        )

    def download_raw(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """<p> Downloads the file content stored from crawl.

        Only crawl source IDs returned as content.source_id from /search, GET /contents/{id}, or POST /completions citations are valid. Local file source IDs accepted by GET /sources/{source_id} return 404 here. </p> <p> The endpoint checks tenant ownership of the crawl source and returns the entire stored file. It does not apply per-chunk authorization policies; applications using enforce authorization should decide whether to expose raw files to each principal. </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            path_template("/sources/{source_id}/raw", source_id=source_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def retrieve_metadata(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedMetadata:
        """<p> Gets metadata for a specific local_file source.

        Crawl source IDs returned by search results are separate IDs and are not accepted here; use GET /sources/{source_id}/raw for stored crawl file content. </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._get(
            path_template("/sources/{source_id}/metadata", source_id=source_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedMetadata,
        )

    def update_metadata(
        self,
        source_id: str,
        *,
        metadata: SharedParamsMetadata,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedMetadata:
        """<p> Updates metadata for a specific source.

        Merges with existing metadata by key. Send val: null to delete a key. </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._put(
            path_template("/sources/{source_id}/metadata", source_id=source_id),
            body=maybe_transform({"metadata": metadata}, source_update_metadata_params.SourceUpdateMetadataParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedMetadata,
        )


class AsyncSourcesResource(AsyncAPIResource):
    """Sources management and metadata"""

    @cached_property
    def with_raw_response(self) -> AsyncSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncSourcesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Source:
        """<p> Gets detailed information about a specific source.

        This endpoint currently supports local_file source IDs. Crawl source IDs returned by /search or GET /contents/{id} are separate IDs and are not accepted here; use GET /sources/{source_id}/raw to download the stored crawl file content. </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._get(
            path_template("/sources/{source_id}", source_id=source_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Source,
        )

    async def list(
        self,
        *,
        after_id: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceListResponse:
        """<p> Lists sources that have metadata records.

        Currently only local_file sources are returned by this endpoint. Crawl source IDs appear in search results and can be used with GET /sources/{source_id}/raw instead. </p> <p> Required roles: All, App </p>

        Args:
          after_id: Fetch records after this ID

          limit: Maximum number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after_id": after_id,
                        "limit": limit,
                    },
                    source_list_params.SourceListParams,
                ),
            ),
            cast_to=SourceListResponse,
        )

    async def batch_set_metadata(
        self,
        *,
        items: Iterable[source_batch_set_metadata_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchSetMetadataResponse:
        """<p> Updates metadata for multiple sources in a single request.

        Merges with existing metadata by key. Send val: null to delete a key. Maximum 50 items per request. </p> <p> Required roles: All </p>

        Args:
          items: List of source metadata items (max 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sources/metadata/batch",
            body=await async_maybe_transform(
                {"items": items}, source_batch_set_metadata_params.SourceBatchSetMetadataParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchSetMetadataResponse,
        )

    async def download_raw(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> bytes:
        """<p> Downloads the original file fetched by crawl.

        Only crawl source IDs returned as content.source_id from /search,
        GET /contents/{id}, or POST /completions citations are valid. Local file
        source IDs accepted by GET /sources/{source_id} return 404 here. </p>
        <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._get(
            path_template("/sources/{source_id}/raw", source_id=source_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=bytes,
        )

    async def delete_metadata(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceDeleteMetadataResponse:
        """<p> Deletes metadata for a specific source.

        </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._delete(
            path_template("/sources/{source_id}/metadata", source_id=source_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceDeleteMetadataResponse,
        )

    async def download_raw(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """<p> Downloads the file content stored from crawl.

        Only crawl source IDs returned as content.source_id from /search, GET /contents/{id}, or POST /completions citations are valid. Local file source IDs accepted by GET /sources/{source_id} return 404 here. </p> <p> The endpoint checks tenant ownership of the crawl source and returns the entire stored file. It does not apply per-chunk authorization policies; applications using enforce authorization should decide whether to expose raw files to each principal. </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/sources/{source_id}/raw", source_id=source_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def retrieve_metadata(
        self,
        source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedMetadata:
        """<p> Gets metadata for a specific local_file source.

        Crawl source IDs returned by search results are separate IDs and are not accepted here; use GET /sources/{source_id}/raw for stored crawl file content. </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._get(
            path_template("/sources/{source_id}/metadata", source_id=source_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedMetadata,
        )

    async def update_metadata(
        self,
        source_id: str,
        *,
        metadata: SharedParamsMetadata,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedMetadata:
        """<p> Updates metadata for a specific source.

        Merges with existing metadata by key. Send val: null to delete a key. </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._put(
            path_template("/sources/{source_id}/metadata", source_id=source_id),
            body=await async_maybe_transform(
                {"metadata": metadata}, source_update_metadata_params.SourceUpdateMetadataParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedMetadata,
        )


class SourcesResourceWithRawResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.retrieve = to_raw_response_wrapper(
            sources.retrieve,
        )
        self.list = to_raw_response_wrapper(
            sources.list,
        )
        self.batch_set_metadata = to_raw_response_wrapper(
            sources.batch_set_metadata,
        )
        self.download_raw = to_custom_raw_response_wrapper(
            sources.download_raw,
            BinaryAPIResponse,
        )
        self.delete_metadata = to_raw_response_wrapper(
            sources.delete_metadata,
        )
        self.download_raw = to_custom_raw_response_wrapper(
            sources.download_raw,
            BinaryAPIResponse,
        )
        self.retrieve_metadata = to_raw_response_wrapper(
            sources.retrieve_metadata,
        )
        self.update_metadata = to_raw_response_wrapper(
            sources.update_metadata,
        )


class AsyncSourcesResourceWithRawResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.retrieve = async_to_raw_response_wrapper(
            sources.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            sources.list,
        )
        self.batch_set_metadata = async_to_raw_response_wrapper(
            sources.batch_set_metadata,
        )
        self.download_raw = async_to_custom_raw_response_wrapper(
            sources.download_raw,
            AsyncBinaryAPIResponse,
        )
        self.delete_metadata = async_to_raw_response_wrapper(
            sources.delete_metadata,
        )
        self.download_raw = async_to_custom_raw_response_wrapper(
            sources.download_raw,
            AsyncBinaryAPIResponse,
        )
        self.retrieve_metadata = async_to_raw_response_wrapper(
            sources.retrieve_metadata,
        )
        self.update_metadata = async_to_raw_response_wrapper(
            sources.update_metadata,
        )


class SourcesResourceWithStreamingResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.retrieve = to_streamed_response_wrapper(
            sources.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            sources.list,
        )
        self.batch_set_metadata = to_streamed_response_wrapper(
            sources.batch_set_metadata,
        )
        self.download_raw = to_custom_streamed_response_wrapper(
            sources.download_raw,
            StreamedBinaryAPIResponse,
        )
        self.delete_metadata = to_streamed_response_wrapper(
            sources.delete_metadata,
        )
        self.download_raw = to_custom_streamed_response_wrapper(
            sources.download_raw,
            StreamedBinaryAPIResponse,
        )
        self.retrieve_metadata = to_streamed_response_wrapper(
            sources.retrieve_metadata,
        )
        self.update_metadata = to_streamed_response_wrapper(
            sources.update_metadata,
        )


class AsyncSourcesResourceWithStreamingResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.retrieve = async_to_streamed_response_wrapper(
            sources.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            sources.list,
        )
        self.batch_set_metadata = async_to_streamed_response_wrapper(
            sources.batch_set_metadata,
        )
        self.download_raw = async_to_custom_streamed_response_wrapper(
            sources.download_raw,
            AsyncStreamedBinaryAPIResponse,
        )
        self.delete_metadata = async_to_streamed_response_wrapper(
            sources.delete_metadata,
        )
        self.download_raw = async_to_custom_streamed_response_wrapper(
            sources.download_raw,
            AsyncStreamedBinaryAPIResponse,
        )
        self.retrieve_metadata = async_to_streamed_response_wrapper(
            sources.retrieve_metadata,
        )
        self.update_metadata = async_to_streamed_response_wrapper(
            sources.update_metadata,
        )
