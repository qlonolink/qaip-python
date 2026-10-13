# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PolicyDefinition",
    "BusinessConfidential",
    "BusinessConfidentialExample",
    "BusinessConfidentialExampleRedactionPolicyBusinessExample",
    "BusinessConfidentialInclude",
    "Address",
]


class BusinessConfidentialExampleRedactionPolicyBusinessExample(BaseModel):
    """
    An example sentence for the model, paired with the parts of it the model should return. An empty `findings` list marks a counterexample the model should not return anything for. It does not exclude matching text from detection.
    """

    findings: List[str]

    text: str


BusinessConfidentialExample: TypeAlias = Union[str, BusinessConfidentialExampleRedactionPolicyBusinessExample]


class BusinessConfidentialInclude(BaseModel):
    mode: Literal["exact", "value_clause", "exact_or_value_clause", "value"]
    """How a literal occurrence of `text` is masked.

    `exact` masks the word itself. `value_clause` masks from the word to the end of
    the clause only when a value follows it (an assignment such as `は` / `:` / `=`,
    or a number right after the word). `exact_or_value_clause` masks the value
    clause when a value follows and the word alone otherwise. `value` masks only the
    number that follows the word and never the word itself.
    """

    text: str


class BusinessConfidential(BaseModel):
    definition: str

    examples: List[BusinessConfidentialExample]
    """
    Example sentences shown to the model only; they are never matched against the
    input. A plain string is a whole-sentence example, and a `{text, findings}`
    object shows the model which parts of the sentence to return. Use `include` with
    mode `exact` to always mask a fixed phrase and `exclude` to keep one.
    """

    exclude: List[str]
    """
    Words that literally appear in the input and must not be masked as business
    confidential, such as public product names or compound words that contain an
    include word.
    """

    include: List[BusinessConfidentialInclude]
    """
    Words that literally appear in the input, such as product or project names and
    cost items. Descriptive phrases that never occur verbatim have no effect.
    """

    semantic_boundary: Optional[Literal["clause", "finding"]] = FieldInfo(alias="semanticBoundary", default=None)
    """
    Boundary applied to every model finding that is not covered by `include`,
    including findings the model returns by following `examples`. `clause` (default)
    expands the finding to its clause and `finding` keeps only the reported text
    (the value, name or identifier itself). Omitted from responses when it is the
    default.
    """


class Address(BaseModel):
    """How category `A` (address) findings are accepted.

    With `requireStreetNumber` the model's address findings that do not contain a street number (`1-2-3`, `3丁目`, `12番地`, `5号`, `〒`) are dropped, so city names, shop names and facility names are not masked. Defaults to `false`, and the whole object is omitted from responses when it is the default.
    """

    require_street_number: bool = FieldInfo(alias="requireStreetNumber")


class PolicyDefinition(BaseModel):
    business_confidential: Optional[BusinessConfidential] = FieldInfo(alias="businessConfidential", default=None)

    enabled_categories: List[Literal["N", "T", "E", "A", "I", "C", "P", "K", "B"]] = FieldInfo(
        alias="enabledCategories"
    )

    skipped_boundaries: List[
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
    ] = FieldInfo(alias="skippedBoundaries")
    """Boundaries this policy leaves unredacted, in canonical order.

    An empty array means every boundary is redacted.
    """

    address: Optional[Address] = None
    """How category `A` (address) findings are accepted.

    With `requireStreetNumber` the model's address findings that do not contain a
    street number (`1-2-3`, `3丁目`, `12番地`, `5号`, `〒`) are dropped, so city
    names, shop names and facility names are not masked. Defaults to `false`, and
    the whole object is omitted from responses when it is the default.
    """
