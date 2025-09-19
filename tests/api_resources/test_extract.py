# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from qaip import Qaip, AsyncQaip
from qaip.types import ExtractPerformResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtract:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_perform(self, client: Qaip) -> None:
        extract = client.extract.perform(
            schema={},
        )
        assert_matches_type(ExtractPerformResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_perform_with_all_params(self, client: Qaip) -> None:
        extract = client.extract.perform(
            schema={},
            date_from=0,
            date_to=0,
            domains=["string"],
            file_types=["html"],
            limit=1,
            llm_model="llm_model",
            offset=0,
            prompt="prompt",
            source_types=["crawl"],
            tag_ids=["string"],
        )
        assert_matches_type(ExtractPerformResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_perform(self, client: Qaip) -> None:
        response = client.extract.with_raw_response.perform(
            schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractPerformResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_perform(self, client: Qaip) -> None:
        with client.extract.with_streaming_response.perform(
            schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractPerformResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtract:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_perform(self, async_client: AsyncQaip) -> None:
        extract = await async_client.extract.perform(
            schema={},
        )
        assert_matches_type(ExtractPerformResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_perform_with_all_params(self, async_client: AsyncQaip) -> None:
        extract = await async_client.extract.perform(
            schema={},
            date_from=0,
            date_to=0,
            domains=["string"],
            file_types=["html"],
            limit=1,
            llm_model="llm_model",
            offset=0,
            prompt="prompt",
            source_types=["crawl"],
            tag_ids=["string"],
        )
        assert_matches_type(ExtractPerformResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_perform(self, async_client: AsyncQaip) -> None:
        response = await async_client.extract.with_raw_response.perform(
            schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractPerformResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_perform(self, async_client: AsyncQaip) -> None:
        async with async_client.extract.with_streaming_response.perform(
            schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractPerformResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True
