---
title: "RepoMasterEval - DEP-E"
generated_at: "2026-07-21"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of RepoMasterEval's repository-level code-completion benchmark and executable evaluation design."
source_status: "complete local PDF, full-paper HTML, metadata HTML, and source bundle inspected; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-21"
temporal_cutoff: "arXiv:2408.03519v2 revised 2025-10-31; ASE 2025 program record"
primary_url: "https://arxiv.org/abs/2408.03519"
stable_identifier: "arXiv:2408.03519v2; DOI 10.48550/arXiv.2408.03519"
confidence_summary: "High for identity, method reconstruction, and table transcription; medium for benchmark validity; low for independent reproducibility and broad industrial correlation."
safety_scope: "authorized offline benchmark evaluation, sandboxed code execution, and public-safe implementation planning"
distribution_notes: "No PDF, HTML, source archive, extracted text, cache, rendering, local path, or repair record is redistributed."
---

# RepoMasterEval - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | RepoMasterEval arXiv record | Primary metadata | HTML | arXiv:2408.03519v2; DOI 10.48550/arXiv.2408.03519 | https://arxiv.org/abs/2408.03519 | Links CC BY-NC-SA 4.0; metadata only | 2026-07-21 | Inspected |
| S2 | RepoMasterEval complete paper | Primary artifact | PDF | v2; revised 2025-10-31; 12 pages | https://arxiv.org/pdf/2408.03519 | Verified local copy withheld | 2026-07-21 | Full text, tables, and figures inspected |
| S3 | RepoMasterEval full-paper HTML | Primary artifact | HTML | v1 fallback | https://arxiv.org/html/2408.03519v1 | Verified complete-paper local copy withheld | 2026-07-21 | Inspected for structure and cross-checking |
| S4 | RepoMasterEval source bundle | Primary artifact | TeX/source archive | 30 readable entries | https://arxiv.org/e-print/2408.03519 | Local copy withheld | 2026-07-21 | Method, tables, and results inspected |
| S5 | ASE 2025 Industry Showcase | Official venue record | Conference page | 40th IEEE/ACM ASE, Industry Showcase | https://conf.researchr.org/details/ase-2025/ase-2025-industry-showcase/50/RepoMasterEval-Evaluating-Code-Completion-via-Real-World-Repositories | Program metadata | 2026-07-21 | Inspected |
| S6 | Repository Context Modalities DEP | Related Black Lake artifact | Markdown | DEP-A-20260716 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-Repo%20Context%20Modalities/2604.13725-whitepaper-review.md | Repository synthesis context | 2026-07-21 | Inspected |
| S7 | CLOVER Test Benchmark DEP | Related Black Lake artifact | Markdown | DEP-E-20260719 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-CLOVER%20Test%20Benchmark/clover_test_benchmark_manuscript.md | Repository synthesis context | 2026-07-21 | Inspected |
| S8 | Smart Coverage Goals DEP | Related Black Lake artifact | Markdown | DEP-E-20260717 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Smart%20Coverage%20Goals/smart_coverage_goals_manuscript.md | Repository synthesis context | 2026-07-21 | Inspected |
| S9 | Black Lake repository rules | Deposition authority | Markdown | Live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md and https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Public repository governance | 2026-07-21 | Inspected live |
| S10 | Black-Lake-Data repository rules | Related-repository authority | Markdown | Live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Public repository governance | 2026-07-21 | Inspected live |

Paper/work metadata:

