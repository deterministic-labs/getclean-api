# list_links

List the links of a record, free: every link with its kind and the block and section that hold it, in document order, one page of results at a time, without the 1,000-link cap a fetch puts on `formats: links`.

Give it the record's `cnt_` id and the filters you want; every filter you send must match. Use `fetch_contents` to read a linked page; use `list_blocks` for the blocks themselves.

**What it costs.** The key needs `contents:read`. The call is free.

`GET /v1/contents/{contents_id}/links`

## The file links of a record, one of them

The request:

```sh
curl https://api.getclean.ai/v1/contents/cnt_3Fk9abaUhNX7t2eKkgfd3e/links?link_kinds=file \
  -H "Authorization: Bearer $GETCLEAN_API_KEY"
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_01Jp0SRsqpJGQ9hFdqVC27
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
  "links": [
    {
      "url": "https://example.com/q3/report.pdf",
      "text": "Full report",
      "kind": "file",
      "external": false,
      "block_id": "b12",
      "section_id": "s3"
    }
  ],
  "notices": [],
  "request_id": "req_01Jp0SRsqpJGQ9hFdqVC27"
}
```

Every rule of `list_links`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
