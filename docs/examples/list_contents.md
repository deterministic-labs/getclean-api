# list_contents

List the records the account keeps, newest first, free. Each item is a `ContentsCompact`: the record's id, outcome, source and dates, with no text, no map, no model work and no cost, and its `execution` as stored.

Use it to see which pages the account already has before fetching one again; `get_contents` reads one record whole. Every filter you send must match. The list does not move any record's `expires_at`.

**What it costs.** The key needs `contents:read`. The call is free. The answer is `200` with `ContentsPage`.

`GET /v1/contents`

## A list with one record, about one site

The request:

```sh
curl https://api.getclean.ai/v1/contents \
  -H "Authorization: Bearer $GETCLEAN_API_KEY"
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_01Sof5z2SAa45Wc4HZYpfe
Content-Type: application/json

{
  "contents": [
    {
      "id": "cnt_3Fk9abaUhNX7t2eKkgfd3e",
      "outcome": {
        "kind": "delivered",
        "reason": "whole"
      },
      "notices": [],
      "fetched_at": "2026-11-04T08:40:12Z",
      "fingerprint": "sha-256=:kw4QGoYGxOYpZ0EZGL+nxMfFUXfrxcp+P0M4EOrEiH4=:",
      "scope": "main",
      "record_scope": "main",
      "formats": [],
      "truncated": false,
      "counts": {
        "characters": 6210,
        "blocks": {
          "heading": 4,
          "text": 22,
          "table": 1
        },
        "links": {
          "page": 9
        }
      },
      "source": {
        "url": "https://example.com/q3",
        "final_url": "https://example.com/q3",
        "title": "Quarterly results",
        "published_date": "2026-10-28"
      },
      "execution": {
        "version": "1.0.0",
        "configuration": "cfg-2026-11",
        "models": [
          {
            "step": "highlights",
            "version": "hl-2026-10"
          },
          {
            "step": "summary",
            "version": "sum-2026-10"
          }
        ],
        "elapsed_seconds": 7.1
      },
      "retention": "hold",
      "run_id": "run_default",
      "expires_at": "2026-11-06T08:40:12Z"
    }
  ],
  "notices": [],
  "request_id": "req_01Sof5z2SAa45Wc4HZYpfe"
}
```

Every rule of `list_contents`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
