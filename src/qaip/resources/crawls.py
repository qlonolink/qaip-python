# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    crawl_list_params,
    crawl_create_params,
    crawl_update_setting_params,
    crawl_create_url_list_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.crawl import Crawl
from .._base_client import make_request_options
from ..types.crawl_setting import CrawlSetting
from ..types.crawl_list_response import CrawlListResponse
from ..types.shared_params.metadata import Metadata

__all__ = ["CrawlsResource", "AsyncCrawlsResource"]


class CrawlsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CrawlsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return CrawlsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CrawlsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return CrawlsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        max_depth: int,
        max_num_files: int,
        name: str,
        start_url: str,
        content_pattern: SequenceNotStr[str] | Omit = omit,
        file_extensions: SequenceNotStr[str] | Omit = omit,
        html_only: bool | Omit = omit,
        metadata: Metadata | Omit = omit,
        path_filters: SequenceNotStr[str] | Omit = omit,
        rrule: str | Omit = omit,
        use_browser: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Crawl:
        """<p> Creates a new web crawl data source and starts ingestion.

        </p> <p> Required roles: All </p>

        Args:
          max_depth: Maximum crawl depth

          max_num_files: Maximum number of files to crawl

          name: Name of the web crawl data source

          start_url: Start URL of the web crawl

          content_pattern: Content patterns for filtering. The total number of characters across all
              elements in the array must be 2000 or fewer.

          file_extensions: File extensions to include (e.g. ".pdf", ".docx"). For supported file
              extensions, please refer to
              https://developer.qaip.com/docs/datasources#%E5%AF%BE%E5%BF%9C%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%BD%A2%E5%BC%8F

          html_only: When true, only HTML files will be downloaded

          metadata: (reserved for future use) Additional metadata for the web crawl data source

          path_filters: Path filters for crawling. The total number of characters across all elements in
              the array must be 2000 or fewer.

          rrule: Recurrence rule (RFC 5545 RRULE)

          use_browser: Whether to use a headless browser for crawling

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crawls",
            body=maybe_transform(
                {
                    "max_depth": max_depth,
                    "max_num_files": max_num_files,
                    "name": name,
                    "start_url": start_url,
                    "content_pattern": content_pattern,
                    "file_extensions": file_extensions,
                    "html_only": html_only,
                    "metadata": metadata,
                    "path_filters": path_filters,
                    "rrule": rrule,
                    "use_browser": use_browser,
                },
                crawl_create_params.CrawlCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Crawl,
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
    ) -> Crawl:
        """<p> Gets detailed information about a specific web crawl data source.

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
            path_template("/crawls/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Crawl,
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
    ) -> CrawlListResponse:
        """<p> Lists web crawl data sources with cursor-based pagination.

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
            "/crawls",
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
                    crawl_list_params.CrawlListParams,
                ),
            ),
            cast_to=CrawlListResponse,
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
    ) -> Crawl:
        """
        <p> Initiates an asynchronous deletion job for the specified web crawl data source. The response indicates that the deletion job has been accepted, not that the deletion is complete. </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/crawls/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Crawl,
        )

    def create_url_list(
        self,
        *,
        name: str,
        target_urls: SequenceNotStr[str],
        max_num_files: int | Omit = omit,
        metadata: Metadata | Omit = omit,
        rrule: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Crawl:
        """<p> Creates a new web crawl data source by directly downloading a list of URLs.

        Unlike the standard crawl endpoint, this does not follow links or crawl pages — it downloads the specified URLs directly. </p> <p> Required roles: All </p>

        Args:
          name: Name of the web crawl data source

          target_urls: List of URLs to download directly. Each URL must use http or https scheme.

          max_num_files: Maximum number of files to download. Defaults to the number of target URLs if
              omitted.

          metadata: (reserved for future use) Additional metadata for the web crawl data source

          rrule: Recurrence rule (RFC 5545 RRULE)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crawl-url-lists",
            body=maybe_transform(
                {
                    "name": name,
                    "target_urls": target_urls,
                    "max_num_files": max_num_files,
                    "metadata": metadata,
                    "rrule": rrule,
                },
                crawl_create_url_list_params.CrawlCreateURLListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Crawl,
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
    ) -> CrawlSetting:
        """<p> Gets the setting (schedule, URL, etc.) for web crawl data sources.

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
            path_template("/crawl-settings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrawlSetting,
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
    ) -> CrawlSetting:
        """<p> Updates the setting (name, schedule) for web crawl data sources.

        </p> <p> Required roles: All </p>

        Args:
          name: Name of the web crawl data source

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
            path_template("/crawl-settings/{id}", id=id),
            body=maybe_transform(
                {
                    "name": name,
                    "rrule": rrule,
                },
                crawl_update_setting_params.CrawlUpdateSettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrawlSetting,
        )


class AsyncCrawlsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCrawlsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCrawlsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCrawlsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncCrawlsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        max_depth: int,
        max_num_files: int,
        name: str,
        start_url: str,
        content_pattern: SequenceNotStr[str] | Omit = omit,
        file_extensions: SequenceNotStr[str] | Omit = omit,
        html_only: bool | Omit = omit,
        metadata: Metadata | Omit = omit,
        path_filters: SequenceNotStr[str] | Omit = omit,
        rrule: str | Omit = omit,
        use_browser: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Crawl:
        """<p> Creates a new web crawl data source and starts ingestion.

        </p> <p> Required roles: All </p>

        Args:
          max_depth: Maximum crawl depth

          max_num_files: Maximum number of files to crawl

          name: Name of the web crawl data source

          start_url: Start URL of the web crawl

          content_pattern: Content patterns for filtering. The total number of characters across all
              elements in the array must be 2000 or fewer.

          file_extensions: File extensions to include (e.g. ".pdf", ".docx"). For supported file
              extensions, please refer to
              https://developer.qaip.com/docs/datasources#%E5%AF%BE%E5%BF%9C%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%BD%A2%E5%BC%8F

          html_only: When true, only HTML files will be downloaded

          metadata: (reserved for future use) Additional metadata for the web crawl data source

          path_filters: Path filters for crawling. The total number of characters across all elements in
              the array must be 2000 or fewer.

          rrule: Recurrence rule (RFC 5545 RRULE)

          use_browser: Whether to use a headless browser for crawling

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crawls",
            body=await async_maybe_transform(
                {
                    "max_depth": max_depth,
                    "max_num_files": max_num_files,
                    "name": name,
                    "start_url": start_url,
                    "content_pattern": content_pattern,
                    "file_extensions": file_extensions,
                    "html_only": html_only,
                    "metadata": metadata,
                    "path_filters": path_filters,
                    "rrule": rrule,
                    "use_browser": use_browser,
                },
                crawl_create_params.CrawlCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Crawl,
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
    ) -> Crawl:
        """<p> Gets detailed information about a specific web crawl data source.

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
            path_template("/crawls/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Crawl,
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
    ) -> CrawlListResponse:
        """<p> Lists web crawl data sources with cursor-based pagination.

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
            "/crawls",
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
                    crawl_list_params.CrawlListParams,
                ),
            ),
            cast_to=CrawlListResponse,
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
    ) -> Crawl:
        """
        <p> Initiates an asynchronous deletion job for the specified web crawl data source. The response indicates that the deletion job has been accepted, not that the deletion is complete. </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/crawls/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Crawl,
        )

    async def create_url_list(
        self,
        *,
        name: str,
        target_urls: SequenceNotStr[str],
        max_num_files: int | Omit = omit,
        metadata: Metadata | Omit = omit,
        rrule: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Crawl:
        """<p> Creates a new web crawl data source by directly downloading a list of URLs.

        Unlike the standard crawl endpoint, this does not follow links or crawl pages — it downloads the specified URLs directly. </p> <p> Required roles: All </p>

        Args:
          name: Name of the web crawl data source

          target_urls: List of URLs to download directly. Each URL must use http or https scheme.

          max_num_files: Maximum number of files to download. Defaults to the number of target URLs if
              omitted.

          metadata: (reserved for future use) Additional metadata for the web crawl data source

          rrule: Recurrence rule (RFC 5545 RRULE)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crawl-url-lists",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "target_urls": target_urls,
                    "max_num_files": max_num_files,
                    "metadata": metadata,
                    "rrule": rrule,
                },
                crawl_create_url_list_params.CrawlCreateURLListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Crawl,
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
    ) -> CrawlSetting:
        """<p> Gets the setting (schedule, URL, etc.) for web crawl data sources.

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
            path_template("/crawl-settings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrawlSetting,
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
    ) -> CrawlSetting:
        """<p> Updates the setting (name, schedule) for web crawl data sources.

        </p> <p> Required roles: All </p>

        Args:
          name: Name of the web crawl data source

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
            path_template("/crawl-settings/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "rrule": rrule,
                },
                crawl_update_setting_params.CrawlUpdateSettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrawlSetting,
        )


