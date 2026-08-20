---
title: "Smart Coverage Goals - DEP-E"
generated_at: "2026-07-17 (date only; exact run time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "A source-first review of smart selection for reducing redundant coverage objectives in search-based Java unit-test generation."
source_status: "Verified local PDF, full-paper HTML, metadata HTML, and TeX bundle withheld; public URLs cited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-17"
temporal_cutoff: "Sources available through 2026-07-17"
primary_url: "https://arxiv.org/abs/2208.04096"
stable_identifier: "arXiv:2208.04096v1; DOI:10.1145/3551349.3556902"
confidence_summary: "High for paper identity, mechanism, and reported tables; medium for generalization because experiments were not rerun."
safety_scope: "Non-sensitive software-testing research; synthetic or public-code examples only"
distribution_notes: "Original PDF, HTML, source archive, extracted text, and caches remain local and were not uploaded."
---

# Smart Coverage Goals - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | *Selectively Combining Multiple Coverage Goals in Search-Based Unit Test Generation* | Primary paper | Verified PDF, full-paper HTML, metadata HTML, TeX/source package | arXiv:2208.04096v1 | https://arxiv.org/abs/2208.04096 | arXiv record; local source files withheld from publication | 2026-07-17 | Complete paper inspected locally |
| S2 | Public PDF | Primary paper locator | PDF | arXiv:2208.04096v1 | https://arxiv.org/pdf/2208.04096 | Public equivalent of inspected PDF; not redistributed | 2026-07-17 | Inspected locally and structurally verified |
| S3 | ar5iv paper rendering | Primary paper fallback | Full-paper HTML | arXiv:2208.04096v1 | https://ar5iv.labs.arxiv.org/html/2208.04096 | Approved fallback after official `/html/` returned 404; not redistributed | 2026-07-17 | Inspected locally and structurally verified |
| S4 | arXiv source package | Primary paper source | TeX/source archive | arXiv:2208.04096v1 | https://arxiv.org/e-print/2208.04096 | Used locally to inspect sections, equations, tables, and figures; not redistributed | 2026-07-17 | 66 archive entries inspected |
| S5 | ASE 2022 research-paper record | Venue record | Conference program page | ASE 2022 research paper | https://conf.researchr.org/details/ase-2022/ase-2022-research-papers/14/Selectively-Combining-Multiple-Coverage-Goals-in-Search-Based-Unit-Test-Generation | Official venue metadata | 2026-07-17 | Inspected by URL |
| S6 | ACM DOI | Publisher locator | DOI record | 10.1145/3551349.3556902 | https://doi.org/10.1145/3551349.3556902 | Persistent publication identifier | 2026-07-17 | DOI and venue cross-checked |
| S7 | ASE 2022 artifact-evaluation record | Artifact context | Conference program page | Zenodo DOI 10.5281/zenodo.7026797 | https://conf.researchr.org/details/ase-2022/ase-2022-artifact-evaluation/7/Artifact-for-Selectively-Combining-Multiple-Coverage-Goals-in-Search-Based-Unit-Test | Official artifact-evaluation metadata; artifact not executed here | 2026-07-17 | Inspected by URL |
| S8 | Paper-cited online artifact | Artifact locator | DOI record | 10.5281/zenodo.6467640 | https://doi.org/10.5281/zenodo.6467640 | Cited in the TeX source; artifact not downloaded or executed | 2026-07-17 | Locator recorded |
| S9 | Yutian Tang publications | Author context | Publication list | Updated author list | https://chrisyttang.org/pages/publications.html | Confirms conference publication and later journal extension | 2026-07-17 | Inspected by URL |

