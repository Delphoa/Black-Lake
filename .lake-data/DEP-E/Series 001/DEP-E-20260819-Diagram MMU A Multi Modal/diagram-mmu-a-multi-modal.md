---
title: "Diagram MMU A Multi Modal - DEP-E"
generated_at: "2026-08-18T20:49:54Z"
run_date: "2026-08-19"
artifact_type: "DEP research artifact"
primary_subject: "Diagram-MMU: A Multi-Modal Benchmark for Scientific Diagrams"
source_status: "Repository source package and public metadata inspected; no original source files collected"
reviewer: "Codex recurring automation"
schema_version: "2026-07-07-expanded"
source_dep: "Black-Lake-Data/.lake-data/DEP-20260818-Tech Intel 1105"
selection_record: "117 candidates; 32 excluded; 85 eligible; draw 550504538; zero-based index 83"
expansion_record: "13 retained public locators; draw 885484915; zero-based index 3"
confidence_summary: "High for source identity and repository provenance; medium for source-package claims; low for unreplicated transfer claims"
safety_scope: "Research review, defensive evaluation, and bounded implementation planning"
distribution_notes: "No local paths, credentials, private data, source payloads, datasets, models, or executable artifacts are redistributed"
---

# Diagram MMU A Multi Modal - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Selected source DEP README | Source package boundary | Markdown | DEP-20260818-Tech Intel 1105 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260818-Tech%20Intel%201105/README.md | Repository evidence; public URL | 2026-08-19 | Inspected |
| S2 | Deposited source artifact | Source synthesis | Markdown | daily_research_findings_2026-08-18_1105.md | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260818-Tech%20Intel%201105/daily_research_findings_2026-08-18_1105.md | Repository evidence; public URL | 2026-08-19 | Inspected |
| S3 | Diagram-MMU: A Multi-Modal Benchmark for Scientific Diagrams | Selected supporting source | arXiv record | 2608.12262 | https://arxiv.org/abs/2608.12262v1 | Metadata and source-package claims only | 2026-08-19 | Canonical arXiv Atom record inspected |

- Paper/work title: Diagram-MMU: A Multi-Modal Benchmark for Scientific Diagrams
- Authors or producing organization: Weihao Bo; Shan Zhang; Yanpeng Sun; Jie Liu; Yongke Yao; Jinhao Du; Wei He; Kai Zou; Zechao Li; Jingdong Wang
- Source platform: arXiv
- Publication date: 2026-08-12
- Revision/version date: 2026-08-12
- Stable identifier: 2608.12262
- Categories: cs.CV, cs.AI
- Local source files: none collected for publication

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260818-Tech%20Intel%201105/README.md | Source DEP README | DEP identity, inventory, attribution, and package boundaries | Source package identity | High | Repository metadata does not independently validate linked claims. |
| E2 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260818-Tech%20Intel%201105/daily_research_findings_2026-08-18_1105.md | Deposited source synthesis | ** Submitted 2026-08-12, VAKRA evaluates agents over more than 8,000 executable APIs across 62 domains in endpoint-style, compositional, and multi-source settings. Correctness is checked by re-executing predicted calls against live APIs while a fixed ReAct harness isolates model capability. The best reported model reaches 70.4% on single-hop endpoint tasks, falls to 50–51% on compositional APIs, loses more than half its performance as reasoning depth grows, and reaches as low as 2.4% on unanswerable policy-constrained questions. | Source-package claim and selected-thread context | Medium | Derived source synthesis; not an independent reproduction. |
| E3 | https://arxiv.org/abs/2608.12262v1 | Canonical arXiv metadata | Title, identity, version/date metadata, authors or credited organization, and availability | Primary source identity | High | No code, data, model, benchmark, or experiment was executed. |

## Executive Summary

This artifact expands the selected DEP through Diagram-MMU: A Multi-Modal Benchmark for Scientific Diagrams. The deposited source package reports that ** Submitted 2026-08-12, VAKRA evaluates agents over more than 8,000 executable APIs across 62 domains in endpoint-style, compositional, and multi-source settings. Correctness is checked by re-executing predicted calls against live APIs while a fixed ReAct harness isolates model capability. The best reported model reaches 70.4% on single-hop endpoint tasks, falls to 50–51% on compositional APIs, loses more than half its performance as reasoning depth grows, and reaches as low as 2.4% on unanswerable policy-constrained questions. This is a source-package claim tied to E2, not an independently reproduced result.

