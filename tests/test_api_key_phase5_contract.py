from __future__ import annotations

import json
from typing import Any, Iterator, AsyncIterator
from datetime import datetime, timezone
from typing_extensions import override

import httpx
import pytest

from qaip import Qaip, AsyncQaip, ConflictError
from qaip.types import CreatedAPIKey, CreatedApiKey, IssuableAPIKeyScope, IssuableApiKeyScope, CreatedExpiringAPIKey
from qaip.resources import APIKeysResource, ApiKeysResource, AsyncAPIKeysResource, AsyncApiKeysResource
from qaip.resources.api_keys import __all__ as api_key_exports
from qaip.types.api_key_create_params import APIKeyCreateParams, ApiKeyCreateParams

KEY_ID = "019febbe-235a-7d69-a141-be4bbef5bb03"
EXPIRY = "2030-01-01T00:00:00Z"


def _payload() -> dict[str, Any]:
    return {
        "id": KEY_ID,
        "creation_time": "2026-09-07T00:00:00Z",
        "expires_at": EXPIRY,
        "key": "synthetic-test-key",
        "key_kind": "personal",
        "name": "contract-test",
        "scopes": ["knowledge:read"],
    }


def test_published_api_key_imports_remain_compatible() -> None:
    assert CreatedApiKey is CreatedAPIKey
    assert IssuableApiKeyScope is IssuableAPIKeyScope
    assert ApiKeyCreateParams is APIKeyCreateParams
    assert ApiKeysResource is APIKeysResource
    assert AsyncApiKeysResource is AsyncAPIKeysResource
    assert {"ApiKeysResource", "AsyncApiKeysResource"} <= set(api_key_exports)


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("expiration", [{"ttl": 3600}, {"expires_at": EXPIRY}])
async def test_expiring_key_and_revoke_wire_contract(asynchronous: bool, expiration: dict[str, Any]) -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        assert request.headers["X-API-Key"] == "synthetic-caller"
        assert "authorization" not in request.headers
        if request.method == "POST":
            assert request.url.path == "/api/v1/api-keys/expiring"
            assert request.headers["Idempotency-Key"] == "contract-issuance-1"
            assert json.loads(request.content) == {
                "name": "contract-test",
                "key_kind": "personal",
                "scopes": ["knowledge:read"],
                **expiration,
            }
            return httpx.Response(201, json=_payload())
        assert request.method == "DELETE"
        assert request.url.path == f"/api/v1/api-keys/{KEY_ID}"
        return httpx.Response(204)

    arguments: dict[str, Any] = {
        "name": "contract-test",
        "key_kind": "personal",
        "scopes": ["knowledge:read"],
        "idempotency_key": "contract-issuance-1",
        **expiration,
    }
    transport = httpx.MockTransport(handler)
    if asynchronous:
        async with AsyncQaip(
            api_key="synthetic-caller",
            base_url="https://example.test/api/v1",
            http_client=httpx.AsyncClient(transport=transport),
        ) as client:
            result = await client.api_keys.create_expiring(**arguments)
            assert await client.api_keys.revoke(KEY_ID) is None
    else:
        with Qaip(
            api_key="synthetic-caller",
            base_url="https://example.test/api/v1",
            http_client=httpx.Client(transport=transport),
        ) as sync_client:
            result = sync_client.api_keys.create_expiring(**arguments)
            assert sync_client.api_keys.revoke(KEY_ID) is None
    assert isinstance(result, CreatedExpiringAPIKey)
    assert result.expires_at == datetime(2030, 1, 1, tzinfo=timezone.utc)
    assert len(requests) == 2


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("streaming", [False, True])
async def test_lost_response_preserves_idempotency_and_exposes_recovery_conflict(
    asynchronous: bool, streaming: bool
) -> None:
    requests: list[httpx.Request] = []
    error = {"code": "credential_already_created", "details": {"api_key_id": KEY_ID}, "retryable": False}

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if len(requests) == 1:
            raise httpx.ReadTimeout("synthetic response loss", request=request)
        if len(requests) > 2:
            raise httpx.ReadTimeout("synthetic failure after recovery", request=request)
        return httpx.Response(
            409,
            headers={"content-type": "application/json"},
            stream=httpx.ByteStream(json.dumps({"error": error}).encode()),
        )

    arguments: dict[str, Any] = {
        "name": "contract-test",
        "key_kind": "personal",
        "scopes": ["knowledge:read"],
        "idempotency_key": "contract-recovery-1",
        "ttl": 3600,
    }
    transport = httpx.MockTransport(handler)
    with pytest.raises(ConflictError) as caught:
        if asynchronous:
            async with AsyncQaip(
                api_key="synthetic-caller",
                base_url="https://example.test/api/v1",
                http_client=httpx.AsyncClient(transport=transport),
            ) as client:
                if streaming:
                    async with client.api_keys.with_streaming_response.create_expiring(**arguments):
                        pytest.fail("復旧用の409を返す必要がある")
                else:
                    await client.api_keys.create_expiring(**arguments)
        else:
            with Qaip(
                api_key="synthetic-caller",
                base_url="https://example.test/api/v1",
                http_client=httpx.Client(transport=transport),
            ) as sync_client:
                if streaming:
                    with sync_client.api_keys.with_streaming_response.create_expiring(**arguments):
                        pytest.fail("復旧用の409を返す必要がある")
                else:
                    sync_client.api_keys.create_expiring(**arguments)
    assert caught.value.body == {"error": error}
    assert len(requests) == 2
    assert requests[0].content == requests[1].content
    assert all(request.headers["Idempotency-Key"] == "contract-recovery-1" for request in requests)


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("streaming", [False, True])
async def test_in_progress_issuance_is_retried(asynchronous: bool, streaming: bool) -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if len(requests) == 1:
            return httpx.Response(
                409,
                headers={"content-type": "application/json", "retry-after-ms": "1"},
                stream=httpx.ByteStream(
                    json.dumps({"error": {"code": "idempotency_in_progress", "retryable": True}}).encode()
                ),
            )
        return httpx.Response(201, json=_payload())

    arguments: dict[str, Any] = {
        "name": "contract-test",
        "key_kind": "personal",
        "scopes": ["knowledge:read"],
        "idempotency_key": "contract-pending-1",
        "ttl": 3600,
    }
    transport = httpx.MockTransport(handler)
    if asynchronous:
        async with AsyncQaip(
            api_key="synthetic-caller",
            base_url="https://example.test/api/v1",
            http_client=httpx.AsyncClient(transport=transport),
        ) as client:
            if streaming:
                async with client.api_keys.with_streaming_response.create_expiring(**arguments) as response:
                    result = await response.parse()
            else:
                result = await client.api_keys.create_expiring(**arguments)
    else:
        with Qaip(
            api_key="synthetic-caller",
            base_url="https://example.test/api/v1",
            http_client=httpx.Client(transport=transport),
        ) as sync_client:
            if streaming:
                with sync_client.api_keys.with_streaming_response.create_expiring(**arguments) as sync_response:
                    result = sync_response.parse()
            else:
                result = sync_client.api_keys.create_expiring(**arguments)
    assert result.id == KEY_ID
    assert len(requests) == 2
    assert requests[0].content == requests[1].content
    assert all(request.headers["Idempotency-Key"] == "contract-pending-1" for request in requests)


