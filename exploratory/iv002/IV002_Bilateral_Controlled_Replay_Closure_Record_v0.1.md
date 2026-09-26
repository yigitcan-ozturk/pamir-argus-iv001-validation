# IV-002 — Bilateral Controlled-Replay Closure Record v0.1

**Date:** 2026-09-26  
**Status:** BILATERAL CONTROLLED-REPLAY MILESTONE CLOSED; ORIGINAL RUNTIME PROVENANCE OPEN / NOT ESTABLISHED.

## Bilateral clarification

Stan confirmed in Discussion #3 that Run 004 is a **separate controlled replay fixture suite**, created because the original IV-002 runtime inputs were not recoverable as a complete, independently ingestible artifact set. In particular, the original TRACE-side runtime artifact associated with the earlier `call-material-move-001` reference could not be established.

Accordingly:

1. The Run 004 taxonomy is fixture-specific and does **not** revise or replace the earlier IV-002 semantic matrix.
2. The Run 004 E1–E6 suite was deliberately constructed to exercise independent ingest over nominal and perturbed controlled inputs.
3. ARGUS independently reproduced the frozen Run 004 classifications 6/6.
4. Original IV-002 runtime provenance remains **not established**.
5. No claim is made for original TRACE runtime recovery, native runtime provenance, physical-world effect validation, or production interoperability.

## Frozen Run 004 fixture result

| Case | Frozen Run 004 classification | ARGUS independent result |
|---|---|---|
| E1 | CORRELATED | PASS / CORRELATED |
| E2 | UNRESOLVED | PASS / UNRESOLVED |
| E3 | TRACE_INTEGRITY_FAILURE | PASS / TRACE_INTEGRITY_FAILURE |
| E4 | EXECUTION_DIVERGENCE | PASS / EXECUTION_DIVERGENCE |
| E5 | AUTHORITY_FAILURE | PASS / AUTHORITY_FAILURE |
| E6 | COMMIT_FAILURE | PASS / COMMIT_FAILURE |

**Independent reproduction result: 6/6 PASS.**

## Evidence anchors

- External frozen fixture commit: `a0f6ce4f5d50ad8c1241ea165fb0f8dbcd82a2cf`
- External fixture root: `argus/iv002/run004/`
- ARGUS independent CI run: https://github.com/yigitcan-ozturk/pamir-argus-iv001-validation/actions/runs/36233553477
- ARGUS verifier: `exploratory/iv002/verify_run004.py`
- ARGUS result record: `exploratory/iv002/IV002_Run004_Independent_Controlled_Fixture_Reproduction_v0.1.md`
- Bilateral clarification: omwei-org/eabc-external-validation Discussion #3, Stan comment dated 2026-09-26.

## Closure wording

> ARGUS independently reproduced all six classifications over the frozen IV-002 Run 004 controlled EABC/TRACE replay fixture set. The bilateral parties agree that Run 004 is a separate reconstructed controlled experiment and does not revise the earlier IV-002 semantic matrix. Original IV-002 runtime provenance is not established because the original TRACE runtime artifact could not be recovered. This closure does not establish production interoperability, native runtime provenance, cryptographic authenticity of the original runtime evidence, or independently verified physical-world effects.

## Disposition

**Closed:** controlled Run 004 independent-ingest reproducibility milestone.  
**Open / not established:** original IV-002 runtime provenance and any stronger production/runtime claims.