The practical relevance is that ** It measures the failure boundary that matters in enterprise agents—entity grounding, cross-source composition, and policy-constrained tool use—rather than treating retrieval, APIs, and reasoning as separate benchmark skills. The executable evaluation surface is useful for reproducing claims and for designing safer tool-use gates. Canonical source identity and availability were inspected (E3), while implementation, data, model, benchmark, and production behavior remain untested. Confidence is therefore high for provenance, medium for the deposited synthesis, and low for claims that would require independent execution.

## Detailed Summary

### Problem context

The selected thread addresses a research or engineering decision represented in the source package as consequential for downstream systems. The package frames the motivation as follows: ** It measures the failure boundary that matters in enterprise agents—entity grounding, cross-source composition, and policy-constrained tool use—rather than treating retrieval, APIs, and reasoning as separate benchmark skills. The executable evaluation surface is useful for reproducing claims and for designing safer tool-use gates.

### Source-reported contribution

The selected DEP summarizes the contribution this way: ** Submitted 2026-08-12, VAKRA evaluates agents over more than 8,000 executable APIs across 62 domains in endpoint-style, compositional, and multi-source settings. Correctness is checked by re-executing predicted calls against live APIs while a fixed ReAct harness isolates model capability. The best reported model reaches 70.4% on single-hop endpoint tasks, falls to 50–51% on compositional APIs, loses more than half its performance as reasoning depth grows, and reaches as low as 2.4% on unanswerable policy-constrained questions. The canonical record confirms the work's identity, credited authorship or organization, publication locator, and version/date metadata, but this review does not elevate the deposited summary into independently verified evidence.

### Evidence and transfer boundary

The review connects three layers: the DEP's inventory and attribution boundary (E1), the deposited synthesis and its selected claim (E2), and the canonical public record (E3). No prior same-DEP review lineage was required to interpret this item. No external code, dataset, model, benchmark payload, or source archive was collected.

### Practical interpretation

The work is most useful as a testable research direction. A downstream team should convert its claims into versioned hypotheses, identify required inputs and comparison baselines, and define a stop condition before implementation. That interpretation is reviewer analysis, not a claim attributed to the source.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | The deposited source package reports that ** Submitted 2026-08-12, VAKRA evaluates agents over more than 8,000 executable APIs across 62 domains in endpoint-style, compositional, and multi-source settings. Correctness is checked by re-executing predicted calls against live APIs while a fixed ReAct harness isolates model capability. The best reported model reaches 70.4% on single-hop endpoint tasks, falls to 50–51% on compositional APIs, loses more than half its performance as reasoning depth grows, and reaches as low as 2.4% on unanswerable policy-constrained questions. | Source-package claim | E2 | Preserved as a source claim; no independent rerun was performed. | Medium |
| C2 | The selected supporting record is Diagram-MMU: A Multi-Modal Benchmark for Scientific Diagrams, credited to Weihao Bo; Shan Zhang; Yanpeng Sun; Jie Liu; Yongke Yao; Jinhao Du; Wei He; Kai Zou; Zechao Li; Jingdong Wang. | Source metadata | E3 | Canonical identity and availability were directly checked. | High |
| C3 | ** It measures the failure boundary that matters in enterprise agents—entity grounding, cross-source composition, and policy-constrained tool use—rather than treating retrieval, APIs, and reasoning as separate benchmark skills. The executable evaluation surface is useful for reproducing claims and for designing safer tool-use gates. | Reviewer interpretation grounded in source package | E1-E3 | Useful as a research direction, not proof of deployment readiness. | Medium |

## Methodology

- **Research objective**: Preserve and expand one randomly selected supporting thread from DEP-20260818-Tech Intel 1105 as a schema-complete DEP-E research artifact.
- **Sources inspected**: Live Black-Lake and Black-Lake-Data repository rules; selected DEP README and deposited artifact; canonical selected-source metadata; no required prior review lineage.
- **Discovery strategy**: Enumerated public locators in the selected DEP, removed discovery-only category pages, used cryptographic rejection sampling, and inspected canonical metadata for the selected locator.
- **Inclusion criteria**: Repository evidence tied to the selected DEP and the randomly selected primary or near-primary public locator.
- **Exclusion criteria**: Unselected source threads were retained only as context; inaccessible, private, redistributable-source, code-execution, and benchmark-replay work was excluded.
- **Analytical approach**: Conceptual, comparative, implementation, safety/ethics, product research, and replication planning.
- **Evidence handling**: Source claims, metadata facts, and reviewer interpretations are labeled separately and mapped to evidence IDs.
- **Uncertainty handling**: Missing execution evidence, unavailable artifacts, and transfer assumptions remain explicit rather than inferred.

