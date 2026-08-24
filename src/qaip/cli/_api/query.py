from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast
from argparse import ArgumentParser

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
    validate_json_body_fields,
)
from .._errors import CLIError, mark_non_retryable
from ..._exceptions import APIStatusError

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction

_ALLOWED_CREATE_BODY_KEYS = frozenset({"sql"})


def _outcome_unknown_location(err: APIStatusError) -> str | None:
    body = err.body
    if not isinstance(body, dict):
        return None
    error = cast(dict[str, Any], body).get("error")
    if not isinstance(error, dict) or cast(dict[str, Any], error).get("type") != "outcome_unknown":
        return None
    return err.response.headers.get("location") or ""


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser("query.create", help="Query external tables")
    add_json_param(sub)
    sub.add_argument("--sql", help="A single read-only SELECT")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create)

    sub = subparser.add_parser("query.retrieve_schema", help="Get external table schema")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve_schema)

    sub = subparser.add_parser("query.retrieve", help="Get external query state")
    sub.add_argument("-i", "--id", required=True, dest="request_id", help="Request ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve)

    sub = subparser.add_parser("query.cancel", help="Cancel an external query")
    sub.add_argument("-i", "--id", required=True, dest="request_id", help="Request ID")
    add_dry_run(sub)
    add_yes(sub)
    add_fields(sub)
    sub.set_defaults(func=_cancel)


def _create(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    if args.sql is not None and "sql" not in body:
        body["sql"] = args.sql
    if "sql" not in body:
        raise CLIError("--sql or --json with 'sql' field is required")
    validate_json_body_fields(body, allowed=_ALLOWED_CREATE_BODY_KEYS)

    if args.dry_run:
        print_dry_run("POST", "/query", body)
        return

    client = get_client(args)
    try:
        response = client.external_queries.with_raw_response.create(sql=body["sql"])
    except APIStatusError as err:
        location = _outcome_unknown_location(err)
        if location is not None:
            hint = "External query outcome is unknown. Check its retained status before retrying."
            if location:
                hint = f"{hint} Retrieve {location}."
            mark_non_retryable(err, hint)
        raise

    result = response.parse().model_dump()
    location = response.headers.get("location")
    if location is not None:
        result["location"] = location
    retry_after = response.headers.get("retry-after")
    if retry_after is not None:
        try:
            result["retry_after_seconds"] = int(retry_after)
        except ValueError:
            result["retry_after_seconds"] = retry_after
    print_result(result, args)


def _retrieve_schema(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", "/query/schema")
        return

    client = get_client(args)
    result = client.external_queries.retrieve_schema()
    print_result(result.model_dump(), args)


def _retrieve(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/query/{args.request_id}")
        return

    validate_id(args.request_id, label="request_id")
    client = get_client(args)
    result = client.external_queries.retrieve(args.request_id)
    print_result(result.model_dump(), args)


def _cancel(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("DELETE", f"/query/{args.request_id}")
        return

    validate_id(args.request_id, label="request_id")
    require_yes(args, action="query.cancel")
    client = get_client(args)
    result = client.external_queries.cancel(args.request_id)
    print_result(result.model_dump(), args)
