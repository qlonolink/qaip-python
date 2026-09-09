from __future__ import annotations

import httpx
import pytest

from qaip import Qaip, AsyncQaip, APIStatusError

pytestmark = pytest.mark.filterwarnings("ignore:deprecated:DeprecationWarning")


def _issued_payload(request: httpx.Request) -> httpx.Response:
    return httpx.Response(
        201,
        json={
            "id": "019febbe-235a-7d69-a141-be4bbef5bb03",
            "name": "n",
            "key": "qaip_plaintext",
            "scopes": ["inference:run"],
            "creation_time": 1,
        },
        request=request,
    )


class TestApiKeyIssuanceIsNotRetried:
    """発行は冪等でないため、応答が失われた再送で鍵が重複してはいけない。"""

    def test_sync_create_does_not_retry_on_5xx(self) -> None:
        calls: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(request)
            if len(calls) == 1:
                return httpx.Response(
                    500,
                    json={"error": "lost after commit"},
                    headers={"x-should-retry": "true", "retry-after-ms": "0"},
                    request=request,
                )
            return _issued_payload(request)

        client = Qaip(
            api_key="caller",
            base_url="https://example.test",
            http_client=httpx.Client(transport=httpx.MockTransport(handler)),
        )
        with pytest.raises(APIStatusError):
            client.api_keys.create(name="n", scopes=["inference:run"])  # pyright: ignore[reportDeprecated]
        assert len(calls) == 1

    async def test_async_create_does_not_retry_on_5xx(self) -> None:
        calls: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(request)
            if len(calls) == 1:
                return httpx.Response(
                    500,
                    json={"error": "lost after commit"},
                    headers={"x-should-retry": "true", "retry-after-ms": "0"},
                    request=request,
                )
            return _issued_payload(request)

        client = AsyncQaip(
            api_key="caller",
            base_url="https://example.test",
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
        )
        with pytest.raises(APIStatusError):
            await client.api_keys.create(name="n", scopes=["inference:run"])  # pyright: ignore[reportDeprecated]
        assert len(calls) == 1
