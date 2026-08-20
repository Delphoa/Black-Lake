---
title: "Evidence-Governed Agents - DEP-E"
generated_at: "2026-08-18"
artifact_type: "DEP research artifact"
primary_subject: "How explicit state, verification, structural controls, and compute specialization shape capable and governable AI systems."
source_status: "URLs only"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-18"
temporal_cutoff: "2026-08-18"
primary_url: "https://github.com/Delphoa-Labs/Black-Lake-Data/tree/623a12b35530088ef0263bf2cfa78a6346ee3952/.lake-data/DEP-20260724-Tech%20Intel%201105"
stable_identifier: "DEP-20260724-Tech Intel 1105"
confidence_summary: "Medium-high for source characterization; lower for deployment transfer because results were not independently reproduced."
safety_scope: "defensive research, evaluation, and bounded implementation planning"
distribution_notes: "No external source payloads are deposited; public URLs and repository-relative provenance only."
---

# Evidence-Governed Agents - DEP-E

## Source Metadata

This initial-pass artifact reviews the ten primary papers collected by `Black-Lake-Data/.lake-data/DEP-20260724-Tech Intel 1105`. The selected DEP README and findings file were inspected at source commit `623a12b35530088ef0263bf2cfa78a6346ee3952`. Complete arXiv HTML was inspected for every paper; implementation surfaces were inspected when the paper exposed a stable public locator.