@pytest.mark.parametrize(
    "method,path,body,headers,expected",
    [
        (
            "POST",
            "/api/v1/api-keys/expiring",
            '{"error":{"code":"idempotency_conflict","retryable":false}}',
            {"x-should-retry": "true"},
            False,
        ),
        (
            "POST",
            "/other",
            '{"error":{"code":"credential_already_created","retryable":false}}',
            {},
            True,
        ),
        (
            "GET",
            "/api/v1/api-keys/expiring",
            '{"error":{"code":"credential_already_created","retryable":false}}',
            {},
            True,
        ),
        ("POST", "/api/v1/api-keys/expiring", "invalid JSON", {}, True),
        ("POST", "/api/v1/api-keys/expiring", '{"error":"conflict"}', {}, True),
        ("POST", "/api/v1/api-keys/expiring", "[]", {}, True),
    ],
)
def test_terminal_conflict_retry_policy_is_scoped(
    method: str, path: str, body: str, headers: dict[str, str], expected: bool
) -> None:
    with Qaip(api_key="synthetic-caller") as client:
        response = httpx.Response(
            409, content=body, headers=headers, request=httpx.Request(method, f"https://example.test{path}")
        )
        assert client._should_retry(response) is expected  # pyright: ignore[reportPrivateUsage]


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("max_retries", [0, 2])
@pytest.mark.parametrize("retry_veto", [False, True])
async def test_streaming_conflict_preserves_final_read_timeout(
    asynchronous: bool, max_retries: int, retry_veto: bool
) -> None:
    class FailingSyncStream(httpx.SyncByteStream):
        @override
        def __iter__(self) -> Iterator[bytes]:
            yield b"{"
            raise httpx.ReadTimeout("synthetic incomplete conflict")

    class FailingAsyncStream(httpx.AsyncByteStream):
        @override
        async def __aiter__(self) -> AsyncIterator[bytes]:
            yield b"{"
            raise httpx.ReadTimeout("synthetic incomplete conflict")

    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        headers = {"content-type": "application/json", "retry-after-ms": "1"}
        if retry_veto:
            headers["x-should-retry"] = "false"
        return httpx.Response(
            409,
            headers=headers,
            stream=FailingAsyncStream() if asynchronous else FailingSyncStream(),
        )

    arguments: dict[str, Any] = {
        "name": "contract-test",
        "key_kind": "personal",
        "scopes": ["knowledge:read"],
        "idempotency_key": "contract-read-timeout-1",
        "ttl": 3600,
    }
    transport = httpx.MockTransport(handler)
    with pytest.raises(httpx.ReadTimeout, match="synthetic incomplete conflict"):
        if asynchronous:
            async with AsyncQaip(
                api_key="synthetic-caller",
                max_retries=max_retries,
                base_url="https://example.test/api/v1",
                http_client=httpx.AsyncClient(transport=transport),
            ) as client:
                async with client.api_keys.with_streaming_response.create_expiring(**arguments):
                    pytest.fail("本文の通信エラーを返す必要がある")
        else:
            with Qaip(
                api_key="synthetic-caller",
                max_retries=max_retries,
                base_url="https://example.test/api/v1",
                http_client=httpx.Client(transport=transport),
            ) as sync_client:
                with sync_client.api_keys.with_streaming_response.create_expiring(**arguments):
                    pytest.fail("本文の通信エラーを返す必要がある")
    assert len(requests) == (1 if retry_veto else max_retries + 1)
