# summarize_contents

Have a model write a summary of a record you already have, at most 1,500 characters in the content's language, from the copy getclean keeps. It is the same step as `fetch_contents`'s `summary`. Use `highlight_contents` to find words and `fill_schema` to fill fields.

**What it costs.** The key needs `contents:model`. The price is 1 `model_steps`. The answer is `200` with `ContentsSummary`; the call moves the record's `expires_at` 48 hours ahead.

`POST /v1/contents/{contents_id}:summarize`

## A summary written from a record you already have

The request:

```sh
curl https://api.getclean.ai/v1/contents/cnt_3Fk9abaUhNX7t2eKkgfd3e:summarize \
  -H "Authorization: Bearer $GETCLEAN_API_KEY" \
  -H "Idempotency-Key: $(uuidgen)" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_01Js1UX1k8Axr2vRanQO5u
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
  "summary": "Revenue rose 12% in the quarter, driven by volume in Europe; margin expanded on lower input costs and mix; guidance was raised.",
  "execution": {
    "version": "1.0.0",
    "configuration": "cfg-2026-11",
    "models": [
      {
        "step": "summary",
        "version": "sum-2026-10"
      }
    ],
    "elapsed_seconds": 1.9
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
  "notices": [],
  "request_id": "req_01Js1UX1k8Axr2vRanQO5u"
}
```

Every rule of `summarize_contents`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
