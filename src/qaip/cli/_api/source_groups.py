from __future__ import annotations

from typing import TYPE_CHECKING, Any
from argparse import ArgumentParser

from .._utils import get_client
from ._common import add_fields, add_dry_run, print_result, print_dry_run, add_json_param, parse_json_body
from ..._types import omit
from .._errors import CLIError

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser("source-groups.retrieve", help="Get a source group by ID")
    sub.add_argument("-i", "--id", required=True, dest="source_group_id", help="Source group ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve)

    sub = subparser.add_parser("source-groups.list", help="List source groups")
    sub.add_argument("--limit", type=int, help="Maximum number of results")
    sub.add_argument("--after-id", help="Cursor for pagination")
    sub.add_argument(
        "--source-type",
        help="Filter by source type (e.g. crawl, local_file, google_drive, github, notion)",
    )
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list)

    sub = subparser.add_parser("source-groups.list_sources", help="List sources in a source group")
    sub.add_argument("-i", "--id", required=True, dest="source_group_id", help="Source group ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list_sources)

    sub = subparser.add_parser("source-groups.retrieve_metadata", help="Get source group metadata")
    sub.add_argument("-i", "--id", required=True, dest="source_group_id", help="Source group ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve_metadata)

    sub = subparser.add_parser("source-groups.update_metadata", help="Update source group metadata")
    sub.add_argument("-i", "--id", required=True, dest="source_group_id", help="Source group ID")
    add_json_param(sub)
    add_dry_run(sub)
    sub.set_defaults(func=_update_metadata)

    sub = subparser.add_parser("source-groups.delete_metadata", help="Delete source group metadata")
    sub.add_argument("-i", "--id", required=True, dest="source_group_id", help="Source group ID")
    add_dry_run(sub)
    sub.set_defaults(func=_delete_metadata)

    sub = subparser.add_parser("source-groups.batch_set_metadata", help="Batch set source group metadata")
    add_json_param(sub)
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_batch_set_metadata)


def _retrieve(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/source-groups/{args.source_group_id}")
        return
    client = get_client(args)
    result = client.source_groups.retrieve(args.source_group_id)
    print_result(result.model_dump(), args)


def _list(args: Namespace) -> None:
    limit: int | None = args.limit
    after_id: str | None = args.after_id
    source_type: str | None = args.source_type

    if args.dry_run:
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if after_id is not None:
            params["after_id"] = after_id
        if source_type is not None:
            params["source_type"] = source_type
        print_dry_run("GET", "/source-groups", params if params else None)
        return
    client = get_client(args)
    result = client.source_groups.list(
        limit=limit if limit is not None else omit,
        after_id=after_id if after_id is not None else omit,
        source_type=source_type if source_type is not None else omit,  # type: ignore[arg-type]
    )
    print_result(result.model_dump(), args)


def _list_sources(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/source-groups/{args.source_group_id}/sources")
        return
    client = get_client(args)
    result = client.source_groups.list_sources(args.source_group_id)
    print_result(result.model_dump(), args)


def _retrieve_metadata(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/source-groups/{args.source_group_id}/metadata")
        return
    client = get_client(args)
    result = client.source_groups.retrieve_metadata(args.source_group_id)
    print_result(result.model_dump(), args)


def _update_metadata(args: Namespace) -> None:
    body = parse_json_body(args)
    if body is None:
        raise CLIError("--json is required for update_metadata")
    if args.dry_run:
        print_dry_run("PUT", f"/source-groups/{args.source_group_id}/metadata", body)
        return
    client = get_client(args)
    result = client.source_groups.update_metadata(args.source_group_id, **body)
    print_result(result.model_dump(), args)


def _delete_metadata(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("DELETE", f"/source-groups/{args.source_group_id}/metadata")
        return
    client = get_client(args)
    result = client.source_groups.delete_metadata(args.source_group_id)
    print_result(result.model_dump(), args)


def _batch_set_metadata(args: Namespace) -> None:
    body = parse_json_body(args)
    if body is None:
        raise CLIError("--json is required for batch_set_metadata")
    if args.dry_run:
        print_dry_run("POST", "/source-groups/metadata/batch", body)
        return
    client = get_client(args)
    result = client.source_groups.batch_set_metadata(**body)
    print_result(result.model_dump(), args)
