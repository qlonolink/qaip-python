# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from qaip import Qaip, AsyncQaip
from qaip.types import SearchQueryResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_query(self, client: Qaip) -> None:
        search = client.search.query(
            query="machine learning and artificial intelligence",
        )
        assert_matches_type(SearchQueryResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_query_with_all_params(self, client: Qaip) -> None:
        search = client.search.query(
            query="machine learning and artificial intelligence",
            date_from=1677649420,
            date_to=1677649420,
            domains=["example.com", "blog.example.com"],
            file_types=["html"],
            limit=10,
            offset=0,
            source_types=["crawl"],
            tag_ids=["string"],
        )
        assert_matches_type(SearchQueryResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: Qaip) -> None:
        response = client.search.with_raw_response.query(
            query="machine learning and artificial intelligence",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchQueryResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: Qaip) -> None:
        with client.search.with_streaming_response.query(
            query="machine learning and artificial intelligence",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchQueryResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncQaip) -> None:
        search = await async_client.search.query(
            query="machine learning and artificial intelligence",
        )
        assert_matches_type(SearchQueryResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncQaip) -> None:
        search = await async_client.search.query(
            query="machine learning and artificial intelligence",
            date_from=1677649420,
            date_to=1677649420,
            domains=["example.com", "blog.example.com"],
            file_types=["html"],
            limit=10,
            offset=0,
            source_types=["crawl"],
            tag_ids=["string"],
        )
        assert_matches_type(SearchQueryResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncQaip) -> None:
        response = await async_client.search.with_raw_response.query(
            query="machine learning and artificial intelligence",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchQueryResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncQaip) -> None:
        async with async_client.search.with_streaming_response.query(
            query="machine learning and artificial intelligence",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchQueryResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True
