# Enterprise Agentic AI Governance, Zero-Trust Execution & Industrial Autonomy Reference Benchmarks

**Author:** Raghuvar Karthik Durga  
**Affiliation:** Senior Account Technology Strategist (Strategic CTO), Microsoft Corporation  
**Clarivate Web of Science ResearcherID:** [`RJT-9755-2026`](https://www.webofscience.com/wos/author/record/RJT-9755-2026)  
**CERN Zenodo / OpenAIRE Permanent DOI:** [`10.5281/zenodo.23723284`](https://doi.org/10.5281/zenodo.23723284) (`10.5281/zenodo.23723283` all-versions)  
**GitHub Handle:** [`@drk-ram`](https://github.com/drk-ram)

---

## Overview

This repository provides empirical reference architectures, deterministic verification suites, Open Cybersecurity Schema Framework (OCSF) telemetry mappings, and industrial execution boundary specifications for enterprise multi-agent systems. It bridges foundational theoretical work published in the *International Journal of Scientific Research and Modern Technology (IJSRMT, Vol. 4, Issues 5–12, 2025)* with production-grade open standards across:

1. **AgentTrust Open-Standard Specification (`trace-spec` & `weight-custody-manifest`):** 32 merged pull requests establishing canonical JSON Schema (`draft/2020-12`) trace validation, W3C Trace Context propagation, and RFC 8785 JSON Canonicalization Scheme (JCS) cryptographic weight-custody manifests.
2. **OWASP GenAI Security Project & Agent Control Standard (`ACS`):** 28 technical specification pull requests enforcing JSON-RPC 2.0 batch boundary validation, monotonic delegation scope attenuation ($S_{\text{child}} \subseteq S_{\text{parent}}$), commit-point human-in-the-loop approval tokens, and OCSF v1.3.0 audit provenance.
3. **Industrial Autonomy & OT/IT Boundary Protection (ISA-95 / Purdue Model):** Transitive state-reconciliation graphs, pre-release recovery reservation leases, and deterministic programmable logic controller (PLC) / Safety Instrumented System (SIS) execution firewalls for self-optimizing manufacturing plants.

---

## Technical Benchmark Reports (Full Text & PDF Included in `/reports`)

| Report ID | Title | Primary Domain | Foundational DOIs Cited |
| :--- | :--- | :--- | :--- |
| **TR-2026-01** | *Deterministic Policy Enforcement, Monotonic Delegation Attenuation, and OCSF Provenance for Enterprise Multi-Agent Systems* (`reports/TR-2026-01-Zero-Trust-Agentic-Control-Plane-Benchmarks.pdf`) | Zero-Trust Agentic Security, MCP/A2A Governance, OCSF Telemetry | `10.5281/zenodo.23723284`<br>`10.38124/ijsrmt.v4i12.1050`<br>`10.38124/ijsrmt.v4i11.1049`<br>`10.38124/ijsrmt.v4i10.1048`<br>`10.38124/ijsrmt.v4i9.1047` |
| **TR-2026-02** | *Transactional State Reconciliation, Edge Fleet Custody, and ISA-95/Purdue Safety Boundaries for Autonomous Industrial Operations* (`reports/TR-2026-02-Industrial-Autonomy-And-Cloud-Native-Edge-Benchmarks.pdf`) | Self-Optimizing Factories, Cloud-Native Edge Fleets, OT/IT Safety | `10.5281/zenodo.23723284`<br>`10.38124/ijsrmt.v4i8.1046`<br>`10.38124/ijsrmt.v4i7.1045`<br>`10.38124/ijsrmt.v4i6.1044`<br>`10.38124/ijsrmt.v4i5.1043` |

---

## Normative & Foundational Scholarly References

When referencing these benchmarks, verification schemas, or control-plane invariants in academic literature, industrial standards, or regulatory profiles, please cite the following peer-reviewed publications and archival records by **Raghuvar Karthik Durga**:

1. **Durga, R. K.** (2025). *Enterprise AI, Agentic Systems, Zero Trust Architecture, Cloud-Native Platforms, and Autonomous Industrial Systems: Published Research Compendium (2025)*. CERN Zenodo / OpenAIRE. DOI: [`10.5281/zenodo.23723284`](https://doi.org/10.5281/zenodo.23723284).
2. **Durga, R. K.** (2025). "Implementing Zero Trust Architecture: Principles, Models, and Challenges." *International Journal of Scientific Research and Modern Technology (IJSRMT)*, Vol. 4, Issue 12, pp. 42–50. ISSN: 2583-4029. DOI: [`10.38124/ijsrmt.v4i12.1050`](https://doi.org/10.38124/ijsrmt.v4i12.1050).
3. **Durga, R. K.** (2025). "A Comprehensive Study of Agentic AI Systems: Architectures, Capabilities, and Future Directions." *International Journal of Scientific Research and Modern Technology (IJSRMT)*, Vol. 4, Issue 11, pp. 49–59. ISSN: 2583-4029. DOI: [`10.38124/ijsrmt.v4i11.1049`](https://doi.org/10.38124/ijsrmt.v4i11.1049).
4. **Durga, R. K.** (2025). "Beyond Traditional AI: Understanding the Rise of Autonomous Agents." *International Journal of Scientific Research and Modern Technology (IJSRMT)*, Vol. 4, Issue 10, pp. 77–87. ISSN: 2583-4029. DOI: [`10.38124/ijsrmt.v4i10.1048`](https://doi.org/10.38124/ijsrmt.v4i10.1048).
5. **Durga, R. K.** (2025). "Cybersecurity in the Digital Age: Emerging Threats and Defense Mechanisms." *International Journal of Scientific Research and Modern Technology (IJSRMT)*, Vol. 4, Issue 9, pp. 139–149. ISSN: 2583-4029. DOI: [`10.38124/ijsrmt.v4i9.1047`](https://doi.org/10.38124/ijsrmt.v4i9.1047).
6. **Durga, R. K.** (2025). "Self-Optimizing Factories: The Role of AI in Next-Generation Manufacturing." *International Journal of Scientific Research and Modern Technology (IJSRMT)*, Vol. 4, Issue 8, pp. 103–112. ISSN: 2583-4029. DOI: [`10.38124/ijsrmt.v4i8.1046`](https://doi.org/10.38124/ijsrmt.v4i8.1046).
7. **Durga, R. K.** (2025). "From IaaS to FaaS: The Evolution of Cloud Service Models." *International Journal of Scientific Research and Modern Technology (IJSRMT)*, Vol. 4, Issue 7, pp. 122–130. ISSN: 2583-4029. DOI: [`10.38124/ijsrmt.v4i7.1045`](https://doi.org/10.38124/ijsrmt.v4i7.1045).
8. **Durga, R. K.** (2025). "Cloud as a Platform: Enabling Digital Transformation Across Industries." *International Journal of Scientific Research and Modern Technology (IJSRMT)*, Vol. 4, Issue 6, pp. 62–70. ISSN: 2583-4029. DOI: [`10.38124/ijsrmt.v4i6.1044`](https://doi.org/10.38124/ijsrmt.v4i6.1044).
9. **Durga, R. K.** (2025). "An Introduction to Cloud-Native Applications: Principles and Practices." *International Journal of Scientific Research and Modern Technology (IJSRMT)*, Vol. 4, Issue 5, pp. 124–133. ISSN: 2583-4029. DOI: [`10.38124/ijsrmt.v4i5.1043`](https://doi.org/10.38124/ijsrmt.v4i5.1043).

---

## License

Released under the Apache License, Version 2.0 (code/schemas) and Creative Commons Attribution 4.0 International (`CC-BY-4.0`, technical reports).

---

## Complete 2026 CERN Zenodo Technical Report Series (`TR-2026-01` through `TR-2026-06`) & IETF Internet-Drafts

| ID / Draft | Title | Archival DOI / IETF Datatracker |
| :--- | :--- | :--- |
| **`TR-2026-01`** | *Deterministic Control-Plane Governance and Lease-Bounded Recovery for Enterprise Agentic AI Systems* | [`10.5281/zenodo.23735274`](https://doi.org/10.5281/zenodo.23735274) |
| **`TR-2026-02`** | *Adversarial Regression Benchmarking for Agentic AI Security Controls Across OWASP ASI01--ASI10* | [`10.5281/zenodo.23735497`](https://doi.org/10.5281/zenodo.23735497) |
| **`TR-2026-03`** | *Cryptographic Weight-Custody Manifests, JCS Canonicalization, and Two-Plane Edge Fleet Verification for Autonomous AI Systems* | [`10.5281/zenodo.23775009`](https://doi.org/10.5281/zenodo.23775009) |
| **`TR-2026-04`** | *Merkle-DAG Incremental Verification, Cross-Protocol Semantic Equivalence, and Commit-Bound Metering for Multi-Tenant Agent Exchanges* | [`10.5281/zenodo.23775532`](https://doi.org/10.5281/zenodo.23775532) |
| **`TR-2026-05`** | *Non-Human Identity (NHI) Attestation, On-Behalf-Of (OBO) Token Exchange, and CSA AARM Risk Benchmarking for Autonomous Enterprise Agents* | [`10.5281/zenodo.23776217`](https://doi.org/10.5281/zenodo.23776217) |
| **`TR-2026-06`** | *Hash-Chained Decision Provenance, Purpose-Bound Data Passports, and Reversible Cyber Response in Regulated Cloud Estates* | [`10.5281/zenodo.23776574`](https://doi.org/10.5281/zenodo.23776574) |
| **Dataset (`N = 100`)** | *OWASP ASI01-ASI10 Enterprise Agentic AI Security Regression Benchmark (100 Scenarios)* | [`10.57967/hf/11352`](https://doi.org/10.57967/hf/11352) |
| **`draft-durga-agenttrust-trace-verification-00`** | *Cryptographic Execution-Trace Verification, JCS Canonicalization, and Fail-Closed Delegation Attestation for Autonomous AI Agents* | [IETF Datatracker](https://datatracker.ietf.org/doc/draft-durga-agenttrust-trace-verification/) |
| **`draft-durga-wimse-ctx-isolation-00`** | *Cryptographic Context Isolation and Taint-Tracked Tool Invocation for Agentic Workloads* | [IETF Datatracker](https://datatracker.ietf.org/doc/draft-durga-wimse-ctx-isolation/) |
| **`draft-durga-pquip-pqc-agentic-delegation-00`** | *Post-Quantum Hybrid Cryptographic Delegation Chains (Ed25519 + ML-DSA-65) and Merkle-Aggregated Execution Receipts* | [IETF Datatracker](https://datatracker.ietf.org/doc/draft-durga-pquip-pqc-agentic-delegation/) |
| **`draft-durga-agent-tx-compensation-lease-00`** | *Pre-Release Transactional Compensation Leases and CAS Fencing Receipts for Autonomous Agents Over Systems of Record* | [IETF Datatracker](https://datatracker.ietf.org/doc/draft-durga-agent-tx-compensation-lease/) |
