# get_search

Read a search you already have, free: the first page as it was answered, and behind it the full list the search stored, including the results it dropped and why. Nothing is searched again and nothing is charged; only the record's `expires_at` moves.

The first page is the original answer as stored, whatever `page_size`: its members and the notices kept with it. A notice of the original answer that was not kept does not come back, and `dropped_reason` is absent on every candidate. A later page is the stored list in rank order, and every item on it carries `dropped_reason`. Every other member comes as stored; `request_id` is this call's, and `expires_at` is the record's new one. `next_page_token` comes while more remain. `fetch_contents` reads a candidate by its URL.

**What it costs.** The key needs `search:read`. The call is free. The answer is `200` with `Search`; the call moves the record's `expires_at` 48 hours ahead.

`GET /v1/search/{search_id}`

## A later page of the stored list, a dropped candidate with its reason, every other member as stored

The request:

```sh
curl https://api.getclean.ai/v1/search/srch_4HmUunqCCXquleKVCosqFG?page_token=eyJzIjoic3JjaF80SG0iLCJvIjoyfQ \
  -H "Authorization: Bearer $GETCLEAN_API_KEY"
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_02Bm6tTFlq4Fjkaic7g4OM
Content-Type: application/json

{
  "id": "srch_4HmUunqCCXquleKVCosqFG",
  "retention": "hold",
  "outcome": {
    "kind": "delivered",
    "reason": "candidates"
  },
  "notices": [],
  "coverage_gaps": [],
  "candidates": [
    {
      "id": "cand_b7v7hQoJ35NvgmndljizaO",
      "url": "https://example.org/commentary",
      "title": "Commentary",
      "dropped_reason": "not_relevant",
      "relevance_score": 0.31,
      "fetch_cost": {
        "amount": "0.0050",
        "currency": "USD"
      },
      "source_profile": {
        "kind": "press",
        "role": "secondary",
        "independence": "unknown",
        "review": {
          "kind": "editorial",
          "by": null
        }
      },
      "copy_count": 0,
      "language_versions": [],
      "carrier": "web",
      "access": {
        "kind": "open",
        "declared_terms": [],
        "robots": "allowed"
      },
      "identifier_matches": [],
      "excerpts": [],
      "matches": [
        {
          "wording_index": 0,
          "datasource_id": "web",
          "rank": 17
        }
      ]
    }
  ],
  "counts": {
    "returned": 3,
    "found": 41,
    "dropped": {
      "not_relevant": 30,
      "undated": 0,
      "max_per_domain": 0,
      "blocked_domain": 0,
      "outside_allowed": 0,
      "source_kind": 0,
      "source_independence": 0,
      "folded_copy": 8,
      "phrase_check": 0,
      "exclusion_check": 0,
      "beyond_max_candidates": 0
    }
  },
  "end_reason": "relevance",
  "interpretation": {
    "canonical_query": "EU AI Act article 50 marking obligations",
    "phrases": [],
    "exclusions": [],
    "operators": [],
    "wordings": [
      {
        "index": 0,
        "text": "EU AI Act article 50 marking obligations",
        "language": "en",
        "language_basis": "detected",
        "origin": "caller",
        "result_counts": {
          "web": 41
        }
      }
    ],
    "languages_searched": [
      "en"
    ]
  },
  "applied_request": {
    "query": "EU AI Act article 50 marking obligations",
    "datasources": [
      "web"
    ],
    "published_within_days": 365,
    "undated": "shown",
    "safe_search": "moderate",
    "max_per_datasource": 10,
    "ranking_order": "relevance",
    "max_candidates": 3,
    "max_excerpt_characters": 600,
    "max_total_characters": 40000,
    "contents": {
      "top": 1,
      "max_characters": 8000,
      "scope": "main",
      "summary": false
    },
    "view": "full",
    "wait_seconds": 10,
    "max_cost": {
      "amount": "0.1000",
      "currency": "USD"
    },
    "deterministic_only": false,
    "pinned_version": "1.0.0",
    "run_id": "run_default",
    "retention": "hold"
  },
  "datasources_searched": [
    {
      "id": "web",
      "display_name": "Web",
      "group": "web",
      "reason": "default",
      "outcome": {
        "kind": "delivered",
        "reason": "candidates"
      },
      "effective_country": "DE",
      "effective_language": "en",
      "wordings": [
        0
      ],
      "returned_count": 41,
      "result_count": 41,
      "result_count_kind": "exact",
      "lead_count": 3,
      "filters_applied": {
        "allowed_domains": {
          "state": "not_applicable"
        },
        "blocked_domains": {
          "state": "not_applicable"
        },
        "published_from": {
          "state": "not_applicable"
        },
        "published_until": {
          "state": "not_applicable"
        },
        "published_within_days": {
          "state": "native"
        },
        "undated": {
          "state": "emulated",
          "how": "pages without a detectable date kept, as asked"
        },
        "languages": {
          "state": "not_applicable"
        },
        "media_types": {
          "state": "not_applicable"
        },
        "safe_search": {
          "state": "native"
        },
        "source_kinds": {
          "state": "not_applicable"
        },
        "source_independence": {
          "state": "not_applicable"
        },
        "as_of_date": {
          "state": "not_applicable"
        }
      },
      "operators_applied": {
        "phrase": {
          "state": "not_applicable"
        },
        "exclusion": {
          "state": "not_applicable"
        },
        "alternatives": {
          "state": "not_applicable"
        },
        "site": {
          "state": "not_applicable"
        },
        "filetype": {
          "state": "not_applicable"
        },
        "intitle": {
          "state": "not_applicable"
        },
        "inurl": {
          "state": "not_applicable"
        },
        "before": {
          "state": "not_applicable"
        },
        "after": {
          "state": "not_applicable"
        },
        "wildcard": {
          "state": "not_applicable"
        }
      },
      "access_used": "open",
      "cost": {
        "ceiling": {
          "amount": "0.0100",
          "currency": "USD"
        },
        "actual": {
          "amount": "0.0010",
          "currency": "USD"
        },
        "units": {
          "datasource_queries": 1
        },
        "replayed": false
      }
    }
  ],
  "ranking": {
    "reranked": true,
    "reranker_version": "rr-2026-10",
    "min_score": 0.42,
    "instructions_applied": false,
    "priorities": [],
    "order": "relevance",
    "preferred_domains": [],
    "merge": "stratified_rank_fusion",
    "strata": [
      {
        "datasource_id": "web",
        "language": "en",
        "lead_count": 3
      }
    ]
  },
  "execution": {
    "version": "1.0.0",
    "configuration": "cfg-2026-11",
    "models": [
      {
        "step": "reranking",
        "version": "rr-2026-10"
      },
      {
        "step": "discovery",
        "version": "disc-2026-10"
      }
    ],
    "elapsed_seconds": 8.4
  },
  "cost": {
    "ceiling": {
      "amount": "0.1000",
      "currency": "USD"
    },
    "actual": {
      "amount": "0.0200",
      "currency": "USD"
    },
    "units": {
      "searches": 1,
      "datasource_queries": 1,
      "model_steps": 2,
      "contents": 1
    },
    "replayed": false
  },
  "searched_at": "2026-11-05T09:00:00Z",
  "run_id": "run_default",
  "expires_at": "2026-11-07T09:30:00Z",
  "request_id": "req_02Bm6tTFlq4Fjkaic7g4OM",
  "next_page_token": "eyJzIjoic3JjaF80SG0iLCJvIjozfQ"
}
```

Every rule of `get_search`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
