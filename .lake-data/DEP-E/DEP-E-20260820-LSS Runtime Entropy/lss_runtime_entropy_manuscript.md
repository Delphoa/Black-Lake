---
title: "LSS Runtime Entropy - DEP-E"
generated_at: "2026-08-20"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of Loosely-Structured Software for runtime-generated and evolving multi-agent systems."
source_status: "source files collected locally and withheld; public URLs cited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-20"
temporal_cutoff: "arXiv:2603.15690v1 and related repository entries inspected through 2026-08-20"
primary_url: "https://arxiv.org/abs/2603.15690"
stable_identifier: "arXiv:2603.15690v1; DOI:10.48550/arXiv.2603.15690"
confidence_summary: "High for source identity and reported method/evaluation details; medium for transfer because results were not independently reproduced."
safety_scope: "bounded, defensive, evaluation-only implementation planning"
distribution_notes: "PDF, HTML, metadata, extracted text, cache, verification records, and source package were withheld locally."
---

# LSS Runtime Entropy - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv metadata record | Primary source | HTML | arXiv:2603.15690v1 | https://arxiv.org/abs/2603.15690 | CC BY 4.0 shown on the arXiv HTML record | 2026-08-20 | Inspected |
| S2 | Full paper | Primary source | HTML | arXiv:2603.15690v1 | https://arxiv.org/html/2603.15690 | Full paper inspected; source file withheld | 2026-08-20 | Verified complete and inspected |
| S3 | Persistent identifier | Identity source | DOI | 10.48550/arXiv.2603.15690 | https://doi.org/10.48550/arXiv.2603.15690 | ArXiv-issued DOI | 2026-08-20 | Resolved |
| S4 | Local source and cache records | Processing evidence | PDF, HTML, JSON, text | Selected archive unit and central cache | Public paths intentionally omitted | Source files and derived cache withheld | 2026-08-20 | Integrity and cache checks passed |
| S5 | Agent Reliability Gates - DEP-E | Related DEP | Markdown | Black Lake repository-relative entry | `.lake-data/DEP-E/DEP-E-20260728-Agent Reliability Gates/agent-reliability-gates.md` | Derived synthesis only | 2026-08-20 | Inspected |
| S6 | Agent Context - DEP-E | Related DEP | Markdown | Black Lake repository-relative entry | `.lake-data/DEP-E/DEP-E-20260815-Agent Context Systems/agent-context-systems.md` | Derived synthesis only | 2026-08-20 | Inspected |
| S7 | Agent Systems - DEP-E | Related DEP | Markdown | Black Lake repository-relative entry | `.lake-data/DEP-E/DEP-E-20260804-Agent Systems/agent-systems.md` | Derived synthesis only | 2026-08-20 | Inspected |

The local source state was initially partial because the PDF was present without full-paper HTML. One bounded repair produced a verified PDF/full-paper HTML pair before review. The source package was unavailable. No source file, cache, extracted text, or local path is redistributed in this manuscript.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Title, authors, submission date, version, subjects, DOI, and license | Work identity and provenance | High | Metadata does not establish empirical validity |
| E2 | S2 | Primary paper | LSS definition, runtime elements, execution primitives, and three-layer framework | Conceptual model and mechanism | High | Framework is partly normative and high-level |
| E3 | S2 | Primary paper | View/Context, Structure, and Evolution design principles and patterns | Implementation implications | High | Pattern transfer across stacks was not independently tested |
| E4 | S2 | Primary paper | RepoBench-R setup, three retrieval variants, Hit@5, Top-1 Accuracy, context tokens, and token-cost trade-off | Quantitative evidence for context routing | High for transcription; medium for replication | Results are source-reported; API, candidate pool, and prompts were not recovered |
| E5 | S2 | Primary paper | File-based research workflow, 10 rounds, task cap, 23 generated skills, subjective review, human control points | Workflow evidence and limitations | Medium-high | Not a standardized end-to-end benchmark |
| E6 | S4 | Local processing record | Complete-source verification and `missing-only` cache with pypdf/html-regex | Processing methodology and locality | High for process status | Private records are not publicly inspectable |
| E7 | S5-S7 | Related DEP entries | Verification gates, context controls, routed state, and generation-time checks | Related conceptual bridge | Medium | Related entries are syntheses, not a joint experiment |

