# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import GitHubReferenceType, github_list_params, github_create_params, github_update_setting_params
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
from .._base_client import make_request_options
from ..types.github import GitHub
from ..types.github_setting import GitHubSetting
from ..types.github_list_response import GitHubListResponse
from ..types.github_reference_type import GitHubReferenceType
from ..types.shared_params.metadata import Metadata

__all__ = ["GithubsResource", "AsyncGithubsResource"]


class GithubsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GithubsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return GithubsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GithubsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return GithubsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        repository: str,
        github_token: str | Omit = omit,
        metadata: Metadata | Omit = omit,
        path_filters: SequenceNotStr[str] | Omit = omit,
        reference_param: str | Omit = omit,
        reference_type: GitHubReferenceType | Omit = omit,
        rrule: str | Omit = omit,
        secret_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHub:
        """<p> Creates a new GitHub data source and starts ingestion.

        </p> <p> Required roles: All </p>

        Args:
          name: Name of the GitHub data source

          repository: GitHub repository in owner/repo format (e.g. "octocat/Hello-World")

          github_token: One-time GitHub personal access token (mutually exclusive with secret_id)

          metadata: (reserved for future use) Additional metadata for the GitHub data source

          path_filters: Path filters patterns. The total number of characters across all elements in the
              array must be 2000 or fewer.

          reference_param: Reference parameter (branch name, tag name, or commit hash)

          reference_type: Git reference type

          rrule: Recurrence rule (RFC 5545 RRULE). Requires secret_id (not one-time token).

          secret_id: ID of a stored secret to use (mutually exclusive with github_token)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/githubs",
            body=maybe_transform(
                {
                    "name": name,
                    "repository": repository,
                    "github_token": github_token,
                    "metadata": metadata,
                    "path_filters": path_filters,
                    "reference_param": reference_param,
                    "reference_type": reference_type,
                    "rrule": rrule,
                    "secret_id": secret_id,
                },
                github_create_params.GitHubCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHub,
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
    ) -> GitHub:
        """<p> Gets detailed information about a specific GitHub data source.

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
            path_template("/githubs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHub,
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
    ) -> GitHubListResponse:
        """<p> Lists GitHub data sources with cursor-based pagination.

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
            "/githubs",
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
                    github_list_params.GitHubListParams,
                ),
            ),
            cast_to=GitHubListResponse,
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
    ) -> GitHub:
        """<p> Initiates an asynchronous deletion job for the specified GitHub data source.

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
            path_template("/githubs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHub,
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
    ) -> GitHubSetting:
        """<p> Gets the setting (schedule, repository, etc.) for GitHub data sources.

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
            path_template("/github-settings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubSetting,
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
    ) -> GitHubSetting:
        """<p> Updates the setting (name, schedule) for GitHub data sources.

        </p> <p> Required roles: All </p>

        Args:
          name: Name of the GitHub data source

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
            path_template("/github-settings/{id}", id=id),
            body=maybe_transform(
                {
                    "name": name,
                    "rrule": rrule,
                },
                github_update_setting_params.GitHubUpdateSettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubSetting,
        )


class AsyncGithubsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGithubsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGithubsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGithubsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncGithubsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        repository: str,
        github_token: str | Omit = omit,
        metadata: Metadata | Omit = omit,
        path_filters: SequenceNotStr[str] | Omit = omit,
        reference_param: str | Omit = omit,
        reference_type: GitHubReferenceType | Omit = omit,
        rrule: str | Omit = omit,
        secret_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHub:
        """<p> Creates a new GitHub data source and starts ingestion.

        </p> <p> Required roles: All </p>

        Args:
          name: Name of the GitHub data source

          repository: GitHub repository in owner/repo format (e.g. "octocat/Hello-World")

          github_token: One-time GitHub personal access token (mutually exclusive with secret_id)

          metadata: (reserved for future use) Additional metadata for the GitHub data source

          path_filters: Path filters patterns. The total number of characters across all elements in the
              array must be 2000 or fewer.

          reference_param: Reference parameter (branch name, tag name, or commit hash)

          reference_type: Git reference type

          rrule: Recurrence rule (RFC 5545 RRULE). Requires secret_id (not one-time token).

          secret_id: ID of a stored secret to use (mutually exclusive with github_token)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/githubs",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "repository": repository,
                    "github_token": github_token,
                    "metadata": metadata,
                    "path_filters": path_filters,
                    "reference_param": reference_param,
                    "reference_type": reference_type,
                    "rrule": rrule,
                    "secret_id": secret_id,
                },
                github_create_params.GitHubCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHub,
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
    ) -> GitHub:
        """<p> Gets detailed information about a specific GitHub data source.

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
            path_template("/githubs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHub,
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
    ) -> GitHubListResponse:
        """<p> Lists GitHub data sources with cursor-based pagination.

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
            "/githubs",
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
                    github_list_params.GitHubListParams,
                ),
            ),
            cast_to=GitHubListResponse,
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
    ) -> GitHub:
        """<p> Initiates an asynchronous deletion job for the specified GitHub data source.

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
            path_template("/githubs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHub,
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
    ) -> GitHubSetting:
        """<p> Gets the setting (schedule, repository, etc.) for GitHub data sources.

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
            path_template("/github-settings/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubSetting,
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
    ) -> GitHubSetting:
        """<p> Updates the setting (name, schedule) for GitHub data sources.

        </p> <p> Required roles: All </p>

        Args:
          name: Name of the GitHub data source

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
            path_template("/github-settings/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "rrule": rrule,
                },
                github_update_setting_params.GitHubUpdateSettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubSetting,
        )


class GithubsResourceWithRawResponse:
    def __init__(self, githubs: GithubsResource) -> None:
        self._githubs = githubs

        self.create = to_raw_response_wrapper(
            githubs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            githubs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            githubs.list,
        )
        self.delete = to_raw_response_wrapper(
            githubs.delete,
        )
        self.retrieve_setting = to_raw_response_wrapper(
            githubs.retrieve_setting,
        )
        self.update_setting = to_raw_response_wrapper(
            githubs.update_setting,
        )


class AsyncGithubsResourceWithRawResponse:
    def __init__(self, githubs: AsyncGithubsResource) -> None:
        self._githubs = githubs

        self.create = async_to_raw_response_wrapper(
            githubs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            githubs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            githubs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            githubs.delete,
        )
        self.retrieve_setting = async_to_raw_response_wrapper(
            githubs.retrieve_setting,
        )
        self.update_setting = async_to_raw_response_wrapper(
            githubs.update_setting,
        )


class GithubsResourceWithStreamingResponse:
    def __init__(self, githubs: GithubsResource) -> None:
        self._githubs = githubs

        self.create = to_streamed_response_wrapper(
            githubs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            githubs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            githubs.list,
        )
        self.delete = to_streamed_response_wrapper(
            githubs.delete,
        )
        self.retrieve_setting = to_streamed_response_wrapper(
            githubs.retrieve_setting,
        )
        self.update_setting = to_streamed_response_wrapper(
            githubs.update_setting,
        )


class AsyncGithubsResourceWithStreamingResponse:
    def __init__(self, githubs: AsyncGithubsResource) -> None:
        self._githubs = githubs

        self.create = async_to_streamed_response_wrapper(
            githubs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            githubs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            githubs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            githubs.delete,
        )
        self.retrieve_setting = async_to_streamed_response_wrapper(
            githubs.retrieve_setting,
        )
        self.update_setting = async_to_streamed_response_wrapper(
            githubs.update_setting,
        )
