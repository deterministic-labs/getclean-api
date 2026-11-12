# fetch_contents

Fetch a web page or a document at a URL. You get its main content with the structure intact, in the formats you ask for, the map of its sections, the facts of the source, a fingerprint and the price, as one record that is kept for later reads.

The record is kept 48 hours after its last call and at most 30 days from its making, and every later question about it, through `get_contents`, `get_section`, `list_blocks` and `list_links`, is answered from the same copy, free. Use `upload_contents` for a file you hold, or for a long document that must run as a job; use `search` when you have a question and no URL yet; use `get_contents` to read a record you already have.

**What it costs.** The key needs `contents:fetch`, plus `contents:model` when you send `json_schema`, set `summary` or send `highlights` without `deterministic_only`; getclean decides this from the request before any work, so a missing scope is `403` before any `422`. The price is 1 `contents`, plus `document_pages` and `recognized_pages` when the URL serves a document, plus `model_steps` for each model field that ran, plus `screenshots` when one was made. An `unchanged` answer bills the same 1 `contents`. A fetch that failed, was refused or needs a person bills nothing.

`POST /v1/contents`

## A page fetched with two highlights and a summary

The request:

```sh
curl https://api.getclean.ai/v1/contents \
  -H "Authorization: Bearer $GETCLEAN_API_KEY" \
  -H "Idempotency-Key: $(uuidgen)" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/q3", "highlights": ["Revenue rose 12%", "what drove the margin"], "summary": true}'
```

The answer:

```http
HTTP/1.1 201 Created
Location: https://api.getclean.ai/v1/contents/cnt_3Fk9abaUhNX7t2eKkgfd3e
Request-Id: req_01JzsALAAlsNsdoVz1EElr
Content-Type: application/json

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
  "formats": [
    "markdown"
  ],
  "truncated": false,
  "markdown": "# Quarterly results\n\n<mark id=\"h1\">Revenue rose 12%</mark> to … <mark id=\"h2\">Margin expanded on lower input costs and mix.</mark> …",
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
  "highlights": [
    {
      "id": "h1",
      "query_index": 0,
      "text": "Revenue rose 12%",
      "basis": "exact",
      "section_id": "s1",
      "block_id": "b3"
    },
    {
      "id": "h2",
      "query_index": 1,
      "text": "Margin expanded on lower input costs and mix.",
      "basis": "judged",
      "section_id": "s2",
      "block_id": "b9"
    }
  ],
  "summary": "Revenue rose 12% in the quarter, driven by volume in Europe; margin expanded on lower input costs and mix; guidance was raised.",
  "hidden_text": [],
  "left_out": [
    {
      "kind": "navigation",
      "characters": 1480
    }
  ],
  "source": {
    "url": "https://example.com/q3",
    "final_url": "https://example.com/q3",
    "redirects": [],
    "status_code": 200,
    "media_type": "text/html",
    "carrier": "web",
    "access_kind": "open",
    "title": "Quarterly results",
    "authors": [],
    "published_date": "2026-10-28",
    "published_date_precision": "day",
    "published_date_basis": "structured_data",
    "modified_date": null,
    "publisher": "Example Corp",
    "canonical_url": null,
    "language": "en",
    "language_versions": [],
    "profile": {
      "kind": "company",
      "role": "primary",
      "independence": "unknown",
      "review": {
        "kind": "none",
        "by": null
      }
    },
    "robots": "allowed",
    "declared_terms": [],
    "structured_data": [
      {
        "@type": "NewsArticle",
        "headline": "Quarterly results"
      }
    ],
    "origins": [
      {
        "origin": "https://cdn.example.com",
        "kind": "script"
      }
    ],
    "visitor": {
      "country": "DE",
      "language": "de-DE,de;q=0.9",
      "network": "datacenter"
    }
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
  "cost": {
    "ceiling": {
      "amount": "0.0500",
      "currency": "USD"
    },
    "actual": {
      "amount": "0.0090",
      "currency": "USD"
    },
    "units": {
      "contents": 1,
      "model_steps": 2
    },
    "replayed": false
  },
  "retention": "hold",
  "run_id": "run_default",
  "expires_at": "2026-11-06T08:40:12Z",
  "request_id": "req_01JzsALAAlsNsdoVz1EElr"
}
```

## A failed fetch, a bot challenge where the page should be

The request:

```sh
curl https://api.getclean.ai/v1/contents \
  -H "Authorization: Bearer $GETCLEAN_API_KEY" \
  -H "Idempotency-Key: $(uuidgen)" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://shop.example/offer"}'
```

The answer:

