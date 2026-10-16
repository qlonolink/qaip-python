## Setting up the environment

Install [uv](https://docs.astral.sh/uv/) at the version in `scripts/toolchain.json`, then run:

```sh
./scripts/bootstrap
```

The bootstrap uses `uv.lock` without resolving new versions. Run local Python commands with
`uv run --no-sync python ...`. The public SDK dependency ranges remain in `pyproject.toml`;
CI uses locked environments for Python 3.9/3.13 and Pydantic v1/v2.

To update dependencies, set `tool.uv.exclude-newer` to at most seven days before the current date,
run `uv lock`, review the lock diff, and run the checks below.

## Modifying/Adding code

Most of the SDK is generated code. Modifications to code will be persisted between generations, but may
result in merge conflicts between manual patches and changes from the generator. The generator will never
modify the contents of the `src/qaip/lib/` and `examples/` directories.

## Adding and running examples

All files in the `examples/` directory are not modified by the generator and can be freely edited or added to.

```py
# add an example to examples/<your-example>.py

#!/usr/bin/env -S uv run --no-sync python
…
```

```sh
$ chmod +x examples/<your-example>.py
# run the example against your api
$ ./examples/<your-example>.py
```

## Using the repository from source

If you’d like to use the repository from source, you can either install from git or link to a cloned repository:

To install via git:

```sh
$ pip install git+ssh://git@github.com/qlonolink/qaip-python.git
```

Alternatively, you can build from source and install the wheel file:

Building this package will create two files in the `dist/` directory, a `.tar.gz` containing the source files and a `.whl` that can be used to install the package efficiently.

To create a distributable version of the library, all you have to do is run this command:

```sh
$ ./scripts/build
```

Then to install:

```sh
$ pip install ./path-to-wheel-file.whl
```

## Running tests

```sh
$ ./scripts/test
```

## Linting and formatting

This repository uses [ruff](https://github.com/astral-sh/ruff) to format the code in the repository.

To lint:

```sh
$ ./scripts/lint
```

To format and fix all ruff issues automatically:

```sh
$ ./scripts/format
```

## Publishing and releases

SDK validation and builds consume only the hash-locked `uv.lock`. The generator also emits
`requirements.lock` and `requirements-dev.lock`; no CI or validation script installs from them.

Changes made to this repository via the automated release PR pipeline should publish to PyPI automatically. If
the changes aren't made through the automated pipeline, you may want to make releases manually.

### Publish with a GitHub workflow

A published stable GitHub Release dispatches `Publish PyPI` on `main`. The controller verifies the
Release tag and protected source definitions, builds without publishing credentials, and sends the
inspected wheel/sdist from a separate upload job. The `pypi-release` environment permits only the
`main` branch. Only the upload job has `id-token: write`; builds and tests cannot request a
publishing identity. `uv publish --trusted-publishing always` uses GitHub OIDC and requires no
manually issued PyPI API token or secret.

In [PyPI's publishing settings](https://pypi.org/manage/project/qaip/settings/publishing/),
register a GitHub Trusted Publisher with owner `qlonolink`, repository `qaip-python`, workflow
filename `publish-pypi.yml`, and environment `pypi-release`. All four fields must match.
Check this registration before enabling publication; a missing registration stops the upload.

A retry uses the same published Release tag:

```sh
gh workflow run publish-pypi.yml --repo qlonolink/qaip-python --ref main -f tag=vX.Y.Z
```

The upload job checks GitHub's immutable artifact identity/digest and the inspected distribution
hashes. It does not rebuild the package. After publication, compare PyPI's hashes with the saved
`release-manifest.json` and verify installation and the `qaip` command.

`bin/publish-pypi vX.Y.Z` dispatches the same main workflow using your `gh` authentication.
It performs the same validation and build steps and does not require a local PyPI token.
