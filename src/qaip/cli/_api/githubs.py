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
    sub = subparser.add_parser("githubs.create", help="Create a GitHub integration")
    add_json_param(sub)
    sub.add_argument("--name", help="Name")
    sub.add_argument("--repository", help="GitHub repository in owner/repo format (e.g. octocat/Hello-World)")
    sub.add_argument("--secret-id", help="Stored secret ID (mutually exclusive with --github-token)")
    sub.add_argument("--github-token", help="One-time GitHub PAT (mutually exclusive with --secret-id)")
    sub.add_argument("--reference", dest="reference_param", help="Branch name, tag name, or commit hash")
    sub.add_argument("--reference-type", help="Git reference type (branch, tag, or commit)")
    sub.add_argument("--path-filters", help="Comma-separated path filter patterns")
    sub.add_argument("--rrule", help="Recurrence rule (RFC 5545 RRULE)")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create)

    sub = subparser.add_parser("githubs.retrieve", help="Get a GitHub integration by ID")
    sub.add_argument("-i", "--id", required=True, help="GitHub integration ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve)

    sub = subparser.add_parser("githubs.list", help="List GitHub integrations")
    sub.add_argument("--limit", type=int, help="Maximum number of results")
    sub.add_argument("--after-id", help="Cursor for pagination")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list)

    sub = subparser.add_parser("githubs.delete", help="Delete a GitHub integration")
    sub.add_argument("-i", "--id", required=True, help="GitHub integration ID")
    add_dry_run(sub)
    sub.set_defaults(func=_delete)

    sub = subparser.add_parser("githubs.retrieve_setting", help="Get GitHub settings")
    sub.add_argument("-i", "--id", required=True, help="GitHub integration ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve_setting)

    sub = subparser.add_parser("githubs.update_setting", help="Update GitHub settings")
    sub.add_argument("-i", "--id", required=True, help="GitHub integration ID")
    add_json_param(sub)
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_update_setting)


def _create(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    if args.name and "name" not in body:
        body["name"] = args.name
    if args.repository and "repository" not in body:
        body["repository"] = args.repository
    if args.secret_id and "secret_id" not in body:
        body["secret_id"] = args.secret_id
    if args.github_token and "github_token" not in body:
        body["github_token"] = args.github_token
    if args.reference_param and "reference_param" not in body:
        body["reference_param"] = args.reference_param
    if args.reference_type and "reference_type" not in body:
        body["reference_type"] = args.reference_type
    if args.path_filters and "path_filters" not in body:
        body["path_filters"] = [p.strip() for p in args.path_filters.split(",")]
    if args.rrule and "rrule" not in body:
        body["rrule"] = args.rrule

    for field in ("name", "repository"):
        if field not in body:
            raise CLIError(f"--{field.replace('_', '-')} or --json with '{field}' field is required")

    if args.dry_run:
        print_dry_run("POST", "/githubs", body, sensitive_keys=("github_token",))
        return
    client = get_client(args)
    result = client.githubs.create(**body)
    print_result(result.model_dump(), args)


def _retrieve(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/githubs/{args.id}")
        return
    client = get_client(args)
    result = client.githubs.retrieve(args.id)
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
        print_dry_run("GET", "/githubs", params if params else None)
        return
    client = get_client(args)
    result = client.githubs.list(
        limit=limit if limit is not None else omit,
        after_id=after_id if after_id is not None else omit,
    )
    print_result(result.model_dump(), args)


def _delete(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("DELETE", f"/githubs/{args.id}")
        return
    client = get_client(args)
    result = client.githubs.delete(args.id)
    print_result(result.model_dump(), args)


def _retrieve_setting(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/github-settings/{args.id}")
        return
    client = get_client(args)
    result = client.githubs.retrieve_setting(args.id)
    print_result(result.model_dump(), args)


def _update_setting(args: Namespace) -> None:
    body = parse_json_body(args)
    if body is None:
        raise CLIError("--json is required for update_setting")
    if args.dry_run:
        print_dry_run("PUT", f"/github-settings/{args.id}", body)
        return
    client = get_client(args)
    result = client.githubs.update_setting(args.id, **body)
    print_result(result.model_dump(), args)
