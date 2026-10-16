"""mainの公開controllerでReleaseの起点と配布物の内容・ハッシュを検証する。"""

from __future__ import annotations

import re
import json
import hashlib
import tarfile
import zipfile
import argparse
import urllib.request
from typing import Any
from pathlib import Path
from email.parser import BytesParser

from release_control import SHA, PUBLIC, api

TAG = re.compile(r"v(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)")
MAX_SIZE = 128 * 1024 * 1024


def release_commit(tag: str) -> str:
    if not TAG.fullmatch(tag):
        raise ValueError("公開には安定版vX.Y.Zタグを指定してください")
    release = api(f"repos/{PUBLIC}/releases/tags/{tag}")
    if (
        release.get("draft")
        or release.get("prerelease")
        or not release.get("published_at")
        or release.get("tag_name") != tag
    ):
        raise ValueError("公開済みの安定版GitHub Releaseではありません")
    reference = api(f"repos/{PUBLIC}/git/ref/tags/{tag}")["object"]
    for _ in range(5):
        if reference["type"] == "commit":
            break
        if reference["type"] != "tag":
            raise ValueError("Release tagはcommitを指す必要があります")
        reference = api(f"repos/{PUBLIC}/git/tags/{reference['sha']}")["object"]
    if reference["type"] != "commit" or not SHA.fullmatch(reference["sha"]):
        raise ValueError("Release commitを解決できません")
    return str(reference["sha"])


def protected(path: str) -> bool:
    return path.startswith((".github/", "scripts/", "bin/")) or path in {
        "pyproject.toml",
        "uv.lock",
        ".python-version",
        "release-please-config.json",
        "noxfile.py",
    }


def validate_source(tag: str, trusted_sha: str) -> str:
    if not SHA.fullmatch(trusted_sha):
        raise ValueError("controllerのSHAが不正です")
    candidate = release_commit(tag)
    comparison = api(f"repos/{PUBLIC}/compare/{candidate}...{trusted_sha}")
    if comparison.get("merge_base_commit", {}).get("sha") != candidate:
        raise ValueError("Release tagが信頼済みmainの祖先ではありません")
    trees: list[dict[str, dict[str, Any]]] = []
    for sha in (candidate, trusted_sha):
        tree = api(f"repos/{PUBLIC}/git/trees/{sha}?recursive=1")
        if tree.get("truncated"):
            raise ValueError("source treeが途中で打ち切られました")
        trees.append(
            {entry["path"]: entry for entry in tree["tree"] if entry["type"] == "blob" and protected(entry["path"])}
        )
    if trees[0] != trees[1]:
        # APIのblob URLはtreeによらず同一であり、版の更新以外を例外にしない。
        differing = {path for path in trees[0].keys() | trees[1].keys() if trees[0].get(path) != trees[1].get(path)}
        if differing != {"pyproject.toml"}:
            raise ValueError("Release tagのworkflow・script・lockがmainの承認済み定義と異なります")
        import base64

        contents: list[str] = []
        for sha in (candidate, trusted_sha):
            document = api(f"repos/{PUBLIC}/contents/pyproject.toml?ref={sha}")
            contents.append(base64.b64decode(document["content"]).decode())
        normalized = [re.sub(r'(?m)^version = "[^"]+"$', 'version = "RELEASE"', text, count=1) for text in contents]
        if normalized[0] != normalized[1]:
            raise ValueError("Releaseのpyproject変更が版の更新だけではありません")
    return candidate


def check_metadata(data: bytes, version: str) -> None:
    metadata = BytesParser().parsebytes(data)
    if metadata.get_all("Name") != ["qaip"] or metadata.get_all("Version") != [version]:
        raise ValueError("配布物のpackage名または版がReleaseと一致しません")


def distribution_hashes(directory: Path, version: str) -> dict[str, str]:
    expected = {f"qaip-{version}-py3-none-any.whl", f"qaip-{version}.tar.gz"}
    files = {path.name: path for path in directory.iterdir() if path.name != "release-manifest.json"}
    if set(files) != expected or any(
        path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_SIZE for path in files.values()
    ):
        raise ValueError("配布物の個数・名前・種類・サイズが不正です")
    wheel = files[f"qaip-{version}-py3-none-any.whl"]
    with zipfile.ZipFile(wheel) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)) or sum(item.file_size for item in archive.infolist()) > MAX_SIZE:
            raise ValueError("wheelに重複または過大な内容があります")
        check_metadata(archive.read(f"qaip-{version}.dist-info/METADATA"), version)
    sdist = files[f"qaip-{version}.tar.gz"]
    with tarfile.open(sdist, "r:gz") as archive:
        members = archive.getmembers()
        if sum(item.size for item in members) > MAX_SIZE or any(
            not (item.isfile() or item.isdir()) for item in members
        ):
            raise ValueError("sdistに過大な内容または特殊ファイルがあります")
        names = [item.name for item in members]
        if len(names) != len(set(names)):
            raise ValueError("sdistに重複したentryがあります")
        stream = archive.extractfile(f"qaip-{version}/PKG-INFO")
        if stream is None:
            raise ValueError("sdistのmetadataがありません")
        check_metadata(stream.read(), version)
    return {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in sorted(files.items())}


def manifest(directory: Path, tag: str, candidate: str, trusted_sha: str, *, verify: bool) -> dict[str, Any]:
    if not TAG.fullmatch(tag) or not SHA.fullmatch(candidate) or not SHA.fullmatch(trusted_sha):
        raise ValueError("配布物の起点が不正です")
    result = {
        "tag": tag,
        "candidate_sha": candidate,
        "controller_sha": trusted_sha,
        "files": distribution_hashes(directory, tag[1:]),
    }
    path = directory / "release-manifest.json"
    if verify:
        if path.is_symlink() or json.loads(path.read_text()) != result:
            raise ValueError("検査後に配布物またはmanifestが差し替わりました")
    else:
        path.write_text(json.dumps(result, indent=2) + "\n")
    return result


def check_pypi(metadata: dict[str, Any], record: dict[str, Any]) -> None:
    if metadata.get("info", {}).get("name") != "qaip" or metadata["info"].get("version") != record["tag"][1:]:
        raise ValueError("PyPIのpackage名・版が一致しません")
    published = {item["filename"]: item["digests"]["sha256"] for item in metadata["urls"]}
    if len(metadata["urls"]) != len(published) or published != record["files"]:
        raise ValueError("PyPI公開物のハッシュが検査済み配布物と一致しません")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("source", "record", "verify", "pypi"))
    parser.add_argument("--tag", required=True)
    parser.add_argument("--trusted-sha", required=True)
    parser.add_argument("--candidate")
    parser.add_argument("--directory", type=Path)
    args = parser.parse_args()
    if args.operation == "source":
        print(validate_source(args.tag, args.trusted_sha))
    elif args.directory is not None and args.candidate is not None:
        record = manifest(args.directory, args.tag, args.candidate, args.trusted_sha, verify=args.operation != "record")
        if args.operation == "pypi":
            with urllib.request.urlopen(f"https://pypi.org/pypi/qaip/{args.tag[1:]}/json", timeout=30) as response:
                check_pypi(json.load(response), record)
        print(json.dumps(record))
    else:
        parser.error("record/verify requires --directory and --candidate")


if __name__ == "__main__":
    main()
