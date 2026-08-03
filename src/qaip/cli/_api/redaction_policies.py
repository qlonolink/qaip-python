from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any, Protocol, cast
from argparse import ArgumentParser

from .._utils import get_client
from ._common import (
    add_yes,
    add_fields,
    add_dry_run,
    require_yes,
    print_result,
    print_dry_run,
    add_json_param,
    parse_json_body,
)
from ..._types import omit
from .._errors import CLIError

if TYPE_CHECKING:
    from argparse import Namespace, _SubParsersAction


_UNSET = object()
_NAME_RE = re.compile(r"^[a-z][a-z0-9-]{0,63}$")
_VERSION_RE = re.compile(r"^[1-9][0-9]*$")
_ALIASES = {
    "businessConfidential": "business_confidential",
    "expectedActiveVersion": "expected_active_version",
}


class _SDKResult(Protocol):
    def model_dump(self) -> dict[str, Any]: ...


class _RedactionPoliciesResource(Protocol):
    def validate(self, **body: Any) -> _SDKResult: ...

    def create(self, **body: Any) -> _SDKResult: ...

    def list(self) -> _SDKResult: ...

    def retrieve(self, name: str) -> _SDKResult: ...

    def create_version(self, name: str, **body: Any) -> _SDKResult: ...

    def list_versions(self, name: str, **params: Any) -> _SDKResult: ...

    def retrieve_version(self, name: str, version: str) -> _SDKResult: ...

    def activate_version(self, name: str, version: str, **body: Any) -> _SDKResult: ...

    def archive(self, name: str, **body: Any) -> _SDKResult: ...

    def delete_version(self, name: str, version: str) -> _SDKResult | None: ...


class _QaipWithRedactionPolicies(Protocol):
    redaction_policies: _RedactionPoliciesResource


def register(subparser: _SubParsersAction[ArgumentParser]) -> None:
    sub = subparser.add_parser("redaction-policies.validate", help="Validate a tenant redaction policy")
    _add_create_body_args(sub, include_name=True)
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_validate)

    sub = subparser.add_parser("redaction-policies.create", help="Create a tenant redaction policy DRAFT")
    _add_create_body_args(sub, include_name=True)
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create)

    sub = subparser.add_parser("redaction-policies.list", help="List redaction policy summaries")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list)

    sub = subparser.add_parser("redaction-policies.retrieve", help="Get a redaction policy")
    _add_name(sub)
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve)

    sub = subparser.add_parser("redaction-policies.create-version", help="Create the next policy DRAFT")
    _add_name(sub)
    _add_create_body_args(sub, include_name=False)
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_create_version)

    sub = subparser.add_parser("redaction-policies.list-versions", help="List policy versions")
    _add_name(sub)
    sub.add_argument("--limit", type=int, help="Maximum number of versions (1-100)")
    sub.add_argument("--before-version", help="Server-returned version cursor")
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_list_versions)

    sub = subparser.add_parser("redaction-policies.retrieve-version", help="Get a complete policy version")
    _add_name(sub)
    _add_version(sub)
    add_dry_run(sub)
    add_fields(sub)
    sub.set_defaults(func=_retrieve_version)

    sub = subparser.add_parser("redaction-policies.activate-version", help="Activate or roll back a policy version")
    _add_name(sub)
    _add_version(sub)
    _add_cas_body_args(sub)
    add_dry_run(sub)
    add_yes(sub)
    add_fields(sub)
    sub.set_defaults(func=_activate_version)

    sub = subparser.add_parser("redaction-policies.archive", help="Archive the current ACTIVE policy")
    _add_name(sub)
    _add_cas_body_args(sub)
    add_dry_run(sub)
    add_yes(sub)
    add_fields(sub)
    sub.set_defaults(func=_archive)

    sub = subparser.add_parser("redaction-policies.delete-version", help="Delete a never-activated DRAFT")
    _add_name(sub)
    _add_version(sub)
    add_dry_run(sub)
    add_yes(sub)
    sub.set_defaults(func=_delete_version)


def _add_name(parser: ArgumentParser) -> None:
    parser.add_argument("--name", required=True, help="Tenant-local policy name")


def _add_version(parser: ArgumentParser) -> None:
    parser.add_argument("--version", required=True, help="Positive decimal version string")


def _add_create_body_args(parser: ArgumentParser, *, include_name: bool) -> None:
    add_json_param(parser)
    if include_name:
        parser.add_argument("--name", default=_UNSET, help="Tenant-local policy name")
    parser.add_argument("--description", default=_UNSET, help="Display-only description")


def _add_cas_body_args(parser: ArgumentParser) -> None:
    add_json_param(parser)
    parser.add_argument(
        "--expected-active-version",
        default=_UNSET,
        help="Expected ACTIVE version, or literal 'null' when no ACTIVE version is expected",
    )


