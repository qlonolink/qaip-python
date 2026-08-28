from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from qaip import Qaip, AsyncQaip
from qaip._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

_CRAWL_ID = "11111111-1111-1111-1111-111111111111"
_SOURCE_ID = "22222222-2222-2222-2222-222222222222"


class TestCrawlRawAPI:
    @pytest.mark.respx(base_url=base_url)
    def test_list_crawl_sources_with_cursor(self, client: Qaip, respx_mock: MockRouter) -> None:
        route = respx_mock.get(f"/source-groups/{_CRAWL_ID}/sources").mock(
            return_value=httpx.Response(
                200,
                json={
                    "sources": [],
                    "pagination": {"has_more": False, "limit": 100, "next_id": None, "total": 0},
                },
            )
        )

        response = client.source_groups.list_sources(_CRAWL_ID, limit=100, after_id=_SOURCE_ID)

        assert response.sources == []
        assert dict(route.calls.last.request.url.params) == {"limit": "100", "after_id": _SOURCE_ID}

    @pytest.mark.respx(base_url=base_url)
    def test_download_raw_uses_crawl_id(self, client: Qaip, respx_mock: MockRouter) -> None:
        route = respx_mock.get(f"/sources/{_SOURCE_ID}/raw").mock(return_value=httpx.Response(200, content=b"raw"))

        response = client.sources.download_raw(_SOURCE_ID, crawl_id=_CRAWL_ID)

        assert isinstance(response, BinaryAPIResponse)
        assert response.read() == b"raw"
        assert dict(route.calls.last.request.url.params) == {"crawl_id": _CRAWL_ID}

    @pytest.mark.respx(base_url=base_url)
    def test_download_selected_raw_archive(self, client: Qaip, respx_mock: MockRouter) -> None:
        route = respx_mock.post(f"/crawls/{_CRAWL_ID}/raw-archive").mock(
            return_value=httpx.Response(200, content=b"zip", headers={"content-type": "application/zip"})
        )

        response = client.crawls.download_raw_archive(_CRAWL_ID, source_ids=[_SOURCE_ID])

        assert isinstance(response, BinaryAPIResponse)
        assert response.read() == b"zip"
        assert route.calls.last.request.read() == f'{{"source_ids":["{_SOURCE_ID}"]}}'.encode()

    @pytest.mark.respx(base_url=base_url)
    def test_stream_all_raw_archive(self, client: Qaip, respx_mock: MockRouter) -> None:
        route = respx_mock.post(f"/crawls/{_CRAWL_ID}/raw-archive").mock(
            return_value=httpx.Response(200, content=b"zip", headers={"content-type": "application/zip"})
        )

        with client.crawls.with_streaming_response.download_raw_archive(_CRAWL_ID) as response:
            assert isinstance(response, StreamedBinaryAPIResponse)
            assert b"".join(response.iter_bytes()) == b"zip"

        assert cast(Any, response.is_closed) is True
        assert route.calls.last.request.read() in {b"", b"{}"}


class TestAsyncCrawlRawAPI:
    @pytest.mark.respx(base_url=base_url)
    async def test_download_selected_raw_archive(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        route = respx_mock.post(f"/crawls/{_CRAWL_ID}/raw-archive").mock(
            return_value=httpx.Response(200, content=b"zip", headers={"content-type": "application/zip"})
        )

        response = await async_client.crawls.download_raw_archive(_CRAWL_ID, source_ids=[_SOURCE_ID])

        assert isinstance(response, AsyncBinaryAPIResponse)
        assert await response.read() == b"zip"
        assert route.calls.last.request.read() == f'{{"source_ids":["{_SOURCE_ID}"]}}'.encode()

    @pytest.mark.respx(base_url=base_url)
    async def test_stream_raw_archive(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        respx_mock.post(f"/crawls/{_CRAWL_ID}/raw-archive").mock(
            return_value=httpx.Response(200, content=b"zip", headers={"content-type": "application/zip"})
        )

        async with async_client.crawls.with_streaming_response.download_raw_archive(
            _CRAWL_ID, source_ids=[_SOURCE_ID]
        ) as response:
            assert isinstance(response, AsyncStreamedBinaryAPIResponse)
            chunks = [chunk async for chunk in response.iter_bytes()]
            assert b"".join(chunks) == b"zip"

        assert cast(Any, response.is_closed) is True
