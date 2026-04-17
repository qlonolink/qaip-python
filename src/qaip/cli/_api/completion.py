from __future__ import annotations

from typing import TYPE_CHECKING
from argparse import ArgumentParser

from .._utils import get_client
from ._common import (
    add_fields,
    add_dry_run,
    print_result,
    print_dry_run,
    add_json_param,
    parse_json_arg,
    parse_json_body,
)
from .._errors import CLIError

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser("completion.create", help="Generate AI completions")

    add_json_param(sub)
    sub.add_argument("-m", "--messages", help="Messages as JSON array (e.g. '[{\"role\":\"user\",\"content\":\"hello\"}]')")
    sub.add_argument("--tags", help="Comma-separated tag names")
    sub.add_argument("--citation", action="store_true", default=None, help="Include citations")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create)


def _create(args: Namespace) -> None:
    body = parse_json_body(args) or {}

    if args.messages and "messages" not in body:
        body["messages"] = parse_json_arg(args.messages, label="--messages")
    if args.tags and "tags" not in body:
        body["tags"] = [t.strip() for t in args.tags.split(",")]
    if args.citation is not None and "citation" not in body:
        body["citation"] = args.citation

    if "messages" not in body:
        raise CLIError("--messages or --json with 'messages' field is required")

    if args.dry_run:
        print_dry_run("POST", "/completions", body)
        return

    client = get_client(args)
    result = client.completion(**body)
    print_result(result.model_dump(), args)
