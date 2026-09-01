from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any, cast
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
    validate_loose_id,
    validate_json_body_fields,
)
from ..._types import omit
from .._errors import CLIError
from ...types.create_agent_run_input_param import CreateAgentRunInputParam

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction

_RUN_BODY_KEYS = frozenset(
    {
        "context",
        "forwarded_props",
        "messages",
        "parent_run_id",
        "redaction_policy_id",
        "resume",
        "state",
        "thread_id",
        "tools",
    }
)
_CREATE_RUN_BODY_KEYS = frozenset({"input", "idempotency_key"})


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser(
        "agent.run",
        help="Run an agent and stream events (AG-UI)",
    )
    add_json_param(sub)
    sub.add_argument("--messages", help="Messages as JSON array")
    sub.add_argument("--thread-id", help="Optional ID for the thread")
    sub.add_argument("--redaction-policy-id", help="Optional redaction policy ID")
    sub.add_argument(
        "--forwarded-props",
        help="Forwarded props as JSON object (AG-UI standard)",
    )
    add_dry_run(sub)
    sub.set_defaults(func=_run)

    sub = subparser.add_parser("agent.create_run", help="Create an asynchronous agent run")
    add_json_param(sub)
    sub.add_argument("--messages", help="Messages as JSON array for input.messages")
    sub.add_argument("--thread-id", help="Optional thread ID for input.thread_id")
    sub.add_argument("--redaction-policy-id", help="Optional redaction policy ID for input.redaction_policy_id")
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

    sub = subparser.add_parser("agent.stream_run_events", help="Stream persisted agent run events")
    sub.add_argument("-i", "--id", required=True, dest="run_id", help="Run ID")
    sub.add_argument("--after", type=int, help="Last persisted event index received")
    sub.add_argument(
        "--last-event-id",
        help="SSE reconnect cursor used when --after is omitted",
    )
    sub.add_argument("--principal-id", help="Principal scope")
    add_dry_run(sub)
    sub.set_defaults(func=_stream_run_events)

    sub = subparser.add_parser("agent.list_threads", help="List agent conversation threads")
    sub.add_argument("--limit", type=int, help="Maximum number of results")
    sub.add_argument("--offset", type=int, help="Number of results to skip")
    sub.add_argument("--principal-id", help="Principal scope")
    sub.add_argument(
        "--all-principals",
        action="store_true",
        help="Return threads across all principals",
    )
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list_threads)

    sub = subparser.add_parser("agent.retrieve_thread", help="Get an agent thread's run tree")
    sub.add_argument("-i", "--id", required=True, dest="thread_id", help="Thread ID")
    sub.add_argument("--principal-id", help="Principal scope")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve_thread)


def _collect_agent_input_fields(args: Namespace, target: dict[str, Any]) -> None:
    """CLI フラグから messages/thread_id/redaction_policy_id/forwarded_props を target に埋める。

    既に target に存在するキーは上書きしない。
    """
    if args.messages and "messages" not in target:
        target["messages"] = parse_json_arg(args.messages, label="--messages")
    if args.thread_id and "thread_id" not in target:
        target["thread_id"] = validate_loose_id(args.thread_id, label="thread_id")
    if args.redaction_policy_id and "redaction_policy_id" not in target:
        target["redaction_policy_id"] = validate_loose_id(
            args.redaction_policy_id,
            label="redaction_policy_id",
        )
    if args.forwarded_props and "forwarded_props" not in target:
        target["forwarded_props"] = parse_json_arg(args.forwarded_props, label="--forwarded-props")


def _build_agent_body(args: Namespace) -> dict[str, Any]:
    """agent.run の body を組み立てる"""
    body = parse_json_body(args) or {}
    _collect_agent_input_fields(args, body)
    validate_json_body_fields(body, allowed=_RUN_BODY_KEYS)
    return body


def _run(args: Namespace) -> None:
    body = _build_agent_body(args)

    if args.dry_run:
        print_dry_run("POST", "/agent/runs", {"input": body})
        return

    client = get_client(args)
    run = client.agent.create_run(input=cast(CreateAgentRunInputParam, body))
    forwarded_props = body.get("forwarded_props")
    principal_id: str | None = None
    if isinstance(forwarded_props, dict):
        candidate = cast(dict[str, Any], forwarded_props).get("principal_id")
        if isinstance(candidate, str):
            principal_id = candidate
    stream = client.agent.stream_run_events(
        run.run_id,
        principal_id=principal_id if principal_id is not None else omit,
    )
    for event in stream:
        # Stream[AgentStreamRunEventsResponse] は SSE data を文字列として返す。
        sys.stdout.write(event + "\n")
        sys.stdout.flush()


