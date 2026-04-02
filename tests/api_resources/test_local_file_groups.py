# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from qaip import Qaip, AsyncQaip
from qaip.types import (
    LocalFileGroup,
    LocalFileGroupListResponse,
    LocalFileGroupCreateResponse,
    LocalFileGroupDeleteResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocalFileGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Qaip) -> None:
        local_file_group = client.local_file_groups.create(
            files=[b"Example data"],
            last_modified=["string"],
            name="name",
        )
        assert_matches_type(LocalFileGroupCreateResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Qaip) -> None:
        local_file_group = client.local_file_groups.create(
            files=[b"Example data"],
            last_modified=["string"],
            name="name",
            chunk_metadata_keys="chunk_metadata_keys",
        )
        assert_matches_type(LocalFileGroupCreateResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Qaip) -> None:
        response = client.local_file_groups.with_raw_response.create(
            files=[b"Example data"],
            last_modified=["string"],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        local_file_group = response.parse()
        assert_matches_type(LocalFileGroupCreateResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Qaip) -> None:
        with client.local_file_groups.with_streaming_response.create(
            files=[b"Example data"],
            last_modified=["string"],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            local_file_group = response.parse()
            assert_matches_type(LocalFileGroupCreateResponse, local_file_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Qaip) -> None:
        local_file_group = client.local_file_groups.retrieve(
            "id",
        )
        assert_matches_type(LocalFileGroup, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Qaip) -> None:
        response = client.local_file_groups.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        local_file_group = response.parse()
        assert_matches_type(LocalFileGroup, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Qaip) -> None:
        with client.local_file_groups.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            local_file_group = response.parse()
            assert_matches_type(LocalFileGroup, local_file_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.local_file_groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Qaip) -> None:
        local_file_group = client.local_file_groups.list()
        assert_matches_type(LocalFileGroupListResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Qaip) -> None:
        local_file_group = client.local_file_groups.list(
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
        )
        assert_matches_type(LocalFileGroupListResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Qaip) -> None:
        response = client.local_file_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        local_file_group = response.parse()
        assert_matches_type(LocalFileGroupListResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Qaip) -> None:
        with client.local_file_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            local_file_group = response.parse()
            assert_matches_type(LocalFileGroupListResponse, local_file_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Qaip) -> None:
        local_file_group = client.local_file_groups.delete(
            "id",
        )
        assert_matches_type(LocalFileGroupDeleteResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Qaip) -> None:
        response = client.local_file_groups.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        local_file_group = response.parse()
        assert_matches_type(LocalFileGroupDeleteResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Qaip) -> None:
        with client.local_file_groups.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            local_file_group = response.parse()
            assert_matches_type(LocalFileGroupDeleteResponse, local_file_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.local_file_groups.with_raw_response.delete(
                "",
            )


class TestAsyncLocalFileGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncQaip) -> None:
        local_file_group = await async_client.local_file_groups.create(
            files=[b"Example data"],
            last_modified=["string"],
            name="name",
        )
        assert_matches_type(LocalFileGroupCreateResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncQaip) -> None:
        local_file_group = await async_client.local_file_groups.create(
            files=[b"Example data"],
            last_modified=["string"],
            name="name",
            chunk_metadata_keys="chunk_metadata_keys",
        )
        assert_matches_type(LocalFileGroupCreateResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncQaip) -> None:
        response = await async_client.local_file_groups.with_raw_response.create(
            files=[b"Example data"],
            last_modified=["string"],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        local_file_group = await response.parse()
        assert_matches_type(LocalFileGroupCreateResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncQaip) -> None:
        async with async_client.local_file_groups.with_streaming_response.create(
            files=[b"Example data"],
            last_modified=["string"],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            local_file_group = await response.parse()
            assert_matches_type(LocalFileGroupCreateResponse, local_file_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncQaip) -> None:
        local_file_group = await async_client.local_file_groups.retrieve(
            "id",
        )
        assert_matches_type(LocalFileGroup, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncQaip) -> None:
        response = await async_client.local_file_groups.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        local_file_group = await response.parse()
        assert_matches_type(LocalFileGroup, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncQaip) -> None:
        async with async_client.local_file_groups.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            local_file_group = await response.parse()
            assert_matches_type(LocalFileGroup, local_file_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.local_file_groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncQaip) -> None:
        local_file_group = await async_client.local_file_groups.list()
        assert_matches_type(LocalFileGroupListResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncQaip) -> None:
        local_file_group = await async_client.local_file_groups.list(
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
        )
        assert_matches_type(LocalFileGroupListResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncQaip) -> None:
        response = await async_client.local_file_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        local_file_group = await response.parse()
        assert_matches_type(LocalFileGroupListResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncQaip) -> None:
        async with async_client.local_file_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            local_file_group = await response.parse()
            assert_matches_type(LocalFileGroupListResponse, local_file_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncQaip) -> None:
        local_file_group = await async_client.local_file_groups.delete(
            "id",
        )
        assert_matches_type(LocalFileGroupDeleteResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncQaip) -> None:
        response = await async_client.local_file_groups.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        local_file_group = await response.parse()
        assert_matches_type(LocalFileGroupDeleteResponse, local_file_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncQaip) -> None:
        async with async_client.local_file_groups.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            local_file_group = await response.parse()
            assert_matches_type(LocalFileGroupDeleteResponse, local_file_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.local_file_groups.with_raw_response.delete(
                "",
            )
