from __future__ import annotations

from typing import TYPE_CHECKING
from argparse import ArgumentParser

from ...types import Tag
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
from .._errors import CLIError

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser("tags.list", help="List tags")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list)

    sub = subparser.add_parser("tags.create", help="Create a tag")
    add_json_param(sub)
    sub.add_argument("--name", help="Tag name")
    sub.add_argument("--description", help="Tag description")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create)

    sub = subparser.add_parser("tags.update", help="Update a tag's name or description")
    sub.add_argument("-i", "--id", required=True, dest="id", help="Tag ID")
    add_json_param(sub)
    sub.add_argument("--name", help="New tag name")
    sub.add_argument("--description", help="New tag description")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_update)

    sub = subparser.add_parser("tags.delete", help="Delete a tag")
    sub.add_argument("-i", "--id", required=True, dest="id", help="Tag ID")
    add_dry_run(sub)
    add_yes(sub)
    sub.set_defaults(func=_delete)


def _list(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", "/tags")
        return

    client = get_client(args)
    result = client.tags()
    print_result(result.model_dump(), args)


def _create(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    if args.name and "name" not in body:
        body["name"] = args.name
    if args.description and "description" not in body:
        body["description"] = args.description

    if "name" not in body:
        raise CLIError("--name or --json with 'name' field is required")

    if args.dry_run:
        print_dry_run("POST", "/tags", body)
        return
    client = get_client(args)
    result = client.post("/tags", body=body, cast_to=Tag)
    print_result(result.model_dump(), args)


def _update(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    if args.name and "name" not in body:
        body["name"] = args.name
    if args.description and "description" not in body:
        body["description"] = args.description

    # 部分更新。name / description のいずれも無ければ no-op になるので弾く。
    if not body:
        raise CLIError("at least one of --name / --description (or --json) is required")

    if args.dry_run:
        print_dry_run("PUT", f"/tags/{args.id}", body)
        return
    validate_id(args.id, label="id")
    client = get_client(args)
    result = client.put(f"/tags/{args.id}", body=body, cast_to=Tag)
    print_result(result.model_dump(), args)


def _delete(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("DELETE", f"/tags/{args.id}")
        return
    validate_id(args.id, label="id")
    require_yes(args, action="tags.delete")
    client = get_client(args)
    result = client.delete(f"/tags/{args.id}", cast_to=Tag)
    print_result(result.model_dump(), args)
