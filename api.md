# Shared Types

```python
from qaip.types import (
    BatchSetMetadataResponse,
    CommonFilter,
    Content,
    ExtractResult,
    FileType,
    JobError,
    JobStatus,
    LogicalOperator,
    MessageRole,
    Metadata,
    MetadataFilter,
    MetadataFilterGroup,
    MetadataRecord,
    MetadataType,
    Pagination,
    SourceType,
    Tag,
    TagSourceGroup,
)
```

# Qaip

Types:

```python
from qaip.types import CompletionResponse, ExtractResponse, SearchResponse, TagsResponse
```

Methods:

- <code title="post /completions">client.<a href="./src/qaip/_client.py">completion</a>(\*\*<a href="src/qaip/types/client_completion_params.py">params</a>) -> <a href="./src/qaip/types/completion_response.py">CompletionResponse</a></code>
- <code title="get /contents/{id}">client.<a href="./src/qaip/_client.py">content</a>(id) -> <a href="./src/qaip/types/shared/content.py">Content</a></code>
- <code title="post /extract">client.<a href="./src/qaip/_client.py">extract</a>(\*\*<a href="src/qaip/types/client_extract_params.py">params</a>) -> <a href="./src/qaip/types/extract_response.py">ExtractResponse</a></code>
- <code title="post /search">client.<a href="./src/qaip/_client.py">search</a>(\*\*<a href="src/qaip/types/client_search_params.py">params</a>) -> <a href="./src/qaip/types/search_response.py">SearchResponse</a></code>
- <code title="get /tags">client.<a href="./src/qaip/_client.py">tags</a>() -> <a href="./src/qaip/types/tags_response.py">TagsResponse</a></code>

# Agent

Types:

```python
from qaip.types import (
    AgentExecutionMode,
    AgentFilters,
    AgentMessage,
    AgentMessageContent,
    AgentProvider,
    AgentRun,
    AgentRunEvent,
    AgentRunStatus,
    AgentListRunEventsResponse,
    AgentRetrieveRunResultResponse,
    AgentRunResponse,
)
```

Methods:

- <code title="post /agent/runs/{run_id}/cancel">client.agent.<a href="./src/qaip/resources/agent.py">cancel_run</a>(run_id) -> <a href="./src/qaip/types/agent_run.py">AgentRun</a></code>
- <code title="post /agent/runs">client.agent.<a href="./src/qaip/resources/agent.py">create_run</a>(\*\*<a href="src/qaip/types/agent_create_run_params.py">params</a>) -> <a href="./src/qaip/types/agent_run.py">AgentRun</a></code>
- <code title="get /agent/runs/{run_id}/events">client.agent.<a href="./src/qaip/resources/agent.py">list_run_events</a>(run_id, \*\*<a href="src/qaip/types/agent_list_run_events_params.py">params</a>) -> <a href="./src/qaip/types/agent_list_run_events_response.py">AgentListRunEventsResponse</a></code>
- <code title="get /agent/runs/{run_id}">client.agent.<a href="./src/qaip/resources/agent.py">retrieve_run</a>(run_id) -> <a href="./src/qaip/types/agent_run.py">AgentRun</a></code>
- <code title="get /agent/runs/{run_id}/result">client.agent.<a href="./src/qaip/resources/agent.py">retrieve_run_result</a>(run_id) -> <a href="./src/qaip/types/agent_retrieve_run_result_response.py">AgentRetrieveRunResultResponse</a></code>
- <code title="post /agent/run">client.agent.<a href="./src/qaip/resources/agent.py">run</a>(\*\*<a href="src/qaip/types/agent_run_params.py">params</a>) -> str</code>

# TagSourceGroups

Methods:

- <code title="post /tag-source-groups">client.tag_source_groups.<a href="./src/qaip/resources/tag_source_groups.py">create</a>(\*\*<a href="src/qaip/types/tag_source_group_create_params.py">params</a>) -> <a href="./src/qaip/types/shared/tag_source_group.py">TagSourceGroup</a></code>
- <code title="delete /tag-source-groups">client.tag_source_groups.<a href="./src/qaip/resources/tag_source_groups.py">delete</a>(\*\*<a href="src/qaip/types/tag_source_group_delete_params.py">params</a>) -> <a href="./src/qaip/types/shared/tag_source_group.py">TagSourceGroup</a></code>

# SourceGroups

Types:

```python
from qaip.types import (
    SourceGroup,
    SourceGroupListResponse,
    SourceGroupDeleteMetadataResponse,
    SourceGroupListSourcesResponse,
)
```

