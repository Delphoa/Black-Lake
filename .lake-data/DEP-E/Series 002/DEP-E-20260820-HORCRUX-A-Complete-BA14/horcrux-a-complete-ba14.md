---
title: "HORCRUX A Complete PQC - DEP-E"
generated_at: "2026-08-19T22:59:33Z"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of HORCRUX: A Complete PQC RISC-V eXtension Architecture"
source_status: "URLs only; official arXiv metadata and full HTML inspected"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-20"
temporal_cutoff: "2026-08-20"
primary_url: "https://arxiv.org/abs/2607.13939"
stable_identifier: "arXiv:2607.13939"
confidence_summary: "Medium for source characterization; low for independent outcome validation because no reproduction was performed."
safety_scope: "research review and bounded implementation analysis"
distribution_notes: "Derived review only; no source PDFs, datasets, code, credentials, or private material are redistributed."
---

# HORCRUX A Complete PQC - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository-relative path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | HORCRUX: A Complete PQC RISC-V eXtension Architecture | Primary research artifact | arXiv HTML and Atom metadata | arXiv:2607.13939 | https://arxiv.org/abs/2607.13939; https://arxiv.org/html/2607.13939 | Public research source; no source file redistributed | 2026-08-20 | Inspected |
| S2 | Selected source DEP | Provenance and deposited finding | Markdown | DEP-20260717-Tech Intel 0104 | https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260717-Tech%20Intel%200104 | Repository evidence; no source file copied | 2026-08-20 | Inspected |
| S3 | Latest prior Report-Mark | Iterative-expansion context | Markdown | Black-Lake-Data/.lake-data/DEP-20260717-Tech Intel 0104/BL-DEP-Mark001 Report-Mark.md | Black-Lake-Data/.lake-data/DEP-20260717-Tech Intel 0104/BL-DEP-Mark001 Report-Mark.md | Repository evidence | 2026-08-20 | Inspected |

The selected DEP contains 3 inspected Markdown file(s) and no newly collected source payload. The primary publication date recorded by official metadata is `2026-07-15T15:21:26Z`. Prior material was detected. The latest Report-Mark was reviewed first, and one research thread was selected from its related-reading/source-reference pool using cryptographic rejection sampling. The chosen thread was `https://arxiv.org/abs/2607.13939`; inaccessible candidates, if any, are recorded in the artifact log.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 canonical metadata and abstract | Primary research source | Title, authors, identifier, publication metadata, abstract-level problem framing and claimed contribution | C1, C2 | High for metadata; medium for claims | Source-reported research; no independent reproduction |
| E2 | S1 full HTML | Primary full text or access trace | Presence and role of method, evaluation, limitation, and conclusion sections | C2, C3 | Medium-high when available | No raw-data, code, or numerical recomputation was performed |
| E3 | S2 source DEP | Repository provenance | Deposited synthesis, relevance framing, source inventory, and explicit validation boundary | C1, C3 | Medium | Generated source recap is not independent validation |
| E4 | S3 prior Report-Mark | Prior review context | Related-reading and source-reference pool used for the new expansion draw | C3 | Medium | Prior generated review; references require independent inspection |

## Executive Summary

