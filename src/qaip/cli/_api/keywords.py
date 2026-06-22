from __future__ import annotations

from typing import TYPE_CHECKING, Any
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
    sub = subparser.add_parser("keywords.create", help="Create a keyword")
    add_json_param(sub)
    sub.add_argument("--name", help="Keyword name")
    sub.add_argument("--meaning", help="Keyword meaning")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create)

    sub = subparser.add_parser("keywords.retrieve", help="Get a keyword by ID")
    sub.add_argument("-i", "--id", required=True, dest="id", help="Keyword ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve)

    sub = subparser.add_parser("keywords.update", help="Update a keyword")
    sub.add_argument("-i", "--id", required=True, dest="id", help="Keyword ID")
    add_json_param(sub)
    sub.add_argument("--name", help="Keyword name")
    sub.add_argument("--meaning", help="Keyword meaning")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_update)

    sub = subparser.add_parser("keywords.list", help="List keywords")
    sub.add_argument("--offset", type=int, help="Number of records to skip")
    sub.add_argument("--page-size", type=int, dest="page_size", help="Maximum number of results")
    sub.add_argument("--sort-field", dest="sort_field", help="Field to sort by")
    sub.add_argument("--sort-order", dest="sort_order", help="Sort order (asc/desc)")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list)

    sub = subparser.add_parser("keywords.delete", help="Delete a keyword")
    sub.add_argument("-i", "--id", required=True, dest="id", help="Keyword ID")
    add_dry_run(sub)
    add_yes(sub)
    sub.set_defaults(func=_delete)


def _create(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    if args.name and "name" not in body:
        body["name"] = args.name
    if args.meaning and "meaning" not in body:
        body["meaning"] = args.meaning

    if "name" not in body:
        raise CLIError("--name or --json with 'name' field is required")

    if args.dry_run:
        print_dry_run("POST", "/keywords", body)
        return
    client = get_client(args)
    result = client.keywords.create(**body)
    print_result(result.model_dump(), args)


def _retrieve(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/keywords/{args.id}")
        return
    validate_id(args.id, label="id")
    client = get_client(args)
    result = client.keywords.retrieve(args.id)
    print_result(result.model_dump(), args)


def _update(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    if args.name and "name" not in body:
        body["name"] = args.name
    if args.meaning and "meaning" not in body:
        body["meaning"] = args.meaning

    if "name" not in body:
        raise CLIError("--name or --json with 'name' field is required")

    if args.dry_run:
        print_dry_run("PUT", f"/keywords/{args.id}", body)
        return
    validate_id(args.id, label="id")
    client = get_client(args)
    result = client.keywords.update(args.id, **body)
    print_result(result.model_dump(), args)


def _list(args: Namespace) -> None:
    offset: int | None = args.offset
    page_size: int | None = args.page_size
    sort_field: str | None = args.sort_field
    sort_order: str | None = args.sort_order

    if args.dry_run:
        params: dict[str, Any] = {}
        if offset is not None:
            params["offset"] = offset
        if page_size is not None:
            params["page_size"] = page_size
        if sort_field is not None:
            params["sort_field"] = sort_field
        if sort_order is not None:
            params["sort_order"] = sort_order
        print_dry_run("GET", "/keywords", params if params else None)
        return
    client = get_client(args)
    result = client.keywords.list(
        offset=offset if offset is not None else omit,
        page_size=page_size if page_size is not None else omit,
        sort_field=sort_field if sort_field is not None else omit,
        sort_order=sort_order if sort_order is not None else omit,
    )
    print_result(result.model_dump(), args)


def _delete(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("DELETE", f"/keywords/{args.id}")
        return
    validate_id(args.id, label="id")
    require_yes(args, action="keywords.delete")
    client = get_client(args)
    result = client.keywords.delete(args.id)
    print_result(result.model_dump(), args)
