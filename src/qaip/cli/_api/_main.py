from __future__ import annotations

from argparse import ArgumentParser

from . import (
    tags,
    agent,
    crawls,
    search,
    content,
    extract,
    githubs,
    notions,
    secrets,
    sources,
    completion,
    google_drives,
    source_groups,
    local_file_groups,
    tag_source_groups,
)


def register_commands(parser: ArgumentParser) -> None:
    subparsers = parser.add_subparsers(help="All API subcommands")

    completion.register(subparsers)
    search.register(subparsers)
    extract.register(subparsers)
    content.register(subparsers)
    tags.register(subparsers)
    sources.register(subparsers)
    source_groups.register(subparsers)
    secrets.register(subparsers)
    crawls.register(subparsers)
    google_drives.register(subparsers)
    githubs.register(subparsers)
    notions.register(subparsers)
    local_file_groups.register(subparsers)
    agent.register(subparsers)
    tag_source_groups.register(subparsers)