## Executive Summary

The paper proposes Loosely-Structured Software (LSS), a paradigm for multi-agent systems whose effective program is assembled from runtime Views, semantic bindings, and rewritable Artifacts. Its three-layer framework assigns engineering responsibility to View/Context Engineering, Structure Engineering, and Evolution Engineering, corresponding to Context Entropy, Self-Organization Entropy, and Evolutionary Entropy (E2-E3).

The clearest empirical support is bounded context routing on RepoBench-R. With the same DeepSeek API and a top-5 candidate budget, Lens+Worker raises Hit@5 from `0.70` to `0.78`, and Lens+Index+Worker reaches `0.84`; Top-1 Accuracy remains `0.10–0.12`. Worker input context falls from `1,543` tokens to `1,395` or about `1,422`, but total token cost rises because selection is externalized (E4). The broader workflow evaluation is informative but not standardized: it uses 10 rounds, at most 10 tasks per round, 23 generated skills, one basic experiment-agent round, and subjective reviewer scores with human control points (E5).

Reviewer assessment: LSS is most useful as a design vocabulary and replication target for making runtime flexibility observable, scoped, reversible, and provenance-bearing. It is not evidence that unconstrained self-evolution is safe or that the reported gains transfer to production without independent evaluation.

## Detailed Summary

### Problem context

LLM-based multi-agent systems increasingly search, plan, code, and iterate through free-form interactions. The paper argues that adding agents can amplify context pressure, coordination errors, communication overhead, and system drift. The problem is therefore architectural: how to govern what an agent sees, which capability it binds to, and how persistent artifacts change over repeated use (E2).

### LSS model

LSS describes an agentic system using four runtime elements:

- **Intent (`I_t`)** — the explicit objective or subtask.
- **Global Artifacts (`A_t`)** — prompts, skills, plans, code, tool registries, contracts, traces, documents, memories, and other persistent files.
- **View (`V_t`)** — the task-specific projection of artifacts and history injected into the model context.
- **Output (`O_t`)** — generated content, actions, and environmental feedback.

The execution cycle uses four primitives: `Project` constructs a View, `Execute` produces an Output, `Update` evolves the Artifact set, and `Formulate` creates the next Intent. The paper emphasizes that these primitives can be split across specialized agents, so one agent’s output can become another agent’s View (E2).

### Three engineering layers

**View/Context Engineering** governs Context Entropy. The paper recommends minimal-sufficient disclosure, adaptive context expansion, context backpressure, branching and stitching, and per-step isolation. The Semantic Lens retrieves and composes a compact View; the Context Curator distills history; the Mediator negotiates a clean task-specific contract; and End Criteria define when an ephemeral agent can retire (E3).

**Structure Engineering** governs Self-Organization Entropy. Binding can miss, bind to the wrong artifact or agent, or bind too much. Task-scoped modularity, binding provenance, and “structure as ability” are proposed as controls. Semantic Router, Index Generator, Team Generator, Inheritance Generator, Supply Chain, and Facade & Filter patterns turn runtime binding into a more inspectable operation (E3).

**Evolution Engineering** governs Evolutionary Entropy. Persistent self-modification can be too slow, too active, or misaligned. Sandbox Mode, Evolver, Semantic Palimpsest, Artifact Maintainer, Artifact Tiering, and Shared Interaction Space are proposed to bound blast radius, preserve history, consolidate artifacts, and retain human acceptance signals (E3).

### RepoBench-R evaluation

