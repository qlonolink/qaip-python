# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import api_key_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.created_api_key import CreatedApiKey
from ..types.issuable_api_key_scope import IssuableApiKeyScope

__all__ = ["ApiKeysResource", "AsyncApiKeysResource"]


class ApiKeysResource(SyncAPIResource):
    """API key issuance"""

    @cached_property
    def with_raw_response(self) -> ApiKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return ApiKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApiKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return ApiKeysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        scopes: List[IssuableApiKeyScope],
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedApiKey:
        """<p> Issues a new API key with the requested scopes.

        The plaintext key is returned only in this response and cannot be retrieved
        afterwards. </p> <p> Required scope: `apikeys:issue` </p> <p> The issued key is
        always weaker than the caller: the requested scopes must be a subset of the
        scopes held by the calling key, `apikeys:issue` itself cannot be granted, and
        `external_data:*` scopes are not issuable through this endpoint (they require
        dashboard sign-in). </p>

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
        # 発行は冪等ではない。応答が失われただけの再送でも鍵は増え、しかも平文は
        # 最初の応答にしか無いので「利用者が知らない有効な鍵」が残る。
        # 取りこぼすくらいなら失敗させる方が安全なので、この操作だけ再試行しない。
        options["max_retries"] = 0
        return self._post(
            "/api-keys",
            body=maybe_transform(
                {
                    "name": name,
                    "scopes": scopes,
                    "description": description,
                },
                api_key_create_params.ApiKeyCreateParams,
            ),
            options=options,
            cast_to=CreatedApiKey,
        )


class AsyncApiKeysResource(AsyncAPIResource):
    """API key issuance"""

    @cached_property
    def with_raw_response(self) -> AsyncApiKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApiKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApiKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncApiKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        scopes: List[IssuableApiKeyScope],
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedApiKey:
        """<p> Issues a new API key with the requested scopes.

        The plaintext key is returned only in this response and cannot be retrieved
        afterwards. </p> <p> Required scope: `apikeys:issue` </p> <p> The issued key is
        always weaker than the caller: the requested scopes must be a subset of the
        scopes held by the calling key, `apikeys:issue` itself cannot be granted, and
        `external_data:*` scopes are not issuable through this endpoint (they require
        dashboard sign-in). </p>

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
        # 同期側と同じ理由で、発行だけは自動再試行を無効にする。
        options["max_retries"] = 0
        return await self._post(
            "/api-keys",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "scopes": scopes,
                    "description": description,
                },
                api_key_create_params.ApiKeyCreateParams,
            ),
            options=options,
            cast_to=CreatedApiKey,
        )


class ApiKeysResourceWithRawResponse:
    def __init__(self, api_keys: ApiKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_raw_response_wrapper(
            api_keys.create,
        )


class AsyncApiKeysResourceWithRawResponse:
    def __init__(self, api_keys: AsyncApiKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_raw_response_wrapper(
            api_keys.create,
        )


class ApiKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: ApiKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_streamed_response_wrapper(
            api_keys.create,
        )


class AsyncApiKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: AsyncApiKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_streamed_response_wrapper(
            api_keys.create,
        )