- `Full title`: *RepoMasterEval: Evaluating Code Completion via Real-World Repositories*.
- `Authors`: Qinyun Wu, Chao Peng, Pengfei Gao, Ruida Hu, Haoyu Gan, Bo Jiang, Jinhe Tang, Zhiwen Deng, Zhanming Guan, Cuiyun Gao, Xia Liu, and Ping Yang.
- `Affiliations shown in the paper`: ByteDance and Harbin Institute of Technology, Shenzhen.
- `Initial submission`: 2024-08-07.
- `Inspected revision`: arXiv v2, revised 2025-10-31.
- `Subjects`: Software Engineering (`cs.SE`) and Artificial Intelligence (`cs.AI`).
- `Venue context`: ASE 2025 Industry Showcase.
- `License`: CC BY-NC-SA 4.0 as linked from the arXiv record.
- `Source files deposited`: none. All original and intermediate source material is withheld locally.
- `Implementation availability`: no verified public benchmark implementation was established from the inspected paper, source bundle, arXiv record, venue record, or bounded exact-name search.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S4 | Primary paper, metadata, and source | Identity, versions, authors, abstract, full text, TeX, tables, figures, and references | Source identity and complete-paper review | High | HTML fallback is v1 while current PDF/source record is v2 |
| E2 | S2-S4, Sections III.A-III.C, Tables II-III | Primary method evidence | Prefix/mask/suffix/retrieved-context/test structure; six repositories; coverage-based hole construction; BM25 retrieval | Benchmark construction | High for source reporting | Benchmark artifact and repository snapshots were not rerun |
| E3 | S2-S4, Section III.D, Tables IV-V | Primary test evidence | Mutation operators, original and augmented tests, mutation-score changes | Test-adequacy mechanism and reported gains | High for transcription | Equivalent mutants and manual-test process are not independently audited |
| E4 | S2-S4, Sections IV-V, Tables VI-VIII | Primary empirical evidence | Ten model configurations, five generations, Pass@k, exact match, Jaccard, pre/post augmentation results | Model comparison and metric behavior | High for reported values | No confidence intervals, seeds, or full output bundle inspected |
| E5 | S2-S4, Section V.C, Table XI | Primary slice evidence | Python/TypeScript category-level Pass@1 | Heterogeneous strengths and failure regions | High for transcription | Some slices are small; no uncertainty or multiple-comparison control |
| E6 | S2-S4, Section VI, Table XII | Primary industrial evidence | Relative changes across confidential internal versions; Spearman correlation 0.9601 | Offline-online association | Medium | Absolute values, sample sizes, cohorts, and uncertainty are withheld; correlation is not causal |
| E7 | S5 | Official venue evidence | Title, authors, track, schedule, and abstract | ASE 2025 placement | High | Venue page is not independent replication |
| E8 | S6-S8 | Related DEP evidence | Context quality-cost frontier, executable test contracts, coverage/mutation objective selection | Cross-DEP synthesis | Medium to high | Conceptual relation; no joint experiment |
| E9 | S9-S10 and process records | Governance/process evidence | Live rules, uniform draw, dedup scan, source repair, validation, and source withholding | Deposit compliance and provenance | High | Operational evidence, not paper evidence |

## Executive Summary

RepoMasterEval argues that code-completion benchmarks should resemble the in-editor task rather than isolated natural-language programming exercises. Its 288 tasks come from six real Python and TypeScript repositories. Each task masks a test-covered code snippet and supplies prefix, suffix, up to five BM25-retrieved cross-file snippets, and executable tests. The benchmark spans line, block, and function completion and groups tasks into 13 functional categories [E2].

The strongest methodological contribution is test-suite strengthening. The authors apply mutation testing, then add human-LLM-authored tests for surviving mutants. They report adding 186 tests to 1,105 existing tests, raising mutation score from 73.6% to 84.5% for Python and from 58.0% to 68.2% for TypeScript. Every evaluated model configuration loses pass rate under the stronger tests, indicating that the original suites accepted some faulty completions [E3-E4]. This supports test augmentation as a stricter filter; it does not prove that the resulting suites are complete or free of overfitting.

Among the ten reported configurations, DeepSeek-Coder-Base-33B has the best Pass@1 on both Python (44.87%) and TypeScript (34.57%). GPT-3.5 has the best reported Python Pass@5 at 55.65%, while DeepSeek-Coder-Base-33B has the best TypeScript Pass@5 at 40.46%. Exact match and Jaccard similarity do not track functional correctness cleanly, reinforcing the value of executable evaluation [E4].

