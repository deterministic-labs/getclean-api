# get_contents

Read a record you already have, free: the same copy in any format, at any size, under either view, with the model work the fetch made.

Give it the `cnt_` id an earlier `fetch_contents`, `upload_contents` or `search` returned. Nothing is fetched from the web; the answer comes from the copy getclean kept. Use `fetch_contents` for a URL; use `get_section`, `list_blocks` and `list_links` to read one part of the record at a time.

**What it costs.** The key needs `contents:read`. The call is free, so the record carries no `cost` on this answer.

`GET /v1/contents/{contents_id}`

## A record you already have, read whole under a larger max_characters than its fetch allowed

The request:

```sh
curl https://api.getclean.ai/v1/contents/cnt_5Gh7cdyeVQ6qoJhBFE31L1?max_characters=1000000 \
  -H "Authorization: Bearer $GETCLEAN_API_KEY"
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_01PaufBlzLM6CZzXNwUinf
Content-Type: application/json

{
  "id": "cnt_5Gh7cdyeVQ6qoJhBFE31L1",
  "outcome": {
    "kind": "delivered",
    "reason": "sections_only"
  },
  "notices": [],
  "fetched_at": "2026-11-04T08:50:30Z",
  "fingerprint": "sha-256=:Vn2VtrGw48PmhVZSc0+War4NLekU3Ecg5FLbdwF1nMM=:",
  "scope": "main",
  "record_scope": "main",
  "formats": [
    "markdown"
  ],
  "truncated": false,
  "markdown": "# Annual report 2025\n\n…the whole text under max_characters 200000…",
  "counts": {
    "characters": 61200,
    "blocks": {
      "heading": 14,
      "text": 120,
      "table": 6
    },
    "links": {
      "page": 40
    }
  },
  "hidden_text": [],
  "left_out": [
    {
      "kind": "navigation",
      "characters": 1480
    }
  ],
  "source": {
    "url": "https://example.com/annual-2025",
    "final_url": "https://example.com/annual-2025",
    "redirects": [],
    "status_code": 200,
    "media_type": "text/html",
    "carrier": "web",
    "access_kind": "open",
    "title": "Annual report 2025",
    "authors": [],
    "publisher": "Example Corp",
    "canonical_url": null,
    "published_date": "2026-03-12",
    "published_date_precision": "day",
    "published_date_basis": "structured_data",
    "modified_date": null,
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
    "structured_data": [],
    "origins": [],
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
    "elapsed_seconds": 9.0
  },
  "retention": "hold",
  "run_id": "run_default",
  "expires_at": "2026-11-06T12:00:00Z",
  "request_id": "req_01PaufBlzLM6CZzXNwUinf"
}
```

## A record read after it expired

The answer:

```http
HTTP/1.1 410 Gone
Request-Id: req_01QEihyEKxtyS4rknqVJEV
Content-Type: application/problem+json

{
  "type": "https://api.getclean.ai/problems/contents-expired",
  "title": "The record has expired",
  "status": 410,
  "detail": "The record has expired; fetch the page again.",
  "instance": "https://api.getclean.ai/requests/req_01QEihyEKxtyS4rknqVJEV",
  "request_id": "req_01QEihyEKxtyS4rknqVJEV",
  "who_must_act": "caller",
  "retryable": false,
  "expired_at": "2026-11-06T12:00:00Z",
  "change": {
    "operation": "fetch_contents",
    "field": "url"
  }
}
```

Every rule of `get_contents`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
