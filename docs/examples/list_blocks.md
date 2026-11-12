# list_blocks

List the blocks of a record, free: by kind, by section, by document page or by id, in document order, one page of results at a time.

Give it the record's `cnt_` id and the filters you want; every filter you send must match. Each block is the record's own `Block`: its id, kind, section, size and text, a table as its rows and spans, an image as its address and size. `block_ids` reads the blocks a highlight names by `block_id`, so you can read the whole block around a match. Use `get_section` for a section's text in one piece; use `get_contents` for the whole record.

**What it costs.** The key needs `contents:read`. The call is free.

`GET /v1/contents/{contents_id}/blocks`

## The table blocks of a record, one of them

The request:

```sh
curl https://api.getclean.ai/v1/contents/cnt_3Fk9abaUhNX7t2eKkgfd3e/blocks?block_kinds=table \
  -H "Authorization: Bearer $GETCLEAN_API_KEY"
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_01J3WbmHqruHQMHIwlFrMB
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
  "blocks": [
    {
      "id": "b7",
      "kind": "table",
      "section_id": "s2",
      "characters": 412,
      "links": [],
      "highlight_ids": [],
      "table": {
        "caption": null,
        "rows": [
          [
            "Quarter",
            "Margin"
          ],
          [
            "Q3",
            "41.2%"
          ]
        ],
        "spans": [],
        "header_rows": [
          0
        ],
        "header_columns": [],
        "basis": "structure"
      }
    }
  ],
  "notices": [],
  "request_id": "req_01J3WbmHqruHQMHIwlFrMB"
}
```

Every rule of `list_blocks`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
