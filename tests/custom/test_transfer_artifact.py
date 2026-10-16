from __future__ import annotations

"""GitHub側のartifact識別子とdigestを照合し、許可ファイルだけを受け取る。"""

import io
import sys
import hashlib
import zipfile
from typing import Any
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import transfer_artifact as stlc_artifact


def archive(files: list[tuple[str, bytes]]) -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w") as packed:
        for name, content in files:
            packed.writestr(name, content)
    return output.getvalue()


@pytest.mark.parametrize(
    "invalid", [None, "digest", "null-digest", "run", "sha", "repo", "name", "expired", "path", "duplicate", "symlink"]
)
def test_artifact_identity_and_contents_are_checked(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, invalid: str | None
) -> None:
    content = archive([("sdk.bundle", b"git data")])
    if invalid == "path":
        content = archive([("../sdk.bundle", b"git data")])
    if invalid == "duplicate":
        with pytest.warns(UserWarning, match="Duplicate name"):
            content = archive([("sdk.bundle", b"first"), ("sdk.bundle", b"second")])
    if invalid == "symlink":
        output = io.BytesIO()
        with zipfile.ZipFile(output, "w") as packed:
            member = zipfile.ZipInfo("sdk.bundle")
            member.create_system = 3
            member.external_attr = 0o120777 << 16
            packed.writestr(member, "../credential")
        content = output.getvalue()
    metadata: dict[str, Any] = {
        "id": 11,
        "name": "candidate" if invalid != "name" else "other",
        "digest": "sha256:" + ("0" * 64 if invalid == "digest" else hashlib.sha256(content).hexdigest()),
        "expired": invalid == "expired",
        "workflow_run": {
            "id": 31 if invalid != "run" else 32,
            "repository_id": 41,
            "head_repository_id": 41 if invalid != "repo" else 42,
            "head_sha": "a" * 40 if invalid != "sha" else "b" * 40,
        },
    }
    if invalid == "null-digest":
        metadata["digest"] = None

    def fake_metadata(_repo: str, _id: int) -> dict[str, Any]:
        return metadata

    def fake_download(_repo: str, _id: int) -> bytes:
        return content

    monkeypatch.setattr(stlc_artifact, "metadata", fake_metadata)
    monkeypatch.setattr(stlc_artifact, "download", fake_download)
    output = tmp_path / "received"

    def receive() -> dict[str, str]:
        return stlc_artifact.receive(
            "qlonolink/qaip-python-staging",
            11,
            output,
            name="candidate",
            run_id=31,
            repository_id=41,
            source_sha="a" * 40,
            files={"sdk.bundle"},
        )

    if invalid:
        with pytest.raises(ValueError):
            receive()
        assert not output.exists()
    else:
        assert receive() == {"sdk.bundle": hashlib.sha256(b"git data").hexdigest()}
        assert (output / "sdk.bundle").read_bytes() == b"git data"
