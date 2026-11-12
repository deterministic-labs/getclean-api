# getclean-api

The getclean API contract: the data layer for research agents, in one OpenAPI 3.1 file.

getclean is the data layer for research agents. Give it a URL or a document and it returns the main content exactly as the source has it, every heading, table and word in place, the same output every time, and keeps the record so every later question about that source is answered from the same copy. Give it a question and it returns one ranked list of results across the web and specialist sources, with a receipt of what was searched where. Every record says first what happened, and every billed call what it cost.

## What is here

| Path | What it is |
|---|---|
| `spec/openapi.yaml` | the contract, OpenAPI 3.1, one file: 22 operations and 121 schemas, every example complete |
| `spec/SDK-NOTES.md` | what every official SDK does beyond the contract: the client, the idempotency key, the retries, the timeouts, the pagers, the upload; `spec/SDK-NOTES.yml` carries the environment, the per-request headers, the type of the request a search's answer carries, the pagers and the retries as data |
| `docs/` | `auth.md`, how a call is authenticated and where a key comes from; `agents.md`, how an agent reads an answer and every problem with who must act; `examples/`, one page per operation with its requests and answers, written from the contract's own examples |
| `RELEASE.md` | how versions are numbered and what a release promises; `CHANGELOG.md`, every change of the contract by date |

The official SDKs for Python and TypeScript follow this contract exactly, each in its own repository under `github.com/deterministic-labs`.

## Reading the contract

Three rules make the rest readable. Every record carries an `outcome`, the first thing to read: its `kind` is one of `delivered`, `partial`, `failed`, `refused` and `needs_person`, then `reason`, and `message` where a next step exists. A page or a source that fails is an outcome inside a `201` record, never an HTTP error, so a client reads what happened before anything else. An HTTP error is an RFC 9457 problem whose `type` is `https://api.getclean.ai/problems/<name>`, with `who_must_act`, `retryable` and, where the fix is data, `change`.

## What you can rely on

Every example in the contract validates against its schema. A member keeps its name in every operation and every SDK. The example pages under `docs/examples/` are written from the contract and equal it.
