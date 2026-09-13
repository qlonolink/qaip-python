from __future__ import annotations

from argparse import ArgumentParser

from . import (
    agent,
    api_keys,
    completion,
    content,
    conversations,
    crawls,
    extract,
    githubs,
    google_drives,
    local_file_groups,
    notions,
    query,
    search,
    secrets,
    source_groups,
    sources,
    tag_source_groups,
    tags,
)


def register_commands(parser: ArgumentParser) -> None:
    subparsers = parser.add_subparsers(help="All API subcommands")

    completion.register(subparsers)
    search.register(subparsers)
    extract.register(subparsers)
    content.register(subparsers)
    tags.register(subparsers)
    query.register(subparsers)
    sources.register(subparsers)
    source_groups.register(subparsers)
    secrets.register(subparsers)
    crawls.register(subparsers)
    google_drives.register(subparsers)
    githubs.register(subparsers)
    notions.register(subparsers)
    local_file_groups.register(subparsers)
    agent.register(subparsers)
    conversations.register(subparsers)
    tag_source_groups.register(subparsers)
    api_keys.register(subparsers)
