# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml==6.0.3"]
# ///
"""Write one page per operation under docs/examples from the contract's own examples.

Run from the repository's root:  uv run tools/example_pages.py

Each page opens with what the operation does and what it costs, in the contract's own words, then
shows every example the contract carries for it: the request as a curl command and the answer with
its status and headers, pretty-printed. The pages are generated, never edited by hand, so they say
exactly what the contract says; run this after every change of spec/openapi.yaml.
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONTRACT = ROOT / "spec" / "openapi.yaml"
OUT = ROOT / "docs" / "examples"
SERVER = "https://api.getclean.ai"
REASON = {
    200: "OK",
    201: "Created",
    202: "Accepted",
    204: "No Content",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    409: "Conflict",
    410: "Gone",
    413: "Content Too Large",
    415: "Unsupported Media Type",
    422: "Unprocessable Content",
    429: "Too Many Requests",
    451: "Unavailable For Legal Reasons",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
}
JSON_PARTS = {"json_schema", "max_cost", "max_source_price", "metadata"}


def load() -> dict:
    """Read the contract."""
    with CONTRACT.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def purpose(description: str) -> str:
    """The paragraphs of an operation's description up to and including the one that says what it costs."""
    kept: list[str] = []
    for paragraph in description.split("\n\n"):
        kept.append(paragraph.strip())
        if paragraph.startswith(("**What it costs.**", "**Scope and price.**")):
            break
    return "\n\n".join(kept)


def first_sentence(description: str) -> str:
    """The first sentence of a description, for the index."""
    head = description.split("\n\n", 1)[0]
    for mark in (". ", ": "):
        if mark in head:
            return head.split(mark, 1)[0] + "."
    return head


def header_names(doc: dict, operation: dict) -> set[str]:
    """The names of the header parameter components an operation references."""
    names: set[str] = set()
    for parameter in operation.get("parameters", []):
        if "$ref" in parameter:
            names.add(parameter["$ref"].rsplit("/", 1)[-1])
    return names


def path_with_examples(path: str, operation: dict) -> str:
    """The path with every path parameter replaced by its example."""
    for parameter in operation.get("parameters", []):
        if parameter.get("in") == "path":
            path = path.replace(
                "{" + parameter["name"] + "}", str(parameter["example"])
            )
    return path


def shell_single(text: str) -> str:
    """Quote a string for a single-quoted shell argument."""
    return "'" + text.replace("'", "'\"'\"'") + "'"


def query_with_examples(doc: dict, operation: dict) -> str:
    """The query string of the parameters that carry an example, so the sample asks what its answer shows."""
    pairs = []
    for parameter in operation.get("parameters", []):
        if "$ref" in parameter:
            parameter = doc["components"]["parameters"][
                parameter["$ref"].split("/")[-1]
            ]
        if parameter.get("in") != "query":
            continue
        value = parameter.get(
            "example", parameter["examples"][0] if parameter.get("examples") else None
        )
        if value is None:
            value = parameter.get("schema", {}).get("example")
        if value is None:
            continue
        values = value if isinstance(value, list) else [value]
        pairs += [f"{parameter['name']}={v}" for v in values]
    return "?" + "&".join(pairs) if pairs else ""


def curl(
    doc: dict,
    oid: str,
    method: str,
    path: str,
    operation: dict,
    media: str | None,
    value,
    example_name: str | None = None,
) -> str:
    """The request as a curl command."""
    lines = [
        f"curl {SERVER}{path_with_examples(path, operation)}{query_with_examples(doc, operation)}"
    ]
    if method != "get" and value is None:
        lines.append(f"  -X {method.upper()}")
    lines.append('  -H "Authorization: Bearer $GETCLEAN_API_KEY"')
    if header_names(doc, operation) & {"IdempotencyKey", "IdempotencyKeyRequired"}:
        # A copied sample must never replay another body's key, so the page shows a fresh key made at the shell.
        lines.append('  -H "Idempotency-Key: $(uuidgen)"')
    if media == "application/json" and value is not None:
        lines.append('  -H "Content-Type: application/json"')
        lines.append("  -d " + shell_single(json.dumps(value, ensure_ascii=False)))
    elif media == "multipart/form-data" and value is not None:
        for name, part in value.items():
            if name == "document":
                lines.append(f'  -F "document=@{part};type=application/octet-stream"')
            elif name in JSON_PARTS:
                lines.append(
                    "  -F "
                    + shell_single(
                        f"{name}={json.dumps(part, ensure_ascii=False)};type=application/json"
                    )
                )
            elif isinstance(part, list):
                lines.extend(f'  -F "{name}={item}"' for item in part)
            else:
                lines.append(
                    f'  -F "{name}={json.dumps(part) if isinstance(part, bool) else part}"'
                )
    return " \\\n".join(lines)


