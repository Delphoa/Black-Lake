---
title: "CLOVER Test Benchmark - DEP-E"
generated_at: "2026-07-19"
artifact_type: "DEP research artifact and paper report"
primary_subject: "A source-grounded review of CLOVER's coverage-guided, long-context benchmark for LLM-generated Python tests."
source_status: "verified local complete; public URLs only"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-19"
temporal_cutoff: "arXiv v1 and public records available through 2026-07-19"
primary_url: "https://arxiv.org/abs/2502.08806"
stable_identifier: "arXiv:2502.08806v1; DOI:10.48550/arXiv.2502.08806"
confidence_summary: "High for paper identity, mechanism, and table transcription; medium for generalization and reproducibility because the benchmark was not rerun and an official release repository was not established."
safety_scope: "defensive software evaluation in isolated, authorized environments"
distribution_notes: "Original PDF, HTML, metadata, and source-package files are withheld in the private local archive and are not included in this DEP."
---

# CLOVER Test Benchmark - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | *CLOVER: A Test Case Generation Benchmark with Coverage, Long-Context, and Verification* | Primary paper | Verified PDF, full-paper HTML, and TeX/source package | arXiv:2502.08806v1 | https://arxiv.org/abs/2502.08806 | arXiv version is CC BY-NC-SA 4.0; originals withheld locally | 2026-07-19 | Complete paper inspected |
| S2 | arXiv full-paper HTML | Primary paper rendering | HTML | arXiv:2502.08806v1 | https://arxiv.org/html/2502.08806 | Full document, not the `/abs/` metadata page | 2026-07-19 | Structurally verified and inspected |
| S3 | arXiv PDF | Primary paper rendering | PDF | arXiv:2502.08806v1 | https://arxiv.org/pdf/2502.08806 | Public equivalent of the verified local PDF; not redistributed | 2026-07-19 | Sixteen pages; visually inspected |
| S4 | arXiv source package | Primary source | TeX/source archive | arXiv:2502.08806v1 | https://arxiv.org/e-print/2502.08806 | Used locally to cross-check tables, prompts, URLs, and source structure; not redistributed | 2026-07-19 | Inspected locally |
| S5 | DL4C @ ICLR 2025 record | Venue record | OpenReview page | OpenReview:gPpQa4PGEZ | https://openreview.net/forum?id=gPpQa4PGEZ | Record reports CC BY 4.0 for the workshop version | 2026-07-19 | Inspected by URL |
| S6 | Jiacheng Xu publication list | Author context | Author-maintained page | Publication listing | https://jiacheng-xu.github.io/ | Confirms the paper and author list; no implementation claims imported | 2026-07-19 | Inspected by URL |
| S7 | Black Lake repository rules | Repository authority | README | fetched default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Controls public layout, attribution, naming, and source locality | 2026-07-19 | Inspected live before drafting |
| S8 | Black Lake DEP rules | Repository authority | README | fetched default branch | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Controls DEP-E container filing and publication-index maintenance | 2026-07-19 | Inspected live before drafting |
| S9 | Black-Lake-Data rules | Related-repository authority | README | fetched default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Read before cross-repository dedup and related-entry reliance | 2026-07-19 | Inspected live before drafting |