- `Paper/work title`: *Selectively Combining Multiple Coverage Goals in Search-Based Unit Test Generation*.
- `Authors`: Zhichao Zhou; Yuming Zhou; Chunrong Fang; Zhenyu Chen; Yutian Tang.
- `Venue`: 37th IEEE/ACM International Conference on Automated Software Engineering (ASE 2022), article 91.
- `Submission date`: 2022-08-08; arXiv v1 is the inspected preprint version.
- `DOI`: https://doi.org/10.1145/3551349.3556902.
- `Artifact identifiers`: the paper source cites https://doi.org/10.5281/zenodo.6467640, while the official ASE artifact-evaluation page exposes https://doi.org/10.5281/zenodo.7026797. Both are preserved as distinct locators; neither artifact was executed in this review.
- `Local source file paths`: withheld by repository policy. No source file was copied into this DEP.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S4 | Primary paper bundle | Abstract, introduction, background, method, evaluation, discussion, conclusion, tables, TeX equations, and source inventory | Paper mechanism, experiment design, reported results, threats to validity | High | Results were read, not independently rerun |
| E2 | S1 | Official arXiv metadata | Title, authors, submission date, subject, abstract | Stable identity and version | High | Abstract alone does not establish empirical claims |
| E3 | S5-S6 | Official venue and publisher locators | ASE placement, authorship, DOI, conference abstract | Publication context | High | Publisher full text was not separately inspected |
| E4 | S7-S8 | Artifact records | Artifact-evaluation listing and two public DOI locators | Artifact availability and identifier discrepancy | Medium | Artifact contents and reproducibility were not tested |
| E5 | S9 | Author publication list | Conference citation and later *Coverage Goal Selector* journal extension | Research-line continuity | Medium | Author-maintained page is contextual, not independent validation |
| E6 | Selection and dedup record | Process evidence | Uniform eligible-index draw, repository/memory index, title/slug check, 24-hour marker check | Random selection and non-duplication | High | Coverage depends on parsed identifiers and current repository refs |
| E7 | Local verification report, withheld | Process evidence | PDF header/EOF, HTML body/structure checks, source-archive listing, no partial files | Complete-paper gate | High | Structural integrity does not prove semantic correctness |
| E8 | Black-Lake-Data SCATE entry | Related DEP evidence | Coverage-guided learned supervision for coding-agent test generation | Adaptive goal/action selection bridge | Medium | Related DEP summarizes a separate recent preprint |
| E9 | Black-Lake-Data SWE-Bench Pro audit entry | Related DEP evidence | Low-coverage, overly strict, and misleading tests as benchmark defects | Coverage adequacy and test-oracle governance bridge | Medium | Related DEP summarizes an official lab audit |
| E10 | Black-Lake-Data AgentCompass entry | Related DEP evidence | Benchmark/harness/environment separation and trajectory analysis | Reusable evaluation-infrastructure bridge | Medium | Related DEP summarizes a separate preprint |

## Executive Summary

The paper addresses a practical failure mode in search-based software testing (SBST): combining eight coverage criteria gives a generator a broader definition of test quality, but it also increases and roughens the optimization space. The authors' `smart selection` method reduces that objective set while trying to preserve the properties expressed by the omitted goals. It clusters correlated criteria, chooses representatives with more useful fitness gradients, and retains subsuming goal subsets for unselected criteria.

The evaluation covers 400 Java classes, three EvoSuite genetic algorithms, ten criterion configurations, 30 repetitions per configuration, and a two-minute search budget per run. The authors report that smart selection most clearly improves the original all-goal combination for Whole Suite Generation (WS) and for classes with at least 200 branches. MOSA shows smaller but still concentrated gains on larger classes. DynaMOSA, which already activates goals according to dependency structure, shows slight differences and can favor the original combination on smaller classes. Averaged across the three algorithms, smart selection wins on 77 classes, or 65.1% of classes with significant differences; this is an author-reported aggregate, not an independently reproduced result [E1].

Reviewer interpretation: the paper is strongest as an auditable objective-budgeting pattern, not as proof that fewer goals are universally better. Its own RQ4 ablation shows that removing the subsumption strategy can improve several criteria while hurting weak mutation or top-level method coverage. The method therefore exposes a Pareto problem among search guidance, property preservation, suite size, and criterion-specific coverage. Confidence is high in the description of the source and tables, but medium in transfer to current projects, languages, or EvoSuite versions because the artifact and experiments were not run [E1, E4].

## Detailed Summary

### Problem and Background

SBST turns test generation into optimization. A coverage criterion supplies goals, and each goal supplies a fitness function that estimates whether or how closely a candidate test covers it. EvoSuite integrates several genetic algorithms: WS sums goal fitness into a suite-level objective; MOSA treats individual goals as many objectives; DynaMOSA activates goals according to control dependencies.

Using only one criterion can miss useful test-suite properties, so prior work combines multiple criteria. The paper studies eight EvoSuite defaults: branch coverage (BC), direct branch coverage (DBC), line coverage (LC), weak mutation (WM), top-level method coverage (TMC), no-exception top-level method coverage (NTMC), exception coverage (EC), and output coverage (OC). The original combination exposes all goals to the search. The authors argue that this enlarges the search space and adds discontinuous or weakly monotonic fitness signals, diluting progress on individual criteria.

### Smart-Selection Mechanism

The mechanism has three stages.

