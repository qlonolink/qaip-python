# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["JobStatus"]

JobStatus: TypeAlias = Literal[
    "unknown",
    "queued",
    "not_started",
    "managed",
    "starting",
    "started",
    "success",
    "failure",
    "canceling",
    "canceled",
    "deleting",
    "delete_job_failure",
]
