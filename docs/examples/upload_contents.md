# upload_contents

Read a document you hold, or one at a URL that needs more time than a fetch gives. You get the same record a fetch makes, the content with its structure intact, the map of its sections, the facts of the source, a fingerprint and the price, with `pages` saying how many pages were read, which failed and which were recognized from their image, and the record is kept for later reads.

Send the file as the `document` part, or its address as `url`. The parse runs on as a job when it needs more than `wait_seconds`: a scanned document takes seconds per page, and stopping early would lose pages, so this call may answer with a job where `fetch_contents` never does. Use `fetch_contents` for a web page, or for a document at a URL that fits in one wait; use `get_contents` to read a record you already have.

**What it costs.** The key needs `contents:fetch`, plus `contents:model` when you send `json_schema`, set `summary` or send `highlights` without `deterministic_only`; getclean decides this from the form before any work. The price is 1 `contents`, plus `document_pages` for every page parsed and `recognized_pages` for every page recognized, plus `model_steps` for each model field that ran. A long scan is the most expensive call there is, since each recognized page bills both page units. It is billed when the record becomes final: in the call that answered `201`, or when the job completes or is canceled with pages done. An `unchanged` answer bills the same 1 `contents`. A parse that failed, was refused or needs a person bills nothing.

`POST /v1/contents:upload`

## A ten-page PDF with a text layer, parsed whole within the wait

The request:

```sh
curl https://api.getclean.ai/v1/contents:upload \
  -H "Authorization: Bearer $GETCLEAN_API_KEY" \
  -H "Idempotency-Key: $(uuidgen)" \
  -F "document=@minutes.pdf;type=application/octet-stream"
```

The answer:

```http
HTTP/1.1 201 Created
Location: https://api.getclean.ai/v1/contents/cnt_2Kp0zzrSBNSNtgjapZm9pq
Request-Id: req_01MWhgMG0UHPXXGtnjhJJO
Content-Type: application/json

{
  "contents": {
    "id": "cnt_2Kp0zzrSBNSNtgjapZm9pq",
    "outcome": {
      "kind": "delivered",
      "reason": "whole"
    },
    "notices": [],
    "fetched_at": "2026-11-04T10:05:00Z",
    "fingerprint": "sha-256=:Ab3QtW7hCl7ACP+qfkR6P97Od1HtkFFDIcl9B4pPos0=:",
    "scope": "main",
    "record_scope": "main",
    "formats": [
      "markdown"
    ],
    "truncated": false,
    "markdown": "# Minutes of the meeting…",
    "counts": {
      "characters": 18400,
      "blocks": {
        "heading": 6,
        "text": 40
      },
      "links": {}
    },
    "source": {
      "redirects": [],
      "media_type": "application/pdf",
      "carrier": "upload",
      "filename": "minutes.pdf",
      "document_digest": "sha-256=:7HqC7GihbMvNe0QRGihXoSzWNR2cLpquMihXOseZoSw=:",
      "title": "Minutes",
      "authors": [],
      "published_date": "2026-09-01",
      "published_date_precision": "day",
      "published_date_basis": "document_properties",
      "modified_date": null,
      "language": "en",
      "language_versions": [],
      "robots": "not_applicable",
      "declared_terms": [],
      "structured_data": [],
      "origins": []
    },
    "pages": {
      "count": 10,
      "parsed_count": 10,
      "failed_pages": [],
      "recognized": [],
      "pictured": []
    },
    "execution": {
      "version": "1.0.0",
      "configuration": "cfg-2026-11",
      "models": [],
      "elapsed_seconds": 3.2
    },
    "cost": {
      "ceiling": {
        "amount": "1.0000",
        "currency": "USD"
      },
      "actual": {
        "amount": "0.0150",
        "currency": "USD"
      },
      "units": {
        "contents": 1,
        "document_pages": 10
      },
      "replayed": false
    },
    "retention": "hold",
    "run_id": "run_default",
    "expires_at": "2026-11-06T10:05:00Z",
    "request_id": "req_01MWhgMG0UHPXXGtnjhJJO"
  },
  "request_id": "req_01MWhgMG0UHPXXGtnjhJJO"
}
```

## A 312-page document with three scanned pages, its parse running as a job

The request:

```sh
curl https://api.getclean.ai/v1/contents:upload \
  -H "Authorization: Bearer $GETCLEAN_API_KEY" \
  -H "Idempotency-Key: $(uuidgen)" \
  -F "document=@records.pdf;type=application/octet-stream" \
  -F 'max_cost={"amount": "1.0000", "currency": "USD"};type=application/json'
```

The answer:

```http
HTTP/1.1 202 Accepted
Location: https://api.getclean.ai/v1/jobs/job_8Rt2mqXKclxu58MCwLkSCV
Retry-After: 20
Request-Id: req_01LyBFDAgNmn3TTbQ2Fe4r
Content-Type: application/json

{
  "job": {
    "id": "job_8Rt2mqXKclxu58MCwLkSCV",
    "kind": "upload_contents",
    "state": "running",
    "finished": false,
    "stage": "recognizing",
    "counts": {
      "parsed_count": 41,
      "failed_count": 0,
      "remaining_count": 271
    },
    "cost": {
      "ceiling": {
        "amount": "1.0000",
        "currency": "USD"
      },
      "actual": {
        "amount": "0.0610",
        "currency": "USD"
      },
      "units": {
        "contents": 1,
        "document_pages": 41,
        "recognized_pages": 3
      },
      "replayed": false
    },
    "retry_after_seconds": 20,
    "created_at": "2026-11-04T10:02:11Z",
    "updated_at": "2026-11-04T10:02:41Z",
    "request_id": "req_01LyBFDAgNmn3TTbQ2Fe4r"
  },
  "request_id": "req_01LyBFDAgNmn3TTbQ2Fe4r"
}
```

## The upload's document and url sent together

The answer:

```http
HTTP/1.1 422 Unprocessable Content
Request-Id: req_01NdCq5kEHkceDpAo9MfAV
Content-Type: application/problem+json

{
  "type": "https://api.getclean.ai/problems/invalid-field",
  "title": "A field is invalid",
  "status": 422,
  "detail": "document and url exclude each other; send one.",
  "instance": "https://api.getclean.ai/requests/req_01NdCq5kEHkceDpAo9MfAV",
  "request_id": "req_01NdCq5kEHkceDpAo9MfAV",
  "who_must_act": "caller",
  "retryable": false,
  "violations": [
    {
      "kind": "exclusive",
      "place": "form",
      "field": "url",
      "message": "excludes document"
    },
    {
      "kind": "exclusive",
      "place": "form",
      "field": "document",
      "message": "excludes url"
    }
  ]
}
```

Every rule of `upload_contents`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
