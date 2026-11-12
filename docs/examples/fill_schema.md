# fill_schema

Fill your JSON Schema from a record you already have. You get a value only where the record states it, never a plausible one, with the place and the cited words for each property, and `empty`, `absent` or `unread` where the record says nothing. It is the same step as `fetch_contents`'s `json_schema`, run on the copy getclean keeps.

**What it costs.** The key needs `contents:model`. The price is 1 `model_steps`. The answer is `200` with `SchemaFill`; the call moves the record's `expires_at` 48 hours ahead.

`POST /v1/contents/{contents_id}:fill`

## One property found with its cited words, one absent from the record

The request:

```sh
curl https://api.getclean.ai/v1/contents/cnt_3Fk9abaUhNX7t2eKkgfd3e:fill \
  -H "Authorization: Bearer $GETCLEAN_API_KEY" \
  -H "Idempotency-Key: $(uuidgen)" \
  -H "Content-Type: application/json" \
  -d '{"json_schema": {"type": "object", "properties": {"revenue_growth": {"type": "string"}, "dividend": {"type": "string"}}}}'
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_01Jkf30AHpVn2m9UKIRfWE
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
  "schema_values": {
    "revenue_growth": "12%"
  },
  "schema_statuses": {
    "/revenue_growth": {
      "status": "found",
      "text": "Revenue rose 12% to EUR 4.1 bn",
      "section_id": "s1",
      "block_id": "b3"
    },
    "/dividend": {
      "status": "absent"
    }
  },
  "execution": {
    "version": "1.0.0",
    "configuration": "cfg-2026-11",
    "models": [
      {
        "step": "json_schema",
        "version": "fill-2026-10"
      }
    ],
    "elapsed_seconds": 2.3
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
  "request_id": "req_01Jkf30AHpVn2m9UKIRfWE"
}
```

## A schema fill whose model step gave a bad answer

The answer:

```http
HTTP/1.1 502 Bad Gateway
Request-Id: req_nPdXW8ob1JmugUbhiwrZTZ
Content-Type: application/problem+json

{
  "type": "https://api.getclean.ai/problems/gateway-error",
  "title": "A step behind the service failed",
  "status": 502,
  "detail": "The model step that fills the schema gave a bad answer; nothing was billed, and a retry may work.",
  "instance": "https://api.getclean.ai/requests/req_nPdXW8ob1JmugUbhiwrZTZ",
  "request_id": "req_nPdXW8ob1JmugUbhiwrZTZ",
  "who_must_act": "service",
  "retryable": true
}
```

## A schema fill whose model step passed its time bound

The answer:

```http
HTTP/1.1 504 Gateway Timeout
Request-Id: req_uARLFe4a7MjE3pzwKAToD8
Content-Type: application/problem+json

{
  "type": "https://api.getclean.ai/problems/gateway-timeout",
  "title": "A step behind the service timed out",
  "status": 504,
  "detail": "The model step that fills the schema passed its 20-second bound; nothing was billed, and a retry may work.",
  "instance": "https://api.getclean.ai/requests/req_uARLFe4a7MjE3pzwKAToD8",
  "request_id": "req_uARLFe4a7MjE3pzwKAToD8",
  "who_must_act": "service",
  "retryable": true
}
```

Every rule of `fill_schema`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