def answer_headers(status: int, response: dict, body) -> list[str]:
    """The status line and the headers an answer example carries that a reader acts on."""
    lines = [f"HTTP/1.1 {status} {REASON[status]}"]
    declared = response.get("headers", {})
    if "Location" in declared and isinstance(body, dict):
        record = body.get("contents") or body.get("job") or body
        rid = record.get("id", "")
        where = {"cnt_": "/v1/contents/", "srch_": "/v1/search/", "job_": "/v1/jobs/"}
        for prefix, base in where.items():
            if rid.startswith(prefix):
                lines.append(f"Location: {SERVER}{base}{rid}")
    if "Retry-After" in declared and isinstance(body, dict):
        job = body.get("job") or body
        if isinstance(job, dict) and "retry_after_seconds" in job:
            lines.append(f"Retry-After: {job['retry_after_seconds']}")
    if isinstance(body, dict) and "request_id" in body:
        lines.append(f"Request-Id: {body['request_id']}")
    if body is not None:
        kind = "application/problem+json" if status >= 400 else "application/json"
        lines.append(f"Content-Type: {kind}")
    return lines


def problem_examples(doc: dict, oid: str) -> list[tuple[int, dict]]:
    """The problem examples the shared responses carry for one operation, with their status."""
    found: list[tuple[int, dict]] = []
    for name, response in doc["components"]["responses"].items():
        status = int(name.removeprefix("Problem"))
        examples = (
            response.get("content", {})
            .get("application/problem+json", {})
            .get("examples", {})
        )
        for key, example in examples.items():
            if key.startswith(oid + "."):
                found.append((status, example))
    return found


def page(doc: dict, method: str, path: str, operation: dict) -> str:
    """One operation's page."""
    oid = operation["operationId"]
    out = [
        f"# {oid}",
        "",
        purpose(operation["description"]),
        "",
        f"`{method.upper()} {path}`",
        "",
    ]
    body = operation.get("requestBody", {}).get("content", {})
    media, requests = None, {}
    for kind, content in body.items():
        media, requests = kind, content.get("examples", {})
    shown = 0
    for status_text, response in operation["responses"].items():
        if "$ref" in response:
            continue
        status = int(status_text)
        examples = (
            response.get("content", {}).get("application/json", {}).get("examples", {})
        )
        if not examples and status == 204:
            out += [
                "## The request",
                "",
                "```sh",
                curl(doc, oid, method, path, operation, None, None),
                "```",
                "",
                "## The answer",
                "",
                "```http",
                *answer_headers(status, response, None),
                "```",
                "",
            ]
            shown += 1
        for label, example in examples.items():
            request = requests.get(label, {})
            out += [f"## {example['summary']}", ""]
            out += [
                "The request:",
                "",
                "```sh",
                curl(
                    doc,
                    oid,
                    method,
                    path,
                    operation,
                    media,
                    request.get("value"),
                    label,
                ),
                "```",
                "",
                "The answer:",
                "",
                "```http",
                *answer_headers(status, response, example["value"]),
                "",
                json.dumps(example["value"], indent=2, ensure_ascii=False),
                "```",
                "",
            ]
            shown += 1
    for status, example in problem_examples(doc, oid):
        out += [
            f"## {example['summary']}",
            "",
            "The answer:",
            "",
            "```http",
            *answer_headers(status, {}, example["value"]),
            "",
            json.dumps(example["value"], indent=2, ensure_ascii=False),
            "```",
            "",
        ]
    out += [
        f"Every rule of `{oid}`, its refusals, its notices and its problem types, stands in its description in the contract, [`spec/openapi.yaml`](../../spec/openapi.yaml). The other operations are listed in [the index](README.md).",
        "",
    ]
    return "\n".join(out)


def main() -> None:
    """Write every page and the index."""
    doc = load()
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.md"):
        old.unlink()
    rows = []
    for path, item in doc["paths"].items():
        for method, operation in item.items():
            if method not in {"get", "post", "put", "patch", "delete"}:
                continue
            oid = operation["operationId"]
            (OUT / f"{oid}.md").write_text(
                page(doc, method, path, operation), encoding="utf-8"
            )
            rows.append(
                f"| [`{oid}`]({oid}.md) | `{method.upper()} {path}` | {first_sentence(operation['description'])} |"
            )
    index = [
        "# Examples, one page per operation",
        "",
        "Each page shows what the operation does and what it costs, in the contract's own words, then every example the contract carries for it: the request as a curl command and the answer with its status and headers. The pages are written by `tools/example_pages.py` from `spec/openapi.yaml` and change only when the contract does.",
        "",
        "| Operation | Call | What it does |",
        "|---|---|---|",
        *rows,
        "",
    ]
    (OUT / "README.md").write_text("\n".join(index), encoding="utf-8")
    print(f"wrote {len(rows)} pages and the index into {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
