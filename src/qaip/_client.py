# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, List, Mapping, Iterable
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_search_params, client_extract_params, client_completion_params
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    SequenceNotStr,
    omit,
    not_given,
)
from ._utils import (
    is_given,
    path_template,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._compat import cached_property
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import QaipError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.tags_response import TagsResponse
from .types.shared.content import Content
from .types.search_response import SearchResponse
from .types.extract_response import ExtractResponse
from .types.shared.file_type import FileType
from .types.shared.source_type import SourceType
from .types.completion_response import CompletionResponse
from .types.shared.logical_operator import LogicalOperator
from .types.shared_params.metadata_filter_group import MetadataFilterGroup

if TYPE_CHECKING:
    from .resources import (
        agent,
        crawls,
        githubs,
        notions,
        secrets,
        sources,
        google_drives,
        source_groups,
        local_file_groups,
        tag_source_groups,
    )
    from .resources.agent import AgentResource, AsyncAgentResource
    from .resources.crawls import CrawlsResource, AsyncCrawlsResource
    from .resources.githubs import GithubsResource, AsyncGithubsResource
    from .resources.notions import NotionsResource, AsyncNotionsResource
    from .resources.secrets import SecretsResource, AsyncSecretsResource
    from .resources.sources import SourcesResource, AsyncSourcesResource
    from .resources.google_drives import GoogleDrivesResource, AsyncGoogleDrivesResource
    from .resources.source_groups import SourceGroupsResource, AsyncSourceGroupsResource
    from .resources.local_file_groups import LocalFileGroupsResource, AsyncLocalFileGroupsResource
    from .resources.tag_source_groups import TagSourceGroupsResource, AsyncTagSourceGroupsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Qaip", "AsyncQaip", "Client", "AsyncClient"]


class Qaip(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Qaip client instance.

        This automatically infers the `api_key` argument from the `QAIP_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("QAIP_API_KEY")
        if api_key is None:
            raise QaipError(
                "The api_key client option must be set either by passing api_key to the client or by setting the QAIP_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("QAIP_BASE_URL")
        if base_url is None:
            base_url = f"https://developer.qaip.com/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def agent(self) -> AgentResource:
        """(Experimental) Agent operations"""
        from .resources.agent import AgentResource

        return AgentResource(self)

    @cached_property
    def tag_source_groups(self) -> TagSourceGroupsResource:
        """Tag and source group associations"""
        from .resources.tag_source_groups import TagSourceGroupsResource

        return TagSourceGroupsResource(self)

    @cached_property
    def source_groups(self) -> SourceGroupsResource:
        """Source group (job) management and metadata"""
        from .resources.source_groups import SourceGroupsResource

        return SourceGroupsResource(self)

    @cached_property
    def sources(self) -> SourcesResource:
        """Sources management and metadata"""
        from .resources.sources import SourcesResource

        return SourcesResource(self)

    @cached_property
    def local_file_groups(self) -> LocalFileGroupsResource:
        """Local file group management"""
        from .resources.local_file_groups import LocalFileGroupsResource

        return LocalFileGroupsResource(self)

    @cached_property
    def secrets(self) -> SecretsResource:
        """Secret management"""
        from .resources.secrets import SecretsResource

        return SecretsResource(self)

    @cached_property
    def google_drives(self) -> GoogleDrivesResource:
        from .resources.google_drives import GoogleDrivesResource

        return GoogleDrivesResource(self)

    @cached_property
    def crawls(self) -> CrawlsResource:
        from .resources.crawls import CrawlsResource

        return CrawlsResource(self)

    @cached_property
    def githubs(self) -> GithubsResource:
        from .resources.githubs import GithubsResource

        return GithubsResource(self)

    @cached_property
    def notions(self) -> NotionsResource:
        from .resources.notions import NotionsResource

        return NotionsResource(self)

    @cached_property
    def with_raw_response(self) -> QaipWithRawResponse:
        return QaipWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QaipWithStreamedResponse:
        return QaipWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def completion(
        self,
        *,
        messages: Iterable[client_completion_params.Message],
        chunk_metadata: MetadataFilterGroup | Omit = omit,
        citation: bool | Omit = omit,
        date_from: int | Omit = omit,
        date_to: int | Omit = omit,
        domains: SequenceNotStr[str] | Omit = omit,
        file_types: List[FileType] | Omit = omit,
        metadata: MetadataFilterGroup | Omit = omit,
        source_metadata: MetadataFilterGroup | Omit = omit,
        source_types: List[SourceType] | Omit = omit,
        stream: bool | Omit = omit,
        tag_filter_logic: LogicalOperator | Omit = omit,
        tag_ids: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionResponse:
        """<p> Generates a completion based on the input messages and retrieval chunks.

        If the 'stream' parameter is set to true, the response is returned as a stream of plain text (text/plain). </p> <p> Required roles: All, App </p>

        Args:
          messages: The messages to generate completion for

          chunk_metadata: Filter by chunk-level metadata from chunk_metadatas table

          citation: Whether to include citations in the response

          date_from: Start date for content search (Unix timestamp in seconds)

          date_to: End date for content search (Unix timestamp in seconds)

          domains: Array of domains to search within (supports partial matching)

          metadata: (reserved for future use) Filter group with nested structure. Supports combining
              filters with AND/OR logic.

          source_metadata: Filter by individual source/file metadata from source_metadatas table

          stream: Whether to stream the response. If true, the response is sent as a stream using
              the 'text/plain' content type.

          tag_filter_logic: Logical operator for combining filter conditions

          tag_ids: target tag IDs to be obtained

          tags: target tag names to be obtained

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "chunk_metadata": chunk_metadata,
                    "citation": citation,
                    "date_from": date_from,
                    "date_to": date_to,
                    "domains": domains,
                    "file_types": file_types,
                    "metadata": metadata,
                    "source_metadata": source_metadata,
                    "source_types": source_types,
                    "stream": stream,
                    "tag_filter_logic": tag_filter_logic,
                    "tag_ids": tag_ids,
                    "tags": tags,
                },
                client_completion_params.ClientCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionResponse,
        )

    def content(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Content:
        """<p> Get through indexed content.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self.get(
            path_template("/contents/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Content,
        )

    def extract(
        self,
        *,
        schema: object,
        chunk_metadata: MetadataFilterGroup | Omit = omit,
        date_from: int | Omit = omit,
        date_to: int | Omit = omit,
        domains: SequenceNotStr[str] | Omit = omit,
        file_types: List[FileType] | Omit = omit,
        limit: int | Omit = omit,
        metadata: MetadataFilterGroup | Omit = omit,
        offset: int | Omit = omit,
        prompt: str | Omit = omit,
        related_filter: client_extract_params.RelatedFilter | Omit = omit,
        source_metadata: MetadataFilterGroup | Omit = omit,
        source_types: List[SourceType] | Omit = omit,
        tag_filter_logic: LogicalOperator | Omit = omit,
        tag_ids: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        use_related: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractResponse:
        """
        <p> Performs data extraction using LLM based on the specified data source, filter conditions, and JSON schema. Retrieves chunked data and uses the schema to extract and return the result as JSON via LLM. </p> <p> Required roles: All, App </p>

        Args:
          schema: JSON Schema for the data to be extracted.

          chunk_metadata: Filter by chunk-level metadata from chunk_metadatas table

          date_from: Start date for content search (Unix timestamp in seconds)

          date_to: End date for content search (Unix timestamp in seconds)

          metadata: (reserved for future use) Filter group with nested structure. Supports combining
              filters with AND/OR logic.

          prompt: Additional prompt for the LLM (optional, if not specified, a default prompt in
              Japanese will be used).

          source_metadata: Filter by individual source/file metadata from source_metadatas table

          tag_filter_logic: Logical operator for combining filter conditions

          use_related: Whether to search for and use related content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/extract",
            body=maybe_transform(
                {
                    "schema": schema,
                    "chunk_metadata": chunk_metadata,
                    "date_from": date_from,
                    "date_to": date_to,
                    "domains": domains,
                    "file_types": file_types,
                    "limit": limit,
                    "metadata": metadata,
                    "offset": offset,
                    "prompt": prompt,
                    "related_filter": related_filter,
                    "source_metadata": source_metadata,
                    "source_types": source_types,
                    "tag_filter_logic": tag_filter_logic,
                    "tag_ids": tag_ids,
                    "tags": tags,
                    "use_related": use_related,
                },
                client_extract_params.ClientExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    def search(
        self,
        *,
        query: str,
        chunk_metadata: MetadataFilterGroup | Omit = omit,
        date_from: int | Omit = omit,
        date_to: int | Omit = omit,
        domains: SequenceNotStr[str] | Omit = omit,
        file_types: List[FileType] | Omit = omit,
        limit: int | Omit = omit,
        metadata: MetadataFilterGroup | Omit = omit,
        offset: int | Omit = omit,
        source_metadata: MetadataFilterGroup | Omit = omit,
        source_types: List[SourceType] | Omit = omit,
        tag_filter_logic: LogicalOperator | Omit = omit,
        tag_ids: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """<p> Searches through indexed content using query.

        </p> <p> Required roles: All, App </p>

        Args:
          query: Search query string

          chunk_metadata: Filter by chunk-level metadata from chunk_metadatas table

          date_from: Start date for content search (Unix timestamp in seconds)

          date_to: End date for content search (Unix timestamp in seconds)

          domains: Array of domains to search within (supports partial matching)

          limit: Maximum number of results to return

          metadata: (reserved for future use) Filter group with nested structure. Supports combining
              filters with AND/OR logic.

          offset: Number of results to skip

          source_metadata: Filter by individual source/file metadata from source_metadatas table

          tag_filter_logic: Logical operator for combining filter conditions

          tag_ids: target tag IDs to be obtained

          tags: target tag names to be obtained

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/search",
            body=maybe_transform(
                {
                    "query": query,
                    "chunk_metadata": chunk_metadata,
                    "date_from": date_from,
                    "date_to": date_to,
                    "domains": domains,
                    "file_types": file_types,
                    "limit": limit,
                    "metadata": metadata,
                    "offset": offset,
                    "source_metadata": source_metadata,
                    "source_types": source_types,
                    "tag_filter_logic": tag_filter_logic,
                    "tag_ids": tag_ids,
                    "tags": tags,
                },
                client_search_params.ClientSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResponse,
        )

    def tags(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagsResponse:
        """<p> Returns the list of tags. </p> <p> Required roles: All, App </p>"""
        return self.get(
            "/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagsResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncQaip(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncQaip client instance.

        This automatically infers the `api_key` argument from the `QAIP_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("QAIP_API_KEY")
        if api_key is None:
            raise QaipError(
                "The api_key client option must be set either by passing api_key to the client or by setting the QAIP_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("QAIP_BASE_URL")
        if base_url is None:
            base_url = f"https://developer.qaip.com/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def agent(self) -> AsyncAgentResource:
        """(Experimental) Agent operations"""
        from .resources.agent import AsyncAgentResource

        return AsyncAgentResource(self)

    @cached_property
    def tag_source_groups(self) -> AsyncTagSourceGroupsResource:
        """Tag and source group associations"""
        from .resources.tag_source_groups import AsyncTagSourceGroupsResource

        return AsyncTagSourceGroupsResource(self)

    @cached_property
    def source_groups(self) -> AsyncSourceGroupsResource:
        """Source group (job) management and metadata"""
        from .resources.source_groups import AsyncSourceGroupsResource

        return AsyncSourceGroupsResource(self)

    @cached_property
    def sources(self) -> AsyncSourcesResource:
        """Sources management and metadata"""
        from .resources.sources import AsyncSourcesResource

        return AsyncSourcesResource(self)

    @cached_property
    def local_file_groups(self) -> AsyncLocalFileGroupsResource:
        """Local file group management"""
        from .resources.local_file_groups import AsyncLocalFileGroupsResource

        return AsyncLocalFileGroupsResource(self)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        """Secret management"""
        from .resources.secrets import AsyncSecretsResource

        return AsyncSecretsResource(self)

    @cached_property
    def google_drives(self) -> AsyncGoogleDrivesResource:
        from .resources.google_drives import AsyncGoogleDrivesResource

        return AsyncGoogleDrivesResource(self)

    @cached_property
    def crawls(self) -> AsyncCrawlsResource:
        from .resources.crawls import AsyncCrawlsResource

        return AsyncCrawlsResource(self)

    @cached_property
    def githubs(self) -> AsyncGithubsResource:
        from .resources.githubs import AsyncGithubsResource

        return AsyncGithubsResource(self)

    @cached_property
    def notions(self) -> AsyncNotionsResource:
        from .resources.notions import AsyncNotionsResource

        return AsyncNotionsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncQaipWithRawResponse:
        return AsyncQaipWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQaipWithStreamedResponse:
        return AsyncQaipWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def completion(
        self,
        *,
        messages: Iterable[client_completion_params.Message],
        chunk_metadata: MetadataFilterGroup | Omit = omit,
        citation: bool | Omit = omit,
        date_from: int | Omit = omit,
        date_to: int | Omit = omit,
        domains: SequenceNotStr[str] | Omit = omit,
        file_types: List[FileType] | Omit = omit,
        metadata: MetadataFilterGroup | Omit = omit,
        source_metadata: MetadataFilterGroup | Omit = omit,
        source_types: List[SourceType] | Omit = omit,
        stream: bool | Omit = omit,
        tag_filter_logic: LogicalOperator | Omit = omit,
        tag_ids: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionResponse:
        """<p> Generates a completion based on the input messages and retrieval chunks.

        If the 'stream' parameter is set to true, the response is returned as a stream of plain text (text/plain). </p> <p> Required roles: All, App </p>

        Args:
          messages: The messages to generate completion for

          chunk_metadata: Filter by chunk-level metadata from chunk_metadatas table

          citation: Whether to include citations in the response

          date_from: Start date for content search (Unix timestamp in seconds)

          date_to: End date for content search (Unix timestamp in seconds)

          domains: Array of domains to search within (supports partial matching)

          metadata: (reserved for future use) Filter group with nested structure. Supports combining
              filters with AND/OR logic.

          source_metadata: Filter by individual source/file metadata from source_metadatas table

          stream: Whether to stream the response. If true, the response is sent as a stream using
              the 'text/plain' content type.

          tag_filter_logic: Logical operator for combining filter conditions

          tag_ids: target tag IDs to be obtained

          tags: target tag names to be obtained

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "chunk_metadata": chunk_metadata,
                    "citation": citation,
                    "date_from": date_from,
                    "date_to": date_to,
                    "domains": domains,
                    "file_types": file_types,
                    "metadata": metadata,
                    "source_metadata": source_metadata,
                    "source_types": source_types,
                    "stream": stream,
                    "tag_filter_logic": tag_filter_logic,
                    "tag_ids": tag_ids,
                    "tags": tags,
                },
                client_completion_params.ClientCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionResponse,
        )

    async def content(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Content:
        """<p> Get through indexed content.

        </p> <p> Required roles: All, App </p>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self.get(
            path_template("/contents/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Content,
        )

    async def extract(
        self,
        *,
        schema: object,
        chunk_metadata: MetadataFilterGroup | Omit = omit,
        date_from: int | Omit = omit,
        date_to: int | Omit = omit,
        domains: SequenceNotStr[str] | Omit = omit,
        file_types: List[FileType] | Omit = omit,
        limit: int | Omit = omit,
        metadata: MetadataFilterGroup | Omit = omit,
        offset: int | Omit = omit,
        prompt: str | Omit = omit,
        related_filter: client_extract_params.RelatedFilter | Omit = omit,
        source_metadata: MetadataFilterGroup | Omit = omit,
        source_types: List[SourceType] | Omit = omit,
        tag_filter_logic: LogicalOperator | Omit = omit,
        tag_ids: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        use_related: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractResponse:
        """
        <p> Performs data extraction using LLM based on the specified data source, filter conditions, and JSON schema. Retrieves chunked data and uses the schema to extract and return the result as JSON via LLM. </p> <p> Required roles: All, App </p>

        Args:
          schema: JSON Schema for the data to be extracted.

          chunk_metadata: Filter by chunk-level metadata from chunk_metadatas table

          date_from: Start date for content search (Unix timestamp in seconds)

          date_to: End date for content search (Unix timestamp in seconds)

          metadata: (reserved for future use) Filter group with nested structure. Supports combining
              filters with AND/OR logic.

          prompt: Additional prompt for the LLM (optional, if not specified, a default prompt in
              Japanese will be used).

          source_metadata: Filter by individual source/file metadata from source_metadatas table

          tag_filter_logic: Logical operator for combining filter conditions

          use_related: Whether to search for and use related content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/extract",
            body=await async_maybe_transform(
                {
                    "schema": schema,
                    "chunk_metadata": chunk_metadata,
                    "date_from": date_from,
                    "date_to": date_to,
                    "domains": domains,
                    "file_types": file_types,
                    "limit": limit,
                    "metadata": metadata,
                    "offset": offset,
                    "prompt": prompt,
                    "related_filter": related_filter,
                    "source_metadata": source_metadata,
                    "source_types": source_types,
                    "tag_filter_logic": tag_filter_logic,
                    "tag_ids": tag_ids,
                    "tags": tags,
                    "use_related": use_related,
                },
                client_extract_params.ClientExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    async def search(
        self,
        *,
        query: str,
        chunk_metadata: MetadataFilterGroup | Omit = omit,
        date_from: int | Omit = omit,
        date_to: int | Omit = omit,
        domains: SequenceNotStr[str] | Omit = omit,
        file_types: List[FileType] | Omit = omit,
        limit: int | Omit = omit,
        metadata: MetadataFilterGroup | Omit = omit,
        offset: int | Omit = omit,
        source_metadata: MetadataFilterGroup | Omit = omit,
        source_types: List[SourceType] | Omit = omit,
        tag_filter_logic: LogicalOperator | Omit = omit,
        tag_ids: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """<p> Searches through indexed content using query.

        </p> <p> Required roles: All, App </p>

        Args:
          query: Search query string

          chunk_metadata: Filter by chunk-level metadata from chunk_metadatas table

          date_from: Start date for content search (Unix timestamp in seconds)

          date_to: End date for content search (Unix timestamp in seconds)

          domains: Array of domains to search within (supports partial matching)

          limit: Maximum number of results to return

          metadata: (reserved for future use) Filter group with nested structure. Supports combining
              filters with AND/OR logic.

          offset: Number of results to skip

          source_metadata: Filter by individual source/file metadata from source_metadatas table

          tag_filter_logic: Logical operator for combining filter conditions

          tag_ids: target tag IDs to be obtained

          tags: target tag names to be obtained

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "chunk_metadata": chunk_metadata,
                    "date_from": date_from,
                    "date_to": date_to,
                    "domains": domains,
                    "file_types": file_types,
                    "limit": limit,
                    "metadata": metadata,
                    "offset": offset,
                    "source_metadata": source_metadata,
                    "source_types": source_types,
                    "tag_filter_logic": tag_filter_logic,
                    "tag_ids": tag_ids,
                    "tags": tags,
                },
                client_search_params.ClientSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResponse,
        )

    async def tags(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagsResponse:
        """<p> Returns the list of tags. </p> <p> Required roles: All, App </p>"""
        return await self.get(
            "/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagsResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class QaipWithRawResponse:
    _client: Qaip

    def __init__(self, client: Qaip) -> None:
        self._client = client

        self.completion = to_raw_response_wrapper(
            client.completion,
        )
        self.content = to_raw_response_wrapper(
            client.content,
        )
        self.extract = to_raw_response_wrapper(
            client.extract,
        )
        self.search = to_raw_response_wrapper(
            client.search,
        )
        self.tags = to_raw_response_wrapper(
            client.tags,
        )

    @cached_property
    def agent(self) -> agent.AgentResourceWithRawResponse:
        """(Experimental) Agent operations"""
        from .resources.agent import AgentResourceWithRawResponse

        return AgentResourceWithRawResponse(self._client.agent)

    @cached_property
    def tag_source_groups(self) -> tag_source_groups.TagSourceGroupsResourceWithRawResponse:
        """Tag and source group associations"""
        from .resources.tag_source_groups import TagSourceGroupsResourceWithRawResponse

        return TagSourceGroupsResourceWithRawResponse(self._client.tag_source_groups)

    @cached_property
    def source_groups(self) -> source_groups.SourceGroupsResourceWithRawResponse:
        """Source group (job) management and metadata"""
        from .resources.source_groups import SourceGroupsResourceWithRawResponse

        return SourceGroupsResourceWithRawResponse(self._client.source_groups)

    @cached_property
    def sources(self) -> sources.SourcesResourceWithRawResponse:
        """Sources management and metadata"""
        from .resources.sources import SourcesResourceWithRawResponse

        return SourcesResourceWithRawResponse(self._client.sources)

    @cached_property
    def local_file_groups(self) -> local_file_groups.LocalFileGroupsResourceWithRawResponse:
        """Local file group management"""
        from .resources.local_file_groups import LocalFileGroupsResourceWithRawResponse

        return LocalFileGroupsResourceWithRawResponse(self._client.local_file_groups)

    @cached_property
    def secrets(self) -> secrets.SecretsResourceWithRawResponse:
        """Secret management"""
        from .resources.secrets import SecretsResourceWithRawResponse

        return SecretsResourceWithRawResponse(self._client.secrets)

    @cached_property
    def google_drives(self) -> google_drives.GoogleDrivesResourceWithRawResponse:
        from .resources.google_drives import GoogleDrivesResourceWithRawResponse

        return GoogleDrivesResourceWithRawResponse(self._client.google_drives)

    @cached_property
    def crawls(self) -> crawls.CrawlsResourceWithRawResponse:
        from .resources.crawls import CrawlsResourceWithRawResponse

        return CrawlsResourceWithRawResponse(self._client.crawls)

    @cached_property
    def githubs(self) -> githubs.GithubsResourceWithRawResponse:
        from .resources.githubs import GithubsResourceWithRawResponse

        return GithubsResourceWithRawResponse(self._client.githubs)

    @cached_property
    def notions(self) -> notions.NotionsResourceWithRawResponse:
        from .resources.notions import NotionsResourceWithRawResponse

        return NotionsResourceWithRawResponse(self._client.notions)


class AsyncQaipWithRawResponse:
    _client: AsyncQaip

    def __init__(self, client: AsyncQaip) -> None:
        self._client = client

        self.completion = async_to_raw_response_wrapper(
            client.completion,
        )
        self.content = async_to_raw_response_wrapper(
            client.content,
        )
        self.extract = async_to_raw_response_wrapper(
            client.extract,
        )
        self.search = async_to_raw_response_wrapper(
            client.search,
        )
        self.tags = async_to_raw_response_wrapper(
            client.tags,
        )

    @cached_property
    def agent(self) -> agent.AsyncAgentResourceWithRawResponse:
        """(Experimental) Agent operations"""
        from .resources.agent import AsyncAgentResourceWithRawResponse

        return AsyncAgentResourceWithRawResponse(self._client.agent)

    @cached_property
    def tag_source_groups(self) -> tag_source_groups.AsyncTagSourceGroupsResourceWithRawResponse:
        """Tag and source group associations"""
        from .resources.tag_source_groups import AsyncTagSourceGroupsResourceWithRawResponse

        return AsyncTagSourceGroupsResourceWithRawResponse(self._client.tag_source_groups)

    @cached_property
    def source_groups(self) -> source_groups.AsyncSourceGroupsResourceWithRawResponse:
        """Source group (job) management and metadata"""
        from .resources.source_groups import AsyncSourceGroupsResourceWithRawResponse

        return AsyncSourceGroupsResourceWithRawResponse(self._client.source_groups)

    @cached_property
    def sources(self) -> sources.AsyncSourcesResourceWithRawResponse:
        """Sources management and metadata"""
        from .resources.sources import AsyncSourcesResourceWithRawResponse

        return AsyncSourcesResourceWithRawResponse(self._client.sources)

    @cached_property
    def local_file_groups(self) -> local_file_groups.AsyncLocalFileGroupsResourceWithRawResponse:
        """Local file group management"""
        from .resources.local_file_groups import AsyncLocalFileGroupsResourceWithRawResponse

        return AsyncLocalFileGroupsResourceWithRawResponse(self._client.local_file_groups)

    @cached_property
    def secrets(self) -> secrets.AsyncSecretsResourceWithRawResponse:
        """Secret management"""
        from .resources.secrets import AsyncSecretsResourceWithRawResponse

        return AsyncSecretsResourceWithRawResponse(self._client.secrets)

    @cached_property
    def google_drives(self) -> google_drives.AsyncGoogleDrivesResourceWithRawResponse:
        from .resources.google_drives import AsyncGoogleDrivesResourceWithRawResponse

        return AsyncGoogleDrivesResourceWithRawResponse(self._client.google_drives)

    @cached_property
    def crawls(self) -> crawls.AsyncCrawlsResourceWithRawResponse:
        from .resources.crawls import AsyncCrawlsResourceWithRawResponse

        return AsyncCrawlsResourceWithRawResponse(self._client.crawls)

    @cached_property
    def githubs(self) -> githubs.AsyncGithubsResourceWithRawResponse:
        from .resources.githubs import AsyncGithubsResourceWithRawResponse

        return AsyncGithubsResourceWithRawResponse(self._client.githubs)

    @cached_property
    def notions(self) -> notions.AsyncNotionsResourceWithRawResponse:
        from .resources.notions import AsyncNotionsResourceWithRawResponse

        return AsyncNotionsResourceWithRawResponse(self._client.notions)


class QaipWithStreamedResponse:
    _client: Qaip

    def __init__(self, client: Qaip) -> None:
        self._client = client

        self.completion = to_streamed_response_wrapper(
            client.completion,
        )
        self.content = to_streamed_response_wrapper(
            client.content,
        )
        self.extract = to_streamed_response_wrapper(
            client.extract,
        )
        self.search = to_streamed_response_wrapper(
            client.search,
        )
        self.tags = to_streamed_response_wrapper(
            client.tags,
        )

    @cached_property
    def agent(self) -> agent.AgentResourceWithStreamingResponse:
        """(Experimental) Agent operations"""
        from .resources.agent import AgentResourceWithStreamingResponse

        return AgentResourceWithStreamingResponse(self._client.agent)

    @cached_property
    def tag_source_groups(self) -> tag_source_groups.TagSourceGroupsResourceWithStreamingResponse:
        """Tag and source group associations"""
        from .resources.tag_source_groups import TagSourceGroupsResourceWithStreamingResponse

        return TagSourceGroupsResourceWithStreamingResponse(self._client.tag_source_groups)

    @cached_property
    def source_groups(self) -> source_groups.SourceGroupsResourceWithStreamingResponse:
        """Source group (job) management and metadata"""
        from .resources.source_groups import SourceGroupsResourceWithStreamingResponse

        return SourceGroupsResourceWithStreamingResponse(self._client.source_groups)

    @cached_property
    def sources(self) -> sources.SourcesResourceWithStreamingResponse:
        """Sources management and metadata"""
        from .resources.sources import SourcesResourceWithStreamingResponse

        return SourcesResourceWithStreamingResponse(self._client.sources)

    @cached_property
    def local_file_groups(self) -> local_file_groups.LocalFileGroupsResourceWithStreamingResponse:
        """Local file group management"""
        from .resources.local_file_groups import LocalFileGroupsResourceWithStreamingResponse

        return LocalFileGroupsResourceWithStreamingResponse(self._client.local_file_groups)

    @cached_property
    def secrets(self) -> secrets.SecretsResourceWithStreamingResponse:
        """Secret management"""
        from .resources.secrets import SecretsResourceWithStreamingResponse

        return SecretsResourceWithStreamingResponse(self._client.secrets)

    @cached_property
    def google_drives(self) -> google_drives.GoogleDrivesResourceWithStreamingResponse:
        from .resources.google_drives import GoogleDrivesResourceWithStreamingResponse

        return GoogleDrivesResourceWithStreamingResponse(self._client.google_drives)

    @cached_property
    def crawls(self) -> crawls.CrawlsResourceWithStreamingResponse:
        from .resources.crawls import CrawlsResourceWithStreamingResponse

        return CrawlsResourceWithStreamingResponse(self._client.crawls)

    @cached_property
    def githubs(self) -> githubs.GithubsResourceWithStreamingResponse:
        from .resources.githubs import GithubsResourceWithStreamingResponse

        return GithubsResourceWithStreamingResponse(self._client.githubs)

    @cached_property
    def notions(self) -> notions.NotionsResourceWithStreamingResponse:
        from .resources.notions import NotionsResourceWithStreamingResponse

        return NotionsResourceWithStreamingResponse(self._client.notions)


class AsyncQaipWithStreamedResponse:
    _client: AsyncQaip

    def __init__(self, client: AsyncQaip) -> None:
        self._client = client

        self.completion = async_to_streamed_response_wrapper(
            client.completion,
        )
        self.content = async_to_streamed_response_wrapper(
            client.content,
        )
        self.extract = async_to_streamed_response_wrapper(
            client.extract,
        )
        self.search = async_to_streamed_response_wrapper(
            client.search,
        )
        self.tags = async_to_streamed_response_wrapper(
            client.tags,
        )

    @cached_property
    def agent(self) -> agent.AsyncAgentResourceWithStreamingResponse:
        """(Experimental) Agent operations"""
        from .resources.agent import AsyncAgentResourceWithStreamingResponse

        return AsyncAgentResourceWithStreamingResponse(self._client.agent)

    @cached_property
    def tag_source_groups(self) -> tag_source_groups.AsyncTagSourceGroupsResourceWithStreamingResponse:
        """Tag and source group associations"""
        from .resources.tag_source_groups import AsyncTagSourceGroupsResourceWithStreamingResponse

        return AsyncTagSourceGroupsResourceWithStreamingResponse(self._client.tag_source_groups)

    @cached_property
    def source_groups(self) -> source_groups.AsyncSourceGroupsResourceWithStreamingResponse:
        """Source group (job) management and metadata"""
        from .resources.source_groups import AsyncSourceGroupsResourceWithStreamingResponse

        return AsyncSourceGroupsResourceWithStreamingResponse(self._client.source_groups)

    @cached_property
    def sources(self) -> sources.AsyncSourcesResourceWithStreamingResponse:
        """Sources management and metadata"""
        from .resources.sources import AsyncSourcesResourceWithStreamingResponse

        return AsyncSourcesResourceWithStreamingResponse(self._client.sources)

    @cached_property
    def local_file_groups(self) -> local_file_groups.AsyncLocalFileGroupsResourceWithStreamingResponse:
        """Local file group management"""
        from .resources.local_file_groups import AsyncLocalFileGroupsResourceWithStreamingResponse

        return AsyncLocalFileGroupsResourceWithStreamingResponse(self._client.local_file_groups)

    @cached_property
    def secrets(self) -> secrets.AsyncSecretsResourceWithStreamingResponse:
        """Secret management"""
        from .resources.secrets import AsyncSecretsResourceWithStreamingResponse

        return AsyncSecretsResourceWithStreamingResponse(self._client.secrets)

    @cached_property
    def google_drives(self) -> google_drives.AsyncGoogleDrivesResourceWithStreamingResponse:
        from .resources.google_drives import AsyncGoogleDrivesResourceWithStreamingResponse

        return AsyncGoogleDrivesResourceWithStreamingResponse(self._client.google_drives)

    @cached_property
    def crawls(self) -> crawls.AsyncCrawlsResourceWithStreamingResponse:
        from .resources.crawls import AsyncCrawlsResourceWithStreamingResponse

        return AsyncCrawlsResourceWithStreamingResponse(self._client.crawls)

    @cached_property
    def githubs(self) -> githubs.AsyncGithubsResourceWithStreamingResponse:
        from .resources.githubs import AsyncGithubsResourceWithStreamingResponse

        return AsyncGithubsResourceWithStreamingResponse(self._client.githubs)

    @cached_property
    def notions(self) -> notions.AsyncNotionsResourceWithStreamingResponse:
        from .resources.notions import AsyncNotionsResourceWithStreamingResponse

        return AsyncNotionsResourceWithStreamingResponse(self._client.notions)


Client = Qaip

AsyncClient = AsyncQaip
