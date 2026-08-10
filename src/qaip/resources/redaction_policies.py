# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    redaction_policy_create_params,
    redaction_policy_archive_params,
    redaction_policy_validate_params,
    redaction_policy_list_versions_params,
    redaction_policy_create_version_params,
    redaction_policy_activate_version_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.policy_detail import PolicyDetail
from ..types.policy_version import PolicyVersion
from ..types.policy_versions import PolicyVersions
from ..types.redaction_policy_list_response import RedactionPolicyListResponse
from ..types.redaction_policy_validate_response import RedactionPolicyValidateResponse

__all__ = ["RedactionPoliciesResource", "AsyncRedactionPoliciesResource"]


class RedactionPoliciesResource(SyncAPIResource):
    """
    Tenant redaction policy management (requires the `policy:redaction:manage` scope)
    """

    @cached_property
    def with_raw_response(self) -> RedactionPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return RedactionPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RedactionPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return RedactionPoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        business_confidential: redaction_policy_create_params.BusinessConfidential,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyVersion:
        """Creates the first DRAFT for a tenant-local name.

        Replaying the same normalized
        DRAFT returns 200; a new DRAFT returns 201. Required scope:
        `policy:redaction:manage`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/redaction/policies",
            body=maybe_transform(
                {
                    "business_confidential": business_confidential,
                    "name": name,
                    "description": description,
                },
                redaction_policy_create_params.RedactionPolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyVersion,
        )

    def retrieve(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyDetail:
        """Built-in policies have an ACTIVE snapshot only.

        An archived-only tenant name is
        returned with both current snapshots null. Required scope:
        `policy:redaction:manage`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            path_template("/redaction/policies/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyDetail,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedactionPolicyListResponse:
        """Returns summaries only; policy definitions are not included.

        Required scope:
        `policy:redaction:manage`.
        """
        return self._get(
            "/redaction/policies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedactionPolicyListResponse,
        )

    def activate_version(
        self,
        version: str,
        *,
        name: str,
        expected_active_version: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyVersion:
        """
        Revalidates the stored snapshot and changes ACTIVE only when
        expectedActiveVersion matches. null means that no ACTIVE version is expected.
        Required scope: `policy:redaction:manage`.

        Args:
          expected_active_version: null requires that no ACTIVE version currently exists.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return self._post(
            path_template("/redaction/policies/{name}/versions/{version}/activate", name=name, version=version),
            body=maybe_transform(
                {"expected_active_version": expected_active_version},
                redaction_policy_activate_version_params.RedactionPolicyActivateVersionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyVersion,
        )

    def archive(
        self,
        name: str,
        *,
        expected_active_version: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyDetail:
        """Leaves any DRAFT unchanged.

        null means that no ACTIVE version is expected.
        Required scope: `policy:redaction:manage`.

        Args:
          expected_active_version: null requires that no ACTIVE version currently exists.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._post(
            path_template("/redaction/policies/{name}/archive", name=name),
            body=maybe_transform(
                {"expected_active_version": expected_active_version},
                redaction_policy_archive_params.RedactionPolicyArchiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyDetail,
        )

    def create_version(
        self,
        name: str,
        *,
        business_confidential: redaction_policy_create_version_params.BusinessConfidential,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyVersion:
        """Appends MAX(version)+1 for an existing tenant name.

        The version is assigned by
        the server. Required scope: `policy:redaction:manage`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._post(
            path_template("/redaction/policies/{name}/versions", name=name),
            body=maybe_transform(
                {
                    "business_confidential": business_confidential,
                    "description": description,
                },
                redaction_policy_create_version_params.RedactionPolicyCreateVersionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyVersion,
        )

    def delete_version(
        self,
        version: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Hard-deletes only a DRAFT that has never been ACTIVE.

        Required scope:
        `policy:redaction:manage`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/redaction/policies/{name}/versions/{version}", name=name, version=version),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_versions(
        self,
        name: str,
        *,
        before_version: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyVersions:
        """Uses the opaque server-returned beforeVersion cursor.

        Version summaries do not
        contain a policy definition. Required scope: `policy:redaction:manage`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            path_template("/redaction/policies/{name}/versions", name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before_version": before_version,
                        "limit": limit,
                    },
                    redaction_policy_list_versions_params.RedactionPolicyListVersionsParams,
                ),
            ),
            cast_to=PolicyVersions,
        )

    def retrieve_version(
        self,
        version: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyVersion:
        """Returns the canonical definition for the requested version.

        Required scope:
        `policy:redaction:manage`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return self._get(
            path_template("/redaction/policies/{name}/versions/{version}", name=name, version=version),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyVersion,
        )

    def validate(
        self,
        *,
        business_confidential: redaction_policy_validate_params.BusinessConfidential,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedactionPolicyValidateResponse:
        """
        Normalizes and validates a schema version 1 tenant policy, then returns the
        canonical definition and behavior digest without accessing the tenant policy
        store. Required scope: `policy:redaction:manage`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/redaction/policies/validate",
            body=maybe_transform(
                {
                    "business_confidential": business_confidential,
                    "name": name,
                    "description": description,
                },
                redaction_policy_validate_params.RedactionPolicyValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedactionPolicyValidateResponse,
        )


class AsyncRedactionPoliciesResource(AsyncAPIResource):
    """
    Tenant redaction policy management (requires the `policy:redaction:manage` scope)
    """

    @cached_property
    def with_raw_response(self) -> AsyncRedactionPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRedactionPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRedactionPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncRedactionPoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        business_confidential: redaction_policy_create_params.BusinessConfidential,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyVersion:
        """Creates the first DRAFT for a tenant-local name.

        Replaying the same normalized
        DRAFT returns 200; a new DRAFT returns 201. Required scope:
        `policy:redaction:manage`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/redaction/policies",
            body=await async_maybe_transform(
                {
                    "business_confidential": business_confidential,
                    "name": name,
                    "description": description,
                },
                redaction_policy_create_params.RedactionPolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyVersion,
        )

    async def retrieve(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyDetail:
        """Built-in policies have an ACTIVE snapshot only.

        An archived-only tenant name is
        returned with both current snapshots null. Required scope:
        `policy:redaction:manage`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            path_template("/redaction/policies/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyDetail,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedactionPolicyListResponse:
        """Returns summaries only; policy definitions are not included.

        Required scope:
        `policy:redaction:manage`.
        """
        return await self._get(
            "/redaction/policies",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedactionPolicyListResponse,
        )

    async def activate_version(
        self,
        version: str,
        *,
        name: str,
        expected_active_version: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyVersion:
        """
        Revalidates the stored snapshot and changes ACTIVE only when
        expectedActiveVersion matches. null means that no ACTIVE version is expected.
        Required scope: `policy:redaction:manage`.

        Args:
          expected_active_version: null requires that no ACTIVE version currently exists.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return await self._post(
            path_template("/redaction/policies/{name}/versions/{version}/activate", name=name, version=version),
            body=await async_maybe_transform(
                {"expected_active_version": expected_active_version},
                redaction_policy_activate_version_params.RedactionPolicyActivateVersionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyVersion,
        )

    async def archive(
        self,
        name: str,
        *,
        expected_active_version: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyDetail:
        """Leaves any DRAFT unchanged.

        null means that no ACTIVE version is expected.
        Required scope: `policy:redaction:manage`.

        Args:
          expected_active_version: null requires that no ACTIVE version currently exists.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._post(
            path_template("/redaction/policies/{name}/archive", name=name),
            body=await async_maybe_transform(
                {"expected_active_version": expected_active_version},
                redaction_policy_archive_params.RedactionPolicyArchiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyDetail,
        )

    async def create_version(
        self,
        name: str,
        *,
        business_confidential: redaction_policy_create_version_params.BusinessConfidential,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyVersion:
        """Appends MAX(version)+1 for an existing tenant name.

        The version is assigned by
        the server. Required scope: `policy:redaction:manage`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._post(
            path_template("/redaction/policies/{name}/versions", name=name),
            body=await async_maybe_transform(
                {
                    "business_confidential": business_confidential,
                    "description": description,
                },
                redaction_policy_create_version_params.RedactionPolicyCreateVersionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyVersion,
        )

    async def delete_version(
        self,
        version: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Hard-deletes only a DRAFT that has never been ACTIVE.

        Required scope:
        `policy:redaction:manage`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/redaction/policies/{name}/versions/{version}", name=name, version=version),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_versions(
        self,
        name: str,
        *,
        before_version: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyVersions:
        """Uses the opaque server-returned beforeVersion cursor.

        Version summaries do not
        contain a policy definition. Required scope: `policy:redaction:manage`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            path_template("/redaction/policies/{name}/versions", name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "before_version": before_version,
                        "limit": limit,
                    },
                    redaction_policy_list_versions_params.RedactionPolicyListVersionsParams,
                ),
            ),
            cast_to=PolicyVersions,
        )

    async def retrieve_version(
        self,
        version: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyVersion:
        """Returns the canonical definition for the requested version.

        Required scope:
        `policy:redaction:manage`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return await self._get(
            path_template("/redaction/policies/{name}/versions/{version}", name=name, version=version),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyVersion,
        )

    async def validate(
        self,
        *,
        business_confidential: redaction_policy_validate_params.BusinessConfidential,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedactionPolicyValidateResponse:
        """
        Normalizes and validates a schema version 1 tenant policy, then returns the
        canonical definition and behavior digest without accessing the tenant policy
        store. Required scope: `policy:redaction:manage`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/redaction/policies/validate",
            body=await async_maybe_transform(
                {
                    "business_confidential": business_confidential,
                    "name": name,
                    "description": description,
                },
                redaction_policy_validate_params.RedactionPolicyValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedactionPolicyValidateResponse,
        )


class RedactionPoliciesResourceWithRawResponse:
    def __init__(self, redaction_policies: RedactionPoliciesResource) -> None:
        self._redaction_policies = redaction_policies

        self.create = to_raw_response_wrapper(
            redaction_policies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            redaction_policies.retrieve,
        )
        self.list = to_raw_response_wrapper(
            redaction_policies.list,
        )
        self.activate_version = to_raw_response_wrapper(
            redaction_policies.activate_version,
        )
        self.archive = to_raw_response_wrapper(
            redaction_policies.archive,
        )
        self.create_version = to_raw_response_wrapper(
            redaction_policies.create_version,
        )
        self.delete_version = to_raw_response_wrapper(
            redaction_policies.delete_version,
        )
        self.list_versions = to_raw_response_wrapper(
            redaction_policies.list_versions,
        )
        self.retrieve_version = to_raw_response_wrapper(
            redaction_policies.retrieve_version,
        )
        self.validate = to_raw_response_wrapper(
            redaction_policies.validate,
        )


class AsyncRedactionPoliciesResourceWithRawResponse:
    def __init__(self, redaction_policies: AsyncRedactionPoliciesResource) -> None:
        self._redaction_policies = redaction_policies

        self.create = async_to_raw_response_wrapper(
            redaction_policies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            redaction_policies.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            redaction_policies.list,
        )
        self.activate_version = async_to_raw_response_wrapper(
            redaction_policies.activate_version,
        )
        self.archive = async_to_raw_response_wrapper(
            redaction_policies.archive,
        )
        self.create_version = async_to_raw_response_wrapper(
            redaction_policies.create_version,
        )
        self.delete_version = async_to_raw_response_wrapper(
            redaction_policies.delete_version,
        )
        self.list_versions = async_to_raw_response_wrapper(
            redaction_policies.list_versions,
        )
        self.retrieve_version = async_to_raw_response_wrapper(
            redaction_policies.retrieve_version,
        )
        self.validate = async_to_raw_response_wrapper(
            redaction_policies.validate,
        )


class RedactionPoliciesResourceWithStreamingResponse:
    def __init__(self, redaction_policies: RedactionPoliciesResource) -> None:
        self._redaction_policies = redaction_policies

        self.create = to_streamed_response_wrapper(
            redaction_policies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            redaction_policies.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            redaction_policies.list,
        )
        self.activate_version = to_streamed_response_wrapper(
            redaction_policies.activate_version,
        )
        self.archive = to_streamed_response_wrapper(
            redaction_policies.archive,
        )
        self.create_version = to_streamed_response_wrapper(
            redaction_policies.create_version,
        )
        self.delete_version = to_streamed_response_wrapper(
            redaction_policies.delete_version,
        )
        self.list_versions = to_streamed_response_wrapper(
            redaction_policies.list_versions,
        )
        self.retrieve_version = to_streamed_response_wrapper(
            redaction_policies.retrieve_version,
        )
        self.validate = to_streamed_response_wrapper(
            redaction_policies.validate,
        )


class AsyncRedactionPoliciesResourceWithStreamingResponse:
    def __init__(self, redaction_policies: AsyncRedactionPoliciesResource) -> None:
        self._redaction_policies = redaction_policies

        self.create = async_to_streamed_response_wrapper(
            redaction_policies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            redaction_policies.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            redaction_policies.list,
        )
        self.activate_version = async_to_streamed_response_wrapper(
            redaction_policies.activate_version,
        )
        self.archive = async_to_streamed_response_wrapper(
            redaction_policies.archive,
        )
        self.create_version = async_to_streamed_response_wrapper(
            redaction_policies.create_version,
        )
        self.delete_version = async_to_streamed_response_wrapper(
            redaction_policies.delete_version,
        )
        self.list_versions = async_to_streamed_response_wrapper(
            redaction_policies.list_versions,
        )
        self.retrieve_version = async_to_streamed_response_wrapper(
            redaction_policies.retrieve_version,
        )
        self.validate = async_to_streamed_response_wrapper(
            redaction_policies.validate,
        )
