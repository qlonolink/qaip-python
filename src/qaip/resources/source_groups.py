# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import (
    source_group_list_params,
    source_group_update_metadata_params,
    source_group_batch_set_metadata_params,
)
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
from ..types.source_group import SourceGroup
from ..types.shared.metadata import Metadata as SharedMetadata
from ..types.shared.source_type import SourceType
from ..types.shared_params.metadata import Metadata as SharedParamsMetadata
from ..types.source_group_list_response import SourceGroupListResponse
from ..types.shared.batch_set_metadata_response import BatchSetMetadataResponse
from ..types.source_group_list_sources_response import SourceGroupListSourcesResponse
from ..types.source_group_delete_metadata_response import SourceGroupDeleteMetadataResponse

__all__ = ["SourceGroupsResource", "AsyncSourceGroupsResource"]


class SourceGroupsResource(SyncAPIResource):
    """Source group (job) management and metadata"""

    @cached_property
    def with_raw_response(self) -> SourceGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return SourceGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourceGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return SourceGroupsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        source_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGroup:
        """<p> Gets detailed information about a specific source group.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_group_id:
            raise ValueError(f"Expected a non-empty value for `source_group_id` but received {source_group_id!r}")
        return self._get(
            path_template("/source-groups/{source_group_id}", source_group_id=source_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceGroup,
        )

    def list(
        self,
        *,
        after_id: str | Omit = omit,
        limit: int | Omit = omit,
        source_type: SourceType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGroupListResponse:
        """
        <p> Lists source groups (jobs) across all source types: crawl, local_file, google_drive, github, notion. </p> <p> Required roles: All, App </p>

        Args:
          after_id: Fetch records after this ID

          limit: Maximum number of results to return

          source_type: Filter by source type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/source-groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_id": after_id,
                        "limit": limit,
                        "source_type": source_type,
                    },
                    source_group_list_params.SourceGroupListParams,
                ),
            ),
            cast_to=SourceGroupListResponse,
        )

    def batch_set_metadata(
        self,
        *,
        items: Iterable[source_group_batch_set_metadata_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchSetMetadataResponse:
        """<p> Updates metadata for multiple source groups in a single request.

        Merges with existing metadata by key. Send val: null to delete a key. Maximum 50 items per request. </p> <p> Required roles: All </p>

        Args:
          items: List of source group metadata items (max 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/source-groups/metadata/batch",
            body=maybe_transform(
                {"items": items}, source_group_batch_set_metadata_params.SourceGroupBatchSetMetadataParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchSetMetadataResponse,
        )

    def delete_metadata(
        self,
        source_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGroupDeleteMetadataResponse:
        """<p> Deletes metadata for a specific source group.

        </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_group_id:
            raise ValueError(f"Expected a non-empty value for `source_group_id` but received {source_group_id!r}")
        return self._delete(
            path_template("/source-groups/{source_group_id}/metadata", source_group_id=source_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceGroupDeleteMetadataResponse,
        )

    def list_sources(
        self,
        source_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGroupListSourcesResponse:
        """<p> Lists sources (files) within a specific source group.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_group_id:
            raise ValueError(f"Expected a non-empty value for `source_group_id` but received {source_group_id!r}")
        return self._get(
            path_template("/source-groups/{source_group_id}/sources", source_group_id=source_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceGroupListSourcesResponse,
        )

    def retrieve_metadata(
        self,
        source_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedMetadata:
        """<p> Gets metadata for a specific source group.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_group_id:
            raise ValueError(f"Expected a non-empty value for `source_group_id` but received {source_group_id!r}")
        return self._get(
            path_template("/source-groups/{source_group_id}/metadata", source_group_id=source_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedMetadata,
        )

    def update_metadata(
        self,
        source_group_id: str,
        *,
        metadata: SharedParamsMetadata,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedMetadata:
        """<p> Updates metadata for a specific source group.

        Merges with existing metadata by key. Send val: null to delete a key. </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_group_id:
            raise ValueError(f"Expected a non-empty value for `source_group_id` but received {source_group_id!r}")
        return self._put(
            path_template("/source-groups/{source_group_id}/metadata", source_group_id=source_group_id),
            body=maybe_transform(
                {"metadata": metadata}, source_group_update_metadata_params.SourceGroupUpdateMetadataParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedMetadata,
        )


class AsyncSourceGroupsResource(AsyncAPIResource):
    """Source group (job) management and metadata"""

    @cached_property
    def with_raw_response(self) -> AsyncSourceGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSourceGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourceGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncSourceGroupsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        source_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGroup:
        """<p> Gets detailed information about a specific source group.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_group_id:
            raise ValueError(f"Expected a non-empty value for `source_group_id` but received {source_group_id!r}")
        return await self._get(
            path_template("/source-groups/{source_group_id}", source_group_id=source_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceGroup,
        )

    async def list(
        self,
        *,
        after_id: str | Omit = omit,
        limit: int | Omit = omit,
        source_type: SourceType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGroupListResponse:
        """
        <p> Lists source groups (jobs) across all source types: crawl, local_file, google_drive, github, notion. </p> <p> Required roles: All, App </p>

        Args:
          after_id: Fetch records after this ID

          limit: Maximum number of results to return

          source_type: Filter by source type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/source-groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after_id": after_id,
                        "limit": limit,
                        "source_type": source_type,
                    },
                    source_group_list_params.SourceGroupListParams,
                ),
            ),
            cast_to=SourceGroupListResponse,
        )

    async def batch_set_metadata(
        self,
        *,
        items: Iterable[source_group_batch_set_metadata_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchSetMetadataResponse:
        """<p> Updates metadata for multiple source groups in a single request.

        Merges with existing metadata by key. Send val: null to delete a key. Maximum 50 items per request. </p> <p> Required roles: All </p>

        Args:
          items: List of source group metadata items (max 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/source-groups/metadata/batch",
            body=await async_maybe_transform(
                {"items": items}, source_group_batch_set_metadata_params.SourceGroupBatchSetMetadataParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchSetMetadataResponse,
        )

    async def delete_metadata(
        self,
        source_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGroupDeleteMetadataResponse:
        """<p> Deletes metadata for a specific source group.

        </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_group_id:
            raise ValueError(f"Expected a non-empty value for `source_group_id` but received {source_group_id!r}")
        return await self._delete(
            path_template("/source-groups/{source_group_id}/metadata", source_group_id=source_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceGroupDeleteMetadataResponse,
        )

    async def list_sources(
        self,
        source_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGroupListSourcesResponse:
        """<p> Lists sources (files) within a specific source group.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_group_id:
            raise ValueError(f"Expected a non-empty value for `source_group_id` but received {source_group_id!r}")
        return await self._get(
            path_template("/source-groups/{source_group_id}/sources", source_group_id=source_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceGroupListSourcesResponse,
        )

    async def retrieve_metadata(
        self,
        source_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedMetadata:
        """<p> Gets metadata for a specific source group.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_group_id:
            raise ValueError(f"Expected a non-empty value for `source_group_id` but received {source_group_id!r}")
        return await self._get(
            path_template("/source-groups/{source_group_id}/metadata", source_group_id=source_group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedMetadata,
        )

    async def update_metadata(
        self,
        source_group_id: str,
        *,
        metadata: SharedParamsMetadata,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedMetadata:
        """<p> Updates metadata for a specific source group.

        Merges with existing metadata by key. Send val: null to delete a key. </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not source_group_id:
            raise ValueError(f"Expected a non-empty value for `source_group_id` but received {source_group_id!r}")
        return await self._put(
            path_template("/source-groups/{source_group_id}/metadata", source_group_id=source_group_id),
            body=await async_maybe_transform(
                {"metadata": metadata}, source_group_update_metadata_params.SourceGroupUpdateMetadataParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedMetadata,
        )


class SourceGroupsResourceWithRawResponse:
    def __init__(self, source_groups: SourceGroupsResource) -> None:
        self._source_groups = source_groups

        self.retrieve = to_raw_response_wrapper(
            source_groups.retrieve,
        )
        self.list = to_raw_response_wrapper(
            source_groups.list,
        )
        self.batch_set_metadata = to_raw_response_wrapper(
            source_groups.batch_set_metadata,
        )
        self.delete_metadata = to_raw_response_wrapper(
            source_groups.delete_metadata,
        )
        self.list_sources = to_raw_response_wrapper(
            source_groups.list_sources,
        )
        self.retrieve_metadata = to_raw_response_wrapper(
            source_groups.retrieve_metadata,
        )
        self.update_metadata = to_raw_response_wrapper(
            source_groups.update_metadata,
        )


class AsyncSourceGroupsResourceWithRawResponse:
    def __init__(self, source_groups: AsyncSourceGroupsResource) -> None:
        self._source_groups = source_groups

        self.retrieve = async_to_raw_response_wrapper(
            source_groups.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            source_groups.list,
        )
        self.batch_set_metadata = async_to_raw_response_wrapper(
            source_groups.batch_set_metadata,
        )
        self.delete_metadata = async_to_raw_response_wrapper(
            source_groups.delete_metadata,
        )
        self.list_sources = async_to_raw_response_wrapper(
            source_groups.list_sources,
        )
        self.retrieve_metadata = async_to_raw_response_wrapper(
            source_groups.retrieve_metadata,
        )
        self.update_metadata = async_to_raw_response_wrapper(
            source_groups.update_metadata,
        )


class SourceGroupsResourceWithStreamingResponse:
    def __init__(self, source_groups: SourceGroupsResource) -> None:
        self._source_groups = source_groups

        self.retrieve = to_streamed_response_wrapper(
            source_groups.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            source_groups.list,
        )
        self.batch_set_metadata = to_streamed_response_wrapper(
            source_groups.batch_set_metadata,
        )
        self.delete_metadata = to_streamed_response_wrapper(
            source_groups.delete_metadata,
        )
        self.list_sources = to_streamed_response_wrapper(
            source_groups.list_sources,
        )
        self.retrieve_metadata = to_streamed_response_wrapper(
            source_groups.retrieve_metadata,
        )
        self.update_metadata = to_streamed_response_wrapper(
            source_groups.update_metadata,
        )


class AsyncSourceGroupsResourceWithStreamingResponse:
    def __init__(self, source_groups: AsyncSourceGroupsResource) -> None:
        self._source_groups = source_groups

        self.retrieve = async_to_streamed_response_wrapper(
            source_groups.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            source_groups.list,
        )
        self.batch_set_metadata = async_to_streamed_response_wrapper(
            source_groups.batch_set_metadata,
        )
        self.delete_metadata = async_to_streamed_response_wrapper(
            source_groups.delete_metadata,
        )
        self.list_sources = async_to_streamed_response_wrapper(
            source_groups.list_sources,
        )
        self.retrieve_metadata = async_to_streamed_response_wrapper(
            source_groups.retrieve_metadata,
        )
        self.update_metadata = async_to_streamed_response_wrapper(
            source_groups.update_metadata,
        )
