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
    sub = subparser.add_parser("google-drives.create", help="Create a Google Drive integration")
    add_json_param(sub)
    sub.add_argument("--name", help="Name")
    sub.add_argument("--folder-url", help="Google Drive folder URL")
    sub.add_argument(
        "--secret-id",
        help="Stored secret ID (mutually exclusive with --service-account-key)",
    )
    sub.add_argument(
        "--service-account-key",
        help="One-time service account key JSON (mutually exclusive with --secret-id)",
    )
    sub.add_argument("--rrule", help="Recurrence rule (RFC 5545 RRULE)")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create)

    sub = subparser.add_parser("google-drives.retrieve", help="Get a Google Drive integration by ID")
    sub.add_argument("-i", "--id", required=True, help="Google Drive ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve)

    sub = subparser.add_parser("google-drives.list", help="List Google Drive integrations")
    sub.add_argument("--limit", type=int, help="Maximum number of results")
    sub.add_argument("--after-id", help="Cursor for pagination")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list)

    sub = subparser.add_parser("google-drives.delete", help="Delete a Google Drive integration")
    sub.add_argument("-i", "--id", required=True, help="Google Drive ID")
    add_dry_run(sub)
    sub.set_defaults(func=_delete)

    sub = subparser.add_parser("google-drives.retrieve_setting", help="Get Google Drive settings")
    sub.add_argument("-i", "--id", required=True, help="Google Drive ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve_setting)

    sub = subparser.add_parser("google-drives.update_setting", help="Update Google Drive settings")
    sub.add_argument("-i", "--id", required=True, help="Google Drive ID")
    add_json_param(sub)
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_update_setting)


def _create(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    if args.name and "name" not in body:
        body["name"] = args.name
    if args.folder_url and "folder_url" not in body:
        body["folder_url"] = args.folder_url
    if args.secret_id and "secret_id" not in body:
        body["secret_id"] = args.secret_id
    if args.service_account_key and "service_account_key" not in body:
        body["service_account_key"] = args.service_account_key
    if args.rrule and "rrule" not in body:
        body["rrule"] = args.rrule

    for field in ("name", "folder_url"):
        if field not in body:
            raise CLIError(f"--{field.replace('_', '-')} or --json with '{field}' field is required")

    if args.dry_run:
        print_dry_run("POST", "/google-drives", body, sensitive_keys=("service_account_key",))
        return
    client = get_client(args)
    result = client.google_drives.create(**body)
    print_result(result.model_dump(), args)


def _retrieve(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/google-drives/{args.id}")
        return
    client = get_client(args)
    result = client.google_drives.retrieve(args.id)
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
        print_dry_run("GET", "/google-drives", params if params else None)
        return
    client = get_client(args)
    result = client.google_drives.list(
        limit=limit if limit is not None else omit,
        after_id=after_id if after_id is not None else omit,
    )
    print_result(result.model_dump(), args)


def _delete(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("DELETE", f"/google-drives/{args.id}")
        return
    client = get_client(args)
    result = client.google_drives.delete(args.id)
    print_result(result.model_dump(), args)


def _retrieve_setting(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/google-drive-settings/{args.id}")
        return
    client = get_client(args)
    result = client.google_drives.retrieve_setting(args.id)
    print_result(result.model_dump(), args)


def _update_setting(args: Namespace) -> None:
    body = parse_json_body(args)
    if body is None:
        raise CLIError("--json is required for update_setting")
    if args.dry_run:
        print_dry_run("PUT", f"/google-drive-settings/{args.id}", body)
        return
    client = get_client(args)
    result = client.google_drives.update_setting(args.id, **body)
    print_result(result.model_dump(), args)