class CrawlsResourceWithRawResponse:
    def __init__(self, crawls: CrawlsResource) -> None:
        self._crawls = crawls

        self.create = to_raw_response_wrapper(
            crawls.create,
        )
        self.retrieve = to_raw_response_wrapper(
            crawls.retrieve,
        )
        self.list = to_raw_response_wrapper(
            crawls.list,
        )
        self.delete = to_raw_response_wrapper(
            crawls.delete,
        )
        self.create_url_list = to_raw_response_wrapper(
            crawls.create_url_list,
        )
        self.retrieve_setting = to_raw_response_wrapper(
            crawls.retrieve_setting,
        )
        self.update_setting = to_raw_response_wrapper(
            crawls.update_setting,
        )


class AsyncCrawlsResourceWithRawResponse:
    def __init__(self, crawls: AsyncCrawlsResource) -> None:
        self._crawls = crawls

        self.create = async_to_raw_response_wrapper(
            crawls.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            crawls.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            crawls.list,
        )
        self.delete = async_to_raw_response_wrapper(
            crawls.delete,
        )
        self.create_url_list = async_to_raw_response_wrapper(
            crawls.create_url_list,
        )
        self.retrieve_setting = async_to_raw_response_wrapper(
            crawls.retrieve_setting,
        )
        self.update_setting = async_to_raw_response_wrapper(
            crawls.update_setting,
        )


class CrawlsResourceWithStreamingResponse:
    def __init__(self, crawls: CrawlsResource) -> None:
        self._crawls = crawls

        self.create = to_streamed_response_wrapper(
            crawls.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            crawls.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            crawls.list,
        )
        self.delete = to_streamed_response_wrapper(
            crawls.delete,
        )
        self.create_url_list = to_streamed_response_wrapper(
            crawls.create_url_list,
        )
        self.retrieve_setting = to_streamed_response_wrapper(
            crawls.retrieve_setting,
        )
        self.update_setting = to_streamed_response_wrapper(
            crawls.update_setting,
        )


class AsyncCrawlsResourceWithStreamingResponse:
    def __init__(self, crawls: AsyncCrawlsResource) -> None:
        self._crawls = crawls

        self.create = async_to_streamed_response_wrapper(
            crawls.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            crawls.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            crawls.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            crawls.delete,
        )
        self.create_url_list = async_to_streamed_response_wrapper(
            crawls.create_url_list,
        )
        self.retrieve_setting = async_to_streamed_response_wrapper(
            crawls.retrieve_setting,
        )
        self.update_setting = async_to_streamed_response_wrapper(
            crawls.update_setting,
        )
