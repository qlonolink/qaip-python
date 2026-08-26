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
            run_id="run_id",
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_run_with_all_params(self, client: Qaip) -> None:
        agent = client.agent.cancel_run(
            run_id="run_id",
            principal_id="principal_id",
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_run(self, client: Qaip) -> None:
        response = client.agent.with_raw_response.cancel_run(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_run(self, client: Qaip) -> None:
        with client.agent.with_streaming_response.cancel_run(
            run_id="run_id",
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
                run_id="",
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
                "agent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "context": [{"foo": "bar"}],
                "forwarded_props": {"foo": "bar"},
                "input_history_mode": "legacy_full",
                "messages": [{"foo": "bar"}],
                "parent_run_id": "x",
                "redaction_policy_id": "pii-standard",
                "resume": [{"foo": "bar"}],
                "state": {"foo": "bar"},
                "thread_id": "x",
                "tools": [{"foo": "bar"}],
            },
            idempotency_key="x",
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
            after=-1,
            limit=1,
            principal_id="principal_id",
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
            run_id="run_id",
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_run_with_all_params(self, client: Qaip) -> None:
        agent = client.agent.retrieve_run(
            run_id="run_id",
            principal_id="principal_id",
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_run(self, client: Qaip) -> None:
        response = client.agent.with_raw_response.retrieve_run(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_run(self, client: Qaip) -> None:
        with client.agent.with_streaming_response.retrieve_run(
            run_id="run_id",
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
                run_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_run_result(self, client: Qaip) -> None:
        agent = client.agent.retrieve_run_result(
            run_id="run_id",
        )
        assert_matches_type(AgentRetrieveRunResultResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_run_result_with_all_params(self, client: Qaip) -> None:
        agent = client.agent.retrieve_run_result(
            run_id="run_id",
            principal_id="principal_id",
        )
        assert_matches_type(AgentRetrieveRunResultResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_run_result(self, client: Qaip) -> None:
        response = client.agent.with_raw_response.retrieve_run_result(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRetrieveRunResultResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_run_result(self, client: Qaip) -> None:
        with client.agent.with_streaming_response.retrieve_run_result(
            run_id="run_id",
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
                run_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_run_events(self, client: Qaip) -> None:
        agent_stream = client.agent.stream_run_events(
            run_id="run_id",
        )
        agent_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_run_events_with_all_params(self, client: Qaip) -> None:
        agent_stream = client.agent.stream_run_events(
            run_id="run_id",
            after=-1,
            principal_id="principal_id",
            last_event_id="1690260571",
        )
        agent_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_run_events(self, client: Qaip) -> None:
        response = client.agent.with_raw_response.stream_run_events(
            run_id="run_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_run_events(self, client: Qaip) -> None:
        with client.agent.with_streaming_response.stream_run_events(
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stream_run_events(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.agent.with_raw_response.stream_run_events(
                run_id="",
            )


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_run(self, async_client: AsyncQaip) -> None:
        agent = await async_client.agent.cancel_run(
            run_id="run_id",
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_run_with_all_params(self, async_client: AsyncQaip) -> None:
        agent = await async_client.agent.cancel_run(
            run_id="run_id",
            principal_id="principal_id",
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_run(self, async_client: AsyncQaip) -> None:
        response = await async_client.agent.with_raw_response.cancel_run(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_run(self, async_client: AsyncQaip) -> None:
        async with async_client.agent.with_streaming_response.cancel_run(
            run_id="run_id",
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
                run_id="",
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
                "agent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "context": [{"foo": "bar"}],
                "forwarded_props": {"foo": "bar"},
                "input_history_mode": "legacy_full",
                "messages": [{"foo": "bar"}],
                "parent_run_id": "x",
                "redaction_policy_id": "pii-standard",
                "resume": [{"foo": "bar"}],
                "state": {"foo": "bar"},
                "thread_id": "x",
                "tools": [{"foo": "bar"}],
            },
            idempotency_key="x",
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
            after=-1,
            limit=1,
            principal_id="principal_id",
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
            run_id="run_id",
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_run_with_all_params(self, async_client: AsyncQaip) -> None:
        agent = await async_client.agent.retrieve_run(
            run_id="run_id",
            principal_id="principal_id",
        )
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_run(self, async_client: AsyncQaip) -> None:
        response = await async_client.agent.with_raw_response.retrieve_run(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRun, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_run(self, async_client: AsyncQaip) -> None:
        async with async_client.agent.with_streaming_response.retrieve_run(
            run_id="run_id",
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
                run_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_run_result(self, async_client: AsyncQaip) -> None:
        agent = await async_client.agent.retrieve_run_result(
            run_id="run_id",
        )
        assert_matches_type(AgentRetrieveRunResultResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_run_result_with_all_params(self, async_client: AsyncQaip) -> None:
        agent = await async_client.agent.retrieve_run_result(
            run_id="run_id",
            principal_id="principal_id",
        )
        assert_matches_type(AgentRetrieveRunResultResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_run_result(self, async_client: AsyncQaip) -> None:
        response = await async_client.agent.with_raw_response.retrieve_run_result(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRetrieveRunResultResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_run_result(self, async_client: AsyncQaip) -> None:
        async with async_client.agent.with_streaming_response.retrieve_run_result(
            run_id="run_id",
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
                run_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_run_events(self, async_client: AsyncQaip) -> None:
        agent_stream = await async_client.agent.stream_run_events(
            run_id="run_id",
        )
        await agent_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_run_events_with_all_params(self, async_client: AsyncQaip) -> None:
        agent_stream = await async_client.agent.stream_run_events(
            run_id="run_id",
            after=-1,
            principal_id="principal_id",
            last_event_id="1690260571",
        )
        await agent_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_run_events(self, async_client: AsyncQaip) -> None:
        response = await async_client.agent.with_raw_response.stream_run_events(
            run_id="run_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_run_events(self, async_client: AsyncQaip) -> None:
        async with async_client.agent.with_streaming_response.stream_run_events(
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stream_run_events(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.agent.with_raw_response.stream_run_events(
                run_id="",
            )
