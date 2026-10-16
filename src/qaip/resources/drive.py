# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Iterable

import httpx

from ..types import (
    drive_search_params,
    drive_list_files_params,
    drive_list_folders_params,
    drive_list_displays_params,
    drive_list_revisions_params,
    drive_create_transfer_params,
    drive_complete_transfer_params,
    drive_download_original_params,
    drive_retrieve_references_params,
)
from .._files import read_file_content, async_read_file_content
from .._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    BinaryTypes,
    FileContent,
    AsyncBinaryTypes,
    omit,
    not_given,
)
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..types.file import File
from ..types.files import Files
from .._base_client import make_request_options
from ..types.folders import Folders
from ..types.displays import Displays
from ..types.transfer import Transfer
from ..types.revisions import Revisions
from ..types.references import References
from ..types.part_receipt import PartReceipt
from ..types.search_response import SearchResponse
from ..types.display_manifest import DisplayManifest
from ..types.reference_source_param import ReferenceSourceParam
from ..types.complete_transfer_request_param import CompleteTransferRequestParam

__all__ = ["DriveResource", "AsyncDriveResource"]


class DriveResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DriveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return DriveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DriveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return DriveResourceWithStreamingResponse(self)

    def complete_transfer(
        self,
        transfer_id: str,
        *,
        complete_transfer_request: CompleteTransferRequestParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transfer:
        """
        Send an empty JSON object after every expected part has a persisted receipt.
        Completion queues verification; poll until committed or terminal failure.
        Current create and completion permissions are rechecked before the worker
        publishes a revision. Repeating completion does not create another revision.
        Requires a currently active agent connection bound to the authenticated API
        credential. Reference scope and new-output destination are separate; destination
        access does not grant source access.

        Args:
          transfer_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transfer_id:
            raise ValueError(f"Expected a non-empty value for `transfer_id` but received {transfer_id!r}")
        return self._post(
            path_template("/drive/transfers/{transfer_id}/complete", transfer_id=transfer_id),
            body=maybe_transform(complete_transfer_request, drive_complete_transfer_params.DriveCompleteTransferParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
        )

    def create_transfer(
        self,
        *,
        folder_id: str,
        idempotency_key: str,
        media_type: str,
        name: str,
        sha256: str,
        size_bytes: int,
        references: Iterable[ReferenceSourceParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transfer:
        """
        Create or resume a Drive transfer Requires a currently active agent connection
        bound to the authenticated API credential. Reference scope and new-output
        destination are separate; destination access does not grant source access.

        Args:
          folder_id: Canonical lowercase nonzero UUID.

          idempotency_key: Canonical lowercase nonzero UUID.

          media_type: Valid MIME media type without parameters.

          name: Nonblank file or folder name; no slash, backslash, control characters, . or .. .

          references: Optional agent-declared sources. Omitted and empty references are equivalent.
              Sources require current read authorization as well as source scope. All tuples
              are validated before transfer creation and before publication. Removing
              references permits saving an unrecorded output.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/drive/transfers",
            body=maybe_transform(
                {
                    "folder_id": folder_id,
                    "idempotency_key": idempotency_key,
                    "media_type": media_type,
                    "name": name,
                    "sha256": sha256,
                    "size_bytes": size_bytes,
                    "references": references,
                },
                drive_create_transfer_params.DriveCreateTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
        )

    def download_original(
        self,
        file_id: str,
        *,
        revision_id: str,
        range: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Pin revision_id when resuming across requests; omitted means the current
        revision at admission. GET supports one byte range (including suffix ranges).
        HEAD returns whole-original metadata and ignores Range. Stream GET to a file
        without buffering the original. If the transport closes, restart with Range and
        the same revision_id. Access and trash state are checked during delivery;
        revoked access aborts the stream. The shared internal transport limits a
        connection to 10 minutes, so large originals require bounded Range requests.
        Requires a currently active agent connection bound to the authenticated API
        credential. Reference scope and new-output destination are separate; destination
        access does not grant source access.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          revision_id: Fixed original revision ID returned by an allowed file lookup. A mismatched or
              unavailable revision is denied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Range": range}), **(extra_headers or {})}
        return self._get(
            path_template("/drive/files/{file_id}/original", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"revision_id": revision_id}, drive_download_original_params.DriveDownloadOriginalParams
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def download_page_png(
        self,
        page_id: str,
        *,
        file_id: str,
        display_id: str,
        range: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Returns the immutable page asset for the exact file/display/page tuple.

        GET
        supports a single byte Range and verifies the whole fixed asset hash before
        sending any bytes; HEAD ignores Range. The server rechecks current authorization
        and agent scope before return and during delivery. PNG/SVG assets are limited to
        32 MiB. Keys and S3 VersionIds are private. Resume with the same tuple; original
        updates never substitute another page.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          display_id: Canonical lowercase nonzero UUID.

          page_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        if not display_id:
            raise ValueError(f"Expected a non-empty value for `display_id` but received {display_id!r}")
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Range": range}), **(extra_headers or {})}
        return self._get(
            path_template(
                "/drive/files/{file_id}/displays/{display_id}/pages/{page_id}/png",
                file_id=file_id,
                display_id=display_id,
                page_id=page_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def download_page_svg(
        self,
        page_id: str,
        *,
        file_id: str,
        display_id: str,
        range: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Returns the immutable page asset for the exact file/display/page tuple.

        GET
        supports a single byte Range and verifies the whole fixed asset hash before
        sending any bytes; HEAD ignores Range. The server rechecks current authorization
        and agent scope before return and during delivery. PNG/SVG assets are limited to
        32 MiB. Keys and S3 VersionIds are private. Resume with the same tuple; original
        updates never substitute another page.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          display_id: Canonical lowercase nonzero UUID.

          page_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        if not display_id:
            raise ValueError(f"Expected a non-empty value for `display_id` but received {display_id!r}")
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        extra_headers = {"Accept": "image/svg+xml", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Range": range}), **(extra_headers or {})}
        return self._get(
            path_template(
                "/drive/files/{file_id}/displays/{display_id}/pages/{page_id}/svg",
                file_id=file_id,
                display_id=display_id,
                page_id=page_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def list_displays(
        self,
        file_id: str,
        *,
        revision_id: str,
        after_id: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Displays:
        """Fixed original/display/page IDs are immutable.

        Current app, credential, resource
        permissions and agent reference scope are checked before returning data.
        Unknown, mismatched and inaccessible tuples return the same access_denied error
        without source details. Storage keys and S3 VersionIds are never returned.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          revision_id: Canonical lowercase nonzero UUID.

          after_id: Exclusive last returned ID. Results are in ascending UUID order; an empty page
              ends the scan.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            path_template("/drive/files/{file_id}/displays", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "revision_id": revision_id,
                        "after_id": after_id,
                        "limit": limit,
                    },
                    drive_list_displays_params.DriveListDisplaysParams,
                ),
            ),
            cast_to=Displays,
        )

    def list_files(
        self,
        *,
        after_id: str | Omit = omit,
        all_folders: bool | Omit = omit,
        folder_id: str | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Files:
        """
        Lists files by name within the current agent connection reference scope and
        current resource permissions. Filtering happens before pagination. Omit
        folder_id for root files, or use all_folders=true to find allowed files across
        folders. Duplicate or unknown query fields are rejected. An unknown, expired or
        revoked connection is denied. Use pagination.next_id for the next request.
        Requires a currently active agent connection bound to the authenticated API
        credential. Reference scope and new-output destination are separate; destination
        access does not grant source access.

        Args:
          after_id: Exclusive last returned ID. Results are in ascending UUID order; an empty page
              ends the scan.

          folder_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/drive/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_id": after_id,
                        "all_folders": all_folders,
                        "folder_id": folder_id,
                        "limit": limit,
                        "q": q,
                    },
                    drive_list_files_params.DriveListFilesParams,
                ),
            ),
            cast_to=Files,
        )

    def list_folders(
        self,
        *,
        after_id: str | Omit = omit,
        limit: int | Omit = omit,
        parent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folders:
        """
        List Drive folders Requires a currently active agent connection bound to the
        authenticated API credential. Reference scope and new-output destination are
        separate; destination access does not grant source access.

        Args:
          after_id: Exclusive last returned ID. Results are in ascending UUID order; an empty page
              ends the scan.

          parent_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/drive/folders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_id": after_id,
                        "limit": limit,
                        "parent_id": parent_id,
                    },
                    drive_list_folders_params.DriveListFoldersParams,
                ),
            ),
            cast_to=Folders,
        )

    def list_revisions(
        self,
        file_id: str,
        *,
        after_id: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Revisions:
        """
        List fixed Drive revisions Requires a currently active agent connection bound to
        the authenticated API credential. Reference scope and new-output destination are
        separate; destination access does not grant source access.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          after_id: Exclusive last returned ID. Results are in ascending UUID order; an empty page
              ends the scan.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            path_template("/drive/files/{file_id}/revisions", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_id": after_id,
                        "limit": limit,
                    },
                    drive_list_revisions_params.DriveListRevisionsParams,
                ),
            ),
            cast_to=Revisions,
        )

    def retrieve_display(
        self,
        display_id: str,
        *,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DisplayManifest:
        """Fixed original/display/page IDs are immutable.

        Current app, credential, resource
        permissions and agent reference scope are checked before returning data.
        Unknown, mismatched and inaccessible tuples return the same access_denied error
        without source details. Storage keys and S3 VersionIds are never returned.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          display_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        if not display_id:
            raise ValueError(f"Expected a non-empty value for `display_id` but received {display_id!r}")
        return self._get(
            path_template("/drive/files/{file_id}/displays/{display_id}", file_id=file_id, display_id=display_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisplayManifest,
        )

    def retrieve_file(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Get Drive file metadata Requires a currently active agent connection bound to
        the authenticated API credential. Reference scope and new-output destination are
        separate; destination access does not grant source access.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            path_template("/drive/files/{file_id}", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    def retrieve_references(
        self,
        file_id: str,
        *,
        revision_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> References:
        """
        Requires a fixed output revision_id and current reference permission on the
        output. Sources are agent claims, not independent proof that the agent read
        them. Output access never grants access to source material. Each source is
        checked independently against current connection scope, resource permission and
        fixed revision/display/page correspondence. Unavailable sources return only
        ordinal/status, without source IDs, names or content. recorded=false means no
        source information was provided.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          revision_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            path_template("/drive/files/{file_id}/references", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"revision_id": revision_id}, drive_retrieve_references_params.DriveRetrieveReferencesParams
                ),
            ),
            cast_to=References,
        )

    def retrieve_transfer(
        self,
        transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transfer:
        """
        Get a Drive transfer and persisted part receipts Requires a currently active
        agent connection bound to the authenticated API credential. Reference scope and
        new-output destination are separate; destination access does not grant source
        access.

        Args:
          transfer_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transfer_id:
            raise ValueError(f"Expected a non-empty value for `transfer_id` but received {transfer_id!r}")
        return self._get(
            path_template("/drive/transfers/{transfer_id}", transfer_id=transfer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
        )

    def search(
        self,
        *,
        query: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Searches currently authorized published analysis generations without requiring
        file IDs. The server fixes the complete allowed revision scope before retrieval
        and validates evidence against Drive metadata and content hashes. Permission or
        publication changes abort the response. Results include a matching reason and
        fixed original, display, page and analysis IDs. Search examines at most 1000
        ranked chunks; search_truncated reports this boundary. pending_analysis_count
        counts currently accessible originals without a published analysis. Pagination
        uses pagination.next_offset, rather than the file-list UUID cursor. Repeating a
        search reevaluates current permissions and content. The query, vectors, tables,
        tenant and actor cannot change the authorized scope.

        Args:
          query: Natural-language information need. Whitespace-only queries are rejected.

          offset: Use pagination.next_offset from the preceding response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/drive/search",
            body=maybe_transform(
                {
                    "query": query,
                    "limit": limit,
                    "offset": offset,
                },
                drive_search_params.DriveSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResponse,
        )

    def upload_part(
        self,
        part_number: int,
        body: FileContent | BinaryTypes,
        *,
        transfer_id: str,
        x_drive_sha256: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartReceipt:
        """Streams one part.

        Use the returned part_size and declared original size to
        determine the exact length; only the final part may be smaller. SHA-256 is
        checked against the received bytes before a receipt is persisted. The same part
        number, size and hash are idempotent; changed input returns 409.
        Transfer-Encoding is not accepted. After interruption, fetch receipts and resend
        only missing parts with the same current credential. Requires a currently active
        agent connection bound to the authenticated API credential. Reference scope and
        new-output destination are separate; destination access does not grant source
        access.

        Args:
          transfer_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transfer_id:
            raise ValueError(f"Expected a non-empty value for `transfer_id` but received {transfer_id!r}")
        extra_headers = {"X-Drive-SHA256": x_drive_sha256, **(extra_headers or {})}
        extra_headers["Content-Type"] = "application/octet-stream"
        return self._put(
            path_template(
                "/drive/transfers/{transfer_id}/parts/{part_number}", transfer_id=transfer_id, part_number=part_number
            ),
            content=read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PartReceipt,
        )


class AsyncDriveResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDriveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qlonolink/qaip-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDriveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDriveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qlonolink/qaip-python#with_streaming_response
        """
        return AsyncDriveResourceWithStreamingResponse(self)

    async def complete_transfer(
        self,
        transfer_id: str,
        *,
        complete_transfer_request: CompleteTransferRequestParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transfer:
        """
        Send an empty JSON object after every expected part has a persisted receipt.
        Completion queues verification; poll until committed or terminal failure.
        Current create and completion permissions are rechecked before the worker
        publishes a revision. Repeating completion does not create another revision.
        Requires a currently active agent connection bound to the authenticated API
        credential. Reference scope and new-output destination are separate; destination
        access does not grant source access.

        Args:
          transfer_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transfer_id:
            raise ValueError(f"Expected a non-empty value for `transfer_id` but received {transfer_id!r}")
        return await self._post(
            path_template("/drive/transfers/{transfer_id}/complete", transfer_id=transfer_id),
            body=await async_maybe_transform(
                complete_transfer_request, drive_complete_transfer_params.DriveCompleteTransferParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
        )

    async def create_transfer(
        self,
        *,
        folder_id: str,
        idempotency_key: str,
        media_type: str,
        name: str,
        sha256: str,
        size_bytes: int,
        references: Iterable[ReferenceSourceParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transfer:
        """
        Create or resume a Drive transfer Requires a currently active agent connection
        bound to the authenticated API credential. Reference scope and new-output
        destination are separate; destination access does not grant source access.

        Args:
          folder_id: Canonical lowercase nonzero UUID.

          idempotency_key: Canonical lowercase nonzero UUID.

          media_type: Valid MIME media type without parameters.

          name: Nonblank file or folder name; no slash, backslash, control characters, . or .. .

          references: Optional agent-declared sources. Omitted and empty references are equivalent.
              Sources require current read authorization as well as source scope. All tuples
              are validated before transfer creation and before publication. Removing
              references permits saving an unrecorded output.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/drive/transfers",
            body=await async_maybe_transform(
                {
                    "folder_id": folder_id,
                    "idempotency_key": idempotency_key,
                    "media_type": media_type,
                    "name": name,
                    "sha256": sha256,
                    "size_bytes": size_bytes,
                    "references": references,
                },
                drive_create_transfer_params.DriveCreateTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
        )

    async def download_original(
        self,
        file_id: str,
        *,
        revision_id: str,
        range: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Pin revision_id when resuming across requests; omitted means the current
        revision at admission. GET supports one byte range (including suffix ranges).
        HEAD returns whole-original metadata and ignores Range. Stream GET to a file
        without buffering the original. If the transport closes, restart with Range and
        the same revision_id. Access and trash state are checked during delivery;
        revoked access aborts the stream. The shared internal transport limits a
        connection to 10 minutes, so large originals require bounded Range requests.
        Requires a currently active agent connection bound to the authenticated API
        credential. Reference scope and new-output destination are separate; destination
        access does not grant source access.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          revision_id: Fixed original revision ID returned by an allowed file lookup. A mismatched or
              unavailable revision is denied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Range": range}), **(extra_headers or {})}
        return await self._get(
            path_template("/drive/files/{file_id}/original", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"revision_id": revision_id}, drive_download_original_params.DriveDownloadOriginalParams
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def download_page_png(
        self,
        page_id: str,
        *,
        file_id: str,
        display_id: str,
        range: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Returns the immutable page asset for the exact file/display/page tuple.

        GET
        supports a single byte Range and verifies the whole fixed asset hash before
        sending any bytes; HEAD ignores Range. The server rechecks current authorization
        and agent scope before return and during delivery. PNG/SVG assets are limited to
        32 MiB. Keys and S3 VersionIds are private. Resume with the same tuple; original
        updates never substitute another page.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          display_id: Canonical lowercase nonzero UUID.

          page_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        if not display_id:
            raise ValueError(f"Expected a non-empty value for `display_id` but received {display_id!r}")
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Range": range}), **(extra_headers or {})}
        return await self._get(
            path_template(
                "/drive/files/{file_id}/displays/{display_id}/pages/{page_id}/png",
                file_id=file_id,
                display_id=display_id,
                page_id=page_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def download_page_svg(
        self,
        page_id: str,
        *,
        file_id: str,
        display_id: str,
        range: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Returns the immutable page asset for the exact file/display/page tuple.

        GET
        supports a single byte Range and verifies the whole fixed asset hash before
        sending any bytes; HEAD ignores Range. The server rechecks current authorization
        and agent scope before return and during delivery. PNG/SVG assets are limited to
        32 MiB. Keys and S3 VersionIds are private. Resume with the same tuple; original
        updates never substitute another page.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          display_id: Canonical lowercase nonzero UUID.

          page_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        if not display_id:
            raise ValueError(f"Expected a non-empty value for `display_id` but received {display_id!r}")
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        extra_headers = {"Accept": "image/svg+xml", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Range": range}), **(extra_headers or {})}
        return await self._get(
            path_template(
                "/drive/files/{file_id}/displays/{display_id}/pages/{page_id}/svg",
                file_id=file_id,
                display_id=display_id,
                page_id=page_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def list_displays(
        self,
        file_id: str,
        *,
        revision_id: str,
        after_id: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Displays:
        """Fixed original/display/page IDs are immutable.

        Current app, credential, resource
        permissions and agent reference scope are checked before returning data.
        Unknown, mismatched and inaccessible tuples return the same access_denied error
        without source details. Storage keys and S3 VersionIds are never returned.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          revision_id: Canonical lowercase nonzero UUID.

          after_id: Exclusive last returned ID. Results are in ascending UUID order; an empty page
              ends the scan.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            path_template("/drive/files/{file_id}/displays", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "revision_id": revision_id,
                        "after_id": after_id,
                        "limit": limit,
                    },
                    drive_list_displays_params.DriveListDisplaysParams,
                ),
            ),
            cast_to=Displays,
        )

    async def list_files(
        self,
        *,
        after_id: str | Omit = omit,
        all_folders: bool | Omit = omit,
        folder_id: str | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Files:
        """
        Lists files by name within the current agent connection reference scope and
        current resource permissions. Filtering happens before pagination. Omit
        folder_id for root files, or use all_folders=true to find allowed files across
        folders. Duplicate or unknown query fields are rejected. An unknown, expired or
        revoked connection is denied. Use pagination.next_id for the next request.
        Requires a currently active agent connection bound to the authenticated API
        credential. Reference scope and new-output destination are separate; destination
        access does not grant source access.

        Args:
          after_id: Exclusive last returned ID. Results are in ascending UUID order; an empty page
              ends the scan.

          folder_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/drive/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after_id": after_id,
                        "all_folders": all_folders,
                        "folder_id": folder_id,
                        "limit": limit,
                        "q": q,
                    },
                    drive_list_files_params.DriveListFilesParams,
                ),
            ),
            cast_to=Files,
        )

    async def list_folders(
        self,
        *,
        after_id: str | Omit = omit,
        limit: int | Omit = omit,
        parent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Folders:
        """
        List Drive folders Requires a currently active agent connection bound to the
        authenticated API credential. Reference scope and new-output destination are
        separate; destination access does not grant source access.

        Args:
          after_id: Exclusive last returned ID. Results are in ascending UUID order; an empty page
              ends the scan.

          parent_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/drive/folders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after_id": after_id,
                        "limit": limit,
                        "parent_id": parent_id,
                    },
                    drive_list_folders_params.DriveListFoldersParams,
                ),
            ),
            cast_to=Folders,
        )

    async def list_revisions(
        self,
        file_id: str,
        *,
        after_id: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Revisions:
        """
        List fixed Drive revisions Requires a currently active agent connection bound to
        the authenticated API credential. Reference scope and new-output destination are
        separate; destination access does not grant source access.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          after_id: Exclusive last returned ID. Results are in ascending UUID order; an empty page
              ends the scan.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            path_template("/drive/files/{file_id}/revisions", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after_id": after_id,
                        "limit": limit,
                    },
                    drive_list_revisions_params.DriveListRevisionsParams,
                ),
            ),
            cast_to=Revisions,
        )

    async def retrieve_display(
        self,
        display_id: str,
        *,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DisplayManifest:
        """Fixed original/display/page IDs are immutable.

        Current app, credential, resource
        permissions and agent reference scope are checked before returning data.
        Unknown, mismatched and inaccessible tuples return the same access_denied error
        without source details. Storage keys and S3 VersionIds are never returned.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          display_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        if not display_id:
            raise ValueError(f"Expected a non-empty value for `display_id` but received {display_id!r}")
        return await self._get(
            path_template("/drive/files/{file_id}/displays/{display_id}", file_id=file_id, display_id=display_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisplayManifest,
        )

    async def retrieve_file(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Get Drive file metadata Requires a currently active agent connection bound to
        the authenticated API credential. Reference scope and new-output destination are
        separate; destination access does not grant source access.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            path_template("/drive/files/{file_id}", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    async def retrieve_references(
        self,
        file_id: str,
        *,
        revision_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> References:
        """
        Requires a fixed output revision_id and current reference permission on the
        output. Sources are agent claims, not independent proof that the agent read
        them. Output access never grants access to source material. Each source is
        checked independently against current connection scope, resource permission and
        fixed revision/display/page correspondence. Unavailable sources return only
        ordinal/status, without source IDs, names or content. recorded=false means no
        source information was provided.

        Args:
          file_id: Canonical lowercase nonzero UUID.

          revision_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            path_template("/drive/files/{file_id}/references", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"revision_id": revision_id}, drive_retrieve_references_params.DriveRetrieveReferencesParams
                ),
            ),
            cast_to=References,
        )

    async def retrieve_transfer(
        self,
        transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transfer:
        """
        Get a Drive transfer and persisted part receipts Requires a currently active
        agent connection bound to the authenticated API credential. Reference scope and
        new-output destination are separate; destination access does not grant source
        access.

        Args:
          transfer_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transfer_id:
            raise ValueError(f"Expected a non-empty value for `transfer_id` but received {transfer_id!r}")
        return await self._get(
            path_template("/drive/transfers/{transfer_id}", transfer_id=transfer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transfer,
        )

    async def search(
        self,
        *,
        query: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Searches currently authorized published analysis generations without requiring
        file IDs. The server fixes the complete allowed revision scope before retrieval
        and validates evidence against Drive metadata and content hashes. Permission or
        publication changes abort the response. Results include a matching reason and
        fixed original, display, page and analysis IDs. Search examines at most 1000
        ranked chunks; search_truncated reports this boundary. pending_analysis_count
        counts currently accessible originals without a published analysis. Pagination
        uses pagination.next_offset, rather than the file-list UUID cursor. Repeating a
        search reevaluates current permissions and content. The query, vectors, tables,
        tenant and actor cannot change the authorized scope.

        Args:
          query: Natural-language information need. Whitespace-only queries are rejected.

          offset: Use pagination.next_offset from the preceding response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/drive/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "limit": limit,
                    "offset": offset,
                },
                drive_search_params.DriveSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResponse,
        )

    async def upload_part(
        self,
        part_number: int,
        body: FileContent | AsyncBinaryTypes,
        *,
        transfer_id: str,
        x_drive_sha256: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartReceipt:
        """Streams one part.

        Use the returned part_size and declared original size to
        determine the exact length; only the final part may be smaller. SHA-256 is
        checked against the received bytes before a receipt is persisted. The same part
        number, size and hash are idempotent; changed input returns 409.
        Transfer-Encoding is not accepted. After interruption, fetch receipts and resend
        only missing parts with the same current credential. Requires a currently active
        agent connection bound to the authenticated API credential. Reference scope and
        new-output destination are separate; destination access does not grant source
        access.

        Args:
          transfer_id: Canonical lowercase nonzero UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transfer_id:
            raise ValueError(f"Expected a non-empty value for `transfer_id` but received {transfer_id!r}")
        extra_headers = {"X-Drive-SHA256": x_drive_sha256, **(extra_headers or {})}
        extra_headers["Content-Type"] = "application/octet-stream"
        return await self._put(
            path_template(
                "/drive/transfers/{transfer_id}/parts/{part_number}", transfer_id=transfer_id, part_number=part_number
            ),
            content=await async_read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PartReceipt,
        )


class DriveResourceWithRawResponse:
    def __init__(self, drive: DriveResource) -> None:
        self._drive = drive

        self.complete_transfer = to_raw_response_wrapper(
            drive.complete_transfer,
        )
        self.create_transfer = to_raw_response_wrapper(
            drive.create_transfer,
        )
        self.download_original = to_custom_raw_response_wrapper(
            drive.download_original,
            BinaryAPIResponse,
        )
        self.download_page_png = to_custom_raw_response_wrapper(
            drive.download_page_png,
            BinaryAPIResponse,
        )
        self.download_page_svg = to_custom_raw_response_wrapper(
            drive.download_page_svg,
            BinaryAPIResponse,
        )
        self.list_displays = to_raw_response_wrapper(
            drive.list_displays,
        )
        self.list_files = to_raw_response_wrapper(
            drive.list_files,
        )
        self.list_folders = to_raw_response_wrapper(
            drive.list_folders,
        )
        self.list_revisions = to_raw_response_wrapper(
            drive.list_revisions,
        )
        self.retrieve_display = to_raw_response_wrapper(
            drive.retrieve_display,
        )
        self.retrieve_file = to_raw_response_wrapper(
            drive.retrieve_file,
        )
        self.retrieve_references = to_raw_response_wrapper(
            drive.retrieve_references,
        )
        self.retrieve_transfer = to_raw_response_wrapper(
            drive.retrieve_transfer,
        )
        self.search = to_raw_response_wrapper(
            drive.search,
        )
        self.upload_part = to_raw_response_wrapper(
            drive.upload_part,
        )


class AsyncDriveResourceWithRawResponse:
    def __init__(self, drive: AsyncDriveResource) -> None:
        self._drive = drive

        self.complete_transfer = async_to_raw_response_wrapper(
            drive.complete_transfer,
        )
        self.create_transfer = async_to_raw_response_wrapper(
            drive.create_transfer,
        )
        self.download_original = async_to_custom_raw_response_wrapper(
            drive.download_original,
            AsyncBinaryAPIResponse,
        )
        self.download_page_png = async_to_custom_raw_response_wrapper(
            drive.download_page_png,
            AsyncBinaryAPIResponse,
        )
        self.download_page_svg = async_to_custom_raw_response_wrapper(
            drive.download_page_svg,
            AsyncBinaryAPIResponse,
        )
        self.list_displays = async_to_raw_response_wrapper(
            drive.list_displays,
        )
        self.list_files = async_to_raw_response_wrapper(
            drive.list_files,
        )
        self.list_folders = async_to_raw_response_wrapper(
            drive.list_folders,
        )
        self.list_revisions = async_to_raw_response_wrapper(
            drive.list_revisions,
        )
        self.retrieve_display = async_to_raw_response_wrapper(
            drive.retrieve_display,
        )
        self.retrieve_file = async_to_raw_response_wrapper(
            drive.retrieve_file,
        )
        self.retrieve_references = async_to_raw_response_wrapper(
            drive.retrieve_references,
        )
        self.retrieve_transfer = async_to_raw_response_wrapper(
            drive.retrieve_transfer,
        )
        self.search = async_to_raw_response_wrapper(
            drive.search,
        )
        self.upload_part = async_to_raw_response_wrapper(
            drive.upload_part,
        )


class DriveResourceWithStreamingResponse:
    def __init__(self, drive: DriveResource) -> None:
        self._drive = drive

        self.complete_transfer = to_streamed_response_wrapper(
            drive.complete_transfer,
        )
        self.create_transfer = to_streamed_response_wrapper(
            drive.create_transfer,
        )
        self.download_original = to_custom_streamed_response_wrapper(
            drive.download_original,
            StreamedBinaryAPIResponse,
        )
        self.download_page_png = to_custom_streamed_response_wrapper(
            drive.download_page_png,
            StreamedBinaryAPIResponse,
        )
        self.download_page_svg = to_custom_streamed_response_wrapper(
            drive.download_page_svg,
            StreamedBinaryAPIResponse,
        )
        self.list_displays = to_streamed_response_wrapper(
            drive.list_displays,
        )
        self.list_files = to_streamed_response_wrapper(
            drive.list_files,
        )
        self.list_folders = to_streamed_response_wrapper(
            drive.list_folders,
        )
        self.list_revisions = to_streamed_response_wrapper(
            drive.list_revisions,
        )
        self.retrieve_display = to_streamed_response_wrapper(
            drive.retrieve_display,
        )
        self.retrieve_file = to_streamed_response_wrapper(
            drive.retrieve_file,
        )
        self.retrieve_references = to_streamed_response_wrapper(
            drive.retrieve_references,
        )
        self.retrieve_transfer = to_streamed_response_wrapper(
            drive.retrieve_transfer,
        )
        self.search = to_streamed_response_wrapper(
            drive.search,
        )
        self.upload_part = to_streamed_response_wrapper(
            drive.upload_part,
        )


class AsyncDriveResourceWithStreamingResponse:
    def __init__(self, drive: AsyncDriveResource) -> None:
        self._drive = drive

        self.complete_transfer = async_to_streamed_response_wrapper(
            drive.complete_transfer,
        )
        self.create_transfer = async_to_streamed_response_wrapper(
            drive.create_transfer,
        )
        self.download_original = async_to_custom_streamed_response_wrapper(
            drive.download_original,
            AsyncStreamedBinaryAPIResponse,
        )
        self.download_page_png = async_to_custom_streamed_response_wrapper(
            drive.download_page_png,
            AsyncStreamedBinaryAPIResponse,
        )
        self.download_page_svg = async_to_custom_streamed_response_wrapper(
            drive.download_page_svg,
            AsyncStreamedBinaryAPIResponse,
        )
        self.list_displays = async_to_streamed_response_wrapper(
            drive.list_displays,
        )
        self.list_files = async_to_streamed_response_wrapper(
            drive.list_files,
        )
        self.list_folders = async_to_streamed_response_wrapper(
            drive.list_folders,
        )
        self.list_revisions = async_to_streamed_response_wrapper(
            drive.list_revisions,
        )
        self.retrieve_display = async_to_streamed_response_wrapper(
            drive.retrieve_display,
        )
        self.retrieve_file = async_to_streamed_response_wrapper(
            drive.retrieve_file,
        )
        self.retrieve_references = async_to_streamed_response_wrapper(
            drive.retrieve_references,
        )
        self.retrieve_transfer = async_to_streamed_response_wrapper(
            drive.retrieve_transfer,
        )
        self.search = async_to_streamed_response_wrapper(
            drive.search,
        )
        self.upload_part = async_to_streamed_response_wrapper(
            drive.upload_part,
        )
