# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import List, Union
from datetime import datetime

import httpx

from ..types import APIKeyKind, api_key_create_params, api_key_create_expiring_params
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
from ..types.api_key_kind import APIKeyKind
from ..types.created_api_key import CreatedAPIKey
from ..types.issuable_api_key_scope import IssuableAPIKeyScope
from ..types.created_expiring_api_key import CreatedExpiringAPIKey

__all__ = ["APIKeysResource", "AsyncAPIKeysResource"]


class APIKeysResource(SyncAPIResource):
    """API key issuance (requires the `apikeys:issue` scope)"""

    @cached_property
    def with_raw_response(self) -> APIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return APIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return APIKeysResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def create(
        self,
        *,
        name: str,
        scopes: List[IssuableAPIKeyScope],
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedAPIKey:
        """<p> Issues a new API key with the requested scopes.

        The plaintext key is returned only in this response and cannot be retrieved afterwards. </p> <p> Required scope: `apikeys:issue` </p> <p> The issued key is always weaker than the caller: the requested scopes must be a subset of the scopes held by the calling key, `apikeys:issue` itself cannot be granted, and `external_data:*` scopes are not issuable through this endpoint (they require dashboard sign-in). </p> <p> This endpoint accepts API key authentication only. Issuing from the dashboard is done in the console, which is also the only way to grant `apikeys:issue` and `external_data:*`. </p>

        Args:
          name: Name of the API key

          scopes: Scopes granted to the issued key. Must be a subset of the caller's scopes.

          description: Description of the API key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        options = make_request_options(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        # 旧発行APIは冪等でないため、応答喪失後の再送で回収不能な鍵を増やさない。
        options["max_retries"] = 0
        return self._post(
            "/api-keys",
            body=maybe_transform(
                {
                    "name": name,
                    "scopes": scopes,
                    "description": description,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=options,
            cast_to=CreatedAPIKey,
        )

    def create_expiring(
        self,
        *,
        key_kind: APIKeyKind,
        name: str,
        scopes: List[IssuableAPIKeyScope],
        idempotency_key: str,
        description: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        ttl: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedExpiringAPIKey:
        """Issues an API key that expires at a caller-selected time.

        Exactly one of
        `expires_at` or `ttl` is required. The plaintext key is returned only for the
        first successful request. If that response is lost, repeating the same request
        and Idempotency-Key returns `credential_already_created` with the non-secret key
        ID; revoke that key and retry with a new Idempotency-Key.

        Args:
          key_kind: Principal binding of the issued API key.

          name: Name of the API key

          scopes: Scopes granted to the issued key. Must be a subset of the caller's scopes.

          description: Description of the API key

          expires_at: Absolute expiration time. Mutually exclusive with `ttl`.

          ttl: Lifetime in seconds. Mutually exclusive with `expires_at`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return self._post(
            "/api-keys/expiring",
            body=maybe_transform(
                {
                    "key_kind": key_kind,
                    "name": name,
                    "scopes": scopes,
                    "description": description,
                    "expires_at": expires_at,
                    "ttl": ttl,
                },
                api_key_create_expiring_params.APIKeyCreateExpiringParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedExpiringAPIKey,
        )

    def revoke(
        self,
        api_key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Revokes an API key bound to the authenticated caller.

        Repeating the request is
        safe and does not change the original revocation time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_id:
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api-keys/{api_key_id}", api_key_id=api_key_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAPIKeysResource(AsyncAPIResource):
    """API key issuance (requires the `apikeys:issue` scope)"""

    @cached_property
    def with_raw_response(self) -> AsyncAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncAPIKeysResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def create(
        self,
        *,
        name: str,
        scopes: List[IssuableAPIKeyScope],
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedAPIKey:
        """<p> Issues a new API key with the requested scopes.

        The plaintext key is returned only in this response and cannot be retrieved afterwards. </p> <p> Required scope: `apikeys:issue` </p> <p> The issued key is always weaker than the caller: the requested scopes must be a subset of the scopes held by the calling key, `apikeys:issue` itself cannot be granted, and `external_data:*` scopes are not issuable through this endpoint (they require dashboard sign-in). </p> <p> This endpoint accepts API key authentication only. Issuing from the dashboard is done in the console, which is also the only way to grant `apikeys:issue` and `external_data:*`. </p>

        Args:
          name: Name of the API key

          scopes: Scopes granted to the issued key. Must be a subset of the caller's scopes.

          description: Description of the API key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        options = make_request_options(
            extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
        # 同期APIと同様に、非冪等な鍵発行の自動再試行を禁止する。
        options["max_retries"] = 0
        return await self._post(
            "/api-keys",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "scopes": scopes,
                    "description": description,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=options,
            cast_to=CreatedAPIKey,
        )

    async def create_expiring(
        self,
        *,
        key_kind: APIKeyKind,
        name: str,
        scopes: List[IssuableAPIKeyScope],
        idempotency_key: str,
        description: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        ttl: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedExpiringAPIKey:
        """Issues an API key that expires at a caller-selected time.

        Exactly one of
        `expires_at` or `ttl` is required. The plaintext key is returned only for the
        first successful request. If that response is lost, repeating the same request
        and Idempotency-Key returns `credential_already_created` with the non-secret key
        ID; revoke that key and retry with a new Idempotency-Key.

        Args:
          key_kind: Principal binding of the issued API key.

          name: Name of the API key

          scopes: Scopes granted to the issued key. Must be a subset of the caller's scopes.

          description: Description of the API key

          expires_at: Absolute expiration time. Mutually exclusive with `ttl`.

          ttl: Lifetime in seconds. Mutually exclusive with `expires_at`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return await self._post(
            "/api-keys/expiring",
            body=await async_maybe_transform(
                {
                    "key_kind": key_kind,
                    "name": name,
                    "scopes": scopes,
                    "description": description,
                    "expires_at": expires_at,
                    "ttl": ttl,
                },
                api_key_create_expiring_params.APIKeyCreateExpiringParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedExpiringAPIKey,
        )

    async def revoke(
        self,
        api_key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Revokes an API key bound to the authenticated caller.

        Repeating the request is
        safe and does not change the original revocation time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_id:
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api-keys/{api_key_id}", api_key_id=api_key_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class APIKeysResourceWithRawResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                api_keys.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_expiring = to_raw_response_wrapper(
            api_keys.create_expiring,
        )
        self.revoke = to_raw_response_wrapper(
            api_keys.revoke,
        )


class AsyncAPIKeysResourceWithRawResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                api_keys.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_expiring = async_to_raw_response_wrapper(
            api_keys.create_expiring,
        )
        self.revoke = async_to_raw_response_wrapper(
            api_keys.revoke,
        )


class APIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                api_keys.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_expiring = to_streamed_response_wrapper(
            api_keys.create_expiring,
        )
        self.revoke = to_streamed_response_wrapper(
            api_keys.revoke,
        )


class AsyncAPIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                api_keys.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_expiring = async_to_streamed_response_wrapper(
            api_keys.create_expiring,
        )
        self.revoke = async_to_streamed_response_wrapper(
            api_keys.revoke,
        )
