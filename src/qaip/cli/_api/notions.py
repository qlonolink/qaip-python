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
    sub = subparser.add_parser("notions.create", help="Create a Notion integration")
    add_json_param(sub)
    sub.add_argument("--name", help="Name")
    sub.add_argument("--page-id", help="Notion page ID")
    sub.add_argument("--secret-id", help="Stored secret ID (mutually exclusive with --notion-token)")
    sub.add_argument("--notion-token", help="One-time Notion integration token (mutually exclusive with --secret-id)")
    sub.add_argument("--rrule", help="Recurrence rule (RFC 5545 RRULE)")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create)

    sub = subparser.add_parser("notions.retrieve", help="Get a Notion integration by ID")
    sub.add_argument("-i", "--id", required=True, help="Notion integration ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve)

    sub = subparser.add_parser("notions.list", help="List Notion integrations")
    sub.add_argument("--limit", type=int, help="Maximum number of results")
    sub.add_argument("--after-id", help="Cursor for pagination")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list)

    sub = subparser.add_parser("notions.delete", help="Delete a Notion integration")
    sub.add_argument("-i", "--id", required=True, help="Notion integration ID")
    add_dry_run(sub)
    sub.set_defaults(func=_delete)

    sub = subparser.add_parser("notions.retrieve_setting", help="Get Notion settings")
    sub.add_argument("-i", "--id", required=True, help="Notion integration ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve_setting)

    sub = subparser.add_parser("notions.update_setting", help="Update Notion settings")
    sub.add_argument("-i", "--id", required=True, help="Notion integration ID")
    add_json_param(sub)
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_update_setting)


def _create(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    if args.name and "name" not in body:
        body["name"] = args.name
    if args.page_id and "page_id" not in body:
        body["page_id"] = args.page_id
    if args.secret_id and "secret_id" not in body:
        body["secret_id"] = args.secret_id
    if args.notion_token and "notion_token" not in body:
        body["notion_token"] = args.notion_token
    if args.rrule and "rrule" not in body:
        body["rrule"] = args.rrule

    for field in ("name", "page_id"):
        if field not in body:
            raise CLIError(f"--{field.replace('_', '-')} or --json with '{field}' field is required")

    if args.dry_run:
        print_dry_run("POST", "/notions", body, sensitive_keys=("notion_token",))
        return
    client = get_client(args)
    result = client.notions.create(**body)
    print_result(result.model_dump(), args)


def _retrieve(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/notions/{args.id}")
        return
    client = get_client(args)
    result = client.notions.retrieve(args.id)
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
        print_dry_run("GET", "/notions", params if params else None)
        return
    client = get_client(args)
    result = client.notions.list(
        limit=limit if limit is not None else omit,
        after_id=after_id if after_id is not None else omit,
    )
    print_result(result.model_dump(), args)


def _delete(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("DELETE", f"/notions/{args.id}")
        return
    client = get_client(args)
    result = client.notions.delete(args.id)
    print_result(result.model_dump(), args)


def _retrieve_setting(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/notion-settings/{args.id}")
        return
    client = get_client(args)
    result = client.notions.retrieve_setting(args.id)
    print_result(result.model_dump(), args)


def _update_setting(args: Namespace) -> None:
    body = parse_json_body(args)
    if body is None:
        raise CLIError("--json is required for update_setting")
    if args.dry_run:
        print_dry_run("PUT", f"/notion-settings/{args.id}", body)
        return
    client = get_client(args)
    result = client.notions.update_setting(args.id, **body)
    print_result(result.model_dump(), args)
