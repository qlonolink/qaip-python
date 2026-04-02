# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from qaip import Qaip, AsyncQaip
from tests.utils import assert_matches_type
from qaip.types.shared import TagSourceGroup

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTagSourceGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Qaip) -> None:
        tag_source_group = client.tag_source_groups.create(
            source_group_id="source_group_id",
            tag_id="tag_id",
        )
        assert_matches_type(TagSourceGroup, tag_source_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Qaip) -> None:
        response = client.tag_source_groups.with_raw_response.create(
            source_group_id="source_group_id",
            tag_id="tag_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_source_group = response.parse()
        assert_matches_type(TagSourceGroup, tag_source_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Qaip) -> None:
        with client.tag_source_groups.with_streaming_response.create(
            source_group_id="source_group_id",
            tag_id="tag_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_source_group = response.parse()
            assert_matches_type(TagSourceGroup, tag_source_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Qaip) -> None:
        tag_source_group = client.tag_source_groups.delete(
            source_group_id="source_group_id",
            tag_id="tag_id",
        )
        assert_matches_type(TagSourceGroup, tag_source_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Qaip) -> None:
        response = client.tag_source_groups.with_raw_response.delete(
            source_group_id="source_group_id",
            tag_id="tag_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_source_group = response.parse()
        assert_matches_type(TagSourceGroup, tag_source_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Qaip) -> None:
        with client.tag_source_groups.with_streaming_response.delete(
            source_group_id="source_group_id",
            tag_id="tag_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_source_group = response.parse()
            assert_matches_type(TagSourceGroup, tag_source_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTagSourceGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncQaip) -> None:
        tag_source_group = await async_client.tag_source_groups.create(
            source_group_id="source_group_id",
            tag_id="tag_id",
        )
        assert_matches_type(TagSourceGroup, tag_source_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncQaip) -> None:
        response = await async_client.tag_source_groups.with_raw_response.create(
            source_group_id="source_group_id",
            tag_id="tag_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_source_group = await response.parse()
        assert_matches_type(TagSourceGroup, tag_source_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncQaip) -> None:
        async with async_client.tag_source_groups.with_streaming_response.create(
            source_group_id="source_group_id",
            tag_id="tag_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_source_group = await response.parse()
            assert_matches_type(TagSourceGroup, tag_source_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncQaip) -> None:
        tag_source_group = await async_client.tag_source_groups.delete(
            source_group_id="source_group_id",
            tag_id="tag_id",
        )
        assert_matches_type(TagSourceGroup, tag_source_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncQaip) -> None:
        response = await async_client.tag_source_groups.with_raw_response.delete(
            source_group_id="source_group_id",
            tag_id="tag_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_source_group = await response.parse()
        assert_matches_type(TagSourceGroup, tag_source_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncQaip) -> None:
        async with async_client.tag_source_groups.with_streaming_response.delete(
            source_group_id="source_group_id",
            tag_id="tag_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_source_group = await response.parse()
            assert_matches_type(TagSourceGroup, tag_source_group, path=["response"])

        assert cast(Any, response.is_closed) is True
