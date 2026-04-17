from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any
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
from ..._types import omit
from .._errors import CLIError

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser(
        "agent.run",
        help="Run an agent and stream events (AG-UI)",
    )
    add_json_param(sub)
    sub.add_argument("--messages", help="Messages as JSON array")
    sub.add_argument("--run-id", help="Optional ID for the run")
    sub.add_argument("--thread-id", help="Optional ID for the thread")
    sub.add_argument(
        "--forwarded-props",
        help="Forwarded props as JSON object (AG-UI standard)",
    )
    add_dry_run(sub)
    sub.set_defaults(func=_run)

    sub = subparser.add_parser("agent.create_run", help="Create an asynchronous agent run")
    add_json_param(sub)
    sub.add_argument("--messages", help="Messages as JSON array for input.messages")
    sub.add_argument("--run-id", help="Optional run ID for input.run_id")
    sub.add_argument("--thread-id", help="Optional thread ID for input.thread_id")
    sub.add_argument(
        "--forwarded-props",
        help="Forwarded props as JSON object for input.forwarded_props",
    )
    sub.add_argument("--idempotency-key", help="Idempotency key for reusing an existing run")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create_run)

    sub = subparser.add_parser("agent.retrieve_run", help="Get an agent run by ID")
    sub.add_argument("-i", "--id", required=True, dest="run_id", help="Run ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve_run)

    sub = subparser.add_parser("agent.cancel_run", help="Cancel an agent run")
    sub.add_argument("-i", "--id", required=True, dest="run_id", help="Run ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_cancel_run)

    sub = subparser.add_parser("agent.retrieve_run_result", help="Get agent run result")
    sub.add_argument("-i", "--id", required=True, dest="run_id", help="Run ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve_run_result)

    sub = subparser.add_parser("agent.list_run_events", help="List agent run events")
    sub.add_argument("-i", "--id", required=True, dest="run_id", help="Run ID")
    sub.add_argument("--limit", type=int, help="Maximum number of results")
    sub.add_argument("--after", type=int, help="Cursor for pagination (event ID)")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list_run_events)


def _collect_agent_input_fields(args: Namespace, target: dict[str, Any]) -> None:
    """CLI フラグから messages/run_id/thread_id/forwarded_props を target に埋める。

    既に target に存在するキーは上書きしない。
    """
    if args.messages and "messages" not in target:
        target["messages"] = parse_json_arg(args.messages, label="--messages")
    if args.run_id and "run_id" not in target:
        target["run_id"] = args.run_id
    if args.thread_id and "thread_id" not in target:
        target["thread_id"] = args.thread_id
    if args.forwarded_props and "forwarded_props" not in target:
        target["forwarded_props"] = parse_json_arg(
            args.forwarded_props, label="--forwarded-props"
        )


def _build_agent_body(args: Namespace) -> dict[str, Any]:
    """agent.run の body を組み立てる"""
    body = parse_json_body(args) or {}
    _collect_agent_input_fields(args, body)
    return body


def _run(args: Namespace) -> None:
    body = _build_agent_body(args)

    if args.dry_run:
        print_dry_run("POST", "/agent/run", body if body else None)
        return

    client = get_client(args)
    stream = client.agent.run(**body)
    for event in stream:
        # Stream[AgentRunResponse] の要素は text/event-stream を行単位にパースした str。
        sys.stdout.write(event + "\n")
        sys.stdout.flush()


def _create_run(args: Namespace) -> None:
    body = parse_json_body(args) or {}

    # --json で直接 input を渡された場合はそれを使う。
    # そうでなければ、CLIフラグから input 構造を組み立てる。
    if "input" not in body:
        input_obj: dict[str, Any] = {}
        _collect_agent_input_fields(args, input_obj)
        if not input_obj:
            raise CLIError(
                "--json with 'input' field, or at least one of --messages/--run-id/--thread-id/--forwarded-props is required"
            )
        body["input"] = input_obj

    if args.idempotency_key and "idempotency_key" not in body:
        body["idempotency_key"] = args.idempotency_key

    if args.dry_run:
        print_dry_run("POST", "/agent/runs", body)
        return
    client = get_client(args)
    result = client.agent.create_run(**body)
    print_result(result.model_dump(), args)


def _retrieve_run(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/agent/runs/{args.run_id}")
        return
    client = get_client(args)
    result = client.agent.retrieve_run(args.run_id)
    print_result(result.model_dump(), args)


def _cancel_run(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("POST", f"/agent/runs/{args.run_id}/cancel")
        return
    client = get_client(args)
    result = client.agent.cancel_run(args.run_id)
    print_result(result.model_dump(), args)


def _retrieve_run_result(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/agent/runs/{args.run_id}/result")
        return
    client = get_client(args)
    result = client.agent.retrieve_run_result(args.run_id)
    print_result(result.model_dump(), args)


def _list_run_events(args: Namespace) -> None:
    limit: int | None = args.limit
    after: int | None = args.after

    if args.dry_run:
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if after is not None:
            params["after"] = after
        print_dry_run("GET", f"/agent/runs/{args.run_id}/events", params if params else None)
        return
    client = get_client(args)
    result = client.agent.list_run_events(
        args.run_id,
        limit=limit if limit is not None else omit,
        after=after if after is not None else omit,
    )
    print_result(result.model_dump(), args)