The paper uses the Python `python_cff` test-easy split of RepoBench-R. Each query begins with a lexical candidate pool and each variant selects five snippets. Candidate briefs are limited to 280 characters and worker-side reads to 700 characters per selected item. The comparison is:

1. Worker-only retrieval, where one Worker scans candidates and selects the top five.
2. Lens+Worker, where a Lens selects candidates from brief evidence and the Worker reads only those items.
3. Lens+Index+Worker, where an Index Generator creates compact descriptions before Lens selection.

The reported Hit@5 values are `0.70`, `0.78`, and `0.84`. Top-1 Accuracy stays low at `0.10–0.12`. Average Worker context falls from `1,543` tokens for Worker-only to `1,395` with Lens+Worker and about `1,422` with Lens+Index+Worker. Total token cost increases for Lens-assisted variants, with the paper arguing that index-generation cost can be amortized when candidate sets are reused (E4).

### Comprehensive workflow evaluation

The second evaluation uses a file-based project knowledge base containing atomic ideas, references, experiment records, decisions, and drafts. A user Intent becomes `task.md` work items in a Task Pool; a reviewer/controller generates and routes tasks; Workers append outputs and logs to a Result Memory; and the reviewer accepts or issues another round (E5).

For the replay, the Task Generator was capped at 10 tasks per round and the run used 10 rounds. Worker Agents performed writing, literature research, basic experiments, and figure-prompt generation. The experiment agent was limited to a single round, 23 skills were generated, and the semantic router was bypassed in this simplified evaluation. The authors explicitly state that human review and fine-grained intervention remain necessary and that a standardized “good research” metric is difficult (E5).

### Limitations

The paper presents a high-level design language rather than an exhaustive implementation catalogue. The RepoBench-R evaluation is tied to a single benchmark split, model/API configuration, candidate budget, and prompt/evidence limits. The workflow evaluation is interactive, open-ended, and partly subjective. No official code repository was identified from the arXiv record or repository search, and no experiment was independently rerun in this review. Source-package unavailability also prevents source-level inspection of implementation details.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | LSS is a software paradigm characterized by runtime View construction, semantic binding, and endogenous Artifact evolution. | Author claim | E2; full HTML sections 1 and 3 | Directly supported as the paper’s definition; external generality remains open. | High |
| C2 | The View, Structure, and Evolution layers provide a framework for governing three forms of runtime entropy. | Author claim | E2-E3; full HTML sections 3-6 | The framework is clearly articulated and internally coherent, but its governance effect is mostly conceptual. | High |
| C3 | Lens and Index mechanisms improve recall-oriented retrieval and reduce or bound Worker context in the reported RepoBench-R setup. | Author-reported empirical claim | E4; full HTML section 8.1 | Exact values are traceable in the HTML; reproducibility and transfer are unverified. | Medium-high |
| C4 | Lens-assisted routing increases total token cost but can make index overhead amortizable. | Author interpretation | E4; full HTML section 8.1 | Plausible for reused candidate sets; requires workload-level cost accounting. | Medium |
| C5 | The comprehensive LSS workflow demonstrates a reliable general research automation method. | Implied author claim | E5; full HTML section 8.2 | Not established: the paper reports subjective scores, limited experimentation, and ongoing human control. | Low-medium |
| C6 | Provenance, sandboxing, rollback, and external acceptance should be treated as first-class controls for runtime evolution. | Reviewer interpretation | E3, E5, and E7 | Strong implementation implication, not a measured result of this paper. | Medium |

## Methodology

