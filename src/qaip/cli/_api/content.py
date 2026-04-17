from __future__ import annotations

from typing import TYPE_CHECKING
from argparse import ArgumentParser

from .._utils import get_client
from ._common import add_fields, add_dry_run, print_result, print_dry_run
from .._errors import CLIError

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser("content.retrieve", help="Retrieve content by ID")
    sub.add_argument("-i", "--id", required=True, help="Content ID")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve)


def _retrieve(args: Namespace) -> None:
    if not args.id:
        raise CLIError("--id is required")

    if args.dry_run:
        print_dry_run("GET", f"/contents/{args.id}")
        return

    client = get_client(args)
    result = client.content(args.id)
    print_result(result.model_dump(), args)
