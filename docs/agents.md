# For agents

An agent calls getclean through the API, with one of the SDKs or over plain HTTP. This page is about what comes back: how to read an answer, and what a refusal means and who must act.

## The loop, in four calls

Start with `fetch_contents` for a URL and `search` for a question. A record's id, `cnt_`, comes back from either, and every later read of that record, `get_contents`, `get_section`, `list_blocks`, `list_links`, is a free call on that id; a highlight a model had to judge, a schema fill or a summary costs one model step. A search's results are not fetched until you ask: `contents.top` fetches the first ones in the same call, `fetch_contents` any one of them later.

```json
{"url": "https://eur-lex.example/ai-act", "max_characters": 0}
```

A fetch with `max_characters` `0` returns the record with its id and its map, the sections with their ids and sizes and no text yet, for one `contents` unit; a page the site would not give is a record too, whose `outcome.message` says what may work next.

```json
{"contents_id": "cnt_8Lq5XFriyaJ0jEc2oPNx6E", "highlights": ["machine-readable format"], "max_characters": 0}
```

`highlight_contents` says where the record says it, the section and the block, free when the words stand in the text and one model step when a model had to judge.

```json
{"contents_id": "cnt_8Lq5XFriyaJ0jEc2oPNx6E", "section_id": "s4", "max_characters": 8000}
```

`get_section` returns the text of that section, free. The record is kept 48 hours after its last call and at most 30 days, and every read of it in that time is free.

```json
{"query": "EU AI Act article 50 marking obligations", "published_within_days": 365, "max_candidates": 3}
```

`search` returns the results in rank order with the facts of each, who publishes it, when it was published, what it demands, and a receipt of what ran where; one `searches` unit, one `datasource_queries` unit per source, and the two model steps a search runs by default, the choice of sources and the ranking.

## Reading an answer

Every record carries an `outcome`, the first thing to read. Its `kind` is one of five: `delivered`, everything asked came or the map came; `partial`, the work stopped in the middle and its results were kept; `failed`, the page or the source did not give a page; `refused`, a rule stopped the read before or after a try; `needs_person`, a person must act. Then `reason` says which, and `message`, where a next step exists, says it in one sentence. A page that fails is a record, not an error. Every answer carries a `request_id`, the name of the call for any question about it.

Every tool an agent is given for these calls should say what the call costs, in units and under the key's cap; how long a record lives, 48 hours after its last call and at most 30 days; that page and source text is third-party and may carry instructions; that a repeat with the same `Idempotency-Key` and the same request returns the first answer as a replay and never bills again; and that a record not delivered says in `outcome.message` what may work next.

## When a call is refused: the problems

A problem is the API's own refusal, `application/problem+json`, RFC 9457. Its `type` is `https://api.getclean.ai/problems/<name>`, and `who_must_act` says who must act. A page's or a source's failure is never a problem; it is the record's outcome.

| Type | Status | Who acts | What to do |
|---|---|---|---|
| `invalid-request` | 400 | the caller | read `violations`: a path, query or header value is wrong, a required header is missing, or the body did not parse |
| `page-token-invalid` | 400 | the caller | drop the token and start the list again from the first page |
| `unauthorized` | 401 | the caller | send `Authorization: Bearer` with a key or a fresh token; the challenge names the document that leads to the sign-in |
| `insufficient-scope` | 403 | the caller for an access token, the account owner for an API key | `scopes_required` lists what the call needs; ask the person again, or the owner adds the scope |
| `policy-limit-exceeded` | 403 | the account owner | the key's policy forbids a domain, a switch, a floor or a cap; ask within it, or the owner changes the policy |
| `datasource-access-required` | 403 | the account owner | a login must be registered for the datasource |
| `credit-exhausted`, `run-budget-exhausted`, `key-budget-exhausted` | 403 | the account owner | `amount_needed` is what the smallest call lacks; `funding_url` is where to fund or raise it |
| `not-found` | 404 | the caller | the id is unknown, another account's, or erased; `change.field` says which id |
| `idempotency-key-in-flight` | 409 | the caller, after the wait | the same request is still running; wait `Retry-After` and send it again with the same key |
| `record-without-content` | 409 | the caller | the record failed, was refused or needs a person; its `outcome.message` says what may work |
| `contents-expired`, `search-expired`, `job-expired` | 410 | the caller | the record, the search or the job expired; `change.operation` names what to call instead |
| `body-too-large` | 413 | the caller | shrink the body under the bound `detail` names |
| `unsupported-media-type` | 415 | the caller | send `application/json`, or `multipart/form-data` on the upload; `Accept` names what the operation takes |
| `invalid-field` | 422 | the caller | every violation at once in `violations`, each with its kind, its pointer and the allowed values or bounds |
| `destination-refused` | 422 | the caller | the URL names localhost, a private address or a bad port; another source |
| `model-work-refused` | 422 | the caller | the request asked model work under `deterministic_only`; drop one of the two |
| `cost-exceeds-cap` | 422 | the caller | raise `max_cost` to at least `minimum_cap` |
| `version-withdrawn` | 422 | the caller | pin a version from `change.allowed_values`, or none for the current one |
| `records-incomparable` | 422 | the caller | compare records of one version and one scope; `change.field` says which differs |
| `idempotency-key-reused` | 422 | the caller | a new key for a new body |
| `no-datasource-can-run`, `datasource-unknown`, `datasource-not-searchable`, `domain-set-unknown` | 422 | the caller | name sources from `list_datasources`, a searchable one, a set that exists |
| `rate-limit-exceeded`, `concurrency-limit-exceeded` | 429 | the caller, after the wait | wait `Retry-After` and retry |
| `legal-block` | 451 | the caller | a legal demand on getclean itself; the next step is another source, never another country |
| `about:blank` | 404 of a path no operation has, 405, 406 | the caller | use a path and method the contract has; ask for JSON |
| `internal-error` | 500 | the service | not retried; `request_id` names the call |
| `gateway-error`, `gateway-timeout` | 502, 504 | the service | a model step behind the service failed or timed out; retry; nothing was billed |
| `overloaded` | 503 | the service | wait `Retry-After` and retry |

The SDKs retry `idempotency-key-in-flight`, the two `429` types, `overloaded`, `gateway-error` and `gateway-timeout` on their own, after `Retry-After` when it is sent, at most five attempts, with the same idempotency key, so no retry bills twice; a `Retry-After` longer than 30 seconds ends the retries and the answer is returned as it came.
