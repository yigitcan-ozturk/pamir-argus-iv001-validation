# IV-002 Run 004 — ARGUS Source-Fixture Intake Record v0.1

**Date:** 2026-09-26
**Status:** SOURCE FIXTURES LOCATED / INDEPENDENT INGEST NOT YET EXECUTED
**External repository:** `omwei-org/eabc-external-validation`
**Branch:** `experiment/iv002-shared-controlled-event`
**Frozen commit:** `a0f6ce4f5d50ad8c1241ea165fb0f8dbcd82a2cf`
**Fixture root:** `argus/iv002/run004/`

## Provenance boundary

The frozen README states that these are controlled replay fixtures derived from the IV-002 controlled event. They are **not** a recovered copy of the unrecovered public TRACE runtime artifact `call-material-move-001`. TRACE inputs use the public TRACE action-receipt conformance shape; EABC inputs use the controlled IV-002 EABC artifact shape.

A passing ingest over this set can demonstrate reproducibility of the controlled experiment only. It does not establish production TRACE × EABC interoperability or recovery of original runtime provenance.

## Frozen cases and expected classifications

| Case | Controlled perturbation | Frozen expected classification |
|---|---|---|
| E1 | Nominal shared event | CORRELATED |
| E2 | TRACE `call_id` and receipt binding changed | UNRESOLVED |
| E3 | TRACE `action_ref` changed | TRACE_INTEGRITY_FAILURE |
| E4 | EABC governed-action digest changed | EXECUTION_DIVERGENCE |
| E5 | EABC execution authority invalidated | AUTHORITY_FAILURE |
| E6 | EABC commit removed | COMMIT_FAILURE |

Each case contains exactly `eabc.json` and `trace.json`.

## Repository integrity identifiers

The source manifest explicitly records **Git blob SHA-1 identifiers**, not SHA-256 digests. Independent consumers are instructed to compute SHA-256 over exact checked-out bytes before ingestion.

| File | Git blob SHA-1 |
|---|---|
| e1/eabc.json | 647f7c57b0c6fec93e042317f9e8b78520a21351 |
| e1/trace.json | b4c96b8f60eba3c9b0d5cd65d8b6c61ae3f494e5 |
| e2/eabc.json | eb5f5c47a9898e52ec7551b73a3ad4461dbb5229 |
| e2/trace.json | fc53a210b6d1d42b132b1fdd51cb53c6661e2c7b |
| e3/eabc.json | 4bdca839b9ea77d7d06e9019cb8edfc1a2010757 |
| e3/trace.json | 26b5bf45f06d76d60760787e65e689bed09b6ab7 |
| e4/eabc.json | 17d20458edcaf3abdc9b08a3ef6694437a50d395 |
| e4/trace.json | ec82a5c4a49df78d7cc0a57364185528ed947d5a |
| e5/eabc.json | 72e82110f418b485545c918511473cf87344614a |
| e5/trace.json | 71c2916979ef62592182ae4a399af4504e454eb3 |
| e6/eabc.json | 064feff07aa4e51a5a7f45541a394f2365076691 |
| e6/trace.json | 272783cea36745c82876e016307ed5f9d78c1efb |

## Immediate ARGUS observation

The new Run 004 fixture set does **not** match the earlier Discussion-reported semantic matrix exactly. The frozen README at commit `a0f6ce4...` defines:

- E2 as `UNRESOLVED`, not `CORRELATED + EXECUTION_DIVERGENCE`
- E3 as `TRACE_INTEGRITY_FAILURE`, not `UNRESOLVED`
- E4 as `EXECUTION_DIVERGENCE`, not `NOT_CORRELATED`
- E5 as `AUTHORITY_FAILURE`, not `CORRELATED + REJECTED`
- E6 as `COMMIT_FAILURE`, not `INTEGRITY_FAILURE / UNDETERMINED`

This is not treated as an error by ARGUS at intake. It means the newly frozen **Run 004 source-fixture experiment** must be treated as a distinct frozen test set from the earlier reported semantic matrix until Stan confirms whether the classifications were intentionally revised.

## Next gate

1. Compute independent SHA-256 over the 12 exact frozen source files.
2. Build ARGUS source-neutral adapters against these exact bytes.
3. Execute classification without reading the frozen expected-result table as an oracle.
4. Compare observed ARGUS classifications with the frozen README expectations.
5. Record any discrepancy explicitly.
6. Do not claim production interoperability or original public TRACE artifact recovery.
