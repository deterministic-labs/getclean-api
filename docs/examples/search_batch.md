# search_batch

Run 1 to 20 searches in one call, one record each. You get the tally first, then one result per item in input order, each a search record or the problem that skipped it; nothing is atomic, so a skipped item leaves the others standing. Each item carries its own question, wordings, identifiers, country and purpose; every other field of `search` stands once at the top and is shared by every item.

**What it costs.** The key needs `search:run`. The price is the sum of the searches' costs, `units` summed by name. The answer is `200` with `SearchBatch`. The body is at most 4 MiB.

`POST /v1/search:batch`

## One search delivered and one item skipped, the ceiling's remainder below its smallest call

The request:

```sh
curl https://api.getclean.ai/v1/search:batch \
  -H "Authorization: Bearer $GETCLEAN_API_KEY" \
  -H "Idempotency-Key: $(uuidgen)" \
  -H "Content-Type: application/json" \
  -d '{"items": [{"label": "a", "query": "EU AI Act article 50 marking obligations"}, {"label": "b", "query": "EU AI Act article 52 transparency"}], "max_candidates": 3, "max_cost": {"amount": "0.0150", "currency": "USD"}}'
```

The answer:

```http
HTTP/1.1 200 OK
Request-Id: req_02Cibui4kSLfZhLrsUYlO2
Content-Type: application/json

{
  "counts": {
    "delivered": 1,
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
      "search": {
        "id": "srch_5JnMVBRlNJRXAtzF4CVX0F",
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
                "truncated": false
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
          "undated": "shown",
          "safe_search": "moderate",
          "max_per_datasource": 10,
          "ranking_order": "relevance",
          "max_candidates": 3,
          "max_excerpt_characters": 600,
          "max_total_characters": 40000,
          "view": "full",
          "wait_seconds": 10,
          "max_cost": {
            "amount": "0.0150",
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
                "state": "not_applicable"
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
                "amount": "0.0150",
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
          "elapsed_seconds": 7.9
        },
        "cost": {
          "ceiling": {
            "amount": "0.0150",
            "currency": "USD"
          },
          "actual": {
            "amount": "0.0150",
            "currency": "USD"
          },
          "units": {
            "searches": 1,
            "datasource_queries": 1,
            "model_steps": 2
          },
          "replayed": false
        },
        "searched_at": "2026-11-05T09:10:00Z",
        "run_id": "run_default",
        "expires_at": "2026-11-07T09:10:00Z",
        "request_id": "req_02Cibui4kSLfZhLrsUYlO2"
      }
    },
    {
      "index": 1,
      "label": "b",
      "problem": {
        "type": "https://api.getclean.ai/problems/cost-exceeds-cap",
        "title": "The cost cap is below the smallest call",
        "detail": "The remainder of max_cost cannot cover this item's smallest call.",
        "instance": "https://api.getclean.ai/requests/req_02Cibui4kSLfZhLrsUYlO2/items/1",
        "request_id": "req_02Cibui4kSLfZhLrsUYlO2",
        "who_must_act": "caller",
        "retryable": false,
        "minimum_cap": {
          "amount": "0.0110",
          "currency": "USD"
        }
      }
    }
  ],
  "cost": {
    "ceiling": {
      "amount": "0.0150",
      "currency": "USD"
    },
    "actual": {
      "amount": "0.0150",
      "currency": "USD"
    },
    "units": {
      "searches": 1,
      "datasource_queries": 1,
      "model_steps": 2
    },
    "replayed": false
  },
  "request_id": "req_02Cibui4kSLfZhLrsUYlO2"
}
```

Every rule of `search_batch`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).
