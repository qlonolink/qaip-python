# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "RedactionPolicyValidateParams",
    "BusinessConfidential",
    "BusinessConfidentialExample",
    "BusinessConfidentialExampleRedactionPolicyBusinessExample",
    "BusinessConfidentialInclude",
    "Address",
]


class RedactionPolicyValidateParams(TypedDict, total=False):
    business_confidential: Required[Annotated[BusinessConfidential, PropertyInfo(alias="businessConfidential")]]

    name: Required[str]

    address: Address
    """How category `A` (address) findings are accepted.

    With `requireStreetNumber` the model's address findings that do not contain a
    street number (`1-2-3`, `3丁目`, `12番地`, `5号`, `〒`) are dropped, so city
    names, shop names and facility names are not masked. Defaults to `false`, and
    the whole object is omitted from responses when it is the default.
    """

    description: Optional[str]

    skipped_boundaries: Annotated[
        Optional[
            List[
                Literal[
                    "initial_input",
                    "rag_query",
                    "rag_result",
                    "google_query",
                    "google_result",
                    "tool_result",
                    "external_table_result",
                    "x_query",
                    "xai_query",
                    "chartmetric_query",
                    "chartmetric_result",
                    "completions_messages",
                    "completions_query",
                    "completions_docs",
                ]
            ]
        ],
        PropertyInfo(alias="skippedBoundaries"),
    ]
    """
    Boundaries to leave unredacted (the policy still redacts every other boundary,
    including boundaries added to QAIP later). Omitted, `null` or `[]` redacts every
    boundary. Listing every boundary is rejected: omit `redactionPolicyId` on the
    run instead. Skipping `rag_result` / `completions_docs` sends knowledge-base
    chunks to the external model unmasked; only do so when the chunks were masked at
    ingestion, and note that ingestion-time masking covers 7 PII categories only,
    never `K` (credentials) or `B` (business confidential).
    """


class BusinessConfidentialExampleRedactionPolicyBusinessExample(TypedDict, total=False):
    """
    An example sentence for the model, paired with the parts of it the model should return. An empty `findings` list marks a counterexample the model should not return anything for. It does not exclude matching text from detection.
    """

    findings: Required[SequenceNotStr[str]]

    text: Required[str]


BusinessConfidentialExample: TypeAlias = Union[str, BusinessConfidentialExampleRedactionPolicyBusinessExample]


class BusinessConfidentialInclude(TypedDict, total=False):
    mode: Required[Literal["exact", "value_clause", "exact_or_value_clause", "value"]]
    """How a literal occurrence of `text` is masked.

    `exact` masks the word itself. `value_clause` masks from the word to the end of
    the clause only when a value follows it (an assignment such as `は` / `:` / `=`,
    or a number right after the word). `exact_or_value_clause` masks the value
    clause when a value follows and the word alone otherwise. `value` masks only the
    number that follows the word and never the word itself.
    """

    text: Required[str]


class BusinessConfidential(TypedDict, total=False):
    definition: Required[str]

    examples: Required[SequenceNotStr[BusinessConfidentialExample]]
    """
    Example sentences shown to the model only; they are never matched against the
    input. A plain string is a whole-sentence example, and a `{text, findings}`
    object shows the model which parts of the sentence to return. Use `include` with
    mode `exact` to always mask a fixed phrase and `exclude` to keep one.
    """

    exclude: Required[SequenceNotStr[str]]
    """
    Words that literally appear in the input and must not be masked as business
    confidential, such as public product names or compound words that contain an
    include word.
    """

    include: Required[Iterable[BusinessConfidentialInclude]]
    """
    Words that literally appear in the input, such as product or project names and
    cost items. Descriptive phrases that never occur verbatim have no effect.
    """

    semantic_boundary: Annotated[Literal["clause", "finding"], PropertyInfo(alias="semanticBoundary")]
    """
    Boundary applied to every model finding that is not covered by `include`,
    including findings the model returns by following `examples`. `clause` (default)
    expands the finding to its clause and `finding` keeps only the reported text
    (the value, name or identifier itself). Omitted from responses when it is the
    default.
    """


class Address(TypedDict, total=False):
    """How category `A` (address) findings are accepted.

    With `requireStreetNumber` the model's address findings that do not contain a street number (`1-2-3`, `3丁目`, `12番地`, `5号`, `〒`) are dropped, so city names, shop names and facility names are not masked. Defaults to `false`, and the whole object is omitted from responses when it is the default.
    """

    require_street_number: Required[Annotated[bool, PropertyInfo(alias="requireStreetNumber")]]
