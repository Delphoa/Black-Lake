---
title: "PIArena Evaluation - DEP-E"
generated_at: "2026-07-16"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of unified and adaptive prompt-injection evaluation."
source_status: "verified complete local PDF and full-paper HTML inspected; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "arXiv:2604.08499v1 and official repository state inspected on 2026-07-16"
primary_url: "https://arxiv.org/abs/2604.08499v1"
stable_identifier: "arXiv:2604.08499v1; DOI 10.48550/arXiv.2604.08499"
confidence_summary: "High for source identity, architecture, and reported tables; medium for generalization; low for independent reproducibility because experiments were not rerun."
safety_scope: "defensive evaluation, authorized red-team research, and benchmark governance"
distribution_notes: "Original paper files, local archive records, extraction caches, and derived text remain local and are not redistributed."
---

# PIArena Evaluation - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | PIArena: A Platform for Prompt Injection Evaluation | Primary metadata | arXiv record | arXiv:2604.08499v1; DOI 10.48550/arXiv.2604.08499 | https://arxiv.org/abs/2604.08499v1 | CC BY 4.0 on the inspected record | 2026-07-16 | Inspected |
| S2 | Complete PIArena paper | Primary artifact | PDF and official full-paper HTML | v1, submitted 2026-04-09 | https://arxiv.org/pdf/2604.08499 and https://arxiv.org/html/2604.08499 | Verified local copies withheld | 2026-07-16 | Inspected in full |
| S3 | PIArena official implementation | Official code | GitHub repository | default branch `main` | https://github.com/sleeepeer/PIArena | MIT; code, documentation, dataset and leaderboard links inspected without execution | 2026-07-16 | Inspected |
| S4 | Agent Systems Review | Related Black Lake artifact | DEP-E manuscript | DEP-E-20260708 | `.lake-data/DEP-E/DEP-E-20260708-Tech Intel Review/tech-intel-agent-systems-review.md` | Repository synthesis context | 2026-07-16 | Inspected |
| S5 | Agent Memory Forensics | Related Black Lake artifact | DEP-E manuscript | DEP-E-20260711 | `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md` | Repository synthesis context | 2026-07-16 | Inspected |
| S6 | Judge Conformal | Related Black Lake artifact | DEP-E manuscript | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md` | Repository synthesis context | 2026-07-16 | Inspected |
| S7 | Black Lake README | Repository authority | Live repository README | default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Deposition and source-handling contract | 2026-07-16 | Inspected |

The paper is by Runpeng Geng, Chenlong Yin, Yanting Wang, Ying Chen, and Jinyuan Jia. The arXiv record lists Cryptography and Security as the primary subject, with Artificial Intelligence, Computation and Language, and Machine Learning as additional subjects. Its comments say the paper is to appear at ACL 2026. The official repository describes the project as ACL 2026 work and exposes an MIT license, but conference proceedings were not independently inspected.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S2 | Primary paper | Metadata, full text, threat model, method, tables, appendix, future directions | Identity, design, reported results, and boundaries | High | v1 and author-reported; no independent rerun |
| E2 | S2, Sections 2 and 4 | Primary method evidence | Three-actor threat model; benchmark, attack, defense, and evaluator modules; standardized sample schema | Platform mechanism and interface claims | High for transcription | Interface behavior not executed |
| E3 | S2, Section 4.5 and Appendix G | Primary method evidence | Candidate strategies, feedback categories, iterative rewriting, cost analysis | Adaptive black-box attack mechanism | High for transcription | Search budget and attacker-model dependence remain |
| E4 | S2, Tables 2-4 | Primary empirical evidence | Cross-dataset defense results, backend-model results, and task-aligned knowledge-corruption results | Limited transfer, adaptive vulnerability, and content-verification gap | High for reporting | Heterogeneous metrics; author-reported; evaluator uncertainty |
| E5 | S2, Tables 5-10 and Appendix E | Primary empirical and measurement evidence | Agentic/general benchmark portability, GCG and search comparisons, judge prompt, dataset statistics | Portability, comparative attack evidence, and measurement caveats | High for reporting | Static WASP reduction; some utility values unavailable; no raw-label audit |
| E6 | S3 | Official code | README, supported datasets/attacks/defenses, CLI entry points, agent-benchmark integration, repository license | Implementation availability and declared scope | High for inventory | Dependencies, datasets, APIs, and outputs not run |
| E7 | S4-S6 | Related repository artifacts | Tool-description poisoning, memory-channel traces, conformal judge intervals | Cross-DEP synthesis | Medium | Conceptual overlap; no joint evaluation |
| E8 | Process records | Selection and cache evidence | Uniform draw, dedup checks, complete-source repair, missing-only extraction | Workflow provenance | High | Operational evidence, not scientific evidence |

## Executive Summary

PIArena is a modular platform for evaluating prompt-injection attacks and defenses across tasks, models, and benchmark families. Its core engineering contribution is standardization: benchmark samples carry a target instruction, context, injected task, reference answers, and category; attack and defense modules expose common interfaces; and an evaluator reports target-task utility and injected-task attack success rate (ASR). The paper argues that this common harness makes robustness claims more comparable and makes it easier to move defenses into new benchmarks.

The empirical contribution is a broad stress test. The appendix reports 1,700 samples across 13 dataset/task variants spanning question answering, information extraction, summarization, retrieval-augmented generation, long context, retrieval, and code generation. Across Table 2, static attack results vary sharply by defense and dataset. The paper's feedback-guided strategy attack is substantially stronger: average ASR is reported as 0.99 without defense, 0.86 for PISanitizer, 0.58 for DataFilter, 0.92 for PromptArmor, 0.92 for PromptGuard, and 0.79 for PIGuard; SecAlign++ is lower at 0.21 but also reduces clean average utility from 0.74 without defense to 0.58.

Two boundaries matter. First, PIArena uses task-specific utility metrics and an LLM judge for ASR; a 100-sample audit reports 98% accuracy, but evaluator uncertainty is not propagated through the tables. Second, when an injected task aligns with the target task, the attack can reduce to disinformation with no explicit malicious instruction. On NQ knowledge corruption, reported ASR remains 0.58-0.82 for several prevention defenses and 0.44-0.81 for several detectors, while the near-zero ASR of AttentionTracker coincides with zero clean utility. This is evidence that instruction filtering alone cannot establish content truth.

Reviewer confidence is high for what the paper and repository report, medium for the comparative direction of the findings, and low for universal robustness conclusions. No experiments were rerun; some agentic evaluation is reduced to static output scoring; attack strength depends on attacker model and budget; and defense trade-offs are not always directly comparable. PIArena is best treated as an extensible evaluation substrate, not a certification authority.

## Detailed Summary

### Problem and Threat Model

The paper models a user who supplies a target instruction and context to a backend LLM, an attacker who inserts an injected prompt into untrusted context, and a defender who tries to preserve clean utility while preventing the injected task. This framing covers RAG documents, web content, messages, code bases, and tool-returned data. Prevention defenses modify or robustly process input; detection defenses classify and reject suspected contamination.

The model is valuable because it separates two objectives that are often collapsed: completing the user's intended task and preventing the attacker's task. PIArena therefore measures utility and ASR separately. That prevents a defense from appearing successful merely because it refuses everything, although detection defenses still create a comparability problem because the paper does not report attack-time utility when a flagged input produces no response.

### Platform Architecture

PIArena has four modules. The benchmark module provides datasets and a standard record containing `target_inst`, `context`, `injected_task`, `target_task_answer`, `injected_task_answer`, and `category`. The attack module turns an injected task into an injected prompt and inserts it into the context. The defense module produces a response through detection, sanitization, filtering, or robust generation. The evaluator scores target-task utility and injected-task success.

The reviewed benchmark set spans SQuAD v2; Dolly question answering, information extraction, and summarization; NQ, MS-MARCO, and HotpotQA RAG; HotpotQA-Long, Qasper, GovReport, MultiNews, PassageRetrieval, and LCC. Four injected-task categories are balanced under attack: phishing injection, content promotion, access denial, and infrastructure failure. The authors generate context-aware tasks rather than relying only on generic strings, increasing ecological relevance while also introducing generator-model dependence.

### Adaptive Strategy Attack

The strategy attack treats a defense as a black box. It first generates candidates from a library of rewriting strategies, tests them, and then refines selected candidates according to observed failure: increase stealth if detected or sanitized, increase imperativeness if ignored, or perform general failure analysis otherwise. The paper reports ten rewriting strategies, average convergence near one to two iterations for most tested defenses, 4.555 iterations for SecAlign++, and roughly eight seconds per sample with batching and vLLM.

This is not a proof of worst-case robustness. It is a practical adversarial-search method whose strength depends on the attacker LLM, strategy library, candidate count, iteration limit, success classifier, backend model, and defense feedback surface. Its scientific value is showing that fixed-template evaluations can materially underestimate adaptive risk.

### Main Comparative Results

Table 2 averages 13 dataset/task variants. Under no attack, the no-defense average utility is 0.74. PISanitizer and PromptArmor preserve that clean average, while SecAlign++ reports 0.58, DataFilter 0.63, PromptGuard 0.66, AttentionTracker 0.15, and PIGuard 0.72. Against the Combined static attack, reported average ASR ranges from 0.00 for AttentionTracker to 0.58 for PromptArmor; against Direct, it ranges from 0.00 for AttentionTracker to 0.56 without defense. Under Strategy, ASR rises to 0.86 for PISanitizer, 0.58 for DataFilter, 0.92 for PromptArmor and PromptGuard, and 0.79 for PIGuard. AttentionTracker's low attack rates must be interpreted alongside its severe utility loss.

Table 3 tests ten backend models on SQuAD v2 with the Direct attack. Reported ASR ranges from 0.31 for Claude-Sonnet-4.5 to 0.92 for GPT-4o; GPT-5 is reported at 0.70. This supports the narrow claim that model scale or closed-source deployment alone did not remove the tested vulnerability. It does not establish current behavior outside the named model versions and experiment settings.

### Task Alignment and Agentic Portability

For NQ knowledge corruption, the injected behavior aligns with question answering and can be expressed as manipulated content rather than a visible instruction. Table 4 reports 0.81 ASR without defense; 0.67 for PISanitizer; 0.58 for SecAlign++; 0.78 for DataFilter; 0.82 for PromptArmor; and 0.44-0.81 for several detectors. The exception, AttentionTracker at 0.01 ASR, also has 0.00 utility without attack in that table. The paper reasonably interprets this as a content-verification problem, but it does not evaluate a complete provenance or corroboration solution.

PIArena also integrates defenses into InjecAgent, AgentDojo, AgentDyn, WASP, Open-Prompt-Injection, and SEP. The results demonstrate interface portability, not uniform experimental equivalence. WASP is reduced to the initial injected webpage and an intermediate judge outcome, while other agent suites use their original environments. A future comparison should distinguish static exposure, intermediate compromise, tool invocation, and terminal harmful action.

### Measurement and Reproducibility

Utility is task-specific: short-context tasks often use an LLM judge; long-context tasks use F1, ROUGE-L, retrieval score, or code similarity. ASR uses a Qwen3-4B-Instruct judge that answers whether a response completes a target or injected task. The authors manually inspect 100 random cases and report 98% judge accuracy. That is useful but too small to characterize uncertainty across all datasets, defenses, attacks, and edge cases.

The official MIT repository exposes installation, CLI and configuration workflows, attack/defense registries, search entry points, and agent-benchmark adapters. It also links a public dataset and leaderboard. This review did not clone or run the project, authenticate to model services, verify dataset cards, pin all dependency versions, or regenerate a table.

## Key Claims and Evidence

| Claim | Type | Evidence | Assessment | Confidence |
|---|---|---|---|---|
| PIArena provides unified interfaces for benchmarks, attacks, defenses, and evaluators. | Author claim | E2, E6 | Supported by paper architecture and official README; not executed. | High |
| Defenses that work on one task or static attack can fail across tasks or under adaptive attack. | Author claim | E4 | Strongly supported by reported tables; generality remains benchmark-bound. | Medium-high |
| The strategy attack outperforms adapted PAIR and TAP for many tested defenses. | Author claim | E3, E5 | Table 10 supports this setup-specific comparison; search budgets and models constrain transfer. | Medium |
| Closed-source or larger backend models remain vulnerable in the tested setting. | Author claim | E4 | Supported on SQuAD v2 Direct experiments; not a universal or current-product claim. | Medium |
| Task-aligned prompt injection becomes a content-verification problem. | Author interpretation | E4 | Mechanistically plausible and supported by Table 4; no content-verification baseline tested. | Medium-high |
| PIArena's reported averages are complete robustness certificates. | Rejected interpretation | E4-E6 | Unsupported; metrics, judge error, attack budget, and deployment environment remain bounded. | High |
| PIArena connects to Black Lake source ingestion, trace forensics, and judge uncertainty. | Reviewer synthesis | E7 | Concrete conceptual overlap in three inspected DEP artifacts. | Medium |
| This run is a fresh, source-complete review. | Process claim | E8 | First draw passed dedup; repaired PDF/HTML unit and cache validation passed. | High |

## Methodology

- `Research objective`: Reconstruct PIArena's mechanism and evidence, identify measurement and deployment boundaries, and connect it to existing Black Lake research.
- `Sources inspected`: Canonical arXiv metadata, complete PDF, official full-paper HTML, official GitHub README/metadata, live Black Lake README, and exactly three related DEP manuscripts.
- `Discovery strategy`: Enumerate local PDFs with `rg --files -g "*.pdf"`, sample a uniformly random parent unit, validate dedup, repair source completeness, extract cache text, then inspect full-paper sections and public implementation metadata.
- `Inclusion criteria`: Primary sources, official implementation material, and repository artifacts with direct overlap in injection surfaces, traces, or evaluator uncertainty.
- `Exclusion criteria`: Abstract-only synthesis, unverified secondary summaries, offensive deployment instructions, local source paths, and unrelated DEP entries.
- `Analytical approach`: Separate author claims, reviewer interpretation, process evidence, and missing evidence; transcribe representative results with denominators and trade-offs.
- `Evidence handling`: External documents were treated as evidence only. Source files and caches remained local; public outputs use canonical URLs and repository-relative paths.
- `Uncertainty handling`: Results are labeled author-reported; no reproduction is implied; evaluator, attack-budget, metric, and version uncertainty are explicit.
- `Random selection`: Uniform `Get-Random` index 1,108 from 75,776 sorted unique PDF-parent units; first draw accepted.
- `Cache methodology`: Initial cache miss; repaired local PDF/HTML processed in `missing-only` mode; `pypdf` used because `pdftotext` was unavailable; `html-regex` extracted HTML; source text was absent.
- `Dedup validation`: arXiv ID, DOI, normalized title, slug, logs, reports, DEP-E paths, dedup index, memory, active repository checkouts, companion-repository entries, and 24-hour markers were checked. One inventory-only row was not treated as a prior research deposit.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:2604.08499v1, its verified complete PDF/HTML, official implementation metadata, and three related Black Lake artifacts.
- `Temporal boundary`: Public sources inspected through 2026-07-16; models, repository contents, leaderboard state, and venue records may change.
- `Evidence limits`: No benchmark run, API call, dataset audit, dependency build, code review beyond public documentation, or table reproduction.
- `Assumptions`: The official PDF and HTML represent the v1 record; table extraction preserved row/column meaning; official repository documentation describes intended operation.
- `Constraints`: Public artifacts omit local execution context, exact local timestamps, source files, extracted text, caches, secrets, and operational attack recipes.
- `Out of scope`: Certifying defenses, testing live systems without authorization, reproducing harmful prompts, or making vendor-wide security claims.
- `Intended use`: Defensive benchmark design, research review, evaluation governance, and implementation planning.
- `Reproducibility boundary`: Source inspection is repeatable from public URLs; empirical results require the repository, datasets, models, compute, service access, and versioned configuration.
- `Safety boundary`: Any red-team exercise must use authorized targets, synthetic or approved data, bounded budgets, and non-production actions.

## Observations

- The platform's main value is comparability infrastructure, not a single novel defense.
- Adaptive-search results are more decision-relevant than static attack results because they test a defense-aware adversary.
- Utility and ASR form a coupled outcome; low ASR without usable task performance is not operational success.
- Task-aligned corruption changes the security object from instruction detection to evidence trust.
- Judge-based evaluation is itself a model-dependent control surface that needs calibration, abstention, and provenance.
- Agentic benchmarks need explicit outcome levels: exposure, intermediate compliance, tool call, state change, and terminal harm.

## Considerations

PIArena can improve security review only if configurations and evidence remain inspectable. A leaderboard row should identify dataset version, attack budget, attacker model, defense version, backend model, evaluator prompt/model, seed, refusal policy, and utility denominator. Without those fields, nominally comparable ASR values may encode different risk questions.

Defensive testing also needs governance. Adaptive attacks can create harmful or deceptive content, consume external model services, and contaminate logs or datasets. Safe use requires authorized systems, synthetic defaults, no autonomous external actions, bounded generations, output retention limits, and human review before disclosing new vulnerabilities.

The task-alignment result is especially relevant to RAG and agents. Provenance, retrieval trust, source corroboration, action confirmation, and least privilege sit outside a text-only detector. A mature defense program should therefore combine benchmark-level model tests with system-level invariants and trace evidence.

## Strengths

- Clear modular decomposition and standardized data/interface contracts.
- Broad cross-task evaluation rather than one narrow benchmark.
- Explicit utility-ASR trade-off rather than attack success alone.
- Adaptive black-box attack that exposes static-evaluation optimism.
- Coverage of prevention, detection, open, closed, long-context, RAG, code, and agentic settings.
- Public MIT implementation, dataset link, documentation, and extension points.
- Appendix contains dataset counts, judge prompt, cost analysis, and additional attack comparisons.

## Weaknesses

- Heterogeneous utility metrics and judge-based ASR complicate cross-dataset averages.
- A 100-case judge audit is insufficient to propagate evaluator uncertainty across the full matrix.
- Detection-defense utility under attack is absent, limiting direct trade-off analysis.
- Adaptive results depend on one attacker-model/configuration family and do not test held-out strategy transfer.
- Some agentic evaluation abstractions differ substantially, especially the static WASP reduction.
- No independent replication, end-to-end dependency lock, or table regeneration was established here.
- Results are version-bound and should not be generalized to later models or defense updates.

## Potential Improvements

| Improvement | Why | Expected value | Risk | Validation |
|---|---|---|---|---|
| Publish machine-readable run manifests | Rankings depend on many hidden configuration choices | Reproducible comparison and audit trails | Manifest complexity | Recreate table rows from manifests |
| Add calibrated multi-judge evaluation | A single judge creates correlated label error | Confidence intervals and abstention | Higher cost | Compare against stratified human labels |
| Report attack-time utility for detector refusals | Missing values hide denial-of-service trade-offs | Fairer defense comparison | Metric design disagreement | Report conditional and end-to-end utility |
| Hold out strategy families and attacker models | In-sample search may overstate generality | Stronger adaptive-robustness claims | More compute | Pre-register held-out attack suites |
| Separate agent outcome stages | Static and end-to-end ASR answer different questions | Better risk localization | More instrumentation | Trace exposure-to-action transitions |
| Add provenance/corroboration baselines | Task-aligned corruption is not an instruction-only problem | System-level comparison | External-source trust and privacy | Evaluate trusted-source and conflict cases |

## Potential Implementations

1. `Versioned PIArena runner`: Wrap each authorized benchmark run with a manifest containing source revisions, model identifiers, prompts, seeds, attack budget, evaluator configuration, and hashes of non-sensitive outputs.
2. `Judge uncertainty adapter`: Apply calibrated intervals or ensemble disagreement to utility/ASR labels, routing ambiguous cases to human review instead of forcing binary benchmark outcomes.
3. `Agent injection trace schema`: Normalize context exposure, detector decision, model response, tool request, policy decision, state mutation, and final outcome so agentic benchmarks can compare the same compromise stage.

## Three Ways to Exercise This Research

1. `Reproduce one safe table slice`: Objective: validate the harness on a synthetic question-answering set. Inputs: pinned open model, synthetic contexts, one benign attack template, one defense, fixed judge rubric. Method: run clean/direct conditions with deterministic manifests. Output: utility-ASR table plus failures. Success: every row is reproducible from the manifest. Safety: no external actions or real phishing content.
2. `Stress evaluator stability`: Objective: measure whether conclusions change with judge choice. Inputs: a stratified set of benign and injected responses, two judges, human labels, and abstention rules. Method: compare agreement, confidence, and ranking changes. Output: calibration report. Success: uncertainty accompanies each aggregate. Safety: redact sensitive content and use authorized data.
3. `Map task alignment to provenance controls`: Objective: test whether corroboration reduces manipulated-context errors. Inputs: synthetic RAG corpus with trusted and untrusted provenance, conflict labels, and bounded retrieval. Method: compare instruction detection, provenance filtering, and corroboration. Output: accuracy, ASR, latency, and false-rejection report. Success: controls improve corruption resistance without collapsing clean utility. Safety: synthetic facts and offline execution.

## Example MVP Product

- `Product name`: Injection Evaluation Ledger
- `Target user`: Security engineers and benchmark maintainers evaluating LLM applications.
- `Problem`: Attack/defense scores are difficult to compare because configurations, judge uncertainty, and agent outcome stages are inconsistently recorded.
- `Core workflow`: Import a safe benchmark manifest, run or ingest authorized results, validate denominators, attach evaluator uncertainty, classify compromise stage, and publish a reviewable Markdown/JSON evidence ledger.
- `Data requirements`: Synthetic or authorized prompts and contexts, versioned model/defense identifiers, non-sensitive outputs, human labels for calibration, and policy decisions.
- `Architecture`: Manifest validator, isolated runner adapter, bounded attack scheduler, evaluator ensemble, trace normalizer, result store, public-safe report generator, and human-review queue.
- `Success metrics`: Reproducible row rate, human-judge agreement, uncertainty coverage, clean utility, ASR by outcome stage, manifest completeness, and zero unauthorized external actions.
- `Risk controls`: Authorized targets only, synthetic defaults, rate and token budgets, secret scanning, no autonomous tool execution, sandboxing, content retention limits, role-based review, and explicit publication approval.
- `Limitations`: Cannot prove worst-case safety, depends on benchmark representativeness, and may not reproduce proprietary model behavior.
- `MVP boundary`: Offline evaluation of synthetic or approved text responses; no live production testing or offensive deployment.

## Related Research and Reading

1. `.lake-data/DEP-E/DEP-E-20260708-Tech Intel Review/tech-intel-agent-systems-review.md` - source basis: inspected sections on ShareLock-like distributed tool-description injection and process-grounded evaluation. Relevance: PIArena's untrusted-context model extends naturally to tool metadata and multi-source prompt assembly.
2. `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md` - source basis: inspected threat-model and observation sections distinguishing memory-channel compromise from prompt-inline injection. Relevance: PIArena can test responses, while forensic traces identify the channel and action path.
3. `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md` - source basis: inspected evidence ledger and interval-evaluation method. Relevance: PIArena relies on judge decisions for utility and ASR, so calibrated uncertainty can prevent false precision.

Together these records form a three-layer defensive stack: enumerate adversarial context surfaces, preserve channel/action traces, and quantify uncertainty in the metric used to declare success.

## Source References

- Geng, Runpeng; Yin, Chenlong; Wang, Yanting; Chen, Ying; Jia, Jinyuan. *PIArena: A Platform for Prompt Injection Evaluation*. arXiv:2604.08499v1. https://arxiv.org/abs/2604.08499v1
- Complete paper PDF. https://arxiv.org/pdf/2604.08499
- Official full-paper HTML. https://arxiv.org/html/2604.08499
- arXiv-issued DOI. https://doi.org/10.48550/arXiv.2604.08499
- Official PIArena implementation. https://github.com/sleeepeer/PIArena
- Agent Systems Review. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260708-Tech%20Intel%20Review/tech-intel-agent-systems-review.md
- Agent Memory Forensics. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Agent%20Memory%20Forensics/memory-forensics.md
- Judge Conformal. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Judge%20Conformal/llm_judge_conformal_manuscript.md
- Black Lake repository README. https://github.com/Delphoa/Black-Lake/blob/main/README.md

## Appendix

### Reported Result Snapshot

| Setting | Reported result | Interpretation boundary |
|---|---:|---|
| Table 2 no-defense average, Strategy | Utility 0.19; ASR 0.99 | 13 heterogeneous dataset/task variants; author-reported |
| Table 2 SecAlign++ average, Strategy | Utility 0.45; ASR 0.21 | Lower ASR with lower clean average utility |
| Table 2 PromptArmor average, Strategy | Utility 0.21; ASR 0.92 | Adaptive attack defeats reported static robustness |
| Table 3 GPT-5, Direct on SQuAD v2 | Utility 0.81; ASR 0.70 | Named model/version and task only |
| Table 4 no defense, NQ knowledge corruption | Utility 0.43; ASR 0.81 | Task-aligned disinformation setting |
| Table 10 PISanitizer, Strategy | Utility 0.48; ASR 0.85 | Search-method comparison on SQuAD v2 |

### Workflow Validation

- Candidate universe: 75,777 PDFs representing 75,776 unique parent units.
- Draw: uniform random index 1,108; accepted first draw.
- Dedup: zero substantive prior deposits, zero exclusions, zero reselections, one metadata-only inventory row.
- Initial source state: partial because full-paper HTML was missing.
- Repair: official HTML and metadata fetched once; valid PDF preserved; zero remaining partials.
- Final source state: complete; PDF and full-paper HTML passed all required gates.
- Cache: miss to cached in `missing-only` mode; `pypdf` fallback and `html-regex` succeeded.
- Source policy: original and derived source documents withheld locally; no `.source/` directory created.
- Validation boundary: source inspection completed; scientific reproduction not performed.
