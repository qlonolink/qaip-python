# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import google_drive_list_params, google_drive_create_params, google_drive_update_setting_params
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
from ..types.google_drive import GoogleDrive
from ..types.google_drive_setting import GoogleDriveSetting
from ..types.shared_params.metadata import Metadata
from ..types.google_drive_list_response import GoogleDriveListResponse

__all__ = ["GoogleDrivesResource", "AsyncGoogleDrivesResource"]


class GoogleDrivesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GoogleDrivesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return GoogleDrivesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GoogleDrivesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return GoogleDrivesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        folder_url: str,
        name: str,
        metadata: Metadata | Omit = omit,
        rrule: str | Omit = omit,
        secret_id: str | Omit = omit,
        service_account_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoogleDrive:
        """<p> Creates a new Google Drive data source and starts ingestion.

        </p> <p> Required roles: All </p>

        Args:
          folder_url: Google Drive folder URL

          name: Name of the Google Drive data source

          metadata: (reserved for future use) Additional metadata for the Google Drive data source

          rrule: Recurrence rule (RFC 5545 RRULE). Requires secret_id (not one-time key).

          secret_id: ID of a stored secret to use (mutually exclusive with service_account_key)

          service_account_key: One-time service account key JSON (mutually exclusive with secret_id)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/google-drives",
            body=maybe_transform(
                {
                    "folder_url": folder_url,
                    "name": name,
                    "metadata": metadata,
                    "rrule": rrule,
                    "secret_id": secret_id,
                    "service_account_key": service_account_key,
                },
                google_drive_create_params.GoogleDriveCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoogleDrive,
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
    ) -> GoogleDrive:
        """<p> Gets detailed information about a specific Google Drive data source.

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
            path_template("/google-drives/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoogleDrive,
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
    ) -> GoogleDriveListResponse:
        """<p> Lists Google Drive data sources with cursor-based pagination.

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
            "/google-drives",
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
                    google_drive_list_params.GoogleDriveListParams,
                ),
            ),
            cast_to=GoogleDriveListResponse,
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
    ) -> GoogleDrive:
        """
        <p> Initiates an asynchronous deletion job for the specified Google Drive data source. The response indicates that the deletion job has been accepted, not that the deletion is complete. </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/google-drives/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoogleDrive,
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
    ) -> GoogleDriveSetting:
        """<p> Gets the setting (schedule, folder URL, etc.) for Google Drive data sources.

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
            path_template("/google-drive-settings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoogleDriveSetting,
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
    ) -> GoogleDriveSetting:
        """<p> Updates the setting (name, schedule) for Google Drive data sources.

        </p> <p> Required roles: All </p>

        Args:
          name: Name of the Google Drive data source

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
            path_template("/google-drive-settings/{id}", id=id),
            body=maybe_transform(
                {
                    "name": name,
                    "rrule": rrule,
                },
                google_drive_update_setting_params.GoogleDriveUpdateSettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoogleDriveSetting,
        )


class AsyncGoogleDrivesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGoogleDrivesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGoogleDrivesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGoogleDrivesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncGoogleDrivesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        folder_url: str,
        name: str,
        metadata: Metadata | Omit = omit,
        rrule: str | Omit = omit,
        secret_id: str | Omit = omit,
        service_account_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoogleDrive:
        """<p> Creates a new Google Drive data source and starts ingestion.

        </p> <p> Required roles: All </p>

        Args:
          folder_url: Google Drive folder URL

          name: Name of the Google Drive data source

          metadata: (reserved for future use) Additional metadata for the Google Drive data source

          rrule: Recurrence rule (RFC 5545 RRULE). Requires secret_id (not one-time key).

          secret_id: ID of a stored secret to use (mutually exclusive with service_account_key)

          service_account_key: One-time service account key JSON (mutually exclusive with secret_id)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/google-drives",
            body=await async_maybe_transform(
                {
                    "folder_url": folder_url,
                    "name": name,
                    "metadata": metadata,
                    "rrule": rrule,
                    "secret_id": secret_id,
                    "service_account_key": service_account_key,
                },
                google_drive_create_params.GoogleDriveCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoogleDrive,
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
    ) -> GoogleDrive:
        """<p> Gets detailed information about a specific Google Drive data source.

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
            path_template("/google-drives/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoogleDrive,
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
    ) -> GoogleDriveListResponse:
        """<p> Lists Google Drive data sources with cursor-based pagination.

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
            "/google-drives",
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
                    google_drive_list_params.GoogleDriveListParams,
                ),
            ),
            cast_to=GoogleDriveListResponse,
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
    ) -> GoogleDrive:
        """
        <p> Initiates an asynchronous deletion job for the specified Google Drive data source. The response indicates that the deletion job has been accepted, not that the deletion is complete. </p> <p> Required roles: All </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/google-drives/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoogleDrive,
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
    ) -> GoogleDriveSetting:
        """<p> Gets the setting (schedule, folder URL, etc.) for Google Drive data sources.

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
            path_template("/google-drive-settings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoogleDriveSetting,
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
    ) -> GoogleDriveSetting:
        """<p> Updates the setting (name, schedule) for Google Drive data sources.

        </p> <p> Required roles: All </p>

        Args:
          name: Name of the Google Drive data source

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
            path_template("/google-drive-settings/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "rrule": rrule,
                },
                google_drive_update_setting_params.GoogleDriveUpdateSettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoogleDriveSetting,
        )


class GoogleDrivesResourceWithRawResponse:
    def __init__(self, google_drives: GoogleDrivesResource) -> None:
        self._google_drives = google_drives

        self.create = to_raw_response_wrapper(
            google_drives.create,
        )
        self.retrieve = to_raw_response_wrapper(
            google_drives.retrieve,
        )
        self.list = to_raw_response_wrapper(
            google_drives.list,
        )
        self.delete = to_raw_response_wrapper(
            google_drives.delete,
        )
        self.retrieve_setting = to_raw_response_wrapper(
            google_drives.retrieve_setting,
        )
        self.update_setting = to_raw_response_wrapper(
            google_drives.update_setting,
        )


class AsyncGoogleDrivesResourceWithRawResponse:
    def __init__(self, google_drives: AsyncGoogleDrivesResource) -> None:
        self._google_drives = google_drives

        self.create = async_to_raw_response_wrapper(
            google_drives.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            google_drives.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            google_drives.list,
        )
        self.delete = async_to_raw_response_wrapper(
            google_drives.delete,
        )
        self.retrieve_setting = async_to_raw_response_wrapper(
            google_drives.retrieve_setting,
        )
        self.update_setting = async_to_raw_response_wrapper(
            google_drives.update_setting,
        )


class GoogleDrivesResourceWithStreamingResponse:
    def __init__(self, google_drives: GoogleDrivesResource) -> None:
        self._google_drives = google_drives

        self.create = to_streamed_response_wrapper(
            google_drives.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            google_drives.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            google_drives.list,
        )
        self.delete = to_streamed_response_wrapper(
            google_drives.delete,
        )
        self.retrieve_setting = to_streamed_response_wrapper(
            google_drives.retrieve_setting,
        )
        self.update_setting = to_streamed_response_wrapper(
            google_drives.update_setting,
        )


class AsyncGoogleDrivesResourceWithStreamingResponse:
    def __init__(self, google_drives: AsyncGoogleDrivesResource) -> None:
        self._google_drives = google_drives

        self.create = async_to_streamed_response_wrapper(
            google_drives.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            google_drives.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            google_drives.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            google_drives.delete,
        )
        self.retrieve_setting = async_to_streamed_response_wrapper(
            google_drives.retrieve_setting,
        )
        self.update_setting = async_to_streamed_response_wrapper(
            google_drives.update_setting,
        )