## Scope, Constraints, and Assumptions

- **Scope**: Repository source-package review and one selected supporting-thread expansion.
- **Temporal boundary**: Sources accessed on 2026-08-19; canonical metadata reflects the version visible during this run.
- **Evidence limits**: No independent paper reproduction, code audit, dataset inspection, model inference, benchmark replay, hardware test, or production telemetry review.
- **Assumptions**: The selected DEP accurately preserves its own source inventory; canonical metadata identifies the intended supporting work.
- **Constraints**: Public evidence only; no credentials, restricted data, private endpoints, clinical decisions, or offensive operations.
- **Out of scope**: Deployment certification, causal proof, legal advice, clinical validation, security certification, and claims beyond inspected evidence.
- **Intended use**: DEP deposition, research triage, implementation planning, and follow-on replication design.
- **Audience**: Researchers, engineers, evaluators, product leads, and safety reviewers.
- **Reproducibility boundary**: Provenance can be reproduced from public URLs; empirical results cannot be reproduced from this artifact alone.

## Observations

- **Observed pattern**: The source package becomes more reusable when its selected claim is separated from canonical identity and reviewer inference.
- **Technical implication**: Any implementation should preserve source version, configuration, input identity, output, and failure receipts.
- **Open question**: Which source-reported result remains stable under a matched baseline and independently controlled evaluation?
- **Reviewer hypothesis**: The highest-value next step is a bounded replication or comparison rather than immediate production adoption.

## Considerations

- Version drift can change source claims, implementation behavior, and evaluation results.
- Data rights, privacy, safety, and domain-specific governance must be reviewed before using non-public inputs.
- Reported metrics need matched baselines, sample definitions, uncertainty, and failure distributions.
- Operational adoption requires dependency review, monitoring, rollback, provenance receipts, and human escalation paths.

## Strengths

- The selected thread has a canonical public locator and a preserved source-package context (E1-E3).
- The DEP provides a concise relevance statement that supports downstream triage without hiding its provenance boundary (E2).
- The artifact turns a discovery record into explicit claims, evidence, constraints, and replication questions.

## Weaknesses

- The source-package synthesis is not an independent reproduction of the selected work.
- Code, data, models, prompts, benchmark harnesses, and execution environments were not inspected unless represented by public metadata.
- Generalization, cost, safety, and production-readiness claims remain untested.
- Unselected related threads were retained as locators rather than substantively re-reviewed.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Pin a reproducible source bundle | Provenance | Public pages and versions can drift | Stable claim-to-source trace | Storage and license review | Hash and re-open every permitted artifact |
| Run a matched baseline study | Evidence | Source-reported gains need controlled comparison | Stronger causal and practical confidence | Compute, data, and implementation cost | Pre-register metrics, budgets, and stop conditions |
| Add failure and subgroup analysis | Evaluation | Aggregate results can hide boundary failures | Better deployment decisions | Larger evaluation matrix | Report paired outcomes and uncertainty |

## Potential Implementations

| Implementation | User | Goal | Core Mechanism | Inputs | Outputs | Risk Controls | Evaluation |
|---|---|---|---|---|---|---|---|
| Evidence receipt generator | Research reviewer | Preserve claim lineage | Versioned source and claim ledger | Public metadata and review notes | Signed review receipt | Redaction, allowlisted URLs, immutable history | Trace completeness and reviewer agreement |
| Bounded replication harness | Evaluation engineer | Test one source claim | Matched baseline and explicit configuration | Authorized data, implementation, metrics | Reproduction report | Synthetic/public data first, resource caps, stop rules | Paired metrics, failures, and uncertainty |
| Research decision dashboard | Product or research lead | Compare adoption options | Evidence-confidence-risk matrix | Ledger, costs, constraints | Decision brief and backlog | Human approval, uncertainty labels, no autonomous deployment | Decision usefulness and auditability |

## Three Ways to Exercise This Research

