# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import agent_run_params, agent_create_run_params, agent_list_run_events_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.agent_run import AgentRun
from ..types.agent_run_response import AgentRunResponse
from ..types.agent_message_param import AgentMessageParam
from ..types.agent_list_run_events_response import AgentListRunEventsResponse
from ..types.agent_retrieve_run_result_response import AgentRetrieveRunResultResponse

__all__ = ["AgentResource", "AsyncAgentResource"]


class AgentResource(SyncAPIResource):
    """(Experimental) Agent operations"""

    @cached_property
    def with_raw_response(self) -> AgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AgentResourceWithStreamingResponse(self)

    def cancel_run(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRun:
        """<p> Mark an asynchronous agent run as cancelled.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._post(
            path_template("/agent/runs/{run_id}/cancel", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRun,
        )

    def create_run(
        self,
        *,
        input: agent_create_run_params.Input,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRun:
        """<p> Create an asynchronous agent run and start execution in the background.

        </p> <p> Required roles: All, App </p>

        Args:
          idempotency_key: Optional idempotency key for reusing an existing asynchronous run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agent/runs",
            body=maybe_transform(
                {
                    "input": input,
                    "idempotency_key": idempotency_key,
                },
                agent_create_run_params.AgentCreateRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRun,
        )

    def list_run_events(
        self,
        run_id: str,
        *,
        after: int | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListRunEventsResponse:
        """<p> List persisted events for an asynchronous agent run.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/agent/runs/{run_id}/events", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    agent_list_run_events_params.AgentListRunEventsParams,
                ),
            ),
            cast_to=AgentListRunEventsResponse,
        )

    def retrieve_run(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRun:
        """<p> Get the current state of an asynchronous agent run.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/agent/runs/{run_id}", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRun,
        )

    def retrieve_run_result(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveRunResultResponse:
        """<p> Get the terminal result and error state for an asynchronous agent run.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/agent/runs/{run_id}/result", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveRunResultResponse,
        )

    def run(
        self,
        *,
        forwarded_props: agent_run_params.ForwardedProps | Omit = omit,
        messages: Iterable[AgentMessageParam] | Omit = omit,
        run_id: str | Omit = omit,
        thread_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[AgentRunResponse]:
        """<p> Run the agent with the given input and stream the events.

        </p> <p> Required roles: All, App </p>

        Args:
          forwarded_props: Forwarded properties for the run (AG-UI standard)

          run_id: Optional ID for the run

          thread_id: Optional ID for the thread

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/agent/run",
            body=maybe_transform(
                {
                    "forwarded_props": forwarded_props,
                    "messages": messages,
                    "run_id": run_id,
                    "thread_id": thread_id,
                },
                agent_run_params.AgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
            stream=True,
            stream_cls=Stream[AgentRunResponse],
        )


class AsyncAgentResource(AsyncAPIResource):
    """(Experimental) Agent operations"""

    @cached_property
    def with_raw_response(self) -> AsyncAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncAgentResourceWithStreamingResponse(self)

    async def cancel_run(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRun:
        """<p> Mark an asynchronous agent run as cancelled.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._post(
            path_template("/agent/runs/{run_id}/cancel", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRun,
        )

    async def create_run(
        self,
        *,
        input: agent_create_run_params.Input,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRun:
        """<p> Create an asynchronous agent run and start execution in the background.

        </p> <p> Required roles: All, App </p>

        Args:
          idempotency_key: Optional idempotency key for reusing an existing asynchronous run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agent/runs",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "idempotency_key": idempotency_key,
                },
                agent_create_run_params.AgentCreateRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRun,
        )

    async def list_run_events(
        self,
        run_id: str,
        *,
        after: int | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListRunEventsResponse:
        """<p> List persisted events for an asynchronous agent run.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/agent/runs/{run_id}/events", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    agent_list_run_events_params.AgentListRunEventsParams,
                ),
            ),
            cast_to=AgentListRunEventsResponse,
        )

    async def retrieve_run(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRun:
        """<p> Get the current state of an asynchronous agent run.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/agent/runs/{run_id}", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRun,
        )

    async def retrieve_run_result(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveRunResultResponse:
        """<p> Get the terminal result and error state for an asynchronous agent run.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/agent/runs/{run_id}/result", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveRunResultResponse,
        )

    async def run(
        self,
        *,
        forwarded_props: agent_run_params.ForwardedProps | Omit = omit,
        messages: Iterable[AgentMessageParam] | Omit = omit,
        run_id: str | Omit = omit,
        thread_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[AgentRunResponse]:
        """<p> Run the agent with the given input and stream the events.

        </p> <p> Required roles: All, App </p>

        Args:
          forwarded_props: Forwarded properties for the run (AG-UI standard)

          run_id: Optional ID for the run

          thread_id: Optional ID for the thread

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/agent/run",
            body=await async_maybe_transform(
                {
                    "forwarded_props": forwarded_props,
                    "messages": messages,
                    "run_id": run_id,
                    "thread_id": thread_id,
                },
                agent_run_params.AgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
            stream=True,
            stream_cls=AsyncStream[AgentRunResponse],
        )


class AgentResourceWithRawResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.cancel_run = to_raw_response_wrapper(
            agent.cancel_run,
        )
        self.create_run = to_raw_response_wrapper(
            agent.create_run,
        )
        self.list_run_events = to_raw_response_wrapper(
            agent.list_run_events,
        )
        self.retrieve_run = to_raw_response_wrapper(
            agent.retrieve_run,
        )
        self.retrieve_run_result = to_raw_response_wrapper(
            agent.retrieve_run_result,
        )
        self.run = to_raw_response_wrapper(
            agent.run,
        )


class AsyncAgentResourceWithRawResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.cancel_run = async_to_raw_response_wrapper(
            agent.cancel_run,
        )
        self.create_run = async_to_raw_response_wrapper(
            agent.create_run,
        )
        self.list_run_events = async_to_raw_response_wrapper(
            agent.list_run_events,
        )
        self.retrieve_run = async_to_raw_response_wrapper(
            agent.retrieve_run,
        )
        self.retrieve_run_result = async_to_raw_response_wrapper(
            agent.retrieve_run_result,
        )
        self.run = async_to_raw_response_wrapper(
            agent.run,
        )


class AgentResourceWithStreamingResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.cancel_run = to_streamed_response_wrapper(
            agent.cancel_run,
        )
        self.create_run = to_streamed_response_wrapper(
            agent.create_run,
        )
        self.list_run_events = to_streamed_response_wrapper(
            agent.list_run_events,
        )
        self.retrieve_run = to_streamed_response_wrapper(
            agent.retrieve_run,
        )
        self.retrieve_run_result = to_streamed_response_wrapper(
            agent.retrieve_run_result,
        )
        self.run = to_streamed_response_wrapper(
            agent.run,
        )


class AsyncAgentResourceWithStreamingResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.cancel_run = async_to_streamed_response_wrapper(
            agent.cancel_run,
        )
        self.create_run = async_to_streamed_response_wrapper(
            agent.create_run,
        )
        self.list_run_events = async_to_streamed_response_wrapper(
            agent.list_run_events,
        )
        self.retrieve_run = async_to_streamed_response_wrapper(
            agent.retrieve_run,
        )
        self.retrieve_run_result = async_to_streamed_response_wrapper(
            agent.retrieve_run_result,
        )
        self.run = async_to_streamed_response_wrapper(
            agent.run,
        )
