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
    sub.set_defaults(func=_delete_metadata)

    # sources.batch_set_metadata
    sub = subparser.add_parser("sources.batch_set_metadata", help="Batch set source metadata")
    add_json_param(sub)
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_batch_set_metadata)


def _retrieve(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/sources/{args.source_id}")
        return

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

    client = get_client(args)
    result = client.sources.update_metadata(args.source_id, **body)
    print_result(result.model_dump(), args)


def _delete_metadata(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("DELETE", f"/sources/{args.source_id}/metadata")
        return

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
