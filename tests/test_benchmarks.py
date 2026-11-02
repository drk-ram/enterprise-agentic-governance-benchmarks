import json
import pathlib
from agentic_governance_benchmarks import (
    canonicalize_jcs,
    sha256_jcs,
    verify_delegation_chain,
    evaluate_asi_scenario,
)
from agentic_governance_benchmarks.verifier import verify_canonical_b64url
import pytest


def test_jcs_canonicalization_and_rejections():
    assert canonicalize_jcs({"b": 1, "a": 2}) == b'{"a":2,"b":1}'
    with pytest.raises(ValueError):
        canonicalize_jcs({"x": float("nan")})
    with pytest.raises(ValueError):
        canonicalize_jcs({"s": "\ud800"})


def test_canonical_base64url_hygiene():
    raw = verify_canonical_b64url("AQID")
    assert raw == b"\x01\x02\x03"
    with pytest.raises(ValueError):
        verify_canonical_b64url("AQID=")


def test_delegation_chain_verification():
    hop0 = {"hop": 0, "issued_at": 1700000000, "expires_at": 1700003600, "scopes": ["erp:read", "erp:write"]}
    hop1 = {
        "hop": 1,
        "parent_record_hash": sha256_jcs(hop0),
        "issued_at": 1700000100,
        "expires_at": 1700001800,
        "scopes": ["erp:read"],
    }
    res = verify_delegation_chain([hop0, hop1])
    assert res["verified"] is True
    assert res["hops"] == 2

    # Reject boolean timestamp masquerading as int
    bad_hop = dict(hop0, issued_at=True)
    assert verify_delegation_chain([bad_hop])["verified"] is False

    # Reject scope escalation
    esc_hop = dict(hop1, scopes=["erp:read", "erp:admin"])
    assert verify_delegation_chain([hop0, esc_hop])["reason"] == "scope_escalation"


def test_100_owasp_asi_scenarios_dataset():
    ds_path = pathlib.Path(__file__).resolve().parent.parent / "dataset_hf" / "owasp_asi01_asi10_100_scenarios.jsonl"
    lines = ds_path.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 100
    for line in lines:
        scen = json.loads(line)
        out = evaluate_asi_scenario(scen)
        assert out["blocked"] is scen["expected_blocked"]
