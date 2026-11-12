# search

Search up to ten datasources with one question, in up to twenty wordings, and get one ranked list of results with the facts of each and a receipt of what ran where, before any page is read. Each result is a lead, the one page shown for a group of copies. The search is kept as a record, so its full list is read again free, and every cut, skip or change is named in the answer. Use `contents` to fetch the top leads in the same call, `fetch_contents` to read one by its URL, and `list_datasources` to see what can be searched.

**What it costs.** The key needs `search:run`, which covers everything a search does, the inline fetches and their model fields included, under the key's policy. The price is 1 `searches`, plus 1 `datasource_queries` per source per wording that ran, plus 1 `model_steps` for the ranking and 1 for the choice of sources when they ran, plus the inline fetches priced as `fetch_contents`; a ranking cut by the deadline is not billed. The answer is `201 Created` with `Location` naming the record, `Search`. The record is kept 48 hours after its last call and at most 30 days from its making; `get_search` pages the list the search stored and never searches again or charges. A search answers within `wait_seconds`; what did not finish is named in a `partial` outcome. There is no job, no stream and no webhook.

`POST /v1/search`

## A question searched with the first lead fetched in the same call

The request:

```sh
curl https://api.getclean.ai/v1/search \
  -H "Authorization: Bearer $GETCLEAN_API_KEY" \
  -H "Idempotency-Key: $(uuidgen)" \
  -H "Content-Type: application/json" \
  -d '{"query": "EU AI Act article 50 marking obligations", "published_within_days": 365, "max_candidates": 3, "contents": {"top": 1, "max_characters": 8000}, "max_cost": {"amount": "0.1000", "currency": "USD"}}'
```

The answer:

```http
HTTP/1.1 201 Created
Location: https://api.getclean.ai/v1/search/srch_4HmUunqCCXquleKVCosqFG
Request-Id: req_02ARUKU1YFino5zjD2hYpX
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
      "id": "cand_a1dYqVUaEDEMqh7Qgn8yip",
      "url": "https://eur-lex.example/ai-act",
      "final_url": "https://eur-lex.example/ai-act",
      "title": "Regulation (EU) 2024/1689",
      "language": "en",
      "media_type": "text/html",
      "source_profile": {
        "kind": "state",
        "role": "primary",
        "independence": "unknown",
        "review": {
          "kind": "none",
          "by": null
        }
      },
      "copy_count": 2,
      "language_versions": [],
      "carrier": "web",
      "published_date": "2024-07-12",
      "published_date_basis": "structured_data",
      "published_date_precision": "day",
      "access": {
        "kind": "open",
        "declared_terms": [],
        "robots": "allowed"
      },
      "identifier_matches": [],
      "relevance_score": 0.93,
      "excerpts": [
        {
          "text": "Providers of AI systems … shall ensure …",
          "wording_index": 0,
          "origin": "snippet",
          "truncated": false,
          "section_id": "s4",
          "block_id": "b31"
        }
      ],
      "matches": [
        {
          "wording_index": 0,
          "datasource_id": "web",
          "rank": 1
        }
      ],
      "fetch_cost": {
        "amount": "0.0050",
        "currency": "USD"
      },
      "contents": {
        "id": "cnt_8Lq5XFriyaJ0jEc2oPNx6E",
        "outcome": {
          "kind": "delivered",
          "reason": "sections_only"
        },
        "notices": [],
        "fetched_at": "2026-11-05T09:00:03Z",
        "fingerprint": "sha-256=:Zt4DIioPPcwNH3magrYziAsXB0Fj8m1dwQBKY5IRuzs=:",
        "scope": "main",
        "record_scope": "main",
        "formats": [],
        "truncated": true,
        "counts": {
          "characters": 9500,
          "blocks": {
            "heading": 3,
            "text": 18
          },
          "links": {
            "page": 12
          }
        },
        "sections": [
          {
            "id": "s0",
            "title": null,
            "level": 0,
            "characters": 400,
            "basis": "structure"
          },
          {
            "id": "s4",
            "title": "Article 50",
            "level": 2,
            "characters": 9100,
            "basis": "structure"
          }
        ],
        "source": {
          "url": "https://eur-lex.example/ai-act",
          "final_url": "https://eur-lex.example/ai-act",
          "title": "Regulation (EU) 2024/1689",
          "published_date": "2024-07-12"
        },
        "execution": {
          "version": "1.0.0",
          "configuration": "cfg-2026-11",
          "models": [],
          "elapsed_seconds": 6.2
        },
        "cost": {
          "ceiling": {
            "amount": "0.0100",
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
        "expires_at": "2026-11-07T09:00:03Z"
      }
    },
    {
      "id": "cand_a27BTvL7IEwl2lokVFjz6n",
      "url": "https://commentary.example/ai-act-50",
      "title": "Article 50 AI Act: transparency obligations, a commentary",
      "language": "en",
      "media_type": "text/html",
      "source_profile": {
        "kind": "scholarly_publisher",
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
      "published_date": "2025-02-03",
      "published_date_basis": "meta_tag",
      "published_date_precision": "day",
      "access": {
        "kind": "open",
        "declared_terms": [],
        "robots": "allowed"
      },
      "identifier_matches": [],
      "relevance_score": 0.81,
      "excerpts": [
        {
          "text": "Article 50 requires providers to mark synthetic output in a machine-readable form …",
          "wording_index": 0,
          "origin": "snippet",
          "truncated": false
        }
      ],
      "matches": [
        {
          "wording_index": 0,
          "datasource_id": "web",
          "rank": 2
        }
      ],
      "fetch_cost": {
        "amount": "0.0050",
        "currency": "USD"
      }
    },
    {
      "id": "cand_a3fKWtZ0PhMBOSM78lATqf",
      "url": "https://law-firm.example/briefing",
      "title": "Client briefing: marking obligations under the AI Act",
      "language": "en",
      "media_type": "text/html",
      "source_profile": {
        "kind": "professional_practice",
        "role": "secondary",
        "independence": "unknown",
        "review": {
          "kind": "none",
          "by": null
        }
      },
      "copy_count": 3,
      "language_versions": [],
      "carrier": "web",
      "published_date": "2025-09-15",
      "published_date_basis": "byline",
      "published_date_precision": "day",
      "access": {
        "kind": "open",
        "declared_terms": [],
        "robots": "allowed"
      },
      "identifier_matches": [],
      "relevance_score": 0.64,
      "excerpts": [
        {
          "text": "From 2 August 2026, deployers and providers must …",
          "wording_index": 0,
          "origin": "snippet",
          "truncated": false
        }
      ],
      "matches": [
        {
          "wording_index": 0,
          "datasource_id": "web",
          "rank": 5
        }
      ],
      "fetch_cost": {
        "amount": "0.0050",
        "currency": "USD"
      }
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
  "expires_at": "2026-11-07T09:00:03Z",
  "request_id": "req_02ARUKU1YFino5zjD2hYpX"
}
```

Every rule of `search`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
