# IV-002 Run 004 — Bilateral Review Questions v0.1

**Date:** 2026-09-26  
**Status:** ARGUS controlled-fixture reproduction PASS (6/6); bilateral interpretation and original-source verification OPEN.

ARGUS independent CI run: https://github.com/yigitcan-ozturk/pamir-argus-iv001-validation/actions/runs/36233553477  
ARGUS result record: exploratory/iv002/IV002_Run004_Independent_Controlled_Fixture_Reproduction_v0.1.md  
External fixture commit: a0f6ce4f5d50ad8c1241ea165fb0f8dbcd82a2cf

## Reproduction scope

ARGUS checked out the frozen external fixture commit, matched all 12 file bytes to the manifest's Git blob SHA-1 identifiers, computed independent SHA-256 values and obtained 6/6 expected Run 004 classifications using its own fixture-relative verifier. The machine-readable hash report is available as the CI run artifact.

## Items requiring bilateral confirmation

1. The earlier Discussion semantic matrix (E2 CORRELATED+EXECUTION_DIVERGENCE; E3 UNRESOLVED; E4 NOT_CORRELATED; E5 CORRELATED+REJECTED; E6 INTEGRITY_FAILURE/UNDETERMINED) differs from the newly frozen Run 004 fixture README (E2 UNRESOLVED; E3 TRACE_INTEGRITY_FAILURE; E4 EXECUTION_DIVERGENCE; E5 AUTHORITY_FAILURE; E6 COMMIT_FAILURE). Are these deliberately different experimental suites or was the semantic taxonomy revised?
2. Confirm whether the newly frozen Run 004 source-fixture reproduction can be bilaterally recorded as a **controlled replay milestone**, explicitly separate from the earlier semantic matrix.
3. If further verification is desired, provide exact original runtime source bytes and SHA-256 identities where available. The Run 004 README explicitly says the public TRACE runtime artifact call-material-move-001 has not been recovered. We will not treat controlled fixtures as original runtime evidence.
4. Clarify whether native TRACE signature verification against the provided trusted issuer key is within the intended IV-002 scope. The current ARGUS verifier checks fixture-relative action/receipt references but does not validate Ed25519 signatures.

**Proposed milestone wording:** "ARGUS independently reproduced all six classifications over the frozen IV-002 Run 004 controlled EABC/TRACE replay fixture set. This does not establish original-runtime provenance, native TRACE cryptographic verification, physical-world effects, or production interoperability."

**No bilateral IV-002 closure is asserted by this document.**
