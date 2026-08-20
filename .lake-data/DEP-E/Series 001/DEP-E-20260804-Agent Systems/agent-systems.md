---
title: "Agent Systems - DEP-E"
generated_at: "2026-08-04"
artifact_type: "DEP research artifact"
primary_subject: "Verification-first agent systems and governed technical state"
source_status: "Source package and ten public arXiv records inspected; no original source files collected"
reviewer: "Codex recurring automation"
schema_version: "2026-07-07-expanded"
run_date: "2026-08-04"
source_dep: "Black-Lake-Data/.lake-data/DEP-20260716-Tech Intel 1303"
selection_record: "103 candidates; 2 excluded; 101 eligible; OS-cryptographic draw index 54"
---

# Agent Systems - DEP-E

## Source Metadata

| Field | Value |
|---|---|
| Source DEP | `Black-Lake-Data/.lake-data/DEP-20260716-Tech Intel 1303` |
| Source package | `README.md` and `daily_research_findings_2026-07-16_1303.md` |
| Source package date | 2026-07-16 |
| Review date | 2026-08-04 |
| Artifact class | DEP-E research artifact |
| Source status | Ten public arXiv abstract/metadata records were checked against the source inventory; no original PDFs, source archives, datasets, code repositories, models, or experiment outputs were collected. |
| Selection record | 103 canonical candidates; 2 recent same-family exclusions; 101 eligible; accepted UInt32 `1148443380`; zero-based index 54; eligible-list SHA-256 `49f68bbe78da8a1724150c928b1b9507f04fe38abaccdcf840d201849e303562`. |
| Eligibility cutoff | `2026-08-02T15:01:39Z` |
| Prior-material status | No direct same-family report, Report-Mark, output log, or DEP Class artifact was found for this selected DEP. A separate Smart Coverage Goals artifact references the AgentCompass item as related context only. |
| Research object | Ten source-reported preprint threads spanning agent security, runtime governance, evaluation, memory, medical support, AI-for-science, programming languages, and quantum hardware. |
| Intended use | Follow-on review, replication planning, safe MVP design, and provenance-preserving semantic linking. |