1. **Metadata-to-claim audit:** Select one central source-package statement, map every noun and metric to E1-E3, produce a one-page receipt, and stop if a required source version cannot be identified.
2. **Synthetic matched comparison:** Implement a toy or public-data version of the selected mechanism beside a simple baseline, hold inputs and budgets fixed, report paired outcomes and failures, and stop before using restricted or production data.
3. **Boundary review workshop:** Ask a researcher, implementer, and safety reviewer to score evidence strength, transfer risk, and missing controls independently, reconcile disagreements, and succeed only when unresolved uncertainty remains visible.

## Example MVP Product

- **Product name**: Source-Bound Research Ledger.
- **Target user**: Research reviewer, evaluation engineer, or technical product lead.
- **Problem**: Discovery notes often lose the boundary between source claims, metadata facts, and reviewer interpretation.
- **Core workflow**: Import approved URLs, pin metadata, enter claims, map evidence, record uncertainty, and export a public-safe review receipt.
- **Data requirements**: Public metadata, repository-relative locators, reviewer notes, and optional synthetic evaluation results.
- **Architecture**: Local-first Markdown parser, source registry, evidence graph, validation rules, and signed export bundle.
- **Success metrics**: Source coverage, unsupported-claim rate, reviewer agreement, reproduction backlog completion, and zero sensitive-data leaks.
- **Risk controls**: URL allowlist, no credential capture, public-data default, redaction scan, human approval, and immutable provenance.
- **Limitations**: Does not reproduce empirical results, certify safety, determine legality, or replace domain experts.
- **Deployment model**: Local CLI or review-only web application.
- **Failure modes**: Stale metadata, mistaken source identity, copied unsupported claims, and false confidence from checklist completion.

## Related Research and Reading

### New in this pass: Diagram-MMU: A Multi-Modal Benchmark for Scientific Diagrams

| Item | Type | New evidence inspected | Relevance |
|---|---|---|---|
| [Diagram-MMU: A Multi-Modal Benchmark for Scientific Diagrams](https://arxiv.org/abs/2608.12262v1) | Primary arXiv record | Canonical identity, authorship or credited organization, version/date metadata, categories when available, and public availability | Expands the selected DEP through one cryptographically selected supporting thread. |

### Retained from the selected DEP

| Item | Type | Relevance |
|---|---|---|
| https://arxiv.org/abs/2608.12282 | Retained source-package context | Listed by the selected DEP; not re-opened as the expansion target in this pass. |
| https://github.com/IBM/VAKRA | Retained source-package context | Listed by the selected DEP; not re-opened as the expansion target in this pass. |
| https://huggingface.co/datasets/ibm-research/VAKRA | Retained source-package context | Listed by the selected DEP; not re-opened as the expansion target in this pass. |
| https://arxiv.org/abs/2608.12273 | Retained source-package context | Listed by the selected DEP; not re-opened as the expansion target in this pass. |
| https://arxiv.org/abs/2608.12249 | Retained source-package context | Listed by the selected DEP; not re-opened as the expansion target in this pass. |

## Source References

| ID | Reference | Supports | Access date | Notes |
|---|---|---|---|---|
| R1 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260818-Tech%20Intel%201105/README.md | E1 and selected DEP identity | 2026-08-19 | Live source DEP README inspected. |
| R2 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260818-Tech%20Intel%201105/daily_research_findings_2026-08-18_1105.md | E2 and source-package synthesis | 2026-08-19 | Deposited artifact inspected; claims remain source-qualified. |
| R3 | https://arxiv.org/abs/2608.12262v1 | E3 and selected supporting-source identity | 2026-08-19 | Canonical arXiv Atom record inspected; no source payload redistributed. |

No original PDF, source archive, code repository, dataset, model, benchmark payload, container, credential, private record, or hardware artifact was collected or deposited.

## Appendix

- Batch item: 31 of 50.
- Eligibility cutoff: 2026-08-17T20:49:54Z; candidate count 117; excluded count 32; eligible count 85.
- DEP draw: accepted UInt32 550504538; rejection limit 4294967295; attempts 1; zero-based index 83.
- Supporting draw: pool 13; accepted UInt32 885484915; rejection limit 4294967287; attempts 1; zero-based index 3.
- Prior-material status: No prior same-DEP review marker detected in the inspected repositories.
- Validation boundary: schema, title/H1 identity, required headings, exactly three exercise paths, MVP fields, source-reference coverage, public-output sanitization, and singleton commit contents are checked; empirical reproduction remains out of scope.