This DEP-E artifact reviews *HORCRUX: A Complete PQC RISC-V eXtension Architecture*, attributed to Alessandra Dolmeta; Valeria Piscopo; Michael Hutter; Maurizio Martina; Guido Masera. The selected source DEP characterizes the work as a current research claim and summarizes it as follows: Abstract This work presents a compact RISC-V extension for Post-Quantum Cryptography (PQC) called HORCRUX , which provides a unified Instruction-Set Extension (ISE) supporting all NIST-approved PQC algorithms. HORCRUX addresses the difficult trade-off between crypto-agility, high performance, and low resource consumption in constrained environments, a balance typically missing in hardware extensions that focus on limited PQC subsets. By targeting shared kernels across ML-KEM , ML-DSA , SLH-DSA , HQC , and Falcon , the extension introduces new RISC-V instructions executed by a resource-efficient, tightly coupled coprocessor. This architecture is specifically optimized for embedded systems with strict energy budgets and limited area. Experimental evaluation on a Zynq UltraScale+ FPGA demonstrates speedups of up to 129 for hash-based, 9 for lattice-based, and 27 for code-based schemes, while adding fewer than 21k LUTs and 4.4k FFs. ASIC results from post-synthesis characterization in 65 nm CMOS are also reported, alongside a rigorous power characterization to validate the architecture’s energy efficiency. The extension’s modular structure maintains backward compatibility with standard RISC-V cores, offering a scalable solution for deploying PQC on constrained embedded systems. [E1, E3]. Official arXiv metadata and full HTML were inspected, while no source file, dataset, code repository, model, or execution trace was collected.

The strongest supported conclusion is that the work presents a concrete and reviewable contribution in medical or health research, but the operational strength of its outcome claims remains unverified. The full HTML exposes a method, approach, framework, or architecture section that was inspected for mechanism-level context. The full HTML exposes an experiment, evaluation, result, or analysis section. This review records its existence and claim role but does not recompute reported values. Confidence is bounded because this pass did not reproduce experiments, inspect private data, execute code, or establish peer-review status [E1-E3].

Reviewer interpretation: Agent safety t This is a reason to prioritize structured evaluation, not a basis for production, clinical, security, procurement, or policy decisions without the independent checks listed below.

## Detailed Summary

### Problem and contribution

The primary source addresses the research object identified by its canonical title, *HORCRUX: A Complete PQC RISC-V eXtension Architecture*. The source DEP preserves the following concise account: Abstract This work presents a compact RISC-V extension for Post-Quantum Cryptography (PQC) called HORCRUX , which provides a unified Instruction-Set Extension (ISE) supporting all NIST-approved PQC algorithms. HORCRUX addresses the difficult trade-off between crypto-agility, high performance, and low resource consumption in constrained environments, a balance typically missing in hardware extensions that focus on limited PQC subsets. By targeting shared kernels across ML-KEM , ML-DSA , SLH-DSA , HQC , and Falcon , the extension introduces new RISC-V instructions executed by a resource-efficient, tightly coupled coprocessor. This architecture is specifically optimized for embedded systems with strict energy budgets and limited area. Experimental evaluation on a Zynq UltraScale+ FPGA demonstrates speedups of up to 129 for hash-based, 9 for lattice-based, and 27 for code-based schemes, while adding fewer than 21k LUTs and 4.4k FFs. ASIC results from post-synthesis characterization in 65 nm CMOS are also reported, alongside a rigorous power characterization to validate the architecture’s energy efficiency. The extension’s modular structure maintains backward compatibility with standard RISC-V cores, offering a scalable solution for deploying PQC on constrained embedded systems. [E1, E3]. This artifact treats that account as a source-reported claim rather than an independently established fact.

### Mechanism and methodology trace

The full HTML exposes a method, approach, framework, or architecture section that was inspected for mechanism-level context. The review verified the source's section structure and provenance but did not infer implementation details that were absent from the inspected evidence. The practical mechanism should therefore be read through the canonical paper before implementation decisions are made [E2].

### Evaluation and results trace

The full HTML exposes an experiment, evaluation, result, or analysis section. This review records its existence and claim role but does not recompute reported values. Any quantitative claims in the paper remain author-reported because this pass did not obtain raw counts, rerun code, recreate datasets, or recompute statistics. The evidence is adequate for research triage and replication planning, but not for independent outcome certification [E1, E2].

### Limitations and conclusion trace

