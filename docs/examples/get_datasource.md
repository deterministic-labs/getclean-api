# get_datasource

Read one entry of the catalog whole, free; the answer may be cached for an hour. You get what the source covers, how it is reached, which filters and operators it honors, which identifier schemes it resolves and with which issuer codes, and whether it keeps history for `as_of_date`.

**What it costs.** The key needs `search:read`. The call is free. The answer is `200` with `Datasource` and `Cache-Control: max-age=3600`.

`GET /v1/datasources/{datasource_id}`

## A legal register that resolves dockets and reporter citations

The request:

```sh
curl https://api.getclean.ai/v1/datasources/courtlistener \
  -H "Authorization: Bearer $GETCLEAN_API_KEY"
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_02DBMPlcTpjeCo52E9vS45
Content-Type: application/json

{
  "id": "courtlistener",
  "display_name": "CourtListener",
  "group": "legal",
  "countries": [
    "US"
  ],
  "languages": [
    "en"
  ],
  "access": {
    "kind": "open"
  },
  "searchable": true,
  "filters": {
    "allowed_domains": "not_applicable",
    "blocked_domains": "not_applicable",
    "published_from": "native",
    "published_until": "native",
    "published_within_days": "native",
    "undated": "emulated",
    "languages": "not_applicable",
    "media_types": "emulated",
    "safe_search": "not_applicable",
    "source_kinds": "not_applicable",
    "source_independence": "not_applicable",
    "as_of_date": "not_applicable"
  },
  "operators": {
    "phrase": "native",
    "exclusion": "native",
    "alternatives": "native",
    "site": "not_applicable",
    "filetype": "not_applicable",
    "intitle": "emulated",
    "inurl": "not_applicable",
    "before": "native",
    "after": "native",
    "wildcard": "dropped"
  },
  "identifier_schemes": [
    "docket",
    "reporter_citation"
  ],
  "issuers": {
    "docket": [
      "ca9",
      "cand",
      "nysd"
    ]
  },
  "history": false,
  "card_url": "https://api.getclean.ai/datasources/courtlistener",
  "request_id": "req_02DBMPlcTpjeCo52E9vS45"
}
```

Every rule of `get_datasource`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
