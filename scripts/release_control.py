"""mainの信頼済みjobから、公開候補とデータだけのGit反映を検証する。"""

from __future__ import annotations

import os
import re
import json
import base64
import argparse
import subprocess
from typing import Any
from pathlib import Path

STAGING = "qlonolink/qaip-python-staging"
PUBLIC = "qlonolink/qaip-python"
SHA = re.compile(r"[0-9a-f]{40}")
REQUIRED = {
    "ci.yml": {"lint", "build", "test"},
    "cli.yml": {"test (3.9, v1)", "test (3.9, v2)", "test (3.13, v1)", "test (3.13, v2)", "build"},
}


def api(path: str, *, token: str | None = None) -> dict[str, Any]:
    environment = os.environ.copy()
    if token is not None:
        environment["GH_TOKEN"] = token
    result = subprocess.run(["gh", "api", path], env=environment, text=True, capture_output=True, check=True)
    response: dict[str, Any] = json.loads(result.stdout)
    return response


def validate_tip(candidate: str, actual: str) -> None:
    if not SHA.fullmatch(candidate) or candidate != actual:
        raise ValueError("候補は現在のstaging mainの完全なSHAと一致する必要があります")


def validate_ci(
    run: dict[str, Any], jobs: list[dict[str, Any]], candidate: str, workflow: str, required: set[str]
) -> None:
    expected = {
        "head_sha": candidate,
        "head_branch": "main",
        "event": "push",
        "status": "completed",
        "conclusion": "success",
        "path": f".github/workflows/{workflow}",
    }
    if any(run.get(key) != value for key, value in expected.items()):
        raise ValueError("候補SHAに対する正規のmain CI成功ではありません")
    if any(run.get(key, {}).get("full_name") != STAGING for key in ("repository", "head_repository")):
        raise ValueError("CIのrepositoryが一致しません")
    if {job.get("name") for job in jobs} != required or any(job.get("conclusion") != "success" for job in jobs):
        raise ValueError("必須CI jobに未実行・skip・失敗・重複があります")
    if len(jobs) != len(required):
        raise ValueError("必須CI jobが重複しています")


def main_tip(repository: str) -> str:
    return str(api(f"repos/{repository}/git/ref/heads/main")["object"]["sha"])


def writer_token(repository: str) -> str:
    token = os.environ["APP_TOKEN"]
    inventory = api("installation/repositories?per_page=100", token=token)
    if inventory.get("total_count") != 1 or [r["full_name"] for r in inventory["repositories"]] != [repository]:
        raise ValueError("App tokenの対象repoが一致しません")
    return token


def verify_candidate(candidate: str) -> None:
    validate_tip(candidate, main_tip(STAGING))
    for workflow, required in REQUIRED.items():
        endpoint = f"repos/{STAGING}/actions/workflows/{workflow}"
        metadata = api(endpoint)
        runs = api(endpoint + f"/runs?head_sha={candidate}&event=push&branch=main&per_page=100")["workflow_runs"]
        if not runs:
            raise ValueError(f"候補SHAの必須CIがありません: {workflow}")
        # 再実行中や失敗後に、過去の成功runへフォールバックしない。
        run = max(runs, key=lambda item: item["id"])
        if run.get("workflow_id") != metadata["id"]:
            raise ValueError("CI workflow IDが一致しません")
        detail = api(f"repos/{STAGING}/actions/runs/{run['id']}")
        jobs = api(f"repos/{STAGING}/actions/runs/{run['id']}/jobs?filter=latest&per_page=100")["jobs"]
        validate_ci(detail, jobs, candidate, workflow, required)
    validate_tip(candidate, main_tip(STAGING))


def git(
    arguments: list[str], repository: Path, *, token: str | None = None, check: bool = True
) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    # 転送したGit設定・hookや、runner側のglobal設定を反映先へ持ち込まない。
    environment.update(
        {
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_COUNT": "3",
            "GIT_CONFIG_KEY_0": "core.hooksPath",
            "GIT_CONFIG_VALUE_0": os.devnull,
            "GIT_CONFIG_KEY_1": "maintenance.auto",
            "GIT_CONFIG_VALUE_1": "false",
            "GIT_CONFIG_KEY_2": "gc.auto",
            "GIT_CONFIG_VALUE_2": "0",
        }
    )
    if token is not None:
        environment.update(
            {
                "GIT_CONFIG_COUNT": "4",
                "GIT_CONFIG_KEY_3": "http.https://github.com/.extraheader",
                "GIT_CONFIG_VALUE_3": "AUTHORIZATION: basic "
                + base64.b64encode(("x-access-token:" + token).encode()).decode(),
            }
        )
    return subprocess.run(
        ["git", *arguments], cwd=repository, env=environment, text=True, capture_output=True, check=check
    )