The selected source synthesis was written as a technology-intelligence package. It is not a single paper and does not establish a common experimental comparison. The manuscript therefore preserves each paper as a distinct evidence item and labels cross-domain connections as reviewer interpretation or inference.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | Selected DEP README | Repository source file | Package boundary, tags, inventory, source-collection status, and attribution rules. | Source identity and provenance. | High | The README is a package manifest, not independent research evidence. |
| E2 | Selected DEP findings file | Repository source file | Ten source-reported summaries, source roles, relevance tags, and direct arXiv URLs. | Initial cross-source map and source inventory. | High for inventory; medium for summarized claims | The file is a synthesis and states that claims were not independently reproduced. |
| E3 | [arXiv:2607.14006](https://arxiv.org/abs/2607.14006) | Primary preprint record | Objective-driven behavioral evaluation, influence surfaces, failure criteria, and scenario-based testing. | Objective-level security testing. | Medium | Abstract/metadata depth; no deployment test performed. |
| E4 | [arXiv:2607.13716](https://arxiv.org/abs/2607.13716) | Primary working paper | Canonical action objects, semantic patterns, approval binding, receipt integrity, portability, and a 96-seed/384-variant benchmark. | Runtime governance and auditability. | Medium | Reference implementation and benchmark were not audited or rerun. |
| E5 | [arXiv:2607.13705](https://arxiv.org/abs/2607.13705) | Primary preprint record | Benchmark/Harness/Environment separation, fault-tolerant asynchronous execution, trajectory analysis, and more than 20 benchmarks across five dimensions. | Composable evaluation infrastructure. | Medium | The source package predates the current record's later revisions; current implementation was not inspected. |
| E6 | [arXiv:2607.14004](https://arxiv.org/abs/2607.14004) | Primary technical report | Two-phase continual evaluation; reported lifelong average pass rates of 76.4%, 66.0%, 64.6%, and 58.7% for the compared systems. | Regression-aware optimization. | Medium | Results are source-reported; no Terminal-Bench run or equal-compute replication was performed. |
| E7 | [arXiv:2607.13884](https://arxiv.org/abs/2607.13884) | Primary preprint record | Directed action-decision graphs, graph-edit corrections, memory-graph retrieval, and loop-free evaluation on ALFWorld and ScienceWorld. | Structured failure memory. | Medium | Abstract-level results; transfer to richer tools and environments is untested here. |
| E8 | [arXiv:2607.13940](https://arxiv.org/abs/2607.13940) | Primary preprint record | Governed longitudinal memory, synthetic year-long evaluation, 900 probes, privacy probes, and reported accuracy/context-exposure changes. | Privacy-bounded longitudinal state. | Medium | Offline synthetic evaluation; clinical effectiveness and prospective safety remain open. |
| E9 | [arXiv:2607.13608](https://arxiv.org/abs/2607.13608) | Primary preprint record | LLM-plus-symbolic-regression ODE discovery, admissible variables, mechanistic constraints, and ablation warning against trajectory-only fitting. | Mechanism-aware scientific automation. | Medium | No biological dataset, code, or model was independently inspected. |
| E10 | [arXiv:2607.13220](https://arxiv.org/abs/2607.13220) | Primary preprint record | Active shared context, routed observations and hypotheses, and a biological multi-omics case. | Team-scale context routing. | Medium | The source record has later revisions; the reported campaign is not a broad benchmark. |
| E11 | [arXiv:2607.13921](https://arxiv.org/abs/2607.13921) | Primary preprint record | Sealor transformation, partial-program compiler feedback, Lean-mechanized properties, and repository-level Rust evaluation. | Generation-time verification. | Medium | The reviewed source summary was based on an earlier version; no Rust task reproduction was run. |
| E12 | [arXiv:2607.13834](https://arxiv.org/abs/2607.13834) | Primary experimental preprint record | Wireless resonator excitation at millikelvin temperatures, wired/wireless comparison, and stray-radiation pathways. | Physical boundary conditions for hardware scaling. | Medium | A resonator demonstration is not a complete qubit-control or system-scale interconnect. |

## Executive Summary

The selected DEP's ten records point to a common reviewer hypothesis: dependable agentic systems need explicit boundaries around objectives, actions, evidence, memory, operating conditions, and physical resources. The security records make behavioral objectives and canonical action identity visible; the evaluation records make harnesses, environments, trajectories, and regression control visible; the memory records separate reusable state from private history; and the science, compiler, and quantum records show that domain constraints must remain inspectable rather than being left to unconstrained model output (E3-E12).

The evidence does not justify a claim that these papers form one validated architecture. Several records are preprints or working papers, some have revised arXiv versions after the source package was written, and no code, dataset, hardware, or benchmark was executed in this pass. The durable contribution of this artifact is a provenance-preserving vocabulary for designing and reviewing boundary-bearing systems, not a pooled performance estimate.

## Detailed Summary

### 1. Security and runtime governance

The penetration-testing paper reframes success as inducing a behavior that violates an operational objective under an explicit threat model, including influence through prompts, retrieved content, memory, tools, or human-AI loops (E3). CAVA complements that framing by proposing a canonical action object that can bind approvals, semantic patterns, receipts, and optional attestation across heterogeneous runtimes (E4). Together, the papers suggest that a security review should preserve both the intended objective and the exact action representation that was approved or executed.

### 2. Evaluation and continual reliability

AgentCompass separates benchmark definitions, execution harnesses, and environments, with trajectory analysis for failure modes such as reward hacking (E5). The continual-evaluation study argues that one-shot optimization gains can regress when new tasks arrive and reports the strongest lifelong average for the method with explicit regression control (E6). The reviewer implication is that agent releases need reusable environment contracts, trajectory receipts, and continual gates rather than a single static score.

### 3. Memory, privacy, and shared context

Experience Memory Graph turns failed and successful trajectories into graph edits that can guide a loop-free execution (E7). HealthClaw separates shared safety rules and medical knowledge from private longitudinal memory and reports offline gains in a synthetic setting, including lower prompt-side context exposure and fewer unsafe disclosures (E8). Mycelium extends the idea from one agent to a team: observations and hypotheses are routed to the person, agent, instrument, or robot whose next decision they can inform (E10). These are distinct mechanisms, but all make state selection and routing explicit.

### 4. Scientific, software, and hardware constraints

MEDA uses knowledge-guided formalization and mechanistic constraints so that biologically plausible equations matter in addition to trajectory fit (E9). Generative compilation inserts compiler feedback into partial Rust generation and formalizes key properties in Lean (E11). The wireless-interconnect paper demonstrates a cryogenic feasibility step while exposing stray-radiation pathways that become engineering constraints (E12). In each case, the system's useful boundary is an inspectable constraint that can reject, refine, or contextualize a model output.

## Key Claims and Evidence

| Claim ID | Claim | Classification | Evidence | Reviewer interpretation |
|---|---|---|---|---|
| C1 | Agent security should test whether an operational objective can be violated through model-mediated influence, not only whether infrastructure was compromised. | Author claim | E3 | This broadens the test oracle and requires explicit threat-model and objective registries. |
| C2 | Canonical action identity and approval-bound receipts are a plausible substrate for portable runtime governance. | Author claim plus reviewer interpretation | E4 | Portability is useful only if canonicalization preserves meaningful distinctions and fails closed on ambiguity. |
| C3 | Evaluation infrastructure becomes more reusable when benchmark, harness, environment, and trajectory analysis are separable. | Author claim | E5 | The separation also makes it easier to isolate confounds in downstream replications. |
| C4 | Continual evaluation can reveal regression behavior hidden by one-shot optimization. | Author claim | E6 | The reported result supports a release-gate hypothesis, not a universal ranking across agent optimizers. |
| C5 | Structured memory can trade indiscriminate context replay for targeted correction or privacy-bounded state. | Author claim plus reviewer interpretation | E7-E8 | The transfer boundary is unresolved outside the reported task families and offline settings. |
| C6 | Shared scientific context and mechanistic constraints can make distributed or domain-specific reasoning more actionable. | Author claim plus reviewer interpretation | E9-E10 | The cross-paper link is inferential; the studies use different domains and evaluation designs. |
| C7 | Verification should move closer to generation or execution when late, aggregate checks allow error cascades or hide physical constraints. | Derived inference | E11-E12 | This is a design pattern inferred across software and hardware evidence, not a result jointly tested by the sources. |

## Methodology

- `Research objective`: Convert one randomly selected raw DEP into a schema-complete, provenance-preserving research artifact and identify reusable boundary concepts without pooling incompatible results.
- `Sources inspected`: The selected DEP README, the selected findings Markdown file, the live source and output repository README rules, ten canonical arXiv abstract/metadata records, and one related Black-Lake artifact only to distinguish contextual cross-linking from direct prior material.
- `Discovery strategy`: Enumerated canonical `.lake-data/DEP-*` directories, checked same-family source reports, Report-Mark files, output logs, and output DEP identifiers, then used OS-cryptographic rejection sampling over the sorted eligible list.
- `Inclusion criteria`: The selected DEP's own files and all ten primary records explicitly listed in its findings file.
- `Exclusion criteria`: Recent same-family markers inside the 24-hour cutoff; secondary summaries not needed for the selected source inventory; unreviewed implementation claims; inaccessible or uncollected source files.
- `Analytical approach`: Provenance, conceptual, comparative, implementation, safety/ethics, and replication-boundary analysis.
- `Evidence handling`: Source-file statements are separated from author claims, reviewer interpretation, and derived inference. Quantitative values are retained only as source-reported values with the relevant limitation.
- `Uncertainty handling`: Abstract/metadata-only review is labeled; later arXiv revisions are separated from the versions represented in the source package; missing code, data, experiments, and deployment evidence remain explicit.
- `Artifact mode`: DEP-ready manuscript research artifact and initial synthesis; no iterative supporting-document expansion was selected because no direct prior material existed for this DEP.

## Scope, Constraints, and Assumptions

- `Scope`: Ten research threads about governed agent behavior, evaluation, memory, context routing, scientific constraints, code-generation verification, and cryogenic interconnects.
- `Temporal boundary`: Source package dated 2026-07-16; arXiv record checks performed on 2026-08-04. Current record revisions are noted when visible.
- `Evidence limits`: The repository package contains summaries and URLs, not collected full papers. The review used public arXiv abstract/metadata pages; no PDFs, source archives, code, models, datasets, benchmarks, or hardware were run.
- `Assumptions`: The URLs and titles in the selected findings file are the intended source inventory; each arXiv identifier is treated as a stable locator while version changes are recorded.
- `Constraints`: Public output must contain repository-relative paths and public URLs only; no local system details, private source files, credentials, or machine execution context are preserved.
- `Out of scope`: Clinical deployment, security exploitation, production authorization, benchmark leaderboard claims, statistical recomputation, theorem verification, hardware replication, and legal or regulatory approval.
- `Intended use`: Review planning, safe prototype design, evidence-led architecture discussion, and future DEP expansion.

## Observations

1. The strongest cross-source pattern is explicit state and boundary instrumentation: action identity, objectives, harnesses, memory classes, routed context, mechanistic constraints, compiler diagnostics, and cryogenic coupling paths.
2. The records repeatedly distinguish a useful intermediate representation from raw model text: canonical actions, trajectories, graph edits, memory entries, equations, partial programs, and resonator responses.
3. The source set spans high-stakes domains, but the evidence maturity is uneven. Security and medical claims have meaningful governance implications yet remain preprint or offline evidence here.
4. Version drift matters. AgentCompass, Mycelium, and Generative Compilation show later arXiv versions than the 2026-07-16 source package; the artifact preserves the reviewed source context rather than silently substituting later results.
5. The selected source package contains no original source files. Provenance is therefore URL- and repository-path-based, not archive-based.

## Considerations

Boundary objects can become new failure surfaces. A canonical action schema may collapse distinctions that a policy needs; a memory graph may retain an unsafe or stale correction; a routing layer may send sensitive context to the wrong recipient; a compiler checker may overconstrain valid partial programs; and a wireless link may create electromagnetic paths that a wired design did not expose. Each implementation should therefore emit a receipt containing the input boundary, decision, evidence, rejected alternatives, and operating conditions.

Cross-domain comparison should remain qualitative. A pass-rate percentage, a privacy-probe result, a structural-recovery result, and a cryogenic resonator response cannot be placed on one scale. The safe synthesis is a design vocabulary and a research backlog, not a claim that one technique dominates the others.

Privacy and safety constraints should be designed into the data path. The HealthClaw evidence is explicitly synthetic and offline; the penetration-testing framing is dual-use; and the code-generation and runtime-governance material could be misapplied to real systems. Prototype exercises should use synthetic inputs, isolated environments, bounded actions, and human review before any repository or external-system write.

## Strengths

1. The artifact preserves the selected DEP boundary, source inventory, public URLs, and the distinction between source claims and reviewer synthesis.
2. The evidence ledger makes the heterogeneous source quality visible instead of presenting one pooled confidence score.
3. The synthesis identifies a reusable semantic pattern while keeping security, medical, scientific, software, and hardware claims separate.
4. Implementation ideas are bounded to local, synthetic, auditable, and defensive workflows.
5. Version drift and missing source artifacts are explicitly recorded for follow-on reviewers.

## Weaknesses

1. No full paper, code repository, dataset, model, benchmark, or hardware artifact was independently executed or audited.
2. Most evidence depth is abstract/metadata level, so method details and negative results may be incomplete.
3. The source package is a dated technology-intelligence snapshot; later versions may change titles, claims, metrics, or implementation availability.
4. Cross-domain connections are reviewer interpretations and may not survive focused replication.
5. The artifact does not establish deployment readiness, clinical safety, secure authorization, or performance parity.

## Potential Improvements

| Improvement | Target | Rationale | Validation approach |
|---|---|---|---|
| Pin reviewed versions | Evidence provenance | Later arXiv revisions can change methods or results. | Record versioned URLs and compare abstract, method, and result deltas. |
| Add source-depth tiers | Evidence quality | Abstract-only and full-text evidence should not look equivalent. | Reclassify each item after full-text inspection and attach section-level evidence IDs. |
| Build a boundary-receipt schema | Cross-source reuse | The common pattern needs a machine-readable representation. | Validate receipts against synthetic action, memory, context, compiler, and hardware fixtures. |
| Reproduce one metric per cluster | Replication | A small set of independent checks would anchor the synthesis. | Select one security, evaluation, memory, science, software, and hardware claim with pinned inputs. |
| Add failure and counterexample cases | Safety | Boundary mechanisms can fail through ambiguity, stale state, or leakage. | Construct adversarial but non-exploitative synthetic cases and require fail-closed behavior. |

## Potential Implementations

### 1. Boundary Receipt Gateway

- `User`: Agent-platform or security-review team.
- `Goal`: Record what an agent intended, what action was canonicalized, what policy allowed it, and what evidence was attached.
- `Core mechanism`: Convert a bounded action request into a canonical object, bind approval to a hashable receipt, and reject ambiguous or unsupported action shapes.
- `Required inputs`: Synthetic action catalog, policy rules, approval token, execution context, and evidence references.
- `Outputs`: Public-safe receipt, decision status, reason code, and replay fixture.
- `Risk controls`: No credentials or private payloads in receipts, fail-closed unknown actions, isolated execution, human approval for writes, and schema validation.
- `Evaluation`: Semantic-equivalence tests, wrapper-bypass fixtures, approval-binding checks, deterministic replay, and receipt-integrity checks.

### 2. Continual Agent Evaluation Ledger

- `User`: Agent-evaluation researcher or release engineer.
- `Goal`: Detect regressions when a harness or optimizer is updated with new tasks.
- `Core mechanism`: Separate benchmark, harness, and environment versions; store trajectory-level outcomes; compare static and continual gates under matched budgets.
- `Required inputs`: Public toy tasks, pinned runtime versions, fixed seeds, tool traces, and baseline policies.
- `Outputs`: Versioned evaluation ledger, failure taxonomy, regression decision, and bounded remediation queue.
- `Risk controls`: Synthetic or public tasks only, no autonomous production actions, fixed resource budgets, privacy-safe traces, and manual release approval.
- `Evaluation`: Transfer performance, regression rate, task coverage, trace completeness, cost, and reviewer agreement.

### 3. Governed Context and Mechanism Lab

- `User`: AI-for-science or code-generation research team.
- `Goal`: Compare targeted context routing and domain constraints against indiscriminate context replay or unconstrained generation.
- `Core mechanism`: Route synthetic observations to typed recipients, preserve provenance, apply mechanistic or compiler checks, and record rejected hypotheses or partial programs.
- `Required inputs`: Synthetic scientific records, toy equations, partial Rust-like programs, typed context graph, and constraint rules.
- `Outputs`: Decision-linked context graph, constraint receipt, accepted/rejected candidate, and review report.
- `Risk controls`: No clinical or proprietary data, no executable unreviewed code, bounded compiler calls, local-only processing, and explicit uncertainty labels.
- `Evaluation`: Provenance completeness, constraint precision/recall, useful-context rate, false rejection rate, and reproducibility of the final receipt.

## Three Ways to Exercise This Research

1. `Synthetic action-governance replay`: Create a small catalog of semantically equivalent and intentionally distinct actions, bind approvals to canonical receipts, and test that ambiguous or wrapper-altered actions fail closed. Success requires deterministic identity and an evidence trail for every decision.
2. `Continual-evaluation microbenchmark`: Use public or synthetic tasks with pinned harness and environment versions; compare one-shot and continual updates under equal budgets; inspect transfer, regression, and trajectory receipts. Stop if the test cannot separate task, harness, and environment changes.
3. `Context-and-constraint sandbox`: Route synthetic scientific observations and partial code snippets through typed context and mechanistic/compiler checks; compare targeted routing with full-history replay and unconstrained generation. Success requires provenance completeness and a documented reason for every accepted or rejected candidate.

## Example MVP Product

- `Product name`: Boundary Ledger Lab.
- `Target user`: Agent-evaluation researcher, safety reviewer, or AI-for-science platform designer.
- `Problem`: Agent experiments often mix objectives, actions, context, evidence, and operating conditions, making failures hard to reproduce or govern.
- `Core workflow`: Import a synthetic task and action catalog; version the benchmark, harness, environment, and context graph; emit boundary receipts; run bounded checks; compare decisions and failures; export a public-safe review report.
- `Data requirements`: Synthetic actions, policy rules, task definitions, typed context items, evidence references, version identifiers, and optional public benchmark results.
- `Architecture`: Local-only CLI or notebook; receipt schema; deterministic policy engine; pluggable benchmark/harness/environment adapters; graph-backed context store; static Markdown/HTML report.
- `Success metrics`: Receipt completeness, deterministic replay rate, protected-action rejection accuracy, regression detection rate, provenance coverage, reviewer time to decision, and zero private-data findings.
- `Risk controls`: Synthetic/public data by default, no credentials, no automatic external writes, bounded subprocesses, fail-closed unknowns, human approval, and staged public-output sanitization.
- `Limitations`: The MVP cannot establish clinical safety, production security, generalization, or hardware feasibility; it tests the evidence and governance plumbing around toy tasks.

## Related Research and Reading

### Primary records retained from the selected DEP

| Item | Relevance to this artifact | Version note |
|---|---|---|
| [Rethinking Penetration Testing for AI-Enabled Systems](https://arxiv.org/abs/2607.14006) | Defines objective-driven behavioral evaluation and influence-surface mapping for AI-enabled systems. | v1 record reviewed. |
| [CAVA: Canonical Action Verification and Attestation](https://arxiv.org/abs/2607.13716) | Provides an action-level identity, approval, receipt, and portability vocabulary. | v1 working-paper record reviewed. |
| [AgentCompass](https://arxiv.org/abs/2607.13705) | Separates benchmark, harness, and environment while adding trajectory diagnosis. | Selected DEP used the early record; the current page shows later revisions. |
| [Do Agent Optimizers Compound?](https://arxiv.org/abs/2607.14004) | Tests transfer and regression across continual optimization. | v1 technical-report record reviewed. |
| [Experience Memory Graph](https://arxiv.org/abs/2607.13884) | Represents failures and corrections as reusable action-decision graph edits. | v1 record reviewed. |
| [HealthClaw](https://arxiv.org/abs/2607.13940) | Separates shared medical/safety knowledge from private longitudinal memory. | v1 record reviewed; code link is source-reported and was not audited. |
| [MEDA](https://arxiv.org/abs/2607.13608) | Uses mechanistic constraints with symbolic regression for biological ODE discovery. | v1 record reviewed. |
| [Mycelium](https://arxiv.org/abs/2607.13220) | Routes observations and hypotheses through a shared human-AI scientific context. | Selected DEP used the early record; the current page shows later revisions. |
| [Generative Compilation](https://arxiv.org/abs/2607.13921) | Moves compiler feedback into partial-program generation and formalizes key properties. | Selected DEP used the early record; the current page shows a later revision. |
| [Wireless millikelvin interconnects](https://arxiv.org/abs/2607.13834) | Demonstrates a cryogenic interconnect feasibility step and exposes stray-radiation constraints. | v1 record reviewed. |

This is an initial synthesis, not an iterative supporting-document expansion. No new supporting thread was randomly selected because no direct prior material existed for the selected DEP. The separate Smart Coverage Goals artifact is retained only as a contextual repository link for AgentCompass and is not treated as evidence for the ten source records.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260716-Tech%20Intel%201303/README.md | E1, source package identity and attribution | 2026-08-04 | Repository-relative source package; no local path published. |
| R2 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260716-Tech%20Intel%201303/daily_research_findings_2026-07-16_1303.md | E2, ten-item inventory and source-reported summaries | 2026-08-04 | Source synthesis; not a substitute for independent reproduction. |
| R3 | https://arxiv.org/abs/2607.14006 | E3, objective-driven behavioral security testing | 2026-08-04 | v1 record; abstract/metadata inspected. |
| R4 | https://arxiv.org/abs/2607.13716 | E4, canonical action verification and attestation | 2026-08-04 | v1 working-paper record; abstract/metadata inspected. |
| R5 | https://arxiv.org/abs/2607.13705 | E5, modular evaluation infrastructure | 2026-08-04 | Source package reflects an early record; current page shows v3. |
| R6 | https://arxiv.org/abs/2607.14004 | E6, continual optimizer evaluation | 2026-08-04 | v1 technical-report record; source-reported percentages only. |
| R7 | https://arxiv.org/abs/2607.13884 | E7, graph-based experience memory | 2026-08-04 | v1 record; abstract/metadata inspected. |
| R8 | https://arxiv.org/abs/2607.13940 | E8, governed longitudinal health memory | 2026-08-04 | v1 record; abstract/metadata inspected; clinical use is out of scope. |
| R9 | https://arxiv.org/abs/2607.13608 | E9, mechanistic ODE discovery | 2026-08-04 | v1 record; abstract/metadata inspected. |
| R10 | https://arxiv.org/abs/2607.13220 | E10, active shared scientific context | 2026-08-04 | Source package reflects an early record; current page shows v3. |
| R11 | https://arxiv.org/abs/2607.13921 | E11, generation-time compiler feedback | 2026-08-04 | Source package reflects an early record; current page shows v2. |
| R12 | https://arxiv.org/abs/2607.13834 | E12, wireless cryogenic interconnects | 2026-08-04 | v1 record; abstract/metadata inspected. |
| R13 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-Smart%20Coverage%20Goals/smart_coverage_goals_manuscript.md | Contextual relation only | 2026-08-04 | Separate artifact that cites AgentCompass; not evidence for this selected source package. |

## Appendix

### Public provenance and validation boundary

- `Source files collected`: None. The public artifact preserves repository-relative paths and canonical URLs only.
- `Source package reviewed`: The selected DEP README and findings file were inspected before the external records.
- `External review depth`: Public arXiv abstract/metadata records, titles, authors, submission/version history, and source-relevant abstract claims were checked. Full-paper PDFs, source archives, code, models, datasets, and hardware were not collected or executed.
- `Missing evidence`: Independent statistical verification, code audit, dataset inspection, benchmark replay, theorem verification, clinical validation, physical replication, and production-readiness assessment.
- `Sanitization boundary`: Public files contain no local absolute paths, home directories, usernames, machine identifiers, local timezone labels, or exact local execution timestamps.
- `Follow-on rule`: A later pass may add a new Report-Mark and a new DEP-E artifact or correction note; it must preserve this artifact's source URLs, evidence limits, and version distinctions.
