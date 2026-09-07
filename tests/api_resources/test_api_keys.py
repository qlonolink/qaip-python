# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from qaip import Qaip, AsyncQaip
from qaip.types import (
    CreatedAPIKey,
    CreatedExpiringAPIKey,
)
from qaip._utils import parse_datetime
from tests.utils import assert_matches_type

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Qaip) -> None:
        with pytest.warns(DeprecationWarning):
            api_key = client.api_keys.create(
                name="x",
                scopes=["inference:run"],
            )

        assert_matches_type(CreatedAPIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Qaip) -> None:
        with pytest.warns(DeprecationWarning):
            api_key = client.api_keys.create(
                name="x",
                scopes=["inference:run"],
                description="description",
            )

        assert_matches_type(CreatedAPIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Qaip) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.api_keys.with_raw_response.create(
                name="x",
                scopes=["inference:run"],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(CreatedAPIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Qaip) -> None:
        with pytest.warns(DeprecationWarning):
            with client.api_keys.with_streaming_response.create(
                name="x",
                scopes=["inference:run"],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                api_key = response.parse()
                assert_matches_type(CreatedAPIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_expiring(self, client: Qaip) -> None:
        api_key = client.api_keys.create_expiring(
            key_kind="personal",
            name="x",
            scopes=["inference:run"],
            idempotency_key="x",
        )
        assert_matches_type(CreatedExpiringAPIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_expiring_with_all_params(self, client: Qaip) -> None:
        api_key = client.api_keys.create_expiring(
            key_kind="personal",
            name="x",
            scopes=["inference:run"],
            idempotency_key="x",
            description="description",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            ttl=300,
        )
        assert_matches_type(CreatedExpiringAPIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_expiring(self, client: Qaip) -> None:
        response = client.api_keys.with_raw_response.create_expiring(
            key_kind="personal",
            name="x",
            scopes=["inference:run"],
            idempotency_key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(CreatedExpiringAPIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_expiring(self, client: Qaip) -> None:
        with client.api_keys.with_streaming_response.create_expiring(
            key_kind="personal",
            name="x",
            scopes=["inference:run"],
            idempotency_key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(CreatedExpiringAPIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke(self, client: Qaip) -> None:
        api_key = client.api_keys.revoke(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke(self, client: Qaip) -> None:
        response = client.api_keys.with_raw_response.revoke(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke(self, client: Qaip) -> None:
        with client.api_keys.with_streaming_response.revoke(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert api_key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_revoke(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_id` but received ''"):
            client.api_keys.with_raw_response.revoke(
                "",
            )


class TestAsyncAPIKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncQaip) -> None:
        with pytest.warns(DeprecationWarning):
            api_key = await async_client.api_keys.create(
                name="x",
                scopes=["inference:run"],
            )

        assert_matches_type(CreatedAPIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncQaip) -> None:
        with pytest.warns(DeprecationWarning):
            api_key = await async_client.api_keys.create(
                name="x",
                scopes=["inference:run"],
                description="description",
            )

        assert_matches_type(CreatedAPIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncQaip) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.api_keys.with_raw_response.create(
                name="x",
                scopes=["inference:run"],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(CreatedAPIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncQaip) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.api_keys.with_streaming_response.create(
                name="x",
                scopes=["inference:run"],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                api_key = await response.parse()
                assert_matches_type(CreatedAPIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_expiring(self, async_client: AsyncQaip) -> None:
        api_key = await async_client.api_keys.create_expiring(
            key_kind="personal",
            name="x",
            scopes=["inference:run"],
            idempotency_key="x",
        )
        assert_matches_type(CreatedExpiringAPIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_expiring_with_all_params(self, async_client: AsyncQaip) -> None:
        api_key = await async_client.api_keys.create_expiring(
            key_kind="personal",
            name="x",
            scopes=["inference:run"],
            idempotency_key="x",
            description="description",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            ttl=300,
        )
        assert_matches_type(CreatedExpiringAPIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_expiring(self, async_client: AsyncQaip) -> None:
        response = await async_client.api_keys.with_raw_response.create_expiring(
            key_kind="personal",
            name="x",
            scopes=["inference:run"],
            idempotency_key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(CreatedExpiringAPIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_expiring(self, async_client: AsyncQaip) -> None:
        async with async_client.api_keys.with_streaming_response.create_expiring(
            key_kind="personal",
            name="x",
            scopes=["inference:run"],
            idempotency_key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(CreatedExpiringAPIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke(self, async_client: AsyncQaip) -> None:
        api_key = await async_client.api_keys.revoke(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncQaip) -> None:
        response = await async_client.api_keys.with_raw_response.revoke(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncQaip) -> None:
        async with async_client.api_keys.with_streaming_response.revoke(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert api_key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_id` but received ''"):
            await async_client.api_keys.with_raw_response.revoke(
                "",
            )
