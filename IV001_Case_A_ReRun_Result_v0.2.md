# IV-001 — Case A Re-run Result v0.2

**PAMIR ARGUS × EABC External Validation**

Status: **CASE A CORRELATION ESTABLISHED WITHIN THE POC EVIDENCE BOUNDARY**  
Frozen fixture corpus: **v0.2 (unchanged)**  
Additional EABC evidence: **Run 004 / EABC Overlay v0.3**

## Evidence inputs

- Frozen IV-001 v0.2 corpus
- EABC Overlay v0.3
- `halos-1.3-atl-analysis` CI Run 004
- Run 004 artifact digest:
  `sha256:4c4548fb432782392cbc51797f10d45f1874abe9d8e516e9f84aec40c5b133b7`
- Extracted `run-004-evidence.json` digest:
  `sha256:a77c7ceef53e76a71668d6751a3bfd13c8056d52206297eada7f1e6421aab3dd`

The artifact digest and extracted evidence-file digest were independently rechecked during the ARGUS-side review.

## Run 004 observations

### Case A — nominal

`governed_action_digest`:

`d9caaff4f46b50d88ef0d397bb0451f21972602f834cf7383a3796a23ba5fc07`

`committed_action_digest`:

`d9caaff4f46b50d88ef0d397bb0451f21972602f834cf7383a3796a23ba5fc07`

`actuator_payload_digest`:

`d9caaff4f46b50d88ef0d397bb0451f21972602f834cf7383a3796a23ba5fc07`

Observed `applied_payload_digest`:

`d9caaff4f46b50d88ef0d397bb0451f21972602f834cf7383a3796a23ba5fc07`

The `EffectCorrelationEvidence` record is hash-chain linked through `prev_hash` and `record_hash`.

Within the released PoC evidence boundary, the verifier can therefore establish:

**Exact Governed Action → Commit → Actuator Payload → Observed Adapter Effect**

for the Run 004 nominal case.

### Case B — post-gate transformation control

The governed/committed action digest remains:

`d9caaff4f46b50d88ef0d397bb0451f21972602f834cf7383a3796a23ba5fc07`

while the actuator payload digest becomes:

`1bffb64d1d310eaa9f58fd25385989b9ad5befa24fd01675f68b4ae6d04422f2`

and the observed applied-payload digest matches that transformed actuator payload.

This control demonstrates that a post-gate transformation is visible rather than silently collapsing into the nominal evidence path.

## Independent verifier conclusion

The previously open Case A question can now be answered **yes within the PoC evidence boundary**:

> An independent verifier can establish exact Commit → Observed Effect correlation from the combined integrity-protected EABC Run 004 evidence, where “Observed Effect” means the deterministic `RecordingRelay` adapter observation contained in the released evidence chain.

Accordingly, the original Case A result changes from:

**INCONCLUSIVE**

to:

**VALIDATED FOR TESTED TRANSACTION — POC EVIDENCE BOUNDARY**

## Boundary retained

This result does **not** establish independent physical-world attestation.

`RecordingRelay` is an instrumented PoC adapter. The evidence chain establishes cryptographic and semantic continuity from governed action through commit and actuator payload to the recorded adapter observation. It does not independently prove that an external physical-world state is attested by a separate trusted sensor or attestation mechanism.

Therefore:

**Evidence integrity ≠ independent physical-world attestation**

## Effect on IV-001

- Frozen v0.2 fixture corpus: unchanged
- Cases B–F: unchanged
- Case A: re-run completed using the additional EABC Overlay v0.3 / Run 004 evidence
- Remaining boundary: physical-world attestation outside the PoC adapter trust boundary

## Non-claims

This result does not claim:

- production interoperability;
- physical-world attestation;
- security certification;
- regulatory approval;
- deployment readiness;
- general EABC conformance;
- modification of the frozen ARGUS baseline.

---

**Record:** IV-001 Case A Re-run Result v0.2  
**Organisation:** PAMILANGA / PAMIR ARGUS  
**Date:** 2026-09-25
