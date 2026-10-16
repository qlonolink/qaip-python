from __future__ import annotations

import sys
import subprocess
from copy import deepcopy
from typing import Any
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import release_control as control
from release_control import validate_ci, validate_tip

SHA = "a" * 40
REPOSITORY = "qlonolink/qaip-python-staging"


def successful_run() -> dict[str, object]:
    return {
        "head_sha": SHA,
        "head_branch": "main",
        "event": "push",
        "status": "completed",
        "conclusion": "success",
        "path": ".github/workflows/ci.yml",
        "repository": {"full_name": REPOSITORY},
        "head_repository": {"full_name": REPOSITORY},
    }


def test_exact_candidate_is_required() -> None:
    validate_tip(SHA, SHA)
    for value in ("", "main", "a" * 7, "b" * 40):
        with pytest.raises(ValueError):
            validate_tip(value, SHA)


@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("head_sha", "b" * 40),
        ("head_branch", "feature"),
        ("event", "pull_request"),
        ("conclusion", "failure"),
        ("status", "in_progress"),
        ("path", ".github/workflows/fake.yml"),
        ("head_repository", {"full_name": "attacker/fork"}),
    ],
)
def test_ci_from_another_source_is_rejected(key: str, value: object) -> None:
    run = successful_run()
    run[key] = value
    with pytest.raises(ValueError):
        validate_ci(run, [{"name": "lint", "conclusion": "success"}], SHA, "ci.yml", {"lint"})


def test_skipped_or_missing_required_job_is_rejected() -> None:
    jobs: list[dict[str, object]] = [{"name": name, "conclusion": "success"} for name in ("lint", "build", "test")]
    validate_ci(successful_run(), jobs, SHA, "ci.yml", {"lint", "build", "test"})
    for conclusion in ("skipped", "failure", None):
        altered = deepcopy(jobs)
        altered[0]["conclusion"] = conclusion
        with pytest.raises(ValueError):
            validate_ci(successful_run(), altered, SHA, "ci.yml", {"lint", "build", "test"})
    with pytest.raises(ValueError):
        validate_ci(successful_run(), jobs[:2], SHA, "ci.yml", {"lint", "build", "test"})


def test_candidate_advancing_after_validation_stops_before_push(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    checks = 0
    commands: list[list[str]] = []

    def candidate_check(_candidate: str) -> None:
        nonlocal checks
        checks += 1
        if checks == 2:
            raise ValueError("stale candidate")

    def fake_git(arguments: list[str], _repository: Path, **_options: Any) -> subprocess.CompletedProcess[str]:
        commands.append(arguments)
        return subprocess.CompletedProcess(arguments, 0, stdout=SHA + "\n", stderr="")

    def scoped_writer(_repository: str) -> str:
        return "DUMMY_SCOPED_TOKEN"

    monkeypatch.setattr(control, "verify_candidate", candidate_check)
    monkeypatch.setattr(control, "git", fake_git)
    monkeypatch.setattr(control, "writer_token", scoped_writer)
    with pytest.raises(ValueError, match="stale candidate"):
        control.push_bundle(tmp_path / "candidate.bundle", tmp_path / "writer.git", SHA)
    assert checks == 2
    assert not any(command[0] == "push" for command in commands)


@pytest.mark.parametrize("repositories", [[control.STAGING], [control.PUBLIC, control.STAGING]])
def test_writer_token_is_limited_to_the_target_repository(
    repositories: list[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    def inventory(_path: str, *, token: str | None = None) -> dict[str, Any]:
        assert token == "DUMMY_SCOPED_TOKEN"
        return {"total_count": len(repositories), "repositories": [{"full_name": repo} for repo in repositories]}

    monkeypatch.setenv("APP_TOKEN", "DUMMY_SCOPED_TOKEN")
    monkeypatch.setattr(control, "api", inventory)
    with pytest.raises(ValueError, match="対象repo"):
        control.writer_token(control.PUBLIC)
