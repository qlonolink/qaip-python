# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import local_file_group_list_params, local_file_group_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, path_template, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.local_file_group import LocalFileGroup
from ..types.local_file_group_list_response import LocalFileGroupListResponse
from ..types.local_file_group_create_response import LocalFileGroupCreateResponse
from ..types.local_file_group_delete_response import LocalFileGroupDeleteResponse

__all__ = ["LocalFileGroupsResource", "AsyncLocalFileGroupsResource"]


class LocalFileGroupsResource(SyncAPIResource):
    """Local file group management"""

    @cached_property
    def with_raw_response(self) -> LocalFileGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return LocalFileGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocalFileGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return LocalFileGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        files: SequenceNotStr[FileTypes],
        last_modified: SequenceNotStr[str],
        name: str,
        chunk_metadata_keys: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocalFileGroupCreateResponse:
        """
        <p> Creates a new local file group by uploading files directly via multipart form data. </p> <p> The total request body size must not exceed 500 MB. </p> <p> Required roles: All </p>

        Args:
          files: Files to upload

          last_modified: Last modified timestamps in Unix epoch milliseconds (integer) for each file
              (same order and count as files). For example, 1709971200000 represents
              2024-03-09T12:00:00Z.

          name: Name of the local file group

          chunk_metadata_keys: JSON array of chunk metadata key configurations. Each element is an object with
              "key" (string) and "type" (one of "string", "integer", "float", "date",
              "datetime"). Example:
              [{"key":"author","type":"string"},{"key":"page_number","type":"integer"}]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "files": files,
                "last_modified": last_modified,
                "name": name,
                "chunk_metadata_keys": chunk_metadata_keys,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/local-file-groups",
            body=maybe_transform(body, local_file_group_create_params.LocalFileGroupCreateParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocalFileGroupCreateResponse,
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
    ) -> LocalFileGroup:
        """<p> Returns a single local file group by ID.

        </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/local-file-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocalFileGroup,
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
    ) -> LocalFileGroupListResponse:
        """<p> Lists local file groups with cursor-based pagination.

        </p> <p> Required roles: All </p>

        Args:
          after_id: Fetch records after this ID

          limit: Maximum number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/local-file-groups",
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
                    local_file_group_list_params.LocalFileGroupListParams,
                ),
            ),
            cast_to=LocalFileGroupListResponse,
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
    ) -> LocalFileGroupDeleteResponse:
        """<p> Initiates an asynchronous deletion job for the specified local file group.

        The response indicates that the deletion job has been accepted, not that the deletion is complete. </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/local-file-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocalFileGroupDeleteResponse,
        )


class AsyncLocalFileGroupsResource(AsyncAPIResource):
    """Local file group management"""

    @cached_property
    def with_raw_response(self) -> AsyncLocalFileGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLocalFileGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocalFileGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncLocalFileGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        files: SequenceNotStr[FileTypes],
        last_modified: SequenceNotStr[str],
        name: str,
        chunk_metadata_keys: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocalFileGroupCreateResponse:
        """
        <p> Creates a new local file group by uploading files directly via multipart form data. </p> <p> The total request body size must not exceed 500 MB. </p> <p> Required roles: All </p>

        Args:
          files: Files to upload

          last_modified: Last modified timestamps in Unix epoch milliseconds (integer) for each file
              (same order and count as files). For example, 1709971200000 represents
              2024-03-09T12:00:00Z.

          name: Name of the local file group

          chunk_metadata_keys: JSON array of chunk metadata key configurations. Each element is an object with
              "key" (string) and "type" (one of "string", "integer", "float", "date",
              "datetime"). Example:
              [{"key":"author","type":"string"},{"key":"page_number","type":"integer"}]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "files": files,
                "last_modified": last_modified,
                "name": name,
                "chunk_metadata_keys": chunk_metadata_keys,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/local-file-groups",
            body=await async_maybe_transform(body, local_file_group_create_params.LocalFileGroupCreateParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocalFileGroupCreateResponse,
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
    ) -> LocalFileGroup:
        """<p> Returns a single local file group by ID.

        </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/local-file-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocalFileGroup,
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
    ) -> LocalFileGroupListResponse:
        """<p> Lists local file groups with cursor-based pagination.

        </p> <p> Required roles: All </p>

        Args:
          after_id: Fetch records after this ID

          limit: Maximum number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/local-file-groups",
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
                    local_file_group_list_params.LocalFileGroupListParams,
                ),
            ),
            cast_to=LocalFileGroupListResponse,
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
    ) -> LocalFileGroupDeleteResponse:
        """<p> Initiates an asynchronous deletion job for the specified local file group.

        The response indicates that the deletion job has been accepted, not that the deletion is complete. </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/local-file-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocalFileGroupDeleteResponse,
        )


class LocalFileGroupsResourceWithRawResponse:
    def __init__(self, local_file_groups: LocalFileGroupsResource) -> None:
        self._local_file_groups = local_file_groups

        self.create = to_raw_response_wrapper(
            local_file_groups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            local_file_groups.retrieve,
        )
        self.list = to_raw_response_wrapper(
            local_file_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            local_file_groups.delete,
        )


class AsyncLocalFileGroupsResourceWithRawResponse:
    def __init__(self, local_file_groups: AsyncLocalFileGroupsResource) -> None:
        self._local_file_groups = local_file_groups

        self.create = async_to_raw_response_wrapper(
            local_file_groups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            local_file_groups.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            local_file_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            local_file_groups.delete,
        )


class LocalFileGroupsResourceWithStreamingResponse:
    def __init__(self, local_file_groups: LocalFileGroupsResource) -> None:
        self._local_file_groups = local_file_groups

        self.create = to_streamed_response_wrapper(
            local_file_groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            local_file_groups.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            local_file_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            local_file_groups.delete,
        )


class AsyncLocalFileGroupsResourceWithStreamingResponse:
    def __init__(self, local_file_groups: AsyncLocalFileGroupsResource) -> None:
        self._local_file_groups = local_file_groups

        self.create = async_to_streamed_response_wrapper(
            local_file_groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            local_file_groups.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            local_file_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            local_file_groups.delete,
        )
