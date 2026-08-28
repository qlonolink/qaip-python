from __future__ import annotations

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
from .sources import (
    _download_raw_result,
    _prepare_output_path,
    _stream_response_to_path,
    _stream_response_to_stdout,
)
from ..._types import omit
from .._errors import CLIError

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser("crawls.create", help="Create a web crawl")
    add_json_param(sub)
    sub.add_argument("--name", help="Crawl name")
    sub.add_argument("--start-url", help="URL to start crawling from")
    sub.add_argument("--max-depth", type=int, help="Maximum crawl depth")
    sub.add_argument("--max-num-files", type=int, help="Maximum number of files to crawl")
    sub.add_argument("--content-pattern", help="Comma-separated content patterns")
    sub.add_argument("--file-extensions", help="Comma-separated file extensions (e.g. .pdf,.docx)")
    sub.add_argument("--path-filters", help="Comma-separated path filter patterns")
    sub.add_argument("--html-only", action="store_true", default=None, help="Process HTML files only")
    sub.add_argument("--use-browser", action="store_true", default=None, help="Use headless browser for rendering")
    sub.add_argument(
        "--no-canonical-check", action="store_true", default=None, help="Disable duplicate filtering by canonical URL"
    )
    sub.add_argument("--rrule", help="Recurrence rule (RFC 5545 RRULE)")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create)

    sub = subparser.add_parser("crawls.retrieve", help="Get a crawl by ID")
    sub.add_argument("-i", "--id", required=True, help="Crawl ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve)

    sub = subparser.add_parser("crawls.list", help="List crawls")
    sub.add_argument("--limit", type=int, help="Maximum number of results")
    sub.add_argument("--after-id", help="Cursor for pagination")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list)

    sub = subparser.add_parser("crawls.delete", help="Delete a crawl")
    sub.add_argument("-i", "--id", required=True, help="Crawl ID")
    add_dry_run(sub)
    add_yes(sub)
    sub.set_defaults(func=_delete)

    sub = subparser.add_parser("crawls.download_raw_archive", help="Download crawl raw files as a ZIP archive")
    sub.add_argument("-i", "--id", required=True, dest="crawl_id", help="Crawl ID")
    sub.add_argument(
        "--source-id",
        action="append",
        dest="source_ids",
        help="Source ID to include; repeat to select multiple files (omit to include all)",
    )
    sub.add_argument("-o", "--output", help="Write downloaded ZIP bytes to this file")
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
        help="Write ZIP bytes to stdout instead of a file",
    )
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_download_raw_archive)

    sub = subparser.add_parser("crawls.retrieve_setting", help="Get crawl settings")
    sub.add_argument("-i", "--id", required=True, help="Crawl ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve_setting)

    sub = subparser.add_parser("crawls.update_setting", help="Update crawl settings")
    sub.add_argument("-i", "--id", required=True, help="Crawl ID")
    add_json_param(sub)
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_update_setting)

    sub = subparser.add_parser(
        "crawls.create_url_list",
        help="Create a crawl that downloads a specific list of URLs directly",
    )
    add_json_param(sub)
    sub.add_argument("--name", help="Name of the web crawl data source")
    sub.add_argument("--urls", help="Comma-separated list of URLs to download (target_urls)")
    sub.add_argument("--max-num-files", type=int, help="Maximum number of files to download")
    sub.add_argument(
        "--no-canonical-check", action="store_true", default=None, help="Disable duplicate filtering by canonical URL"
    )
    sub.add_argument("--rrule", help="Recurrence rule (RFC 5545 RRULE)")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create_url_list)