- `Paper title`: *CLOVER: A Test Case Generation Benchmark with Coverage, Long-Context, and Verification*.
- `Authors`: Jiacheng Xu; Bo Pang; Jin Qu; Hiroaki Hayashi; Caiming Xiong; Yingbo Zhou.
- `Producing organization`: Salesforce AI Research.
- `Primary subject`: Software Engineering (`cs.SE`); additional subjects Artificial Intelligence (`cs.AI`) and Machine Learning (`cs.LG`).
- `Submission/version date`: arXiv v1 submitted 2025-02-12. No later arXiv version was shown in the inspected record.
- `Venue context`: DL4C @ ICLR 2025, long-paper track, published on OpenReview in March 2025.
- `DOI`: https://doi.org/10.48550/arXiv.2502.08806.
- `Benchmark cutoff`: 2024-08-30, according to Appendix A.
- `Local source file paths`: withheld by repository policy. No original source file is copied into this DEP.
- `Code/data availability`: the paper says code, benchmark data, Docker environment, and recipes will be released. No official CLOVER repository or dataset release was established from the inspected source package, arXiv/OpenReview records, author page, Hugging Face paper record, or exact GitHub searches. This review therefore does not claim that the artifact is presently reproducible.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | https://arxiv.org/pdf/2502.08806 and https://arxiv.org/html/2502.08806 | Primary paper | Abstract, method, equations, Tables 1-8, figures, prompts, limitations, impact statement, and appendices | Benchmark construction, tasks, metrics, model results, limitations | High | Author-reported study; experiments not rerun |
| E2 | https://arxiv.org/abs/2502.08806 | Primary metadata | Title, ordered authors, version date, subjects, DOI, license, public artifact links | Identity and version pinning | High | Abstract alone is not used for empirical claims |
| E3 | https://arxiv.org/e-print/2502.08806 | Primary source | TeX table files, prompt files, bibliography, and absence of a paper-specific code URL | Table/prompt cross-checking and release-status caution | High for inspected source; medium for global absence | A later unlinked release could exist |
| E4 | https://openreview.net/forum?id=gPpQa4PGEZ | Official venue record | DL4C @ ICLR 2025 status, dates, track, keywords, and license | Venue context | High | Venue page is not an independent replication |
| E5 | [Smart Coverage Goals DEP](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Smart%20Coverage%20Goals/smart_coverage_goals_manuscript.md) | Related DEP artifact | Search-based testing objectives, coverage-signal selection, and evaluation tradeoffs | Coverage-governance bridge | High for the DEP's stated synthesis | Related paper studies Java/SBST, not LLM test generation |
| E6 | [TACO Terminal Context DEP](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-TACO%20Terminal%20Context/2604.19572-whitepaper-review.md) | Related DEP artifact | Adaptive observation filtering, terminal benchmarks, token/accuracy tradeoffs, and complaint-based repair | Long-context and execution-harness bridge | High for the DEP's source-grounded account | Later agent system; not a direct CLOVER baseline |
| E7 | [ContextWeaver DEP](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-ContextWeaver%20Selective%20a/2604.23069-whitepaper-review.md) | Related DEP artifact | Dependency-structured memory, test-result tracking, and selective context retention | Dependency-aware retrieval bridge | Medium | Review reports paper results without independent reproduction |
| E8 | https://github.com/Delphoa/Black-Lake/blob/main/README.md and https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Repository authority | DEP-E path, README, source-withholding, indexing, attribution, and commit rules | Deposit compliance | High | Operational authority, not research evidence |
| E9 | Local integrity verification, summarized publicly without paths | Local verification record | PDF header/EOF, HTML size/body/marker/headings/structure, metadata, source package, and partial-file checks | Complete-source gate | High | Private local files are intentionally not published |

## Executive Summary

CLOVER evaluates whether language models can complete or generate executable Python tests while satisfying increasingly specific requirements. It contributes three tasks: assertion-mask completion, target-aware test implementation, and coverage-oriented test implementation. The authors construct 845 unique problems from 12 permissively licensed repositories and expand them to 5,312 instances across problem-only and 4k-128k contextual settings [E1]. Their distinctive move is to derive an oracle context order from execution coverage: files uniquely associated with a peer test are ranked above less discriminative files, while repository-baseline files that are covered even by an empty test rank last.

The paper's strongest evidence is diagnostic rather than a claim of solved test generation. On Task III, GPT-4o reaches a reported 32.7% success rate at 64k context, while no evaluated open-source model exceeds 10%. Execution rates are consistently higher than requirement-satisfying success rates; for GPT-4o at 64k, the reported values are 42.1% execution and 32.7% success. Longer context is also not monotonically helpful. Several open-source models collapse at or after 16k even though the input fits their advertised window, while selected proprietary models extract modest gains from coverage-ranked context [E1].

Reviewer interpretation: CLOVER is best read as a benchmark-design paper about three coupled contracts—source selection, executable verification, and context budgeting. It shows that “the test runs” is weaker than “the test satisfies the requested behavioral or coverage condition,” and that an oracle retrieval set can still overwhelm a model. Confidence is high in the inspected mechanism and table transcription, but medium in broader conclusions because the study is limited to Python/pytest, model snapshots from 2024, 12 repositories, heuristic sandbox construction, and an unreproduced release status.

## Detailed Summary

### Problem and Benchmark Position

Existing code benchmarks often evaluate function synthesis, issue resolution, or shorter-context test generation. CLOVER asks a narrower but operationally important question: can a model write tests that both execute and obey explicit test requirements in a repository-scale setting? Table 1 positions CLOVER against SWE-bench, TestEval, TestBench, SWT-Bench, and TestGenEval. CLOVER's differentiators are three completion/generation tasks, executable repositories, coverage-based constructed context, and contexts up to 128k tokens.

The authors started from 42 Python repositories, automatically configured 25, and retained 12: Pillow, elasticsearch-py, flask, httpx, jinja, kombu, paramiko, pip, requests, sqlalchemy, starlette, and pylint. Repositories were excluded for unsupported pytest/pytest-cov workflows, environment-setup failures, nonstandard test/source layouts, evaluation cost, or external/system requirements. Eleven repositories required manual folder-name specification. This is evidence of realism, but also evidence that the pipeline is not fully automatic.

### Executable Sandbox and Verification

The benchmark extracts tests with Python AST tooling, preserves necessary setup, and packages repositories into Dockerized environments using Python 3.10. The `verify` API checks whether generated code can execute, with timeout handling, error logging, batching, and repository restoration. The `cov` API uses `pytest-cov` to report hit and missed lines even when execution fails. Evaluations run sequentially by task and concurrently across repositories, with a two-hour CPU budget per model and per-repository caps of 50 examples for Task I and 25 for Tasks II and III.

