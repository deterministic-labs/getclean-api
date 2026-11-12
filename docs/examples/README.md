# Examples, one page per operation

Each page shows what the operation does and what it costs, in the contract's own words, then every example the contract carries for it: the request as a curl command and the answer with its status and headers. The pages are written by `tools/example_pages.py` from `spec/openapi.yaml` and change only when the contract does.

| Operation | Call | What it does |
|---|---|---|
| [`fetch_contents`](fetch_contents.md) | `POST /v1/contents` | Fetch a web page or a document at a URL. |
| [`list_contents`](list_contents.md) | `GET /v1/contents` | List the records the account keeps, newest first, free. |
| [`get_contents`](get_contents.md) | `GET /v1/contents/{contents_id}` | Read a record you already have, free. |
| [`delete_contents`](delete_contents.md) | `DELETE /v1/contents/{contents_id}` | Erase a record before it expires: the record, its screenshot, its raw HTML, its document images, its recognized page images and its stored replays. |
| [`get_section`](get_section.md) | `GET /v1/contents/{contents_id}/sections/{section_id}` | Read one section of a record, free. |
| [`list_blocks`](list_blocks.md) | `GET /v1/contents/{contents_id}/blocks` | List the blocks of a record, free. |
| [`list_links`](list_links.md) | `GET /v1/contents/{contents_id}/links` | List the links of a record, free. |
| [`upload_contents`](upload_contents.md) | `POST /v1/contents:upload` | Read a document you hold, or one at a URL that needs more time than a fetch gives. |
| [`list_jobs`](list_jobs.md) | `GET /v1/jobs` | List the account's jobs, newest first, free. |
| [`get_job`](get_job.md) | `GET /v1/jobs/{job_id}` | Read a job, or wait for it to finish, free. |
| [`cancel_job`](cancel_job.md) | `POST /v1/jobs/{job_id}:cancel` | Ask a job to stop, free. |
| [`fetch_contents_batch`](fetch_contents_batch.md) | `POST /v1/contents:batch` | Fetch 1 to 20 pages or documents at their URLs in one call. |
| [`highlight_contents`](highlight_contents.md) | `POST /v1/contents/{contents_id}:highlight` | Find words or questions in a record you already have and mark where they stand, without fetching again. |
| [`fill_schema`](fill_schema.md) | `POST /v1/contents/{contents_id}:fill` | Fill your JSON Schema from a record you already have. |
| [`summarize_contents`](summarize_contents.md) | `POST /v1/contents/{contents_id}:summarize` | Have a model write a summary of a record you already have, at most 1,500 characters in the content's language, from the copy getclean keeps. |
| [`compare_contents`](compare_contents.md) | `POST /v1/contents/{contents_id}:compare` | Compare a record you already have with a baseline, block by block and cell by cell, without a model, free. |
| [`get_limits`](get_limits.md) | `GET /v1/limits` | Read your key's limits and your account's money in one answer, free, before a batch or any call that must fit a budget. |
| [`search`](search.md) | `POST /v1/search` | Search up to ten datasources with one question, in up to twenty wordings, and get one ranked list of results with the facts of each and a receipt of what ran where, before any page is read. |
| [`get_search`](get_search.md) | `GET /v1/search/{search_id}` | Read a search you already have, free: the first page as it was answered, and behind it the full list the search stored, including the results it dropped and why. |
| [`search_batch`](search_batch.md) | `POST /v1/search:batch` | Run 1 to 20 searches in one call, one record each. |
| [`list_datasources`](list_datasources.md) | `GET /v1/datasources` | List the places getclean can search, free; the answer may be cached for an hour. |
| [`get_datasource`](get_datasource.md) | `GET /v1/datasources/{datasource_id}` | Read one entry of the catalog whole, free; the answer may be cached for an hour. |
