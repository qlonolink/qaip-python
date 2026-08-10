# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest

from qaip import Qaip, AsyncQaip, APIStatusError
from qaip.types import CreatedApiKey
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApiKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Qaip) -> None:
        api_key = client.api_keys.create(
            name="name",
            scopes=["inference:run"],
        )
        assert_matches_type(CreatedApiKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Qaip) -> None:
        api_key = client.api_keys.create(
            name="name",
            scopes=["inference:run"],
            description="description",
        )
        assert_matches_type(CreatedApiKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Qaip) -> None:
        response = client.api_keys.with_raw_response.create(
            name="name",
            scopes=["inference:run"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(CreatedApiKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Qaip) -> None:
        with client.api_keys.with_streaming_response.create(
            name="name",
            scopes=["inference:run"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(CreatedApiKey, api_key, path=["response"])

        assert cast("Any", response.is_closed) is True


class TestAsyncApiKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncQaip) -> None:
        api_key = await async_client.api_keys.create(
            name="name",
            scopes=["inference:run"],
        )
        assert_matches_type(CreatedApiKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncQaip) -> None:
        api_key = await async_client.api_keys.create(
            name="name",
            scopes=["inference:run"],
            description="description",
        )
        assert_matches_type(CreatedApiKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncQaip) -> None:
        response = await async_client.api_keys.with_raw_response.create(
            name="name",
            scopes=["inference:run"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(CreatedApiKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncQaip) -> None:
        async with async_client.api_keys.with_streaming_response.create(
            name="name",
            scopes=["inference:run"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(CreatedApiKey, api_key, path=["response"])

        assert cast("Any", response.is_closed) is True


def _issued_payload(request: httpx.Request) -> httpx.Response:
    return httpx.Response(
        201,
        json={
            "id": "019febbe-235a-7d69-a141-be4bbef5bb03",
            "name": "n",
            "key": "qaip_plaintext",
            "scopes": ["inference:run"],
            "creation_time": 1,
        },
        request=request,
    )


class TestApiKeyIssuanceIsNotRetried:
    """発行は冪等でないため、応答が失われた再送で鍵が重複してはいけない。"""

    def test_sync_create_does_not_retry_on_5xx(self) -> None:
        calls: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(request)
            if len(calls) == 1:
                return httpx.Response(
                    500,
                    json={"error": "lost after commit"},
                    headers={"x-should-retry": "true", "retry-after-ms": "0"},
                    request=request,
                )
            return _issued_payload(request)

        client = Qaip(
            api_key="caller",
            base_url="https://example.test",
            http_client=httpx.Client(transport=httpx.MockTransport(handler)),
        )
        with pytest.raises(APIStatusError):
            client.api_keys.create(name="n", scopes=["inference:run"])
        assert len(calls) == 1

    async def test_async_create_does_not_retry_on_5xx(self) -> None:
        calls: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(request)
            if len(calls) == 1:
                return httpx.Response(
                    500,
                    json={"error": "lost after commit"},
                    headers={"x-should-retry": "true", "retry-after-ms": "0"},
                    request=request,
                )
            return _issued_payload(request)

        client = AsyncQaip(
            api_key="caller",
            base_url="https://example.test",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        with pytest.raises(APIStatusError):
            await client.api_keys.create(name="n", scopes=["inference:run"])
        assert len(calls) == 1
