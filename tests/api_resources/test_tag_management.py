# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from qaip import Qaip, AsyncQaip
from tests.utils import assert_matches_type
from qaip.types.shared import Tag

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTagManagement:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Qaip) -> None:
        tag_management = client.tag_management.create(
            name="name",
        )
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Qaip) -> None:
        tag_management = client.tag_management.create(
            name="name",
            description="description",
        )
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Qaip) -> None:
        response = client.tag_management.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_management = response.parse()
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Qaip) -> None:
        with client.tag_management.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_management = response.parse()
            assert_matches_type(Tag, tag_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Qaip) -> None:
        tag_management = client.tag_management.update(
            id="id",
        )
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Qaip) -> None:
        tag_management = client.tag_management.update(
            id="id",
            description="description",
            name="name",
        )
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Qaip) -> None:
        response = client.tag_management.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_management = response.parse()
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Qaip) -> None:
        with client.tag_management.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_management = response.parse()
            assert_matches_type(Tag, tag_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tag_management.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Qaip) -> None:
        tag_management = client.tag_management.delete(
            "id",
        )
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Qaip) -> None:
        response = client.tag_management.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_management = response.parse()
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Qaip) -> None:
        with client.tag_management.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_management = response.parse()
            assert_matches_type(Tag, tag_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tag_management.with_raw_response.delete(
                "",
            )


class TestAsyncTagManagement:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncQaip) -> None:
        tag_management = await async_client.tag_management.create(
            name="name",
        )
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncQaip) -> None:
        tag_management = await async_client.tag_management.create(
            name="name",
            description="description",
        )
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncQaip) -> None:
        response = await async_client.tag_management.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_management = await response.parse()
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncQaip) -> None:
        async with async_client.tag_management.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_management = await response.parse()
            assert_matches_type(Tag, tag_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncQaip) -> None:
        tag_management = await async_client.tag_management.update(
            id="id",
        )
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncQaip) -> None:
        tag_management = await async_client.tag_management.update(
            id="id",
            description="description",
            name="name",
        )
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncQaip) -> None:
        response = await async_client.tag_management.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_management = await response.parse()
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncQaip) -> None:
        async with async_client.tag_management.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_management = await response.parse()
            assert_matches_type(Tag, tag_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tag_management.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncQaip) -> None:
        tag_management = await async_client.tag_management.delete(
            "id",
        )
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncQaip) -> None:
        response = await async_client.tag_management.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_management = await response.parse()
        assert_matches_type(Tag, tag_management, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncQaip) -> None:
        async with async_client.tag_management.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_management = await response.parse()
            assert_matches_type(Tag, tag_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tag_management.with_raw_response.delete(
                "",
            )
