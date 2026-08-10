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


# 非冪等な操作の失敗に付ける印。status を保った APIStatusError のまま
# retryable だけを落としたいので、例外を包み替えずに属性で伝える
# (包み替えると status 由来の exit code と http_status が失われる)。
_NON_RETRYABLE_ATTR = "_qaip_cli_non_retryable_hint"


def mark_non_retryable(err: APIStatusError, hint: str) -> None:
    """再実行してはいけない失敗として印を付ける。"""
    setattr(err, _NON_RETRYABLE_ATTR, hint)


def _non_retryable_hint(err: APIStatusError) -> str | None:
    return getattr(err, _NON_RETRYABLE_ATTR, None)


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
        hint = _non_retryable_hint(err)
        payload = {
            "code": "api_error",
            "message": str(err),
            "http_status": err.status_code,
            "retryable": hint is None and err.status_code in (408, 425, 429, 500, 502, 503, 504),
        }
        if hint is not None:
            payload["hint"] = hint
        return {"error": payload}
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
        sys.stderr.write(json.dumps(_to_json_payload(err), ensure_ascii=False, default=str) + "\n")
        return
    sys.stderr.write("Error: {}\n".format(err))
    # text 形式では hint を出さない設計だが、「再実行するな」は落とすと危険なので出す。
    if isinstance(err, APIStatusError):
        hint = _non_retryable_hint(err)
        if hint is not None:
            sys.stderr.write("Hint: {}\n".format(hint))
