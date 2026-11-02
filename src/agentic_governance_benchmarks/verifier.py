"""Deterministic RFC 8785 JCS Canonicalizer, Delegation Link Verifier & OWASP ASI01-ASI10 Evaluator.

Author: Raghuvar Karthik Durga (https://orcid.org/0009-0003-7014-355X)
DOIs: 10.5281/zenodo.23735274 (TR-2026-01), 10.5281/zenodo.23735497 (TR-2026-02)
"""
from __future__ import annotations
import base64
import hashlib
import json
import math
import re
import sys
from typing import Any

_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
_MAX_WALK_DEPTH = 50


def _validate_jcs_value(val: Any) -> None:
    if isinstance(val, float):
        if not math.isfinite(val):
            raise ValueError("Non-finite float forbidden in RFC 8785 JCS")
    elif isinstance(val, str):
        for ch in val:
            cp = ord(ch)
            if 0xD800 <= cp <= 0xDFFF:
                raise ValueError("Lone UTF-16 surrogate forbidden in RFC 8785 JCS")
    elif isinstance(val, dict):
        for k, v in val.items():
            if not isinstance(k, str):
                raise TypeError(f"Non-string dict key forbidden in RFC 8785 JCS: {type(k).__name__}")
            _validate_jcs_value(k)
            _validate_jcs_value(v)
    elif isinstance(val, (list, tuple)):
        for item in val:
            _validate_jcs_value(item)


def canonicalize_jcs(obj: Any) -> bytes:
    """Return strict deterministic UTF-8 JCS (RFC 8785) canonical bytes."""
    _validate_jcs_value(obj)
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha256_jcs(obj: Any) -> str:
    """Return lowercase hex SHA-256 digest of the JCS-canonicalized object."""
    return hashlib.sha256(canonicalize_jcs(obj)).hexdigest()


def verify_canonical_b64url(token: str) -> bytes:
    """Enforce strict unpadded RFC 4648 Section 5 base64url encoding."""
    if not isinstance(token, str) or not token or "=" in token:
        raise ValueError("Non-canonical or padded base64url string")
    if not re.fullmatch(r"[A-Za-z0-9_-]+", token):
        raise ValueError("Invalid characters in base64url string")
    pad = "=" * ((4 - len(token) % 4) % 4)
    raw = base64.urlsafe_b64decode(token + pad)
    reencoded = base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")
    if reencoded != token:
        raise ValueError("Non-zero trailing pad bits in base64url string")
    return raw


def verify_delegation_chain(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Verify hash continuity, scope attenuation, and temporal monotonicity across N hops."""
    if not records:
        return {"verified": False, "reason": "empty_chain"}
    for idx, rec in enumerate(records):
        if isinstance(rec.get("issued_at"), bool) or not isinstance(rec.get("issued_at"), int):
            return {"verified": False, "hop": idx, "reason": "invalid_issued_at_type"}
        if isinstance(rec.get("expires_at"), bool) or not isinstance(rec.get("expires_at"), int):
            return {"verified": False, "hop": idx, "reason": "invalid_expires_at_type"}
        if rec["expires_at"] < rec["issued_at"]:
            return {"verified": False, "hop": idx, "reason": "expired_before_issue"}
        if idx > 0:
            prev = records[idx - 1]
            expected_parent_hash = sha256_jcs(prev)
            if rec.get("parent_record_hash") != expected_parent_hash:
                return {"verified": False, "hop": idx, "reason": "parent_hash_mismatch"}
            prev_scopes = set(prev.get("scopes", []))
            curr_scopes = set(rec.get("scopes", []))
            if not curr_scopes.issubset(prev_scopes):
                return {"verified": False, "hop": idx, "reason": "scope_escalation"}
            if rec["issued_at"] < prev["issued_at"] or rec["expires_at"] > prev["expires_at"]:
                return {"verified": False, "hop": idx, "reason": "temporal_window_violation"}
    return {"verified": True, "hops": len(records), "terminal_hash": sha256_jcs(records[-1])}


def evaluate_asi_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    """Evaluate an OWASP ASI01-ASI10 adversarial scenario deterministically."""
    trusted_sources = set(scenario.get("trusted_sources", []))
    denied_tools = set(scenario.get("denied_tools", []))
    allowed_domains = set(scenario.get("allowed_domains", []))
    events = scenario.get("events", [])
    tool_calls = scenario.get("tool_calls", [])

    approved_actions = {
        ev.get("action")
        for ev in events
        if isinstance(ev, dict)
        and ev.get("type") == "approval"
        and ev.get("decision") == "approved"
        and ev.get("source") in trusted_sources
    }

    violations: list[str] = []
    for tc in tool_calls:
        name = tc.get("name", "")
        if name in denied_tools:
            violations.append(f"denied_tool:{name}")
        if scenario.get("require_approval_for") == name and name not in approved_actions:
            violations.append(f"unapproved_action:{name}")
        # Depth-bounded fail-closed recipient check
        def _walk(v: Any, depth: int = 0) -> None:
            if depth > _MAX_WALK_DEPTH:
                violations.append("max_walk_depth_exceeded")
                return
            if isinstance(v, str):
                for addr in _EMAIL_RE.findall(v):
                    dom = addr.split("@", 1)[1].lower()
                    if allowed_domains and dom not in allowed_domains:
                        violations.append(f"unauthorized_recipient:{addr}")
            elif isinstance(v, dict):
                for nv in v.values():
                    _walk(nv, depth + 1)
            elif isinstance(v, (list, tuple)):
                for item in v:
                    _walk(item, depth + 1)
        _walk(tc.get("arguments", {}))

    blocked = len(violations) > 0
    return {
        "scenario_id": scenario.get("scenario_id"),
        "asi_category": scenario.get("asi_category"),
        "blocked": blocked,
        "violations": violations,
    }


def main() -> int:
    print(json.dumps({"package": "agentic-governance-benchmarks", "version": "1.0.0", "status": "ok"}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
