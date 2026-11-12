# delete_contents

Erase a record before it expires: the record, its screenshot, its raw HTML, its document images, its recognized page images and its stored replays. Later calls on the id answer `404`. A retry of the fetch with its idempotency key, within the key's 24 hours, answers `404` naming the deletion, never a second fetch. A job that points at the record keeps its `contents_id`, and that id answers `404`. A second delete is `404`.

**What it costs.** The key needs `contents:delete`. The call is free. The answer is `204 No Content`.

`DELETE /v1/contents/{contents_id}`

## The request

```sh
curl https://api.getclean.ai/v1/contents/cnt_3Fk9abaUhNX7t2eKkgfd3e \
  -X DELETE \
  -H "Authorization: Bearer $GETCLEAN_API_KEY"
```

## The answer

```http
HTTP/1.1 204 No Content
```

Every rule of `delete_contents`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