def push_bundle(bundle: Path, destination: Path, candidate: str) -> None:
    verify_candidate(candidate)
    if destination.exists():
        raise ValueError("writerには新しいbare repositoryが必要です")
    destination.mkdir(parents=True)
    git(["init", "--bare", "--initial-branch=stlc-writer"], destination)
    git(
        ["fetch", "--no-tags", "--no-write-fetch-head", str(bundle.resolve()), "HEAD:refs/heads/candidate"], destination
    )
    actual = git(["rev-parse", "refs/heads/candidate"], destination).stdout.strip()
    validate_tip(candidate, actual)
    token = writer_token(PUBLIC)
    url = f"https://github.com/{PUBLIC}.git"
    git(["fetch", "--no-tags", "--no-write-fetch-head", url, "refs/heads/main:refs/heads/public"], destination)
    if git(["merge-base", "--is-ancestor", "refs/heads/public", candidate], destination, check=False).returncode:
        raise ValueError("公開mainが候補の祖先ではありません。back-syncが必要です")
    # token発行前の検査に加え、実際のpush直前にも現在の候補と必須CIを確認する。
    verify_candidate(candidate)
    git(["push", "--atomic", url, f"{candidate}:refs/heads/main"], destination, token=token)
    print(json.dumps({"candidate_sha": candidate, "public_main": main_tip(PUBLIC)}))
    validate_tip(candidate, main_tip(PUBLIC))


def sync_snapshot(bundle: Path, trusted_sha: str) -> str:
    validate_tip(trusted_sha, main_tip(STAGING))
    candidate = main_tip(PUBLIC)
    if not SHA.fullmatch(candidate) or bundle.exists():
        raise ValueError("back-syncの起点または転送先が不正です")
    origin = bundle.parent / "sync-snapshot.git"
    origin.mkdir(parents=True, exist_ok=False)
    git(["init", "--bare", "--initial-branch=stlc-snapshot"], origin)
    git(
        [
            "fetch",
            "--no-tags",
            "--no-write-fetch-head",
            f"https://github.com/{PUBLIC}.git",
            "refs/heads/main:refs/heads/back-sync",
        ],
        origin,
    )
    validate_tip(candidate, git(["rev-parse", "refs/heads/back-sync"], origin).stdout.strip())
    git(["bundle", "create", str(bundle.resolve()), "refs/heads/back-sync"], origin)
    return candidate


def sync_bundle(bundle: Path, destination: Path, candidate: str, trusted_sha: str) -> None:
    validate_tip(candidate, main_tip(PUBLIC))
    validate_tip(trusted_sha, main_tip(STAGING))
    destination.mkdir(parents=True, exist_ok=False)
    git(["init", "--bare", "--initial-branch=stlc-writer"], destination)
    git(
        [
            "fetch",
            "--no-tags",
            "--no-write-fetch-head",
            str(bundle.resolve()),
            "refs/heads/back-sync:refs/heads/public",
        ],
        destination,
    )
    validate_tip(candidate, git(["rev-parse", "refs/heads/public"], destination).stdout.strip())
    token = writer_token(STAGING)
    url = f"https://github.com/{STAGING}.git"
    git(
        ["fetch", "--no-tags", "--no-write-fetch-head", url, "refs/heads/main:refs/heads/staging"],
        destination,
        token=token,
    )
    validate_tip(trusted_sha, git(["rev-parse", "refs/heads/staging"], destination).stdout.strip())
    if git(["merge-base", "--is-ancestor", candidate, trusted_sha], destination, check=False).returncode == 0:
        print("公開mainはstagingへ取り込み済みです")
        return
    if git(["merge-base", "--is-ancestor", trusted_sha, candidate], destination, check=False).returncode:
        raise ValueError("stagingと公開mainが分岐しています。自動同期を停止します")
    validate_tip(candidate, main_tip(PUBLIC))
    validate_tip(trusted_sha, main_tip(STAGING))
    git(["push", "--atomic", url, f"{candidate}:refs/heads/main"], destination, token=token)
    validate_tip(candidate, main_tip(STAGING))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("check-candidate", "promote", "sync-snapshot", "sync"))
    parser.add_argument("--candidate")
    parser.add_argument("--trusted-sha", required=True)
    parser.add_argument("--bundle", type=Path)
    parser.add_argument("--repository", type=Path)
    args = parser.parse_args()
    if args.operation == "sync-snapshot" and args.bundle is not None:
        candidate = sync_snapshot(args.bundle, args.trusted_sha)
        if output := os.environ.get("GITHUB_OUTPUT"):
            with Path(output).open("a") as stream:
                stream.write(f"public_sha={candidate}\n")
        print(candidate)
        return
    if args.candidate is None:
        parser.error("candidate SHA is required")
    if args.operation != "sync":
        validate_tip(args.candidate, args.trusted_sha)
    if args.operation == "check-candidate":
        verify_candidate(args.candidate)
        print(json.dumps({"candidate_sha": args.candidate, "ci_verified": True}))
    elif args.bundle is not None and args.repository is not None:
        if args.operation == "sync":
            sync_bundle(args.bundle, args.repository, args.candidate, args.trusted_sha)
        else:
            push_bundle(args.bundle, args.repository, args.candidate)
    else:
        parser.error("promote requires --bundle and --repository")


if __name__ == "__main__":
    main()
