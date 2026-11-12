# highlight_contents

Find words or questions in a record you already have and mark where they stand, without fetching again. You get each place with its section and block ids, and, when you ask for text, the sections that hold them, marked. A string found verbatim is free; one a model has to judge costs one model step, once per call however many strings needed it.

**What it costs.** The key needs `contents:read`, and `contents:model` unless `deterministic_only` is true, since a string may need a model. Free when every string was found verbatim; 1 `model_steps` when any string had to be judged, once per call. The answer is `200` with `ContentsHighlights`; the call moves the record's `expires_at` 48 hours ahead.

`POST /v1/contents/{contents_id}:highlight`

## One string found verbatim, one judged and not found, the step billed once

The request:

```sh
curl https://api.getclean.ai/v1/contents/cnt_3Fk9abaUhNX7t2eKkgfd3e:highlight \
  -H "Authorization: Bearer $GETCLEAN_API_KEY" \
  -H "Idempotency-Key: $(uuidgen)" \
  -H "Content-Type: application/json" \
  -d '{"highlights": ["Revenue rose 12%", "dividend policy"], "max_characters": 0}'
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_01JIuousU3aZV7sHAB3vEy
Content-Type: application/json

{
  "contents_id": "cnt_3Fk9abaUhNX7t2eKkgfd3e",
  "final_url": "https://example.com/q3",
  "fetched_at": "2026-11-04T08:40:12Z",
  "fingerprint": "sha-256=:kw4QGoYGxOYpZ0EZGL+nxMfFUXfrxcp+P0M4EOrEiH4=:",
  "scope": "main",
  "version": "1.0.0",
  "configuration": "cfg-2026-11",
  "expires_at": "2026-11-06T08:40:12Z",
  "highlights": [
    {
      "id": "h1",
      "query_index": 0,
      "text": "Revenue rose 12%",
      "basis": "exact",
      "section_id": "s1",
      "block_id": "b3"
    }
  ],
  "formats": [],
  "truncated": false,
  "execution": {
    "version": "1.0.0",
    "configuration": "cfg-2026-11",
    "models": [
      {
        "step": "highlights",
        "version": "hl-2026-10"
      }
    ],
    "elapsed_seconds": 1.4
  },
  "cost": {
    "ceiling": {
      "amount": "0.0020",
      "currency": "USD"
    },
    "actual": {
      "amount": "0.0020",
      "currency": "USD"
    },
    "units": {
      "model_steps": 1
    },
    "replayed": false
  },
  "notices": [
    {
      "code": "highlight_not_found",
      "message": "No block bears on the string.",
      "field": "highlights",
      "pointer": "/highlights/1"
    }
  ],
  "request_id": "req_01JIuousU3aZV7sHAB3vEy"
}
```

## A highlight asked of a record that has no content

The answer:

```http
HTTP/1.1 409 Conflict
Request-Id: req_5kQ2mZ8vT4wR9nB1cX7pL0
Content-Type: application/problem+json

{
  "type": "https://api.getclean.ai/problems/record-without-content",
  "title": "The record has no content",
  "status": 409,
  "detail": "The record named failed, so it has no text to highlight; fetch the page again and highlight the new record.",
  "instance": "https://api.getclean.ai/requests/req_5kQ2mZ8vT4wR9nB1cX7pL0",
  "request_id": "req_5kQ2mZ8vT4wR9nB1cX7pL0",
  "who_must_act": "caller",
  "retryable": false,
  "change": {
    "operation": "fetch_contents",
    "field": "url"
  }
}
```

Every rule of `highlight_contents`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