The source includes an identifiable limitations or discussion section, strengthening the evidence boundary for downstream review. An identifiable conclusion section was also inspected to confirm the authors' closing scope. Reviewer interpretation remains deliberately narrower than the paper's prospective implications.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | The selected source DEP identifies this publication as a relevant research object and preserves a primary locator. | Source-deposited claim | E3 | Directly supported as provenance, not as outcome validation. | High |
| C2 | The publication presents a contribution and evaluation relevant to medical or health research. | Author claim | E1, E2 | Credible enough for structured review; independent reproduction remains necessary. | Medium |
| C3 | The work should be evaluated through independent clinical validation, representative cohorts, calibration, and privacy review before operational adoption. | Reviewer interpretation | E1-E3 | This follows from the preprint status, evidence limits, and domain risk. | Medium-high |

## Methodology

- Research objective: Convert the randomly selected source DEP into a provenance-preserving, schema-complete DEP research artifact.
- Sources inspected: Every Markdown file in `Black-Lake-Data/.lake-data/DEP-20260717-Tech Intel 0104`, the canonical primary record, official metadata, and full HTML when accessible; the latest Report-Mark was also inspected for iterative passes.
- Discovery strategy: Repository inventory review, URL extraction, official metadata retrieval, full-HTML section tracing, and prior-reference review when available.
- Inclusion criteria: Primary or near-primary sources directly named by the selected DEP or its latest Report-Mark.
- Exclusion criteria: Unrelated discovery links, inaccessible payloads as evidence, and claims not traceable to inspected material.
- Analytical approach: Conceptual, empirical-evidence review, comparative framing, implementation translation, safety/ethics, product research, and replication planning.
- Evidence handling: Author claims, source-deposited summaries, reviewer interpretation, and missing evidence are labeled separately and mapped to the applicable evidence-ledger IDs.
- Uncertainty handling: Unavailable code, data, metrics, peer-review status, and reproduction are recorded as limits rather than inferred.

## Scope, Constraints, and Assumptions

- Scope: The selected DEP, one primary research thread, its official public representation, and directly associated prior review context.
- Temporal boundary: Sources accessed on 2026-08-20; later revisions may differ.
- Evidence limits: No independent code execution, dataset inspection, benchmark replay, statistical recomputation, proof verification, or physical reproduction.
- Assumptions: The official metadata and public HTML correspond to the source locator recorded by the DEP.
- Constraints: Public-source access, redistribution limits, privacy and safety boundaries, and the requirement to avoid local-system disclosure.
- Out of scope: Certification of the paper's results, deployment approval, clinical guidance, offensive operationalization, and legal conclusions.
- Intended use: DEP deposition, research triage, replication planning, implementation ideation, and follow-on evidence review.
- Audience: clinical research and evidence-review teams.
- Reproducibility boundary: Metadata and review structure are reproducible; experimental or theoretical claims are not independently reproduced here.

## Observations

- Observed pattern: The source chain is strongest for identity, provenance, and author-stated scope; outcome confidence is weaker because no independent replay was performed.
- Technical implication: A future reviewer can use the stable identifier and section-level evidence trace to design a focused validation rather than restarting discovery.
- Contradiction or tension: Research usefulness is immediate, while deployment usefulness depends on evidence that is not yet present in this artifact.
- Open question: Which result survives the most relevant independent baseline, variance, and distribution-shift checks?

## Considerations

- Adoption should be gated on independent clinical validation, representative cohorts, calibration, and privacy review.
- The principal risk is clinical overreach, population shift, privacy leakage, and unsafe decision support.
- Data, code, model, and dependency availability must be verified rather than inferred from the paper's existence.
- Any implementation should preserve source versions, assumptions, negative results, and human review boundaries.

## Strengths

- The selected DEP provides a stable provenance path and explicit primary locator.
- Official metadata and full HTML were inspected when accessible, reducing reliance on a secondary recap alone.
- The review separates author claims, deposited synthesis, reviewer interpretation, and missing evidence.
- The artifact provides a concrete replication and product-evaluation handoff.

## Weaknesses

