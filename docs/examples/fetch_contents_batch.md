# fetch_contents_batch

Fetch 1 to 20 pages or documents at their URLs in one call. You get one record per address, kept as a single fetch's is, with a tally first and the sum of the costs last.

Give it the addresses as `items`, each with its own few fields, and at the top the fields every item shares. The results come in input order, each a record or the problem that skipped it. Nothing here is atomic: an item that fails or is skipped leaves the others standing. The batch is not a resource, so it has no id, no expiry and no `Location`; each record has its own. Use `fetch_contents` for one address; use `upload_contents` for a file you hold. A batch takes at most 20 addresses and no files.

**What it costs.** The key needs `contents:fetch`, plus `contents:model` as on `fetch_contents`, decided over the top fields and every item before any work. The price is the sum of the records' costs, each priced as a fetch, with `units` summed by name. An item that was skipped, or whose record failed, was refused or needs a person, bills nothing.

`POST /v1/contents:batch`

## Two records delivered, one unchanged against its fingerprint, and one item skipped for its address

The request:

```sh
curl https://api.getclean.ai/v1/contents:batch \
  -H "Authorization: Bearer $GETCLEAN_API_KEY" \
  -H "Idempotency-Key: $(uuidgen)" \
  -H "Content-Type: application/json" \
  -d '{"items": [{"url": "https://a.example/report", "label": "a"}, {"url": "https://b.example/filing", "label": "b", "baseline_fingerprint": "sha-256=:kw4QGoYGxOYpZ0EZGL+nxMfFUXfrxcp+P0M4EOrEiH4=:"}, {"url": "http://10.0.0.7/admin", "label": "c"}], "formats": ["json"], "block_kinds": ["table"], "max_total_characters": 60000, "max_cost": {"amount": "0.1000", "currency": "USD"}}'
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_01Jx0V1CDhYS12ULqNUtDm
Content-Type: application/json

{
  "counts": {
    "delivered": 2,
    "partial": 0,
    "failed": 0,
    "refused": 0,
    "needs_person": 0,
    "skipped": 1
  },
  "results": [
    {
      "index": 0,
      "label": "a",
      "contents": {
        "id": "cnt_1aQXCj1gfV92qewVcOExbP",
        "outcome": {
          "kind": "delivered",
          "reason": "whole"
        },
        "notices": [],
        "fetched_at": "2026-11-04T09:12:00Z",
        "fingerprint": "sha-256=:Nq4iU56FPWeajZrOTZ7lW1KHecsKmVU+O6hc5H0r3RE=:",
        "scope": "main",
        "record_scope": "main",
        "formats": [
          "json"
        ],
        "truncated": false,
        "blocks": [
          {
            "id": "b4",
            "kind": "table",
            "section_id": "s1",
            "characters": 58,
            "links": [],
            "highlight_ids": [],
            "table": {
              "caption": "Revenue by year",
              "rows": [
                [
                  "Year",
                  "Revenue"
                ],
                [
                  "2024",
                  "3.7 bn"
                ],
                [
                  "2025",
                  "4.1 bn"
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
        "counts": {
          "characters": 5120,
          "blocks": {
            "heading": 3,
            "text": 15,
            "table": 1
          },
          "links": {
            "page": 6
          }
        },
        "hidden_text": [],
        "left_out": [
          {
            "kind": "navigation",
            "characters": 900
          }
        ],
        "source": {
          "url": "https://a.example/report",
          "final_url": "https://a.example/report",
          "redirects": [],
          "status_code": 200,
          "media_type": "text/html",
          "carrier": "web",
          "access_kind": "open",
          "title": "Annual report",
          "authors": [],
          "published_date": "2026-03-02",
          "published_date_precision": "day",
          "published_date_basis": "structured_data",
          "modified_date": null,
          "publisher": "A Example",
          "canonical_url": null,
          "language": "en",
          "language_versions": [],
          "profile": {
            "kind": "company",
            "role": "primary",
            "independence": "unknown",
            "review": {
              "kind": "none",
              "by": null
            }
          },
          "robots": "allowed",
          "declared_terms": [],
          "structured_data": [],
          "origins": [],
          "visitor": {
            "country": "DE",
            "language": "de-DE,de;q=0.9",
            "network": "datacenter"
          }
        },
        "execution": {
          "version": "1.0.0",
          "configuration": "cfg-2026-11",
          "models": [],
          "elapsed_seconds": 5.8
        },
        "cost": {
          "ceiling": {
            "amount": "0.0050",
            "currency": "USD"
          },
          "actual": {
            "amount": "0.0050",
            "currency": "USD"
          },
          "units": {
            "contents": 1
          },
          "replayed": false
        },
        "retention": "hold",
        "run_id": "run_default",
        "expires_at": "2026-11-06T09:12:00Z",
        "request_id": "req_01Jx0V1CDhYS12ULqNUtDm"
      }
    },
    {
      "index": 1,
      "label": "b",
      "contents": {
        "id": "cnt_2bLpzRvKxOEx0I72jKoQSw",
        "outcome": {
          "kind": "delivered",
          "reason": "unchanged"
        },
        "notices": [],
        "fetched_at": "2026-11-04T09:12:00Z",
        "fingerprint": "sha-256=:kw4QGoYGxOYpZ0EZGL+nxMfFUXfrxcp+P0M4EOrEiH4=:",
        "scope": "main",
        "record_scope": "main",
        "formats": [],
        "truncated": false,
        "source": {
          "url": "https://b.example/filing",
          "final_url": "https://b.example/filing",
          "redirects": [],
          "status_code": 200,
          "media_type": "text/html",
          "carrier": "web",
          "access_kind": "open",
          "title": "Annual filing 2025",
          "authors": [],
          "published_date": "2026-02-14",
          "published_date_precision": "day",
          "published_date_basis": "meta_tag",
          "modified_date": null,
          "publisher": "B Example",
          "canonical_url": null,
          "language": "en",
          "language_versions": [],
          "profile": {
            "kind": "company",
            "role": "primary",
            "independence": "unknown",
            "review": {
              "kind": "none",
              "by": null
            }
          },
          "robots": "allowed",
          "declared_terms": [],
          "structured_data": [],
          "origins": [],
          "visitor": {
            "country": "DE",
            "language": "de-DE,de;q=0.9",
            "network": "datacenter"
          }
        },
        "execution": {
          "version": "1.0.0",
          "configuration": "cfg-2026-11",
          "models": [],
          "elapsed_seconds": 6.1
        },
        "cost": {
          "ceiling": {
            "amount": "0.0050",
            "currency": "USD"
          },
          "actual": {
            "amount": "0.0050",
            "currency": "USD"
          },
          "units": {
            "contents": 1
          },
          "replayed": false
        },
        "retention": "hold",
        "run_id": "run_default",
        "expires_at": "2026-11-06T09:12:01Z",
        "request_id": "req_01Jx0V1CDhYS12ULqNUtDm"
      }
    },
    {
      "index": 2,
      "label": "c",
      "problem": {
        "type": "https://api.getclean.ai/problems/destination-refused",
        "title": "The destination is refused",
        "detail": "The address is not globally reachable.",
        "instance": "https://api.getclean.ai/requests/req_01Jx0V1CDhYS12ULqNUtDm/items/2",
        "request_id": "req_01Jx0V1CDhYS12ULqNUtDm",
        "who_must_act": "caller",
        "retryable": false
      }
    }
  ],
  "cost": {
    "ceiling": {
      "amount": "0.1000",
      "currency": "USD"
    },
    "actual": {
      "amount": "0.0100",
      "currency": "USD"
    },
    "units": {
      "contents": 2
    },
    "replayed": false
  },
  "request_id": "req_01Jx0V1CDhYS12ULqNUtDm"
}
```

Every rule of `fetch_contents_batch`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
