#!/usr/bin/env python3
"""ARGUS IV-002 Run004 controlled-fixture verifier.

Checks exact checked-out bytes against frozen Git blob IDs, independently
computes SHA-256, and derives classifications from source fields.
Not a TRACE signature verifier or a production interoperability test.
"""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

SOURCE_REPO = "https://github.com/omwei-org/eabc-external-validation.git"
SOURCE_COMMIT = "a0f6ce4f5d50ad8c1241ea165fb0f8dbcd82a2cf"
ROOT = Path("argus/iv002/run004")
EXPECTED = {
    "E1": "CORRELATED",
    "E2": "UNRESOLVED",
    "E3": "TRACE_INTEGRITY_FAILURE",
    "E4": "EXECUTION_DIVERGENCE",
    "E5": "AUTHORITY_FAILURE",
    "E6": "COMMIT_FAILURE",
}


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\\0" + data).hexdigest()


def load_manifest(root):
    out = {}
    for line in (root / "MANIFEST.sha256").read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        digest, name = line.split(maxsplit=1)
        out[name] = digest
    return out


def classify(eabc, trace, baseline):
    # Validate TRACE's source-internal action-to-receipt relationship
    if trace["action"]["action_ref"] != baseline["action"]["action_ref"] or (
        trace["receipt"]["action_ref"] != trace["action"]["action_ref"]
    ):
        return "TRACE_INTEGRITY_FAILURE"
    # EABC-specific status checks remain distinct from correlation
    if eabc["execution_authority"]["authority_state"] != "VALID":
        return "AUTHORITY_FAILURE"
    if eabc["commit"]["status"] != "COMMITTED" or not eabc["evidence"]["commit_observed"]:
        return "COMMIT_FAILURE"
    if eabc["governed_action"]["payload_digest"] != baseline_eabc_digest or (
        eabc["commit"]["governed_action_digest"] != baseline_eabc_digest
    ):
        return "EXECUTION_DIVERGENCE"
    # The controlled bridge here is a declared common experiment event ID.
    # Matching IDs do not independently establish physical-world event identity.
    if trace["context"]["call_id"] != eabc["shared_event_id"] or (
        trace["receipt"]["linked_call_id"] != eabc["shared_event_id"]
    ):
        return "UNRESOLVED"
    return "CORRELATED"


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("checkout", type=Path, help="Checkout of source repository at frozen commit")
    p.add_argument("--output", type=Path, default=Path("iv002_argus_run004_result.json"))
    args = p.parse_args()
    repo = args.checkout
    actual = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    if actual != SOURCE_COMMIT:
        raise SystemExit(f"Refusing unfrozen checkout: {actual}")
    root = repo / ROOT
    manifest = load_manifest(root)
    integrity = {}
    for name, expected_blob in sorted(manifest.items()):
        data = (repo / name).read_bytes()
        actual_blob = git_blob_sha(data)
        integrity[name] = {"git_blob_sha1": actual_blob, "sha256": hashlib.sha256(data).hexdigest(),
                           "git_blob_match": actual_blob == expected_blob}
    if len(integrity) != 12 or not all(v["git_blob_match"] for v in integrity.values()):
        raise SystemExit("Integrity gate failed: 12 exact Git blob matches required")
    baseline = json.loads((root / "e1/trace.json").read_bytes())
    baseline_eabc = json.loads((root / "e1/eabc.json").read_bytes())
    baseline_eabc_digest = baseline_eabc["governed_action"]["payload_digest"]
    results = {}
    for n in range(1, 7):
        case = f"E{n}"
        eabc = json.loads((root / f"e{n}/eabc.json").read_bytes())
        trace = json.loads((root / f"e{n}/trace.json").read_bytes())
        observed = classify(eabc, trace, baseline)
        results[case] = {"observed": observed, "frozen_expected": EXPECTED[case],
                         "matches": observed == EXPECTED[case]}
    report = {
        "source_repo": SOURCE_REPO, "source_commit": actual,
        "claim_boundary": "Controlled replay classification; no signature, physical-effect, or production proof",
        "integrity": integrity, "results": results,
        "all_matches": all(v["matches"] for v in results.values()),
    }
    args.output.write_text(json.dumps(report, indent=2) + "\\n")
    print(json.dumps({"results": results, "all_matches": report["all_matches"],
                      "output": str(args.output)}, indent=2))