The inference setup uses vLLM with temperature `0.2` and `top_p=1.0`. Maximum output lengths are 200 tokens for Task I and 4,000 tokens for Tasks II and III. Ten open-source and four proprietary models are compared. The proprietary snapshots include GPT-4o `2024-08-06` and GPT-4o-mini `2024-07-18`; this version pinning is important because the results should not be read as a current leaderboard.

### Coverage-Calibrated Oracle Context

For each test case, CLOVER runs coverage twice: once with the real test and once with an empty `assert True` test placed in the same location. Files whose coverage does not change relative to the empty run form a repository baseline and are treated as low-information context. A peer baseline identifies source lines uniquely covered by one test among its neighboring tests. Files are then prioritized as peer-unique, other informative, and repository-baseline. If the budget cannot fit all files in a tier, files are randomly selected within that tier.

This mechanism is not learned retrieval and should not be treated as one. It is an oracle constructed from ground-truth test execution. Its value is experimental: it tests whether models can exploit deliberately relevant code when the retrieval problem is partially removed. Its limitation is equally important: production systems do not have the ground-truth test whose coverage trace CLOVER uses to construct context.

### Task I: Assertion Mask Prediction

Task I contains 513 unique problems drawn from 14,952 available candidates. It masks one operand or expression in a real assertion. The paper reports exact match (EM), execution rate (ER), and refined execution rate (RER). RER rejects trivial constant assertions and obvious copies, acknowledging that source-equivalent test code need not textually match the original.

In the problem-only setting, Table 3 reports RER values ranging from 34.3% for Magicoder 6.7B to 72.4% for Claude 3.5 Sonnet. In contextual settings, Table 4 reports the strongest value as 75.4% for Claude 3.5 Sonnet. The surrounding prose says 72.6% to 75.6%, while the table and visual PDF show 72.4% to 75.4%; this artifact treats the table as authoritative and records the prose discrepancy rather than smoothing it over.

Several shorter-window open models degrade sharply with larger inputs. Codestral-22B moves from 63.3% problem-only RER to 22.1% at 32k; Qwen 2.5 Coder 14B moves from 59.8% to 30.7%. By contrast, Llama 3.1-70B, Claude 3.5 Sonnet, and GPT-4o show positive best-case contextual gains. The pattern supports a bounded conclusion: declared window size does not imply effective context utilization under this task and serving configuration.

### Task II: Targeted Test Implementation

Task II contains 151 unique problems from 184 available candidates. The model receives a test skeleton and must call a specified class or function. Contextual settings range from 8k to 64k. Success requires both executable code and satisfaction of the named target constraint.

Table 5 reports a best success rate of 48.4% for Claude 3.5 Sonnet and GPT-4o in their best contextual settings. Claude improves from 26.9% problem-only to 46.2% at 8k and 48.4% at 32k/64k. GPT-4o improves from 28.7% problem-only to 48.4% at 64k. Some open-source models briefly improve at 8k but produce 0% success at 16k or 32k, with the authors reporting malformed or gibberish output under longer inputs.

### Task III: Coverage-Oriented Test Implementation

Task III contains 181 unique problems from 1,098 available candidates. It asks a model to cover up to ten code blocks across up to ten files, using 64k or 128k context. Blocks are selected deterministically from peer-unique coverage and must contain at least five lines. A response succeeds only when it executes and covers every requested block.

At 64k, reported success rates are 4.7% for Yi-Coder-9B, 1.9% for Llama 3.1-8B, 6.5% for Llama 3.1-70B, 19.6% for GPT-4o-mini, 28.0% for Gemini 1.5 Flash, 29.0% for Claude 3.5 Sonnet, and 32.7% for GPT-4o. At 128k, GPT-4o is slightly lower at 31.8%, while Claude rises to 30.8% and GPT-4o-mini to 21.5%.

Execution is not equivalent to satisfying coverage. At 64k, GPT-4o executes 42.1% of cases but succeeds on 32.7%; Gemini executes 38.3% but succeeds on 28.0%; Claude executes 34.6% but succeeds on 29.0%. The requirement gap is therefore a first-class benchmark result, not incidental noise.

### Safety, Legal, and Release Boundaries

The authors warn that generated code may be malicious or corrupted and recommend careful system configuration. Docker isolation reduces risk but did not prevent excluded repositories from sometimes exhausting memory and restarting a host. The paper reports organizational license review across BSD-3-Clause, Apache-2.0, MIT, and LGPL-2.1 repositories. This review did not independently audit every upstream snapshot, transitive dependency, or dataset redistribution right.