- No independent experiment, proof, benchmark, or system reproduction was performed.
- Raw data, code, model artifacts, and environment details were not audited in this pass.
- Cross-paper comparison is limited to locators and prior review context unless explicitly inspected.
- Preprint revisions or later venue versions may alter claims, methods, or reported results.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Acquire executable or auditable evidence | Reproducibility | Source claims cannot be independently checked from metadata alone. | Raises confidence in central outcomes. | Compute, licensing, and dependency risk. | Reproduce one headline result with pinned versions. |
| Add matched baselines and variance | Evaluation | Single reported settings may not generalize. | Clarifies effect size and robustness. | Additional experiments and reviewer time. | Run held-out, ablation, and multi-seed comparisons. |
| Publish a structured evidence card | Provenance | Claims, assumptions, and artifacts are distributed across sections. | Improves downstream auditability. | Maintenance burden. | Verify every claim maps to a versioned source. |
| Test deployment boundaries | Transfer | Research conditions may differ from operational environments. | Prevents unsupported adoption claims. | Domain-specific test design. | Use representative workloads and stop criteria. |

## Potential Implementations

1. Evidence review workspace: User - clinical research and evidence-review teams. Goal - trace claims to versioned sources. Core mechanism - ingest metadata and reviewer-entered evidence IDs. Required inputs - public URLs and approved notes. Outputs - evidence ledger, gaps, and review status. Risk controls - no hidden imputation, visible source status, and human approval. Evaluation - link integrity and reviewer agreement.
2. Bounded reproduction harness: User - research engineers. Goal - test one source-reported result. Core mechanism - pinned configuration, synthetic or authorized data, deterministic runs, and baseline comparison. Required inputs - documented dependencies and safe inputs. Outputs - reproducibility report and variance. Risk controls - sandboxing, resource caps, and no sensitive-data logging. Evaluation - expected-output and failure-case checks.
3. Adoption gate: User - product and assurance teams. Goal - prevent research claims from becoming deployment claims prematurely. Core mechanism - map evidence maturity to required controls. Required inputs - artifact, threat/risk review, and operational constraints. Outputs - proceed, hold, or reject decision with reasons. Risk controls - explicit uncertainty and accountable sign-off. Evaluation - audit sampled decisions against evidence.

## Three Ways to Exercise This Research

1. Claim-to-source audit: Objective - verify the three central claims. Inputs - the canonical record, full HTML, and source DEP. Method - map each claim to a section and record missing evidence. Output - a one-page evidence table. Success criterion - every claim is supported or explicitly unresolved. Stop condition - stop when a source is inaccessible rather than inferring its contents.
2. Synthetic reproduction design: Objective - test the mechanism without restricted data. Inputs - public metadata, synthetic inputs, and a documented baseline. Method - implement the smallest safe comparison with fixed seeds and resource limits. Output - reproducibility plan and expected observations. Success criterion - assumptions and failure modes are testable. Stop condition - stop before production or sensitive-data use.
3. Deployment-boundary review: Objective - translate the paper into an adoption checklist. Inputs - this artifact, operational requirements, and domain controls. Method - compare paper conditions with target conditions and list gaps. Output - gated readiness decision. Success criterion - no deployment claim exceeds inspected evidence. Stop condition - stop if independent validation or accountable approval is missing.

## Example MVP Product

