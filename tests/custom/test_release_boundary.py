from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_release_doctor_does_not_read_pypi_credentials() -> None:
    workflow = (ROOT / ".github/workflows/release-doctor.yml").read_text()
    assert "secrets." not in workflow
    assert "PYPI_TOKEN" not in workflow
    result = subprocess.run(
        ["bash", str(ROOT / "bin/check-release-environment")],
        cwd=ROOT,
        env={key: value for key, value in os.environ.items() if "TOKEN" not in key},
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stderr
    assert "ready to push" not in result.stdout


def test_ci_does_not_execute_unverified_installer() -> None:
    for path in (ROOT / ".github/workflows").glob("*.yml"):
        assert "rye.astral.sh/get" not in path.read_text(), path.name


def test_publication_does_not_build_with_credentials() -> None:
    script = (ROOT / "bin/publish-pypi").read_text()
    assert "set -x" not in script
    assert "set -eux" not in script
    assert "rye build" not in script
    assert "--token=" not in script


def test_only_protected_upload_job_can_request_oidc() -> None:
    workflow = (ROOT / ".github/workflows/publish-pypi.yml").read_text()
    header, _, body = workflow.partition("jobs:\n")
    sections = re.split(r"(?m)^  ([a-z][a-z_-]+):\n", body)
    jobs = dict(zip(sections[1::2], sections[2::2]))
    assert "id-token:" not in header
    assert "id-token: write" in jobs["upload"]
    assert "environment: pypi-release" in jobs["upload"]
    assert "github.ref == 'refs/heads/main'" in jobs["upload"]
    assert all("id-token:" not in job for name, job in jobs.items() if name != "upload")
    assert "--trusted-publishing always" in jobs["upload"]
    assert "--trusted-publishing never" not in workflow
    assert "PYPI_TOKEN" not in workflow
    assert "UV_PUBLISH_TOKEN" not in workflow


def test_local_publication_retry_uses_main_workflow(tmp_path: Path) -> None:
    executable = tmp_path / "gh"
    executable.write_text('#!/bin/sh\nprintf "%s\\n" "$@"\n')
    executable.chmod(0o755)
    result = subprocess.run(
        ["bash", str(ROOT / "bin/publish-pypi"), "v0.18.0"],
        cwd=tmp_path,
        env={"PATH": f"{tmp_path}:{os.defpath}"},
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.splitlines() == [
        "workflow",
        "run",
        "publish-pypi.yml",
        "--repo",
        "qlonolink/qaip-python",
        "--ref",
        "main",
        "-f",
        "tag=v0.18.0",
    ]
