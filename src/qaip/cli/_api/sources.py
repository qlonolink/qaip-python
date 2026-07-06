from __future__ import annotations

import os
import sys
import hashlib
import tempfile
from typing import TYPE_CHECKING, Any
from pathlib import Path
from argparse import ArgumentParser

from .._utils import get_client
from ._common import (
    add_yes,
    add_fields,
    add_dry_run,
    require_yes,
    validate_id,
    print_result,
    print_dry_run,
    add_json_param,
    parse_json_body,
)
from ..._types import omit
from .._errors import CLIError

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    # sources.retrieve
    sub = subparser.add_parser("sources.retrieve", help="Get a source by ID")
    sub.add_argument("-i", "--id", required=True, dest="source_id", help="Source ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve)

    # sources.list
    sub = subparser.add_parser("sources.list", help="List sources")
    sub.add_argument("--limit", type=int, help="Maximum number of results")
    sub.add_argument("--after-id", help="Cursor for pagination")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list)

    # sources.retrieve_metadata
    sub = subparser.add_parser("sources.retrieve_metadata", help="Get source metadata")
    sub.add_argument("-i", "--id", required=True, dest="source_id", help="Source ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve_metadata)

    # sources.update_metadata
    sub = subparser.add_parser("sources.update_metadata", help="Update source metadata")
    sub.add_argument("-i", "--id", required=True, dest="source_id", help="Source ID")
    add_json_param(sub)
    add_dry_run(sub)
    sub.set_defaults(func=_update_metadata)

    # sources.delete_metadata
    sub = subparser.add_parser("sources.delete_metadata", help="Delete source metadata")
    sub.add_argument("-i", "--id", required=True, dest="source_id", help="Source ID")
    add_dry_run(sub)
    add_yes(sub)
    sub.set_defaults(func=_delete_metadata)

    # sources.batch_set_metadata
    sub = subparser.add_parser("sources.batch_set_metadata", help="Batch set source metadata")
    add_json_param(sub)
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_batch_set_metadata)

    # sources.download_raw
    sub = subparser.add_parser("sources.download_raw", help="Download original crawl source raw file")
    sub.add_argument(
        "-i", "--id", required=True, dest="source_id", help="Crawl source ID returned in content.source_id"
    )
    sub.add_argument("-o", "--output", help="Write downloaded bytes to this file")
    sub.add_argument(
        "--force",
        action="store_true",
        default=False,
        help="Overwrite --output if it already exists",
    )
    sub.add_argument(
        "--stdout",
        action="store_true",
        default=False,
        help="Write raw bytes to stdout instead of a file",
    )
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_download_raw)


