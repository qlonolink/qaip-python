from __future__ import annotations

from unittest.mock import patch

import httpx
import pytest

from qaip import Qaip, AsyncQaip, APITimeoutError, InternalServerError

GROUP = "00000000-0000-4000-8000-000000000001"
JOB = "00000000-0000-4000-8000-000000000002"


def failure_transport(failure: str, requests: list[httpx.Request]) -> httpx.MockTransport:
    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if failure == "lost_response":
            raise httpx.ReadTimeout("response was lost", request=request)
        return httpx.Response(503, json={"error": {"message": "temporarily unavailable"}})

    return httpx.MockTransport(handler)


@pytest.mark.parametrize("operation", ["chunk", "bulk"])
@pytest.mark.parametrize("failure", ["lost_response", "status"])
def test_deletion_job_start_sends_once(operation: str, failure: str) -> None:
    requests: list[httpx.Request] = []
    error = APITimeoutError if failure == "lost_response" else InternalServerError
    with Qaip(
        api_key="test",
        base_url="https://test.invalid",
        http_client=httpx.Client(transport=failure_transport(failure, requests)),
    ) as client:
        with patch.object(client, "_calculate_retry_timeout", return_value=0), pytest.raises(error):
            if operation == "chunk":
                client.local_file_groups.start_chunk_deletion(id=GROUP, text_contains=["test"])
            else:
                client.local_file_groups.start_bulk_deletion(source_group_ids=[GROUP])
    assert len(requests) == 1
    assert requests[0].method == "POST"
    expected_path = (
        f"/local-file-groups/{GROUP}/chunk-deletions" if operation == "chunk" else "/local-file-groups/bulk-deletions"
    )
    assert requests[0].url.path == expected_path


@pytest.mark.parametrize("operation", ["chunk", "bulk"])
@pytest.mark.parametrize("failure", ["lost_response", "status"])
async def test_async_deletion_job_start_sends_once(operation: str, failure: str) -> None:
    requests: list[httpx.Request] = []
    error = APITimeoutError if failure == "lost_response" else InternalServerError
    async with AsyncQaip(
        api_key="test",
        base_url="https://test.invalid",
        http_client=httpx.AsyncClient(transport=failure_transport(failure, requests)),
    ) as client:
        with patch.object(client, "_calculate_retry_timeout", return_value=0), pytest.raises(error):
            if operation == "chunk":
                await client.local_file_groups.start_chunk_deletion(id=GROUP, text_contains=["test"])
            else:
                await client.local_file_groups.start_bulk_deletion(source_group_ids=[GROUP])
    assert len(requests) == 1
    assert requests[0].method == "POST"
    expected_path = (
        f"/local-file-groups/{GROUP}/chunk-deletions" if operation == "chunk" else "/local-file-groups/bulk-deletions"
    )
    assert requests[0].url.path == expected_path


@pytest.mark.parametrize("operation", ["chunk", "bulk"])
def test_deletion_status_keeps_default_retries(operation: str) -> None:
    requests: list[httpx.Request] = []
    with Qaip(
        api_key="test",
        base_url="https://test.invalid",
        http_client=httpx.Client(transport=failure_transport("status", requests)),
    ) as client:
        with patch.object(client, "_calculate_retry_timeout", return_value=0), pytest.raises(InternalServerError):
            if operation == "chunk":
                client.local_file_groups.retrieve_chunk_deletion(chunk_deletion_id=JOB, id=GROUP)
            else:
                client.local_file_groups.retrieve_bulk_deletion(bulk_deletion_id=JOB)
    assert len(requests) == 3
    assert all(request.method == "GET" for request in requests)


@pytest.mark.parametrize("operation", ["chunk", "bulk"])
async def test_async_deletion_status_keeps_default_retries(operation: str) -> None:
    requests: list[httpx.Request] = []
    async with AsyncQaip(
        api_key="test",
        base_url="https://test.invalid",
        http_client=httpx.AsyncClient(transport=failure_transport("status", requests)),
    ) as client:
        with patch.object(client, "_calculate_retry_timeout", return_value=0), pytest.raises(InternalServerError):
            if operation == "chunk":
                await client.local_file_groups.retrieve_chunk_deletion(chunk_deletion_id=JOB, id=GROUP)
            else:
                await client.local_file_groups.retrieve_bulk_deletion(bulk_deletion_id=JOB)
    assert len(requests) == 3
    assert all(request.method == "GET" for request in requests)
