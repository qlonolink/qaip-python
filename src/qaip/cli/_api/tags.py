from __future__ import annotations

from typing import TYPE_CHECKING
from argparse import ArgumentParser

from .._utils import get_client
from ._common import add_fields, add_dry_run, print_result, print_dry_run

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser("tags.list", help="List tags")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list)


def _list(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", "/tags")
        return

    client = get_client(args)
    result = client.tags()
    print_result(result.model_dump(), args)
