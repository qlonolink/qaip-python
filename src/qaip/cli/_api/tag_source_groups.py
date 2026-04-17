from __future__ import annotations

from typing import TYPE_CHECKING
from argparse import ArgumentParser

from .._utils import get_client
from ._common import add_fields, add_dry_run, print_result, print_dry_run, add_json_param, parse_json_body
from .._errors import CLIError

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser("tag-source-groups.create", help="Create a tag-source-group association")
    add_json_param(sub)
    sub.add_argument("--tag-id", help="Tag ID")
    sub.add_argument("--source-group-id", help="Source group ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create)

    sub = subparser.add_parser("tag-source-groups.delete", help="Delete a tag-source-group association")
    add_json_param(sub)
    sub.add_argument("--tag-id", help="Tag ID")
    sub.add_argument("--source-group-id", help="Source group ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_delete)


def _create(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    if args.tag_id and "tag_id" not in body:
        body["tag_id"] = args.tag_id
    if args.source_group_id and "source_group_id" not in body:
        body["source_group_id"] = args.source_group_id

    for field in ("tag_id", "source_group_id"):
        if field not in body:
            raise CLIError(f"--{field.replace('_', '-')} or --json with '{field}' field is required")

    if args.dry_run:
        print_dry_run("POST", "/tag-source-groups", body)
        return
    client = get_client(args)
    result = client.tag_source_groups.create(**body)
    print_result(result.model_dump(), args)


def _delete(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    if args.tag_id and "tag_id" not in body:
        body["tag_id"] = args.tag_id
    if args.source_group_id and "source_group_id" not in body:
        body["source_group_id"] = args.source_group_id

    for field in ("tag_id", "source_group_id"):
        if field not in body:
            raise CLIError(f"--{field.replace('_', '-')} or --json with '{field}' field is required")

    if args.dry_run:
        print_dry_run("DELETE", "/tag-source-groups", body)
        return
    client = get_client(args)
    result = client.tag_source_groups.delete(**body)
    print_result(result.model_dump(), args)
