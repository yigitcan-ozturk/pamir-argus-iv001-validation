# CSC-001 — Correlation Binding Artifact (CBA) Contract v0.1

**Status:** EXPERIMENTAL CONTRACT — NOT A TRACE OR EABC SCHEMA  
**Date:** 2026-09-25  
**Scope:** CSC-001 only  
**Baseline impact:** None. PAMIR ARGUS frozen baseline, EABC IV-001, TRACE and EABC source schemas remain unchanged.

## Purpose

The Correlation Binding Artifact (CBA) is a source-neutral, independently inspectable evidence object whose only purpose is to assert a candidate relationship between already-existing evidence produced by independent sources.

It exists because the reviewed public TRACE embodied-action fixture and EABC Run 004 evidence contain strong source-internal bindings but no observed released cross-source binding proving that they refer to the same execution event.

The CBA does **not** make the relationship true merely by asserting it. ARGUS evaluates the CBA together with referenced source evidence.

## Non-authority boundary

A CBA MUST NOT be interpreted as evidence that:

- an action was authorized;
- an action was safe;
- an action caused an observed effect;
- a physical-world effect occurred;
- either source's native semantics are equivalent;
- a source assertion is true merely because it is signed or hashed.

Its claim is narrower:

> The issuer asserts that the specifically referenced source evidence objects are candidates for the same execution event, under the stated relationship material.

## Minimal experimental representation

```json
{
  "type": "argus.correlation_binding.v0",
  "binding_id": "<unique binding identifier>",
  "issued_at": "<timestamp>",
  "issuer": {
    "id": "<issuer identity>",
    "role": "experimental-correlation-binder"
  },
  "subjects": [
    {
      "source": "TRACE",
      "evidence_locator": "<stable source locator>",
      "evidence_digest": "<digest of exact referenced evidence>",
      "execution_ref": "<source-owned execution/call reference>",
      "action_ref": "<source-owned action reference>"
    },
    {
      "source": "EABC",
      "evidence_locator": "<stable source locator>",
      "evidence_digest": "<digest of exact referenced evidence>",
      "execution_ref": "<source-owned command/execution reference>",
      "action_ref": "<source-owned committed/governed action reference>"
    }
  ],
  "relationship": {
    "claim": "same_execution_event_candidate",
    "context_binding": "<optional independently checkable context material>",
    "temporal_binding": "<optional independently checkable temporal material>"
  },
  "integrity": {
    "algorithm": "sha256",
    "payload_digest": "<canonical CBA payload digest>"
  }
}
```

This is an experimental representation, not a canonical ARGUS serialized schema.

## Required vs candidate material

### Required for the CBA itself

1. Stable identity for the binding artifact.
2. Exact locator and digest for each referenced source evidence object.
3. Source-owned execution/action references copied without semantic reinterpretation.
4. Explicit relationship claim limited to same-event candidacy.
5. Issuer/provenance information.
6. Integrity protection over the binding payload.

### Candidate sufficiency material to test

- context binding;
- temporal binding;
- additional independent witness/issuer;
- stronger cryptographic signature over the CBA.

CSC-001 will determine experimentally which relationship material is required for ARGUS to reach a same-event correlation result. It is not frozen in advance.

## Verifier contract

The CSC-001 verifier MUST evaluate evidence in this order:

### 1. Reference resolution
Resolve each CBA subject to the exact evidence object identified by locator and digest.

Failure modes:
- object absent → `UNRESOLVED`
- digest cannot be verified → `UNRESOLVED`
- digest positively mismatches referenced object → `NOT CORRELATED`

### 2. Source assertion extraction
Extract only the source-neutral relationship material needed for correlation:
- execution/event identity candidate;
- action identity candidate;
- time;
- context;
- integrity/provenance;
- outcome/event reference where applicable.

Native source meanings remain attached as provenance and are not translated into each other.

### 3. Relationship consistency
Evaluate whether the CBA claim is consistent with the exact referenced evidence.

A positive material contradiction in a relationship required for same-event identity produces `NOT CORRELATED`.

Absence of a required relationship produces `UNRESOLVED`.

### 4. Sufficiency
Only if the evidence set contains the empirically required relationship material and no material contradiction may the verifier return `CORRELATED`.

## Result object

```json
{
  "experiment": "CSC-001",
  "result": "CORRELATED | NOT_CORRELATED | UNRESOLVED",
  "supported_claim": "same_execution_event",
  "relationships": [
    {
      "class": "<relationship class>",
      "status": "SUPPORTED | CONTRADICTED | MISSING | UNESTABLISHED",
      "evidence_refs": ["<evidence references>"]
    }
  ],
  "non_claims": [
    "causality",
    "authorization",
    "safety",
    "independent_physical_effect"
  ]
}
```

## Three-case construction

### CSC-001-A — intact binding

CBA references exact TRACE and EABC evidence objects and contains the minimum relationship material eventually shown sufficient.

Target experimental outcome: `CORRELATED`.

This outcome is permitted only after the verifier can independently resolve the referenced evidence and validate the relationship material. The target is not pre-assigned as the observed result.

### CSC-001-B — material contradiction

Starting from the sufficient Case A set, introduce one controlled contradiction in a required relationship while preserving the rest of the evidence.

Target experimental outcome: `NOT_CORRELATED`.

The contradiction must be explicit and detectable; it must not merely remove evidence.

### CSC-001-C — required relationship removed

Starting from the sufficient Case A set, remove one relationship shown to be necessary while leaving no positive contradiction.

Target experimental outcome: `UNRESOLVED`.

This distinguishes absence of evidence from contradictory evidence.

## Anti-circularity requirement

The CBA must not become a self-authenticating statement whose presence alone causes `CORRELATED`.

At least one relationship used for the result must be independently checkable against the referenced source evidence. A CBA that simply states “these are the same event” without inspectable binding material is insufficient and yields `UNRESOLVED`.

## Current evidence implication

The current public TRACE fixture and EABC Run 004 evidence, without a CBA or another independently verifiable bridge, remain:

> **UNRESOLVED — NO PROVABLE CROSS-SOURCE EVENT BINDING OBSERVED**

CSC-001 therefore tests the minimum additional evidence needed to change that result, rather than rewriting either source.

## Next gate

Instantiate **CBA Fixture v0.1** against the exact public TRACE `valid-chain.json` and EABC Run 004 references.

Before assigning Case A as `CORRELATED`, define which CBA relationship material is independently verifiable rather than asserted solely by the binder.

---
**PAMILANGA LIMITED — PAMIR ARGUS**  
CSC-001 exploratory validation lane