1. `Group by coverage correlation`: four groups are formed: `{BC, DBC, LC, WM}`, `{TMC, NTMC}`, `{EC}`, and `{OC}`. The grouping uses prior empirical correlation, definitional relationships, and a paper-derived approximation relating branch and line coverage.
2. `Choose representative criteria`: DBC represents the first group, NTMC the second, and EC and OC represent themselves. DBC and NTMC are chosen because they impose the corresponding BC/TMC property plus an additional direct-call or no-exception requirement. The paper also argues that branch-derived fitness has smoother guidance than definition-only line or mutation fitness.
3. `Preserve omitted properties through subsumption`: BC and TMC need no extra goals because DBC and NTMC goals subsume them. For LC, the last line of each basic block represents preceding lines, but blocks shorter than `lineThreshold=8` are skipped. For WM, the selector narrows EvoSuite's mutation operators, removes unary-operator insertion as effectively line-equivalent, and uses static subsumption results for arithmetic- and relational-operator mutants.

The output is a smaller set of fitness functions combining the four representative criteria with selected LC and WM goal subsets. This set replaces the original all-goal combination at the objective-construction point in EvoSuite.

### Experimental Design

The subject set contains 400 Java classes: 158 from the DynaMOSA benchmark and 242 randomly selected from Hadoop, with at least 50 branches per class. The paper distinguishes 315 smaller classes from 85 classes with at least 200 branches. Experiments use EvoSuite defaults plus `lineThreshold=8`.

For each class and genetic algorithm, the study runs ten approaches: smart selection, the original eight-criterion combination, and eight constituent-criterion configurations. EC and OC constituent runs are paired with branch coverage because the authors consider them weak guides alone. Each approach receives 30 runs and a two-minute search budget. The comparison between smart selection and the original combination uses a Mann-Whitney U test with `p < 0.05` and Vargha-Delaney effect direction (`A > 0.5`).

### Reported Results

| Algorithm / stratum | Smart selection wins | Original combination wins | No significant difference | Interpretation |
|---|---:|---:|---:|---|
| WS, all 400 classes | 121 (30.3%) | 20 (4.9%) | 259 (64.8%) | Strongest overall evidence for smart selection |
| WS, 85 large classes | 50 (59.1%) | 1 (1.3%) | 34 (39.6%) | Benefit concentrates in larger objective sets |
| MOSA, all 400 classes | 78 (19.5%) | 42 (10.4%) | 280 (70.1%) | Smaller aggregate advantage |
| MOSA, 85 large classes | 35 (40.9%) | 5 (5.6%) | 46 (53.5%) | Clearer on larger classes |
| DynaMOSA, all 400 classes | 32 (8.1%) | 40 (10.1%) | 328 (81.8%) | Differences are slight; original combination wins more often overall |
| DynaMOSA, 85 large classes | 16 (18.7%) | 6 (7.5%) | 63 (73.8%) | Smart selection regains a modest large-class edge |

For WS across all classes, smart selection reports higher average values than the original combination on all eight criteria, including BC `55%` versus `53%`, LC `60%` versus `58%`, and DBC `55%` versus `53%`. The mean suite size rises from `47.77` tests for the original combination to `51.35` for smart selection. On large WS classes, the BC gap is `45%` versus `41%`, while suite size rises from `89.95` to `103.53`.

For MOSA, gains are smaller on all classes and stronger on large classes. On large classes, smart selection reports BC `49%` versus `46%`, WM `52%` versus `49%`, and exception count `30.54` versus `27.53`; mean suite size rises from `112.38` to `126.56`.

For DynaMOSA, most average coverage values are equal or separated by one point. The authors attribute this to DynaMOSA's own dependency-based goal activation, which already limits active objectives. Mean suite sizes are also close: `61.13` for smart selection and `60.59` for the original combination across all classes.

RQ4 compares smart selection with and without the LC/WM subsumption strategy on 173 eligible classes. Removing the subsumption additions slightly improves many WS criteria and some MOSA/DynaMOSA criteria, while smart selection retains advantages for weak mutation and top-level method coverage. This is important negative evidence: the property-preservation layer changes the objective balance rather than dominating every metric.

### Threats and Research-Line Context

The authors identify external-validity risk from older DynaMOSA benchmark classes and partly address it with 242 Hadoop classes. They identify stochastic internal-validity risk and repeat every configuration 30 times. The paper does not establish transfer to other languages, modern build ecosystems, current EvoSuite releases, or industrial defect detection. The two-minute budget and class-level analysis also leave cost normalization and project-level interactions open.