The paper also reports a Spearman correlation of 0.9601 between RepoMasterEval performance and online suggestion acceptance across confidential internal model versions [E6]. This is promising but not independently verifiable. The record lacks absolute production values, uncertainty, cohort detail, a preregistered analysis, and evidence from multiple organizations. Reviewer confidence is high in the benchmark mechanism and table transcription, medium in the benchmark's validity for similar repository-completion settings, and low that the industrial correlation generalizes without a larger replication.

## Detailed Summary

### Problem Context

Widely used coding benchmarks often ask a model to implement a complete function or class from a descriptive prompt. Real IDE completion is different: the cursor may sit inside a function or block, no natural-language description may exist, and useful evidence may live in neighboring files. Textual similarity is also an unreliable correctness oracle because distinct implementations can satisfy the same tests.

RepoMasterEval addresses three linked gaps. It broadens completion granularity, supplies repository context, and executes model output. It also treats test adequacy as part of benchmark construction instead of assuming that an existing suite is authoritative.

### Task and Data Construction

The benchmark uses three Python repositories (`gpt-engineer`, `semantic-router`, and `raven`) and three TypeScript repositories (`epic-stack`, `lobe-chat`, and `ant-design-web3`). The paper selects repositories created after March 2023, with at least 100 stars and passing tests, to reduce obvious contamination and ensure executable tasks [E2]. This cutoff mitigates leakage but cannot establish that model pretraining, instruction tuning, or later continued training excluded the repositories.

Coverage reports identify source regions exercised by existing tests. The authors convert those regions into 288 masked tasks: 115 Python and 173 TypeScript. Python tasks are reported as 69.5% block, 16.5% line, and 13.0% function completion. TypeScript tasks are 45.0% block, 11.6% line, and 43.4% function completion. Experienced developers spend six person-days labeling tasks into 13 functional categories.

Each task contains five components: prefix, masked code, suffix, retrieved repository information, and tests. BM25 ranks sliding-window snippets from other files using the constrained prefix as the query; at most five snippets enter the prompt. The model generates the masked code, which is reinserted into the repository before tests run.

### Test Augmentation

Mutation testing introduces systematic faults such as arithmetic, logical, relational, conditional, assignment, and statement mutations. Existing tests execute against the mutants. Surviving mutants prompt new tests through human-LLM collaboration, followed by human repair when generated tests do not compile. The process repeats until the targeted mutants are killed [E3].

The six repositories begin with 1,105 tests and receive 186 additional tests. Aggregate mutation score rises by 10.9 percentage points for Python and 10.2 points for TypeScript. Coverage changes much less: the paper reports Python moving from 71% to 72% and TypeScript remaining at 42%. This gap is important. Coverage measures whether code executes; mutation score asks whether tests detect selected behavioral changes. Neither is a complete semantic oracle, but their disagreement exposes weaknesses that coverage alone misses.

### Experimental Evaluation

The paper evaluates ten configurations: DeepSeek-Coder base models at 1.3B, 6.7B, and 33B; DeepSeek-Coder-Instruct 6.7B; CodeQwen 7B; StarCoder2 at 3B and 15B; Codestral 22B; GPT-4-0125-Preview; and GPT-3.5-Turbo-Instruct. Each model generates five candidates per task. Metrics include Pass@1, Pass@3, Pass@5, exact match, and Jaccard similarity [E4].

Stronger tests reduce pass rate for every model. Python reductions range from 1.91 to 5.56 percentage points; TypeScript reductions range from 1.86 to 6.93 points. The result supports the narrow conclusion that augmented suites reject completions that original suites accepted. The study does not classify every newly rejected completion, so some risk of overly strict tests or equivalent-mutant effects remains.

The DeepSeek base series shows a broadly monotonic scale trend in functional pass rate. The instruct variant scores better than the comparable base model on HumanEval in the paper's comparison but worse on RepoMasterEval. An inspected example shows the instruct model continuing with extra functions beyond the masked region. This supports a task-format explanation: instruction following and fill-in-the-middle discipline are not interchangeable capabilities.

