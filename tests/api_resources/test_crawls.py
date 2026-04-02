# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from qaip import Qaip, AsyncQaip
from qaip.types import (
    Crawl,
    CrawlSetting,
    CrawlListResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCrawls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Qaip) -> None:
        crawl = client.crawls.create(
            max_depth=1,
            max_num_files=1,
            name="name",
            start_url="start_url",
        )
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Qaip) -> None:
        crawl = client.crawls.create(
            max_depth=1,
            max_num_files=1,
            name="name",
            start_url="start_url",
            content_pattern=["string"],
            file_extensions=["string"],
            html_only=True,
            metadata={
                "records": [
                    {
                        "key": "key",
                        "val": {},
                        "type": "string",
                    }
                ]
            },
            path_filters=["string"],
            rrule="rrule",
            use_browser=True,
        )
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Qaip) -> None:
        response = client.crawls.with_raw_response.create(
            max_depth=1,
            max_num_files=1,
            name="name",
            start_url="start_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Qaip) -> None:
        with client.crawls.with_streaming_response.create(
            max_depth=1,
            max_num_files=1,
            name="name",
            start_url="start_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(Crawl, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Qaip) -> None:
        crawl = client.crawls.retrieve(
            "id",
        )
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Qaip) -> None:
        response = client.crawls.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Qaip) -> None:
        with client.crawls.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(Crawl, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.crawls.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Qaip) -> None:
        crawl = client.crawls.list()
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Qaip) -> None:
        crawl = client.crawls.list(
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
        )
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Qaip) -> None:
        response = client.crawls.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Qaip) -> None:
        with client.crawls.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(CrawlListResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Qaip) -> None:
        crawl = client.crawls.delete(
            "id",
        )
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Qaip) -> None:
        response = client.crawls.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Qaip) -> None:
        with client.crawls.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(Crawl, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.crawls.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_url_list(self, client: Qaip) -> None:
        crawl = client.crawls.create_url_list(
            name="x",
            target_urls=["string"],
        )
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_url_list_with_all_params(self, client: Qaip) -> None:
        crawl = client.crawls.create_url_list(
            name="x",
            target_urls=["string"],
            max_num_files=0,
            metadata={
                "records": [
                    {
                        "key": "key",
                        "val": {},
                        "type": "string",
                    }
                ]
            },
            rrule="rrule",
        )
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_url_list(self, client: Qaip) -> None:
        response = client.crawls.with_raw_response.create_url_list(
            name="x",
            target_urls=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_url_list(self, client: Qaip) -> None:
        with client.crawls.with_streaming_response.create_url_list(
            name="x",
            target_urls=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(Crawl, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_setting(self, client: Qaip) -> None:
        crawl = client.crawls.retrieve_setting(
            "id",
        )
        assert_matches_type(CrawlSetting, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_setting(self, client: Qaip) -> None:
        response = client.crawls.with_raw_response.retrieve_setting(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(CrawlSetting, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_setting(self, client: Qaip) -> None:
        with client.crawls.with_streaming_response.retrieve_setting(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(CrawlSetting, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_setting(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.crawls.with_raw_response.retrieve_setting(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_setting(self, client: Qaip) -> None:
        crawl = client.crawls.update_setting(
            id="id",
            name="name",
        )
        assert_matches_type(CrawlSetting, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_setting_with_all_params(self, client: Qaip) -> None:
        crawl = client.crawls.update_setting(
            id="id",
            name="name",
            rrule="rrule",
        )
        assert_matches_type(CrawlSetting, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_setting(self, client: Qaip) -> None:
        response = client.crawls.with_raw_response.update_setting(
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = response.parse()
        assert_matches_type(CrawlSetting, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_setting(self, client: Qaip) -> None:
        with client.crawls.with_streaming_response.update_setting(
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = response.parse()
            assert_matches_type(CrawlSetting, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_setting(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.crawls.with_raw_response.update_setting(
                id="",
                name="name",
            )


class TestAsyncCrawls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncQaip) -> None:
        crawl = await async_client.crawls.create(
            max_depth=1,
            max_num_files=1,
            name="name",
            start_url="start_url",
        )
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncQaip) -> None:
        crawl = await async_client.crawls.create(
            max_depth=1,
            max_num_files=1,
            name="name",
            start_url="start_url",
            content_pattern=["string"],
            file_extensions=["string"],
            html_only=True,
            metadata={
                "records": [
                    {
                        "key": "key",
                        "val": {},
                        "type": "string",
                    }
                ]
            },
            path_filters=["string"],
            rrule="rrule",
            use_browser=True,
        )
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncQaip) -> None:
        response = await async_client.crawls.with_raw_response.create(
            max_depth=1,
            max_num_files=1,
            name="name",
            start_url="start_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncQaip) -> None:
        async with async_client.crawls.with_streaming_response.create(
            max_depth=1,
            max_num_files=1,
            name="name",
            start_url="start_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(Crawl, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncQaip) -> None:
        crawl = await async_client.crawls.retrieve(
            "id",
        )
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncQaip) -> None:
        response = await async_client.crawls.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncQaip) -> None:
        async with async_client.crawls.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(Crawl, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.crawls.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncQaip) -> None:
        crawl = await async_client.crawls.list()
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncQaip) -> None:
        crawl = await async_client.crawls.list(
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
        )
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncQaip) -> None:
        response = await async_client.crawls.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(CrawlListResponse, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncQaip) -> None:
        async with async_client.crawls.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(CrawlListResponse, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncQaip) -> None:
        crawl = await async_client.crawls.delete(
            "id",
        )
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncQaip) -> None:
        response = await async_client.crawls.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncQaip) -> None:
        async with async_client.crawls.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(Crawl, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.crawls.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_url_list(self, async_client: AsyncQaip) -> None:
        crawl = await async_client.crawls.create_url_list(
            name="x",
            target_urls=["string"],
        )
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_url_list_with_all_params(self, async_client: AsyncQaip) -> None:
        crawl = await async_client.crawls.create_url_list(
            name="x",
            target_urls=["string"],
            max_num_files=0,
            metadata={
                "records": [
                    {
                        "key": "key",
                        "val": {},
                        "type": "string",
                    }
                ]
            },
            rrule="rrule",
        )
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_url_list(self, async_client: AsyncQaip) -> None:
        response = await async_client.crawls.with_raw_response.create_url_list(
            name="x",
            target_urls=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(Crawl, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_url_list(self, async_client: AsyncQaip) -> None:
        async with async_client.crawls.with_streaming_response.create_url_list(
            name="x",
            target_urls=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(Crawl, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_setting(self, async_client: AsyncQaip) -> None:
        crawl = await async_client.crawls.retrieve_setting(
            "id",
        )
        assert_matches_type(CrawlSetting, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_setting(self, async_client: AsyncQaip) -> None:
        response = await async_client.crawls.with_raw_response.retrieve_setting(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(CrawlSetting, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_setting(self, async_client: AsyncQaip) -> None:
        async with async_client.crawls.with_streaming_response.retrieve_setting(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(CrawlSetting, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_setting(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.crawls.with_raw_response.retrieve_setting(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_setting(self, async_client: AsyncQaip) -> None:
        crawl = await async_client.crawls.update_setting(
            id="id",
            name="name",
        )
        assert_matches_type(CrawlSetting, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_setting_with_all_params(self, async_client: AsyncQaip) -> None:
        crawl = await async_client.crawls.update_setting(
            id="id",
            name="name",
            rrule="rrule",
        )
        assert_matches_type(CrawlSetting, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_setting(self, async_client: AsyncQaip) -> None:
        response = await async_client.crawls.with_raw_response.update_setting(
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crawl = await response.parse()
        assert_matches_type(CrawlSetting, crawl, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_setting(self, async_client: AsyncQaip) -> None:
        async with async_client.crawls.with_streaming_response.update_setting(
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crawl = await response.parse()
            assert_matches_type(CrawlSetting, crawl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_setting(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.crawls.with_raw_response.update_setting(
                id="",
                name="name",
            )
