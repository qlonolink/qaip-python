from __future__ import annotations

import sys
import json
from typing import Any

RESOURCES: dict[str, dict[str, Any]] = {
    "completion": {
        "description": "Generate AI completions from indexed content",
        "methods": {
            "create": {
                "http_method": "POST",
                "path": "/completions",
                "required_params": ["messages"],
                "optional_params": [
                    "chunk_metadata",
                    "citation",
                    "date_from",
                    "date_to",
                    "domains",
                    "file_types",
                    "metadata",
                    "source_metadata",
                    "source_types",
                    "stream",
                    "tag_filter_logic",
                    "tag_ids",
                    "tags",
                ],
            }
        },
    },
    "search": {
        "description": "Search indexed content",
        "methods": {
            "create": {
                "http_method": "POST",
                "path": "/search",
                "required_params": ["query"],
                "optional_params": [
                    "chunk_metadata",
                    "date_from",
                    "date_to",
                    "domains",
                    "file_types",
                    "limit",
                    "metadata",
                    "offset",
                    "source_metadata",
                    "source_types",
                    "tag_filter_logic",
                    "tag_ids",
                    "tags",
                ],
            }
        },
    },
    "extract": {
        "description": "Extract structured data from indexed content",
        "methods": {
            "create": {
                "http_method": "POST",
                "path": "/extract",
                "required_params": ["schema"],
                "optional_params": [
                    "chunk_metadata",
                    "date_from",
                    "date_to",
                    "domains",
                    "file_types",
                    "limit",
                    "metadata",
                    "offset",
                    "prompt",
                    "related_filter",
                    "source_metadata",
                    "source_types",
                    "tag_filter_logic",
                    "tag_ids",
                    "tags",
                    "use_related",
                ],
            }
        },
    },
    "content": {
        "description": "Retrieve content by ID",
        "methods": {
            "retrieve": {
                "http_method": "GET",
                "path": "/contents/{id}",
                "required_params": ["id"],
                "optional_params": [],
            }
        },
    },
    "tags": {
        "description": "List tags",
        "methods": {
            "list": {
                "http_method": "GET",
                "path": "/tags",
                "required_params": [],
                "optional_params": [],
            }
        },
    },
    "sources": {
        "description": "Source management and metadata",
        "methods": {
            "retrieve": {
                "http_method": "GET",
                "path": "/sources/{source_id}",
                "required_params": ["source_id"],
                "optional_params": [],
            },
            "list": {
                "http_method": "GET",
                "path": "/sources",
                "required_params": [],
                "optional_params": ["after_id", "limit"],
            },
            "retrieve_metadata": {
                "http_method": "GET",
                "path": "/sources/{source_id}/metadata",
                "required_params": ["source_id"],
                "optional_params": [],
            },
            "update_metadata": {
                "http_method": "PUT",
                "path": "/sources/{source_id}/metadata",
                "required_params": ["source_id", "metadata"],
                "optional_params": [],
            },
            "delete_metadata": {
                "http_method": "DELETE",
                "path": "/sources/{source_id}/metadata",
                "required_params": ["source_id"],
                "optional_params": [],
            },
            "batch_set_metadata": {
                "http_method": "POST",
                "path": "/sources/metadata/batch",
                "required_params": ["items"],
                "optional_params": [],
            },
        },
    },
    "source-groups": {
        "description": "Source group (job) management and metadata",
        "methods": {
            "retrieve": {
                "http_method": "GET",
                "path": "/source-groups/{source_group_id}",
                "required_params": ["source_group_id"],
                "optional_params": [],
            },
            "list": {
                "http_method": "GET",
                "path": "/source-groups",
                "required_params": [],
                "optional_params": ["after_id", "limit", "source_type"],
            },
            "list_sources": {
                "http_method": "GET",
                "path": "/source-groups/{source_group_id}/sources",
                "required_params": ["source_group_id"],
                "optional_params": [],
            },
            "retrieve_metadata": {
                "http_method": "GET",
                "path": "/source-groups/{source_group_id}/metadata",
                "required_params": ["source_group_id"],
                "optional_params": [],
            },
            "update_metadata": {
                "http_method": "PUT",
                "path": "/source-groups/{source_group_id}/metadata",
                "required_params": ["source_group_id", "metadata"],
                "optional_params": [],
            },
            "delete_metadata": {
                "http_method": "DELETE",
                "path": "/source-groups/{source_group_id}/metadata",
                "required_params": ["source_group_id"],
                "optional_params": [],
            },
            "batch_set_metadata": {
                "http_method": "POST",
                "path": "/source-groups/metadata/batch",
                "required_params": ["items"],
                "optional_params": [],
            },
        },
    },
    "secrets": {
        "description": "Secret management",
        "methods": {
            "create": {
                "http_method": "POST",
                "path": "/secrets",
                "required_params": ["name", "secret", "type"],
                "optional_params": ["description"],
            },
            "retrieve": {
                "http_method": "GET",
                "path": "/secrets/{secret_id}",
                "required_params": ["secret_id"],
                "optional_params": [],
            },
            "update": {
                "http_method": "PUT",
                "path": "/secrets/{secret_id}",
                "required_params": ["secret_id", "name"],
                "optional_params": ["description", "secret"],
            },
            "list": {
                "http_method": "GET",
                "path": "/secrets",
                "required_params": [],
                "optional_params": ["after_id", "limit", "secret_type"],
            },
            "delete": {
                "http_method": "DELETE",
                "path": "/secrets/{secret_id}",
                "required_params": ["secret_id"],
                "optional_params": [],
            },
        },
    },
    "crawls": {
        "description": "Web crawl management",
        "methods": {
            "create": {
                "http_method": "POST",
                "path": "/crawls",
                "required_params": ["max_depth", "max_num_files", "name", "start_url"],
                "optional_params": [
                    "content_pattern",
                    "file_extensions",
                    "html_only",
                    "metadata",
                    "path_filters",
                    "rrule",
                    "use_browser",
                ],
            },
            "retrieve": {
                "http_method": "GET",
                "path": "/crawls/{id}",
                "required_params": ["id"],
                "optional_params": [],
            },
            "list": {
                "http_method": "GET",
                "path": "/crawls",
                "required_params": [],
                "optional_params": ["after_id", "limit"],
            },
            "delete": {
                "http_method": "DELETE",
                "path": "/crawls/{id}",
                "required_params": ["id"],
                "optional_params": [],
            },
            "retrieve_setting": {
                "http_method": "GET",
                "path": "/crawl-settings/{id}",
                "required_params": ["id"],
                "optional_params": [],
            },
            "update_setting": {
                "http_method": "PUT",
                "path": "/crawl-settings/{id}",
                "required_params": ["id", "name"],
                "optional_params": ["rrule"],
            },
            "create_url_list": {
                "http_method": "POST",
                "path": "/crawl-url-lists",
                "required_params": ["name", "target_urls"],
                "optional_params": ["max_num_files", "metadata", "rrule"],
            },
        },
    },
    "google-drives": {
        "description": "Google Drive integration",
        "methods": {
            "create": {
                "http_method": "POST",
                "path": "/google-drives",
                "required_params": ["folder_url", "name"],
                "optional_params": ["metadata", "rrule", "secret_id", "service_account_key"],
            },
            "retrieve": {
                "http_method": "GET",
                "path": "/google-drives/{id}",
                "required_params": ["id"],
                "optional_params": [],
            },
            "list": {
                "http_method": "GET",
                "path": "/google-drives",
                "required_params": [],
                "optional_params": ["after_id", "limit"],
            },
            "delete": {
                "http_method": "DELETE",
                "path": "/google-drives/{id}",
                "required_params": ["id"],
                "optional_params": [],
            },
            "retrieve_setting": {
                "http_method": "GET",
                "path": "/google-drive-settings/{id}",
                "required_params": ["id"],
                "optional_params": [],
            },
            "update_setting": {
                "http_method": "PUT",
                "path": "/google-drive-settings/{id}",
                "required_params": ["id", "name"],
                "optional_params": ["rrule"],
            },
        },
    },
    "githubs": {
        "description": "GitHub repository integration",
        "methods": {
            "create": {
                "http_method": "POST",
                "path": "/githubs",
                "required_params": ["name", "repository"],
                "optional_params": [
                    "github_token",
                    "metadata",
                    "path_filters",
                    "reference_param",
                    "reference_type",
                    "rrule",
                    "secret_id",
                ],
            },
            "retrieve": {
                "http_method": "GET",
                "path": "/githubs/{id}",
                "required_params": ["id"],
                "optional_params": [],
            },
            "list": {
                "http_method": "GET",
                "path": "/githubs",
                "required_params": [],
                "optional_params": ["after_id", "limit"],
            },
            "delete": {
                "http_method": "DELETE",
                "path": "/githubs/{id}",
                "required_params": ["id"],
                "optional_params": [],
            },
            "retrieve_setting": {
                "http_method": "GET",
                "path": "/github-settings/{id}",
                "required_params": ["id"],
                "optional_params": [],
            },
            "update_setting": {
                "http_method": "PUT",
                "path": "/github-settings/{id}",
                "required_params": ["id", "name"],
                "optional_params": ["rrule"],
            },
        },
    },
    "notions": {
        "description": "Notion workspace integration",
        "methods": {
            "create": {
                "http_method": "POST",
                "path": "/notions",
                "required_params": ["name", "page_id"],
                "optional_params": ["metadata", "notion_token", "rrule", "secret_id"],
            },
            "retrieve": {
                "http_method": "GET",
                "path": "/notions/{id}",
                "required_params": ["id"],
                "optional_params": [],
            },
            "list": {
                "http_method": "GET",
                "path": "/notions",
                "required_params": [],
                "optional_params": ["after_id", "limit"],
            },
            "delete": {
                "http_method": "DELETE",
                "path": "/notions/{id}",
                "required_params": ["id"],
                "optional_params": [],
            },
            "retrieve_setting": {
                "http_method": "GET",
                "path": "/notion-settings/{id}",
                "required_params": ["id"],
                "optional_params": [],
            },
            "update_setting": {
                "http_method": "PUT",
                "path": "/notion-settings/{id}",
                "required_params": ["id", "name"],
                "optional_params": ["rrule"],
            },
        },
    },
    "local-file-groups": {
        "description": "Local file group management",
        "methods": {
            "create": {
                "http_method": "POST",
                "path": "/local-file-groups",
                "required_params": ["files", "last_modified", "name"],
                "optional_params": ["chunk_metadata_keys"],
                "content_type": "multipart/form-data",
            },
            "retrieve": {
                "http_method": "GET",
                "path": "/local-file-groups/{id}",
                "required_params": ["id"],
                "optional_params": [],
            },
            "list": {
                "http_method": "GET",
                "path": "/local-file-groups",
                "required_params": [],
                "optional_params": ["after_id", "limit"],
            },
            "delete": {
                "http_method": "DELETE",
                "path": "/local-file-groups/{id}",
                "required_params": ["id"],
                "optional_params": [],
            },
        },
    },
    "agent": {
        "description": "(Experimental) Agent operations",
        "methods": {
            "run": {
                "http_method": "POST",
                "path": "/agent/run",
                "required_params": [],
                "optional_params": [
                    "forwarded_props",
                    "messages",
                    "run_id",
                    "thread_id",
                ],
            },
            "create_run": {
                "http_method": "POST",
                "path": "/agent/runs",
                "required_params": ["input"],
                "optional_params": [
                    "idempotency_key",
                ],
            },
            "retrieve_run": {
                "http_method": "GET",
                "path": "/agent/runs/{run_id}",
                "required_params": ["run_id"],
                "optional_params": [],
            },
            "cancel_run": {
                "http_method": "POST",
                "path": "/agent/runs/{run_id}/cancel",
                "required_params": ["run_id"],
                "optional_params": [],
            },
            "retrieve_run_result": {
                "http_method": "GET",
                "path": "/agent/runs/{run_id}/result",
                "required_params": ["run_id"],
                "optional_params": [],
            },
            "list_run_events": {
                "http_method": "GET",
                "path": "/agent/runs/{run_id}/events",
                "required_params": ["run_id"],
                "optional_params": ["after", "limit"],
            },
        },
    },
    "tag-source-groups": {
        "description": "Tag and source group associations",
        "methods": {
            "create": {
                "http_method": "POST",
                "path": "/tag-source-groups",
                "required_params": ["source_group_id", "tag_id"],
                "optional_params": [],
            },
            "delete": {
                "http_method": "DELETE",
                "path": "/tag-source-groups",
                "required_params": ["source_group_id", "tag_id"],
                "optional_params": [],
            },
        },
    },
}


def show_schema(resource: str | None) -> None:
    if resource is None:
        result = {
            name: {"description": info["description"], "methods": list(info["methods"].keys())}
            for name, info in RESOURCES.items()
        }
        sys.stdout.write(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    else:
        if resource not in RESOURCES:
            sys.stderr.write(
                "Unknown resource: {}\nAvailable: {}\n".format(resource, ", ".join(sorted(RESOURCES.keys())))
            )
            sys.exit(1)
        sys.stdout.write(json.dumps(RESOURCES[resource], indent=2, ensure_ascii=False) + "\n")
