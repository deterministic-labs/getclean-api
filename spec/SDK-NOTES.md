# What every official SDK does beyond the contract

The contract says what the API takes and what it returns. These notes say what the official SDKs, Python and TypeScript, do around it, so that the same call behaves the same way in both. The file beside this page, `SDK-NOTES.yml`, carries the environment, the per-request headers, the echoed request type, the pagers and the retries as data.

## The client

- One client class, `GetClean`. It is built with `api_key`: an API key, an access token, or a function that returns one. The function is called once per call before its first attempt; a later page of a pager is a new call and may call it again. When no credential is given, `GETCLEAN_API_KEY` is read; when that is empty or unset too, construction fails with the SDK's own configuration error, before any request leaves.
- One host, `https://api.getclean.ai`. `GETCLEAN_BASE_URL`, when set and not empty, names another; a `base_url` argument wins over both.
- Every request carries a `User-Agent` of the package's name and version and no other identifying header.
- `traceparent` is sent per request through the request options and is never set on the client.
- A client closes its connection pool: a context manager and a `close` method in Python.

## The idempotency key

Every call that may bill carries `Idempotency-Key`: it is required on `upload_contents`, `fetch_contents_batch` and `search_batch`, and optional on `fetch_contents`, `search`, `highlight_contents`, `fill_schema` and `summarize_contents`. When you give none, the SDK fills one fresh key for the call and reuses it on every retry of that call, so a retry is a replay and never a second charge. The key stands on every error the call raises, as `idempotency_key`, or `idempotencyKey` in TypeScript, so your own repeat after a timeout or a lost connection replays too. `compare_contents` and `cancel_job` bill nothing and take no key.

## Retries

- Retried: `429`, `502`, `503`, `504`, and a `409` whose problem type is `idempotency-key-in-flight`. No other answer is retried, never a `500` and never another `4xx`; a connection that fails before any answer is retried where the language's runtime does so by itself.
- At most 5 attempts in one count across all of these, with a backoff that starts at 1 second and doubles to a ceiling of 30 seconds, with jitter. A `Retry-After` within the ceiling is honored as the server sent it. A `Retry-After` longer than the ceiling ends the retries at once, and the answer is returned as it arrived with `retry_after_seconds` in its body, so you decide whether to wait.
- The client's retry count option governs the one count.

## Timeouts

- The timeout is per attempt, not per call: the operation's own bound from `get_limits` plus 10 seconds, `bounds.<family>.call_seconds.max` for a call that may bill and `bounds.<family>.batch_seconds.max` for the two batches. The limits are read once before the first call that may bill, and again only after a failure other than a `401` or a `403`; until read, 120 seconds. The SDK's timeout applies only where neither the call's options nor the client's construction set one; a failed reading of the limits never fails your call.
- In Python the figure bounds each phase of an attempt, connecting, writing, reading and waiting for the pool.

## Pagers

- Seven operations page with `page_token` in the request and `next_page_token` in the answer: `list_blocks`, `list_links`, `compare_contents` with the token in the request body, `list_jobs`, `list_contents`, `get_search` and `list_datasources`. `next_page_token` is absent on the last page and never null or empty; a page that carries one holds at least one item.
- `list_jobs` and `list_contents` grow while they page and may repeat an item; the SDK's pager drops repeats by `id`.
- `get_section` is not a pager. `iter_section` pages its cut text, taking what `get_section` takes, `page_token` included, and yields each page in turn.

## The upload

- `document` is a path, bytes, a readable stream or the language's own file form; in Python a `str` is always the path of a file. A path means the file whether or not `wait` is set. A stream is read into memory once before the first attempt, so every attempt sends the same bytes under the same key.
- `wait`, off by default. With `wait` on, the SDK polls `get_job` with `wait_seconds` 60 until the job is final or until the job bound, `bounds.contents.job_seconds.max`, plus one minute has passed, 30 minutes plus one until the limits are read. It then reads the record with `get_contents` under the upload's own `max_characters`, `formats` and `block_kinds`, and returns the record with its cost on a `201`, or the record as read and the final job on a `202`. Each poll runs under its own wait plus the margin and carries your headers and abort signal and nothing else of the upload. A poll or the read that fails with a `429`, a `5xx` or a lost connection is tried again within the bound, and no wait begins that would end past it; a `4xx` ends the helper as it arrived with the last job seen on the error. A job that failed with no record raises the typed error of its problem's status with the job on it. A cancel with no record raises `JobCanceled`, which carries the job; in TypeScript it extends `GetCleanError`, so one catch takes every error of the SDK.
- In Python the type of `document` is exported as `DocumentInput` from the package root, so you can annotate with it.

## Errors and headers

- Every `4xx` and `5xx` is a typed error per status, carrying the `Problem` the API sent; a status the contract does not declare raises the base error. The message opens with the problem's title and detail.
- No SDK types the response headers. Every value you act on is repeated in the body: `request_id`, `retry_after_seconds`, the record's id that `Location` also names. The rate limit figures are returned by `get_limits`.

## Types

- Requests are flat: every field at the top level, a scalar, a list of scalars, a map of strings or one of the named objects. The request echoed in a search's answer is typed `AppliedSearchRequest`.
- A closed set used by one member is an enum of its own, named `<Schema><Member>` in Python and nested under its type in TypeScript, as `Candidate.DroppedReason`; the eleven closed sets that two members share are named components. A set the contract calls open is a string.
- Null and absent are kept apart where the language can tell them apart.