The author publication list shows a 2024 IEEE TSE extension titled *Coverage Goal Selector for Combining Multiple Criteria in Search-Based Unit Test Generation*. That later work is relevant follow-up reading, but this artifact does not import its claims into the 2022 paper without a separate full review.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Combining all eight criteria can reduce criterion-specific coverage by increasing and roughening the optimization space. | Author claim with motivating measurements | E1 | Mechanistically plausible and supported by source comparisons, but causal attribution is not isolated from every implementation detail. | Medium |
| C2 | Smart selection preserves criterion properties while reducing goals through correlation, representative selection, and subsumption. | Author method claim | E1 | The rule set is explicit and inspectable; “preserves” should mean the paper's selected subsumption assumptions, not semantic equivalence for every test objective. | High for implementation description; medium for completeness |
| C3 | With WS, smart selection outperforms the original combination, especially on classes with at least 200 branches. | Author empirical claim | E1 | Strongest reported result: 50 versus 1 average significant wins on 85 large classes, with larger suites as a cost. | High for source reporting; medium for external validity |
| C4 | With MOSA, smart selection has a slight overall advantage and a clearer large-class advantage. | Author empirical claim | E1 | Reported direction is consistent with objective-count pressure, though most classes show no significant difference. | High for source reporting; medium for generalization |
| C5 | DynaMOSA reduces the benefit because it already controls active goals through dependencies. | Author explanation | E1 | Results are consistent with the explanation, but the study does not isolate dependency activation as the sole cause. | Medium |
| C6 | Averaged across algorithms, smart selection wins on 77 classes, 65.1% of significant cases. | Author aggregate claim | E1, E3 | Correctly preserved from the paper and ASE page; it hides the algorithm-specific reversal for all-class DynaMOSA and should not stand alone. | High |
| C7 | Smart selection is best understood as auditable objective budgeting rather than universal objective reduction. | Reviewer interpretation | E1, E8-E10 | Supported by algorithm/size stratification, RQ4 tradeoffs, and related work on adaptive testing and evaluation governance. | High |

## Methodology

- `Research objective`: preserve a source-grounded account of the paper's mechanism, evidence, limitations, and implementation relevance while validating random selection, deduplication, and local source completeness.
- `Sources inspected`: verified complete PDF, full-paper HTML fallback, metadata HTML, TeX/source package, arXiv record, ASE research-paper page, ACM DOI, ASE artifact-evaluation page, two artifact DOI locators, author publication list, live repository READMEs, and three related DEP entries.
- `Discovery strategy`: enumerated local PDFs with `rg --files -g "*.pdf"`; grouped by parent directory; parsed arXiv IDs; built a cross-repository and memory used-paper index; performed a uniform PowerShell `Get-Random` draw over eligible units; inspected primary paper sections and tables from TeX/full HTML; then searched repository corpora for concrete conceptual overlap.
- `Inclusion criteria`: sources had to establish paper identity, directly support method/results claims, document artifact or venue status, define repository rules, prove source integrity, or provide a verified related-DEP bridge.
- `Exclusion criteria`: abstract-only evidence was excluded from empirical support; unverified search snippets, unrelated generic “coverage” mentions, local file paths, and original source files were excluded from publication.
- `Analytical approach`: empirical, conceptual, comparative, implementation, replication, product-research, and evaluation-governance analysis.
- `Evidence handling`: author claims are labeled; quantitative results are tied to paper tables/sections; reviewer interpretations are separated; related DEP claims remain summaries of their own sources.
- `Uncertainty handling`: no claim of reproduction is made; artifact contents were not executed; the two public artifact DOI locators are recorded as a discrepancy rather than silently collapsed.
- `Extraction process`: TeX sections and table source were inspected directly; PDF and HTML passed structural verification; URLs and metadata were cross-checked against official records.
- `Version control`: arXiv v1 and the public source locators were pinned. Repository rules and related entries were read from live default-branch refs.
- `Random selection`: 75,777 PDF candidates collapsed to 75,776 parent units. The used index contained 720 arXiv IDs; 178 units were excluded by used ID and 185 identifier-incomplete units were withheld, leaving 75,413 eligible units. The uniform zero-based selected index was 74,157; duplicate reselections were zero.
- `Dedup and recency validation`: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and Black-Lake-Data `.lake-data`/`.reports` were scanned by ID, DOI, normalized title, and slug. No exact match was found. No same-paper or same-unit marker dated on or after the public-safe 2026-07-16 cutoff was found.
- `Source-integrity handling`: the unit was initially partial because full-paper HTML was missing. A valid PDF was preserved; the official arXiv HTML endpoint returned 404; an approved ar5iv full-paper fallback, metadata HTML, and source package were collected with bounded attempts. The unit then passed the complete-paper gate.

## Scope, Constraints, and Assumptions

