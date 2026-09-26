# ARGUS IV-002 Run 004 — Independent Controlled-Fixture Reproduction v0.1

**Status:** PASS — scoped controlled-fixture reproduction only
**Date:** 2026-09-26
**ARGUS CI run:** https://github.com/yigitcan-ozturk/pamir-argus-iv001-validation/actions/runs/36233553477
**External fixture repository:** omwei-org/eabc-external-validation
**Frozen external source commit:** a0f6ce4f5d50ad8c1241ea165fb0f8dbcd82a2cf
**Fixture root:** argus/iv002/run004/
**Verifier:** exploratory/iv002/verify_run004.py
**Machine-readable output:** GitHub Actions artifact `argus-iv002-run004-report`, artifact ID `10903371564`.

## Executed procedure

ARGUS GitHub Actions checked out the exact external commit, verified the Git blob SHA-1 of all 12 frozen source-fixture files against the external manifest, independently computed SHA-256 for each file, ingested the EABC/TRACE JSON pairs, and derived classifications with the ARGUS verifier. The workflow job and report upload succeeded.

The verifier uses E1 as the controlled reference for action-reference and governed-action-digest perturbation detection. It is **fixture-relative classification**, not full independent cryptographic verification of TRACE signatures or native source runtime provenance.

## Observed vs frozen Run 004 expectations

| Case | ARGUS observed | Frozen expectation | Match |
|---|---|---|---|
| E1 | CORRELATED | CORRELATED | PASS |
| E2 | UNRESOLVED | UNRESOLVED | PASS |
| E3 | TRACE_INTEGRITY_FAILURE | TRACE_INTEGRITY_FAILURE | PASS |
| E4 | EXECUTION_DIVERGENCE | EXECUTION_DIVERGENCE | PASS |
| E5 | AUTHORITY_FAILURE | AUTHORITY_FAILURE | PASS |
| E6 | COMMIT_FAILURE | COMMIT_FAILURE | PASS |

**Result:** 6/6 match for this frozen controlled Run 004 fixture set. Workflow conclusion: success.

## Claim limitations and open questions

1. These controlled replay fixtures are **not** the recovered original public TRACE runtime artifact `call-material-move-001`. This run does not demonstrate original-runtime byte-for-byte reproduction.
2. The current verifier validates repository-file identity and computes SHA-256; it does **not** cryptographically verify TRACE Ed25519 receipt signatures or independently attest physical effect.
3. The controlled fixture bridge uses the declared experiment shared-event identifier. Matching this identifier within a deliberately controlled fixture does not establish production cross-system correlation without a separately verifiable bridge.
4. The earlier Discussion-reported IV-002 semantic matrix has different E2–E6 outcomes from this newly frozen Run 004 fixture set. The two result sets must not be conflated; request Stan's confirmation of their intended relationship.
5. Frozen source `MANIFEST.sha256` contains Git blob SHA-1 values (as explicitly stated in its README), not precomputed SHA-256 values. Independently computed SHA-256 values are preserved in the CI artifact.

**Disposition:** controlled-fixture reproduction PASS; original-source provenance, native signature verification, and bilateral IV-002 closure remain OPEN.
