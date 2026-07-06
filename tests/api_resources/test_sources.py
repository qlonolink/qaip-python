# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from qaip import Qaip, AsyncQaip
from qaip.types import (
    Source,
    SourceListResponse,
    SourceDeleteMetadataResponse,
)
from tests.utils import assert_matches_type
from qaip._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from qaip.types.shared import Metadata, BatchSetMetadataResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Qaip) -> None:
        source = client.sources.retrieve(
            "source_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Qaip) -> None:
        response = client.sources.with_raw_response.retrieve(
            "source_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Qaip) -> None:
        with client.sources.with_streaming_response.retrieve(
            "source_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            client.sources.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Qaip) -> None:
        source = client.sources.list()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Qaip) -> None:
        source = client.sources.list(
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Qaip) -> None:
        response = client.sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Qaip) -> None:
        with client.sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_set_metadata(self, client: Qaip) -> None:
        source = client.sources.batch_set_metadata(
            items=[
                {
                    "metadata": {},
                    "source_group_id": "source_group_id",
                    "source_id": "source_id",
                }
            ],
        )
        assert_matches_type(BatchSetMetadataResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch_set_metadata(self, client: Qaip) -> None:
        response = client.sources.with_raw_response.batch_set_metadata(
            items=[
                {
                    "metadata": {},
                    "source_group_id": "source_group_id",
                    "source_id": "source_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(BatchSetMetadataResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch_set_metadata(self, client: Qaip) -> None:
        with client.sources.with_streaming_response.batch_set_metadata(
            items=[
                {
                    "metadata": {},
                    "source_group_id": "source_group_id",
                    "source_id": "source_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(BatchSetMetadataResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_metadata(self, client: Qaip) -> None:
        source = client.sources.delete_metadata(
            "source_id",
        )
        assert_matches_type(SourceDeleteMetadataResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_metadata(self, client: Qaip) -> None:
        response = client.sources.with_raw_response.delete_metadata(
            "source_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceDeleteMetadataResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_metadata(self, client: Qaip) -> None:
        with client.sources.with_streaming_response.delete_metadata(
            "source_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceDeleteMetadataResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_metadata(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            client.sources.with_raw_response.delete_metadata(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_raw(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.get("/sources/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/raw").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        source = client.sources.download_raw(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert source.is_closed
        assert source.json() == {"foo": "bar"}
        assert cast(Any, source.is_closed) is True
        assert isinstance(source, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download_raw(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.get("/sources/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/raw").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        source = client.sources.with_raw_response.download_raw(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert source.is_closed is True
        assert source.http_request.headers.get("X-Stainless-Lang") == "python"
        assert source.json() == {"foo": "bar"}
        assert isinstance(source, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download_raw(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.get("/sources/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/raw").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.sources.with_streaming_response.download_raw(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as source:
            assert not source.is_closed
            assert source.http_request.headers.get("X-Stainless-Lang") == "python"

            assert source.json() == {"foo": "bar"}
            assert cast(Any, source.is_closed) is True
            assert isinstance(source, StreamedBinaryAPIResponse)

        assert cast(Any, source.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download_raw(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            client.sources.with_raw_response.download_raw(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_metadata(self, client: Qaip) -> None:
        source = client.sources.retrieve_metadata(
            "source_id",
        )
        assert_matches_type(Metadata, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_metadata(self, client: Qaip) -> None:
        response = client.sources.with_raw_response.retrieve_metadata(
            "source_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(Metadata, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_metadata(self, client: Qaip) -> None:
        with client.sources.with_streaming_response.retrieve_metadata(
            "source_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(Metadata, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_metadata(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            client.sources.with_raw_response.retrieve_metadata(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_metadata(self, client: Qaip) -> None:
        source = client.sources.update_metadata(
            source_id="source_id",
            metadata={},
        )
        assert_matches_type(Metadata, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_metadata_with_all_params(self, client: Qaip) -> None:
        source = client.sources.update_metadata(
            source_id="source_id",
            metadata={
                "records": [
                    {
                        "key": "key",
                        "val": {},
                        "type": "string",
                    }
                ]
            },
        )
        assert_matches_type(Metadata, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_metadata(self, client: Qaip) -> None:
        response = client.sources.with_raw_response.update_metadata(
            source_id="source_id",
            metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(Metadata, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_metadata(self, client: Qaip) -> None:
        with client.sources.with_streaming_response.update_metadata(
            source_id="source_id",
            metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(Metadata, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_metadata(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            client.sources.with_raw_response.update_metadata(
                source_id="",
                metadata={},
            )


class TestAsyncSources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncQaip) -> None:
        source = await async_client.sources.retrieve(
            "source_id",
        )
        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncQaip) -> None:
        response = await async_client.sources.with_raw_response.retrieve(
            "source_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(Source, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncQaip) -> None:
        async with async_client.sources.with_streaming_response.retrieve(
            "source_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(Source, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            await async_client.sources.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncQaip) -> None:
        source = await async_client.sources.list()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncQaip) -> None:
        source = await async_client.sources.list(
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncQaip) -> None:
        response = await async_client.sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncQaip) -> None:
        async with async_client.sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_set_metadata(self, async_client: AsyncQaip) -> None:
        source = await async_client.sources.batch_set_metadata(
            items=[
                {
                    "metadata": {},
                    "source_group_id": "source_group_id",
                    "source_id": "source_id",
                }
            ],
        )
        assert_matches_type(BatchSetMetadataResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch_set_metadata(self, async_client: AsyncQaip) -> None:
        response = await async_client.sources.with_raw_response.batch_set_metadata(
            items=[
                {
                    "metadata": {},
                    "source_group_id": "source_group_id",
                    "source_id": "source_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(BatchSetMetadataResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch_set_metadata(self, async_client: AsyncQaip) -> None:
        async with async_client.sources.with_streaming_response.batch_set_metadata(
            items=[
                {
                    "metadata": {},
                    "source_group_id": "source_group_id",
                    "source_id": "source_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(BatchSetMetadataResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_metadata(self, async_client: AsyncQaip) -> None:
        source = await async_client.sources.delete_metadata(
            "source_id",
        )
        assert_matches_type(SourceDeleteMetadataResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_metadata(self, async_client: AsyncQaip) -> None:
        response = await async_client.sources.with_raw_response.delete_metadata(
            "source_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceDeleteMetadataResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_metadata(self, async_client: AsyncQaip) -> None:
        async with async_client.sources.with_streaming_response.delete_metadata(
            "source_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceDeleteMetadataResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_metadata(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            await async_client.sources.with_raw_response.delete_metadata(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_raw(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        respx_mock.get("/sources/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/raw").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        source = await async_client.sources.download_raw(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert source.is_closed
        assert await source.json() == {"foo": "bar"}
        assert cast(Any, source.is_closed) is True
        assert isinstance(source, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download_raw(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        respx_mock.get("/sources/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/raw").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        source = await async_client.sources.with_raw_response.download_raw(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert source.is_closed is True
        assert source.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await source.json() == {"foo": "bar"}
        assert isinstance(source, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download_raw(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        respx_mock.get("/sources/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/raw").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.sources.with_streaming_response.download_raw(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as source:
            assert not source.is_closed
            assert source.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await source.json() == {"foo": "bar"}
            assert cast(Any, source.is_closed) is True
            assert isinstance(source, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, source.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download_raw(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            await async_client.sources.with_raw_response.download_raw(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_metadata(self, async_client: AsyncQaip) -> None:
        source = await async_client.sources.retrieve_metadata(
            "source_id",
        )
        assert_matches_type(Metadata, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_metadata(self, async_client: AsyncQaip) -> None:
        response = await async_client.sources.with_raw_response.retrieve_metadata(
            "source_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(Metadata, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_metadata(self, async_client: AsyncQaip) -> None:
        async with async_client.sources.with_streaming_response.retrieve_metadata(
            "source_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(Metadata, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_metadata(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            await async_client.sources.with_raw_response.retrieve_metadata(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_metadata(self, async_client: AsyncQaip) -> None:
        source = await async_client.sources.update_metadata(
            source_id="source_id",
            metadata={},
        )
        assert_matches_type(Metadata, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_metadata_with_all_params(self, async_client: AsyncQaip) -> None:
        source = await async_client.sources.update_metadata(
            source_id="source_id",
            metadata={
                "records": [
                    {
                        "key": "key",
                        "val": {},
                        "type": "string",
                    }
                ]
            },
        )
        assert_matches_type(Metadata, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_metadata(self, async_client: AsyncQaip) -> None:
        response = await async_client.sources.with_raw_response.update_metadata(
            source_id="source_id",
            metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(Metadata, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_metadata(self, async_client: AsyncQaip) -> None:
        async with async_client.sources.with_streaming_response.update_metadata(
            source_id="source_id",
            metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(Metadata, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_metadata(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            await async_client.sources.with_raw_response.update_metadata(
                source_id="",
                metadata={},
            )