- Product name: Research Evidence Workbench
- Target user: clinical research and evidence-review teams
- Problem: Research claims move into implementation planning without a durable evidence and uncertainty trail.
- Core workflow: Import public metadata; register evidence IDs; label author claims and reviewer interpretations; record missing artifacts; export a DEP-ready review.
- Data requirements: Public URLs, version identifiers, reviewer notes, synthetic test data, and optional explicitly authorized results.
- Architecture: Local-first Markdown/JSON evidence store, deterministic schema validator, link checker, and static report renderer.
- Success metrics: All major claims have evidence IDs; zero local-system leaks; source links resolve; independent reviewers agree on evidence status.
- Risk controls: No automatic deployment approval, no raw secret or sensitive-data logging, visible uncertainty, source pinning, and human sign-off.
- Limitations: The product cannot recover unavailable evidence or independently establish a research result.
- MVP boundary: Public-source review and synthetic evaluation only; no autonomous hardware, clinical, security, or production action.
- Deployment model: Local CLI and static Markdown/HTML output.
- Evaluation plan: Schema checks, link checks, known-case tests, and reviewer spot audits.
- Failure modes: Stale sources, mislabeled claims, unreviewed related links, and false confidence from clean formatting.
- Maintenance plan: Recheck source versions, preserve correction history, and require review for changed headline claims.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| HORCRUX: A Complete PQC RISC-V eXtension Architecture | Primary research thread | New in this pass; randomly selected from the latest Report-Mark research pool and inspected as the primary expansion thread. | https://arxiv.org/abs/2607.13939 |
| Official full-text representation | Primary source format | Full HTML used to locate abstract, methodology, evaluation, limitations, and conclusion evidence where available. | https://arxiv.org/html/2607.13939 |
| Selected source DEP | Provenance record | Preserves the deposited finding, source inventory, and explicit non-reproduction boundary. | https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260717-Tech%20Intel%200104 |
| Related locator | Citation or source-deposited context | Discovered through inspected evidence but not independently reviewed in this pass. | https://alignment.anthropic.com/2026/modular-pretraining/ |
| Related locator | Citation or source-deposited context | Discovered through inspected evidence but not independently reviewed in this pass. | https://arxiv.org/abs/2607.08077 |
| Related locator | Citation or source-deposited context | Discovered through inspected evidence but not independently reviewed in this pass. | https://arxiv.org/abs/2607.13157 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2607.13939 | Canonical title, authors, abstract, identifier, and source status | 2026-08-20 | Primary record inspected |
| R2 | https://arxiv.org/html/2607.13939 | Full-text section structure, method/evaluation trace, limitations, and conclusion | 2026-08-20 | Full HTML inspected |
| R3 | https://export.arxiv.org/api/query?id_list=2607.13939 | Canonical Atom metadata and abstract | 2026-08-20 | Official arXiv API inspected |
| R4 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260717-Tech%20Intel%200104/BL-DEP-Mark001%20Report-Mark.md | Selected DEP inventory, deposited claim, or prior Report-Mark context | 2026-08-20 | Repository file inspected by URL; not collected |
| R5 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260717-Tech%20Intel%200104/daily_research_findings_2026-07-17_0104.md | Selected DEP inventory, deposited claim, or prior Report-Mark context | 2026-08-20 | Repository file inspected by URL; not collected |
| R6 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260717-Tech%20Intel%200104/README.md | Selected DEP inventory, deposited claim, or prior Report-Mark context | 2026-08-20 | Repository file inspected by URL; not collected |

## Appendix

### Selection and provenance

- Automation: `Black-Lake Data Processing & Review`
- Selection snapshot: 1020 candidates, 2 excluded, and 1018 eligible.
- Eligibility cutoff (UTC): `2026-08-18T22:59:33Z`
- Selection order: 183 of 200
- Cryptographic draw: `793192668` accepted on attempt 1, rejection limit `4294966720`, zero-based index `48` from a pool of 836.
- Eligible-list SHA-256: `46c0cb9b676edad557dd81e399a7a6e27e7fde4abeead2c6bcdfc2171332c939`
- Iterative status: prior material found and one supporting research thread expanded

### Source inventory and missing evidence

- `Black-Lake-Data/.lake-data/DEP-20260717-Tech Intel 0104/BL-DEP-Mark001 Report-Mark.md` - inspected repository file
- `Black-Lake-Data/.lake-data/DEP-20260717-Tech Intel 0104/daily_research_findings_2026-07-17_0104.md` - inspected repository file
- `Black-Lake-Data/.lake-data/DEP-20260717-Tech Intel 0104/README.md` - inspected repository file
- No external PDF, source archive, dataset, code repository, model, benchmark payload, or execution trace was collected.
- Independent reproduction and operational validation remain future work.
