from __future__ import annotations

from typing import TYPE_CHECKING, Any
from argparse import ArgumentParser

from .._utils import get_client
from ._common import (
    add_yes,
    add_fields,
    add_dry_run,
    require_yes,
    print_result,
    print_dry_run,
    add_json_param,
    parse_json_body,
    validate_loose_id,
    validate_json_body_fields,
)
from ..._types import omit
from .._errors import CLIError

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction

_ALLOWED_UPDATE_BODY_KEYS = frozenset({"title", "current_leaf_id"})


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser("conversations.list", help="List conversations")
    sub.add_argument("--limit", type=int, help="Maximum number of results")
    sub.add_argument("--offset", type=int, help="Number of results to skip")
    sub.add_argument("--principal-id", help="Principal scope")
    sub.add_argument(
        "--all-principals",
        action="store_true",
        help="Return conversations across all principals",
    )
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list)

    sub = subparser.add_parser("conversations.retrieve", help="Get a conversation")
    sub.add_argument("-i", "--id", required=True, dest="conversation_id", help="Conversation ID")
    sub.add_argument("--leaf-id", help="Leaf node used to preview a branch")
    sub.add_argument("--principal-id", help="Principal scope")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve)

    sub = subparser.add_parser("conversations.update", help="Update a conversation")
    sub.add_argument("-i", "--id", required=True, dest="conversation_id", help="Conversation ID")
    add_json_param(sub)
    sub.add_argument("--title", help="New conversation title")
    sub.add_argument("--current-leaf-id", help="Node to use as the active branch leaf")
    sub.add_argument("--principal-id", help="Principal scope")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_update)

    sub = subparser.add_parser("conversations.delete", help="Delete a conversation")
    sub.add_argument("-i", "--id", required=True, dest="conversation_id", help="Conversation ID")
    sub.add_argument("--principal-id", help="Principal scope")
    add_dry_run(sub)
    add_yes(sub)
    sub.set_defaults(func=_delete)


def _list(args: Namespace) -> None:
    params: dict[str, Any] = {}
    if args.limit is not None:
        params["limit"] = args.limit
    if args.offset is not None:
        params["offset"] = args.offset
    if args.principal_id is not None:
        params["principal_id"] = args.principal_id
    if args.all_principals:
        params["all_principals"] = True

    if args.dry_run:
        print_dry_run("GET", "/conversations", params if params else None)
        return

    client = get_client(args)
    result = client.conversations.list(
        limit=args.limit if args.limit is not None else omit,
        offset=args.offset if args.offset is not None else omit,
        principal_id=args.principal_id if args.principal_id is not None else omit,
        all_principals=True if args.all_principals else omit,
    )
    print_result(result.model_dump(), args)


def _retrieve(args: Namespace) -> None:
    params: dict[str, Any] = {}
    if args.leaf_id is not None:
        params["leaf_id"] = args.leaf_id
    if args.principal_id is not None:
        params["principal_id"] = args.principal_id

    if args.dry_run:
        print_dry_run(
            "GET",
            f"/conversations/{args.conversation_id}",
            params if params else None,
        )
        return

    validate_loose_id(args.conversation_id, label="conversation_id")
    client = get_client(args)
    result = client.conversations.retrieve(
        args.conversation_id,
        leaf_id=args.leaf_id if args.leaf_id is not None else omit,
        principal_id=args.principal_id if args.principal_id is not None else omit,
    )
    print_result(result.model_dump(), args)


def _update(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    if args.title is not None and "title" not in body:
        body["title"] = args.title
    if args.current_leaf_id is not None and "current_leaf_id" not in body:
        body["current_leaf_id"] = args.current_leaf_id
    validate_json_body_fields(body, allowed=_ALLOWED_UPDATE_BODY_KEYS)
    if not body:
        raise CLIError("at least one of --title / --current-leaf-id (or --json) is required")

    params = {"principal_id": args.principal_id} if args.principal_id is not None else None
    if args.dry_run:
        print_dry_run(
            "PATCH",
            f"/conversations/{args.conversation_id}",
            body,
            query=params,
        )
        return

    validate_loose_id(args.conversation_id, label="conversation_id")
    client = get_client(args)
    result = client.conversations.update(
        args.conversation_id,
        title=body["title"] if "title" in body else omit,
        current_leaf_id=body["current_leaf_id"] if "current_leaf_id" in body else omit,
        principal_id=args.principal_id if args.principal_id is not None else omit,
    )
    print_result(result.model_dump(), args)


def _delete(args: Namespace) -> None:
    params = {"principal_id": args.principal_id} if args.principal_id is not None else None
    if args.dry_run:
        print_dry_run("DELETE", f"/conversations/{args.conversation_id}", params)
        return

    validate_loose_id(args.conversation_id, label="conversation_id")
    require_yes(args, action="conversations.delete")
    client = get_client(args)
    result = client.conversations.delete(
        args.conversation_id,
        principal_id=args.principal_id if args.principal_id is not None else omit,
    )
    print_result(result, args)
