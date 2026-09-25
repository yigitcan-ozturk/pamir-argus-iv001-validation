# PAMIR ARGUS — Evaluation Kit v0.1
## External Validation Addendum / Cover Note

**Addendum ID:** ARGUS-EK-ADD-EABC-IV001-v1.0
**Date:** 2026-09-25
**Applies to:** PAMIR ARGUS Evaluation Kit v0.1 — ODTU Controlled Release
**Baseline status:** Evaluation Kit v0.1 remains unchanged.

## Purpose
This addendum records external validation evidence produced after the controlled Evaluation Kit v0.1 release. It is a companion record and does not alter, replace, or retrospectively modify the original Evaluation Kit.

## External validation completed
PAMIR ARGUS completed EABC IV-001, a bilateral external interoperability-validation exercise using a frozen public fixture corpus and externally released EABC evidence.

The exercise tested whether an independent verifier could preserve and verify:
**Authorization ≠ Execution ≠ Evidence ≠ Exact Effect Correlation**

Tested path:
**Governed Action → Authorization → Commit → Actuator Payload → Observed Adapter Effect → ARGUS Independent Verification**

## Final result
**VALIDATED FOR TESTED TRANSACTION — POC EVIDENCE BOUNDARY**

The initial nominal verification was **INCONCLUSIVE** because exact integrity-protected Commit → Observed Effect correlation was not established.

After EABC released additional Run 004 effect-correlation evidence, ARGUS repeated Case A against the **same frozen v0.2 corpus**.

For the tested nominal transaction, the combined evidence established matching governed-action, committed-action, actuator-payload and observed applied-payload digests.

A negative post-gate transformation control produced a digest mismatch and exposed the transformed actuator payload in the evidence chain.

## Why this matters for evaluation
The result provides external evidence that ARGUS can:
- consume evidence released by an external authority/execution-boundary implementation;
- distinguish authorization, execution, evidence integrity and effect correlation;
- return **INCONCLUSIVE** when evidence is insufficient;
- identify the specific missing evidence boundary;
- repeat verification against a frozen corpus after new evidence becomes available;
- distinguish a nominal path from a post-gate transformation;
- produce a reproducible, scope-limited verifier conclusion.

## Validation records
ARGUS public IV-001 validation repository:
https://github.com/yigitcan-ozturk/pamir-argus-iv001-validation

Recommended evaluator records:
1. ARGUS External Validation Record — EABC IV-001 v1.0
2. IV-001 Case A Re-run Result v0.2
3. IV-001 Bilateral Closure Record v1.0
4. Institutional Independent External Validation Brief v1.0

External EABC validation evidence:
https://github.com/omwei-org/eabc-external-validation

External implementation evidence:
https://github.com/omwei-org/halos-1.3-atl-analysis

## Assurance boundary
IV-001 validates the tested transaction only within the **PoC adapter evidence boundary**.

The observed effect is an instrumented RecordingRelay adapter observation. It is not independent physical-world attestation.

This addendum therefore does not claim:
- independent physical-world effect attestation;
- production interoperability;
- production deployment readiness;
- security certification;
- regulatory approval;
- general EABC conformance;
- universal ARGUS interoperability.

## Evaluator guidance
Evaluation Kit v0.1 should continue to be evaluated as originally released.

Use this addendum only as subsequent external evidence of ARGUS verifier behavior and interoperability-validation at the stated PoC boundary.

The external validation does not modify the frozen ARGUS baseline or the controlled Evaluation Kit.

---
**PAMILANGA LIMITED**
**PAMIR ARGUS — Evidence & Assurance Infrastructure for Autonomous Defence Systems**
External Validation Addendum to Evaluation Kit v0.1
