# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import shared
from .. import _compat
from .shared import (
    Content as Content,
    FileType as FileType,
    SourceType as SourceType,
    MetadataFilterGroup as MetadataFilterGroup,
)
from .tags_response import TagsResponse as TagsResponse
from .search_response import SearchResponse as SearchResponse
from .extract_response import ExtractResponse as ExtractResponse
from .completion_response import CompletionResponse as CompletionResponse
from .client_search_params import ClientSearchParams as ClientSearchParams
from .client_extract_params import ClientExtractParams as ClientExtractParams
from .client_completion_params import ClientCompletionParams as ClientCompletionParams

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    shared.metadata_filter_group.MetadataFilterGroup.update_forward_refs()  # type: ignore
else:
    shared.metadata_filter_group.MetadataFilterGroup.model_rebuild(_parent_namespace_depth=0)