Methods:

- <code title="get /source-groups/{source_group_id}">client.source_groups.<a href="./src/qaip/resources/source_groups.py">retrieve</a>(source_group_id) -> <a href="./src/qaip/types/source_group.py">SourceGroup</a></code>
- <code title="get /source-groups">client.source_groups.<a href="./src/qaip/resources/source_groups.py">list</a>(\*\*<a href="src/qaip/types/source_group_list_params.py">params</a>) -> <a href="./src/qaip/types/source_group_list_response.py">SourceGroupListResponse</a></code>
- <code title="post /source-groups/metadata/batch">client.source_groups.<a href="./src/qaip/resources/source_groups.py">batch_set_metadata</a>(\*\*<a href="src/qaip/types/source_group_batch_set_metadata_params.py">params</a>) -> <a href="./src/qaip/types/shared/batch_set_metadata_response.py">BatchSetMetadataResponse</a></code>
- <code title="delete /source-groups/{source_group_id}/metadata">client.source_groups.<a href="./src/qaip/resources/source_groups.py">delete_metadata</a>(source_group_id) -> <a href="./src/qaip/types/source_group_delete_metadata_response.py">SourceGroupDeleteMetadataResponse</a></code>
- <code title="get /source-groups/{source_group_id}/sources">client.source_groups.<a href="./src/qaip/resources/source_groups.py">list_sources</a>(source_group_id) -> <a href="./src/qaip/types/source_group_list_sources_response.py">SourceGroupListSourcesResponse</a></code>
- <code title="get /source-groups/{source_group_id}/metadata">client.source_groups.<a href="./src/qaip/resources/source_groups.py">retrieve_metadata</a>(source_group_id) -> <a href="./src/qaip/types/shared/metadata.py">Metadata</a></code>
- <code title="put /source-groups/{source_group_id}/metadata">client.source_groups.<a href="./src/qaip/resources/source_groups.py">update_metadata</a>(source_group_id, \*\*<a href="src/qaip/types/source_group_update_metadata_params.py">params</a>) -> <a href="./src/qaip/types/shared/metadata.py">Metadata</a></code>

# Sources

Types:

```python
from qaip.types import Source, SourceListResponse, SourceDeleteMetadataResponse
```

Methods:

- <code title="get /sources/{source_id}">client.sources.<a href="./src/qaip/resources/sources.py">retrieve</a>(source_id) -> <a href="./src/qaip/types/source.py">Source</a></code>
- <code title="get /sources">client.sources.<a href="./src/qaip/resources/sources.py">list</a>(\*\*<a href="src/qaip/types/source_list_params.py">params</a>) -> <a href="./src/qaip/types/source_list_response.py">SourceListResponse</a></code>
- <code title="post /sources/metadata/batch">client.sources.<a href="./src/qaip/resources/sources.py">batch_set_metadata</a>(\*\*<a href="src/qaip/types/source_batch_set_metadata_params.py">params</a>) -> <a href="./src/qaip/types/shared/batch_set_metadata_response.py">BatchSetMetadataResponse</a></code>
- <code title="delete /sources/{source_id}/metadata">client.sources.<a href="./src/qaip/resources/sources.py">delete_metadata</a>(source_id) -> <a href="./src/qaip/types/source_delete_metadata_response.py">SourceDeleteMetadataResponse</a></code>
- <code title="get /sources/{source_id}/metadata">client.sources.<a href="./src/qaip/resources/sources.py">retrieve_metadata</a>(source_id) -> <a href="./src/qaip/types/shared/metadata.py">Metadata</a></code>
- <code title="put /sources/{source_id}/metadata">client.sources.<a href="./src/qaip/resources/sources.py">update_metadata</a>(source_id, \*\*<a href="src/qaip/types/source_update_metadata_params.py">params</a>) -> <a href="./src/qaip/types/shared/metadata.py">Metadata</a></code>

# LocalFileGroups

Types:

```python
from qaip.types import (
    ChunkMetadataKeyConfig,
    LocalFileGroup,
    LocalFileGroupCreateResponse,
    LocalFileGroupListResponse,
    LocalFileGroupDeleteResponse,
)
```

Methods:

