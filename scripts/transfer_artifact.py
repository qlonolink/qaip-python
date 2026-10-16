"""GitHubが保持するartifactの同一性とdigestを照合し、データだけを受け取る。"""

from __future__ import annotations

import io
import os
import re
import json
import stat
import hashlib
import zipfile
import argparse
import subprocess
from typing import Any, cast
from pathlib import Path

REPOSITORIES = {"qlonolink/qaip-python-staging", "qlonolink/qaip-python"}
MAX_SIZE = 512 * 1024 * 1024


def metadata(repo: str, artifact_id: int) -> dict[str, Any]:
    response: dict[str, Any] = json.loads(
        subprocess.check_output(["gh", "api", f"repos/{repo}/actions/artifacts/{artifact_id}"], text=True)
    )
    return response


def download(repo: str, artifact_id: int) -> bytes:
    return subprocess.check_output(["gh", "api", f"repos/{repo}/actions/artifacts/{artifact_id}/zip"])


def receive(
    repo: str,
    artifact_id: int,
    destination: Path,
    *,
    name: str,
    run_id: int,
    repository_id: int,
    source_sha: str,
    files: set[str],
) -> dict[str, str]:
    if repo not in REPOSITORIES or min(artifact_id, run_id, repository_id) <= 0:
        raise ValueError("invalid artifact identity")
    if not re.fullmatch(r"[0-9a-f]{40}", source_sha) or not files:
        raise ValueError("invalid source or file list")
    if destination.exists() or any(item in {".", ".."} or not re.fullmatch(r"[a-zA-Z0-9_.-]+", item) for item in files):
        raise ValueError("artifact destination must be a fresh data directory")
    info = metadata(repo, artifact_id)
    workflow = info.get("workflow_run", {})
    if not isinstance(workflow, dict):
        raise ValueError("artifact has no workflow identity")
    workflow = cast("dict[str, Any]", workflow)
    if (
        info.get("id") != artifact_id
        or info.get("name") != name
        or info.get("expired") is not False
        or workflow.get("id") != run_id
        or workflow.get("repository_id") != repository_id
        or workflow.get("head_repository_id") != repository_id
        or workflow.get("head_sha") != source_sha
    ):
        raise ValueError("artifact belongs to a different workflow input")
    expected = info.get("digest", "")
    if not isinstance(expected, str) or not re.fullmatch(r"sha256:[0-9a-f]{64}", expected):
        raise ValueError("artifact has no GitHub digest")
    data = download(repo, artifact_id)
    if len(data) > MAX_SIZE or "sha256:" + hashlib.sha256(data).hexdigest() != expected:
        raise ValueError("artifact digest mismatch")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        entries = archive.infolist()
        if len(entries) != len(files) or {item.filename for item in entries} != files:
            raise ValueError("artifact contains unexpected or duplicate files")
        if sum(item.file_size for item in entries) > MAX_SIZE:
            raise ValueError("artifact is too large")
        for item in entries:
            kind = stat.S_IFMT(item.external_attr >> 16)
            if item.is_dir() or kind not in {0, stat.S_IFREG}:
                raise ValueError("artifact contains a non-regular file")
        contents = {item.filename: archive.read(item) for item in entries}
    destination.mkdir(parents=True)
    for filename, content in contents.items():
        (destination / filename).write_bytes(content)
    return {filename: hashlib.sha256(content).hexdigest() for filename, content in contents.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact_id", type=int)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--repo", default="qlonolink/qaip-python-staging")
    parser.add_argument("--name", required=True)
    parser.add_argument("--run-id", type=int, required=True)
    parser.add_argument("--repository-id", type=int, required=True)
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--file", action="append", required=True)
    args = parser.parse_args()
    hashes = receive(
        args.repo,
        args.artifact_id,
        args.destination,
        name=args.name,
        run_id=args.run_id,
        repository_id=args.repository_id,
        source_sha=args.source_sha,
        files=set(args.file),
    )
    rendered = json.dumps(hashes, sort_keys=True)
    print(rendered)
    if output := os.environ.get("GITHUB_OUTPUT"):
        with Path(output).open("a") as stream:
            stream.write(f"files_json={rendered}\n")


if __name__ == "__main__":
    main()
