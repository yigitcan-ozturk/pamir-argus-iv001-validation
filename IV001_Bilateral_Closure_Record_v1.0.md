# IV-001 — Bilateral Closure Record v1.0

**PAMIR ARGUS × EABC External Validation**

**Status:** CLOSED — VALIDATED FOR TESTED TRANSACTION — POC EVIDENCE BOUNDARY  
**Date:** 2026-09-25

## Scope

IV-001 tested whether an independent verifier could establish the evidence path from a governed action through authorization and commit to an observed downstream effect, without collapsing authorization, execution, evidence, and effect correlation into a single success claim.

The PAMIR ARGUS frozen baseline was not modified. The IV-001 v0.2 fixture corpus remained frozen during the final Case A re-run.

## Validation progression

1. v0.2 fixture corpus frozen.
2. ARGUS independent verification completed.
3. Initial Case A result remained INCONCLUSIVE because exact integrity-protected Commit → Observed Effect correlation was not established.
4. EABC supplied Run 004 / EABC Overlay v0.3 as additional integrity-protected evidence.
5. ARGUS re-ran Case A against the same frozen v0.2 corpus.
6. The nominal transaction established matching governed-action, committed-action, actuator-payload, and observed applied-payload digests within the PoC evidence boundary.
7. The negative post-gate transformation control exposed a digest mismatch between the committed governed action and transformed actuator payload.

## Final tested result

**VALIDATED FOR TESTED TRANSACTION — POC EVIDENCE BOUNDARY**

Within the released PoC evidence boundary, the combined evidence is sufficient for an independent verifier to establish:

**Exact Governed Action → Authorization → Commit → Actuator Payload → Observed Adapter Effect**

The negative transformation control demonstrates that a post-gate transformation is visible in the evidence rather than being silently treated as the nominal path.

## Preserved semantic distinctions

**Authorization ≠ Execution ≠ Evidence ≠ Exact Effect Correlation**

The validation result does not weaken these distinctions. Instead, IV-001 demonstrates the additional evidence required to move from authorization/commit evidence to a verifiable effect-correlation statement.

## Remaining boundary

The observed effect is produced by the instrumented `RecordingRelay` PoC adapter.

Accordingly, IV-001 does **not** establish independent physical-world effect attestation.

The remaining assurance question is outside the closed IV-001 scope:

> What independent instrumentation and integrity-protected evidence would be required to extend the evidence boundary from adapter-level observation to independently attested physical-world effect?

Any such work should be treated as a separate validation scope rather than changing the frozen IV-001 corpus or its final result.

## Evidence references

- Frozen fixture corpus: IV-001 v0.2
- EABC evidence overlay: `EABC_Overlay_v0.3.md`
- EABC implementation source: `omwei-org/halos-1.3-atl-analysis`
- CI Run 004: `36097144900`
- Run 004 artifact SHA-256:
  `4c4548fb432782392cbc51797f10d45f1874abe9d8e516e9f84aec40c5b133b7`
- Extracted `run-004-evidence.json` SHA-256:
  `a77c7ceef53e76a71668d6751a3bfd13c8056d52206297eada7f1e6421aab3dd`
- ARGUS Case A re-run record: `IV001_Case_A_ReRun_Result_v0.2.md`

## Non-claims

This closure does not claim:

- independent physical-world attestation;
- production interoperability;
- production deployment;
- security certification;
- regulatory approval;
- general EABC conformance;
- modification of the frozen PAMIR ARGUS baseline.

## Closure

The tested IV-001 transaction evidence path is complete at the PoC adapter boundary. No further IV-001 implementation change is required for this result.

A physical-world attestation experiment, if pursued, should be opened as a separate validation lane with its own evidence model, fixtures, acceptance criteria, and non-claims.

---

**Organisation:** PAMILANGA / PAMIR ARGUS  
**Record:** IV-001 Bilateral Closure Record v1.0