- <code title="post /local-file-groups">client.local_file_groups.<a href="./src/qaip/resources/local_file_groups.py">create</a>(\*\*<a href="src/qaip/types/local_file_group_create_params.py">params</a>) -> <a href="./src/qaip/types/local_file_group_create_response.py">LocalFileGroupCreateResponse</a></code>
- <code title="get /local-file-groups/{id}">client.local_file_groups.<a href="./src/qaip/resources/local_file_groups.py">retrieve</a>(id) -> <a href="./src/qaip/types/local_file_group.py">LocalFileGroup</a></code>
- <code title="get /local-file-groups">client.local_file_groups.<a href="./src/qaip/resources/local_file_groups.py">list</a>(\*\*<a href="src/qaip/types/local_file_group_list_params.py">params</a>) -> <a href="./src/qaip/types/local_file_group_list_response.py">LocalFileGroupListResponse</a></code>
- <code title="delete /local-file-groups/{id}">client.local_file_groups.<a href="./src/qaip/resources/local_file_groups.py">delete</a>(id) -> <a href="./src/qaip/types/local_file_group_delete_response.py">LocalFileGroupDeleteResponse</a></code>

# Secrets

Types:

```python
from qaip.types import Secret, SecretType, SecretListResponse
```

Methods:

- <code title="post /secrets">client.secrets.<a href="./src/qaip/resources/secrets.py">create</a>(\*\*<a href="src/qaip/types/secret_create_params.py">params</a>) -> <a href="./src/qaip/types/secret.py">Secret</a></code>
- <code title="get /secrets/{secret_id}">client.secrets.<a href="./src/qaip/resources/secrets.py">retrieve</a>(secret_id) -> <a href="./src/qaip/types/secret.py">Secret</a></code>
- <code title="put /secrets/{secret_id}">client.secrets.<a href="./src/qaip/resources/secrets.py">update</a>(secret_id, \*\*<a href="src/qaip/types/secret_update_params.py">params</a>) -> <a href="./src/qaip/types/secret.py">Secret</a></code>
- <code title="get /secrets">client.secrets.<a href="./src/qaip/resources/secrets.py">list</a>(\*\*<a href="src/qaip/types/secret_list_params.py">params</a>) -> <a href="./src/qaip/types/secret_list_response.py">SecretListResponse</a></code>
- <code title="delete /secrets/{secret_id}">client.secrets.<a href="./src/qaip/resources/secrets.py">delete</a>(secret_id) -> <a href="./src/qaip/types/secret.py">Secret</a></code>

# GoogleDrives

Types:

```python
from qaip.types import GoogleDrive, GoogleDriveSetting, GoogleDriveListResponse
```

Methods:

- <code title="post /google-drives">client.google_drives.<a href="./src/qaip/resources/google_drives.py">create</a>(\*\*<a href="src/qaip/types/google_drive_create_params.py">params</a>) -> <a href="./src/qaip/types/google_drive.py">GoogleDrive</a></code>
- <code title="get /google-drives/{id}">client.google_drives.<a href="./src/qaip/resources/google_drives.py">retrieve</a>(id) -> <a href="./src/qaip/types/google_drive.py">GoogleDrive</a></code>
- <code title="get /google-drives">client.google_drives.<a href="./src/qaip/resources/google_drives.py">list</a>(\*\*<a href="src/qaip/types/google_drive_list_params.py">params</a>) -> <a href="./src/qaip/types/google_drive_list_response.py">GoogleDriveListResponse</a></code>
- <code title="delete /google-drives/{id}">client.google_drives.<a href="./src/qaip/resources/google_drives.py">delete</a>(id) -> <a href="./src/qaip/types/google_drive.py">GoogleDrive</a></code>
- <code title="get /google-drive-settings/{id}">client.google_drives.<a href="./src/qaip/resources/google_drives.py">retrieve_setting</a>(id) -> <a href="./src/qaip/types/google_drive_setting.py">GoogleDriveSetting</a></code>
- <code title="put /google-drive-settings/{id}">client.google_drives.<a href="./src/qaip/resources/google_drives.py">update_setting</a>(id, \*\*<a href="src/qaip/types/google_drive_update_setting_params.py">params</a>) -> <a href="./src/qaip/types/google_drive_setting.py">GoogleDriveSetting</a></code>

# Crawls

Types:

```python
from qaip.types import Crawl, CrawlSetting, CrawlListResponse
```

Methods:

