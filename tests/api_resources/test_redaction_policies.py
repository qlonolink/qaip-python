# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from qaip import Qaip, AsyncQaip
from qaip.types import (
    PolicyDetail,
    PolicyVersion,
    PolicyVersions,
    RedactionPolicyListResponse,
    RedactionPolicyValidateResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRedactionPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Qaip) -> None:
        redaction_policy = client.redaction_policies.create(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
        )
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Qaip) -> None:
        redaction_policy = client.redaction_policies.create(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
            description="社内契約情報向け",
        )
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Qaip) -> None:
        response = client.redaction_policies.with_raw_response.create(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = response.parse()
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Qaip) -> None:
        with client.redaction_policies.with_streaming_response.create(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = response.parse()
            assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Qaip) -> None:
        redaction_policy = client.redaction_policies.retrieve(
            "name",
        )
        assert_matches_type(PolicyDetail, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Qaip) -> None:
        response = client.redaction_policies.with_raw_response.retrieve(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = response.parse()
        assert_matches_type(PolicyDetail, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Qaip) -> None:
        with client.redaction_policies.with_streaming_response.retrieve(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = response.parse()
            assert_matches_type(PolicyDetail, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.redaction_policies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Qaip) -> None:
        redaction_policy = client.redaction_policies.list()
        assert_matches_type(RedactionPolicyListResponse, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Qaip) -> None:
        response = client.redaction_policies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = response.parse()
        assert_matches_type(RedactionPolicyListResponse, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Qaip) -> None:
        with client.redaction_policies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = response.parse()
            assert_matches_type(RedactionPolicyListResponse, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_activate_version(self, client: Qaip) -> None:
        redaction_policy = client.redaction_policies.activate_version(
            version="496",
            name="name",
            expected_active_version="496",
        )
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_activate_version(self, client: Qaip) -> None:
        response = client.redaction_policies.with_raw_response.activate_version(
            version="496",
            name="name",
            expected_active_version="496",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = response.parse()
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_activate_version(self, client: Qaip) -> None:
        with client.redaction_policies.with_streaming_response.activate_version(
            version="496",
            name="name",
            expected_active_version="496",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = response.parse()
            assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_activate_version(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.redaction_policies.with_raw_response.activate_version(
                version="496",
                name="",
                expected_active_version="496",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.redaction_policies.with_raw_response.activate_version(
                version="",
                name="name",
                expected_active_version="496",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Qaip) -> None:
        redaction_policy = client.redaction_policies.archive(
            name="name",
            expected_active_version="496",
        )
        assert_matches_type(PolicyDetail, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Qaip) -> None:
        response = client.redaction_policies.with_raw_response.archive(
            name="name",
            expected_active_version="496",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = response.parse()
        assert_matches_type(PolicyDetail, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Qaip) -> None:
        with client.redaction_policies.with_streaming_response.archive(
            name="name",
            expected_active_version="496",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = response.parse()
            assert_matches_type(PolicyDetail, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.redaction_policies.with_raw_response.archive(
                name="",
                expected_active_version="496",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_version(self, client: Qaip) -> None:
        redaction_policy = client.redaction_policies.create_version(
            name="name",
            business_confidential={
                "definition": "x",
                "examples": ["x"],
                "exclude": ["x"],
                "include": [
                    {
                        "mode": "exact",
                        "text": "x",
                    }
                ],
            },
        )
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_version_with_all_params(self, client: Qaip) -> None:
        redaction_policy = client.redaction_policies.create_version(
            name="name",
            business_confidential={
                "definition": "x",
                "examples": ["x"],
                "exclude": ["x"],
                "include": [
                    {
                        "mode": "exact",
                        "text": "x",
                    }
                ],
            },
            description="description",
        )
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_version(self, client: Qaip) -> None:
        response = client.redaction_policies.with_raw_response.create_version(
            name="name",
            business_confidential={
                "definition": "x",
                "examples": ["x"],
                "exclude": ["x"],
                "include": [
                    {
                        "mode": "exact",
                        "text": "x",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = response.parse()
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_version(self, client: Qaip) -> None:
        with client.redaction_policies.with_streaming_response.create_version(
            name="name",
            business_confidential={
                "definition": "x",
                "examples": ["x"],
                "exclude": ["x"],
                "include": [
                    {
                        "mode": "exact",
                        "text": "x",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = response.parse()
            assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_version(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.redaction_policies.with_raw_response.create_version(
                name="",
                business_confidential={
                    "definition": "x",
                    "examples": ["x"],
                    "exclude": ["x"],
                    "include": [
                        {
                            "mode": "exact",
                            "text": "x",
                        }
                    ],
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_version(self, client: Qaip) -> None:
        redaction_policy = client.redaction_policies.delete_version(
            version="496",
            name="name",
        )
        assert redaction_policy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_version(self, client: Qaip) -> None:
        response = client.redaction_policies.with_raw_response.delete_version(
            version="496",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = response.parse()
        assert redaction_policy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_version(self, client: Qaip) -> None:
        with client.redaction_policies.with_streaming_response.delete_version(
            version="496",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = response.parse()
            assert redaction_policy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_version(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.redaction_policies.with_raw_response.delete_version(
                version="496",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.redaction_policies.with_raw_response.delete_version(
                version="",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_versions(self, client: Qaip) -> None:
        redaction_policy = client.redaction_policies.list_versions(
            name="name",
        )
        assert_matches_type(PolicyVersions, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_versions_with_all_params(self, client: Qaip) -> None:
        redaction_policy = client.redaction_policies.list_versions(
            name="name",
            before_version="496",
            limit=1,
        )
        assert_matches_type(PolicyVersions, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_versions(self, client: Qaip) -> None:
        response = client.redaction_policies.with_raw_response.list_versions(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = response.parse()
        assert_matches_type(PolicyVersions, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_versions(self, client: Qaip) -> None:
        with client.redaction_policies.with_streaming_response.list_versions(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = response.parse()
            assert_matches_type(PolicyVersions, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_versions(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.redaction_policies.with_raw_response.list_versions(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_version(self, client: Qaip) -> None:
        redaction_policy = client.redaction_policies.retrieve_version(
            version="496",
            name="name",
        )
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_version(self, client: Qaip) -> None:
        response = client.redaction_policies.with_raw_response.retrieve_version(
            version="496",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = response.parse()
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_version(self, client: Qaip) -> None:
        with client.redaction_policies.with_streaming_response.retrieve_version(
            version="496",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = response.parse()
            assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_version(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.redaction_policies.with_raw_response.retrieve_version(
                version="496",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.redaction_policies.with_raw_response.retrieve_version(
                version="",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate(self, client: Qaip) -> None:
        redaction_policy = client.redaction_policies.validate(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
        )
        assert_matches_type(RedactionPolicyValidateResponse, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_with_all_params(self, client: Qaip) -> None:
        redaction_policy = client.redaction_policies.validate(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
            description="社内契約情報向け",
        )
        assert_matches_type(RedactionPolicyValidateResponse, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate(self, client: Qaip) -> None:
        response = client.redaction_policies.with_raw_response.validate(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = response.parse()
        assert_matches_type(RedactionPolicyValidateResponse, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate(self, client: Qaip) -> None:
        with client.redaction_policies.with_streaming_response.validate(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = response.parse()
            assert_matches_type(RedactionPolicyValidateResponse, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRedactionPolicies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncQaip) -> None:
        redaction_policy = await async_client.redaction_policies.create(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
        )
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncQaip) -> None:
        redaction_policy = await async_client.redaction_policies.create(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
            description="社内契約情報向け",
        )
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncQaip) -> None:
        response = await async_client.redaction_policies.with_raw_response.create(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = await response.parse()
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncQaip) -> None:
        async with async_client.redaction_policies.with_streaming_response.create(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = await response.parse()
            assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncQaip) -> None:
        redaction_policy = await async_client.redaction_policies.retrieve(
            "name",
        )
        assert_matches_type(PolicyDetail, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncQaip) -> None:
        response = await async_client.redaction_policies.with_raw_response.retrieve(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = await response.parse()
        assert_matches_type(PolicyDetail, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncQaip) -> None:
        async with async_client.redaction_policies.with_streaming_response.retrieve(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = await response.parse()
            assert_matches_type(PolicyDetail, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.redaction_policies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncQaip) -> None:
        redaction_policy = await async_client.redaction_policies.list()
        assert_matches_type(RedactionPolicyListResponse, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncQaip) -> None:
        response = await async_client.redaction_policies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = await response.parse()
        assert_matches_type(RedactionPolicyListResponse, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncQaip) -> None:
        async with async_client.redaction_policies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = await response.parse()
            assert_matches_type(RedactionPolicyListResponse, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_activate_version(self, async_client: AsyncQaip) -> None:
        redaction_policy = await async_client.redaction_policies.activate_version(
            version="496",
            name="name",
            expected_active_version="496",
        )
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_activate_version(self, async_client: AsyncQaip) -> None:
        response = await async_client.redaction_policies.with_raw_response.activate_version(
            version="496",
            name="name",
            expected_active_version="496",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = await response.parse()
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_activate_version(self, async_client: AsyncQaip) -> None:
        async with async_client.redaction_policies.with_streaming_response.activate_version(
            version="496",
            name="name",
            expected_active_version="496",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = await response.parse()
            assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_activate_version(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.redaction_policies.with_raw_response.activate_version(
                version="496",
                name="",
                expected_active_version="496",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.redaction_policies.with_raw_response.activate_version(
                version="",
                name="name",
                expected_active_version="496",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncQaip) -> None:
        redaction_policy = await async_client.redaction_policies.archive(
            name="name",
            expected_active_version="496",
        )
        assert_matches_type(PolicyDetail, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncQaip) -> None:
        response = await async_client.redaction_policies.with_raw_response.archive(
            name="name",
            expected_active_version="496",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = await response.parse()
        assert_matches_type(PolicyDetail, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncQaip) -> None:
        async with async_client.redaction_policies.with_streaming_response.archive(
            name="name",
            expected_active_version="496",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = await response.parse()
            assert_matches_type(PolicyDetail, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.redaction_policies.with_raw_response.archive(
                name="",
                expected_active_version="496",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_version(self, async_client: AsyncQaip) -> None:
        redaction_policy = await async_client.redaction_policies.create_version(
            name="name",
            business_confidential={
                "definition": "x",
                "examples": ["x"],
                "exclude": ["x"],
                "include": [
                    {
                        "mode": "exact",
                        "text": "x",
                    }
                ],
            },
        )
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_version_with_all_params(self, async_client: AsyncQaip) -> None:
        redaction_policy = await async_client.redaction_policies.create_version(
            name="name",
            business_confidential={
                "definition": "x",
                "examples": ["x"],
                "exclude": ["x"],
                "include": [
                    {
                        "mode": "exact",
                        "text": "x",
                    }
                ],
            },
            description="description",
        )
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_version(self, async_client: AsyncQaip) -> None:
        response = await async_client.redaction_policies.with_raw_response.create_version(
            name="name",
            business_confidential={
                "definition": "x",
                "examples": ["x"],
                "exclude": ["x"],
                "include": [
                    {
                        "mode": "exact",
                        "text": "x",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = await response.parse()
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_version(self, async_client: AsyncQaip) -> None:
        async with async_client.redaction_policies.with_streaming_response.create_version(
            name="name",
            business_confidential={
                "definition": "x",
                "examples": ["x"],
                "exclude": ["x"],
                "include": [
                    {
                        "mode": "exact",
                        "text": "x",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = await response.parse()
            assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_version(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.redaction_policies.with_raw_response.create_version(
                name="",
                business_confidential={
                    "definition": "x",
                    "examples": ["x"],
                    "exclude": ["x"],
                    "include": [
                        {
                            "mode": "exact",
                            "text": "x",
                        }
                    ],
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_version(self, async_client: AsyncQaip) -> None:
        redaction_policy = await async_client.redaction_policies.delete_version(
            version="496",
            name="name",
        )
        assert redaction_policy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_version(self, async_client: AsyncQaip) -> None:
        response = await async_client.redaction_policies.with_raw_response.delete_version(
            version="496",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = await response.parse()
        assert redaction_policy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_version(self, async_client: AsyncQaip) -> None:
        async with async_client.redaction_policies.with_streaming_response.delete_version(
            version="496",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = await response.parse()
            assert redaction_policy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_version(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.redaction_policies.with_raw_response.delete_version(
                version="496",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.redaction_policies.with_raw_response.delete_version(
                version="",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_versions(self, async_client: AsyncQaip) -> None:
        redaction_policy = await async_client.redaction_policies.list_versions(
            name="name",
        )
        assert_matches_type(PolicyVersions, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_versions_with_all_params(self, async_client: AsyncQaip) -> None:
        redaction_policy = await async_client.redaction_policies.list_versions(
            name="name",
            before_version="496",
            limit=1,
        )
        assert_matches_type(PolicyVersions, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_versions(self, async_client: AsyncQaip) -> None:
        response = await async_client.redaction_policies.with_raw_response.list_versions(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = await response.parse()
        assert_matches_type(PolicyVersions, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_versions(self, async_client: AsyncQaip) -> None:
        async with async_client.redaction_policies.with_streaming_response.list_versions(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = await response.parse()
            assert_matches_type(PolicyVersions, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_versions(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.redaction_policies.with_raw_response.list_versions(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_version(self, async_client: AsyncQaip) -> None:
        redaction_policy = await async_client.redaction_policies.retrieve_version(
            version="496",
            name="name",
        )
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_version(self, async_client: AsyncQaip) -> None:
        response = await async_client.redaction_policies.with_raw_response.retrieve_version(
            version="496",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = await response.parse()
        assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_version(self, async_client: AsyncQaip) -> None:
        async with async_client.redaction_policies.with_streaming_response.retrieve_version(
            version="496",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = await response.parse()
            assert_matches_type(PolicyVersion, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_version(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.redaction_policies.with_raw_response.retrieve_version(
                version="496",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.redaction_policies.with_raw_response.retrieve_version(
                version="",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate(self, async_client: AsyncQaip) -> None:
        redaction_policy = await async_client.redaction_policies.validate(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
        )
        assert_matches_type(RedactionPolicyValidateResponse, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncQaip) -> None:
        redaction_policy = await async_client.redaction_policies.validate(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
            description="社内契約情報向け",
        )
        assert_matches_type(RedactionPolicyValidateResponse, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncQaip) -> None:
        response = await async_client.redaction_policies.with_raw_response.validate(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redaction_policy = await response.parse()
        assert_matches_type(RedactionPolicyValidateResponse, redaction_policy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncQaip) -> None:
        async with async_client.redaction_policies.with_streaming_response.validate(
            business_confidential={
                "definition": "未公開の契約・価格・計画に関する情報",
                "examples": ["A社との年間契約額は3,200万円"],
                "exclude": ["公開済みの価格表"],
                "include": [
                    {
                        "mode": "value_clause",
                        "text": "契約金額",
                    }
                ],
            },
            name="internal-contracts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redaction_policy = await response.parse()
            assert_matches_type(RedactionPolicyValidateResponse, redaction_policy, path=["response"])

        assert cast(Any, response.is_closed) is True