The paper promises release of code, data, container images, and recipes. The inspected source package contains paper assets and general tool URLs but no paper-specific repository locator. An exact search of the named GitHub organization and the paper identifier found no official implementation. This is negative evidence, not proof of permanent nonexistence; a later review should repeat the release search.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | CLOVER provides 845 unique problems and 5,312 contextual instances across three executable Python testing tasks. | Author benchmark claim | E1 | Directly supported by Tables 1-2 and task descriptions. | High |
| C2 | Coverage-calibrated oracle context distinguishes peer-unique evidence from repository-baseline noise. | Author method claim | E1, E3 | The mechanism is explicit and inspectable, but it relies on ground-truth execution unavailable during ordinary generation. | High for description; medium for production transfer |
| C3 | Longer context does not reliably improve code-test generation. | Author empirical claim | E1 | Strongly supported for several evaluated open models under the pinned vLLM/model setup; not a universal law about current models. | High for tested settings; medium for generalization |
| C4 | Leading proprietary models use supplied context more effectively than the evaluated open models. | Author comparative claim | E1 | Supported by Tables 4-5, but comparisons mix architectures, sizes, providers, and dated snapshots. | Medium |
| C5 | Task III remains difficult even with oracle context. | Author empirical claim | E1 | GPT-4o's reported best is 32.7% at 64k; no evaluated open model exceeds 10%. | High |
| C6 | Execution-only evaluation overstates test quality. | Derived inference from reported metrics | E1 | Table 6 shows 5-10 point gaps between execution and full coverage success; passing a parser/runtime is not enough. | High |
| C7 | CLOVER is a reusable benchmark implementation. | Release/availability claim | E1-E4 | The paper promises release, but this review did not establish an official code/data repository. Reusability remains unverified. | Low |
| C8 | Coverage traces can guide context selection beyond this benchmark. | Reviewer interpretation | E1, E5-E7 | Plausible bridge to selective objectives and dependency-aware memory, but it needs non-oracle retrieval experiments. | Medium |

## Methodology

- `Research objective`: preserve a source-grounded account of CLOVER's benchmark design, evidence, limitations, and implementation relevance while satisfying the DEP-E manuscript schema and automation integrity rules.
- `Sources inspected`: verified complete local PDF, official full-paper HTML, metadata HTML, TeX/source package, public arXiv record, OpenReview venue record, author publication page, fetched repository READMEs, release searches, and exactly three related Black Lake DEP entries.
- `Discovery strategy`: enumerated the local archive with `rg --files -g "*.pdf"`; collapsed results by parent directory; derived arXiv IDs; built a used-paper index from both repositories and automation memory; excluded duplicate and identifier-incomplete units; used a uniform `Get-Random` draw; repaired the selected source unit before review; inspected full-paper sections, tables, figures, appendices, and source files; then searched live repository trees for conceptual overlap.
- `Inclusion criteria`: sources had to identify the work, support a method/result claim, establish venue or release context, define repository rules, prove complete local source integrity, or ground one of the three DEP bridges.
- `Exclusion criteria`: abstract-only evidence was excluded from empirical support; secondary summaries, ambiguous “Clover” projects, unverified repository matches, local paths, and all original source documents were excluded from public output.
- `Analytical approach`: empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: quantitative claims were checked against PDF tables and full HTML; paper prose/table inconsistencies are disclosed; author claims and reviewer interpretations are labeled separately; negative release evidence is expressed cautiously.
- `Uncertainty handling`: no reproduction claim is made. Missing official release evidence, dated model snapshots, and untested transfer assumptions remain visible.
- `Extraction process`: PDF text extraction was paired with visual page inspection; full HTML and TeX table/prompt sources were cross-checked. No benchmark code or generated tests were executed.
- `Version control`: arXiv v1 and fetched default-branch repository states were used. Date-sensitive availability claims are bounded to 2026-07-19.
- `Random selection`: 75,778 PDFs collapsed to 75,776 parent units. The used index contained 810 arXiv IDs; 192 units were excluded by used ID and 185 identifier-incomplete units were withheld, leaving 75,399 eligible units. The uniform zero-based selected index was 33,124; duplicate reselections were zero.
- `Dedup and recency validation`: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and Black-Lake-Data `.lake-data`/`.reports` were scanned by arXiv ID, DOI, exact/normalized title, and slug. No match or same-unit marker on or after the public-safe 2026-07-18 cutoff was found.
- `Source-integrity handling`: the selected unit was initially partial because full-paper HTML was absent. The valid PDF was preserved; official arXiv full-paper HTML, metadata HTML, and the source package were fetched with bounded requests. The repaired unit passed the complete-source gate before synthesis.

## Scope, Constraints, and Assumptions

