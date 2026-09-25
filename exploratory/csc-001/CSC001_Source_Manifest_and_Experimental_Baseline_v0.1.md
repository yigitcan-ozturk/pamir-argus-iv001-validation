# ARGUS Cross-Source Correlation Experiment — CSC-001
## Source Manifest & Experimental Baseline v0.1

**Date:** 2026-09-25  
**Status:** EXPERIMENT PREPARATION — NO RESULT ASSERTED  
**Baseline impact:** None. PAMIR ARGUS frozen baseline and EABC IV-001 remain unchanged.

## Research question

Can ARGUS establish, using source-neutral Evidence Objects, whether independently produced TRACE evidence, EABC authority/commit evidence, and outcome evidence refer to the same execution event without importing TRACE or EABC semantics into the ARGUS core?

Correlation outcomes are limited to:

- **CORRELATED**
- **NOT CORRELATED**
- **UNRESOLVED**

Correlation does not imply causality, authorization, safety, or independently verified physical effect.

## Conceptual boundary

TRACE / EABC / independent observation
→ source-neutral Evidence Objects
→ correlation
→ reconstruction
→ assurance result

Correlation, reconstruction, and assurance remain separate stages.

## Public source A — AgenTrust TRACE embodied-action evidence

Repository: `agentrust-io/examples`  
Path: `embodied-action-receipts/`

The public fixture set provides offline-verifiable embodied-action evidence and explicitly does not claim physical completion, controller safety, or functional-safety certification.

### Candidate fixtures

| Fixture | Git blob SHA | Native expected receipt result | CSC-001 role |
|---|---|---|---|
| `valid-chain.json` | `0adba677261169413a3a424c50fb65139d2f5b1d` | accepted / valid | nominal source evidence |
| `missing-receipt.json` | `ac3bb089fc23eeac9d1cabe75e69a98600d0a462` | missing / invalid | missing-relationship source material |
| `signature-mismatch.json` | `2d463d35f34051bb222398403af547b97ef1db60` | invalid_signature / invalid | integrity contradiction/control material |

### Observed TRACE-side correlation material in valid-chain

- `trace_id = trace-session-embodied-001`
- `cmcp_call_id = call-material-move-001`
- `action_ref = sha256:6572d6707269d815b6f59aadeca709e29a5a7d73330265f2b5feb92d0290b21f`
- `action_timestamp = 2026-06-25T16:30:00Z`
- action scope: `robot-cell-7/material-bin-a`
- agent identity: `spiffe://factory.example/agent/material-movement/dev`
- receipt issuer: `spiffe://factory.example/controller/robot-cell-7`
- receipt observations at `16:30:01Z` and `16:30:05Z`
- receipt sequence and hash-chain relationship
- signed receipt material

These are source assertions. ARGUS does not reinterpret their TRACE semantics.

## Public source B — EABC Run 004

Repository: `omwei-org/halos-1.3-atl-analysis`  
Validated implementation commit: `31d84ba7d911dbf7d2c9d355fe4eb290c537fdf3`

External validation overlay:
`omwei-org/eabc-external-validation/argus/iv001/mapping/EABC_Overlay_v0.3.md`

Run 004 correlation evidence fields include:

- `command_id`
- `env_id`
- `committed_action_digest`
- `actuator_payload_digest`
- `observation`
- `effect_digest`
- `effect_status`
- `observed_at`
- `effect_source`
- `prev_hash`
- `record_hash`

Run 004 artifact SHA-256:
`4c4548fb432782392cbc51797f10d45f1874abe9d8e516e9f84aec40c5b133b7`

Extracted evidence-file SHA-256:
`a77c7ceef53e76a71668d6751a3bfd13c8056d52206297eada7f1e6421aab3dd`

The EABC evidence remains PoC evidence; RecordingRelay is not independent physical-world attestation.

## Important observation before experiment construction

The currently observed TRACE and EABC public fixtures were produced independently and use different native identifiers, action representations, timestamps, and execution contexts.

Therefore CSC-001 must **not manufacture a same-event relationship** merely to force a nominal CORRELATED result.

A cross-source relationship is admissible only if it is supported by released evidence or by an explicitly defined experimental binding artifact whose provenance and integrity are independently inspectable.

If no such binding exists, the correct ARGUS result may be **UNRESOLVED**.

## Candidate relationship classes — not frozen schema

1. Execution/event identity
2. Action identity
3. Temporal relationship
4. Execution/environment context
5. Integrity/provenance binding
6. Outcome/event binding

The experiment will derive the minimum sufficient subset empirically.

## Planned three-case experiment

### CSC-001-A — nominal candidate
Use the strongest available consistent relationship set. Expected by experimental design: `CORRELATED`; however ARGUS must return `UNRESOLVED` if released evidence does not actually establish the required cross-source binding.

### CSC-001-B — material contradiction
Introduce or select one independently observable material contradiction in a required relationship. Expected: `NOT CORRELATED`.

### CSC-001-C — required relationship removed
Remove one relationship shown by Case A to be required for same-event correlation. Expected: `UNRESOLVED`.

No result is frozen until all three cases are instantiated from inspectable evidence.

## Invariants

- Missing evidence is not evidence of failure.
- Integrity of a source record does not establish truth of every source claim.
- Same-event correlation does not establish causality.
- Same-event correlation does not establish authorization.
- Same-event correlation does not establish safety.
- Same-event correlation does not establish physical-world effect.
- Source semantics remain source-owned.
- ARGUS core remains source-neutral.

## Next gate

Before implementing correlation logic, produce a field-level Evidence Object mapping from the selected genuine TRACE fixture and EABC Run 004 evidence, and identify whether an independently verifiable cross-source binding already exists.

If it does not, record the gap rather than inventing one.

---
**PAMILANGA LIMITED — PAMIR ARGUS**  
CSC-001 exploratory validation lane