def _create_run(args: Namespace) -> None:
    body = parse_json_body(args) or {}
    validate_json_body_fields(body, allowed=_CREATE_RUN_BODY_KEYS)

    # --json で直接 input を渡された場合はそれを使う。
    # そうでなければ、CLIフラグから input 構造を組み立てる。
    if "input" not in body:
        input_obj: dict[str, Any] = {}
        _collect_agent_input_fields(args, input_obj)
        if not input_obj:
            raise CLIError(
                "--json with 'input' field, or at least one of "
                "--messages/--thread-id/--redaction-policy-id/--forwarded-props is required"
            )
        body["input"] = input_obj

    if args.idempotency_key and "idempotency_key" not in body:
        body["idempotency_key"] = args.idempotency_key

    idempotency_key = body.pop("idempotency_key", None)

    if args.dry_run:
        headers = {"Idempotency-Key": idempotency_key} if idempotency_key is not None else None
        print_dry_run("POST", "/agent/runs", body, headers=headers)
        return
    client = get_client(args)
    result = client.agent.create_run(
        input=cast(CreateAgentRunInputParam, body["input"]),
        idempotency_key=idempotency_key if idempotency_key is not None else omit,
    )
    print_result(result.model_dump(), args)


def _retrieve_run(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/agent/runs/{args.run_id}")
        return
    validate_loose_id(args.run_id, label="run_id")
    client = get_client(args)
    result = client.agent.retrieve_run(args.run_id)
    print_result(result.model_dump(), args)


def _cancel_run(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("POST", f"/agent/runs/{args.run_id}/cancel")
        return
    validate_loose_id(args.run_id, label="run_id")
    client = get_client(args)
    result = client.agent.cancel_run(args.run_id)
    print_result(result.model_dump(), args)


def _retrieve_run_result(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", f"/agent/runs/{args.run_id}/result")
        return
    validate_loose_id(args.run_id, label="run_id")
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
    validate_loose_id(args.run_id, label="run_id")
    client = get_client(args)
    result = client.agent.list_run_events(
        args.run_id,
        limit=limit if limit is not None else omit,
        after=after if after is not None else omit,
    )
    print_result(result.model_dump(), args)


def _stream_run_events(args: Namespace) -> None:
    params: dict[str, Any] = {}
    if args.after is not None:
        params["after"] = args.after
    if args.principal_id is not None:
        params["principal_id"] = args.principal_id

    if args.dry_run:
        headers = {"Last-Event-ID": args.last_event_id} if args.last_event_id is not None else None
        print_dry_run(
            "GET",
            f"/agent/runs/{args.run_id}/events/stream",
            headers=headers,
            query=params if params else None,
        )
        return

    validate_loose_id(args.run_id, label="run_id")
    client = get_client(args)
    stream = client.agent.stream_run_events(
        args.run_id,
        after=args.after if args.after is not None else omit,
        last_event_id=args.last_event_id if args.last_event_id is not None else omit,
        principal_id=args.principal_id if args.principal_id is not None else omit,
    )
    for event in stream:
        sys.stdout.write(event + "\n")
        sys.stdout.flush()


def _list_threads(args: Namespace) -> None:
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
        print_dry_run("GET", "/agent/threads", params if params else None)
        return

    client = get_client(args)
    result = client.agent.list_threads(
        limit=args.limit if args.limit is not None else omit,
        offset=args.offset if args.offset is not None else omit,
        principal_id=args.principal_id if args.principal_id is not None else omit,
        all_principals=True if args.all_principals else omit,
    )
    print_result(result.model_dump(), args)


def _retrieve_thread(args: Namespace) -> None:
    if args.dry_run:
        params = {"principal_id": args.principal_id} if args.principal_id is not None else None
        print_dry_run("GET", f"/agent/threads/{args.thread_id}", params)
        return

    validate_loose_id(args.thread_id, label="thread_id")
    client = get_client(args)
    result = client.agent.retrieve_thread(
        args.thread_id,
        principal_id=args.principal_id if args.principal_id is not None else omit,
    )
    print_result(result.model_dump(), args)