### Category and Production Findings

Category-level results show that no model dominates every code domain. Python models are comparatively stronger on common tools, programming basics, and selected data/NLP categories; TypeScript models show better performance in front-end and language-feature slices than server-side tasks. These tables are diagnostic, but small and uneven slice sizes make fine ranking differences uncertain [E5].

For industry validation, the paper compares relative benchmark and online acceptance changes across confidential internal model versions. It reports six months of deployment, roughly one month per model, and Spearman correlation 0.9601. The same prompting and prediction strategy is used offline and online. This alignment is a strength, but the small number of versions, withheld raw values, and shared system components make the estimate fragile and non-causal [E6].

### Availability and Version Boundary

The current arXiv record is v2 and the complete inspected PDF has 12 pages. The verified full-paper HTML fallback is v1, so PDF/source evidence takes precedence for revision-sensitive claims. The source bundle contains the TeX tables and example code used to cross-check extraction. No verified public implementation, data release, environment lock, or output bundle was established; therefore this artifact does not claim reproduction.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | RepoMasterEval more closely models repository-level fill-in-the-middle completion than description-led function benchmarks. | Author claim | E2; task structure and Table I | Supported as a design comparison; real-world representativeness remains limited to six selected repositories | Medium-high |
| C2 | Mutation-guided augmentation improves test adequacy. | Author claim | E3; mutation and coverage tables | Supported for the selected mutation operators and repositories; completeness and equivalent-mutant handling are not established | High within scope |
| C3 | Stronger tests reveal overestimated model performance. | Author claim | E4; all ten configurations lose pass rate after augmentation | Directly supported by reported paired benchmark values; rejection quality was not independently audited | High for reported result |
| C4 | Pass rates better reflect functional capability than exact match or Jaccard similarity. | Author interpretation | E4; divergent metrics and executable tests | Plausible and well motivated, but requires oracle-quality tests and broader alternative-solution audits | Medium-high |
| C5 | RepoMasterEval predicts production acceptance. | Author claim | E6; Spearman 0.9601 and relative version trends | Promising association, not a general validation result; underdocumented and statistically fragile | Low-medium |
| C6 | Context, oracle quality, and downstream validity should be audited as separate release gates. | Reviewer interpretation | E2-E8 | Strong synthesis across the primary paper and three related DEPs; not directly tested as one system | Medium |

## Methodology

- `Research objective`: Preserve a source-grounded review of RepoMasterEval and assess its use as a code-completion evaluation pattern.
- `Sources inspected`: Complete current PDF, verified full-paper HTML fallback, metadata HTML, TeX/source archive, rendered table pages, official arXiv record, official ASE program record, live repository rules, and exactly three related DEP artifacts.
- `Discovery strategy`: Uniform local archive draw, repository and memory deduplication, local source inspection, PDF text extraction, visual table review, TeX cross-checking, official-web verification, and bounded exact-name artifact search.
- `Inclusion criteria`: Primary or official evidence that identifies the paper, reconstructs its method/results, or directly supports one of the three selected conceptual bridges.
- `Exclusion criteria`: Abstract-only empirical claims, unverified code mirrors, generic secondary summaries, and related work without concrete overlap.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, safety, and replication analysis.
- `Evidence handling`: Major claims map to evidence IDs; author claims, reviewer interpretations, and unresolved availability are labeled separately.
- `Uncertainty handling`: Unavailable raw production results, version mismatch, missing implementation artifacts, and unreproduced metrics remain explicit.
- `Extraction process`: PDF text extraction was paired with visual inspection of the benchmark overview, mutation-score, model-result, category-result, and industry-result pages. TeX tables and prose were cross-checked without executing benchmark code.
- `Version control`: arXiv v2 governs revision-sensitive claims; v1 full-paper HTML is used only as a verified structural companion.
- `Reviewer stance`: DEP-ready paper review, critique, implementation translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: Benchmark construction, repository context, executable evaluation, test augmentation, empirical model results, industry correlation, and implementation implications.
- `Temporal boundary`: Sources accessed 2026-07-21; model and repository observations remain tied to the versions reported by the paper.
- `Evidence limits`: No benchmark run, model inference, repository snapshot reproduction, mutation campaign, or production-data reanalysis was performed.
- `Assumptions`: The arXiv PDF/source represent v2; the verified v1 HTML is not used to settle revision-sensitive discrepancies.
- `Constraints`: Original sources remain local; public artifacts omit local paths, machine identifiers, exact execution times, and non-public production information.
- `Out of scope`: Releasing the benchmark, evaluating current models, assessing the legality of every repository snapshot, or validating ByteDance production telemetry.
- `Intended use`: Research review, benchmark design, gated evaluation planning, and DEP deposition.
- `Audience`: Software-engineering researchers, code-model evaluators, developer-tool teams, and benchmark maintainers.
- `Reproducibility boundary`: Tables and source structure are inspectable; empirical and production claims are not independently reproduced.
- `Data sensitivity`: Public paper evidence plus confidential aggregate production evidence reported by the authors; no private data is present in this artifact.