```http
HTTP/1.1 201 Created
Location: https://api.getclean.ai/v1/contents/cnt_7Qp2cdxxK32qkfIDrqRUE2
Request-Id: req_01KXuaBXEPybVuXmnCI9Bl
Content-Type: application/json

{
  "id": "cnt_7Qp2cdxxK32qkfIDrqRUE2",
  "outcome": {
    "kind": "failed",
    "reason": "challenge_served",
    "message": "A bot challenge stood where the page should be; a retry later may work on sites that do not challenge every new visitor, or a person opens the URL and uploads the saved page with captured_url."
  },
  "notices": [],
  "fetched_at": "2026-11-04T08:41:03Z",
  "truncated": false,
  "source": {
    "url": "https://shop.example/offer",
    "final_url": "https://shop.example/offer",
    "redirects": [],
    "status_code": 403,
    "media_type": "text/html",
    "carrier": "web",
    "access_kind": "open",
    "title": "Just a moment",
    "authors": [],
    "published_date": null,
    "modified_date": null,
    "publisher": null,
    "canonical_url": null,
    "language": "en",
    "language_versions": [],
    "profile": {
      "kind": "marketplace",
      "role": "primary",
      "independence": "unknown",
      "review": {
        "kind": "none",
        "by": null
      }
    },
    "robots": "allowed",
    "declared_terms": [],
    "structured_data": [],
    "origins": [
      {
        "origin": "https://challenges.example",
        "kind": "script"
      }
    ],
    "visitor": {
      "country": "DE",
      "language": "de-DE,de;q=0.9",
      "network": "datacenter"
    }
  },
  "execution": {
    "version": "1.0.0",
    "configuration": "cfg-2026-11",
    "models": [],
    "elapsed_seconds": 2.4
  },
  "cost": {
    "ceiling": {
      "amount": "0.0500",
      "currency": "USD"
    },
    "actual": {
      "amount": "0.0000",
      "currency": "USD"
    },
    "units": {},
    "replayed": false
  },
  "retention": "hold",
  "run_id": "run_default",
  "expires_at": "2026-11-06T08:41:03Z",
  "request_id": "req_01KXuaBXEPybVuXmnCI9Bl"
}
```

## A fetch repeated while its first call still runs

The answer:

```http
HTTP/1.1 409 Conflict
Request-Id: req_7nXDWTR71LO0QsrpbfL67K
Content-Type: application/problem+json

{
  "type": "https://api.getclean.ai/problems/idempotency-key-in-flight",
  "title": "The same request is still running",
  "status": 409,
  "detail": "A fetch with this Idempotency-Key is still running; ask again with the same key in 2 seconds.",
  "instance": "https://api.getclean.ai/requests/req_7nXDWTR71LO0QsrpbfL67K",
  "request_id": "req_7nXDWTR71LO0QsrpbfL67K",
  "who_must_act": "caller",
  "retryable": true,
  "retry_after_seconds": 2
}
```

## A formats value outside its set

The answer:

```http
HTTP/1.1 422 Unprocessable Content
Request-Id: req_01JSUEOJ23EQgBxGjfSpcD
Content-Type: application/problem+json

{
  "type": "https://api.getclean.ai/problems/invalid-field",
  "title": "A field is invalid",
  "status": 422,
  "detail": "formats holds a value outside its set.",
  "instance": "https://api.getclean.ai/requests/req_01JSUEOJ23EQgBxGjfSpcD",
  "request_id": "req_01JSUEOJ23EQgBxGjfSpcD",
  "who_must_act": "caller",
  "retryable": false,
  "violations": [
    {
      "kind": "not_allowed",
      "place": "body",
      "pointer": "/formats/0",
      "field": "formats",
      "message": "The value at the pointer is not a value of formats.",
      "allowed_values": [
        "markdown",
        "html",
        "doclang",
        "json",
        "links",
        "screenshot",
        "raw_html"
      ]
    }
  ]
}
```

## A key past its requests for the minute

The answer:

```http
HTTP/1.1 429 Too Many Requests
Request-Id: req_yTfAxBwyT38z4lXC1wqHLn
Content-Type: application/problem+json

{
  "type": "https://api.getclean.ai/problems/rate-limit-exceeded",
  "title": "The rate limit is exceeded",
  "status": 429,
  "detail": "The key has made its 600 requests of this minute; the window resets in 17 seconds.",
  "instance": "https://api.getclean.ai/requests/req_yTfAxBwyT38z4lXC1wqHLn",
  "request_id": "req_yTfAxBwyT38z4lXC1wqHLn",
  "who_must_act": "caller",
  "retryable": true,
  "retry_after_seconds": 17
}
```

## A key with every allowed call already in flight

The answer:

```http
HTTP/1.1 429 Too Many Requests
Request-Id: req_vTKyQfD6c9TGtRlIVKiLCb
Content-Type: application/problem+json

{
  "type": "https://api.getclean.ai/problems/concurrency-limit-exceeded",
  "title": "Too many calls are in flight",
  "status": 429,
  "detail": "The key has 20 calls in flight, the most its concurrency policy allows; ask again in 1 second.",
  "instance": "https://api.getclean.ai/requests/req_vTKyQfD6c9TGtRlIVKiLCb",
  "request_id": "req_vTKyQfD6c9TGtRlIVKiLCb",
  "who_must_act": "caller",
  "retryable": true,
  "retry_after_seconds": 1
}
```

## A fetch that could not start within the queue bound

The answer:

```http
HTTP/1.1 503 Service Unavailable
Request-Id: req_dVKh740AKEi99ibtCu8L6w
Content-Type: application/problem+json

{
  "type": "https://api.getclean.ai/problems/overloaded",
  "title": "The service is overloaded",
  "status": 503,
  "detail": "The request could not start within the 30-second queue bound; ask again with the same key in 15 seconds.",
  "instance": "https://api.getclean.ai/requests/req_dVKh740AKEi99ibtCu8L6w",
  "request_id": "req_dVKh740AKEi99ibtCu8L6w",
  "who_must_act": "service",
  "retryable": true,
  "retry_after_seconds": 15
}
```

Every rule of `fetch_contents`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