- `Scope`: CLOVER's task definitions, construction pipeline, coverage-calibrated context, evaluation setup, reported results, limitations, safety boundary, and implications for test-generation systems.
- `Temporal boundary`: arXiv v1, 2025 venue record, and public release state observed through 2026-07-19.
- `Evidence limits`: experiments and artifact were not run; model APIs and vLLM behavior were not recreated; no official CLOVER code/data repository was established; related DEP claims were not independently rerun here.
- `Assumptions`: PDF tables are authoritative when neighboring prose differs; the public arXiv/venue records correctly represent identity and license; local verification accurately describes source completeness.
- `Constraints`: no source redistribution, no local-path publication, no execution of untrusted generated code, and no inference that Docker alone provides a complete security boundary.
- `Out of scope`: a current model leaderboard, independent reproduction, license audit of the 12 repositories, exploit generation, production deployment, and claims about languages or frameworks outside Python/pytest.
- `Intended use`: research review, benchmark-design critique, safe MVP planning, evaluation-governance design, and follow-on replication planning.
- `Audience`: software-engineering researchers, coding-agent evaluators, benchmark maintainers, and developers building isolated test-generation systems.
- `Reproducibility boundary`: the paper is fully inspectable, but a runnable benchmark package was not established. A replication must reconstruct or locate the exact repository snapshots, prompts, containers, model versions, and evaluation scripts.
- `Data sensitivity`: the paper and repository names are public; source documents remain local. Any future enterprise use should treat target repositories and generated tests as potentially proprietary and security-sensitive.

## Observations

- `Observed pattern`: context utility is non-monotonic. Relevant evidence can help at 8k or 32k and still hurt at 16k or 64k, depending on model and task.
- `Observed pattern`: constraint satisfaction is the real bottleneck. Task III execution exceeds success for every reported model, showing that syntactic validity and runnable code do not imply coverage compliance.
- `Observed pattern`: the benchmark's strongest “oracle” is still lossy. File-level coverage ranking identifies likely evidence, but random selection within a tier and whole-file inclusion can waste budget.
- `Contradiction or tension`: the paper calls the pipeline scalable while reporting that only 25 of 42 repositories configured automatically, only 12 were retained, and 11 required manual folder mapping.
- `Contradiction or tension`: Table 4 reports Claude RER values of 72.4% and 75.4%, while the narrative reports 72.6% and 75.6%.
- `Technical implication`: evaluation harnesses should emit separate parse, execution, assertion-quality, target-use, and coverage-compliance outcomes rather than one pass/fail score.
- `Technical implication`: context selection should be evaluated as a policy with its own recall, budget, dependency, and failure metrics, not as an invisible preprocessing step.
- `Open question`: how much of the long-context collapse comes from model reasoning, tokenization, serving configuration, prompt formatting, or repository-specific distribution shift?
- `Reviewer hypothesis`: replacing oracle whole-file selection with dependency-aware code slices and retained coverage lineage could preserve the signal while reducing distractor tokens.

## Considerations

- `Security`: model-generated tests are executable code. Run them without credentials, with read-only source mounts where practical, explicit CPU/memory/time limits, blocked network access, and disposable state.
- `Measurement validity`: line coverage is necessary for CLOVER's Task III but not sufficient for semantic correctness, fault detection, mutation adequacy, or maintainability.
- `Repository contamination`: generated tests may mutate caches, snapshots, fixtures, or the worktree. Restoration must be verified, not assumed.
- `Dependency drift`: recreating 12 historical Python environments can fail because package indexes, submodules, compilers, or system dependencies change.
- `Cost`: full-repository context and multi-length model sweeps are expensive. Token, wall-clock, and sandbox-reset costs should be reported alongside accuracy.
- `Fairness of comparison`: model window size, tokenizer choice, vLLM compatibility, decoding parameters, and output budgets must be held or disclosed consistently.
- `Governance`: benchmark maintainers should version repository snapshots, prompt templates, evaluator rules, accepted equivalences, and known flaky cases.
- `Legal`: permissive repository licenses do not automatically settle redistribution of derived prompts, test fixtures, transitive assets, or generated outputs.
- `Maintenance`: a live benchmark needs continuous checks for broken environments, newly flaky tests, security advisories, and changes in model-provider behavior.

## Strengths

1. `Executable grounding`: generated tests are run in repository environments, moving beyond text similarity.
2. `Requirement-aware tasks`: Tasks II and III test target use and coverage, not only compilability.
3. `Context diagnosis`: the problem-only/contextual grid reveals whether more context actually helps.
4. `Coverage-calibrated oracle`: regular-versus-empty and peer-unique traces give a principled basis for ranking evidence.
5. `Metric separation`: EM, ER, RER, success rate, and execution rate expose different failure modes.
6. `Transparent limitations`: the paper names Python/pytest scope, agent cost, sandbox memory risk, and environment-construction failures.
7. `Useful appendices`: repository lists, exclusions, prompt templates, and alternate result tables support inspection.

## Weaknesses

