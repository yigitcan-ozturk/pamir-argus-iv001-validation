# IV-002 — ARGUS Independent Reproduction Gate v0.1

**Status:** SOURCE-INPUT REPRODUCTION BLOCKED; SEMANTIC RESULT REPORTED BY EABC SIDE  
**Date:** 2026-09-26  
**Scope:** exploratory validation; no changes to frozen PAMIR ARGUS baseline or IV-001 closure.

## External report

In Discussion #3, Stan reported that IV-002 semantic results were frozen at commit `7f05d3ef7628fd6e578305a40e6928ce2b0e59a1` and identified:
- `evidence/iv002-results.json`
- `evidence/iv002-correlation-map.json`
- `tests/test_iv002_correlation_semantics.py`
- `docs/046-iv002-result.md`
- `docs/046-iv002-integration.md`

Reported classifications:
- E1 CORRELATED
- E2 CORRELATED + EXECUTION_DIVERGENCE
- E3 UNRESOLVED
- E4 NOT_CORRELATED
- E5 CORRELATED + REJECTED
- E6 INTEGRITY_FAILURE / UNDETERMINED

**These are external reported results, not an independent ARGUS rerun.**

## Retrieval check

At preparation time, the frozen commit and files could not be resolved in the checked public repositories `omwei-org/eabc-external-validation` and `omwei-org/halos-1.3-atl-analysis`. This does not establish that the commit is nonexistent; its exact repository or branch remains unconfirmed.

Stan also stated that original TRACE and EABC Run 004 evidence bytes were not yet checked into the IV-002 semantic-result repository. Thus byte-for-byte independent source ingestion is not yet possible from the references currently available to ARGUS.

## Separate acceptance gates

**Gate S — semantic reproducibility:** exact repository and immutable commit resolved; freeze files retrieved; independent test execution reproduces E1–E6 semantics. No source-evidence reproduction claim.

**Gate I — evidence-input reproducibility:** original TRACE and EABC Run 004 source bytes + hashes retrieved and checked; controlled cross-domain test bridge separately identified, provenance and integrity checked; ARGUS independently ingests and classifies E1–E6. No production-interoperability claim.

**Gate C — bilateral closure:** both gate records published with source identities, tool versions, execution command, output hashes, exceptions and scoped claim; closure acknowledged.

## Required information from EABC side

1. Exact repository URL and ref containing frozen commit `7f05d3ef7628fd6e578305a40e6928ce2b0e59a1`.
2. Immutable paths/links for E1–E6 semantic files.
3. Original TRACE artifact exact path and cryptographic digest.
4. Original EABC Run 004 evidence exact path and cryptographic digest.
5. Explicit controlled test bridge fixture and its provenance/digest, distinct from either original source.

## Claim discipline

No ARGUS independent reproduction has been performed or asserted by this gate document. Controlled analytical correlation must not be described as production TRACE × EABC interoperability. Source-internal integrity does not itself prove physical effect.

**Next action:** obtain exact semantic-result repository/ref; complete Gate S while Stan traces source artifacts for Gate I.
