# CSC-001 — Source-Neutral Evidence Object Mapping v0.1

**Status:** FIRST PASS / EMPIRICAL MAPPING  
**Date:** 2026-09-25  
**Inputs:** AgenTrust public embodied-action `valid-chain.json`; EABC Run 004 public overlay and frozen validation references.  
**Non-claim:** This document does not assert that the TRACE fixture and EABC Run 004 describe the same execution event.

## Mapping rule

ARGUS preserves each source assertion and provenance. It maps evidence into source-neutral relationship classes; it does not translate TRACE semantics into EABC semantics or vice versa.

## Evidence Objects

### EO-T1 — TRACE action assertion
Source fields:
- `trace.trace_id = trace-session-embodied-001`
- `trace.cmcp_call_id = call-material-move-001`
- `action.action_ref = sha256:6572d6707269d815b6f59aadeca709e29a5a7d73330265f2b5feb92d0290b21f`
- `action.action_type = move_material`
- `action.action_scope = robot-cell-7/material-bin-a`
- `action.action_timestamp = 2026-06-25T16:30:00Z`
- `action.agent_id = spiffe://factory.example/agent/material-movement/dev`

ARGUS-neutral classes: execution identity candidate; action identity candidate; context; time; provenance.

### EO-T2 — TRACE receipt sequence
Two signed receipts bind to the same `trace_id`, `call_id`, and `action_ref`.
Observed times: `16:30:01Z`, `16:30:05Z`.
Terminal states: `handoff_accepted`, `controller_completed`.
Receipt chain uses `prev_receipt_hash`.

ARGUS-neutral classes: source-internal relationship; temporal ordering; integrity/provenance; outcome assertion.

Boundary retained: TRACE example documentation states this does not prove physical completion.

### EO-E1 — EABC commit/effect correlation assertion
Run 004 correlation material includes:
`command_id`, `env_id`, `committed_action_digest`, `actuator_payload_digest`, `observation`, `effect_digest`, `effect_status`, `observed_at`, `effect_source`, `prev_hash`, `record_hash`.

Case A command: `run004-a-001`.
The EABC overlay states governed action digest equals actuator payload digest; observation reports the same applied-payload digest; relay state is true; effect status is `OBSERVED`; record is hash-chain linked.

ARGUS-neutral classes: execution identity candidate; action identity candidate; source-internal commit→effect relationship; time; context; integrity/provenance; outcome assertion.

Boundary retained: `RecordingRelay` is an instrumented PoC adapter, not independent physical-world attestation.

## Cross-source relationship matrix

| Relationship | TRACE evidence | EABC evidence | Direct cross-source binding observed? | First-pass status |
|---|---|---|---|---|
| Execution identity | `trace_id`, `cmcp_call_id` | `command_id` | No released binding between `call-material-move-001` and `run004-a-001` observed | MISSING |
| Action identity | TRACE `action_ref` | EABC committed/governed action digest | No released digest-equivalence/binding observed | MISSING |
| Temporal relationship | 2026-06-25 action/receipt times | EABC `observed_at` exists in evidence model | No cross-source temporal binding established by reviewed material | UNESTABLISHED |
| Context | robot-cell/material-bin/agent/controller | `env_id`, effect source, execution context | No shared or independently bound context observed | MISSING |
| Integrity/provenance | signed receipt + receipt chain | append-only SHA-256 evidence chain | Each source has internal integrity material; no cross-source integrity binding observed | SOURCE-INTERNAL ONLY |
| Outcome relationship | controller receipt terminal states | RecordingRelay observation/effect status | No evidence these outcome assertions concern the same event | MISSING |

## First-pass finding

The reviewed public evidence strongly supports **source-internal** relationships on both sides, but it does not yet provide a provable cross-source relationship showing that the TRACE embodied-action fixture and EABC Run 004 Case A refer to the same execution event.

Therefore the currently available evidence must not be classified as `CORRELATED` merely because both source chains are individually valid.

At this gate, the cross-source result is:

> **UNRESOLVED — NO PROVABLE CROSS-SOURCE EVENT BINDING OBSERVED**

This is not an execution failure, TRACE failure, EABC failure, or interoperability failure. It is an evidence-sufficiency result for the specific same-event correlation question.

## Minimum missing material

The smallest candidate bridge appears to require at least:

1. an integrity-protected binding between a TRACE execution/action identity and an EABC command/action identity; and
2. enough context or temporal material to rule out accidental/cross-run identifier association.

Whether both are strictly required is to be tested, not assumed.

A bridge may be an external experimental binding artifact. It need not modify TRACE or EABC schemas, but its provenance and integrity must be inspectable.

## Consequence for the three cases

- **Case A / nominal:** cannot yet be honestly instantiated as CORRELATED from the reviewed released evidence alone.
- **Case B / contradiction:** can be constructed only after the nominal cross-source relationship is established; otherwise a contradiction is not distinguishable from unrelated events.
- **Case C / removed relationship:** likewise depends on first identifying the relationship set that makes Case A sufficient.

## Next experimental gate

Define the smallest source-neutral **Correlation Binding Artifact (CBA)** capable of binding the existing TRACE action to the existing EABC command without changing either source schema.

Then test whether:
- intact CBA → CORRELATED;
- materially contradictory CBA/evidence → NOT CORRELATED;
- required CBA relationship removed → UNRESOLVED.

The CBA must not assert authorization, causality, safety, or physical effect. It may assert only an inspectable relationship between source evidence identities.

---
**PAMILANGA LIMITED — PAMIR ARGUS**  
CSC-001 exploratory validation lane