## Observations

- `Observed pattern`: Mutation score changes substantially while line coverage barely moves, showing that coverage quantity and fault-detection quality are distinct.
- `Observed pattern`: Model ranking varies by language, metric, sampling budget, and task category; a single headline score hides operationally relevant failures.
- `Technical implication`: Completion-format discipline should be tested explicitly. A strong instruction model can fail by emitting correct-looking but structurally invalid extra code.
- `Contradiction or tension`: The benchmark seeks real-world validity, yet it relies on only six repositories and a fixed BM25 context policy.
- `Contradiction or tension`: The production correlation is the paper's strongest external-validity claim and its least inspectable evidence.
- `Open question`: Whether mutation-guided tests reject semantically valid alternatives often enough to change rankings is not reported.
- `Reviewer hypothesis`: A three-gate scorecard for context fidelity, oracle adequacy, and downstream correlation will transfer more reliably than any single aggregate benchmark score.

## Considerations

- Repository snapshots need license, commit, dependency, and test-environment manifests. A repository name and date are not enough for replay.
- Executing model-generated code requires disposable, network-denied sandboxes with CPU, memory, process, filesystem, and timeout limits.
- Test augmentation can overfit to chosen mutation operators or reject valid alternative behavior. Manual audits and seeded real faults should complement mutation score.
- User acceptance is affected by latency, suggestion frequency, UI placement, trust, and workflow, not only code correctness. Product telemetry needs a causal design before it becomes a model-quality label.
- Benchmark tasks may leak private or licensed repository content if prompts, outputs, or traces are published without governance.
- Model, tokenizer, context-window, decoding, and provider changes make leaderboard values time-sensitive.

## Strengths

- The benchmark aligns task format with practical fill-in-the-middle completion rather than relying on natural-language function specifications.
- Executable tests allow functionally equivalent completions that exact-match scoring would penalize.
- Mutation-guided augmentation treats the evaluator itself as an object of validation.
- Line, block, and function tasks plus category slices expose more failure modes than one undifferentiated aggregate.
- The industry study attempts an external product signal, which many benchmark papers omit.

## Weaknesses