def _retrieve(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/sources/{args.source_id}")
        return

    validate_id(args.source_id, label="source_id")
    client = get_client(args)
    result = client.sources.retrieve(args.source_id)
    print_result(result.model_dump(), args)


def _list(args: Namespace) -> None:
    limit: int | None = args.limit
    after_id: str | None = args.after_id

    if args.dry_run:
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if after_id is not None:
            params["after_id"] = after_id
        print_dry_run("GET", "/sources", params if params else None)
        return

    client = get_client(args)
    result = client.sources.list(
        limit=limit if limit is not None else omit,
        after_id=after_id if after_id is not None else omit,
    )
    print_result(result.model_dump(), args)


def _retrieve_metadata(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/sources/{args.source_id}/metadata")
        return

    validate_id(args.source_id, label="source_id")
    client = get_client(args)
    result = client.sources.retrieve_metadata(args.source_id)
    print_result(result.model_dump(), args)


def _update_metadata(args: Namespace) -> None:
    body = parse_json_body(args)
    if body is None:
        raise CLIError("--json is required for update_metadata")

    if args.dry_run:
        print_dry_run("PUT", f"/sources/{args.source_id}/metadata", body)
        return

    validate_id(args.source_id, label="source_id")
    client = get_client(args)
    result = client.sources.update_metadata(args.source_id, **body)
    print_result(result.model_dump(), args)


def _delete_metadata(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("DELETE", f"/sources/{args.source_id}/metadata")
        return

    validate_id(args.source_id, label="source_id")
    require_yes(args, action="sources.delete_metadata")
    client = get_client(args)
    result = client.sources.delete_metadata(args.source_id)
    print_result(result.model_dump(), args)


def _batch_set_metadata(args: Namespace) -> None:
    body = parse_json_body(args)
    if body is None:
        raise CLIError("--json is required for batch_set_metadata")

    if args.dry_run:
        print_dry_run("POST", "/sources/metadata/batch", body)
        return

    client = get_client(args)
    result = client.sources.batch_set_metadata(**body)
    print_result(result.model_dump(), args)


def _download_raw(args: Namespace) -> None:
    if args.output and args.stdout:
        raise CLIError("--output and --stdout cannot be used together", code="invalid_argument")
    if args.stdout and args.force:
        raise CLIError("--force can only be used with --output", code="invalid_argument")
    if args.stdout and args.fields:
        raise CLIError("--fields cannot be used with --stdout", code="invalid_argument")

    if args.dry_run:
        body: dict[str, Any] = {}
        if args.output:
            body["output"] = args.output
            body["would_overwrite"] = Path(args.output).exists()
        if args.force:
            body["force"] = True
        if args.stdout:
            body["stdout"] = True
        print_dry_run("GET", f"/sources/{args.source_id}/raw", body if body else None)
        return

    validate_id(args.source_id, label="source_id")

    if not args.output and not args.stdout:
        raise CLIError(
            "--output is required unless --stdout is set",
            code="invalid_argument",
            hint="Pass --output PATH to save the downloaded file, or --stdout to stream raw bytes to stdout.",
        )

    output_path = _prepare_output_path(args.output, force=args.force) if args.output else None
    client = get_client(args)
    with client.sources.with_streaming_response.download_raw(args.source_id) as response:
        if output_path is None:
            _stream_response_to_stdout(response)
            return

        bytes_written, sha256 = _stream_response_to_path(response, output_path)
        print_result(_download_raw_result(response, output_path, bytes_written, sha256), args)


def _prepare_output_path(raw_output: str, *, force: bool) -> Path:
    output = Path(raw_output)
    if output.exists() and output.is_dir():
        raise CLIError(f"Output path is a directory: {raw_output}", code="invalid_argument")
    if (output.exists() or output.is_symlink()) and not force:
        raise CLIError(
            f"Output file already exists: {raw_output}",
            code="confirmation_required",
            hint="Pass --force to overwrite the existing file.",
        )
    parent = output.parent
    if not parent.exists():
        raise CLIError(f"Output directory does not exist: {parent}", code="invalid_argument")
    if not parent.is_dir():
        raise CLIError(f"Output parent is not a directory: {parent}", code="invalid_argument")
    return output


def _stream_response_to_path(response: Any, output: Path) -> tuple[int, str]:  # noqa: ANN401
    tmp_name: str | None = None
    bytes_written = 0
    digest = hashlib.sha256()
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=str(output.parent),
            prefix=f".{output.name}.",
            delete=False,
        ) as tmp:
            tmp_name = tmp.name
            for chunk in response.iter_bytes():
                tmp.write(chunk)
                bytes_written += len(chunk)
                digest.update(chunk)
        os.replace(tmp_name, output)
        return bytes_written, digest.hexdigest()
    except OSError as err:
        if tmp_name is not None:
            _remove_partial_download(tmp_name)
        raise CLIError(f"Failed to write output file: {err}", code="invalid_argument") from err
    except Exception:
        if tmp_name is not None:
            _remove_partial_download(tmp_name)
        raise


def _remove_partial_download(path: str) -> None:
    try:
        os.unlink(path)
    except OSError:
        pass


def _stream_response_to_stdout(response: Any) -> None:  # noqa: ANN401
    stdout = getattr(sys.stdout, "buffer", sys.stdout)
    for chunk in response.iter_bytes():
        stdout.write(chunk)


def _download_raw_result(
    response: Any, output: Path, bytes_written: int, sha256: str
) -> dict[str, Any]:  # noqa: ANN401
    headers = response.http_response.headers
    result: dict[str, Any] = {
        "path": str(output.resolve()),
        "bytes_written": bytes_written,
        "sha256": sha256,
    }

    content_type = headers.get("content-type")
    if content_type is not None:
        result["content_type"] = content_type

    content_length = headers.get("content-length")
    if content_length is not None:
        try:
            result["content_length"] = int(content_length)
        except ValueError:
            result["content_length"] = content_length

    content_disposition = headers.get("content-disposition")
    if content_disposition is not None:
        result["content_disposition"] = content_disposition

    return result
