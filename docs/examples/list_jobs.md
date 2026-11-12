# list_jobs

List the account's jobs, newest first, free. `state` and `kind` filter them, and every filter you send must match. A job started while you page may make an item repeat; when you merge pages, keep one entry per `id`.

**What it costs.** The key needs `jobs:read`. The call is free. The answer is `200` with `JobPage`.

`GET /v1/jobs`

## The account's jobs, one completed job among them

The request:

```sh
curl https://api.getclean.ai/v1/jobs \
  -H "Authorization: Bearer $GETCLEAN_API_KEY"
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_01RcyYPWPnGlycDKoB9AfI
Content-Type: application/json

{
  "jobs": [
    {
      "id": "job_8Rt2mqXKclxu58MCwLkSCV",
      "kind": "upload_contents",
      "state": "completed",
      "finished": true,
      "counts": {
        "parsed_count": 310,
        "failed_count": 2,
        "remaining_count": 0
      },
      "cost": {
        "ceiling": {
          "amount": "1.0000",
          "currency": "USD"
        },
        "actual": {
          "amount": "0.3300",
          "currency": "USD"
        },
        "units": {
          "contents": 1,
          "document_pages": 310,
          "recognized_pages": 3
        },
        "replayed": false
      },
      "outcome": {
        "kind": "partial",
        "reason": "pages_failed"
      },
      "contents_id": "cnt_f9a1LknFzePvIKv1pEkejs",
      "created_at": "2026-11-04T10:02:11Z",
      "updated_at": "2026-11-04T10:14:52Z",
      "expires_at": "2026-12-04T10:14:52Z",
      "request_id": "req_01RcyYPWPnGlycDKoB9AfI"
    }
  ],
  "notices": [],
  "request_id": "req_01RcyYPWPnGlycDKoB9AfI"
}
```

Every rule of `list_jobs`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
