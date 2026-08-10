from __future__ import annotations

from typing import TYPE_CHECKING, Any, get_args
from argparse import ArgumentParser

from .._utils import get_client
from ._common import (
    add_dry_run,
    print_result,
    print_dry_run,
    add_json_param,
    parse_json_body,
)
from ..._types import omit
from .._errors import CLIError, mark_non_retryable
from ..._exceptions import APIStatusError
from ...types.issuable_api_key_scope import IssuableApiKeyScope

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction

_ISSUABLE_SCOPES: tuple[str, ...] = get_args(IssuableApiKeyScope)


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser(
        "api-keys.create",
        help="Issue an API key scoped to a subset of the calling key's scopes",
    )
    add_json_param(sub)
    sub.add_argument("--name", help="API key name")
    sub.add_argument(
        "--scopes",
        help=f"Comma separated scopes to grant. One or more of: {', '.join(_ISSUABLE_SCOPES)}",
    )
    sub.add_argument("--description", help="API key description")
    add_dry_run(sub)
    # 平文の鍵はこの応答でしか取得できないため --fields は付けない。
    # 鍵を含まない絞り込みを許すと、発行済みの鍵を回収できなくなる。
    sub.set_defaults(func=_create)


_ALLOWED_BODY_KEYS = frozenset({"name", "scopes", "description"})


def _validate(body: dict[str, Any]) -> None:
    """--json 経由の値も含めて形と scope 名を検証する。

    SDK の TypedDict / Literal は実行時検証をしないので、ここを通さないと
    dry-run が「検証済み」に見える不正な body をそのまま表示してしまう。
    """
    unknown = sorted(set(body) - _ALLOWED_BODY_KEYS)
    if unknown:
        # extra_body / extra_headers などの SDK 制御引数を素通しすると、
        # dry-run に出た body と実際の送信内容がずれ、意図より広い scope の鍵を
        # 発行させられる。受け付けるキーを本文の3つに固定する。
        raise CLIError(f"unsupported field(s) in --json: {', '.join(unknown)}")

    name = body.get("name")
    if not isinstance(name, str) or not name.strip():
        raise CLIError("name must be a non-empty string")

    scopes = body.get("scopes")
    if not isinstance(scopes, list) or not scopes:
        raise CLIError("scopes must be a non-empty array of scope strings")
    for scope in scopes:  # pyright: ignore[reportUnknownVariableType]
        if not isinstance(scope, str):
            raise CLIError("scopes must contain only strings")
        if scope not in _ISSUABLE_SCOPES:
            raise CLIError(f"{scope} is not issuable via this endpoint. Allowed: {', '.join(_ISSUABLE_SCOPES)}")

    description = body.get("description")
    if description is not None and not isinstance(description, str):
        raise CLIError("description must be a string")


def _create(args: Namespace) -> None:
    body: dict[str, Any] = parse_json_body(args) or {}
    if args.name and "name" not in body:
        body["name"] = args.name
    if args.scopes and "scopes" not in body:
        body["scopes"] = [scope.strip() for scope in args.scopes.split(",") if scope.strip()]
    if args.description and "description" not in body:
        body["description"] = args.description

    for field in ("name", "scopes"):
        if field not in body:
            raise CLIError(f"--{field} or --json with '{field}' field is required")
    _validate(body)

    if args.dry_run:
        print_dry_run("POST", "/api-keys", body)
        return
    # body を **展開せず明示的に渡す。展開すると --json の未知キーが SDK の
    # 制御引数 (extra_body 等) として解釈され、dry-run と実送信がずれる。
    client = get_client(args)
    try:
        result = client.api_keys.create(
            name=body["name"],
            scopes=body["scopes"],
            description=body.get("description", omit),
        )
    except APIStatusError as err:
        # SDK 内部の再試行は切ってあるが、既定のエラー整形は 5xx/429 を
        # retryable: true にする。それを見たエージェントがコマンドごと再実行すると
        # 応答が失われただけの場合に鍵が二重に発行される。
        # status 由来の exit code と http_status は保ったまま印だけ付ける。
        mark_non_retryable(
            err,
            "API key issuance is not idempotent. Check whether the key was created before retrying.",
        )
        raise
    print_result(result.model_dump(), args)
