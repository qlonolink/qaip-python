from pathlib import Path

import nox


@nox.session(venv_backend="none", name="test-pydantic-v1")
def test_pydantic_v1(session: nox.Session) -> None:
    root = Path(__file__).parent
    session.run(
        "bash",
        "scripts/bootstrap",
        external=True,
        env={"SDK_PYDANTIC_VARIANT": "v1", "UV_PROJECT_ENVIRONMENT": str(root / ".venv-pydantic-v1")},
    )
    session.run(
        "uv",
        "run",
        "--no-sync",
        "pytest",
        "--showlocals",
        "--ignore=tests/functional",
        *session.posargs,
        external=True,
        env={"UV_PROJECT_ENVIRONMENT": str(root / ".venv-pydantic-v1")},
    )
