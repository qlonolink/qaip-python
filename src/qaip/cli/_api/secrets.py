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
    sub = subparser.add_parser("secrets.create", help="Create a secret")
    add_json_param(sub)
    sub.add_argument("--name", help="Secret name")
    sub.add_argument("--secret", help="Secret value")
    sub.add_argument("--type", dest="secret_type", help="Secret type")
    sub.add_argument("--description", help="Secret description")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create)

    sub = subparser.add_parser("secrets.retrieve", help="Get a secret by ID")
    sub.add_argument("-i", "--id", required=True, dest="secret_id", help="Secret ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve)

    sub = subparser.add_parser("secrets.update", help="Update a secret")
    sub.add_argument("-i", "--id", required=True, dest="secret_id", help="Secret ID")
    add_json_param(sub)
    sub.add_argument("--name", help="Secret name")
    sub.add_argument("--description", help="Secret description")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_update)

    sub = subparser.add_parser("secrets.list", help="List secrets")
    sub.add_argument("--limit", type=int, help="Maximum number of results")
    sub.add_argument("--after-id", help="Cursor for pagination")
    sub.add_argument("--type", dest="secret_type", help="Filter by secret type")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list)

    sub = subparser.add_parser("secrets.delete", help="Delete a secret")
    sub.add_argument("-i", "--id", required=True, dest="secret_id", help="Secret ID")
    add_dry_run(sub)
    sub.set_defaults(func=_delete)


def _create(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    if args.name and "name" not in body:
        body["name"] = args.name
    if args.secret and "secret" not in body:
        body["secret"] = args.secret
    if args.secret_type and "type" not in body:
        body["type"] = args.secret_type
    if args.description and "description" not in body:
        body["description"] = args.description

    for field in ("name", "secret", "type"):
        if field not in body:
            raise CLIError(f"--{field} or --json with '{field}' field is required")

    if args.dry_run:
        print_dry_run("POST", "/secrets", body, sensitive_keys=("secret",))
        return
    client = get_client(args)
    result = client.secrets.create(**body)
    print_result(result.model_dump(), args)


def _retrieve(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/secrets/{args.secret_id}")
        return
    client = get_client(args)
    result = client.secrets.retrieve(args.secret_id)
    print_result(result.model_dump(), args)


def _update(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    if args.name and "name" not in body:
        body["name"] = args.name
    if args.description and "description" not in body:
        body["description"] = args.description

    if "name" not in body:
        raise CLIError("--name or --json with 'name' field is required")

    if args.dry_run:
        print_dry_run("PUT", f"/secrets/{args.secret_id}", body, sensitive_keys=("secret",))
        return
    client = get_client(args)
    result = client.secrets.update(args.secret_id, **body)
    print_result(result.model_dump(), args)


def _list(args: Namespace) -> None:
    limit: int | None = args.limit
    after_id: str | None = args.after_id
    secret_type: str | None = args.secret_type

    if args.dry_run:
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if after_id is not None:
            params["after_id"] = after_id
        if secret_type is not None:
            params["secret_type"] = secret_type
        print_dry_run("GET", "/secrets", params if params else None)
        return
    client = get_client(args)
    result = client.secrets.list(
        limit=limit if limit is not None else omit,
        after_id=after_id if after_id is not None else omit,
        secret_type=secret_type if secret_type is not None else omit,  # type: ignore[arg-type]
    )
    print_result(result.model_dump(), args)


def _delete(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("DELETE", f"/secrets/{args.secret_id}")
        return
    client = get_client(args)
    result = client.secrets.delete(args.secret_id)
    print_result(result.model_dump(), args)
