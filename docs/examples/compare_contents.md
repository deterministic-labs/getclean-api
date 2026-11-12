# compare_contents

Compare a record you already have with a baseline, block by block and cell by cell, without a model, free. You get whether anything changed, a tally, and each change with both of its sides. The baseline is another record, `baseline_contents_id`, or the markdown you kept yourself as a record returned it, `baseline_markdown` with its `baseline_fingerprint`. It is a `POST` with a body that bills nothing and changes nothing but the record's `expires_at`, so it is safe to repeat.

**What it costs.** The key needs `contents:read`. The call is free. The answer is `200` with `Comparison`; the call moves the current record's `expires_at` 48 hours ahead. The body is at most 8 MiB, so that a baseline of 1,000,000 characters fits in any script.

`POST /v1/contents/{contents_id}:compare`

## One table cell changed between two fetches of the same page a week apart

The request:

```sh
curl https://api.getclean.ai/v1/contents/cnt_9Zze6X8RDFg2XxyKyLlV5T:compare \
  -H "Authorization: Bearer $GETCLEAN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"baseline_contents_id": "cnt_3Fk9abaUhNX7t2eKkgfd3e"}'
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_01JONfNiPNrnysSRQjsH2k
Content-Type: application/json

{
  "contents_id": "cnt_9Zze6X8RDFg2XxyKyLlV5T",
  "expires_at": "2026-11-13T08:40:02Z",
  "baseline_contents_id": "cnt_3Fk9abaUhNX7t2eKkgfd3e",
  "current": {
    "fetched_at": "2026-11-11T08:40:02Z",
    "fingerprint": "sha-256=:Rt11HNu+jiwX5K846APgS7Sri/ToHiTmp+MxA8fDhrM=:",
    "verified": true
  },
  "baseline": {
    "fetched_at": "2026-11-04T08:40:12Z",
    "fingerprint": "sha-256=:kw4QGoYGxOYpZ0EZGL+nxMfFUXfrxcp+P0M4EOrEiH4=:",
    "verified": true
  },
  "changed": true,
  "counts": {
    "added": 0,
    "removed": 0,
    "changed": 1,
    "moved": 0
  },
  "changes": [
    {
      "kind": "changed",
      "block_kind": "table",
      "before": {
        "section_id": "s2",
        "block_id": "b7",
        "text": "| Q3 | 41.2% |"
      },
      "after": {
        "section_id": "s2",
        "block_id": "b7",
        "text": "| Q3 | 41.6% |"
      },
      "cells": [
        {
          "row": 1,
          "column": 1,
          "before_text": "41.2%",
          "after_text": "41.6%"
        }
      ]
    }
  ],
  "notices": [],
  "request_id": "req_01JONfNiPNrnysSRQjsH2k"
}
```

Every rule of `compare_contents`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
