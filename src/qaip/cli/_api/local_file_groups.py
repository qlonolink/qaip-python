from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast
from argparse import ArgumentParser

from qaip import APIStatusError, omit

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
from .._errors import CLIError, mark_non_retryable

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser(
        "local-file-groups.create",
        help="Create a local file group by uploading files via multipart form data",
    )
    sub.add_argument("--name", help="Name of the local file group")
    sub.add_argument(
        "--file",
        dest="files",
        action="append",
        help="Path to a file to upload (repeat for multiple files)",
    )
    sub.add_argument(
        "--last-modified",
        help="Comma-separated Unix epoch millisecond timestamps, one per --file",
    )
    sub.add_argument(
        "--chunk-metadata-keys",
        help="JSON array of chunk metadata key configs (see API docs)",
    )
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create)

    sub = subparser.add_parser("local-file-groups.retrieve", help="Get a local file group by ID")
    sub.add_argument("-i", "--id", required=True, help="Local file group ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve)

    sub = subparser.add_parser("local-file-groups.list", help="List local file groups")
    sub.add_argument("--limit", type=int, help="Maximum number of results")
    sub.add_argument("--after-id", help="Cursor for pagination")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list)

    sub = subparser.add_parser("local-file-groups.delete", help="Delete a local file group")
    sub.add_argument("-i", "--id", required=True, help="Local file group ID")
    add_dry_run(sub)
    add_yes(sub)
    sub.set_defaults(func=_delete)

    sub = subparser.add_parser("local-file-groups.start_bulk_deletion", help="Start a bulk deletion job")
    sub.add_argument(
        "--source-group-id", dest="source_group_ids", action="append", help="Group ID (repeat for multiple groups)"
    )
    add_json_param(sub)
    add_dry_run(sub)
    add_yes(sub)
    add_fields(sub)
    sub.set_defaults(func=_start_bulk_deletion)

    sub = subparser.add_parser(
        "local-file-groups.start_chunk_deletion", help="Start deletion of chunks containing any matching text"
    )
    sub.add_argument("-i", "--id", required=True, help="Local file group ID")
    sub.add_argument("--text-contains", action="append", help="Literal substring (repeat for OR matching)")
    add_json_param(sub)
    add_dry_run(sub)
    add_yes(sub)
    add_fields(sub)
    sub.set_defaults(func=_start_chunk_deletion)

    sub = subparser.add_parser(
        "local-file-groups.retrieve_bulk_deletion", help="Get bulk deletion status and remaining groups"
    )
    sub.add_argument("--bulk-deletion-id", required=True, help="Bulk deletion job ID")
    sub.add_argument("--after", help="remaining_cursor from the previous response")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve_bulk_deletion)

    sub = subparser.add_parser("local-file-groups.retrieve_chunk_deletion", help="Get chunk deletion status")
    sub.add_argument("-i", "--id", required=True, help="Local file group ID")
    sub.add_argument("--chunk-deletion-id", required=True, help="Chunk deletion job ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve_chunk_deletion)


def _create(args: Namespace) -> None:
    import os
    from contextlib import ExitStack

    name: str | None = args.name
    file_paths: list[str] = list(args.files or [])
    last_modified_raw: str | None = args.last_modified
    chunk_metadata_keys: str | None = args.chunk_metadata_keys

    if not name:
        raise CLIError("--name is required")
    if not file_paths:
        raise CLIError("--file is required (specify at least one file path)")

    explicit_last_modified: list[int] | None = None
    if last_modified_raw:
        explicit_last_modified = [int(ts.strip()) for ts in last_modified_raw.split(",")]
        if len(explicit_last_modified) != len(file_paths):
            raise CLIError(
                f"--last-modified has {len(explicit_last_modified)} entries but {len(file_paths)} files were specified"
            )

    # 複数ファイルの open を途中失敗しても既に開いたハンドルをリークさせないため
    # ExitStack で確実にクローズする。mtime も fstat で取得し getmtime+open の
    # 二重 syscall と TOCTOU を回避する。
    with ExitStack() as stack:
        try:
            opened = [(p, stack.enter_context(open(p, "rb"))) for p in file_paths]
        except FileNotFoundError as err:
            raise CLIError(f"File not found: {err.filename}") from err

        if explicit_last_modified is not None:
            last_modified = explicit_last_modified
        else:
            last_modified = [int(os.fstat(fh.fileno()).st_mtime * 1000) for _, fh in opened]

        if args.dry_run:
            dry_body: dict[str, Any] = {
                "name": name,
                "files": [os.path.basename(p) for p, _ in opened],
                "last_modified": last_modified,
            }
            if chunk_metadata_keys:
                dry_body["chunk_metadata_keys"] = chunk_metadata_keys
            print_dry_run("POST", "/local-file-groups", dry_body)
            return

        files = [(os.path.basename(p), fh) for p, fh in opened]
        client = get_client(args)
        result = client.local_file_groups.create(
            name=name,
            files=files,
            last_modified=[str(ts) for ts in last_modified],
            chunk_metadata_keys=chunk_metadata_keys if chunk_metadata_keys is not None else omit,
        )
        print_result(result.model_dump(), args)


def _retrieve(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/local-file-groups/{args.id}")
        return
    validate_id(args.id, label="id")
    client = get_client(args)
    result = client.local_file_groups.retrieve(args.id)
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
        print_dry_run("GET", "/local-file-groups", params if params else None)
        return
    client = get_client(args)
    result = client.local_file_groups.list(
        limit=limit if limit is not None else omit,
        after_id=after_id if after_id is not None else omit,
    )
    print_result(result.model_dump(), args)


def _delete(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("DELETE", f"/local-file-groups/{args.id}")
        return
    validate_id(args.id, label="id")
    require_yes(args, action="local-file-groups.delete")
    client = get_client(args)
    result = client.local_file_groups.delete(args.id)
    print_result(result.model_dump(), args)


def _deletion_values(args: Namespace, field: str) -> list[str]:
    body = parse_json_body(args) or {}
    unknown = set(body) - {field}
    if unknown:
        raise CLIError(f"unsupported field(s) in --json: {', '.join(sorted(unknown))}", code="invalid_argument")
    values = body.get(field, getattr(args, field))
    if (
        not isinstance(values, list)
        or not values
        or any(not isinstance(value, str) or not value for value in cast("list[object]", values))
    ):
        raise CLIError(f"{field} must be a non-empty array of non-empty strings", code="invalid_argument")
    return cast("list[str]", values)


def _start_bulk_deletion(args: Namespace) -> None:
    values = _deletion_values(args, "source_group_ids")
    if args.dry_run:
        print_dry_run("POST", "/local-file-groups/bulk-deletions", {"source_group_ids": values})
        return
    for value in values:
        validate_id(value, label="source_group_ids")
    require_yes(args, action="local-file-groups.start_bulk_deletion")
    client = get_client(args).with_options(max_retries=0)
    try:
        result = client.local_file_groups.start_bulk_deletion(source_group_ids=values)
    except APIStatusError as err:
        mark_non_retryable(err, "Check the deletion outcome before resubmitting the request.")
        raise
    print_result(result.model_dump(), args)


def _start_chunk_deletion(args: Namespace) -> None:
    values = _deletion_values(args, "text_contains")
    if args.dry_run:
        print_dry_run("POST", f"/local-file-groups/{args.id}/chunk-deletions", {"text_contains": values})
        return
    validate_id(args.id, label="id")
    require_yes(args, action="local-file-groups.start_chunk_deletion")
    client = get_client(args).with_options(max_retries=0)
    try:
        result = client.local_file_groups.start_chunk_deletion(args.id, text_contains=values)
    except APIStatusError as err:
        mark_non_retryable(err, "Check the deletion outcome before resubmitting the request.")
        raise
    print_result(result.model_dump(), args)


def _retrieve_bulk_deletion(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run(
            "GET",
            f"/local-file-groups/bulk-deletions/{args.bulk_deletion_id}",
            query={"after": args.after} if args.after is not None else None,
        )
        return
    validate_id(args.bulk_deletion_id, label="bulk_deletion_id")
    if args.after is not None:
        validate_id(args.after, label="after")
    client = get_client(args)
    result = client.local_file_groups.retrieve_bulk_deletion(
        args.bulk_deletion_id, after=args.after if args.after is not None else omit
    )
    print_result(result.model_dump(), args)


def _retrieve_chunk_deletion(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/local-file-groups/{args.id}/chunk-deletions/{args.chunk_deletion_id}")
        return
    validate_id(args.id, label="id")
    validate_id(args.chunk_deletion_id, label="chunk_deletion_id")
    client = get_client(args)
    result = client.local_file_groups.retrieve_chunk_deletion(args.chunk_deletion_id, id=args.id)
    print_result(result.model_dump(), args)