| ID | Source | Role | Type | Identifier / Version | URL | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S0 | Selected source DEP | Primary source bundle | Markdown repository entry | Source commit `623a12b` | [DEP directory](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/623a12b35530088ef0263bf2cfa78a6346ee3952/.lake-data/DEP-20260724-Tech%20Intel%201105) | Repository evidence; no source files copied | 2026-08-18 | README and findings inspected |
| S1 | OpenForge RL | Primary paper | arXiv HTML | arXiv:2607.21557v3 | [Record](https://arxiv.org/abs/2607.21557); [full text](https://arxiv.org/html/2607.21557) | CC BY 4.0 shown by arXiv HTML | 2026-08-18 | Methods, experiments, tables, appendices, and discussion inspected |
| S2 | Agentic Context Management | Primary paper | arXiv HTML | arXiv:2607.21503v1 | [Record](https://arxiv.org/abs/2607.21503); [full text](https://arxiv.org/html/2607.21503) | CC BY 4.0 shown by arXiv HTML | 2026-08-18 | Taxonomy, evaluation, limitations, reproducibility, and privacy appendix inspected |
| S3 | AREX | Primary paper | arXiv HTML | arXiv:2607.21461v2 | [Record](https://arxiv.org/abs/2607.21461); [full text](https://arxiv.org/html/2607.21461) | arXiv non-exclusive license shown | 2026-08-18 | Method, benchmarks, ablations, and conclusion inspected |
| S4 | GuardianAgentBench | Primary paper | arXiv HTML | arXiv:2607.20982v1 | [Record](https://arxiv.org/abs/2607.20982); [full text](https://arxiv.org/html/2607.20982) | arXiv non-exclusive license shown | 2026-08-18 | Benchmark construction, validation, experiments, and guardrails inspected |
| S5 | IssueTrojanBench | Primary paper | arXiv HTML | arXiv:2607.20759v1 | [Record](https://arxiv.org/abs/2607.20759); [full text](https://arxiv.org/html/2607.20759) | CC BY-NC-ND 4.0 shown by arXiv HTML | 2026-08-18 | Threat model, construction, 4,176-run evaluation, ethics, and validity threats inspected |
| S6 | Test-Time Scaling via Error Localization | Primary paper | arXiv HTML | arXiv:2607.21453v2 | [Record](https://arxiv.org/abs/2607.21453); [full text](https://arxiv.org/html/2607.21453) | CC BY-NC-ND 4.0 shown by arXiv HTML | 2026-08-18 | Algorithm, theory, experiments, detailed results, and sensitivity appendices inspected |
| S7 | Windowed-MTP | Primary paper and implementation | arXiv HTML; GitHub repository | arXiv:2607.21535v1 | [Record](https://arxiv.org/abs/2607.21535); [full text](https://arxiv.org/html/2607.21535); [reproduction package](https://github.com/avalliappan-nvidia/windowed-mtp-b200) | Paper CC BY 4.0; package Apache-2.0 with third-party terms | 2026-08-18 | Full paper and repository README/layout inspected; code not run |
| S8 | BaseRT | Primary paper and implementation | arXiv HTML; GitHub repository | arXiv:2607.19438v1 | [Record](https://arxiv.org/abs/2607.19438); [full text](https://arxiv.org/html/2607.19438); [repository](https://github.com/basecompute/baseRT) | Paper CC BY 4.0; repository Apache-2.0; prebuilt engine separately licensed | 2026-08-18 | Paper, public repository surface, benchmarks/docs layout, and license notes inspected; code not run |
| S9 | AAMFM | Primary paper and code locator | arXiv HTML; GitHub repository | arXiv:2607.20057v1 | [Record](https://arxiv.org/abs/2607.20057); [full text](https://arxiv.org/html/2607.20057); [repository](https://github.com/XL-S224/AAMFM) | arXiv non-exclusive license shown; repository license not visible from inspected surface | 2026-08-18 | Paper, appendices, code locator, and public repository surface inspected; no experiments run |
| S10 | DQAOA-GPT | Primary paper | arXiv HTML | arXiv:2607.20225v1 | [Record](https://arxiv.org/abs/2607.20225); [full text](https://arxiv.org/html/2607.20225) | CC BY-NC-ND 4.0 shown by arXiv HTML; U.S. Government notice present | 2026-08-18 | Method, experiment setup, result figure discussion, and conclusion inspected |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E0 | S0 | Source bundle | DEP inventory, synthesis, tags, and original source attributions | Review boundary and provenance | High | The DEP summarized papers before this independent review; its quantitative statements were not treated as sufficient evidence alone |
| E1 | S1 | Primary paper | Proxy/orchestrator method; Claw and GUI training; six-benchmark results; behavior analysis | Harness-native training can reduce train-deploy mismatch and improve measured agent reliability | High for reported setup | Source-reported, expensive 8xB200 training; task synthesis and model-judge choices constrain transfer |
| E2 | S2 | Primary paper | Five lifecycle primitives; cost model; LongMemEval/LoCoMo configuration; limitations and privacy appendix | Context should be governed as a lifecycle, not a store | Medium | Single-author paper tied to a commercial reference implementation; vendor figures are explicitly not controlled comparisons |
| E3 | S3 | Primary paper | Discovery-verification loop; autonomous context update; matched-budget ablations | Preserving verified state and focusing training on decisive steps improves the reported research-agent results | High for reported ablations | Synthetic-task and benchmark transfer to open-ended research is not independently established |
| E4 | S4 | Primary paper | 580 scenarios, six domains, three frameworks, six models, structural guardrails | Execution-time validation can recover failures with low measured false positives | High for benchmark | Guardrails use a strong model and two retries; operational cost and transfer beyond tested frameworks remain open |
| E5 | S5 | Primary paper | Six seed issues expanded to 696 artifacts and 4,176 runs; binary exploit execution; validity threats | Untrusted project artifacts are a material coding-agent control-plane risk | High for the tested matrix | Two Python repositories, one prompt form, three agents, three models, and rapidly changing versions limit generalization |
| E6 | S6 | Primary paper | Feedback-conditioned probability contrast, null-baseline filtering, prefix branching, three benchmarks | Localized suffix regeneration can improve pass-at-k/token efficiency | High for reported experiments | Small math sets, evaluator dependence, and access to token probabilities constrain deployment portability |
| E7 | S7 | Primary paper + official artifact | Draft-only windowing, full-target verification, 1M-context sweeps, exact reproduction package | Separating proposal state from verification state can bound cost without changing target verification | High for documented setup | Headline hardware is B200; results vary by model, batch, topology, KV format, and acceptance length; not rerun here |
| E8 | S8 | Primary paper + official repository | M5 tensor-kernel design, 15 configurations, prefill/decode results, public interfaces and licensing | Hardware-aware specialization changes on-device inference economics | High for measured hardware | M5/Metal-specific; single-device paper scope; public repository and separately licensed engine are not identical artifacts |
| E9 | S9 | Primary paper + code locator | Antigen/epitope adapter, Cal-DPO, SAbDab/OAS evaluation, ablations, stated lack of in-vitro validation | Explicit domain context improves reported proxy metrics for antibody design | Medium-high | Structural/model scores are not biological efficacy; no in-vitro validation; data and code were not executed here |
| E10 | S10 | Primary paper | N=100 dense HUBO setup; subproblem sweep; runtime/accuracy comparison | Generative circuit synthesis can reduce the tested variational-loop cost | Medium-high | Benchmark-scale simulation and best-known reference solutions do not establish quantum advantage or hardware utility |

## Executive Summary

The ten papers converge on a systems thesis: capability becomes more useful when state, verification, authority, and compute are explicit design surfaces. OpenForge RL moves the deployed harness into the training loop; Agentic Context Management and AREX make context retention, compression, verification, and unresolved constraints first-class state; GuardianAgentBench and IssueTrojanBench show that prompt-only protection is inadequate once agents can call tools and ingest untrusted project artifacts. TTEL and Windowed-MTP then show two forms of selective reuse: retain a valid reasoning prefix after localized failure, or bound the proposal model's state while preserving full verification.

The strongest practical inference is not that one architecture wins. It is that production agent systems need a governed evidence-and-action boundary: typed provenance, scoped memory, explicit unresolved claims, pre-execution validation, bounded authority, and replayable traces. The empirical record is uneven. Several papers provide matched-budget ablations or detailed reproducibility packages; others rely on vendor-controlled benchmarks, proxy metrics, single-hardware studies, or simulations. Accordingly, this artifact treats all numbers as source-reported and recommends cross-source evaluation rather than a composite performance claim.

Two domain papers reinforce the same boundary. AAMFM improves computational antibody-design proxies by conditioning on antigen geometry and epitopes, but lacks in-vitro validation. DQAOA-GPT reduces runtime in a benchmark-scale hybrid optimization simulation, but does not demonstrate quantum advantage. BaseRT shows that implementation substrate can dominate prefill throughput on a specific hardware generation. In each case, the claimed gain is useful only inside its evidence boundary.

## Detailed Summary

### Governed state and harnesses

OpenForge RL inserts a proxy between arbitrary inference harnesses and standard RL infrastructure, records harness model calls as trajectories, and uses a Kubernetes orchestrator to isolate remote rollouts. Its OpenForge-Claw SFT+RL model reports 31.7 pass^3 and 55.9 pass@3 on ClawEval, 33.7 pass@1 on QwenClawBench, and 28.1 on the 89-task credential-free MCPAtlas subset. OpenForge-GUI reports 37.7 on OSWorld-Verified, 63.0 on Online-Mind2Web, and 72.3 on WebVoyager. The paper's behavior analysis says RL improves self-verification, tool coverage, and plan completion while error recovery remains weak (E1).

Agentic Context Management decomposes context governance into architecting, ingesting, scoping, anticipating, and compacting/consolidation. Its Maximem Synap configuration reports 92.0% on LongMemEval and 93.2% on LoCoMo categories 1-4, while explicitly warning that vendor results use different answer models, judges, ingestion policies, and methodologies. It reports no production latency numbers, and its motivating retrieval study uses one operator, one keyword engine, one vector store, no chunking, 10,000-document corpora, and incomplete per-query traces (E2).

AREX alternates an inner evidence-gathering loop with an outer constraint-wise verification loop. Its autonomous context-update tool retains verified evidence and unresolved constraints. On BrowseComp, matched ablations reduce accuracy from 82.5 for full AREX to 77.5 with direct mixed training, 74.1 with random-step rather than key-step replay, and 79.4 with standard GRPO instead of step-aware RL. The evidence supports the narrower claim that training attention to decisive research-state updates helps on the evaluated tasks (E3).

### Structural safety and untrusted evidence

GuardianAgentBench evaluates 580 scenarios across six domains, three production-oriented frameworks, six models, and five adversarial modes. Its strongest configuration reaches 74.8 overall. A LlamaIndex proof-of-concept runs argument validation, tool-coverage, and relevance/cost checks before execution, permits at most two correction retries, and then blocks with a human alert. For Claude Opus 4.5 on LlamaIndex, it converts 30 of 151 failed cases while incorrectly blocking 2 of 429 previously successful cases: 19.9% recovery and 0.5% false positives (E4).

IssueTrojanBench begins with six real issues from SymPy and Requests, expands them across four malicious action categories, six delivery vectors, and perturbations into 696 adversarial artifacts, then executes six agent-model configurations for 4,176 runs. The paper reports 2,776 exploit executions (66.5%). Standard text artifacts report 72.2% success, versus 16.7% for image alt-text. Its own validity section limits transfer because only two Python repositories, one task prompt, one authority-marked phrasing strategy, three agents, and three models were tested (E5). The defensive implication is architectural: fetched material is evidence, not authority, and dangerous actions need explicit authorization and enforcement outside the model.

### Selective compute and retained validity

TTEL compares token probabilities under informative feedback with a non-diagnostic baseline, detects a likely error point, preserves the prefix, and regenerates only the suffix. With Qwen3-8B on LiveCodeBench V6, it reports pass@64 of 71.0% at 360.4k generated tokens per question versus 735.0k for independent sampling. The paper repeats experiments across two models, three datasets, and multiple seeds, but AIME-2025 and HMMT-2025 contain only 30 questions each (E6).

Windowed-MTP applies a small window plus attention sink only to the MTP draft head; the full-attention target still verifies accepted tokens. At one million tokens on a single B200, its paper reports roughly 28%-44% lower per-decode-step draft cost across three long-context architectures. The repository provides a compact patch, exact model/config identifiers, seeded synthetic RULER generators, checksums, and run scripts, but requires large model downloads and B200-class memory for the headline regime. No package was executed in this review (E7).

BaseRT routes compute-bound dense/MoE GEMMs and prefill attention through Apple M5 Neural Accelerators while keeping memory-bound decode on specialized kernels. Across 15 model configurations, the paper reports up to 6.4x higher prefill throughput than llama.cpp and 3.9x than MLX, with decode gains up to 1.75x and 1.33x respectively. The paper limits scope to M5/Metal, single-device, single-user inference and notes that tensor kernels do not remove the memory-bandwidth ceiling. The public repository now exposes a broader CLI/API ecosystem, but its prebuilt engine is separately licensed (E8).

### Domain-conditioned scientific systems

AAMFM adapts ESM3 to antibody sequence/structure pairs, adds an antigen geometric-and-epitope adapter, and applies Cal-DPO using Protenix-reproduced AlphaFold3-derived preferences. In full antibody design, AAMFM-CalDPO reports AF3-score 0.892 and ipTM 0.888 versus 0.870 and 0.865 for its SFT-only variant. Removing the antigen adapter or epitope supervision degrades functional proxy metrics. The authors explicitly state that designed antibodies have not been fully validated in vitro, so the results support computational prioritization, not therapeutic efficacy (E9).

DQAOA-GPT decomposes a dense higher-order binary optimization problem, projects subproblems to graphs, and uses a trained generator to produce circuits instead of performing a full variational search per subproblem. For N=100 and 100 DQAOA iterations, reported relative accuracy rises to about 0.78 at subproblem size 12. Conventional DQAOA runtime grows from about 33.80 seconds at n=4 to 683.99 seconds at n=12, while DQAOA-GPT remains near 28 seconds. This is a simulator/benchmark result and not evidence of quantum advantage or production utility (E10).

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Training through the deployed harness can improve measured agent behavior while reducing train-deploy mismatch. | Author claim | E1 | Supported across text and GUI settings; operational cost, synthesized tasks, and judge choices remain important. | Medium-high |
| C2 | Context quality requires lifecycle governance, not storage/retrieval alone. | Source thesis plus reviewer interpretation | E2, E3 | Strong conceptual convergence; benchmark evidence supports selected mechanisms but not a universal architecture. | Medium-high |
| C3 | Verified evidence and unresolved constraints should be durable research state. | Reviewer interpretation | E3, E6 | AREX and TTEL independently support targeted reuse of valid intermediate state. | Medium-high |
| C4 | Prompt-only defenses are insufficient for tool-using agents processing untrusted artifacts. | Cross-source inference | E4, E5 | Strong within tested scenarios; production rates will depend on models, policies, permissions, and task mix. | High for the need for structural controls |
| C5 | Selective reuse can reduce computation without discarding validation. | Cross-source inference | E6, E7 | TTEL preserves a reasoning prefix; Windowed-MTP preserves target verification. Mechanisms and hardware differ, so results must not be pooled. | High for mechanism, medium for transfer |
| C6 | Hardware-aware kernels can dominate on-device prefill performance. | Author claim | E8 | Supported on the tested M5 Pro and model set; not portable to earlier hardware or other serving regimes. | High for tested setup |
| C7 | Domain conditioning improves scientific-design proxy metrics but is not experimental validation. | Source claim plus reviewer boundary | E9, E10 | Both papers show benchmark gains; neither establishes biological efficacy, quantum advantage, or field deployment. | High |

## Methodology

- `Research objective`: Convert one randomly selected eligible Tech Intel DEP into a source-grounded, provenance-preserving DEP-E manuscript and identify a coherent systems thesis across its ten papers.
- `Sources inspected`: The selected DEP README and findings file; full arXiv HTML for all ten primary papers; the public Windowed-MTP, BaseRT, and AAMFM repository surfaces; and the IssueTrojanBench Zenodo locator exposed by the paper.
- `Discovery strategy`: Source URLs came from the selected DEP. Canonical arXiv HTML tables of contents, methods, experiments, results, limitations, appendices, and code locators were followed directly. No secondary web summary was used as technical evidence.
- `Inclusion criteria`: Every one of the selected DEP's ten primary findings was included. Implementation locators were included only when the primary paper exposed a stable public URL and the surface could be inspected.
- `Exclusion criteria`: Discovery category listings, news, vendor marketing, unreviewed citations, and inaccessible redirects were excluded as evidence. Repository presence alone was not treated as reproducibility.
- `Analytical approach`: Mixed conceptual, empirical, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: Source-reported metrics remain attributed to their paper and setup. Reviewer interpretations are labeled and never combine incomparable benchmark scores.
- `Uncertainty handling`: Missing experiments, version drift, proxy-metric limits, source conflicts, hardware dependence, and non-execution are stated where they bound a claim.
- `Extraction process`: HTML sections, result tables, appendices, limitations, repository READMEs, public layouts, and license statements were inspected. No PDF, source package, dataset, model, or code archive was downloaded.
- `Version control`: The source DEP is pinned to commit `623a12b35530088ef0263bf2cfa78a6346ee3952`; arXiv versions are recorded in Source Metadata. Public repositories were inspected as access-date snapshots and were not commit-pinned.
- `Cross-checking`: Quantitative claims were checked against paper tables or explicit result text when rendered. No numerical recomputation or independent benchmark execution was performed.
- `Reviewer stance`: DEP-ready synthesis, critique, defensive implementation translation, and replication backlog.

## Scope, Constraints, and Assumptions

- `Scope`: Ten papers spanning agent training, context management, research verification, tool safety, coding-agent injection, inference-time reasoning, long-context serving, on-device inference, antibody design, and hybrid quantum optimization.
- `Temporal boundary`: Sources were accessed on 2026-08-18; later revisions, commits, benchmarks, models, and hardware may differ.
- `Evidence limits`: No PDF figures were visually re-rendered, no source packages were downloaded, and no datasets, models, code, benchmarks, laboratories, accelerators, or quantum systems were executed.
- `Assumptions`: Canonical arXiv HTML corresponds to the displayed paper version; repository surfaces are author-linked implementation context but not independent validation.
- `Constraints`: Public-only sources, source-locality requirements, license boundaries, defensive security framing, non-clinical use, and no restricted compute or data.
- `Out of scope`: Exploit reproduction, model training, dependency installation, biological or clinical recommendation, fabrication, quantum-advantage claims, procurement advice, and production readiness certification.
- `Intended use`: Research review, DEP deposition, architecture planning, defensive evaluation design, and follow-on replication.
- `Audience`: Agent-system researchers, platform engineers, safety reviewers, research-infrastructure builders, and technical product designers.
- `Reproducibility boundary`: Windowed-MTP exposes the strongest self-contained reproduction surface, but even it requires large public model downloads and specialized hardware; none of the cited results was reproduced here.
- `Operational boundary`: Security mechanisms are discussed for prevention and validation only; no harmful payload or evasion procedure is operationalized.
- `Data sensitivity`: Public research metadata and public repository content only.

## Observations

- `Observed pattern`: The harness, context manager, verifier, guardrail, draft model, kernel, antigen representation, or decomposition policy is part of the effective system—not merely plumbing around a model.
- `Observed pattern`: The papers that expose intermediate state also expose clearer intervention points: verified versus unresolved claims, accepted versus suspect prefixes, proposed versus verified tokens, requested versus authorized tool actions.
- `Technical implication`: A provenance-preserving state machine is a more useful integration primitive than an undifferentiated conversation transcript.
- `Contradiction or tension`: OpenForge RL benefits from training inside rich harnesses, while IssueTrojanBench shows that the same rich artifact/tool surface enlarges the attack boundary.
- `Contradiction or tension`: Context systems seek anticipatory retrieval and broader organizational reuse, but privacy and authorization demand strict scope isolation and minimal disclosure.
- `Reviewer hypothesis`: Evaluations that jointly measure task success, evidence sufficiency, unauthorized action rate, token/latency cost, and recovery quality will be more decision-useful than separate capability and safety leaderboards.
- `Open question`: How much of each reported gain survives model/version changes under one fixed budget and one independently controlled evaluator?

## Considerations

- `Authority`: Treat retrieved documents, issues, tool output, and prior memory as typed evidence. Only an explicit user or policy authority should authorize high-impact action.
- `State`: Record source identity, version, access scope, retention rule, confidence, unresolved constraints, and downstream consumers. Compaction must preserve qualifiers and contradictions.
- `Execution`: Enforce allowlists, capability tokens, argument schemas, side-effect previews, bounded retries, and human escalation outside the model.
- `Evaluation`: Report numerator, denominator, seeds, model/harness versions, judge configuration, task mix, and both task-success and safety-error rates.
- `Operations`: Specialized verification and guardrails consume compute. Budget their latency, false positives, and maintenance rather than treating them as free.
- `Privacy`: Anticipatory and organization-level context can create cross-tenant leakage. Isolation, retention, deletion, and audit controls are prerequisites.
- `Scientific domains`: Proxy scores can prioritize experiments but cannot replace biological validation, physical experiments, or quantum hardware evidence.
- `Licensing`: Paper, repository, model, dataset, container, and binary licenses may differ; deployment review must inspect the exact artifacts used.

## Strengths

- The source set spans the full stack from training and context policy through execution safety and hardware kernels, enabling cross-layer analysis.
- AREX, GuardianAgentBench, TTEL, and Windowed-MTP provide concrete ablations or explicit intervention comparisons rather than thesis-only discussion.
- IssueTrojanBench exposes a realistic external-artifact threat model and publishes its internal/external validity limits.
- Windowed-MTP documents exact checkpoints, flags, generated inputs, checksums, and a bounded reproduction package.
- AAMFM explicitly states that in-vitro validation is missing, and DQAOA-GPT labels its work benchmark-scale, preserving important scientific boundaries.

## Weaknesses

- The ten papers do not share tasks, metrics, budgets, models, hardware, or evaluators, so the synthesis cannot support a quantitative meta-analysis.
- Several claims rely on author-controlled or vendor-controlled evaluation; Agentic Context Management explicitly warns that published memory scores are not controlled comparisons.
- Rapidly changing agent/model versions make security and capability measurements perishable.
- Hardware papers have narrow platform boundaries, while scientific-design papers use computational proxies without downstream experimental validation.
- Public repositories were not executed or audited, and the AREX/OpenForge code surfaces were not independently resolved beyond their paper links.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Unified evidence-action schema | Agent architecture | Context and authority are repeatedly conflated | Typed provenance and enforceable action boundaries | Integration and migration cost | Replay the same tasks with/without typed evidence and measure unauthorized actions plus task success |
| Matched-budget benchmark | Cross-paper evaluation | Current results use incomparable compute and judges | Separates algorithmic gain from budget or evaluator choice | Expensive multi-system harness | Fix model, tokens, latency, retries, judge, and datasets; publish raw traces |
| Versioned threat regression suite | Agent security | Agent/model defenses change quickly | Detects safety regressions before release | Payload handling requires strict containment | Defensive synthetic artifacts, isolated runners, fixed denominators, and no external callbacks |
| Qualifier-preserving compaction test | Context management | Memory accuracy can hide lost caveats | Measures evidence sufficiency rather than recall alone | Requires annotated contradiction/qualifier corpus | Compare raw, summarized, and governed context on claim support and omission severity |
| Independent artifact replay | Reproducibility | Repository presence is not replication | Establishes which results survive outside author environments | Hardware/data/model cost | Reproduce one paper-specific anchor with pinned artifacts and publish deviations |
| Experimental handoff gates | Scientific design | Proxy metrics can be mistaken for efficacy | Prevents computational rankings from becoming deployment claims | Laboratory or hardware collaboration | Pre-register handoff criteria and require in-vitro/physical/hardware results before escalation |

## Potential Implementations

### 1. Evidence-and-Action Gateway

- `User`: Platform teams operating tool-using agents.
- `Goal`: Prevent retrieved evidence from silently becoming execution authority.
- `Core mechanism`: Normalize every input into a typed evidence record, maintain verified/unresolved state, and validate proposed tool calls against explicit capabilities.
- `Required inputs`: User intent, source provenance, tool schemas, policy rules, context items, and proposed actions.
- `Outputs`: Approved calls, blocked calls with reasons, provenance traces, and escalation requests.
- `Risk controls`: Least privilege, no default network egress, secret redaction, immutable logs, bounded retries, and human approval for high-impact actions.
- `Evaluation`: Joint task completion, unauthorized-action rate, false-positive rate, latency, and recovery quality.

### 2. Governed Research State

- `User`: Research agents and human reviewers.
- `Goal`: Preserve verified evidence and open constraints across long research runs.
- `Core mechanism`: AREX-style verified/unresolved claim state combined with provenance-aware lifecycle, compaction, and source replay.
- `Required inputs`: Claims, sources, versions, evidence spans, confidence, contradictions, and search backlog.
- `Outputs`: Claim ledger, targeted follow-up queries, compact context package, and manuscript-ready references.
- `Risk controls`: No source grants authority; preserve negative evidence; prevent cross-project memory reuse without consent.
- `Evaluation`: Citation correctness, unsupported-claim rate, qualifier retention, token cost, and reviewer time.

### 3. Selective-Compute Evaluator

- `User`: Inference and evaluation engineers.
- `Goal`: Compare full regeneration, prefix reuse, bounded drafting, and baseline inference under one budget.
- `Core mechanism`: Instrument per-step state, tokens, latency, accepted work, verification cost, and failure recovery.
- `Required inputs`: Public toy tasks, fixed model versions, deterministic seeds, compute budgets, and failure feedback.
- `Outputs`: Pareto curves, trace diffs, budget violations, and reproduction manifests.
- `Risk controls`: Synthetic inputs, offline execution, no sensitive prompts, hardware/resource caps, and full provenance.
- `Evaluation`: Accuracy, tokens, wall time, energy proxy, acceptance/reuse rate, and error localization precision.

## Three Ways to Exercise This Research

1. `Evidence versus authority tabletop`: Objective—test whether a proposed agent architecture distinguishes untrusted evidence from user authority. Inputs—synthetic issues, documents, and tool outputs containing conflicting requests. Method—trace each item through provenance, policy, proposed action, and approval. Output—an evidence/action matrix. Success criterion—no untrusted item can authorize a side effect while benign tasks remain solvable. Stop condition—any uncontrolled execution path or real credential is encountered.
2. `Qualifier-preserving context replay`: Objective—measure whether compaction retains contradictions and safety qualifiers. Inputs—a public synthetic conversation with dated facts, reversals, scope boundaries, and unresolved claims. Method—compare full context, generic summary, and governed state under the same questions and token budget. Output—claim-level recall, contradiction, and omission report. Success criterion—governed state improves critical-qualifier retention without exceeding budget. Stop condition—private data or external writes would be required.
3. `Selective-compute microbenchmark`: Objective—compare complete retries with prefix/suffix reuse using deterministic toy programs. Inputs—public unit-test tasks, fixed model/configuration, token cap, and isolated execution feedback. Method—record success, tokens, valid-prefix reuse, retries, and wall time. Output—a Pareto chart and trace bundle. Success criterion—reuse improves at least one cost metric without reducing correctness. Stop condition—budget is exceeded, nondeterminism prevents comparison, or the runner leaves the isolated environment.

## Example MVP Product

- `Product name`: Evidence Gate
- `Target user`: Teams deploying research, coding, and operations agents with tool access.
- `Problem`: Agents receive mixed-authority context but often process all natural-language content as equivalent instruction.
- `Core workflow`: Ingest and label evidence; extract claims and unresolved constraints; construct a bounded context package; intercept proposed tool calls; validate provenance, intent, capability, and arguments; execute or escalate; retain a replayable decision trace.
- `Data requirements`: Public or authorized documents, user intent, tool schemas, policy rules, source metadata, and synthetic evaluation cases. Raw secrets are excluded from logs.
- `Architecture`: Local policy service, append-only evidence ledger, context compiler, capability broker, tool-call validator, isolated executor, and review dashboard.
- `Success metrics`: Task completion, unsupported-claim rate, unauthorized-action rate, false-positive rate, qualifier retention, p95 added latency, token cost, and reviewer intervention rate.
- `Risk controls`: Least-privilege capabilities, explicit high-impact approvals, sandboxing, no implicit network egress, secret redaction, per-tenant isolation, retention/deletion controls, and signed audit records.
- `Limitations`: Cannot guarantee model truthfulness, source integrity, or complete attack coverage; adds latency and policy-maintenance cost; requires domain-specific validators.
- `MVP boundary`: Synthetic/public data, read-only tools, and two low-risk action types. No autonomous deployment, clinical workflow, financial transaction, or wet-lab/quantum control.
- `Deployment model`: Local service or sidecar beside an existing agent harness.
- `Evaluation plan`: Replay a fixed benign/adversarial suite across raw-prompt, prompt-warning, and structural-gateway variants; publish denominators, errors, traces, and version pins.
- `Failure modes`: Misclassified authority, stale policy, provenance loss during compaction, validator-model collusion, excessive blocking, and hidden side effects in downstream tools.
- `Maintenance plan`: Version policies and source schemas; rerun regression suites on every model/harness/tool change; review false positives and permission grants monthly.

## Related Research and Reading

**Initial pass:** all entries below were newly inspected for this artifact; no prior Report-Mark or DEP Class artifact existed for the selected DEP.

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| OpenForge RL | Primary paper | Harness-native training, isolated rollouts, and train-deploy alignment | https://arxiv.org/abs/2607.21557; https://arxiv.org/html/2607.21557 |
| Agentic Context Management | Primary paper | Lifecycle model for context, organizational scope, compaction, and memory evaluation caveats | https://arxiv.org/abs/2607.21503; https://arxiv.org/html/2607.21503 |
| AREX | Primary paper | Verification-guided research state and key-step training | https://arxiv.org/abs/2607.21461; https://arxiv.org/html/2607.21461 |
| GuardianAgentBench | Primary paper | Production-framework agent benchmark and pre-execution structural guardrails | https://arxiv.org/abs/2607.20982; https://arxiv.org/html/2607.20982 |
| IssueTrojanBench | Primary paper and artifact locator | Indirect injection through project artifacts, end-to-end execution metric, and released replication toolkit | https://arxiv.org/abs/2607.20759; https://arxiv.org/html/2607.20759; https://doi.org/10.5281/zenodo.19245678 |
| Test-Time Scaling via Error Localization | Primary paper | Feedback-conditioned token-level localization and valid-prefix reuse | https://arxiv.org/abs/2607.21453; https://arxiv.org/html/2607.21453 |
| Windowed-MTP | Primary paper and official reproduction package | Bounded draft state with full target verification and explicit replay artifacts | https://arxiv.org/abs/2607.21535; https://arxiv.org/html/2607.21535; https://github.com/avalliappan-nvidia/windowed-mtp-b200 |
| BaseRT | Primary paper and official repository | Hardware-aware inference specialization and public runtime interfaces | https://arxiv.org/abs/2607.19438; https://arxiv.org/html/2607.19438; https://github.com/basecompute/baseRT |
| AAMFM | Primary paper and code locator | Antigen-conditioned antibody design, preference optimization, proxy metrics, and experimental boundary | https://arxiv.org/abs/2607.20057; https://arxiv.org/html/2607.20057; https://github.com/XL-S224/AAMFM |
| DQAOA-GPT | Primary paper | Generative circuit synthesis inside decomposed hybrid optimization | https://arxiv.org/abs/2607.20225; https://arxiv.org/html/2607.20225 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R0 | [Selected DEP](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/623a12b35530088ef0263bf2cfa78a6346ee3952/.lake-data/DEP-20260724-Tech%20Intel%201105) | Review boundary, tags, inventory, and original ten-source set | 2026-08-18 | Repository files inspected; no file copied |
| R1 | [Selected DEP README](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/623a12b35530088ef0263bf2cfa78a6346ee3952/.lake-data/DEP-20260724-Tech%20Intel%201105/README.md) | Package scope, evidence limits, and attribution | 2026-08-18 | Primary repository metadata |
| R2 | [Daily research findings](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/623a12b35530088ef0263bf2cfa78a6346ee3952/.lake-data/DEP-20260724-Tech%20Intel%201105/daily_research_findings_2026-07-24_1105.md) | Original ten findings and cross-source synthesis | 2026-08-18 | Used as discovery context; claims checked against papers |
| R3 | [OpenForge record](https://arxiv.org/abs/2607.21557) and [v3 full text](https://arxiv.org/html/2607.21557) | Harness architecture, training setup, results, and behavior analysis | 2026-08-18 | Primary full-text evidence |
| R4 | [Agentic Context Management record](https://arxiv.org/abs/2607.21503) and [v1 full text](https://arxiv.org/html/2607.21503) | Lifecycle primitives, cost argument, benchmark setup, limitations, and privacy notes | 2026-08-18 | Primary full-text evidence; commercial reference implementation disclosed |
| R5 | [AREX record](https://arxiv.org/abs/2607.21461) and [v2 full text](https://arxiv.org/html/2607.21461) | Recursive verification, context updating, benchmarks, and ablations | 2026-08-18 | Primary full-text evidence |
| R6 | [GuardianAgentBench record](https://arxiv.org/abs/2607.20982) and [v1 full text](https://arxiv.org/html/2607.20982) | Scenario construction, validation, framework comparison, guardrail results | 2026-08-18 | Primary full-text evidence |
| R7 | [IssueTrojanBench record](https://arxiv.org/abs/2607.20759), [v1 full text](https://arxiv.org/html/2607.20759), and [released artifact DOI](https://doi.org/10.5281/zenodo.19245678) | Threat model, experiment matrix, execution results, ethics, validity, and replication locator | 2026-08-18 | Paper inspected; artifact locator identified but payload not downloaded |
| R8 | [TTEL record](https://arxiv.org/abs/2607.21453) and [v2 full text](https://arxiv.org/html/2607.21453) | Error localization, prefix reuse, experiments, and detailed results | 2026-08-18 | Primary full-text evidence |
| R9 | [Windowed-MTP record](https://arxiv.org/abs/2607.21535), [v1 full text](https://arxiv.org/html/2607.21535), and [reproduction package](https://github.com/avalliappan-nvidia/windowed-mtp-b200) | Draft-only windowing, verification boundary, hardware results, exact run surface, and license notes | 2026-08-18 | Repository README/layout inspected; no execution or download |
| R10 | [BaseRT record](https://arxiv.org/abs/2607.19438), [v1 full text](https://arxiv.org/html/2607.19438), and [public repository](https://github.com/basecompute/baseRT) | M5 kernels, benchmark results, platform limitations, public interfaces, and licensing | 2026-08-18 | Repository snapshot not commit-pinned; engine not executed |
| R11 | [AAMFM record](https://arxiv.org/abs/2607.20057), [v1 full text](https://arxiv.org/html/2607.20057), and [code locator](https://github.com/XL-S224/AAMFM) | Model, data, preference optimization, results, ablations, and in-vitro limitation | 2026-08-18 | Public repository surface reached; no license or complete README visible in inspected rendering |
| R12 | [DQAOA-GPT record](https://arxiv.org/abs/2607.20225) and [v1 full text](https://arxiv.org/html/2607.20225) | Decomposition, GPT circuit generation, N=100 setup, runtime/accuracy sweep, and benchmark boundary | 2026-08-18 | Primary full-text evidence; no implementation locator identified |
| R13 | [Black Lake README](https://github.com/Delphoa/Black-Lake/blob/main/README.md) and [.lake-data filing rules](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md) | DEP-E classification, naming, contents, attribution, and publication-index rules | 2026-08-18 | Live repository authority |

No external PDF, TeX source, code archive, dataset, model, benchmark payload, container, credential, clinical record, biological sample, quantum circuit execution, or hardware trace was collected or deposited.

## Appendix

### Selection record

- `Automation family`: Black-Lake Data Processing & Review / Black-Lake Data Processing & Review 0900
- `Run timestamp (UTC)`: 2026-08-18T00:02:55Z
- `Eligibility cutoff (UTC)`: 2026-08-17T00:02:55Z
- `Canonical candidates`: 113
- `Recent same-family exclusions`: 0
- `Eligible candidates`: 113
- `Eligible-list SHA-256`: `59e42530f9fbda2c9b84fb7ada7c1a19de9935bff9fbdcc2db2ba50c92877d34`
- `Random method`: OS-cryptographic UInt32 with rejection sampling over the sorted eligible list
- `Rejection limit (exclusive)`: 4294967280
- `Accepted UInt32`: 1865695506 on attempt 1
- `Successful zero-based index`: 79
- `Selected DEP`: `DEP-20260724-Tech Intel 1105`

### Source inventory and execution boundary

- Collected source files: none.
- Inspected repository files: selected DEP README and daily findings; live Black Lake root and `.lake-data` READMEs.
- Inspected remote full text: ten canonical arXiv HTML papers.
- Inspected implementation surfaces: Windowed-MTP, BaseRT, AAMFM, and the IssueTrojanBench artifact locator.
- Not executed: repositories, models, datasets, benchmarks, agent harnesses, GPUs, Apple hardware, biological pipelines, quantum simulators, or laboratory systems.
