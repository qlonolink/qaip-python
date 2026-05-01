from __future__ import annotations

import os
import sys
import json
from typing import Any

from .._exceptions import APIError, QaipError, APIStatusError


class CLIError(QaipError):
    """CLI からエージェントに見せるためのエラー。

    code はエージェントによる分類用識別子（`missing_credentials`,
    `invalid_argument`, `invalid_id`, `validation_error`,
    `confirmation_required` など）。message は人間用。hint は次に取るべき
    アクション。retryable は同じ引数で再試行する意味があるかどうか。
    """

    code: str
    hint: str | None
    retryable: bool

    def __init__(
        self,
        message: str,
        *,
        code: str = "cli_error",
        hint: str | None = None,
        retryable: bool = False,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.hint = hint
        self.retryable = retryable


class SilentCLIError(CLIError): ...


def _resolve_format(explicit: str | None) -> str:
    if explicit:
        return explicit.lower()
    return os.environ.get("QAIP_ERROR_FORMAT", "text").lower()


def _to_json_payload(err: Exception) -> dict[str, Any]:
    if isinstance(err, CLIError):
        payload: dict[str, Any] = {
            "code": err.code,
            "message": str(err),
            "retryable": err.retryable,
        }
        if err.hint is not None:
            payload["hint"] = err.hint
        return {"error": payload}
    if isinstance(err, APIStatusError):
        return {
            "error": {
                "code": "api_error",
                "message": str(err),
                "http_status": err.status_code,
                "retryable": err.status_code in (408, 425, 429, 500, 502, 503, 504),
            }
        }
    if isinstance(err, APIError):
        return {
            "error": {
                "code": "api_error",
                "message": str(err),
                "retryable": False,
            }
        }
    return {
        "error": {
            "code": "internal_error",
            "message": str(err),
            "retryable": False,
        }
    }


def display_error(err: CLIError | APIError | Exception, *, error_format: str | None = None) -> None:
    if isinstance(err, SilentCLIError):
        return
    fmt = _resolve_format(error_format)
    if fmt == "json":
        sys.stderr.write(
            json.dumps(_to_json_payload(err), ensure_ascii=False, default=str) + "\n"
        )
        return
    sys.stderr.write("Error: {}\n".format(err))