- Six repositories, two languages, and 288 tasks limit ecological coverage.
- Repository recency reduces but does not eliminate training contamination.
- No verified public benchmark artifact, pinned repository SHAs, environment lock, generated-output bundle, or full rerun path was established.
- The test-augmentation process lacks equivalent-mutant analysis, inter-reviewer agreement, and a false-rejection audit for valid alternatives.
- Model results omit confidence intervals and do not expose repository-level variance.
- The reported 0.9601 production correlation relies on a small, confidential sequence with withheld absolute values and no uncertainty.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish immutable task and environment manifests | Reproducibility | Repository state and dependencies change | Deterministic replay and license audit | Maintenance burden | Rebuild every task from commit SHAs in clean runners |
| Add oracle false-positive and false-negative audits | Measurement validity | Mutation score does not prove semantic completeness | Safer functional scoring | Requires expert review | Seed real faults and valid alternative implementations |
| Compare context policies under equal token budgets | Retrieval validity | BM25 is only one repository-context policy | Separates benchmark difficulty from retrieval choice | More inference cost | Problem-only, BM25, dependency, random, and oracle ablations |
| Report uncertainty and repository-stratified results | Statistical validity | Aggregate values hide small-slice and repository effects | More reliable rankings | Larger run budget | Paired bootstrap and hierarchical models |
| Replicate production validity across teams | External validity | One confidential deployment cannot establish generality | Better evidence for release-gate use | Privacy and coordination burden | Preregistered multi-team study with deidentified aggregates |
| Version the benchmark as an evolving panel | Contamination control | Static tasks become training targets | Longer useful lifetime | Comparability tradeoff | Maintain frozen and rolling tracks with overlap calibration |

## Potential Implementations

1. `Repository completion release gate`
   - `User`: code-model and IDE teams.
   - `Goal`: prevent deployment when a model regresses on realistic repository completion.
   - `Core mechanism`: run pinned fill-in-the-middle tasks through a model adapter, execute outputs in isolated environments, and stratify results by repository, language, and granularity.
   - `Required inputs`: licensed snapshots, task manifests, prompts, test oracles, model/version metadata, and resource policy.
   - `Outputs`: Pass@k, format-failure rate, repository confidence intervals, regression alerts, and signed receipts.
   - `Risk controls`: network denial, no credentials, immutable source mounts, redacted logs, and bounded compute.
   - `Evaluation`: replay a synthetic smoke corpus, then a licensed frozen panel.
2. `Test-adequacy audit service`
   - `User`: benchmark maintainers and QA engineers.
   - `Goal`: detect weak tests before they become model-quality oracles.
   - `Core mechanism`: combine coverage, mutation score, seeded-defect detection, and valid-alternative review.
   - `Required inputs`: tests, mutation configuration, fault seeds, expected behavior, and equivalence-review notes.
   - `Outputs`: adequacy matrix, surviving mutants, likely equivalent mutants, and reviewer queue.
   - `Risk controls`: isolated execution, operator allowlist, timeout policy, and no automatic production merge.
   - `Evaluation`: compare the service against hand-labeled strong and weak suites.
3. `Offline-online calibration monitor`
   - `User`: developer-product analytics and model governance teams.
   - `Goal`: estimate whether offline benchmark changes predict acceptance without overstating causality.
   - `Core mechanism`: join versioned offline receipts with deidentified, aggregate online metrics and fit preregistered lagged analyses.
   - `Required inputs`: model version, benchmark result, rollout cohort, latency, suggestion policy, and aggregate acceptance.
   - `Outputs`: effect intervals, drift warnings, confounder notes, and go/no-go evidence.
   - `Risk controls`: minimum cohort thresholds, no raw code telemetry, privacy review, and human approval.
   - `Evaluation`: backtest on historical rollouts and verify prospective calibration.

## Three Ways to Exercise This Research

1. `Synthetic completion replay`: Build a tiny synthetic Python/TypeScript pair with known line, block, and function masks; compare exact match with executable tests. Success means valid alternatives pass while malformed or semantically wrong completions fail. Stop if sandbox isolation is unavailable.
2. `Mutation adequacy experiment`: Apply a bounded operator set to a synthetic module, measure coverage and mutation score before and after adding tests, and inspect every changed verdict. Success means the stronger suite kills intended faults without rejecting valid alternatives. Stop when equivalent mutants cannot be adjudicated.
3. `Context-policy ablation`: Hold tasks and token budget fixed while comparing problem-only, random-file, BM25, and dependency-aware context. Success means results expose quality, latency, and failure differences with paired uncertainty. Stop before private repositories or uncontrolled provider cost enter the run.

## Example MVP Product

