from __future__ import annotations

import io
import sys
import tarfile
import zipfile
from typing import Any
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import release_artifacts as release

SHA = "a" * 40


def distributions(directory: Path, *, version: str = "0.18.0") -> None:
    metadata = f"Name: qaip\nVersion: {version}\n".encode()
    with zipfile.ZipFile(directory / "qaip-0.18.0-py3-none-any.whl", "w") as archive:
        archive.writestr("qaip-0.18.0.dist-info/METADATA", metadata)
    with tarfile.open(directory / "qaip-0.18.0.tar.gz", "w:gz") as archive:
        info = tarfile.TarInfo("qaip-0.18.0/PKG-INFO")
        info.size = len(metadata)
        archive.addfile(info, io.BytesIO(metadata))


def test_verified_artifacts_are_not_rebuilt(tmp_path: Path) -> None:
    distributions(tmp_path)
    record = release.manifest(tmp_path, "v0.18.0", SHA, SHA, verify=False)
    assert release.manifest(tmp_path, "v0.18.0", SHA, SHA, verify=True) == record
    wheel = tmp_path / "qaip-0.18.0-py3-none-any.whl"
    with zipfile.ZipFile(wheel, "a") as archive:
        archive.writestr("qaip/changed.py", "changed after inspection")
    with pytest.raises(ValueError, match="差し替わり"):
        release.manifest(tmp_path, "v0.18.0", SHA, SHA, verify=True)


def test_distribution_version_and_extra_files_are_rejected(tmp_path: Path) -> None:
    distributions(tmp_path, version="99.0.0")
    with pytest.raises(ValueError, match="版"):
        release.manifest(tmp_path, "v0.18.0", SHA, SHA, verify=False)
    distributions(tmp_path)
    (tmp_path / "unreviewed.whl").write_bytes(b"other artifact")
    with pytest.raises(ValueError, match="個数"):
        release.manifest(tmp_path, "v0.18.0", SHA, SHA, verify=False)


def test_manifest_from_another_commit_is_rejected(tmp_path: Path) -> None:
    distributions(tmp_path)
    release.manifest(tmp_path, "v0.18.0", SHA, SHA, verify=False)
    with pytest.raises(ValueError, match="差し替わり"):
        release.manifest(tmp_path, "v0.18.0", "b" * 40, SHA, verify=True)


def test_published_hashes_must_match_inspected_distributions(tmp_path: Path) -> None:
    distributions(tmp_path)
    record = release.manifest(tmp_path, "v0.18.0", SHA, SHA, verify=False)
    published: dict[str, Any] = {
        "info": {"name": "qaip", "version": "0.18.0"},
        "urls": [{"filename": name, "digests": {"sha256": digest}} for name, digest in record["files"].items()],
    }
    release.check_pypi(published, record)
    published["urls"][0]["digests"]["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="ハッシュ"):
        release.check_pypi(published, record)


@pytest.mark.parametrize("tag", ["main", "../v0.18.0", "v0.18.0-rc1", "v0.18.0\n"])
def test_only_stable_release_tags_are_accepted(tag: str) -> None:
    with pytest.raises(ValueError):
        release.release_commit(tag)


@pytest.mark.parametrize("invalid", ["branch", "workflow", "lock"])
def test_untrusted_release_source_is_rejected(invalid: str, monkeypatch: pytest.MonkeyPatch) -> None:
    trusted = "b" * 40

    def commit(_tag: str) -> str:
        return SHA

    def metadata(path: str) -> dict[str, Any]:
        if "/compare/" in path:
            return {"merge_base_commit": {"sha": "c" * 40 if invalid == "branch" else SHA}}
        name = ".github/workflows/publish-pypi.yml" if invalid == "workflow" else "uv.lock"
        return {
            "truncated": False,
            "tree": [{"path": name, "type": "blob", "sha": "c" * 40 if SHA in path else "d" * 40}],
        }

    monkeypatch.setattr(release, "release_commit", commit)
    monkeypatch.setattr(release, "api", metadata)
    with pytest.raises(ValueError):
        release.validate_source("v0.18.0", trusted)
