# cancel_job

Ask a job to stop, free. The answer is `200` with the job as it stands; the work may finish before it stops, and `Retry-After` comes while it still runs, as on `get_job`. A job already final is unchanged. With pages already parsed the record is `partial`, `canceled`, the pages kept and billed; with none, no record and nothing billed.

**What it costs.** The key needs `jobs:cancel`. The call is free. It takes no body; a body sent is refused `400 invalid-request`.

`POST /v1/jobs/{job_id}:cancel`

## A job canceled with 41 pages done, which are kept and billed

The request:

```sh
curl https://api.getclean.ai/v1/jobs/job_3ZYgQAhOBQmM5xiilC8Fj9:cancel \
  -X POST \
  -H "Authorization: Bearer $GETCLEAN_API_KEY"
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_01Q2Eg6uJmHGdKZo83Xpje
Content-Type: application/json

{
  "id": "job_3ZYgQAhOBQmM5xiilC8Fj9",
  "kind": "upload_contents",
  "state": "canceled",
  "finished": true,
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
  "outcome": {
    "kind": "partial",
    "reason": "canceled"
  },
  "contents_id": "cnt_3xiMwacMbgXiIanT2iBPcB",
  "created_at": "2026-11-04T10:02:11Z",
  "updated_at": "2026-11-04T10:03:05Z",
  "expires_at": "2026-12-04T10:03:05Z",
  "request_id": "req_01Q2Eg6uJmHGdKZo83Xpje"
}
```

Every rule of `cancel_job`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