- `Scope`: the 2022 smart-selection paper, its reported experiments, artifact locators, three related DEP bridges, and safe implementation translation.
- `Temporal boundary`: public records and repository state inspected through 2026-07-17.
- `Evidence limits`: the artifact package, EvoSuite implementation, raw results, and statistical scripts were not executed; publisher full text was not separately inspected; later journal-extension claims were not imported.
- `Assumptions`: TeX tables correspond to the archived arXiv v1 PDF; ASE and DOI records correctly identify the conference publication; public related DEP paths remain stable.
- `Constraints`: source files must remain local; exact local paths, machine identity, timezone label, and execution timestamp are withheld; repository output is Markdown-only.
- `Out of scope`: re-running 400-class experiments, judging current state of the art, validating industrial defect detection, or assessing the full 2024 journal extension.
- `Intended use`: DEP deposition, research review, replication planning, coverage-goal selector design, and evaluation-governance discussion.
- `Audience`: software-testing researchers, SBST engineers, CI platform developers, coding-agent evaluators, and artifact reviewers.
- `Depth target`: schema-complete manuscript with enough method and table detail for a follow-on replication plan.
- `Reproducibility boundary`: identities, source structure, equations, and reported values are traceable; empirical results remain source-reported until the artifact is run.
- `Data sensitivity`: public research sources; no private code or user data is required for the proposed exercises.

## Observations

- `Observed pattern`: gains scale with problem size. WS and MOSA show clearer advantages on the 85 classes with at least 200 branches, matching the hypothesis that redundant objectives hurt more when goal counts grow.
- `Observed pattern`: objective reduction has a suite-size cost. Better reported coverage often accompanies more generated tests, so coverage and maintenance burden should be evaluated together.
- `Contradiction or tension`: the aggregate 65.1% headline obscures DynaMOSA's all-class result, where the original combination wins on more classes than smart selection, although most cases are not significant.
- `Contradiction or tension`: the subsumption layer is justified as property preservation, yet removing it improves several criterion averages. Preservation and search effectiveness form a tradeoff, not a monotonic improvement.
- `Technical implication`: selector evaluation should report per-criterion coverage, suite size, runtime or fitness evaluations, and project complexity, not only one aggregate win rate.
- `Open question`: coverage correlations derived from prior studies and assumptions may drift across languages, bytecode transformations, mutation operators, and generator versions.
- `Reviewer hypothesis`: an adaptive selector could learn which goals are redundant for a particular class, but only if it emits an auditable explanation of retained and omitted properties.
- `Cross-DEP pattern`: SCATE adapts which testing action receives supervision, the SWE-Bench Pro audit challenges whether tests measure the intended task, and AgentCompass separates benchmark, harness, and environment. Together they extend smart selection from goal reduction to governed evaluation pipelines.

## Considerations

Adoption requires an explicit semantics contract. A selector that drops goals can make a search faster while silently narrowing the property set. Every configuration should therefore emit the input criteria, grouping evidence, representative rule, retained goal counts, omitted goal counts, subsumption rationale, and any threshold values.

Cost accounting must be matched. The paper uses equal wall-clock search budgets but reports larger suites for smart selection. A production comparison should also normalize fitness evaluations, CPU time, memory, flaky-test rate, compile time, and post-generation minimization cost. Otherwise a coverage increase may be purchased with maintenance debt.

Statistical governance matters because there are many classes, criteria, and algorithm comparisons. Replication should preserve per-class seeds, confidence intervals, effect sizes, multiple-comparison policy, and raw result hashes. The reported Mann-Whitney/Vargha-Delaney approach is useful, but a release decision should not reduce all strata to one win percentage.

For coding agents, coverage is neither correctness nor oracle quality. SCATE shows how coverage can guide supervision, while the SWE-Bench Pro audit shows that low-coverage or overly strict tests can invalidate evaluation. An adaptive generator should combine coverage goals with oracle review, mutation adequacy, regression relevance, and benchmark-integrity checks. AgentCompass suggests a modular boundary between task definitions, execution harnesses, and environments so selector effects can be diagnosed rather than confounded.

## Strengths

1. `Mechanism is inspectable`: grouping, representative selection, and subsumption are specified in enough detail to audit why each criterion or goal remains.
2. `Evaluation is stratified`: WS, MOSA, and DynaMOSA respond differently, and large versus small classes expose where the hypothesis is strongest.
3. `Repeated experiments`: 30 runs per class/configuration address stochastic SBST variance better than a single-run comparison.
4. `Negative evidence is visible`: DynaMOSA and RQ4 prevent a simplistic universal-win conclusion.
5. `Artifact context exists`: the ASE artifact-evaluation record and public artifact locators support a future reproduction attempt, even though this review did not execute them.

## Weaknesses