- `Research objective`: Preserve and assess the paper’s proposed LSS vocabulary, primary evidence, limitations, and safe implementation relevance for agentic systems.
- `Sources inspected`: Official arXiv metadata and full HTML, locally retained and verified PDF/HTML source material through the extraction cache, local archive verification records, the arXiv-issued DOI, and exactly three related Black Lake DEP manuscripts.
- `Discovery strategy`: Enumerated PDF-backed local archive units with `rg --files -g "*.pdf"`; selected one parent unit uniformly with PowerShell `Get-Random`; checked the public dedup index, local logs/reports/DEPs, automation memory, and Black-Lake-Data search results; then reviewed primary source sections and related repository entries.
- `Inclusion criteria`: Full-paper sources had to pass the local PDF and full-paper HTML integrity gate. Evidence was included when it directly supported identity, method, evaluation, limitation, or implementation implications.
- `Exclusion criteria`: Abstract-only evidence was not used for method or result claims; source files, cache contents, and local paths were excluded from public artifacts; no unverified code, data, or benchmark claims were promoted to facts.
- `Analytical approach`: Conceptual, empirical, comparative, implementation, safety/ethics, product research, and replication planning.
- `Evidence handling`: Claims were mapped to evidence IDs and official source URLs. Author claims, reported measurements, reviewer interpretations, and implementation sketches are labeled separately.
- `Uncertainty handling`: Missing source package, absent official code, non-reproduced measurements, API dependence, subjective workflow scoring, and transfer limits remain explicit.
- `Extraction process`: Extractor preflight found `pypdf` and HTML support but no `pdftotext`. The selected paper began as a cache miss and was processed in local-first `missing-only` mode; PDF and HTML text were cached, while source text was unavailable.
- `Version control`: Review is pinned to arXiv v1, submitted 2026-03-16, with the arXiv HTML record and DOI used as stable public locators.
- `Claim selection`: Prioritized the paradigm definition, runtime formalization, three-layer framework, strongest quantitative results, workflow evaluation, limitations, and implementation implications.
- `Cross-checking`: Cross-checked arXiv metadata against the full HTML and local verification records; source-reported metrics were not independently rerun.
- `Safety handling`: Implementation examples are local, bounded, non-networked decision-logic sketches. Runtime evolution is framed with sandboxing, rollback, provenance, permissions, and external checks.
- `Reviewer stance`: Source-grounded summary, critique, implementation brief, DEP-ready artifact, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: The LSS definition, runtime elements and primitives, three engineering layers, design patterns, two reported evaluations, limitations, related DEP bridge, and safe implementation implications.
- `Temporal boundary`: Sources and related repository entries inspected on 2026-08-20; primary paper version is arXiv:2603.15690v1.
- `Evidence limits`: No source package or official code repository was available; no API, benchmark, workflow, or figure reproduction was performed; full-paper evidence depends on the inspected arXiv rendering and local verified source copy.
- `Assumptions`: The arXiv v1 HTML and PDF represent the same paper version; the reported RepoBench-R values are transcribed as shown; repository-relative related entries remain stable enough for this deposit.
- `Constraints`: Source locality and copyright policy prohibit public redistribution of paper files, extracted text, caches, or local paths. Examples must not mutate real agent artifacts or invoke external tools.
- `Out of scope`: Production deployment, autonomous self-modification, security exploitation, clinical use, legal conclusions, independent benchmark reproduction, and claims of general reliability.
- `Intended use`: Research review, follow-on replication planning, bounded MVP design, and provenance-preserving DEP deposition.
- `Audience`: Agent-system engineers, research reviewers, evaluation designers, and maintainers of evidence-bearing knowledge artifacts.
- `Reproducibility boundary`: A later reviewer can locate the public paper and reproduce the artifact structure, but cannot reproduce the reported numbers without the stated benchmark inputs, API configuration, prompts, and implementation details.
- `Operational boundary`: Discuss runtime routing and evolution conceptually and in safe local sketches only; do not grant arbitrary write or tool permissions.
- `Data sensitivity`: Public paper metadata and public repository-derived Markdown; private source files and local processing records withheld.

## Observations

