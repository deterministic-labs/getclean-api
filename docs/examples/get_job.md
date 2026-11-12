# get_job

Read a job, or wait for it to finish, free. The answer comes at the final state or when `wait_seconds` ends, with the job as it stands; it is `200` when the job failed too, with the failure inside. `Retry-After` and `retry_after_seconds` come on every answer that is not final. Once `contents_id` is set, `get_contents` reads the record; `cancel_job` asks the job to stop.

**What it costs.** The key needs `jobs:read`. The call is free. The answer is `200` with `Job`, never cached. A `HEAD` on this path is answered at once and does not wait.

`GET /v1/jobs/{job_id}`

## A completed job whose record is partial, two pages having failed

The request:

```sh
curl https://api.getclean.ai/v1/jobs/job_8Rt2mqXKclxu58MCwLkSCV \
  -H "Authorization: Bearer $GETCLEAN_API_KEY"
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_01Qm89u0cStrgTL7bxmqKa
Content-Type: application/json

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
  "request_id": "req_01Qm89u0cStrgTL7bxmqKa"
}
```

Every rule of `get_job`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