- `Product name`: RepoGate.
- `Target user`: a team evaluating a code-completion model or retrieval change before IDE rollout.
- `Problem`: common coding benchmarks can reward description-led synthesis, weak test suites, or text similarity while missing repository-level completion failures.
- `Core workflow`: import a versioned task manifest; validate license and environment; construct a bounded context pack; request a completion; run it in a disposable sandbox; record syntax, format, test, mutation, latency, and provenance outcomes; compare against the approved baseline.
- `Data requirements`: synthetic or licensed repository snapshots, pinned commits and dependencies, masks, tests, mutation configuration, model metadata, and a redaction policy.
- `Architecture`: CLI orchestrator -> manifest validator -> context-policy adapters -> model adapters -> network-denied runner -> test/mutation evaluator -> signed result ledger -> release dashboard.
- `Success metrics`: zero host mutations; 100% smoke-corpus evaluator agreement; reproducible receipts; repository-stratified confidence intervals; and a documented release decision.
- `Risk controls`: no secrets, read-only sources, isolated workspaces, network disabled by default, output limits, dependency allowlists, and human approval for rollout.
- `Limitations`: not a reproduction of RepoMasterEval; synthetic tasks underrepresent real repositories; tests and mutation operators remain incomplete proxies; online validity requires separate evidence.
- `MVP boundary`: Python and TypeScript, ten synthetic or permissively licensed tasks per language, four context policies, two model adapters, and no autonomous code deployment.
- `Deployment model`: local-only CLI plus static HTML report.
- `Evaluation plan`: unit-test manifest and evaluator logic, adversarial output fixtures, repeated end-to-end runs, and an isolation review.
- `Failure modes`: flaky dependencies, context truncation, equivalent-mutant misclassification, permissive tests, non-code model output, and accidental source disclosure.
- `Maintenance plan`: pin dependencies, rotate rolling tasks, archive receipts, review mutation operators quarterly, and recalibrate thresholds per model family.

Illustrative result contract:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class CompletionResult:
    task_id: str
    context_policy: str
    syntax_ok: bool
    tests_passed: int
    tests_total: int
    mutation_score: float
    source_disclosed: bool = False

def release_eligible(result: CompletionResult) -> bool:
    return (
        result.syntax_ok
        and result.tests_passed == result.tests_total
        and result.mutation_score >= 0.80
        and not result.source_disclosed
    )