- `Observed pattern`: The paper treats context as an executable slice, not merely a prompt payload; this makes retrieval, compression, routing, and provenance part of program behavior.
- `Technical implication`: Context reduction and retrieval quality are not monotonic substitutes. Lens+Index improves Hit@5 while Top-1 remains low and total token cost rises, so evaluation must measure recall, precision, context pressure, and orchestration cost together.
- `Observed pattern`: The same artifact can be a View, Output, contract, or evolving capability depending on the agent and step. Stable lineage is therefore more valuable than a single static role label.
- `Contradiction or tension`: The paper advocates runtime adaptability while acknowledging that human review is still required for research workflows; the missing bridge is an independently checked acceptance layer.
- `Reviewer hypothesis`: The most practical LSS deployment boundary is a governed control plane around model calls, with external checks deciding what context enters, what bindings persist, and which patches graduate.
- `Open question`: Whether the three entropy categories can be measured with shared telemetry rather than used only as design metaphors remains unresolved.

## Considerations

Adoption requires more than implementing a semantic router. Teams need versioned schemas for artifacts and contracts, clear authority over writes, trace retention, cost budgets, and a way to compare candidate Views without leaking sensitive history. Context backpressure can reduce overload but may omit a critical constraint; a safe system should expose abstention and request escalation rather than silently compressing. Dynamic bindings also complicate debugging because a failure may come from a wrong artifact, a wrong route, or a stale evolution patch. For long-lived systems, retention and deletion policy are governance choices, not housekeeping. These concerns align with the related reliability and context DEP entries, but their cross-domain evidence is heterogeneous and not a pooled validation.

## Strengths

- Provides a compact vocabulary for three coupled sources of agent-system instability.
- Makes runtime context construction and semantic binding explicit architectural events.
- Connects design patterns to concrete artifacts such as indexes, contracts, teams, tasks, and evolution records.
- Reports interpretable retrieval metrics and token-context measurements rather than only an aggregate success score.
- Acknowledges human review, open-ended exploration, subjective scoring, and implementation scope limits.

## Weaknesses

- The central concepts are high-level and can overlap with existing context engineering, orchestration, memory, and software architecture practices.
- RepoBench-R evidence is narrow and source-reported; the exact implementation, API behavior, prompts, and candidate artifacts were not available for reproduction.
- Top-1 retrieval remains low, so improved Hit@5 does not establish precise routing or downstream task success.
- The comprehensive workflow evaluation uses subjective review and a simplified configuration that bypasses the Semantic Router.
- No official code repository or source package was available for implementation audit.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release a pinned reference implementation and benchmark manifest | Reproducibility | Bind prompts, candidate pools, model/API, token limits, and seeds to a versioned run | Makes the RepoBench-R claims independently testable | Maintenance and provider drift | Re-run all three variants with matched budgets and public fixtures |
| Add route-level and evolution-level external graders | Evaluation | Separate retrieval recall from binding correctness, task success, and safe patch acceptance | Converts entropy metaphors into measurable transition outcomes | Grader design can add cost or bias | Use held-out tasks, replay, human audit, and failure taxonomy |
| Compare governed versus unconstrained evolution over long horizons | Safety and lifecycle | Test whether sandbox, rollback, provenance, and tiering actually reduce drift | Establishes boundary conditions for self-modification | Long runs and expensive traces | Pre-register drift, rollback, regression, and cost metrics |

## Potential Implementations

1. **Evidence-bearing context gateway**: user is an agent runtime; goal is to construct a minimal task View; inputs are an Intent, artifact index, and budget; output is a selected View plus provenance and abstention reason; risk controls are schema validation, redaction, read-only defaults, and maximum context/cost budgets; evaluation compares retrieval recall, omission rate, downstream task success, and cost.
2. **Reversible artifact evolution service**: user is a platform engineer; goal is to safely improve skills, routing rules, or indexes; inputs are a candidate patch and replay corpus; output is a signed proposal, check report, and rollback pointer; risk controls are sandbox isolation, external tests, human approval for persistent writes, and automatic revert; evaluation measures regression rate, helpful-change rate, drift, and blast radius.
3. **Agent-workspace lifecycle manager**: user is a research or engineering team; goal is to keep task state navigable across hot, warm, and cold tiers; inputs are tasks, evidence records, traces, and retention policies; output is a linked index, task ledger, and archive; risk controls are access scopes, retention limits, source redaction, and provenance-preserving moves; evaluation measures discovery time, duplicate rate, stale-state rate, and audit completeness.

