from __future__ import annotations

import sys

from .._exceptions import APIError, QaipError


class CLIError(QaipError): ...


class SilentCLIError(CLIError): ...


def display_error(err: CLIError | APIError | Exception) -> None:
    if isinstance(err, SilentCLIError):
        return

    sys.stderr.write("Error: {}\n".format(err))
