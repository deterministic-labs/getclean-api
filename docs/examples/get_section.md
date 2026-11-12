# get_section

Read one section of a record, free: its text when it fits, its own text and the rows of its child sections when it does not, and a page of its text when a cut is needed.

Give it the record's `cnt_` id and the section's `s` id from the map, `sections`, which a fetch returns when the text did not fit or when `max_characters` was `0`. `s0` is the text before the first heading; on a page or a document without headings it is the whole text. Use `get_contents` for the whole record; use `list_blocks` for the blocks of a section by kind.

**What it costs.** The key needs `contents:read`. The call is free.

`GET /v1/contents/{contents_id}/sections/{section_id}`

## A section whose text fits whole

The request:

```sh
curl https://api.getclean.ai/v1/contents/cnt_3Fk9abaUhNX7t2eKkgfd3e/sections/s2 \
  -H "Authorization: Bearer $GETCLEAN_API_KEY"
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_01JgELUWGGDGlc96clfpJQ
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
  "section": {
    "id": "s2",
    "title": "Margin",
    "level": 2,
    "characters": 1810,
    "basis": "structure"
  },
  "formats": [
    "markdown"
  ],
  "markdown": "## Margin\n\n…",
  "truncated": false,
  "notices": [],
  "request_id": "req_01JgELUWGGDGlc96clfpJQ"
}
```

Every rule of `get_section`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