## Three Ways to Exercise This Research

1. **Synthetic retrieval gate**: create a small public code corpus with known cross-file links; compare Worker-only, Lens+Worker, and Lens+Index+Worker using deterministic lexical candidates; output Hit@5, Top-1, context tokens, and cost; success is a reproducible comparison with a clear abstention rule; stop if candidate identity or ground truth is ambiguous.
2. **Sandboxed evolution replay**: use synthetic task files and two competing skill versions; generate candidate patches in a temporary local directory, replay fixed tests, and retain only accepted diffs with rollback metadata; success is zero uncontrolled persistent writes and a complete evidence ledger; stop on any failed isolation or missing rollback record.
3. **Binding provenance audit**: build a local router over three mock capabilities with incompatible schemas; issue labeled intents, record route evidence, and inject safe unknown intents; output route traces and abstention counts; success is complete provenance for every route and no guessed route for unknown inputs; stop before adding live tools or external data.

## Example MVP Product

- `Product name`: ViewGuard Research Gateway
- `Target user`: Teams operating multi-agent research, coding, or knowledge workflows.
- `Problem`: Agents receive too much or too little context, bind to poorly matched capabilities, and evolve shared artifacts without an auditable acceptance path.
- `Core workflow`: An Intent enters a local gateway; a Semantic Lens selects a bounded View; a Router records the binding decision; a Worker produces a candidate Output; an external checker validates the result; only approved summaries or patches enter the warm artifact store.
- `Data requirements`: Synthetic or public task descriptions, a versioned artifact index, route schemas, evaluation fixtures, provenance fields, and retention metadata. No private prompt corpus is required for the MVP.
- `Architecture`: Local CLI or service with read-only artifact index, deterministic pre-filter, optional model-assisted ranking, provenance ledger, sandbox directory, checker interface, and append-only decision record.
- `Success metrics`: Hit@5 and Top-1 on a labeled toy corpus; context-token reduction; route abstention precision; acceptance/regression rate for synthetic patches; audit completeness; and per-task cost.
- `Risk controls`: No external side effects by default; allowlisted paths; schema and size limits; secret redaction; sandbox-only writes; human approval for persistence; rollback pointer for every accepted change; and explicit uncertainty/abstention.
- `Limitations`: Toy data and local checks do not establish production reliability, model-independence, safety of autonomous evolution, or transfer to private enterprise repositories.
- `MVP boundary`: Excludes autonomous external tool calls, unrestricted self-rewriting, private-data ingestion, and deployment decisions.
- `Deployment model`: Local-only CLI or notebook with exported Markdown/JSON evidence records.
- `Evaluation plan`: Deterministic smoke tests, labeled routing fixtures, patch replay, negative/abstention cases, and manual audit of provenance traces.
- `Failure modes`: Missing critical context, false route confidence, stale index, checker blind spot, cost blow-up, and rollback metadata loss.
- `Maintenance plan`: Version route schemas and fixtures; review accepted patches; expire stale indexes; monitor extraction and evaluator drift; and re-run the toy benchmark after dependency or model changes.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Agent Reliability Gates - DEP-E | Related DEP | Verification, routing, memory, auditability, rejection, and intervention controls around agent inference | `.lake-data/DEP-E/DEP-E-20260728-Agent Reliability Gates/agent-reliability-gates.md` |
| Agent Context - DEP-E | Related DEP | Context selection, runtime access plans, memory interference, and independent acceptance boundaries | `.lake-data/DEP-E/DEP-E-20260815-Agent Context Systems/agent-context-systems.md` |
| Agent Systems - DEP-E | Related DEP | Active shared context, routed state, structured failure memory, and generation-time verification | `.lake-data/DEP-E/DEP-E-20260804-Agent Systems/agent-systems.md` |
| arXiv full paper | Primary source | Full LSS framework, patterns, evaluation, and limitations | https://arxiv.org/html/2603.15690 |
| RepoBench | Benchmark context | Repository-level code completion and retrieval setting used by the paper | https://arxiv.org/abs/2306.03091 |
| Lost in the Middle | Context context | Evidence for long-context ordering and utilization limits cited by the paper | https://arxiv.org/abs/2307.03172 |
| Model Context Protocol | Interoperability context | Typed tool/data interface context cited by the paper | https://modelcontextprotocol.io/ |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2603.15690 | Title, authors, date, subjects, DOI, license, abstract, and version | 2026-08-20 | Official metadata record; abstract not used alone for result claims |
| R2 | https://arxiv.org/html/2603.15690 | Full method, runtime model, patterns, RepoBench-R evaluation, workflow evaluation, limitations, and conclusion | 2026-08-20 | Official full-paper HTML inspected |
| R3 | https://doi.org/10.48550/arXiv.2603.15690 | Persistent identifier | 2026-08-20 | ArXiv-issued DOI |
| R4 | `.lake-data/DEP-E/DEP-E-20260728-Agent Reliability Gates/agent-reliability-gates.md` | Related verification and gate concepts | 2026-08-20 | Repository-relative derived entry; no source files redistributed |
| R5 | `.lake-data/DEP-E/DEP-E-20260815-Agent Context Systems/agent-context-systems.md` | Related context, access-plan, memory, and acceptance concepts | 2026-08-20 | Repository-relative derived entry; no source files redistributed |
| R6 | `.lake-data/DEP-E/DEP-E-20260804-Agent Systems/agent-systems.md` | Related routed state and generation-time verification concepts | 2026-08-20 | Repository-relative derived entry; no source files redistributed |
| R7 | Local source and cache records | Integrity, extraction, and source-locality status | 2026-08-20 | Local paths and source payloads intentionally omitted |

