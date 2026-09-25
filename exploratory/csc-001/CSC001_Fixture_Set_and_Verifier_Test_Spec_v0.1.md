# CSC-001 — Fixture Set & Verifier Test Specification v0.1

**Status:** PRE-IMPLEMENTATION / CONTROLLED TEST DESIGN  
**Date:** 2026-09-25

## Current candidate fixture

`fixtures/cba-candidate-unresolved-v0.1.json` captures the exact state of the reviewed public evidence without inventing a bridge.

Expected result:

> **UNRESOLVED**

Reason: both sources can be individually resolved, but no independently verifiable evidence currently binds the TRACE execution/action references to EABC Run 004 Case A.

## Why Case A is not fabricated

The three-case design requires a nominal `CORRELATED` case, but creating a CBA that merely declares the two historical public fixtures to be the same event would make the experiment circular.

Therefore the nominal fixture remains **BLOCKED ON BINDING EVIDENCE** until one of the following exists:

- a pre-existing public artifact that independently binds the exact TRACE and EABC evidence identities; or
- a new controlled experiment in which both systems intentionally emit evidence for one shared test event and the cross-source relationship is observable independently of ARGUS.

The second option is methodologically stronger because it avoids retroactively asserting that unrelated historical fixtures describe one event.

## Verifier acceptance tests

| Test | Input condition | Required result |
|---|---|---|
| T0 | current candidate; source evidence present but no cross-source binding | `UNRESOLVED` |
| T1 | exact source refs + independently checkable sufficient binding; no contradiction | `CORRELATED` |
| T2 | T1 plus positive contradiction in a required relationship | `NOT_CORRELATED` |
| T3 | T1 with one required relationship removed and no contradiction | `UNRESOLVED` |
| T4 | referenced evidence absent/unresolvable | `UNRESOLVED` |
| T5 | referenced evidence positively fails its declared digest identity | `NOT_CORRELATED` |

## Determinism requirement

For a fixed fixture set and fixed source evidence bytes, repeated verifier runs must produce the same classification and relationship-status record.

## Source-neutrality requirement

The core correlation decision must operate on normalized relationship classes, not on rules such as “if TRACE field X equals EABC field Y then pass.”

Source adapters may extract native fields. The core receives only:
- evidence identity/provenance;
- execution/action identity candidates;
- time relationships;
- context relationships;
- integrity status;
- outcome/event references;
- explicit binding evidence.

## Result discipline

The verifier must preserve the distinction:

- contradiction → `NOT_CORRELATED`
- insufficiency/absence → `UNRESOLVED`
- sufficient consistent binding → `CORRELATED`

No default-to-pass behavior is permitted.

## Decision for next implementation step

Do **not** manufacture the nominal case from the two unrelated historical fixtures.

The next valid path is to define a tiny shared-event fixture protocol that Stan/EABC can execute against one genuine TRACE action chain, or identify an already-public bridge artifact if one exists.

Until that gate is satisfied, CSC-001 has already produced a meaningful assurance result: current historical evidence is insufficient for cross-source same-event correlation.

---
**PAMILANGA LIMITED — PAMIR ARGUS**
