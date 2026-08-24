# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import tag_management_create_params, tag_management_update_params
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
from .._base_client import make_request_options
from ..types.shared.tag import Tag

__all__ = ["TagManagementResource", "AsyncTagManagementResource"]


class TagManagementResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TagManagementResourceWithRawResponse:
        return TagManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagManagementResourceWithStreamingResponse:
        return TagManagementResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tag:
        return self._post(
            "/tags",
            body=maybe_transform(
                {"name": name, "description": description},
                tag_management_create_params.TagManagementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )

    def update(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tag:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/tags/{id}", id=id),
            body=maybe_transform(
                {"description": description, "name": name},
                tag_management_update_params.TagManagementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )

    def delete(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tag:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/tags/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )


class AsyncTagManagementResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTagManagementResourceWithRawResponse:
        return AsyncTagManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagManagementResourceWithStreamingResponse:
        return AsyncTagManagementResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tag:
        return await self._post(
            "/tags",
            body=await async_maybe_transform(
                {"name": name, "description": description},
                tag_management_create_params.TagManagementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )

    async def update(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tag:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/tags/{id}", id=id),
            body=await async_maybe_transform(
                {"description": description, "name": name},
                tag_management_update_params.TagManagementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )

    async def delete(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tag:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/tags/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )


class TagManagementResourceWithRawResponse:
    def __init__(self, tag_management: TagManagementResource) -> None:
        self.create = to_raw_response_wrapper(tag_management.create)
        self.update = to_raw_response_wrapper(tag_management.update)
        self.delete = to_raw_response_wrapper(tag_management.delete)


class AsyncTagManagementResourceWithRawResponse:
    def __init__(self, tag_management: AsyncTagManagementResource) -> None:
        self.create = async_to_raw_response_wrapper(tag_management.create)
        self.update = async_to_raw_response_wrapper(tag_management.update)
        self.delete = async_to_raw_response_wrapper(tag_management.delete)


class TagManagementResourceWithStreamingResponse:
    def __init__(self, tag_management: TagManagementResource) -> None:
        self.create = to_streamed_response_wrapper(tag_management.create)
        self.update = to_streamed_response_wrapper(tag_management.update)
        self.delete = to_streamed_response_wrapper(tag_management.delete)


class AsyncTagManagementResourceWithStreamingResponse:
    def __init__(self, tag_management: AsyncTagManagementResource) -> None:
        self.create = async_to_streamed_response_wrapper(tag_management.create)
        self.update = async_to_streamed_response_wrapper(tag_management.update)
        self.delete = async_to_streamed_response_wrapper(tag_management.delete)