## Appendix

### Replication Checklist

- Obtain the exact RepoBench-R Python `python_cff` test-easy split and gold snippet identifiers.
- Pin the three retrieval variants, candidate budget `K=5`, 280-character candidate briefs, and 700-character Worker reads.
- Record model/provider/API version, prompt templates, temperature, retries, seeds, and token accounting.
- Report Hit@5, Top-1 Accuracy, Worker context tokens, total token cost, and per-query traces.
- Add a deterministic synthetic benchmark for View omission, binding miss, binding wrong, and binding too much.
- Evaluate sandboxed artifact evolution with replay tasks, external checks, rollback, and drift metrics.
- Distinguish author-reported numbers from independently reproduced numbers in every result table.

### Final Public-Safety Statement

The local source paper and all derived processing records remain outside the public repository. This manuscript contains only public URLs, repository-relative related-entry references, derived summaries, bounded implementation sketches, and public-safe provenance. No source file was uploaded.

## Attribution Block

- Source URL: https://arxiv.org/abs/2603.15690
  - Applies to: this manuscript.
  - Notes: Official metadata, identity, date, authors, version, subject, DOI, license, and abstract record.
- Source URL: https://arxiv.org/html/2603.15690
  - Applies to: this manuscript.
  - Notes: Full-paper evidence for all method, pattern, evaluation, limitation, and conclusion summaries.
- Source URL: https://doi.org/10.48550/arXiv.2603.15690
  - Applies to: this manuscript.
  - Notes: Persistent DOI locator.