1. `No established release artifact`: the promised code/data/container package was not located, preventing direct reproduction.
2. `Narrow ecosystem`: twelve Python repositories and pytest-specific tooling do not establish transfer to JavaScript, Java, mobile, distributed, or data-intensive systems.
3. `Oracle-production gap`: context ranking depends on the original test's coverage, which is unavailable when generating a genuinely new test.
4. `Heuristic selection`: AST rules, file-layout assumptions, manual folder mapping, and random within-tier context selection may introduce hidden bias.
5. `Coverage proxy`: line/block coverage can reward shallow execution without strong assertions or defect revelation.
6. `Dated model snapshot`: the study compares 2024-era model and serving configurations; it should not be treated as a 2026 ranking.
7. `Limited uncertainty analysis`: the main tables do not foreground repeated-run variance, statistical testing, or per-repository confidence intervals.
8. `Potential table/prose mismatch`: the Claude Task I contextual numbers differ by 0.2 percentage points between Table 4 and prose.
9. `Sandbox caveat`: Dockerized execution can still exhaust host resources; the threat model is incomplete for hostile generated code.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish a versioned artifact manifest | Reproducibility | Pin repository SHAs, containers, prompts, model snapshots, evaluator hashes, and licenses | Makes reported tables auditable and repeatable | Storage and maintenance burden | Rebuild from a clean host and reproduce a checksum-bound smoke subset |
| Replace whole-file oracle context with dependency slices | Context quality | Coverage identifies relevance but whole files contain distractors | Higher evidence density and lower token cost | Slicing may remove dynamic dependencies | Compare recall of required symbols and success/token curves against the current oracle |
| Report multi-run uncertainty by repository | Evaluation | Model generation and sandbox behavior are stochastic | Distinguishes real gains from noise and repository effects | Increased inference cost | Stratified bootstrap, paired tests, and per-repository effect plots |
| Add mutation and fault-revelation outcomes | Measurement validity | Coverage alone does not prove test quality | Better alignment with useful tests | Mutation runs are expensive and can be flaky | Mutation score, seeded-defect detection, and assertion-strength audits |
| Harden execution isolation | Safety | Docker alone does not bound all resource or kernel risks | Safer benchmark operation | More complex infrastructure | Network-denied microVM/container comparison with CPU, memory, process, and filesystem caps |
| Maintain a living environment-health ledger | Operations | Historical dependencies and tests decay | Separates model failure from harness failure | Ongoing triage | Scheduled clean rebuilds, flaky-test detection, and signed status reports |
| Audit semantic equivalence in RER | Evaluator correctness | Execution can accept shortcuts that violate intent | More reliable Task I scoring | Requires oracle design and manual adjudication | Curated equivalence set plus adversarial trivial-assertion tests |

## Potential Implementations

1. `CLOVER-Lite evaluator`
   - `User`: coding-model and agent teams.
   - `Goal`: compare whether generated tests parse, execute, invoke required targets, and satisfy coverage constraints.
   - `Core mechanism`: immutable task manifests, disposable sandboxes, structured evaluator outcomes, and a public-safe result ledger.
   - `Required inputs`: licensed repository snapshot, test skeleton, target specification, coverage blocks, generated test, and resource policy.
   - `Outputs`: parse/execution/target/coverage status, logs, coverage delta, token count, and reproducibility receipt.
   - `Risk controls`: no credentials, network disabled, read-only source, bounded resources, output redaction, and repository reset verification.
   - `Evaluation`: deterministic smoke corpus plus repeated model trials.

2. `Context-utilization profiler`
   - `User`: model and retrieval engineers.
   - `Goal`: measure whether longer or differently selected code context improves requirement satisfaction.
   - `Core mechanism`: generate fixed-budget evidence packs using coverage, static dependencies, and recency baselines; compare them against problem-only input.
   - `Required inputs`: task manifest, code graph, coverage traces where authorized, tokenizer, and model runner.
   - `Outputs`: best/worst context delta, token-normalized success, missing-evidence traces, and context-collapse alerts.
   - `Risk controls`: local-only proprietary code handling, fixed budgets, no automatic code execution outside the sandbox.
   - `Evaluation`: paired runs across context policies and model snapshots.

3. `Coverage-to-dependency retrieval service`
   - `User`: repository-scale coding agents.
   - `Goal`: return a small, traceable set of code slices relevant to a requested test target.
   - `Core mechanism`: combine historical coverage edges, static call/import relations, failed-test lineage, and explicit target constraints.
   - `Required inputs`: repository index, dependency graph, permitted test traces, target symbol, and token budget.
   - `Outputs`: ranked evidence nodes with provenance and exclusion reasons.
   - `Risk controls`: denylisted paths, secret scanning, access-control inheritance, and no source export beyond the authorized workspace.
   - `Evaluation`: required-symbol recall, dependency completeness, downstream test success, and tokens consumed.

## Three Ways to Exercise This Research

1. `Synthetic micro-repository replay`: Build a small, fully synthetic Python package with known branches and tests; implement regular-versus-empty coverage ranking; compare problem-only, random-file, and ranked-context prompts. Output a result matrix. Success means the evaluator distinguishes execution from target and coverage compliance. Stop if the sandbox cannot enforce resource and network bounds.
2. `Context-length stress curve`: Use a fixed safe task and inject increasingly large benign distractor modules at 4k, 8k, 16k, and 32k. Record success, malformed-output rate, tokens, and latency. Success means the run reveals whether failure is monotonic, model-specific, or retrieval-specific. Stop before external/private code or uncontrolled inference cost is introduced.
3. `Evaluator contract audit`: Create hand-written candidate tests covering valid alternatives, trivial assertions, target omission, partial block coverage, timeouts, and workspace mutation. Output a signed pass/fail expectation table. Success means every failure class maps to a distinct evaluator outcome. Stop if any candidate can access credentials, the network, or host-write paths.

