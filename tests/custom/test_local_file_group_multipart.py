from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from qaip import Qaip, AsyncQaip

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


def _assert_repeat_multipart_fields(body: bytes) -> None:
    assert b'name="files[]"' not in body
    assert b'name="last_modified[]"' not in body
    assert body.count(b'name="files"; filename=') == 2
    assert b'name="files"; filename="a.txt"' in body
    assert b'name="files"; filename="b.txt"' in body
    assert body.count(b'name="last_modified"') == 2
    assert b'name="last_modified"\r\n\r\n1000' in body
    assert b'name="last_modified"\r\n\r\n2000' in body
    assert b'name="name"\r\n\r\nlfg' in body


@pytest.mark.respx(base_url=base_url)
def test_local_file_groups_create_uses_repeat_multipart_fields(
    respx_mock: MockRouter,
    client: Qaip,
) -> None:
    captured_bodies: list[bytes] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured_bodies.append(request.read())
        return httpx.Response(200, json={"source_group_id": "019ede24-8c8a-7b95-a5c6-36fff2574cbe"})

    respx_mock.post("/local-file-groups").mock(side_effect=handler)

    result = client.local_file_groups.create(
        files=[("a.txt", b"hello"), ("b.txt", b"world")],
        last_modified=["1000", "2000"],
        name="lfg",
    )

    assert result.source_group_id == "019ede24-8c8a-7b95-a5c6-36fff2574cbe"
    assert len(captured_bodies) == 1
    _assert_repeat_multipart_fields(captured_bodies[0])


@pytest.mark.respx(base_url=base_url)
async def test_async_local_file_groups_create_uses_repeat_multipart_fields(
    respx_mock: MockRouter,
    async_client: AsyncQaip,
) -> None:
    captured_bodies: list[bytes] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured_bodies.append(request.read())
        return httpx.Response(200, json={"source_group_id": "019ede24-8c8a-7b95-a5c6-36fff2574cbe"})

    respx_mock.post("/local-file-groups").mock(side_effect=handler)

    result = await async_client.local_file_groups.create(
        files=[("a.txt", b"hello"), ("b.txt", b"world")],
        last_modified=["1000", "2000"],
        name="lfg",
    )

    assert result.source_group_id == "019ede24-8c8a-7b95-a5c6-36fff2574cbe"
    assert len(captured_bodies) == 1
    _assert_repeat_multipart_fields(captured_bodies[0])