1. `External validity`: 158 classes come from an older benchmark, while the 242 Hadoop classes do not establish language, ecosystem, or project diversity.
2. `Budget sensitivity`: two minutes per run may favor particular objective constructions; equal wall-clock does not equal equal search work.
3. `Threshold generality`: `lineThreshold=8` is justified from benchmark basic-block statistics rather than tuned or validated across broad projects.
4. `Correlation assumptions`: some grouping decisions rely on prior correlations or analytical approximations that may not preserve the same relationship in every class.
5. `Property-preservation ambiguity`: goal subsumption is structural, but developer-perceived fault relevance and oracle strength may not follow structural coverage.
6. `Reproduction gap`: the public artifact was not run here, and the two artifact DOI locators require reconciliation during replication.
7. `Outcome boundary`: coverage and suite size are emphasized more than real fault detection, flaky behavior, readability, build integration, or maintenance cost.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Reproduce on current EvoSuite and recent Java projects | External validity | Tool and project structure have evolved | Establish present-day effect size | Environment and dependency effort | Pinned containers, project-level splits, repeated seeds |
| Equalize multiple budgets | Experimental design | Wall-clock alone hides fitness-evaluation and suite-size costs | Fairer efficiency comparison | More experimental cells | Compare equal time, evaluations, generated tests, and minimized tests |
| Learn correlation per class with a fallback | Goal grouping | Static groups may not hold everywhere | Better local adaptation | Instability and opacity | Holdout coverage, calibration, and deterministic fallback tests |
| Emit selector receipts | Auditability | Omitted goals need traceable rationale | Safer CI and easier review | Metadata volume | Schema validation and replay equality |
| Add mutation/fault outcomes | Practical validity | Coverage is an indirect proxy | Connect selector behavior to defect detection | Expensive fault suites | Defects4J, mutation score, and oracle-quality analysis |
| Evaluate threshold sensitivity | Hyperparameter robustness | `lineThreshold=8` is benchmark-derived | Identify safe ranges and failure strata | More runs | Sweep threshold by project/complexity with Pareto analysis |
| Separate selection from minimization | Suite cost | Smart selection often yields larger suites | Preserve coverage with manageable output | Minimizer can remove valuable diversity | Compare pre/post minimization coverage, mutants, and flakiness |

## Potential Implementations

### 1. EvoSuite Selector Receipt Plugin

- `User`: SBST researcher or CI engineer.
- `Goal`: apply smart-selection rules while producing a machine-reviewable receipt.
- `Core mechanism`: intercept goal construction, group criteria, select representatives and subsuming subsets, then record each decision.
- `Required inputs`: class bytecode, requested criteria, mutation operators, control-flow/basic-block metadata, threshold configuration.
- `Outputs`: selected fitness goals, omitted-goal rationale, counts, configuration hash, and generated test suite.
- `Risk controls`: deterministic mode, fail-closed behavior for unknown criteria, explicit no-drop mode, and source-free public receipts.
- `Evaluation`: replay equality, per-criterion coverage, mutation score, suite size, runtime, and omission audits.

### 2. Multi-Objective CI Test Budgeter

- `User`: repository maintainer with a constrained pull-request test budget.
- `Goal`: allocate test-generation effort across partially redundant quality goals.
- `Core mechanism`: estimate goal overlap from historical public CI metrics, retain mandated goals, and allocate remaining budget along a Pareto frontier.
- `Required inputs`: aggregate coverage/mutation history, module change graph, test runtime, and required policy goals.
- `Outputs`: signed test plan, retained/omitted goal list, expected cost, and rollback rule.
- `Risk controls`: never omit security or compliance tests automatically; no source-code upload; manual review for new modules or correlation drift.
- `Evaluation`: missed-regression rate, wall-clock, flakiness, coverage by stratum, and reviewer override rate.

### 3. Coverage-Guided Coding-Agent Supervisor

- `User`: coding-agent evaluation team.
- `Goal`: decide whether the agent should add a test, target a weak branch, strengthen an oracle, or stop.
- `Core mechanism`: combine smart-selection-style redundancy control with SCATE-like action selection and AgentCompass-style trajectory logging.
- `Required inputs`: public toy repository, current tests, coverage map, mutation outcomes, compiler/test diagnostics, and bounded action catalog.
- `Outputs`: next-action recommendation, evidence receipt, test patch candidate, and stop reason.
- `Risk controls`: isolated execution, no secrets, bounded test time, human approval before repository writes, and benchmark-integrity checks inspired by the SWE-Bench Pro audit.
- `Evaluation`: branch/line/mutation improvement per action, oracle review score, cost, false-stop rate, and deterministic trace replay.

## Three Ways to Exercise This Research