## Example MVP Product

- `Product name`: CLOVER-Lite Audit.
- `Target user`: a coding-agent team evaluating a new model or retrieval policy before repository deployment.
- `Problem`: current test-generation demos often conflate runnable code with useful, requirement-satisfying tests and hide context-selection failures.
- `Core workflow`: import a versioned synthetic or authorized repository task; build one or more bounded context packs; request a generated test; run it in a disposable sandbox; report parse, execution, target-use, coverage, resource, and context-utilization outcomes separately.
- `Data requirements`: immutable repository snapshot, task manifest, approved source visibility, target symbol or coverage blocks, tokenizer, and expected evaluator outcome. Synthetic repositories are the default.
- `Architecture`: CLI orchestrator -> manifest validator -> context builder -> model adapter -> network-denied sandbox -> pytest/coverage evaluator -> public-safe result ledger.
- `Success metrics`: zero host mutations; 100% evaluator agreement on the smoke corpus; reproducible receipts; per-task token/latency bounds; and distinct parse/execution/requirement/coverage outcomes.
- `Risk controls`: no secrets, no default network, read-only source mount, disposable writable layer, CPU/memory/process/time limits, dependency allowlist, output-size cap, and manual approval before using private repositories.
- `Limitations`: not a CLOVER reproduction; synthetic tasks may underrepresent repository complexity; coverage remains an incomplete proxy; model-provider variance can affect results.
- `MVP boundary`: one language (Python), pytest only, synthetic/open licensed fixtures, three context policies, and no autonomous patch deployment.
- `Deployment model`: local CLI or isolated CI runner.
- `Evaluation plan`: deterministic unit tests for the manifest/evaluator, ten safe end-to-end smoke tasks, repeated model trials, and a sandbox escape/resource-abuse review.
- `Failure modes`: incomplete dependency context, flaky upstream tests, silent sandbox mutation, evaluator false positives, truncated model output, and leakage of private source in reports.
- `Maintenance plan`: pin container/tool versions, revalidate fixtures monthly, version evaluator semantics, and archive signed benchmark receipts.

## Related Research and Reading

### Exactly Three Related DEP Entries

| Related DEP entry | Concrete overlap | Source basis |
|---|---|---|
| [Smart Coverage Goals](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Smart%20Coverage%20Goals/smart_coverage_goals_manuscript.md) | Both treat coverage as a structured objective rather than a decorative metric. Smart Coverage Goals reduces redundant optimization goals in search-based testing; CLOVER uses peer-unique coverage to select requirements and rank context. | DEP review of https://arxiv.org/abs/2208.04096 and its ASE record |
| [TACO Terminal Context](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-TACO%20Terminal%20Context/2604.19572-whitepaper-review.md) | Both expose the tension between long observations and useful evidence in software-engineering tasks. TACO learns task-conditioned output filters; CLOVER measures whether models benefit from longer coverage-ranked code context. | DEP review of https://arxiv.org/abs/2604.19572v3 and https://github.com/multimodal-art-projection/TACO |
| [ContextWeaver Selective Context](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-ContextWeaver%20Selective%20a/2604.23069-whitepaper-review.md) | Both preserve task-relevant code/test evidence under a fixed window. ContextWeaver adds dependency edges, validation status, and supersession—mechanisms CLOVER's file-tier oracle does not model. | DEP review of https://arxiv.org/abs/2604.23069v1 |

