# list_datasources

List the places getclean can search, free; the answer may be cached for an hour. An entry's `id`, its `group` or `set:NAME` goes into the search's `datasources`; `filters` and `operators` say what each source honors, before any search; `issuers` gives the codes an identifier scheme takes, so your agent learns a code from the catalog and never guesses one. Every filter you send must match, and the order is the catalog's own.

**What it costs.** The key needs `search:read`. The call is free. The answer is `200` with `DatasourcePage` and `Cache-Control: max-age=3600`, so a cached answer repeats the first call's `request_id` and rate figures, which describe that call and not yours.

`GET /v1/datasources`

## The web and one legal register, two entries of the catalog

The request:

```sh
curl https://api.getclean.ai/v1/datasources \
  -H "Authorization: Bearer $GETCLEAN_API_KEY"
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_02EtiTZXJiQkv6q3XFlqUa
Content-Type: application/json

{
  "datasources": [
    {
      "id": "web",
      "display_name": "Web",
      "group": "web",
      "countries": [],
      "languages": [],
      "access": {
        "kind": "open"
      },
      "searchable": true,
      "filters": {
        "allowed_domains": "native",
        "blocked_domains": "native",
        "published_from": "native",
        "published_until": "native",
        "published_within_days": "native",
        "undated": "emulated",
        "languages": "native",
        "media_types": "native",
        "safe_search": "native",
        "source_kinds": "emulated",
        "source_independence": "emulated",
        "as_of_date": "not_applicable"
      },
      "operators": {
        "phrase": "native",
        "exclusion": "native",
        "alternatives": "native",
        "site": "native",
        "filetype": "native",
        "intitle": "native",
        "inurl": "native",
        "before": "native",
        "after": "native",
        "wildcard": "native"
      },
      "identifier_schemes": [],
      "history": false,
      "card_url": "https://api.getclean.ai/datasources/web",
      "request_id": "req_02EtiTZXJiQkv6q3XFlqUa"
    },
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
      "request_id": "req_02EtiTZXJiQkv6q3XFlqUa"
    }
  ],
  "notices": [],
  "request_id": "req_02EtiTZXJiQkv6q3XFlqUa"
}
```

Every rule of `list_datasources`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
