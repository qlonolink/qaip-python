# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from qaip import Qaip, AsyncQaip
from qaip.types import (
    Crawl,
    CrawlSetting,
    CrawlListResponse,
)
from tests.utils import assert_matches_type
from qaip._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

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
            no_canonical_check=True,
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
            no_canonical_check=True,
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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_raw_archive(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.post("/crawls/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/raw-archive").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        crawl = client.crawls.download_raw_archive(
            crawl_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert crawl.is_closed
        assert crawl.json() == {"foo": "bar"}
        assert cast(Any, crawl.is_closed) is True
        assert isinstance(crawl, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_raw_archive_with_all_params(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.post("/crawls/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/raw-archive").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        crawl = client.crawls.download_raw_archive(
            crawl_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert crawl.is_closed
        assert crawl.json() == {"foo": "bar"}
        assert cast(Any, crawl.is_closed) is True
        assert isinstance(crawl, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download_raw_archive(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.post("/crawls/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/raw-archive").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        crawl = client.crawls.with_raw_response.download_raw_archive(
            crawl_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert crawl.is_closed is True
        assert crawl.http_request.headers.get("X-Stainless-Lang") == "python"
        assert crawl.json() == {"foo": "bar"}
        assert isinstance(crawl, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download_raw_archive(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.post("/crawls/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/raw-archive").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.crawls.with_streaming_response.download_raw_archive(
            crawl_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as crawl:
            assert not crawl.is_closed
            assert crawl.http_request.headers.get("X-Stainless-Lang") == "python"

            assert crawl.json() == {"foo": "bar"}
            assert cast(Any, crawl.is_closed) is True
            assert isinstance(crawl, StreamedBinaryAPIResponse)

        assert cast(Any, crawl.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download_raw_archive(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `crawl_id` but received ''"):
            client.crawls.with_raw_response.download_raw_archive(
                crawl_id="",
            )

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
            no_canonical_check=True,
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
            no_canonical_check=True,
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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_raw_archive(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        respx_mock.post("/crawls/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/raw-archive").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        crawl = await async_client.crawls.download_raw_archive(
            crawl_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert crawl.is_closed
        assert await crawl.json() == {"foo": "bar"}
        assert cast(Any, crawl.is_closed) is True
        assert isinstance(crawl, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_raw_archive_with_all_params(
        self, async_client: AsyncQaip, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/crawls/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/raw-archive").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        crawl = await async_client.crawls.download_raw_archive(
            crawl_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert crawl.is_closed
        assert await crawl.json() == {"foo": "bar"}
        assert cast(Any, crawl.is_closed) is True
        assert isinstance(crawl, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download_raw_archive(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        respx_mock.post("/crawls/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/raw-archive").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        crawl = await async_client.crawls.with_raw_response.download_raw_archive(
            crawl_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert crawl.is_closed is True
        assert crawl.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await crawl.json() == {"foo": "bar"}
        assert isinstance(crawl, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download_raw_archive(
        self, async_client: AsyncQaip, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/crawls/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/raw-archive").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.crawls.with_streaming_response.download_raw_archive(
            crawl_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as crawl:
            assert not crawl.is_closed
            assert crawl.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await crawl.json() == {"foo": "bar"}
            assert cast(Any, crawl.is_closed) is True
            assert isinstance(crawl, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, crawl.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download_raw_archive(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `crawl_id` but received ''"):
            await async_client.crawls.with_raw_response.download_raw_archive(
                crawl_id="",
            )

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