### Primary and Near-Primary Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| TestGenEval | Related benchmark | Real-world unit-test generation/completion with shorter context ceilings | https://arxiv.org/abs/2410.00752 |
| TestBench | Related benchmark | Class-level Java test generation and context variants | https://arxiv.org/abs/2409.17561 |
| SWE-bench | Related executable benchmark | Repository issue resolution and executable evaluation substrate | https://openreview.net/forum?id=VTF8yNQM66 |
| SUPER | Agent evaluation | Evaluates agents on setting up and executing research repositories | https://arxiv.org/abs/2409.07440 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2502.08806 | Canonical identity, authors, date, subjects, DOI, license, and source locators | 2026-07-19 | Metadata only for empirical purposes |
| R2 | https://arxiv.org/pdf/2502.08806 | Full paper, tables, figures, appendices, limitations, safety | 2026-07-19 | Public equivalent of the verified local PDF; not redistributed |
| R3 | https://arxiv.org/html/2502.08806 | Searchable full paper and table cross-check | 2026-07-19 | Verified full document, not abstract-only HTML |
| R4 | https://arxiv.org/e-print/2502.08806 | TeX tables, prompts, bibliography, and paper-source structure | 2026-07-19 | Inspected locally; source package withheld |
| R5 | https://doi.org/10.48550/arXiv.2502.08806 | Persistent arXiv DOI | 2026-07-19 | DataCite-issued arXiv DOI |
| R6 | https://openreview.net/forum?id=gPpQa4PGEZ | DL4C @ ICLR 2025 venue, dates, track, license | 2026-07-19 | Official venue record |
| R7 | https://jiacheng-xu.github.io/ | Author-maintained publication context | 2026-07-19 | Used for identity/context, not results |
| R8 | https://huggingface.co/papers/2502.08806 | Discovery-only release cross-check | 2026-07-19 | No linked model or dataset observed; secondary platform |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public artifact and source-locality rules | 2026-07-19 | Fetched live |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication-index rules | 2026-07-19 | Fetched live |
| R11 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related-repository authority | 2026-07-19 | Fetched live before reliance |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Smart%20Coverage%20Goals/smart_coverage_goals_manuscript.md | Related coverage-objective DEP | 2026-07-19 | Exactly one of three related DEP entries |
| R13 | https://arxiv.org/abs/2208.04096 | Primary source named by Smart Coverage Goals DEP | 2026-07-19 | Related-entry source basis, not re-reviewed in full here |
| R14 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-TACO%20Terminal%20Context/2604.19572-whitepaper-review.md | Related context-filtering DEP | 2026-07-19 | Exactly one of three related DEP entries |
| R15 | https://arxiv.org/abs/2604.19572v3 | Primary source named by TACO DEP | 2026-07-19 | Related-entry source basis |
| R16 | https://github.com/multimodal-art-projection/TACO | Official implementation named by TACO DEP | 2026-07-19 | Contextual reading; not executed here |
| R17 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-ContextWeaver%20Selective%20a/2604.23069-whitepaper-review.md | Related dependency-memory DEP | 2026-07-19 | Exactly one of three related DEP entries |
| R18 | https://arxiv.org/abs/2604.23069v1 | Primary source named by ContextWeaver DEP | 2026-07-19 | Related-entry source basis |
| R19 | https://arxiv.org/abs/2410.00752 | TestGenEval related benchmark | 2026-07-19 | Primary paper locator |
| R20 | https://arxiv.org/abs/2409.17561 | TestBench related benchmark | 2026-07-19 | Primary paper locator |
| R21 | https://openreview.net/forum?id=VTF8yNQM66 | SWE-bench official venue record | 2026-07-19 | Primary/official context |
| R22 | https://arxiv.org/abs/2409.07440 | SUPER agent-evaluation paper | 2026-07-19 | Primary paper locator |

## Appendix

### Selection and Dedup Receipt

- Random method: `rg --files -g "*.pdf"` enumeration, unique parent units, used-ID exclusion, and uniform PowerShell `Get-Random` selection.
- PDF candidates: 75,778.
- Parent units: 75,776.
- Used arXiv IDs: 810.
- Excluded by used ID: 192.
- Identifier-incomplete units withheld: 185.
- Eligible units: 75,399.
- Selected zero-based eligible index: 33,124.
- Selected identifier: arXiv:2502.08806v1.
- Duplicate reselections: 0.
- Dedup scan: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`; automation memory; Black-Lake-Data `.lake-data` and `.reports`.
- Matching keys: arXiv ID, DOI, exact/normalized title, and slug.
- Public-safe 24-hour cutoff: 2026-07-18.
- Result: no prior or recent same-paper marker.

### Local Source-Integrity Receipt

- Initial classification: partial because full-paper HTML was missing.
- Preserved PDF: 827,506 bytes; size, `%PDF-` header, and trailing `%%EOF` checks passed.
- Repaired full-paper HTML: official arXiv HTML, 526,611 bytes; 88,981 body characters; full-document marker; 55 headings/sections; seven paper-structure terms.
- Metadata HTML: 42,490 bytes; metadata-only role.
- Source package: 330,636 bytes; retained locally.
- Partial files after repair: zero.
- Final classification: complete.
- Local records updated: README, attribution/provenance note, CSV summary, JSON verification report.
- Publication gate: all original source files remain local and no `.source/` directory is created in the DEP.

### Replication Checklist

- Locate or reconstruct the official benchmark artifact and pin its commit/release.
- Record exact SHAs and licenses for the 12 repository snapshots at the 2024-08-30 cutoff.
- Rebuild Python 3.10 environments in an isolated, network-controlled runner.
- Recreate task manifests, prompts, coverage tensors, and context tier ordering.
- Pin tokenizer, vLLM, decoding parameters, model snapshots, output budgets, and API dates.
- Validate `verify`, `cov`, RER, target-use, and all-block coverage against an adversarial smoke suite.
- Reproduce a small deterministic subset before attempting the full two-hour-per-model grid.
- Report per-repository outcomes, repeated-run variance, token/latency cost, harness failures, and security incidents separately.
