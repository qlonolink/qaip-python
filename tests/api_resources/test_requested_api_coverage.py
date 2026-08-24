from __future__ import annotations

import os
from unittest.mock import patch

import httpx
import pytest
from respx import MockRouter

from qaip import Qaip, AsyncQaip, APIStatusError
from qaip.types import (
    Tag,
    Conversation,
    AgentThreadDetail,
    ConversationDetail,
    AgentThreadListResponse,
    ConversationListResponse,
    ExternalTableQueryResponse,
    ExternalTableSchemaResponse,
    ExternalQueryPreparingResponse,
    ExternalQueryStateOnlyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
request_id = "00000000-0000-0000-0000-000000000001"


def _state_response(*, state: str = "RUNNING", terminal: bool = False) -> dict[str, object]:
    return {
        "response_type": "state_only",
        "request_id": request_id,
        "state": state,
        "terminal": terminal,
    }


class TestRequestedAPICoverage:
    @pytest.mark.respx(base_url=base_url)
    def test_external_query_create_does_not_retry(self, respx_mock: MockRouter, client: Qaip) -> None:
        calls = 0

        def handler(request: httpx.Request) -> httpx.Response:
            nonlocal calls
            calls += 1
            if calls == 1:
                return httpx.Response(
                    503,
                    request=request,
                    json={"error": {"type": "outcome_unknown", "message": "unknown"}},
                )
            return httpx.Response(
                200,
                request=request,
                json={"columns": [], "rows": [], "row_count": 0, "truncated": False},
            )

        respx_mock.post("/query").mock(side_effect=handler)
        with patch("qaip._base_client.BaseClient._calculate_retry_timeout", return_value=0):
            with pytest.raises(APIStatusError):
                client.external_queries.create(sql="SELECT 1")
        assert calls == 1

    @pytest.mark.respx(base_url=base_url)
    def test_agent_methods(self, respx_mock: MockRouter, client: Qaip) -> None:
        list_route = respx_mock.get("/agent/threads").mock(
            return_value=httpx.Response(
                200,
                json={
                    "threads": [
                        {
                            "thread_id": "thread-1",
                            "latest_run_id": "run-1",
                            "status": "SUCCEEDED",
                        }
                    ]
                },
            )
        )
        listed = client.agent.list_threads(all_principals=True, limit=20, offset=2, principal_id="principal-1")
        assert isinstance(listed, AgentThreadListResponse)
        assert listed.threads[0].thread_id == "thread-1"
        assert dict(list_route.calls.last.request.url.params) == {
            "all_principals": "true",
            "limit": "20",
            "offset": "2",
            "principal_id": "principal-1",
        }

        retrieve_route = respx_mock.get("/agent/threads/thread-1").mock(
            return_value=httpx.Response(
                200,
                json={
                    "thread_id": "thread-1",
                    "runs": [{"run_id": "run-1", "status": "SUCCEEDED"}],
                },
            )
        )
        retrieved = client.agent.retrieve_thread("thread-1", principal_id="principal-1")
        assert isinstance(retrieved, AgentThreadDetail)
        assert retrieved.runs[0].run_id == "run-1"
        assert retrieve_route.calls.last.request.url.params["principal_id"] == "principal-1"

        stream_route = respx_mock.get("/agent/runs/run-1/events/stream").mock(
            return_value=httpx.Response(
                200,
                headers={"Content-Type": "text/event-stream"},
                content='id: 3\ndata: {"type":"RUN_STARTED","runId":"run-1"}\n\n',
            )
        )
        with client.agent.stream_run_events("run-1", after=2, last_event_id="1", principal_id="principal-1") as stream:
            assert list(stream) == [{"type": "RUN_STARTED", "runId": "run-1"}]
        request = stream_route.calls.last.request
        assert request.headers["Last-Event-ID"] == "1"
        assert request.headers["Accept"] == "text/event-stream"
        assert dict(request.url.params) == {"after": "2", "principal_id": "principal-1"}

    @pytest.mark.respx(base_url=base_url)
    def test_conversation_methods(self, respx_mock: MockRouter, client: Qaip) -> None:
        list_route = respx_mock.get("/conversations").mock(
            return_value=httpx.Response(200, json={"conversations": [{"id": "conversation-1"}]})
        )
        listed = client.conversations.list(limit=10, offset=1, all_principals=True)
        assert isinstance(listed, ConversationListResponse)
        assert listed.conversations[0].id == "conversation-1"
        assert dict(list_route.calls.last.request.url.params) == {
            "all_principals": "true",
            "limit": "10",
            "offset": "1",
        }

        retrieve_route = respx_mock.get("/conversations/conversation-1").mock(
            return_value=httpx.Response(
                200,
                json={
                    "id": "conversation-1",
                    "active_path": [{"id": "message-1", "role": "user", "content": "hello"}],
                    "tree": [{"id": "message-1", "role": "user"}],
                },
            )
        )
        retrieved = client.conversations.retrieve("conversation-1", leaf_id="message-1", principal_id="principal-1")
        assert isinstance(retrieved, ConversationDetail)
        assert retrieved.active_path[0].content == "hello"
        assert dict(retrieve_route.calls.last.request.url.params) == {
            "leaf_id": "message-1",
            "principal_id": "principal-1",
        }

        update_route = respx_mock.patch("/conversations/conversation-1").mock(
            return_value=httpx.Response(
                200,
                json={"id": "conversation-1", "title": "New title"},
            )
        )
        updated = client.conversations.update(
            "conversation-1",
            title="New title",
            current_leaf_id="message-1",
            principal_id="principal-1",
        )
        assert isinstance(updated, Conversation)
        assert updated.title == "New title"
        assert update_route.calls.last.request.read() == b'{"current_leaf_id":"message-1","title":"New title"}'
        assert update_route.calls.last.request.url.params["principal_id"] == "principal-1"

        delete_route = respx_mock.delete("/conversations/conversation-1").mock(return_value=httpx.Response(204))
        assert client.conversations.delete("conversation-1", principal_id="principal-1") is None
        assert delete_route.calls.last.request.url.params["principal_id"] == "principal-1"

    @pytest.mark.respx(base_url=base_url)
    def test_external_query_methods(self, respx_mock: MockRouter, client: Qaip) -> None:
        create_route = respx_mock.post("/query").mock(
            return_value=httpx.Response(
                200,
                json={"columns": ["amount"], "rows": [{"amount": 42}], "row_count": 1, "truncated": False},
            )
        )
        created = client.external_queries.create(sql="SELECT amount FROM sales")
        assert isinstance(created, ExternalTableQueryResponse)
        assert created.row_count == 1
        assert create_route.calls.last.request.read() == b'{"sql":"SELECT amount FROM sales"}'

        create_route.mock(
            return_value=httpx.Response(
                202,
                json={
                    "response_type": "preparing",
                    "request_id": request_id,
                    "state": "PREPARING",
                    "status_url": f"/query/{request_id}",
                },
            )
        )
        preparing = client.external_queries.create(sql="SELECT amount FROM sales")
        assert isinstance(preparing, ExternalQueryPreparingResponse)
        assert preparing.state == "PREPARING"

        respx_mock.get("/query/schema").mock(
            return_value=httpx.Response(
                200,
                json={
                    "tables": [
                        {
                            "logical_table": "sales",
                            "columns": [{"name": "amount", "type": "BIGINT"}],
                            "synced_at": "2026-08-24T00:00:00Z",
                        }
                    ]
                },
            )
        )
        schema = client.external_queries.retrieve_schema()
        assert isinstance(schema, ExternalTableSchemaResponse)
        assert schema.tables[0].logical_table == "sales"

        respx_mock.get(f"/query/{request_id}").mock(return_value=httpx.Response(200, json=_state_response()))
        retrieved = client.external_queries.retrieve(request_id)
        assert isinstance(retrieved, ExternalQueryStateOnlyResponse)
        assert retrieved.state == "RUNNING"

        respx_mock.delete(f"/query/{request_id}").mock(
            return_value=httpx.Response(200, json=_state_response(state="CANCELLED", terminal=True))
        )
        cancelled = client.external_queries.cancel(request_id)
        assert isinstance(cancelled, ExternalQueryStateOnlyResponse)
        assert cancelled.state == "CANCELLED"

    @pytest.mark.respx(base_url=base_url)
    def test_tag_management_methods(self, respx_mock: MockRouter, client: Qaip) -> None:
        create_route = respx_mock.post("/tags").mock(
            return_value=httpx.Response(200, json={"id": "tag-1", "name": "important", "description": "Important"})
        )
        created = client.tag_management.create(name="important", description="Important")
        assert isinstance(created, Tag)
        assert create_route.calls.last.request.read() == b'{"name":"important","description":"Important"}'

        update_route = respx_mock.put("/tags/tag-1").mock(
            return_value=httpx.Response(200, json={"id": "tag-1", "name": "renamed", "description": "Important"})
        )
        updated = client.tag_management.update("tag-1", name="renamed")
        assert updated.name == "renamed"
        assert update_route.calls.last.request.read() == b'{"name":"renamed"}'

        respx_mock.delete("/tags/tag-1").mock(
            return_value=httpx.Response(200, json={"id": "tag-1", "name": "renamed", "description": "Important"})
        )
        deleted = client.tag_management.delete("tag-1")
        assert deleted.id == "tag-1"


class TestRequestedAsyncAPICoverage:
    @pytest.mark.respx(base_url=base_url)
    async def test_external_query_create_does_not_retry(self, respx_mock: MockRouter, async_client: AsyncQaip) -> None:
        calls = 0

        def handler(request: httpx.Request) -> httpx.Response:
            nonlocal calls
            calls += 1
            if calls == 1:
                return httpx.Response(
                    503,
                    request=request,
                    json={"error": {"type": "outcome_unknown", "message": "unknown"}},
                )
            return httpx.Response(
                200,
                request=request,
                json={"columns": [], "rows": [], "row_count": 0, "truncated": False},
            )

        respx_mock.post("/query").mock(side_effect=handler)
        with patch("qaip._base_client.BaseClient._calculate_retry_timeout", return_value=0):
            with pytest.raises(APIStatusError):
                await async_client.external_queries.create(sql="SELECT 1")
        assert calls == 1

    @pytest.mark.respx(base_url=base_url)
    async def test_all_resources(self, respx_mock: MockRouter, async_client: AsyncQaip) -> None:
        respx_mock.get("/agent/threads").mock(return_value=httpx.Response(200, json={"threads": []}))
        assert (await async_client.agent.list_threads()).threads == []

        respx_mock.get("/agent/threads/thread-1").mock(
            return_value=httpx.Response(200, json={"thread_id": "thread-1", "runs": []})
        )
        assert (await async_client.agent.retrieve_thread("thread-1")).thread_id == "thread-1"

        respx_mock.get("/agent/runs/run-1/events/stream").mock(
            return_value=httpx.Response(
                200,
                headers={"Content-Type": "text/event-stream"},
                content='data: {"type":"RUN_FINISHED","runId":"run-1"}\n\n',
            )
        )
        async with await async_client.agent.stream_run_events("run-1") as stream:
            assert [event async for event in stream] == [{"type": "RUN_FINISHED", "runId": "run-1"}]

        respx_mock.get("/conversations").mock(return_value=httpx.Response(200, json={"conversations": []}))
        assert (await async_client.conversations.list()).conversations == []
        respx_mock.get("/conversations/conversation-1").mock(
            return_value=httpx.Response(200, json={"id": "conversation-1", "active_path": []})
        )
        assert (await async_client.conversations.retrieve("conversation-1")).id == "conversation-1"
        respx_mock.patch("/conversations/conversation-1").mock(
            return_value=httpx.Response(200, json={"id": "conversation-1"})
        )
        assert (await async_client.conversations.update("conversation-1", title="title")).id == "conversation-1"
        respx_mock.delete("/conversations/conversation-1").mock(return_value=httpx.Response(204))
        assert await async_client.conversations.delete("conversation-1") is None

        respx_mock.post("/query").mock(
            return_value=httpx.Response(200, json={"columns": [], "rows": [], "row_count": 0, "truncated": False})
        )
        assert isinstance(
            await async_client.external_queries.create(sql="SELECT 1"),
            ExternalTableQueryResponse,
        )
        respx_mock.get("/query/schema").mock(return_value=httpx.Response(200, json={"tables": []}))
        assert (await async_client.external_queries.retrieve_schema()).tables == []
        respx_mock.get(f"/query/{request_id}").mock(return_value=httpx.Response(200, json=_state_response()))
        assert (await async_client.external_queries.retrieve(request_id)).request_id == request_id
        respx_mock.delete(f"/query/{request_id}").mock(
            return_value=httpx.Response(200, json=_state_response(state="CANCELLED", terminal=True))
        )
        assert (await async_client.external_queries.cancel(request_id)).state == "CANCELLED"

        tag = {"id": "tag-1", "name": "tag", "description": "description"}
        respx_mock.post("/tags").mock(return_value=httpx.Response(200, json=tag))
        assert (await async_client.tag_management.create(name="tag")).id == "tag-1"
        respx_mock.put("/tags/tag-1").mock(return_value=httpx.Response(200, json=tag))
        assert (await async_client.tag_management.update("tag-1", name="tag")).id == "tag-1"
        respx_mock.delete("/tags/tag-1").mock(return_value=httpx.Response(200, json=tag))
        assert (await async_client.tag_management.delete("tag-1")).id == "tag-1"
