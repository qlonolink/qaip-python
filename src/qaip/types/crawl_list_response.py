# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .crawl import Crawl
from .._models import BaseModel
from .shared.pagination import Pagination

__all__ = ["CrawlListResponse"]


class CrawlListResponse(BaseModel):
    crawls: List[Crawl]

    pagination: Pagination