def _create(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    if args.name and "name" not in body:
        body["name"] = args.name
    if args.start_url and "start_url" not in body:
        body["start_url"] = args.start_url
    if args.max_depth is not None and "max_depth" not in body:
        body["max_depth"] = args.max_depth
    if args.max_num_files is not None and "max_num_files" not in body:
        body["max_num_files"] = args.max_num_files
    if args.content_pattern and "content_pattern" not in body:
        body["content_pattern"] = [p.strip() for p in args.content_pattern.split(",")]
    if args.file_extensions and "file_extensions" not in body:
        body["file_extensions"] = [e.strip() for e in args.file_extensions.split(",")]
    if args.path_filters and "path_filters" not in body:
        body["path_filters"] = [p.strip() for p in args.path_filters.split(",")]
    if args.html_only is not None and "html_only" not in body:
        body["html_only"] = args.html_only
    if args.use_browser is not None and "use_browser" not in body:
        body["use_browser"] = args.use_browser
    if args.no_canonical_check is not None and "no_canonical_check" not in body:
        body["no_canonical_check"] = args.no_canonical_check
    if args.rrule and "rrule" not in body:
        body["rrule"] = args.rrule

    for field in ("name", "start_url", "max_depth", "max_num_files"):
        if field not in body:
            raise CLIError(f"--{field.replace('_', '-')} or --json with '{field}' field is required")

    if args.dry_run:
        print_dry_run("POST", "/crawls", body)
        return
    client = get_client(args)
    result = client.crawls.create(**body)
    print_result(result.model_dump(), args)


def _retrieve(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/crawls/{args.id}")
        return
    validate_id(args.id, label="id")
    client = get_client(args)
    result = client.crawls.retrieve(args.id)
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
        print_dry_run("GET", "/crawls", params if params else None)
        return
    client = get_client(args)
    result = client.crawls.list(
        limit=limit if limit is not None else omit,
        after_id=after_id if after_id is not None else omit,
    )
    print_result(result.model_dump(), args)


def _delete(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("DELETE", f"/crawls/{args.id}")
        return
    validate_id(args.id, label="id")
    require_yes(args, action="crawls.delete")
    client = get_client(args)
    result = client.crawls.delete(args.id)
    print_result(result.model_dump(), args)


def _download_raw_archive(args: Namespace) -> None:
    source_ids: list[str] | None = args.source_ids
    if args.output and args.stdout:
        raise CLIError("--output and --stdout cannot be used together", code="invalid_argument")
    if args.stdout and args.force:
        raise CLIError("--force can only be used with --output", code="invalid_argument")
    if args.stdout and args.fields:
        raise CLIError("--fields cannot be used with --stdout", code="invalid_argument")

    if args.dry_run:
        body: dict[str, Any] = {}
        if source_ids is not None:
            body["source_ids"] = source_ids
        if args.output:
            body["output"] = args.output
            body["would_overwrite"] = Path(args.output).exists()
        if args.force:
            body["force"] = True
        if args.stdout:
            body["stdout"] = True
        print_dry_run("POST", f"/crawls/{args.crawl_id}/raw-archive", body if body else None)
        return

    validate_id(args.crawl_id, label="crawl_id")
    if source_ids is not None:
        if len(source_ids) > 10_000:
            raise CLIError("--source-id can be specified at most 10000 times", code="invalid_argument")
        if len(source_ids) != len(set(source_ids)):
            raise CLIError("Duplicate --source-id values are not allowed", code="invalid_argument")
        for source_id in source_ids:
            validate_id(source_id, label="source_id")

    if not args.output and not args.stdout:
        raise CLIError(
            "--output is required unless --stdout is set",
            code="invalid_argument",
            hint="Pass --output PATH to save the ZIP archive, or --stdout to stream raw bytes to stdout.",
        )

    output_path = _prepare_output_path(args.output, force=args.force) if args.output else None
    client = get_client(args)
    with client.crawls.with_streaming_response.download_raw_archive(
        args.crawl_id,
        source_ids=source_ids if source_ids is not None else omit,
    ) as response:
        if output_path is None:
            _stream_response_to_stdout(response)
            return

        bytes_written, sha256 = _stream_response_to_path(response, output_path)
        print_result(_download_raw_result(response, output_path, bytes_written, sha256), args)


def _retrieve_setting(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/crawl-settings/{args.id}")
        return
    validate_id(args.id, label="id")
    client = get_client(args)
    result = client.crawls.retrieve_setting(args.id)
    print_result(result.model_dump(), args)


def _update_setting(args: Namespace) -> None:
    body = parse_json_body(args)
    if body is None:
        raise CLIError("--json is required for update_setting")
    if args.dry_run:
        print_dry_run("PUT", f"/crawl-settings/{args.id}", body)
        return
    validate_id(args.id, label="id")
    client = get_client(args)
    result = client.crawls.update_setting(args.id, **body)
    print_result(result.model_dump(), args)


def _create_url_list(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    if args.name and "name" not in body:
        body["name"] = args.name
    if args.urls and "target_urls" not in body:
        body["target_urls"] = [u.strip() for u in args.urls.split(",")]
    if args.max_num_files is not None and "max_num_files" not in body:
        body["max_num_files"] = args.max_num_files
    if args.no_canonical_check is not None and "no_canonical_check" not in body:
        body["no_canonical_check"] = args.no_canonical_check
    if args.rrule and "rrule" not in body:
        body["rrule"] = args.rrule

    for field in ("name", "target_urls"):
        if field not in body:
            label = "--urls" if field == "target_urls" else f"--{field}"
            raise CLIError(f"{label} or --json with '{field}' field is required")

    if args.dry_run:
        print_dry_run("POST", "/crawl-url-lists", body)
        return
    client = get_client(args)
    result = client.crawls.create_url_list(**body)
    print_result(result.model_dump(), args)
