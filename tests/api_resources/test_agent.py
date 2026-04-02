# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from qaip import Qaip, AsyncQaip
from qaip.types import (
    AgentRun,
    AgentListRunEventsResponse,
    AgentRetrieveRunResultResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_run(self, client: Qaip) -> None:
        agent = client.agent.cancel_run(
            "run_id",
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_run(self, client: Qaip) -> None:
        response = client.agent.with_raw_response.cancel_run(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_run(self, client: Qaip) -> None:
        with client.agent.with_streaming_response.cancel_run(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRun, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel_run(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.with_raw_response.cancel_run(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_run(self, client: Qaip) -> None:
        agent = client.agent.create_run(
            input={},
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_run_with_all_params(self, client: Qaip) -> None:
        agent = client.agent.create_run(
            input={
                "forwarded_props": {
                    "filters": {
                        "chunk_metadata": {
                            "filters": [
                                {
                                    "key": "key",
                                    "operator": "eq",
                                    "type": "string",
                                    "max": {},
                                    "min": {},
                                    "val": {},
                                }
                            ],
                            "groups": [],
                            "logic": "AND",
                        },
                        "citation": True,
                        "date_from": 1735639200,
                        "date_to": 1735639200,
                        "domains": ["string"],
                        "file_types": ["html"],
                        "metadata": {
                            "filters": [
                                {
                                    "key": "key",
                                    "operator": "eq",
                                    "type": "string",
                                    "max": {},
                                    "min": {},
                                    "val": {},
                                }
                            ],
                            "groups": [],
                            "logic": "AND",
                        },
                        "source_metadata": {
                            "filters": [
                                {
                                    "key": "key",
                                    "operator": "eq",
                                    "type": "string",
                                    "max": {},
                                    "min": {},
                                    "val": {},
                                }
                            ],
                            "groups": [],
                            "logic": "AND",
                        },
                        "source_types": ["crawl"],
                        "tag_filter_logic": "AND",
                        "tag_ids": ["string"],
                        "tags": ["string"],
                    }
                },
                "messages": [
                    {
                        "content": "string",
                        "role": "system",
                    }
                ],
                "run_id": "run_id",
                "thread_id": "thread_id",
            },
            idempotency_key="idempotency_key",
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_run(self, client: Qaip) -> None:
        response = client.agent.with_raw_response.create_run(
            input={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_run(self, client: Qaip) -> None:
        with client.agent.with_streaming_response.create_run(
            input={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRun, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_run_events(self, client: Qaip) -> None:
        agent = client.agent.list_run_events(
            run_id="run_id",
        )
        assert_matches_type(AgentListRunEventsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_run_events_with_all_params(self, client: Qaip) -> None:
        agent = client.agent.list_run_events(
            run_id="run_id",
            after=0,
            limit=1,
        )
        assert_matches_type(AgentListRunEventsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_run_events(self, client: Qaip) -> None:
        response = client.agent.with_raw_response.list_run_events(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListRunEventsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_run_events(self, client: Qaip) -> None:
        with client.agent.with_streaming_response.list_run_events(
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListRunEventsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_run_events(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.with_raw_response.list_run_events(
                run_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_run(self, client: Qaip) -> None:
        agent = client.agent.retrieve_run(
            "run_id",
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_run(self, client: Qaip) -> None:
        response = client.agent.with_raw_response.retrieve_run(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_run(self, client: Qaip) -> None:
        with client.agent.with_streaming_response.retrieve_run(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRun, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_run(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.with_raw_response.retrieve_run(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_run_result(self, client: Qaip) -> None:
        agent = client.agent.retrieve_run_result(
            "run_id",
        )
        assert_matches_type(AgentRetrieveRunResultResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_run_result(self, client: Qaip) -> None:
        response = client.agent.with_raw_response.retrieve_run_result(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRetrieveRunResultResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_run_result(self, client: Qaip) -> None:
        with client.agent.with_streaming_response.retrieve_run_result(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRetrieveRunResultResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_run_result(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.with_raw_response.retrieve_run_result(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Qaip) -> None:
        agent_stream = client.agent.run()
        agent_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Qaip) -> None:
        agent_stream = client.agent.run(
            forwarded_props={
                "filters": {
                    "chunk_metadata": {
                        "filters": [
                            {
                                "key": "key",
                                "operator": "eq",
                                "type": "string",
                                "max": {},
                                "min": {},
                                "val": {},
                            }
                        ],
                        "groups": [],
                        "logic": "AND",
                    },
                    "citation": True,
                    "date_from": 1735639200,
                    "date_to": 1735639200,
                    "domains": ["string"],
                    "file_types": ["html"],
                    "metadata": {
                        "filters": [
                            {
                                "key": "key",
                                "operator": "eq",
                                "type": "string",
                                "max": {},
                                "min": {},
                                "val": {},
                            }
                        ],
                        "groups": [],
                        "logic": "AND",
                    },
                    "source_metadata": {
                        "filters": [
                            {
                                "key": "key",
                                "operator": "eq",
                                "type": "string",
                                "max": {},
                                "min": {},
                                "val": {},
                            }
                        ],
                        "groups": [],
                        "logic": "AND",
                    },
                    "source_types": ["crawl"],
                    "tag_filter_logic": "AND",
                    "tag_ids": ["string"],
                    "tags": ["string"],
                }
            },
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            run_id="run_id",
            thread_id="thread_id",
        )
        agent_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Qaip) -> None:
        response = client.agent.with_raw_response.run()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Qaip) -> None:
        with client.agent.with_streaming_response.run() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_run(self, async_client: AsyncQaip) -> None:
        agent = await async_client.agent.cancel_run(
            "run_id",
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_run(self, async_client: AsyncQaip) -> None:
        response = await async_client.agent.with_raw_response.cancel_run(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_run(self, async_client: AsyncQaip) -> None:
        async with async_client.agent.with_streaming_response.cancel_run(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRun, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel_run(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.with_raw_response.cancel_run(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_run(self, async_client: AsyncQaip) -> None:
        agent = await async_client.agent.create_run(
            input={},
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_run_with_all_params(self, async_client: AsyncQaip) -> None:
        agent = await async_client.agent.create_run(
            input={
                "forwarded_props": {
                    "filters": {
                        "chunk_metadata": {
                            "filters": [
                                {
                                    "key": "key",
                                    "operator": "eq",
                                    "type": "string",
                                    "max": {},
                                    "min": {},
                                    "val": {},
                                }
                            ],
                            "groups": [],
                            "logic": "AND",
                        },
                        "citation": True,
                        "date_from": 1735639200,
                        "date_to": 1735639200,
                        "domains": ["string"],
                        "file_types": ["html"],
                        "metadata": {
                            "filters": [
                                {
                                    "key": "key",
                                    "operator": "eq",
                                    "type": "string",
                                    "max": {},
                                    "min": {},
                                    "val": {},
                                }
                            ],
                            "groups": [],
                            "logic": "AND",
                        },
                        "source_metadata": {
                            "filters": [
                                {
                                    "key": "key",
                                    "operator": "eq",
                                    "type": "string",
                                    "max": {},
                                    "min": {},
                                    "val": {},
                                }
                            ],
                            "groups": [],
                            "logic": "AND",
                        },
                        "source_types": ["crawl"],
                        "tag_filter_logic": "AND",
                        "tag_ids": ["string"],
                        "tags": ["string"],
                    }
                },
                "messages": [
                    {
                        "content": "string",
                        "role": "system",
                    }
                ],
                "run_id": "run_id",
                "thread_id": "thread_id",
            },
            idempotency_key="idempotency_key",
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_run(self, async_client: AsyncQaip) -> None:
        response = await async_client.agent.with_raw_response.create_run(
            input={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_run(self, async_client: AsyncQaip) -> None:
        async with async_client.agent.with_streaming_response.create_run(
            input={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRun, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_run_events(self, async_client: AsyncQaip) -> None:
        agent = await async_client.agent.list_run_events(
            run_id="run_id",
        )
        assert_matches_type(AgentListRunEventsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_run_events_with_all_params(self, async_client: AsyncQaip) -> None:
        agent = await async_client.agent.list_run_events(
            run_id="run_id",
            after=0,
            limit=1,
        )
        assert_matches_type(AgentListRunEventsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_run_events(self, async_client: AsyncQaip) -> None:
        response = await async_client.agent.with_raw_response.list_run_events(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListRunEventsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_run_events(self, async_client: AsyncQaip) -> None:
        async with async_client.agent.with_streaming_response.list_run_events(
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListRunEventsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_run_events(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.with_raw_response.list_run_events(
                run_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_run(self, async_client: AsyncQaip) -> None:
        agent = await async_client.agent.retrieve_run(
            "run_id",
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_run(self, async_client: AsyncQaip) -> None:
        response = await async_client.agent.with_raw_response.retrieve_run(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_run(self, async_client: AsyncQaip) -> None:
        async with async_client.agent.with_streaming_response.retrieve_run(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRun, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_run(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.with_raw_response.retrieve_run(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_run_result(self, async_client: AsyncQaip) -> None:
        agent = await async_client.agent.retrieve_run_result(
            "run_id",
        )
        assert_matches_type(AgentRetrieveRunResultResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_run_result(self, async_client: AsyncQaip) -> None:
        response = await async_client.agent.with_raw_response.retrieve_run_result(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRetrieveRunResultResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_run_result(self, async_client: AsyncQaip) -> None:
        async with async_client.agent.with_streaming_response.retrieve_run_result(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRetrieveRunResultResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_run_result(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.with_raw_response.retrieve_run_result(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncQaip) -> None:
        agent_stream = await async_client.agent.run()
        await agent_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncQaip) -> None:
        agent_stream = await async_client.agent.run(
            forwarded_props={
                "filters": {
                    "chunk_metadata": {
                        "filters": [
                            {
                                "key": "key",
                                "operator": "eq",
                                "type": "string",
                                "max": {},
                                "min": {},
                                "val": {},
                            }
                        ],
                        "groups": [],
                        "logic": "AND",
                    },
                    "citation": True,
                    "date_from": 1735639200,
                    "date_to": 1735639200,
                    "domains": ["string"],
                    "file_types": ["html"],
                    "metadata": {
                        "filters": [
                            {
                                "key": "key",
                                "operator": "eq",
                                "type": "string",
                                "max": {},
                                "min": {},
                                "val": {},
                            }
                        ],
                        "groups": [],
                        "logic": "AND",
                    },
                    "source_metadata": {
                        "filters": [
                            {
                                "key": "key",
                                "operator": "eq",
                                "type": "string",
                                "max": {},
                                "min": {},
                                "val": {},
                            }
                        ],
                        "groups": [],
                        "logic": "AND",
                    },
                    "source_types": ["crawl"],
                    "tag_filter_logic": "AND",
                    "tag_ids": ["string"],
                    "tags": ["string"],
                }
            },
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            run_id="run_id",
            thread_id="thread_id",
        )
        await agent_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncQaip) -> None:
        response = await async_client.agent.with_raw_response.run()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncQaip) -> None:
        async with async_client.agent.with_streaming_response.run() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
