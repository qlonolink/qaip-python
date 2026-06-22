from __future__ import annotations

from typing import TYPE_CHECKING
from argparse import ArgumentParser

from .._utils import get_client
from ._common import add_fields, add_dry_run, print_result, print_dry_run

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser(
        "user-keyword-snapshots.create",
        help="Snapshot the user's keywords and trigger re-indexing",
    )
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create)


def _create(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("POST", "/user-keyword-snapshots")
        return
    client = get_client(args)
    result = client.user_keyword_snapshots.create()
    print_result(result.model_dump(), args)
