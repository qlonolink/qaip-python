# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from qaip import Qaip, AsyncQaip
from qaip.types import (
    File,
    Files,
    Folders,
    Displays,
    Transfer,
    Revisions,
    References,
    PartReceipt,
    SearchResponse,
    DisplayManifest,
)
from tests.utils import assert_matches_type
from qaip._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDrive:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete_transfer(self, client: Qaip) -> None:
        drive = client.drive.complete_transfer(
            transfer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            complete_transfer_request={},
        )
        assert_matches_type(Transfer, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_complete_transfer(self, client: Qaip) -> None:
        response = client.drive.with_raw_response.complete_transfer(
            transfer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            complete_transfer_request={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = response.parse()
        assert_matches_type(Transfer, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_complete_transfer(self, client: Qaip) -> None:
        with client.drive.with_streaming_response.complete_transfer(
            transfer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            complete_transfer_request={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = response.parse()
            assert_matches_type(Transfer, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_complete_transfer(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transfer_id` but received ''"):
            client.drive.with_raw_response.complete_transfer(
                transfer_id="",
                complete_transfer_request={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_transfer(self, client: Qaip) -> None:
        drive = client.drive.create_transfer(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            media_type="x",
            name="x",
            sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
            size_bytes=0,
        )
        assert_matches_type(Transfer, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_transfer_with_all_params(self, client: Qaip) -> None:
        drive = client.drive.create_transfer(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            media_type="x",
            name="x",
            sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
            size_bytes=0,
            references=[
                {
                    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "revision_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "display_revision_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "page_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )
        assert_matches_type(Transfer, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_transfer(self, client: Qaip) -> None:
        response = client.drive.with_raw_response.create_transfer(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            media_type="x",
            name="x",
            sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
            size_bytes=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = response.parse()
        assert_matches_type(Transfer, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_transfer(self, client: Qaip) -> None:
        with client.drive.with_streaming_response.create_transfer(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            media_type="x",
            name="x",
            sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
            size_bytes=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = response.parse()
            assert_matches_type(Transfer, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_original(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.get("/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/original").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        drive = client.drive.download_original(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert drive.is_closed
        assert drive.json() == {"foo": "bar"}
        assert cast(Any, drive.is_closed) is True
        assert isinstance(drive, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_original_with_all_params(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.get("/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/original").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        drive = client.drive.download_original(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            range="Range",
        )
        assert drive.is_closed
        assert drive.json() == {"foo": "bar"}
        assert cast(Any, drive.is_closed) is True
        assert isinstance(drive, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download_original(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.get("/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/original").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        drive = client.drive.with_raw_response.download_original(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert drive.is_closed is True
        assert drive.http_request.headers.get("X-Stainless-Lang") == "python"
        assert drive.json() == {"foo": "bar"}
        assert isinstance(drive, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download_original(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.get("/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/original").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.drive.with_streaming_response.download_original(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as drive:
            assert not drive.is_closed
            assert drive.http_request.headers.get("X-Stainless-Lang") == "python"

            assert drive.json() == {"foo": "bar"}
            assert cast(Any, drive.is_closed) is True
            assert isinstance(drive, StreamedBinaryAPIResponse)

        assert cast(Any, drive.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download_original(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.drive.with_raw_response.download_original(
                file_id="",
                revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_page_png(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/png"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        drive = client.drive.download_page_png(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert drive.is_closed
        assert drive.json() == {"foo": "bar"}
        assert cast(Any, drive.is_closed) is True
        assert isinstance(drive, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_page_png_with_all_params(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/png"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        drive = client.drive.download_page_png(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            range="Range",
        )
        assert drive.is_closed
        assert drive.json() == {"foo": "bar"}
        assert cast(Any, drive.is_closed) is True
        assert isinstance(drive, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download_page_png(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/png"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        drive = client.drive.with_raw_response.download_page_png(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert drive.is_closed is True
        assert drive.http_request.headers.get("X-Stainless-Lang") == "python"
        assert drive.json() == {"foo": "bar"}
        assert isinstance(drive, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download_page_png(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/png"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.drive.with_streaming_response.download_page_png(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as drive:
            assert not drive.is_closed
            assert drive.http_request.headers.get("X-Stainless-Lang") == "python"

            assert drive.json() == {"foo": "bar"}
            assert cast(Any, drive.is_closed) is True
            assert isinstance(drive, StreamedBinaryAPIResponse)

        assert cast(Any, drive.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download_page_png(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.drive.with_raw_response.download_page_png(
                page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_id="",
                display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `display_id` but received ''"):
            client.drive.with_raw_response.download_page_png(
                page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                display_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.drive.with_raw_response.download_page_png(
                page_id="",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_page_svg(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/svg"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        drive = client.drive.download_page_svg(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert drive.is_closed
        assert drive.json() == {"foo": "bar"}
        assert cast(Any, drive.is_closed) is True
        assert isinstance(drive, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_page_svg_with_all_params(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/svg"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        drive = client.drive.download_page_svg(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            range="Range",
        )
        assert drive.is_closed
        assert drive.json() == {"foo": "bar"}
        assert cast(Any, drive.is_closed) is True
        assert isinstance(drive, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download_page_svg(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/svg"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        drive = client.drive.with_raw_response.download_page_svg(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert drive.is_closed is True
        assert drive.http_request.headers.get("X-Stainless-Lang") == "python"
        assert drive.json() == {"foo": "bar"}
        assert isinstance(drive, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download_page_svg(self, client: Qaip, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/svg"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.drive.with_streaming_response.download_page_svg(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as drive:
            assert not drive.is_closed
            assert drive.http_request.headers.get("X-Stainless-Lang") == "python"

            assert drive.json() == {"foo": "bar"}
            assert cast(Any, drive.is_closed) is True
            assert isinstance(drive, StreamedBinaryAPIResponse)

        assert cast(Any, drive.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download_page_svg(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.drive.with_raw_response.download_page_svg(
                page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_id="",
                display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `display_id` but received ''"):
            client.drive.with_raw_response.download_page_svg(
                page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                display_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.drive.with_raw_response.download_page_svg(
                page_id="",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_displays(self, client: Qaip) -> None:
        drive = client.drive.list_displays(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Displays, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_displays_with_all_params(self, client: Qaip) -> None:
        drive = client.drive.list_displays(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
        )
        assert_matches_type(Displays, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_displays(self, client: Qaip) -> None:
        response = client.drive.with_raw_response.list_displays(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = response.parse()
        assert_matches_type(Displays, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_displays(self, client: Qaip) -> None:
        with client.drive.with_streaming_response.list_displays(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = response.parse()
            assert_matches_type(Displays, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_displays(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.drive.with_raw_response.list_displays(
                file_id="",
                revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_files(self, client: Qaip) -> None:
        drive = client.drive.list_files()
        assert_matches_type(Files, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_files_with_all_params(self, client: Qaip) -> None:
        drive = client.drive.list_files(
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            all_folders=True,
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            q="q",
        )
        assert_matches_type(Files, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_files(self, client: Qaip) -> None:
        response = client.drive.with_raw_response.list_files()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = response.parse()
        assert_matches_type(Files, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_files(self, client: Qaip) -> None:
        with client.drive.with_streaming_response.list_files() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = response.parse()
            assert_matches_type(Files, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_folders(self, client: Qaip) -> None:
        drive = client.drive.list_folders()
        assert_matches_type(Folders, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_folders_with_all_params(self, client: Qaip) -> None:
        drive = client.drive.list_folders(
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Folders, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_folders(self, client: Qaip) -> None:
        response = client.drive.with_raw_response.list_folders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = response.parse()
        assert_matches_type(Folders, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_folders(self, client: Qaip) -> None:
        with client.drive.with_streaming_response.list_folders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = response.parse()
            assert_matches_type(Folders, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_revisions(self, client: Qaip) -> None:
        drive = client.drive.list_revisions(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Revisions, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_revisions_with_all_params(self, client: Qaip) -> None:
        drive = client.drive.list_revisions(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
        )
        assert_matches_type(Revisions, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_revisions(self, client: Qaip) -> None:
        response = client.drive.with_raw_response.list_revisions(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = response.parse()
        assert_matches_type(Revisions, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_revisions(self, client: Qaip) -> None:
        with client.drive.with_streaming_response.list_revisions(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = response.parse()
            assert_matches_type(Revisions, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_revisions(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.drive.with_raw_response.list_revisions(
                file_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_display(self, client: Qaip) -> None:
        drive = client.drive.retrieve_display(
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DisplayManifest, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_display(self, client: Qaip) -> None:
        response = client.drive.with_raw_response.retrieve_display(
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = response.parse()
        assert_matches_type(DisplayManifest, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_display(self, client: Qaip) -> None:
        with client.drive.with_streaming_response.retrieve_display(
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = response.parse()
            assert_matches_type(DisplayManifest, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_display(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.drive.with_raw_response.retrieve_display(
                display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `display_id` but received ''"):
            client.drive.with_raw_response.retrieve_display(
                display_id="",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_file(self, client: Qaip) -> None:
        drive = client.drive.retrieve_file(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(File, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_file(self, client: Qaip) -> None:
        response = client.drive.with_raw_response.retrieve_file(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = response.parse()
        assert_matches_type(File, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_file(self, client: Qaip) -> None:
        with client.drive.with_streaming_response.retrieve_file(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = response.parse()
            assert_matches_type(File, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_file(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.drive.with_raw_response.retrieve_file(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_references(self, client: Qaip) -> None:
        drive = client.drive.retrieve_references(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(References, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_references(self, client: Qaip) -> None:
        response = client.drive.with_raw_response.retrieve_references(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = response.parse()
        assert_matches_type(References, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_references(self, client: Qaip) -> None:
        with client.drive.with_streaming_response.retrieve_references(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = response.parse()
            assert_matches_type(References, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_references(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.drive.with_raw_response.retrieve_references(
                file_id="",
                revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_transfer(self, client: Qaip) -> None:
        drive = client.drive.retrieve_transfer(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Transfer, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_transfer(self, client: Qaip) -> None:
        response = client.drive.with_raw_response.retrieve_transfer(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = response.parse()
        assert_matches_type(Transfer, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_transfer(self, client: Qaip) -> None:
        with client.drive.with_streaming_response.retrieve_transfer(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = response.parse()
            assert_matches_type(Transfer, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_transfer(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transfer_id` but received ''"):
            client.drive.with_raw_response.retrieve_transfer(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Qaip) -> None:
        drive = client.drive.search(
            query="x",
        )
        assert_matches_type(SearchResponse, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Qaip) -> None:
        drive = client.drive.search(
            query="x",
            limit=1,
            offset=0,
        )
        assert_matches_type(SearchResponse, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Qaip) -> None:
        response = client.drive.with_raw_response.search(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = response.parse()
        assert_matches_type(SearchResponse, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Qaip) -> None:
        with client.drive.with_streaming_response.search(
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = response.parse()
            assert_matches_type(SearchResponse, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_part(self, client: Qaip) -> None:
        drive = client.drive.upload_part(
            part_number=1,
            body=b"Example data",
            transfer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_drive_sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
        )
        assert_matches_type(PartReceipt, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload_part(self, client: Qaip) -> None:
        response = client.drive.with_raw_response.upload_part(
            part_number=1,
            body=b"Example data",
            transfer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_drive_sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = response.parse()
        assert_matches_type(PartReceipt, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload_part(self, client: Qaip) -> None:
        with client.drive.with_streaming_response.upload_part(
            part_number=1,
            body=b"Example data",
            transfer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_drive_sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = response.parse()
            assert_matches_type(PartReceipt, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload_part(self, client: Qaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transfer_id` but received ''"):
            client.drive.with_raw_response.upload_part(
                part_number=1,
                body=b"Example data",
                transfer_id="",
                x_drive_sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
            )


class TestAsyncDrive:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete_transfer(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.complete_transfer(
            transfer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            complete_transfer_request={},
        )
        assert_matches_type(Transfer, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_complete_transfer(self, async_client: AsyncQaip) -> None:
        response = await async_client.drive.with_raw_response.complete_transfer(
            transfer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            complete_transfer_request={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = await response.parse()
        assert_matches_type(Transfer, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_complete_transfer(self, async_client: AsyncQaip) -> None:
        async with async_client.drive.with_streaming_response.complete_transfer(
            transfer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            complete_transfer_request={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = await response.parse()
            assert_matches_type(Transfer, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_complete_transfer(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transfer_id` but received ''"):
            await async_client.drive.with_raw_response.complete_transfer(
                transfer_id="",
                complete_transfer_request={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_transfer(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.create_transfer(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            media_type="x",
            name="x",
            sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
            size_bytes=0,
        )
        assert_matches_type(Transfer, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_transfer_with_all_params(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.create_transfer(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            media_type="x",
            name="x",
            sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
            size_bytes=0,
            references=[
                {
                    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "revision_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "display_revision_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "page_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )
        assert_matches_type(Transfer, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_transfer(self, async_client: AsyncQaip) -> None:
        response = await async_client.drive.with_raw_response.create_transfer(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            media_type="x",
            name="x",
            sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
            size_bytes=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = await response.parse()
        assert_matches_type(Transfer, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_transfer(self, async_client: AsyncQaip) -> None:
        async with async_client.drive.with_streaming_response.create_transfer(
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            media_type="x",
            name="x",
            sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
            size_bytes=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = await response.parse()
            assert_matches_type(Transfer, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_original(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        respx_mock.get("/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/original").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        drive = await async_client.drive.download_original(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert drive.is_closed
        assert await drive.json() == {"foo": "bar"}
        assert cast(Any, drive.is_closed) is True
        assert isinstance(drive, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_original_with_all_params(
        self, async_client: AsyncQaip, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/original").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        drive = await async_client.drive.download_original(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            range="Range",
        )
        assert drive.is_closed
        assert await drive.json() == {"foo": "bar"}
        assert cast(Any, drive.is_closed) is True
        assert isinstance(drive, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download_original(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        respx_mock.get("/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/original").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        drive = await async_client.drive.with_raw_response.download_original(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert drive.is_closed is True
        assert drive.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await drive.json() == {"foo": "bar"}
        assert isinstance(drive, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download_original(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        respx_mock.get("/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/original").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.drive.with_streaming_response.download_original(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as drive:
            assert not drive.is_closed
            assert drive.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await drive.json() == {"foo": "bar"}
            assert cast(Any, drive.is_closed) is True
            assert isinstance(drive, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, drive.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download_original(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.drive.with_raw_response.download_original(
                file_id="",
                revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_page_png(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/png"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        drive = await async_client.drive.download_page_png(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert drive.is_closed
        assert await drive.json() == {"foo": "bar"}
        assert cast(Any, drive.is_closed) is True
        assert isinstance(drive, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_page_png_with_all_params(
        self, async_client: AsyncQaip, respx_mock: MockRouter
    ) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/png"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        drive = await async_client.drive.download_page_png(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            range="Range",
        )
        assert drive.is_closed
        assert await drive.json() == {"foo": "bar"}
        assert cast(Any, drive.is_closed) is True
        assert isinstance(drive, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download_page_png(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/png"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        drive = await async_client.drive.with_raw_response.download_page_png(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert drive.is_closed is True
        assert drive.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await drive.json() == {"foo": "bar"}
        assert isinstance(drive, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download_page_png(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/png"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.drive.with_streaming_response.download_page_png(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as drive:
            assert not drive.is_closed
            assert drive.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await drive.json() == {"foo": "bar"}
            assert cast(Any, drive.is_closed) is True
            assert isinstance(drive, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, drive.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download_page_png(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.drive.with_raw_response.download_page_png(
                page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_id="",
                display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `display_id` but received ''"):
            await async_client.drive.with_raw_response.download_page_png(
                page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                display_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.drive.with_raw_response.download_page_png(
                page_id="",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_page_svg(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/svg"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        drive = await async_client.drive.download_page_svg(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert drive.is_closed
        assert await drive.json() == {"foo": "bar"}
        assert cast(Any, drive.is_closed) is True
        assert isinstance(drive, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_page_svg_with_all_params(
        self, async_client: AsyncQaip, respx_mock: MockRouter
    ) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/svg"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        drive = await async_client.drive.download_page_svg(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            range="Range",
        )
        assert drive.is_closed
        assert await drive.json() == {"foo": "bar"}
        assert cast(Any, drive.is_closed) is True
        assert isinstance(drive, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download_page_svg(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/svg"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        drive = await async_client.drive.with_raw_response.download_page_svg(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert drive.is_closed is True
        assert drive.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await drive.json() == {"foo": "bar"}
        assert isinstance(drive, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download_page_svg(self, async_client: AsyncQaip, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/drive/files/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/displays/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/pages/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/svg"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.drive.with_streaming_response.download_page_svg(
            page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as drive:
            assert not drive.is_closed
            assert drive.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await drive.json() == {"foo": "bar"}
            assert cast(Any, drive.is_closed) is True
            assert isinstance(drive, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, drive.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download_page_svg(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.drive.with_raw_response.download_page_svg(
                page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_id="",
                display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `display_id` but received ''"):
            await async_client.drive.with_raw_response.download_page_svg(
                page_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                display_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.drive.with_raw_response.download_page_svg(
                page_id="",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_displays(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.list_displays(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Displays, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_displays_with_all_params(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.list_displays(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
        )
        assert_matches_type(Displays, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_displays(self, async_client: AsyncQaip) -> None:
        response = await async_client.drive.with_raw_response.list_displays(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = await response.parse()
        assert_matches_type(Displays, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_displays(self, async_client: AsyncQaip) -> None:
        async with async_client.drive.with_streaming_response.list_displays(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = await response.parse()
            assert_matches_type(Displays, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_displays(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.drive.with_raw_response.list_displays(
                file_id="",
                revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_files(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.list_files()
        assert_matches_type(Files, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_files_with_all_params(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.list_files(
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            all_folders=True,
            folder_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            q="q",
        )
        assert_matches_type(Files, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_files(self, async_client: AsyncQaip) -> None:
        response = await async_client.drive.with_raw_response.list_files()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = await response.parse()
        assert_matches_type(Files, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_files(self, async_client: AsyncQaip) -> None:
        async with async_client.drive.with_streaming_response.list_files() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = await response.parse()
            assert_matches_type(Files, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_folders(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.list_folders()
        assert_matches_type(Folders, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_folders_with_all_params(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.list_folders(
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            parent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Folders, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_folders(self, async_client: AsyncQaip) -> None:
        response = await async_client.drive.with_raw_response.list_folders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = await response.parse()
        assert_matches_type(Folders, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_folders(self, async_client: AsyncQaip) -> None:
        async with async_client.drive.with_streaming_response.list_folders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = await response.parse()
            assert_matches_type(Folders, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_revisions(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.list_revisions(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Revisions, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_revisions_with_all_params(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.list_revisions(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
        )
        assert_matches_type(Revisions, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_revisions(self, async_client: AsyncQaip) -> None:
        response = await async_client.drive.with_raw_response.list_revisions(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = await response.parse()
        assert_matches_type(Revisions, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_revisions(self, async_client: AsyncQaip) -> None:
        async with async_client.drive.with_streaming_response.list_revisions(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = await response.parse()
            assert_matches_type(Revisions, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_revisions(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.drive.with_raw_response.list_revisions(
                file_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_display(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.retrieve_display(
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DisplayManifest, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_display(self, async_client: AsyncQaip) -> None:
        response = await async_client.drive.with_raw_response.retrieve_display(
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = await response.parse()
        assert_matches_type(DisplayManifest, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_display(self, async_client: AsyncQaip) -> None:
        async with async_client.drive.with_streaming_response.retrieve_display(
            display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = await response.parse()
            assert_matches_type(DisplayManifest, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_display(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.drive.with_raw_response.retrieve_display(
                display_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                file_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `display_id` but received ''"):
            await async_client.drive.with_raw_response.retrieve_display(
                display_id="",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_file(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.retrieve_file(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(File, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_file(self, async_client: AsyncQaip) -> None:
        response = await async_client.drive.with_raw_response.retrieve_file(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = await response.parse()
        assert_matches_type(File, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_file(self, async_client: AsyncQaip) -> None:
        async with async_client.drive.with_streaming_response.retrieve_file(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = await response.parse()
            assert_matches_type(File, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_file(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.drive.with_raw_response.retrieve_file(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_references(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.retrieve_references(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(References, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_references(self, async_client: AsyncQaip) -> None:
        response = await async_client.drive.with_raw_response.retrieve_references(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = await response.parse()
        assert_matches_type(References, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_references(self, async_client: AsyncQaip) -> None:
        async with async_client.drive.with_streaming_response.retrieve_references(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = await response.parse()
            assert_matches_type(References, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_references(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.drive.with_raw_response.retrieve_references(
                file_id="",
                revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_transfer(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.retrieve_transfer(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Transfer, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_transfer(self, async_client: AsyncQaip) -> None:
        response = await async_client.drive.with_raw_response.retrieve_transfer(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = await response.parse()
        assert_matches_type(Transfer, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_transfer(self, async_client: AsyncQaip) -> None:
        async with async_client.drive.with_streaming_response.retrieve_transfer(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = await response.parse()
            assert_matches_type(Transfer, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_transfer(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transfer_id` but received ''"):
            await async_client.drive.with_raw_response.retrieve_transfer(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.search(
            query="x",
        )
        assert_matches_type(SearchResponse, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.search(
            query="x",
            limit=1,
            offset=0,
        )
        assert_matches_type(SearchResponse, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncQaip) -> None:
        response = await async_client.drive.with_raw_response.search(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = await response.parse()
        assert_matches_type(SearchResponse, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncQaip) -> None:
        async with async_client.drive.with_streaming_response.search(
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = await response.parse()
            assert_matches_type(SearchResponse, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_part(self, async_client: AsyncQaip) -> None:
        drive = await async_client.drive.upload_part(
            part_number=1,
            body=b"Example data",
            transfer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_drive_sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
        )
        assert_matches_type(PartReceipt, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload_part(self, async_client: AsyncQaip) -> None:
        response = await async_client.drive.with_raw_response.upload_part(
            part_number=1,
            body=b"Example data",
            transfer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_drive_sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        drive = await response.parse()
        assert_matches_type(PartReceipt, drive, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload_part(self, async_client: AsyncQaip) -> None:
        async with async_client.drive.with_streaming_response.upload_part(
            part_number=1,
            body=b"Example data",
            transfer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_drive_sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            drive = await response.parse()
            assert_matches_type(PartReceipt, drive, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload_part(self, async_client: AsyncQaip) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transfer_id` but received ''"):
            await async_client.drive.with_raw_response.upload_part(
                part_number=1,
                body=b"Example data",
                transfer_id="",
                x_drive_sha256="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
            )
