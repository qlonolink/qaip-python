# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import shared
from .. import _compat
from .crawl import Crawl as Crawl
from .github import GitHub as GitHub
from .notion import Notion as Notion
from .secret import Secret as Secret
from .shared import (
    Tag as Tag,
    Content as Content,
    FileType as FileType,
    JobError as JobError,
    Metadata as Metadata,
    JobStatus as JobStatus,
    Pagination as Pagination,
    SourceType as SourceType,
    MessageRole as MessageRole,
    CommonFilter as CommonFilter,
    MetadataType as MetadataType,
    ExtractResult as ExtractResult,
    MetadataFilter as MetadataFilter,
    MetadataRecord as MetadataRecord,
    TagSourceGroup as TagSourceGroup,
    LogicalOperator as LogicalOperator,
    MetadataFilterGroup as MetadataFilterGroup,
    BatchSetMetadataResponse as BatchSetMetadataResponse,
)
from .source import Source as Source
from .agent_run import AgentRun as AgentRun
from .secret_type import SecretType as SecretType
from .google_drive import GoogleDrive as GoogleDrive
from .source_group import SourceGroup as SourceGroup
from .crawl_setting import CrawlSetting as CrawlSetting
from .policy_detail import PolicyDetail as PolicyDetail
from .policy_source import PolicySource as PolicySource
from .policy_status import PolicyStatus as PolicyStatus
from .tags_response import TagsResponse as TagsResponse
from .agent_provider import AgentProvider as AgentProvider
from .github_setting import GitHubSetting as GitHubSetting
from .notion_setting import NotionSetting as NotionSetting
from .policy_summary import PolicySummary as PolicySummary
from .policy_version import PolicyVersion as PolicyVersion
from .agent_run_event import AgentRunEvent as AgentRunEvent
from .policy_versions import PolicyVersions as PolicyVersions
from .search_response import SearchResponse as SearchResponse
from .agent_run_status import AgentRunStatus as AgentRunStatus
from .extract_response import ExtractResponse as ExtractResponse
from .local_file_group import LocalFileGroup as LocalFileGroup
from .crawl_list_params import CrawlListParams as CrawlListParams
from .policy_definition import PolicyDefinition as PolicyDefinition
from .github_list_params import GitHubListParams as GitHubListParams
from .notion_list_params import NotionListParams as NotionListParams
from .secret_list_params import SecretListParams as SecretListParams
from .source_list_params import SourceListParams as SourceListParams
from .completion_response import CompletionResponse as CompletionResponse
from .crawl_create_params import CrawlCreateParams as CrawlCreateParams
from .crawl_list_response import CrawlListResponse as CrawlListResponse
from .agent_execution_mode import AgentExecutionMode as AgentExecutionMode
from .client_search_params import ClientSearchParams as ClientSearchParams
from .github_create_params import GitHubCreateParams as GitHubCreateParams
from .github_list_response import GitHubListResponse as GitHubListResponse
from .google_drive_setting import GoogleDriveSetting as GoogleDriveSetting
from .notion_create_params import NotionCreateParams as NotionCreateParams
from .notion_list_response import NotionListResponse as NotionListResponse
from .secret_create_params import SecretCreateParams as SecretCreateParams
from .secret_list_response import SecretListResponse as SecretListResponse
from .secret_update_params import SecretUpdateParams as SecretUpdateParams
from .source_list_response import SourceListResponse as SourceListResponse
from .client_content_params import ClientContentParams as ClientContentParams
from .client_extract_params import ClientExtractParams as ClientExtractParams
from .github_reference_type import GitHubReferenceType as GitHubReferenceType
from .agent_cancel_run_params import AgentCancelRunParams as AgentCancelRunParams
from .agent_create_run_params import AgentCreateRunParams as AgentCreateRunParams
from .client_completion_params import ClientCompletionParams as ClientCompletionParams
from .google_drive_list_params import GoogleDriveListParams as GoogleDriveListParams
from .source_group_list_params import SourceGroupListParams as SourceGroupListParams
from .agent_retrieve_run_params import AgentRetrieveRunParams as AgentRetrieveRunParams
from .chunk_metadata_key_config import ChunkMetadataKeyConfig as ChunkMetadataKeyConfig
from .google_drive_create_params import GoogleDriveCreateParams as GoogleDriveCreateParams
from .google_drive_list_response import GoogleDriveListResponse as GoogleDriveListResponse
from .source_download_raw_params import SourceDownloadRawParams as SourceDownloadRawParams
from .source_group_list_response import SourceGroupListResponse as SourceGroupListResponse
from .crawl_update_setting_params import CrawlUpdateSettingParams as CrawlUpdateSettingParams
from .agent_list_run_events_params import AgentListRunEventsParams as AgentListRunEventsParams
from .crawl_create_url_list_params import CrawlCreateURLListParams as CrawlCreateURLListParams
from .create_agent_run_input_param import CreateAgentRunInputParam as CreateAgentRunInputParam
from .github_update_setting_params import GitHubUpdateSettingParams as GitHubUpdateSettingParams
from .local_file_group_list_params import LocalFileGroupListParams as LocalFileGroupListParams
from .notion_update_setting_params import NotionUpdateSettingParams as NotionUpdateSettingParams
from .source_update_metadata_params import SourceUpdateMetadataParams as SourceUpdateMetadataParams
from .agent_list_run_events_response import AgentListRunEventsResponse as AgentListRunEventsResponse
from .agent_stream_run_events_params import AgentStreamRunEventsParams as AgentStreamRunEventsParams
from .local_file_group_create_params import LocalFileGroupCreateParams as LocalFileGroupCreateParams
from .local_file_group_list_response import LocalFileGroupListResponse as LocalFileGroupListResponse
from .redaction_policy_create_params import RedactionPolicyCreateParams as RedactionPolicyCreateParams
from .redaction_policy_list_response import RedactionPolicyListResponse as RedactionPolicyListResponse
from .tag_source_group_create_params import TagSourceGroupCreateParams as TagSourceGroupCreateParams
from .tag_source_group_delete_params import TagSourceGroupDeleteParams as TagSourceGroupDeleteParams
from .redaction_policy_archive_params import RedactionPolicyArchiveParams as RedactionPolicyArchiveParams
from .source_delete_metadata_response import SourceDeleteMetadataResponse as SourceDeleteMetadataResponse
from .agent_retrieve_run_result_params import AgentRetrieveRunResultParams as AgentRetrieveRunResultParams
from .agent_stream_run_events_response import AgentStreamRunEventsResponse as AgentStreamRunEventsResponse
from .local_file_group_create_response import LocalFileGroupCreateResponse as LocalFileGroupCreateResponse
from .local_file_group_delete_response import LocalFileGroupDeleteResponse as LocalFileGroupDeleteResponse
from .redaction_policy_validate_params import RedactionPolicyValidateParams as RedactionPolicyValidateParams
from .source_batch_set_metadata_params import SourceBatchSetMetadataParams as SourceBatchSetMetadataParams
from .source_group_list_sources_params import SourceGroupListSourcesParams as SourceGroupListSourcesParams
from .crawl_download_raw_archive_params import CrawlDownloadRawArchiveParams as CrawlDownloadRawArchiveParams
from .agent_retrieve_run_result_response import AgentRetrieveRunResultResponse as AgentRetrieveRunResultResponse
from .google_drive_update_setting_params import GoogleDriveUpdateSettingParams as GoogleDriveUpdateSettingParams
from .redaction_policy_validate_response import RedactionPolicyValidateResponse as RedactionPolicyValidateResponse
from .source_group_list_sources_response import SourceGroupListSourcesResponse as SourceGroupListSourcesResponse
from .source_group_update_metadata_params import SourceGroupUpdateMetadataParams as SourceGroupUpdateMetadataParams
from .redaction_policy_list_versions_params import (
    RedactionPolicyListVersionsParams as RedactionPolicyListVersionsParams,
)
from .source_group_delete_metadata_response import (
    SourceGroupDeleteMetadataResponse as SourceGroupDeleteMetadataResponse,
)
from .redaction_policy_create_version_params import (
    RedactionPolicyCreateVersionParams as RedactionPolicyCreateVersionParams,
)
from .source_group_batch_set_metadata_params import (
    SourceGroupBatchSetMetadataParams as SourceGroupBatchSetMetadataParams,
)
from .redaction_policy_activate_version_params import (
    RedactionPolicyActivateVersionParams as RedactionPolicyActivateVersionParams,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    shared.common_filter.CommonFilter.update_forward_refs()  # type: ignore
    shared.metadata_filter_group.MetadataFilterGroup.update_forward_refs()  # type: ignore
else:
    shared.common_filter.CommonFilter.model_rebuild(_parent_namespace_depth=0)
    shared.metadata_filter_group.MetadataFilterGroup.model_rebuild(_parent_namespace_depth=0)
