from __future__ import annotations

from unittest.mock import patch

import httpx
import pytest

from qaip import Qaip, AsyncQaip, APITimeoutError, InternalServerError
from tests.custom.test_deletion_retries import GROUP, failure_transport


@pytest.mark.parametrize("failure", ["lost_response", "status"])
def test_chunk_bulk_deletion_start_sends_once(failure: str) -> None:
    requests: list[httpx.Request] = []
    error = APITimeoutError if failure == "lost_response" else InternalServerError
    with Qaip(
        api_key="test",
        base_url="https://test.invalid",
        http_client=httpx.Client(transport=failure_transport(failure, requests)),
    ) as client:
        with patch.object(client, "_calculate_retry_timeout", return_value=0), pytest.raises(error):
            client.local_file_groups.start_chunk_bulk_deletion(
                deletions=[{"source_group_id": GROUP, "text_contains": ["test"]}]
            )
    assert len(requests) == 1
    assert requests[0].url.path == "/local-file-groups/chunk-bulk-deletions"


@pytest.mark.parametrize("failure", ["lost_response", "status"])
async def test_async_chunk_bulk_deletion_start_sends_once(failure: str) -> None:
    requests: list[httpx.Request] = []
    error = APITimeoutError if failure == "lost_response" else InternalServerError
    async with AsyncQaip(
        api_key="test",
        base_url="https://test.invalid",
        http_client=httpx.AsyncClient(transport=failure_transport(failure, requests)),
    ) as client:
        with patch.object(client, "_calculate_retry_timeout", return_value=0), pytest.raises(error):
            await client.local_file_groups.start_chunk_bulk_deletion(
                deletions=[{"source_group_id": GROUP, "text_contains": ["test"]}]
            )
    assert len(requests) == 1
    assert requests[0].url.path == "/local-file-groups/chunk-bulk-deletions"
