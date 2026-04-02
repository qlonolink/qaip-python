# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import notion_list_params, notion_create_params, notion_update_setting_params
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
from ..types.notion import Notion
from ..types.notion_setting import NotionSetting
from ..types.notion_list_response import NotionListResponse
from ..types.shared_params.metadata import Metadata

__all__ = ["NotionsResource", "AsyncNotionsResource"]


class NotionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return NotionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return NotionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        page_id: str,
        metadata: Metadata | Omit = omit,
        notion_token: str | Omit = omit,
        rrule: str | Omit = omit,
        secret_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Notion:
        """<p> Creates a new Notion data source and starts ingestion.

        </p> <p> Required roles: All </p>

        Args:
          name: Name of the Notion data source

          page_id: Notion page ID

          metadata: (reserved for future use) Additional metadata for the Notion data source

          notion_token: One-time Notion integration token (mutually exclusive with secret_id)

          rrule: Recurrence rule (RFC 5545 RRULE). Requires secret_id (not one-time token).

          secret_id: ID of a stored secret to use (mutually exclusive with notion_token)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/notions",
            body=maybe_transform(
                {
                    "name": name,
                    "page_id": page_id,
                    "metadata": metadata,
                    "notion_token": notion_token,
                    "rrule": rrule,
                    "secret_id": secret_id,
                },
                notion_create_params.NotionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Notion,
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
    ) -> Notion:
        """<p> Gets detailed information about a specific Notion data source.

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
            path_template("/notions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Notion,
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
    ) -> NotionListResponse:
        """<p> Lists Notion data sources with cursor-based pagination.

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
            "/notions",
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
                    notion_list_params.NotionListParams,
                ),
            ),
            cast_to=NotionListResponse,
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
    ) -> Notion:
        """<p> Initiates an asynchronous deletion job for the specified Notion data source.

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
            path_template("/notions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Notion,
        )

    def retrieve_setting(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotionSetting:
        """<p> Gets the setting (schedule, page ID, etc.) for Notion data sources.

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
            path_template("/notion-settings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotionSetting,
        )

    def update_setting(
        self,
        id: str,
        *,
        name: str,
        rrule: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotionSetting:
        """<p> Updates the setting (name, schedule) for Notion data sources.

        </p> <p> Required roles: All </p>

        Args:
          name: Name of the Notion data source

          rrule: Recurrence rule (RFC 5545 RRULE). Empty string or omission removes the existing
              schedule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/notion-settings/{id}", id=id),
            body=maybe_transform(
                {
                    "name": name,
                    "rrule": rrule,
                },
                notion_update_setting_params.NotionUpdateSettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotionSetting,
        )


class AsyncNotionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncNotionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        page_id: str,
        metadata: Metadata | Omit = omit,
        notion_token: str | Omit = omit,
        rrule: str | Omit = omit,
        secret_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Notion:
        """<p> Creates a new Notion data source and starts ingestion.

        </p> <p> Required roles: All </p>

        Args:
          name: Name of the Notion data source

          page_id: Notion page ID

          metadata: (reserved for future use) Additional metadata for the Notion data source

          notion_token: One-time Notion integration token (mutually exclusive with secret_id)

          rrule: Recurrence rule (RFC 5545 RRULE). Requires secret_id (not one-time token).

          secret_id: ID of a stored secret to use (mutually exclusive with notion_token)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/notions",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "page_id": page_id,
                    "metadata": metadata,
                    "notion_token": notion_token,
                    "rrule": rrule,
                    "secret_id": secret_id,
                },
                notion_create_params.NotionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Notion,
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
    ) -> Notion:
        """<p> Gets detailed information about a specific Notion data source.

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
            path_template("/notions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Notion,
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
    ) -> NotionListResponse:
        """<p> Lists Notion data sources with cursor-based pagination.

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
            "/notions",
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
                    notion_list_params.NotionListParams,
                ),
            ),
            cast_to=NotionListResponse,
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
    ) -> Notion:
        """<p> Initiates an asynchronous deletion job for the specified Notion data source.

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
            path_template("/notions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Notion,
        )

    async def retrieve_setting(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotionSetting:
        """<p> Gets the setting (schedule, page ID, etc.) for Notion data sources.

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
            path_template("/notion-settings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotionSetting,
        )

    async def update_setting(
        self,
        id: str,
        *,
        name: str,
        rrule: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotionSetting:
        """<p> Updates the setting (name, schedule) for Notion data sources.

        </p> <p> Required roles: All </p>

        Args:
          name: Name of the Notion data source

          rrule: Recurrence rule (RFC 5545 RRULE). Empty string or omission removes the existing
              schedule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/notion-settings/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "rrule": rrule,
                },
                notion_update_setting_params.NotionUpdateSettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotionSetting,
        )


class NotionsResourceWithRawResponse:
    def __init__(self, notions: NotionsResource) -> None:
        self._notions = notions

        self.create = to_raw_response_wrapper(
            notions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            notions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            notions.list,
        )
        self.delete = to_raw_response_wrapper(
            notions.delete,
        )
        self.retrieve_setting = to_raw_response_wrapper(
            notions.retrieve_setting,
        )
        self.update_setting = to_raw_response_wrapper(
            notions.update_setting,
        )


class AsyncNotionsResourceWithRawResponse:
    def __init__(self, notions: AsyncNotionsResource) -> None:
        self._notions = notions

        self.create = async_to_raw_response_wrapper(
            notions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            notions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            notions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            notions.delete,
        )
        self.retrieve_setting = async_to_raw_response_wrapper(
            notions.retrieve_setting,
        )
        self.update_setting = async_to_raw_response_wrapper(
            notions.update_setting,
        )


class NotionsResourceWithStreamingResponse:
    def __init__(self, notions: NotionsResource) -> None:
        self._notions = notions

        self.create = to_streamed_response_wrapper(
            notions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            notions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            notions.list,
        )
        self.delete = to_streamed_response_wrapper(
            notions.delete,
        )
        self.retrieve_setting = to_streamed_response_wrapper(
            notions.retrieve_setting,
        )
        self.update_setting = to_streamed_response_wrapper(
            notions.update_setting,
        )


class AsyncNotionsResourceWithStreamingResponse:
    def __init__(self, notions: AsyncNotionsResource) -> None:
        self._notions = notions

        self.create = async_to_streamed_response_wrapper(
            notions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            notions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            notions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            notions.delete,
        )
        self.retrieve_setting = async_to_streamed_response_wrapper(
            notions.retrieve_setting,
        )
        self.update_setting = async_to_streamed_response_wrapper(
            notions.update_setting,
        )
