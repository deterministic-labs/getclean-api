# Authentication

Every call to `https://api.getclean.ai` carries one header:

```http
Authorization: Bearer <key>
```

The bearer value is one of two things, and the API treats them alike:

- an API key, made at `https://app.getclean.ai`, which belongs to an account and carries the scopes its owner gave it;
- an access token issued by `https://auth.getclean.ai/realms/getclean` to a person and the program acting for them, whose scopes are what the person approved on the consent page, never more.

Either one stands for one account, with its scopes, its cap on one call, its budgets, its policy and its default run. A credential in the query string is ignored.

## A first call

```sh
curl https://api.getclean.ai/v1/contents \
  -H "Authorization: Bearer $GETCLEAN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/q3"}'
```

The SDKs read the key from `GETCLEAN_API_KEY` when none is given, so `GetClean()` in Python and `new GetClean({})` in TypeScript are enough on a machine that has it. A function that returns a token is taken in place of the key; the SDK calls it once per call, before the first attempt, and refreshes nothing itself.

## Scopes

Every key carries an explicit list of scopes, deny by default. Each operation names the scope it needs in its description in the contract. A scope that depends on the request, `contents:model`, is decided from the request before any work, so a missing scope is a `403` before any `422`.

| Scope | What it allows |
|---|---|
| `contents:fetch` | `fetch_contents`, `upload_contents`, `fetch_contents_batch` |
| `contents:read` | `get_contents`, `get_section`, `list_blocks`, `list_links`, `compare_contents`, `list_contents`; `highlight_contents` under `deterministic_only` |
| `contents:model` | `fill_schema`, `summarize_contents`; `highlight_contents` unless `deterministic_only`; a fetch that sends `json_schema`, `summary` or `highlights` without `deterministic_only` |
| `contents:delete` | `delete_contents` |
| `jobs:read` | `get_job`, `list_jobs` |
| `jobs:cancel` | `cancel_job` |
| `limits:read` | `get_limits` |
| `search:run` | `search`, `search_batch`, the fetches made inside a search included |
| `search:read` | `get_search`, `list_datasources`, `get_datasource` |

## When the credential is missing or rejected

A call with no usable credential is answered `401`. The challenge names the document that leads to the sign-in:

```http
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer realm="getclean", resource_metadata="https://api.getclean.ai/.well-known/oauth-protected-resource"
Request-Id: req_01Ar9JusXFIyNhFJ0zEcBe
Content-Type: application/problem+json

{
  "type": "https://api.getclean.ai/problems/unauthorized",
  "title": "The key is missing or rejected",
  "status": 401,
  "detail": "No credential was sent: send Authorization: Bearer with an API key from https://app.getclean.ai, or sign in as https://auth.getclean.ai/auth.md describes.",
  "instance": "https://api.getclean.ai/requests/req_01Ar9JusXFIyNhFJ0zEcBe",
  "request_id": "req_01Ar9JusXFIyNhFJ0zEcBe",
  "who_must_act": "caller",
  "retryable": false
}
```

A credential that was sent and rejected gets the same challenge with `error="invalid_token"` added, and the detail says to refresh the token, sign in again, or use another key. The credential itself is never echoed.

A credential short of a scope is answered `403`:

```http
HTTP/1.1 403 Forbidden
WWW-Authenticate: Bearer realm="getclean", error="insufficient_scope", resource_metadata="https://api.getclean.ai/.well-known/oauth-protected-resource", scope="contents:model"
```

The body is a problem of type `insufficient-scope` whose `scopes_required` lists every scope the call needs. For an API key the account owner adds the scope at `https://app.getclean.ai`; for an access token the person may be asked again.

## Signing in as a person

The sign-in steps for a person, and for a program acting for one, are at `https://auth.getclean.ai/auth.md`. The document the `401` names, `https://api.getclean.ai/.well-known/oauth-protected-resource`, is served to anyone: it names the API, the one issuer, the nine scopes above, and that the credential travels in the header. A program that arrives with nothing follows it to the issuer and its device sign-in.

## Transport

HTTPS only, TLS 1.2 or 1.3. A plain HTTP request is answered `400 invalid-request` over that connection, with the HTTPS URL in `detail`, and is never redirected, so a key and a body are never resent in the clear. The API sends no CORS headers: its credentials are secrets held by servers and programs, so a key placed in a web page fails at once.
