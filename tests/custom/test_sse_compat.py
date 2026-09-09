from __future__ import annotations

from collections.abc import Iterator, AsyncIterator

import httpx
import pytest

from qaip import Qaip, AsyncQaip
from qaip._streaming import Stream, AsyncStream


async def _to_async_iterator(iterator: Iterator[bytes]) -> AsyncIterator[bytes]:
    for chunk in iterator:
        yield chunk


@pytest.mark.parametrize("sync", [True, False], ids=["sync", "async"])
async def test_json_stream_ignores_comment_frames_after_event_id(
    sync: bool,
    client: Qaip,
    async_client: AsyncQaip,
) -> None:
    def body() -> Iterator[bytes]:
        yield b'id: 1\ndata: {"type":"RUN_STARTED"}\n\n: flush    \n\n'
        yield b": keepalive\n\n"
        yield b'id: 2\ndata: {"type":"RUN_FINISHED"}\n\n'

    expected = [{"type": "RUN_STARTED"}, {"type": "RUN_FINISHED"}]
    if sync:
        stream = Stream(cast_to=object, client=client, response=httpx.Response(200, content=body()))
        assert list(stream) == expected
        return

    stream = AsyncStream(
        cast_to=object,
        client=async_client,
        response=httpx.Response(200, content=_to_async_iterator(body())),
    )
    assert [event async for event in stream] == expected


@pytest.mark.parametrize("sync", [True, False], ids=["sync", "async"])
async def test_string_stream_preserves_raw_sse_data(
    sync: bool,
    client: Qaip,
    async_client: AsyncQaip,
) -> None:
    def body() -> Iterator[bytes]:
        yield b'data: {"type":"RUN_STARTED","runId":"run-1"}\n\n'

    expected = ['{"type":"RUN_STARTED","runId":"run-1"}']
    if sync:
        stream = Stream(cast_to=str, client=client, response=httpx.Response(200, content=body()))
        assert list(stream) == expected
        return

    stream = AsyncStream(
        cast_to=str,
        client=async_client,
        response=httpx.Response(200, content=_to_async_iterator(body())),
    )
    assert [event async for event in stream] == expected