def _normalize_body(raw: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(raw)
    for wire_name, sdk_name in _ALIASES.items():
        if wire_name not in normalized:
            continue
        if sdk_name in normalized:
            raise CLIError(f"Specify only one of {wire_name} and {sdk_name}", code="invalid_argument")
        normalized[sdk_name] = normalized.pop(wire_name)
    return normalized


def _request_body(
    args: Namespace,
    *,
    allowed: set[str],
    required: set[str],
    override_names: tuple[str, ...],
) -> dict[str, Any]:
    body = _normalize_body(parse_json_body(args) or {})
    for name in override_names:
        value = getattr(args, name, _UNSET)
        if value is _UNSET or name in body:
            continue
        if name == "expected_active_version" and value == "null":
            value = None
        body[name] = value
    unknown = set(body) - allowed
    if unknown:
        raise CLIError(f"Unknown JSON fields: {', '.join(sorted(unknown))}", code="invalid_argument")
    missing = required - set(body)
    if missing:
        raise CLIError(f"Missing required fields: {', '.join(sorted(missing))}", code="invalid_argument")
    return body


def _create_body(args: Namespace, *, include_name: bool) -> dict[str, Any]:
    required = {"business_confidential"}
    allowed = {"description", "business_confidential"}
    if include_name:
        required.add("name")
        allowed.add("name")
    override_names = ("name", "description") if include_name else ("description",)
    body = _request_body(args, allowed=allowed, required=required, override_names=override_names)
    if include_name:
        _validate_name(body["name"])
    return body


def _cas_body(args: Namespace) -> dict[str, Any]:
    body = _request_body(
        args,
        allowed={"expected_active_version"},
        required={"expected_active_version"},
        override_names=("expected_active_version",),
    )
    expected = body["expected_active_version"]
    if expected is not None:
        _validate_version(expected, label="expected_active_version")
    return body


def _wire_body(body: dict[str, Any]) -> dict[str, Any]:
    wire_names = {
        "business_confidential": "businessConfidential",
        "expected_active_version": "expectedActiveVersion",
    }
    return {wire_names.get(name, name): value for name, value in body.items()}


def _validate_name(value: Any) -> str:
    if not isinstance(value, str) or _NAME_RE.fullmatch(value) is None:
        raise CLIError("Invalid policy name", code="invalid_argument", hint="name must match ^[a-z][a-z0-9-]{0,63}$")
    return value


def _validate_version(value: Any, *, label: str = "version") -> str:
    if not isinstance(value, str) or _VERSION_RE.fullmatch(value) is None:
        raise CLIError(f"Invalid {label}", code="invalid_argument", hint=f"{label} must match ^[1-9][0-9]*$")
    return value


def _print_sdk_result(result: _SDKResult | None, args: Namespace) -> None:
    if result is None:
        print_result({}, args)
        return
    print_result(result.model_dump(), args)


def _resource(args: Namespace) -> _RedactionPoliciesResource:
    # Stainless previewで生成されるresourceをCLIの静的境界へ絞る。
    return cast(_QaipWithRedactionPolicies, get_client(args)).redaction_policies


def _validate(args: Namespace) -> None:
    body = _create_body(args, include_name=True)
    if args.dry_run:
        print_dry_run("POST", "/redaction/policies/validate", _wire_body(body))
        return
    result = _resource(args).validate(**body)
    _print_sdk_result(result, args)


def _create(args: Namespace) -> None:
    body = _create_body(args, include_name=True)
    if args.dry_run:
        print_dry_run("POST", "/redaction/policies", _wire_body(body))
        return
    result = _resource(args).create(**body)
    _print_sdk_result(result, args)


def _list(args: Namespace) -> None:
    if args.dry_run:
        print_dry_run("GET", "/redaction/policies")
        return
    result = _resource(args).list()
    _print_sdk_result(result, args)


def _retrieve(args: Namespace) -> None:
    name = _validate_name(args.name)
    if args.dry_run:
        print_dry_run("GET", f"/redaction/policies/{name}")
        return
    result = _resource(args).retrieve(name)
    _print_sdk_result(result, args)


def _create_version(args: Namespace) -> None:
    name = _validate_name(args.name)
    body = _create_body(args, include_name=False)
    if args.dry_run:
        print_dry_run("POST", f"/redaction/policies/{name}/versions", _wire_body(body))
        return
    result = _resource(args).create_version(name, **body)
    _print_sdk_result(result, args)


def _list_versions(args: Namespace) -> None:
    name = _validate_name(args.name)
    if args.limit is not None and not 1 <= args.limit <= 100:
        raise CLIError("--limit must be between 1 and 100", code="invalid_argument")
    before_version = args.before_version
    if before_version is not None:
        _validate_version(before_version, label="before_version")
    params: dict[str, Any] = {}
    if args.limit is not None:
        params["limit"] = args.limit
    if before_version is not None:
        params["beforeVersion"] = before_version
    if args.dry_run:
        print_dry_run("GET", f"/redaction/policies/{name}/versions", params or None)
        return
    result = _resource(args).list_versions(
        name,
        limit=args.limit if args.limit is not None else omit,
        before_version=before_version if before_version is not None else omit,
    )
    _print_sdk_result(result, args)


def _retrieve_version(args: Namespace) -> None:
    name = _validate_name(args.name)
    version = _validate_version(args.version)
    if args.dry_run:
        print_dry_run("GET", f"/redaction/policies/{name}/versions/{version}")
        return
    result = _resource(args).retrieve_version(name, version)
    _print_sdk_result(result, args)


def _activate_version(args: Namespace) -> None:
    name = _validate_name(args.name)
    version = _validate_version(args.version)
    body = _cas_body(args)
    if args.dry_run:
        print_dry_run("POST", f"/redaction/policies/{name}/versions/{version}/activate", _wire_body(body))
        return
    require_yes(args, action="redaction-policies.activate-version")
    result = _resource(args).activate_version(name, version, **body)
    _print_sdk_result(result, args)


def _archive(args: Namespace) -> None:
    name = _validate_name(args.name)
    body = _cas_body(args)
    if args.dry_run:
        print_dry_run("POST", f"/redaction/policies/{name}/archive", _wire_body(body))
        return
    require_yes(args, action="redaction-policies.archive")
    result = _resource(args).archive(name, **body)
    _print_sdk_result(result, args)


def _delete_version(args: Namespace) -> None:
    name = _validate_name(args.name)
    version = _validate_version(args.version)
    if args.dry_run:
        print_dry_run("DELETE", f"/redaction/policies/{name}/versions/{version}")
        return
    require_yes(args, action="redaction-policies.delete-version")
    result = _resource(args).delete_version(name, version)
    _print_sdk_result(result, args)