1. `Synthetic goal-reduction replay`: Objective—verify the grouping and subsumption logic without a large codebase. Inputs—a toy Java class with branches, short/long basic blocks, and arithmetic/comparison mutants. Method—enumerate all eight criteria, apply the selector, and compare retained-goal receipts with a hand-labeled expectation. Output—a Markdown/JSON goal map. Success criterion—every omitted goal has a documented representative or subsumer. Stop condition—any goal lacks a traceable preservation rationale.
2. `Matched-budget microbenchmark`: Objective—test whether the gain survives fairer cost accounting. Inputs—ten public Java classes, fixed seeds, WS/MOSA/DynaMOSA, and both smart/all-goal configurations. Method—run equal wall-clock and equal-fitness-evaluation budgets, then minimize suites. Output—a per-class Pareto table for coverage, mutation score, suite size, and time. Success criterion—results reconcile across repeated runs with confidence intervals. Stop condition—environment pinning, license, or deterministic seed capture fails.
3. `Agent-supervision simulator`: Objective—connect goal selection to a bounded coding-agent action policy. Inputs—a synthetic repository, precomputed coverage/mutation fixtures, and a four-action catalog. Method—compare exhaustive goals, static smart selection, and adaptive action selection without external writes. Output—trajectory receipts and coverage/oracle metrics. Success criterion—adaptive or static selection improves an approved metric without reducing mandated goals. Stop condition—the policy proposes unreviewed code execution or cannot explain an omitted goal.

## Example MVP Product

- `Product name`: GoalBudget Lab.
- `Target user`: software-testing researcher, CI platform engineer, or coding-agent evaluator.
- `Problem`: multi-criterion generators spend limited search budget on redundant or weakly guiding goals, while opaque pruning can hide lost properties.
- `Core workflow`: import a public or synthetic goal inventory; calculate group/subsumption candidates; require reviewer approval for protected goals; simulate selected versus all-goal budgets; export a receipt and comparison report.
- `Data requirements`: criterion names, goal IDs, basic-block/control dependencies, mutation-operator type, aggregate coverage observations, and optional public benchmark results. Raw proprietary source is not required for the MVP.
- `Architecture`: local-only CLI plus a static HTML report; deterministic selector core; pluggable correlation/subsumption rules; receipt schema; isolated experiment adapter.
- `Success metrics`: 100% omitted-goal rationale coverage, deterministic receipt hashes, zero protected-goal removals, matched-budget comparison completeness, and reviewer time to decision.
- `Risk controls`: local processing, no automatic repository writes, protected-goal allowlist, fail-closed unknown-rule handling, bounded subprocess time, and public-safe export scanning.
- `Limitations`: toy-scale rules do not establish production defect detection; correlations can drift; source-level instrumentation varies; receipt completeness does not guarantee semantic test quality.
- `MVP boundary`: no autonomous code modification, no private repository ingestion, no artifact reproduction at 400-class scale, and no claim of replacing expert test design.
- `Deployment model`: local CLI/notebook with optional static report viewer.
- `Evaluation plan`: golden goal maps, deterministic replay, known-subsumption fixtures, matched-budget smoke tests, and a deliberate correlation-drift failure case.
- `Failure modes`: invalid bytecode metadata, incorrect correlation assumptions, over-pruning, flaky generated tests, misleading aggregate coverage, or receipt/source mismatch.
- `Maintenance plan`: version rule packs, pin generator releases, record schema migrations, and revalidate protected-goal policies quarterly.

## Related Research and Reading

### Exactly Three Related DEP Entries

| Related DEP entry | Concrete overlap | Source basis |
|---|---|---|
| [SCATE finding](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260714-Tech%20Intel%201106/daily_research_findings_2026-07-14_1106.md) | Both allocate scarce test-generation effort using coverage signals. Smart selection prunes redundant fitness goals before search; SCATE learns which supervisory testing action to take next. | Related DEP item 7, based on https://arxiv.org/abs/2607.08983 |
| [SWE-Bench Pro audit finding](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260717-Tech%20Intel%200104/daily_research_findings_2026-07-17_0104.md) | Smart selection assumes coverage goals represent useful properties; the audit shows that low-coverage, overly strict, or misleading tests can invalidate the evaluation layer itself. | Related DEP item 2, based on https://openai.com/index/separating-signal-from-noise-coding-evaluations/ |
| [AgentCompass finding](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260716-Tech%20Intel%201303/daily_research_findings_2026-07-16_1303.md) | Both need clean separation between objectives and execution. AgentCompass's benchmark/harness/environment split and trajectory diagnostics provide an infrastructure pattern for isolating selector effects. | Related DEP item 3, based on https://arxiv.org/abs/2607.13705 |