- <code title="post /crawls">client.crawls.<a href="./src/qaip/resources/crawls.py">create</a>(\*\*<a href="src/qaip/types/crawl_create_params.py">params</a>) -> <a href="./src/qaip/types/crawl.py">Crawl</a></code>
- <code title="get /crawls/{id}">client.crawls.<a href="./src/qaip/resources/crawls.py">retrieve</a>(id) -> <a href="./src/qaip/types/crawl.py">Crawl</a></code>
- <code title="get /crawls">client.crawls.<a href="./src/qaip/resources/crawls.py">list</a>(\*\*<a href="src/qaip/types/crawl_list_params.py">params</a>) -> <a href="./src/qaip/types/crawl_list_response.py">CrawlListResponse</a></code>
- <code title="delete /crawls/{id}">client.crawls.<a href="./src/qaip/resources/crawls.py">delete</a>(id) -> <a href="./src/qaip/types/crawl.py">Crawl</a></code>
- <code title="post /crawl-url-lists">client.crawls.<a href="./src/qaip/resources/crawls.py">create_url_list</a>(\*\*<a href="src/qaip/types/crawl_create_url_list_params.py">params</a>) -> <a href="./src/qaip/types/crawl.py">Crawl</a></code>
- <code title="get /crawl-settings/{id}">client.crawls.<a href="./src/qaip/resources/crawls.py">retrieve_setting</a>(id) -> <a href="./src/qaip/types/crawl_setting.py">CrawlSetting</a></code>
- <code title="put /crawl-settings/{id}">client.crawls.<a href="./src/qaip/resources/crawls.py">update_setting</a>(id, \*\*<a href="src/qaip/types/crawl_update_setting_params.py">params</a>) -> <a href="./src/qaip/types/crawl_setting.py">CrawlSetting</a></code>

# Githubs

Types:

```python
from qaip.types import GitHub, GitHubReferenceType, GitHubSetting, GitHubListResponse
```

Methods:

- <code title="post /githubs">client.githubs.<a href="./src/qaip/resources/githubs.py">create</a>(\*\*<a href="src/qaip/types/github_create_params.py">params</a>) -> <a href="./src/qaip/types/github.py">GitHub</a></code>
- <code title="get /githubs/{id}">client.githubs.<a href="./src/qaip/resources/githubs.py">retrieve</a>(id) -> <a href="./src/qaip/types/github.py">GitHub</a></code>
- <code title="get /githubs">client.githubs.<a href="./src/qaip/resources/githubs.py">list</a>(\*\*<a href="src/qaip/types/github_list_params.py">params</a>) -> <a href="./src/qaip/types/github_list_response.py">GitHubListResponse</a></code>
- <code title="delete /githubs/{id}">client.githubs.<a href="./src/qaip/resources/githubs.py">delete</a>(id) -> <a href="./src/qaip/types/github.py">GitHub</a></code>
- <code title="get /github-settings/{id}">client.githubs.<a href="./src/qaip/resources/githubs.py">retrieve_setting</a>(id) -> <a href="./src/qaip/types/github_setting.py">GitHubSetting</a></code>
- <code title="put /github-settings/{id}">client.githubs.<a href="./src/qaip/resources/githubs.py">update_setting</a>(id, \*\*<a href="src/qaip/types/github_update_setting_params.py">params</a>) -> <a href="./src/qaip/types/github_setting.py">GitHubSetting</a></code>

# Notions

Types:

```python
from qaip.types import Notion, NotionSetting, NotionListResponse
```

Methods:

- <code title="post /notions">client.notions.<a href="./src/qaip/resources/notions.py">create</a>(\*\*<a href="src/qaip/types/notion_create_params.py">params</a>) -> <a href="./src/qaip/types/notion.py">Notion</a></code>
- <code title="get /notions/{id}">client.notions.<a href="./src/qaip/resources/notions.py">retrieve</a>(id) -> <a href="./src/qaip/types/notion.py">Notion</a></code>
- <code title="get /notions">client.notions.<a href="./src/qaip/resources/notions.py">list</a>(\*\*<a href="src/qaip/types/notion_list_params.py">params</a>) -> <a href="./src/qaip/types/notion_list_response.py">NotionListResponse</a></code>
- <code title="delete /notions/{id}">client.notions.<a href="./src/qaip/resources/notions.py">delete</a>(id) -> <a href="./src/qaip/types/notion.py">Notion</a></code>
- <code title="get /notion-settings/{id}">client.notions.<a href="./src/qaip/resources/notions.py">retrieve_setting</a>(id) -> <a href="./src/qaip/types/notion_setting.py">NotionSetting</a></code>
- <code title="put /notion-settings/{id}">client.notions.<a href="./src/qaip/resources/notions.py">update_setting</a>(id, \*\*<a href="src/qaip/types/notion_update_setting_params.py">params</a>) -> <a href="./src/qaip/types/notion_setting.py">NotionSetting</a></code>
