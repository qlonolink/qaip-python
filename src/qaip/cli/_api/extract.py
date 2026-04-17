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
    sub = subparser.add_parser("extract.create", help="Extract structured data from indexed content")

    add_json_param(sub)
    sub.add_argument("--schema", dest="extract_schema", help="JSON Schema for extraction (as JSON string)")
    sub.add_argument("--prompt", help="Additional prompt for the LLM")
    sub.add_argument("--tags", help="Comma-separated tag names")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create)


def _create(args: Namespace) -> None:
    body = parse_json_body(args) or {}

    if args.extract_schema and "schema" not in body:
        body["schema"] = parse_json_arg(args.extract_schema, label="--schema")
    if args.prompt and "prompt" not in body:
        body["prompt"] = args.prompt
    if args.tags and "tags" not in body:
        body["tags"] = [t.strip() for t in args.tags.split(",")]

    if "schema" not in body:
        raise CLIError("--schema or --json with 'schema' field is required")

    if args.dry_run:
        print_dry_run("POST", "/extract", body)
        return

    client = get_client(args)
    result = client.extract(**body)
    print_result(result.model_dump(), args)
