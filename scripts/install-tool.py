"""固定ハッシュを照合してからSDK生成用ツールの単一実行ファイルを展開する。"""

import io
import gzip
import hashlib
import tarfile
import argparse
from pathlib import Path, PurePosixPath


def install(source: Path, destination: Path, checksum: str, tool: str) -> None:
    data = source.read_bytes()
    if "sha256:" + hashlib.sha256(data).hexdigest() != checksum:
        raise ValueError(f"{tool} artifact checksum mismatch")
    if tool == "rye":
        binary = gzip.decompress(data)
    elif tool == "uv":
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
            members = archive.getmembers()
            if any(
                PurePosixPath(item.name).is_absolute() or ".." in PurePosixPath(item.name).parts for item in members
            ):
                raise ValueError("uv archive contains an unsafe path")
            candidates = [item for item in members if PurePosixPath(item.name).name == "uv"]
            if len(candidates) != 1 or not candidates[0].isfile():
                raise ValueError("uv archive must contain one regular executable")
            stream = archive.extractfile(candidates[0])
            if stream is None:
                raise ValueError("uv executable is missing")
            binary = stream.read()
    else:
        raise ValueError("unsupported tool")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(binary)
    destination.chmod(0o755)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tool", choices=("uv", "rye"))
    parser.add_argument("archive", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("checksum")
    args = parser.parse_args()
    install(args.archive, args.destination, args.checksum, args.tool)


if __name__ == "__main__":
    main()
