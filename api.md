# Completions

Types:

```python
from qaip.types import FileType, SourceType, CompletionCreateResponse
```

Methods:

- <code title="post /completions">client.completions.<a href="./src/qaip/resources/completions.py">create</a>(\*\*<a href="src/qaip/types/completion_create_params.py">params</a>) -> <a href="./src/qaip/types/completion_create_response.py">CompletionCreateResponse</a></code>

# Contents

Types:

```python
from qaip.types import Content
```

Methods:

- <code title="get /contents/{id}">client.contents.<a href="./src/qaip/resources/contents.py">retrieve</a>(id) -> <a href="./src/qaip/types/content.py">Content</a></code>

# Search

Types:

```python
from qaip.types import SearchQueryResponse
```

Methods:

- <code title="post /search">client.search.<a href="./src/qaip/resources/search.py">query</a>(\*\*<a href="src/qaip/types/search_query_params.py">params</a>) -> <a href="./src/qaip/types/search_query_response.py">SearchQueryResponse</a></code>

# Extract

Types:

```python
from qaip.types import ExtractPerformResponse
```

Methods:

- <code title="post /extract">client.extract.<a href="./src/qaip/resources/extract.py">perform</a>(\*\*<a href="src/qaip/types/extract_perform_params.py">params</a>) -> <a href="./src/qaip/types/extract_perform_response.py">ExtractPerformResponse</a></code>