```

This toy contract is intentionally conservative. Production thresholds require repository-stratified calibration, uncertainty, and human governance.

## Related Research and Reading

Exactly three related DEP entries were selected for concrete overlap:

| Item | Type | Relevance | Source Basis |
|---|---|---|---|
| [Repository Context Modalities](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-Repo%20Context%20Modalities/2604.13725-whitepaper-review.md) | Related DEP review | Both study repository-level code completion/generation under constrained cross-file context. This entry adds matched comparisons among text, vector, and visual compression, turning RepoMasterEval's fixed BM25 context into an explicit quality-cost design choice. | DEP review of https://arxiv.org/abs/2604.13725v1 and its complete paper |
| [CLOVER Test Benchmark](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-CLOVER%20Test%20Benchmark/clover_test_benchmark_manuscript.md) | Related DEP manuscript | Both use real repositories, executable tests, coverage-aware construction, and long code context. CLOVER's distinction between execution and requirement/coverage success sharpens RepoMasterEval's single pass/fail oracle. | DEP review of https://arxiv.org/abs/2502.08806 and official venue context |
| [Smart Coverage Goals](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Smart%20Coverage%20Goals/smart_coverage_goals_manuscript.md) | Related DEP manuscript | Both use coverage and mutation evidence to improve test generation/evaluation. Smart Coverage Goals shows that retaining or removing objectives creates criterion-specific tradeoffs rather than a universally stronger test suite. | DEP review of https://arxiv.org/abs/2208.04096 and ASE artifact context |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2408.03519 | Identity, version, authors, abstract, subjects, DOI, license | 2026-07-21 | Primary metadata |
| R2 | https://arxiv.org/pdf/2408.03519 | Full methods, tables, figures, results, discussion, references | 2026-07-21 | Current complete PDF; local copy withheld |
| R3 | https://arxiv.org/html/2408.03519v1 | Full-paper structural cross-check | 2026-07-21 | Verified v1 fallback; local copy withheld |
| R4 | https://arxiv.org/e-print/2408.03519 | TeX tables, method prose, example code, references | 2026-07-21 | Source archive withheld |
| R5 | https://doi.org/10.48550/arXiv.2408.03519 | Stable DOI | 2026-07-21 | arXiv-issued DOI |
| R6 | https://conf.researchr.org/details/ase-2025/ase-2025-industry-showcase/50/RepoMasterEval-Evaluating-Code-Completion-via-Real-World-Repositories | ASE 2025 venue placement | 2026-07-21 | Official conference record |
| R7 | https://creativecommons.org/licenses/by-nc-sa/4.0/ | License terms linked by arXiv | 2026-07-21 | No source redistributed |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-Repo%20Context%20Modalities/2604.13725-whitepaper-review.md | Related context-compression DEP | 2026-07-21 | Exactly one of three related entries |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-CLOVER%20Test%20Benchmark/clover_test_benchmark_manuscript.md | Related executable-test DEP | 2026-07-21 | Exactly one of three related entries |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Smart%20Coverage%20Goals/smart_coverage_goals_manuscript.md | Related mutation/coverage DEP | 2026-07-21 | Exactly one of three related entries |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository rules | 2026-07-21 | Live default branch inspected |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP class, filing, indexing, and source-locality rules | 2026-07-21 | Live default branch inspected |
| R13 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository rules and dedup context | 2026-07-21 | Live default branch inspected |

## Appendix

### Random Selection and Deduplication

- `Enumeration`: `rg --files -g "*.pdf"` found 75,779 PDFs in 75,776 parent-directory paper units.
- `Identifier exclusion`: 220 units matched the normalized identifier set from existing Black Lake artifacts and automation memory.
- `Eligible set`: 75,556 units.
- `Random draw`: PowerShell `Get-Random`, zero-based eligible index 45,351, first draw.
- `Reselections`: 0.
- `Acceptance scan`: arXiv ID, DOI, normalized title, and slug were checked across Black Lake `.logs`, `.reports`, `.lake-data`, the public dedup index, automation memory, and relevant Black-Lake-Data records.
- `Related-repository result`: only a metadata inventory row was found; no prior review or DEP owns the paper.
- `24-hour gate`: no same-paper marker was found.

### Local Source-Integrity Receipt

- `Initial classification`: partial; a valid 774,901-byte PDF existed, but full-paper HTML was missing.
- `PDF checks`: size threshold, `%PDF-` header, trailing `%%EOF`, parse, 12-page metadata, and SHA-256 all passed; the file was preserved.
- `Repair`: bounded single-paper companion acquisition collected metadata HTML, verified full-paper HTML, and a source archive while preserving partials for inspection if any had occurred.
- `HTML checks`: 461,536 bytes, 66,400 body characters after script/style removal, document marker present, 56 section/heading markers, and six structure terms.
- `Source checks`: 484,515 bytes and 30 readable archive entries.
- `Final classification`: complete; zero partial files.
- `Version note`: current PDF/source evidence governs v2 claims; the verified HTML fallback is v1.
- `Public-source policy`: all PDF, HTML, metadata, TeX/source, extracted content, caches, renderings, and repair records were withheld locally. No `.source/` directory was created and no source file was uploaded.

### Replication Checklist

- Acquire a licensed, immutable snapshot for each repository and record commit SHAs.
- Recreate masks from coverage with a versioned task manifest.
- Pin BM25 tokenization, windowing, ranking, and prompt assembly.
- Validate original and augmented tests against seeded faults and valid alternatives.
- Run model adapters with fixed decoding and five candidates per task.
- Report repository-stratified Pass@k, format failures, latency, and uncertainty.
- Separate offline benchmark evidence from deidentified online-product evidence.
