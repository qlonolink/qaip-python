from __future__ import annotations

from typing import TYPE_CHECKING, Any
from argparse import ArgumentParser

from .._utils import get_client
from ._common import add_fields, add_dry_run, print_result, print_dry_run
from ..._types import omit
from .._errors import CLIError

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
    sub.set_defaults(func=_delete)


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
                f"--last-modified has {len(explicit_last_modified)} entries "
                f"but {len(file_paths)} files were specified"
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
    client = get_client(args)
    result = client.local_file_groups.delete(args.id)
    print_result(result.model_dump(), args)
