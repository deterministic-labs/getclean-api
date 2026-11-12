# get_limits

Read your key's limits and your account's money in one answer, free, before a batch or any call that must fit a budget. You get the prepaid balance after the sums reserved by calls in flight, the use of the current period, every unit's price, the key's cap on one call and its budgets, its rate and the calls allowed in flight at once, the published bounds of both families, the document types taken, the countries getclean can read from, the recognition languages, the archives, the key's policy, and the versions served with the current one. There is no estimate operation: `max_cost` is the protection, and `prices` gives every unit's price.

**What it costs.** The key needs `limits:read`. The call is free. The answer is `200` with `Limits`, never cached, since it is the key's own.

`GET /v1/limits`

## A key's limits on an account with credit left

The request:

```sh
curl https://api.getclean.ai/v1/limits \
  -H "Authorization: Bearer $GETCLEAN_API_KEY"
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_01ZWyyr8KwLQuLkEAedYvD
Content-Type: application/json

{
  "balance": {
    "amount": "42.1000",
    "currency": "USD"
  },
  "usage": {
    "starts_at": "2026-11-01T00:00:00Z",
    "ends_at": "2026-12-01T00:00:00Z",
    "units": {
      "contents": 1840,
      "model_steps": 212,
      "searches": 96
    },
    "spent": {
      "amount": "17.9000",
      "currency": "USD"
    }
  },
  "prices": {
    "contents": {
      "amount": "0.0050",
      "currency": "USD"
    },
    "model_steps": {
      "amount": "0.0020",
      "currency": "USD"
    },
    "screenshots": {
      "amount": "0.0010",
      "currency": "USD"
    },
    "document_pages": {
      "amount": "0.0010",
      "currency": "USD"
    },
    "recognized_pages": {
      "amount": "0.0050",
      "currency": "USD"
    },
    "searches": {
      "amount": "0.0100",
      "currency": "USD"
    },
    "datasource_queries": {
      "amount": "0.0010",
      "currency": "USD"
    }
  },
  "caps": {
    "call_cap": {
      "amount": "0.0500",
      "currency": "USD"
    }
  },
  "rates": {
    "requests_per_minute": 600,
    "concurrency": 20,
    "resets_at": "2026-11-05T09:01:00Z"
  },
  "bounds": {
    "contents": {
      "max_characters": {
        "min": 0,
        "max": 1000000,
        "default_value": 20000,
        "excluded_min": 1,
        "excluded_max": 999
      },
      "list_blocks.max_characters": {
        "min": 1000,
        "max": 1000000,
        "default_value": 20000
      },
      "max_total_characters": {
        "min": 1000,
        "max": 2000000,
        "default_value": 200000
      },
      "wait_seconds": {
        "min": 5,
        "max": 90,
        "default_value": 30
      },
      "get_job.wait_seconds": {
        "min": 0,
        "max": 90,
        "default_value": 0
      },
      "page_size": {
        "min": 1,
        "max": 200,
        "default_value": 50
      },
      "items": {
        "min": 1,
        "max": 20
      },
      "highlights": {
        "min": 1,
        "max": 5
      },
      "recognition_languages": {
        "min": 1,
        "max": 10
      },
      "call_seconds": {
        "max": 110
      },
      "batch_seconds": {
        "max": 600
      },
      "queue_seconds": {
        "max": 30
      },
      "model_step_seconds": {
        "max": 20
      },
      "screenshot_seconds": {
        "max": 15
      },
      "screenshot_bytes": {
        "max": 20000000
      },
      "job_seconds": {
        "max": 1800
      },
      "read_seconds": {
        "max": 10
      },
      "page_bytes": {
        "max": 20000000
      },
      "document_bytes": {
        "max": 104857600
      },
      "document_base64_bytes": {
        "max": 20971520
      },
      "document_pages": {
        "max": 2000
      },
      "document_page_characters": {
        "default_value": 5000
      },
      "body_bytes": {
        "max": 256000
      },
      "batch_body_bytes": {
        "max": 4194304
      },
      "compare_body_bytes": {
        "max": 8388608
      },
      "redirects": {
        "max": 10
      },
      "links": {
        "max": 1000
      },
      "section_rows": {
        "max": 200
      },
      "highlight_occurrences": {
        "max": 50
      },
      "summary_characters": {
        "max": 1500
      },
      "structured_data_bytes": {
        "max": 64000
      },
      "recognition_confidence_min": {
        "min": 0.6
      },
      "version_notice_days": {
        "default_value": 90
      }
    },
    "search": {
      "max_candidates": {
        "min": 1,
        "max": 50,
        "default_value": 10
      },
      "max_per_datasource": {
        "min": 1,
        "max": 100,
        "default_value": 10
      },
      "max_excerpt_characters": {
        "min": 0,
        "max": 4000,
        "default_value": 600
      },
      "max_total_characters": {
        "min": 1000,
        "max": 200000,
        "default_value": 40000
      },
      "wait_seconds": {
        "min": 0.2,
        "max": 60,
        "default_value": 10
      },
      "get_search.page_size": {
        "min": 1,
        "max": 50
      },
      "list_datasources.page_size": {
        "min": 1,
        "max": 200,
        "default_value": 50
      },
      "items": {
        "min": 1,
        "max": 20
      },
      "datasources": {
        "min": 1,
        "max": 10
      },
      "alternate_queries": {
        "min": 1,
        "max": 10
      },
      "call_seconds": {
        "max": 60
      },
      "batch_seconds": {
        "max": 300
      },
      "queue_seconds": {
        "max": 30
      },
      "model_step_seconds": {
        "max": 20
      },
      "body_bytes": {
        "max": 256000
      },
      "batch_body_bytes": {
        "max": 4194304
      }
    }
  },
  "document_media_types": [
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.ms-excel",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "application/vnd.oasis.opendocument.text",
    "application/epub+zip",
    "application/rtf",
    "text/markdown",
    "text/csv",
    "text/html",
    "application/xhtml+xml",
    "application/xml",
    "application/json",
    "application/yaml",
    "text/plain",
    "image/png",
    "image/jpeg",
    "image/tiff",
    "image/webp",
    "image/heic"
  ],
  "exits": [
    "DE",
    "FR",
    "GB",
    "US"
  ],
  "recognition_languages": [
    "en",
    "de",
    "fr",
    "es",
    "it",
    "nl",
    "pt",
    "tr"
  ],
  "archives": [
    "Wayback Machine"
  ],
  "default_exit": "DE",
  "policy": {
    "deterministic_only": false,
    "safe_search": "moderate",
    "retention": "hold",
    "allowed_domains": [],
    "blocked_domains": [],
    "refuse_credential_urls": false
  },
  "versions": [
    {
      "version": "1.0.0",
      "released_at": "2026-10-01T00:00:00Z",
      "changes_url": "https://api.getclean.ai/versions/1.0.0"
    }
  ],
  "current_version": "1.0.0",
  "version_minimum_days": 90,
  "request_id": "req_01ZWyyr8KwLQuLkEAedYvD"
}
```

Every rule of `get_limits`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
