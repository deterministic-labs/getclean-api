# Versions and releases

## The contract's version

The contract's `info.version` follows semantic versioning. A change that removes or narrows what a client may send or may rely on is a major change, and so is a new member of a request object or of a named object a request carries, since every SDK types those objects closed; a major version lives at its own path, `/v2` beside `/v1`. A new operation, a new answer member, a new value of an open set or a new example is a minor change. A change of wording alone is a patch. A contract element is retired by `deprecated: true`, and its answers carry `Deprecation` and, once a date is set, `Sunset`, before it goes. `CHANGELOG.md` beside this page records every change by date.

Before the service's first release the contract may still tighten a rule the service already enforces, such as a bound stated for the first time or a list that was always refused when empty. Such a change corrects the description and is not a breaking change of the API.

## Each SDK's version

Each official SDK carries its own version, which starts at `0.1.0` and moves to `1.0.0` with the service's first release, and names the contract version it was built against. A minor change of the contract gives every SDK a minor bump. A change in one SDK alone, in its own code, its tests or its documents, gives that SDK a patch bump. The version in a package's metadata, in its repository's tag `v<version>` and in its changelog entry are always the same number, and a version is never reused.

## What a release promises

Every SDK of a release agrees with the contract it was released against: every operation, parameter, member, value and description, measured before the release and not assumed. Every behavior an SDK adds beyond the contract, the retries, the idempotency key, the timeouts, the pagers and the upload's helper, is stated in `spec/SDK-NOTES.md`, with the differences a language's runtime imposes named there. Every SDK release reaches its registry from its repository's release workflow, with provenance.

## Where to look

Each SDK repository under `github.com/deterministic-labs` carries a `CHANGELOG.md` with one entry per version and a GitHub release per tag. A problem with the contract is reported as an issue on this repository; a security concern goes to the address in `SECURITY.md`.
