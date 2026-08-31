from __future__ import annotations

from typing import TYPE_CHECKING
from argparse import ArgumentParser

from .._utils import get_client
from ._common import add_fields, add_dry_run, validate_id, print_result, print_dry_run, add_json_param, parse_json_body
from .._errors import CLIError

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser("search.create", help="Search indexed content")

    add_json_param(sub)
    sub.add_argument("-q", "--query", help="Search query string")
    sub.add_argument("--tags", help="Comma-separated tag names")
    sub.add_argument(
        "--source-group-id",
        help="Source group ID to search within (for crawl data, use the crawl ID)",
    )
    sub.add_argument("--limit", type=int, help="Maximum number of results")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create)


def _create(args: Namespace) -> None:
    body = parse_json_body(args) or {}

    if args.query and "query" not in body:
        body["query"] = args.query
    if args.tags and "tags" not in body:
        body["tags"] = [t.strip() for t in args.tags.split(",")]
    if args.source_group_id is not None and "source_group_id" not in body:
        body["source_group_id"] = args.source_group_id
    if args.limit is not None and "limit" not in body:
        body["limit"] = args.limit

    if "query" not in body:
        raise CLIError("--query or --json with 'query' field is required")

    if args.dry_run:
        print_dry_run("POST", "/search", body)
        return

    source_group_id = body.get("source_group_id")
    if source_group_id is not None:
        if not isinstance(source_group_id, str):
            raise CLIError("source_group_id must be a UUID string", code="invalid_id")
        validate_id(source_group_id, label="source_group_id")

    client = get_client(args)
    result = client.search(**body)
    print_result(result.model_dump(), args)