### Primary and Near-Primary Follow-Up Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| *Coverage Goal Selector for Combining Multiple Criteria in Search-Based Unit Test Generation* | Later journal extension | Expanded research line listed by an author; requires a separate full review before importing claims | IEEE TSE 2024, volume 50(4), pages 854-883; author list at https://chrisyttang.org/pages/publications.html |
| EvoSuite | Official project | Implementation substrate for WS, MOSA, DynaMOSA, criteria, and generated Java tests | https://www.evosuite.org/ |
| ASE artifact evaluation | Official artifact record | Starting point for reproduction and identifier reconciliation | https://conf.researchr.org/details/ase-2022/ase-2022-artifact-evaluation/7/Artifact-for-Selectively-Combining-Multiple-Coverage-Goals-in-Search-Based-Unit-Test |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2208.04096 | Canonical identity, version, abstract, subjects | 2026-07-17 | Metadata only; not sufficient for empirical claims |
| R2 | https://arxiv.org/pdf/2208.04096 | Full primary paper | 2026-07-17 | Public equivalent of verified local PDF; not redistributed |
| R3 | https://ar5iv.labs.arxiv.org/html/2208.04096 | Full-paper HTML | 2026-07-17 | Approved fallback; official arXiv HTML returned 404 |
| R4 | https://arxiv.org/e-print/2208.04096 | TeX/source package | 2026-07-17 | Inspected locally; not redistributed |
| R5 | https://doi.org/10.1145/3551349.3556902 | Publisher/venue identity | 2026-07-17 | ASE 2022 article DOI |
| R6 | https://conf.researchr.org/details/ase-2022/ase-2022-research-papers/14/Selectively-Combining-Multiple-Coverage-Goals-in-Search-Based-Unit-Test-Generation | Official venue metadata and abstract | 2026-07-17 | Primary venue record |
| R7 | https://conf.researchr.org/details/ase-2022/ase-2022-artifact-evaluation/7/Artifact-for-Selectively-Combining-Multiple-Coverage-Goals-in-Search-Based-Unit-Test | Artifact-evaluation context | 2026-07-17 | Exposes DOI 10.5281/zenodo.7026797 |
| R8 | https://doi.org/10.5281/zenodo.6467640 | Paper-cited artifact locator | 2026-07-17 | Not downloaded or executed |
| R9 | https://doi.org/10.5281/zenodo.7026797 | ASE artifact-page locator | 2026-07-17 | Not downloaded or executed |
| R10 | https://chrisyttang.org/pages/publications.html | Conference citation and later journal extension | 2026-07-17 | Author-maintained context |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository deposition authority | 2026-07-17 | Live default-branch README inspected |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and index authority | 2026-07-17 | Live default-branch file inspected |
| R13 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion repository authority | 2026-07-17 | Read before related-entry reliance |
| R14 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260714-Tech%20Intel%201106/daily_research_findings_2026-07-14_1106.md | SCATE related DEP bridge | 2026-07-17 | Item 7; source basis R17 |
| R15 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260717-Tech%20Intel%200104/daily_research_findings_2026-07-17_0104.md | SWE-Bench Pro audit related DEP bridge | 2026-07-17 | Item 2; source basis R18 |
| R16 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260716-Tech%20Intel%201303/daily_research_findings_2026-07-16_1303.md | AgentCompass related DEP bridge | 2026-07-17 | Item 3; source basis R19 |
| R17 | https://arxiv.org/abs/2607.08983 | Primary source named by SCATE DEP entry | 2026-07-17 | Used as related-entry source basis, not fully reviewed here |
| R18 | https://openai.com/index/separating-signal-from-noise-coding-evaluations/ | Primary source named by SWE-Bench Pro audit DEP entry | 2026-07-17 | Used as related-entry source basis, not fully reviewed here |
| R19 | https://arxiv.org/abs/2607.13705 | Primary source named by AgentCompass DEP entry | 2026-07-17 | Used as related-entry source basis, not fully reviewed here |
| R20 | https://www.evosuite.org/ | Official implementation context | 2026-07-17 | Contextual reading only; current code was not inspected |

## Appendix

### Source-Integrity Record

- Classification before repair: `partial` because the PDF was valid but full-paper HTML was missing.
- PDF after verification: 1,208,175 bytes, `%PDF-` header, trailing `%%EOF`.
- Full-paper HTML after repair: 560,847 bytes, 87,878 body characters, document marker present, 56 heading/section markers, seven structure terms.
- Metadata HTML: 43,802 bytes; classified as metadata only.
- Source package: 3,839,205 bytes with 66 listed entries.
- Partial files after verification: zero.
- Classification after repair: `complete` / `verified-complete-paper`.
- Publication boundary: no PDF, HTML, source archive, extracted text, cache, or local path is included in the repository.

### Interpretation Guardrails

- “Win” counts are averages across criteria of per-class significant comparisons as presented by the authors; they are not raw counts of unique classes that win every criterion.
- Exception coverage is reported as average triggered exceptions because the total exception population is unknown.
- `p < 0.05` plus Vargha-Delaney direction identifies reported class/criterion differences; it does not by itself establish practical importance.
- Larger suites may explain part of the coverage gain and must remain visible in any deployment decision.
- The paper's results apply to the inspected arXiv v1 experiment description, not automatically to the later journal extension.
