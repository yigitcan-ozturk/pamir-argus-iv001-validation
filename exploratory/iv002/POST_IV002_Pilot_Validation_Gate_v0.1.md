# PAMIR ARGUS — Post-IV-002 Pilot Validation Gate v0.1

**Date:** 2026-09-26  
**Status:** Proposed next-stage protocol; no pilot contracted or executed  
**Isolation:** Do not modify frozen PAMIR v0.1, frozen PAMIR-CUAS, existing ARGUS baseline, IV-001 closure or IV-002 records.

## 1. Verified starting point

IV-001: bilaterally closed within its documented PoC evidence boundary.

IV-002 Run 004: ARGUS independently reproduced all six classifications from a separate, frozen, controlled EABC/TRACE replay fixture suite. Source commit: `a0f6ce4f5d50ad8c1241ea165fb0f8dbcd82a2cf`. ARGUS CI run: https://github.com/yigitcan-ozturk/pamir-argus-iv001-validation/actions/runs/36233553477 . Stan clarified that this is a separate controlled experiment, not a revision of the earlier IV-002 semantic matrix.

**Not established:** original IV-002 TRACE runtime provenance (original artifact unrecovered), original-runtime byte-for-byte reproduction, production interoperability, independent physical-world effect attestation, or certification.

## 2. Proposed pilot hypothesis

Can an independent ARGUS evidence layer ingest native, time-stamped records from a partner's existing autonomous-system test environment, preserve source provenance, distinguish correlation from execution state, and produce reproducible incident classifications without controlling the underlying system?

This is a hypothesis to test, not a validated capability claim.

## 3. Minimum partner input package

- A bounded, non-sensitive test scenario and explicit permitted use.
- Native source records from at least two distinct system boundaries (e.g., decision/controller and execution/observation), with schema/version and collection method.
- Event timestamps, clock-domain and synchronization metadata, known delays or uncertainty.
- Native record identifiers and cryptographic hashes of the delivered bytes; independently verifiable bridge evidence where available.
- Ground-truth annotation method and partner reviewer, including explicitly unknown outcomes.
- Written agreement on data handling, redaction, retention, publication permissions and test ownership.

No assumption of common IDs, identical action semantics, native cryptographic signatures, or independently verified physical effects.

## 4. Acceptance protocol (proposed)

**Gate P0 — data rights and provenance:** permitted source records and their original byte hashes obtained, versioned and verified.

**Gate P1 — ingest and preservation:** independent ingestion with a documented source-to-Evidence-Object mapping; no silent source-semantic rewriting; source hashes and missing fields recorded.

**Gate P2 — controlled incident matrix:** jointly approve nominal, missing-binding, contradiction, integrity failure, authority/commit divergence and temporal-uncertainty scenarios that the supplied data can actually support. Unsupported scenarios are marked NOT TESTABLE, not PASS.

**Gate P3 — independent rerun:** a separate reviewer repeats the pinned code/data execution, compares classifications and checks hashes. Report per-case observed result, expected ground truth, exceptions and disagreements.

**Gate P4 — scoped closure:** joint sign-off only on demonstrated results, with explicit unresolved provenance and physical-effect boundaries.

## 5. Suggested measurable outputs

- Source-file inventory with SHA-256 and provenance.
- Versioned source-neutral Evidence Object mapping.
- Per-case decision trace and first-divergence record where evidence supports one.
- Classification agreement against independently supplied ground truth (counts, not invented targets).
- Reproduction instructions, pinned dependencies, CI/test logs and exceptions.
- Partner-facing Evidence Pack and restricted technical annex.

**Targets, timeline, price and sample sizes:** TBC with the partner; not yet agreed.

## 6. Commercial positioning boundary

Offer a scoped **paid validation pilot** only after partner data availability and procurement fit are confirmed. Describe IV-002 accurately as an independent controlled-fixture reproduction milestone. Do not imply Stan/omwei-org endorsement of a commercial offer or a signed partnership.

## 7. Immediate next actions

1. Prepare a two-page partner-facing validation brief using only verified IV-001/IV-002 claims.
2. Select a candidate pilot environment with legally shareable native records and explicit ground truth.
3. Ask the partner for a short technical discovery meeting and data feasibility check.
4. Keep all pilot-specific work in a separate lane; do not alter frozen artifacts.
