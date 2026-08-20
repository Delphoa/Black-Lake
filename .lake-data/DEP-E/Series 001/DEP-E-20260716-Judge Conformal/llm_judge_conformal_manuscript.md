---
title: "Judge Conformal - DEP-E"
generated_at: "2026-07-16"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of interval-valued LLM judging with conformal prediction."
source_status: "complete local source bundle inspected; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "arXiv:2509.18658v1 and official code commit 6c5d8302999b028d460dd1a7b78d698c56f7b7b7"
primary_url: "https://arxiv.org/abs/2509.18658v1"
stable_identifier: "arXiv:2509.18658v1; DOI 10.48550/arXiv.2509.18658"
confidence_summary: "High for source identity, method transcription, and reported tables; medium for generality; low for independent reproducibility because experiments were not rerun."
safety_scope: "offline evaluation, calibration audit, and bounded product planning"
distribution_notes: "Original paper files and extraction caches remain local and are not redistributed; the official code repository exposes no visible license."
---

# Judge Conformal - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Analyzing Uncertainty of LLM-as-a-Judge | Primary metadata | arXiv record | arXiv:2509.18658v1; DOI 10.48550/arXiv.2509.18658 | https://arxiv.org/abs/2509.18658v1 | arXiv non-exclusive distribution record | 2026-07-16 | Inspected |
| S2 | Complete paper | Primary artifact | PDF and full-paper HTML | v1, submitted 2025-09-23 | https://arxiv.org/pdf/2509.18658 and https://arxiv.org/html/2509.18658 | Local copies verified and withheld | 2026-07-16 | Inspected in full |
| S3 | TeX/source package | Primary artifact | Source archive | arXiv:2509.18658v1 | https://arxiv.org/e-print/2509.18658 | Locally retained; 25 archive entries; not deposited | 2026-07-16 | Inspected |
| S4 | Official implementation | Official code | GitHub repository | commit `6c5d8302999b028d460dd1a7b78d698c56f7b7b7` | https://github.com/BruceSheng1202/Analyzing_Uncertainty_of_LLM-as-a-Judge | No visible repository license; scripts/notebooks inventoried without execution | 2026-07-16 | Inspected |
| S5 | RLMF Uncertainty - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260714 | `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md` | Repository synthesis context only | 2026-07-16 | Inspected |
| S6 | PAC Confidence - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260713 | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Repository synthesis context only | 2026-07-16 | Inspected |
| S7 | ConMax Reasoning - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260708 | `.lake-data/DEP-E/DEP-E-20260708-ConMax Reasoning/conmax_reasoning_manuscript.md` | Repository synthesis context only | 2026-07-16 | Inspected |

The paper is by Huanxin Sheng, Xinyi Liu, Hangfeng He, Jieyu Zhao, and Jian Kang. The inspected arXiv record lists Computation and Language as the primary category. No venue acceptance or journal DOI beyond the arXiv-issued DOI was identified. The official repository describes itself as the implementation and contains conformal predictors, evaluation scripts, analysis notebooks, prompts, and a GenAI-Bench example.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S3 | Primary paper | Metadata, abstract, full text, equations, tables, appendix, limitations, ethics, prompts | Identity, mechanism, experiments, and stated boundaries | High | v1 preprint; claims not independently reproduced |
| E2 | S2-S3, Sections 3 and Appendix A.1 | Primary method evidence | Split conformal construction, logit features, boundary adjustment, theorem and proof | Interval and adjustment mechanism | High for transcription | Proof not independently formalized |
| E3 | S2-S3, Section 4 | Primary empirical evidence | Dataset sizes, judges, frameworks, nine methods, 50/50 split, 30 seeds | Evaluation design | High | Dataset preprocessing and API outputs not rerun |
| E4 | S2-S3, Tables 1-2 | Primary empirical evidence | Coverage and width before/after adjustment | Coverage-improvement claim | High for reporting | Multiple settings still under-cover; author-reported |
| E5 | S2-S3, midpoint tables | Primary empirical evidence | MSE, MAE, and correlation comparisons | Midpoint-score claim | High for transcription | Midpoint is heuristic and task-specific |
| E6 | S2-S3, Sections 5-6 and limitations | Primary analysis | Calibration-size effects, reprompt behavior, task scope | Practical and generality boundaries | High | No long-term or production-shift study |
| E7 | S2-S3, ethical considerations | Primary limitation | Annotation bias and interval-interpretation cautions | Governance boundary | High | Mitigations are not fully evaluated |
| E8 | S4 | Official code | Repository README, file tree, notebooks, scripts, submodules | Implementation availability | High for inventory | No environment lock, license, execution, or result reproduction |
| E9 | S5-S7 | Related DEP artifacts | Faithful uncertainty, PAC intervals, confidence-guided compression | Cross-DEP synthesis | Medium | Conceptual relation; no joint experiment |
| E10 | Process records | Selection and cache evidence | Uniform draw, dedup checks, complete-source gate, missing-only extraction | Provenance and workflow validity | High | Operational evidence, not paper evidence |

## Executive Summary

The paper proposes converting a rating-based LLM judge's token logits into prediction intervals using split conformal prediction. Rather than treating a single Likert score as exact, the framework uses held-out human-rated examples to estimate how far a prediction may be from its reference score at a target miscoverage level. The interval width becomes an uncertainty signal. Because ratings are ordinal and discrete, the authors add a boundary adjustment that aligns interval endpoints with valid labels and prove non-decreasing coverage for the specified transformation.

The empirical scope is unusually broad for one evaluation study. SummEval contributes 1,600 summarization cases and DialSumm 1,400 dialogue-summarization cases, each rated across four dimensions by three humans. Four ROSCOE reasoning subsets contribute roughly 200 examples each. The main grid combines GPT-4o mini, DeepSeek-R1-Distill-Qwen-32B, and Qwen2.5-72B-Instruct; G-Eval and SocREval; seven regression and two ordinal conformal methods; a 50/50 calibration-test split; and 30 seeds. The authors report that boundary adjustment improves coverage across settings and often brings it near or above 90%, although several method/task combinations still under-cover.

Two practical claims deserve separate treatment. First, interval midpoint scores often reduce error against human ratings: the paper highlights an 88.7% MSE reduction from 3.907 to 0.443 for GPT-4o-mini SummEval fluency using a continuous R2CCP midpoint. Second, feeding intervals back to a judge does not reliably improve its score; models may resist changing an integer rating even when it lies outside the interval. Intervals are therefore stronger as audit and routing evidence than as persuasive prompts.

Confidence in source transcription is high because complete PDF, HTML, TeX, tables, and code inventory were inspected. Confidence in general deployment validity is medium-low. Conformal guarantees require exchangeability, human labels can encode bias, the repository was not run, and judge/prompt/model drift can invalidate calibration. The work supports uncertainty-aware evaluation, not autonomous trust in LLM judgments.

## Detailed Summary

### Problem Context

LLM-as-a-judge systems are scalable and adaptable, but a single score hides variability, model bias, prompt sensitivity, and decoding randomness. Self-reported confidence can be overconfident or strategically unreliable, while repeated sampling increases cost. The paper asks whether one judge pass plus token-level logits can support statistically meaningful uncertainty for rating tasks.

### Split Conformal Foundation

For a held-out calibration set, a prediction function maps judge logits `z` to a score estimate. A nonconformity function measures how unusual a reference score is relative to that prediction. For a target miscoverage rate `alpha`, the finite-sample conformal quantile of calibration nonconformity scores determines an interval around a test prediction. Under exchangeability, the paper cites the standard marginal coverage band from `1-alpha` to `1-alpha + 1/(n+1)`.

The construction is post-hoc and distribution-free in the conformal sense: it does not require a parametric distribution for judge errors. It is not assumption-free. Calibration and test examples must be exchangeable, labels must be meaningful, and the feature extraction/prediction procedure must remain fixed within the declared envelope.

### Logit Features and Conformal Methods

The framework locates the rating-token position in a judge response and extracts logits for candidate Likert labels, aggregating semantically equivalent tokens such as words and numerals. Regression-style methods receive logits directly; ordinal methods receive softmax probabilities. The paper evaluates CQR, asymmetric CQR, CHR, LVD, boosted CQR, boosted LCP, R2CCP, Ordinal APS, and Ordinal Risk Control. Heteroscedasticity tests in the appendix motivate conditional interval methods.

### Discrete Boundary Adjustment

Continuous endpoints can fall between legal rating labels. The proposed score transformation makes calibration scores consistent at integer labels, then shrinks or expands endpoints to aligned rating values. Shrinking removes continuous space containing no possible labels; expansion can capture nearby discrete labels missed by calibration variability. Theorem 1 states that the adjustment does not decrease coverage under its conditions.

Adjustment is not universally free. An expanded interval can increase width and human-review load. The correct comparison is therefore coverage and efficiency together, not coverage alone. The paper uses average width as its efficiency measure.

### Experimental Design

SummEval and DialSumm use average ratings from three annotators as GPA-like ground truth across consistency, coherence, fluency, and relevance. ROSCOE contributes CosmosQA, DROP, e-SNLI, and GSM8K reasoning evaluations, each around 200 examples. G-Eval is the primary framework; SocREval is added for reasoning. Judge choices reflect resource constraints but cover proprietary and open-weight families.

Each conformal configuration uses half the data for calibration and half for testing, repeated across seeds 1 through 30. Coverage is the fraction of references inside intervals; efficiency is average interval width. The paper also varies calibration size, tests prompt/model sensitivity, evaluates midpoint errors and correlations, and investigates reprompting.

### Representative Results

Before adjustment, CQR frequently exceeds 90% coverage but yields wide intervals; several narrower methods under-cover, particularly on smaller ROSCOE subsets. After adjustment, coverage improves broadly. The paper's concrete example is LVD on e-SNLI with Qwen2.5-72B-Instruct under SocREval, increasing from 85.96% to 95.53%.

Calibration size matters: mean coverage moves toward 90% and variability shrinks as more calibration examples are used. This supports a mundane but crucial conclusion—uncertainty estimates need sufficient labeled support. Small reasoning subsets produce wide and unstable intervals.

The paper recommends DeepSeek-R1-Distill-Qwen-32B for consistent coverage, Qwen2.5-72B-Instruct for narrower intervals, and R2CCP as a coverage-width balance. Those are empirical recommendations within the tested versions, prompts, tasks, and costs, not general rankings.

### Midpoints and Reprompting

Continuous and adjusted R2CCP midpoints are compared with raw integer scores and token-probability weighted averages. Midpoints usually lower MSE and MAE and show comparable correlations. The highlighted SummEval fluency case reduces MSE from 3.907 to 0.443. The paper warns that a midpoint is not a statistical mean or mode and does not imply symmetric uncertainty.

Reprompting a judge with interval information often reinforces the original score. When an integer score lies outside a non-integer interval, a judge may refuse the nearest integer change or produce a value that still violates the interval. Allowing intermediate scores sometimes moves it toward a boundary, but this is prompt behavior rather than a coverage theorem.

### Code and Reproducibility

The official repository contains seven named conformal-predictor files, analysis notebooks, evaluation and reprompt scripts, a GenAI-Bench example, three submodule pointers, and result-oriented notebooks. The pinned repository exposes no license. The review did not install dependencies, call model APIs, recover datasets, execute notebooks, or confirm that every published table is deterministically regenerated.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Split conformal prediction can attach marginal prediction intervals to rating-based LLM judgments using token-logit features. | Author method claim | E2-E3 | Directly supported by equations and implementation inventory; validity is conditional on exchangeability. | High for formulation |
| C2 | Boundary adjustment has non-decreasing coverage under the paper's stated construction. | Author theoretical claim | E2 | The proof was inspected in source but not independently formalized. | High for reporting; medium for verification |
| C3 | Adjustment improves empirical coverage across the evaluated grid. | Author empirical claim | E4 | Broadly supported by reported tables, but some combinations remain below 90%. | High for transcription |
| C4 | Interval midpoints can reduce error relative to raw or weighted scores. | Author empirical claim | E5 | Strong task-level results; midpoint semantics remain heuristic. | Medium-high |
| C5 | Reprompting with intervals is not a reliable correction mechanism. | Author analysis | E6 | Examples and aggregate analysis support resistance and boundary anchoring. | Medium-high |
| C6 | Interval width should route review rather than certify correctness. | Reviewer interpretation | E4-E7, E9 | Follows from conditional coverage, label bias, and method dependence. | High |
| C7 | Official code availability does not establish reproducibility. | Reviewer implementation observation | E8 | Repository is substantive but unlicensed and unexecuted in this review. | High |

## Methodology

- `Research objective`: Preserve a schema-complete review of interval-valued LLM judging and translate its evidence into bounded implementation and governance choices.
- `Sources inspected`: Complete arXiv v1 PDF, official full-paper HTML, metadata HTML, TeX/source archive, official GitHub README/tree at a pinned commit, and exactly three related Black Lake manuscripts.
- `Discovery strategy`: Uniform random selection from local PDF-parent units, multi-layer dedup search, local integrity repair, missing-only extraction cache, source-section/table inspection, official repository inspection, and targeted related-DEP search.
- `Inclusion criteria`: Primary material supporting identity, method, theorem, experiments, limitations, ethics, code availability, or direct conceptual overlap.
- `Exclusion criteria`: Secondary summaries, unverified venue claims, unexecuted code claims, and related records without concrete calibration/confidence overlap.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: Major claims map to evidence IDs; author claims, exact reported results, reviewer inference, and negative evidence are labeled separately.
- `Uncertainty handling`: Unreproduced results, exchangeability, missing license, annotation subjectivity, and drift risks remain explicit.
- `Extraction process`: Preflight identified `pypdf` as the PDF fallback; `missing-only` extraction produced PDF, HTML, and source text from the complete local bundle.
- `Selection methodology`: `rg --files -g "*.pdf"` enumerated 75,777 PDFs in 75,776 unique parent units; `Get-Random` selected zero-based index 29,719. The first draw passed dedup with zero exclusions and reselections.
- `Dedup methodology`: The arXiv ID, title, slug, DOI, logs, reports, DEP entries, dedup index, memory, active worktrees, author inventory, and Black-Lake-Data were checked. A metadata-only inventory row was not treated as a prior deposit.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:2509.18658v1, its complete paper/source bundle, official implementation inventory, and three related repository artifacts.
- `Temporal boundary`: Sources and repository state inspected through 2026-07-16; code pinned to the commit recorded above.
- `Evidence limits`: No experiment rerun, notebook execution, model API call, dataset audit, formal proof assistant, or long-term drift evaluation.
- `Assumptions`: The verified arXiv v1 artifacts form a coherent source bundle; reported tables reflect the submitted experiments; human averages serve as the paper's reference labels.
- `Constraints`: Public-safe output, no source redistribution, no automatic consequential decisions, and no implied rights from repository availability.
- `Out of scope`: Production certification, exhaustive conformal literature review, independent annotation study, API-cost audit, and multimodal reproduction.
- `Intended use`: DEP preservation, research review, offline calibration design, and implementation planning.
- `Audience`: Evaluation researchers, ML platform teams, safety reviewers, and human-review operations designers.
- `Reproducibility boundary`: Source and code inventory support a replication plan but not a reproduced result claim.
- `Data sensitivity`: Public research metadata; downstream calibration deployments may involve proprietary or sensitive human labels and require governance.

## Observations

- `Observed pattern`: Good average coverage can coexist with wide intervals or weak slice support; validity and usefulness are separate axes.
- `Technical implication`: Every interval should carry its calibration manifest, support count, model/prompt versions, method, target coverage, and empirical holdout result.
- `Contradiction or tension`: Boundary adjustment improves coverage partly by expanding to nearby labels, which may increase review load even when statistical validity improves.
- `Open question`: How should coverage be maintained after model, prompt, rubric, or annotator-population updates?
- `Reviewer hypothesis`: A fail-closed judge registry with interval replay tests would prevent more evaluation errors than reprompting models with confidence prose.

## Considerations

Exchangeability is an operational release condition, not a footnote. Calibration evidence should be invalidated or requalified after meaningful changes to the judge model, generation model, prompt, task mix, language, rubric, population, or annotation process. Shift detection cannot prove coverage; it signals that earlier evidence may no longer apply.

Human scores are not neutral ground truth. Annotator subjectivity and systematic bias can be reproduced inside apparently valid intervals. Coverage should be reported by relevant slices, paired with appeal paths and error-cost analysis, and never used to automate punitive, medical, legal, or financial decisions without independent governance.

Review routing creates capacity constraints. Wider intervals may appropriately increase abstention while overwhelming reviewers. A deployment needs review budgets, latency targets, escalation policies, and monitoring for selective automation that disadvantages specific groups or task types.

Token logits may be inaccessible or unstable across providers. Systems should treat logit availability, tokenization, rating-position detection, and equivalent-token aggregation as versioned dependencies. A fallback based on repeated judgments changes the cost and statistical model and needs separate validation.

## Strengths

- The paper converts an intuitive reliability concern into an explicit interval with a testable coverage target.
- It evaluates multiple conformal families rather than presenting one hand-picked method.
- The grid spans summarization and reasoning, three judge models, two evaluation frameworks, and 30 seeds.
- The boundary adjustment addresses the discrete semantics of rating scales and includes a proof.
- The appendix is unusually substantive, covering heteroscedasticity, runtime, memory, prompts, calibration size, shift, human baselines, and multimodal extension.
- Official code and analysis notebooks expose a concrete starting point for replication.

## Weaknesses

- Marginal coverage under exchangeability does not establish robustness to production drift or subgroup error.
- The smaller reasoning subsets yield unstable calibration and wide intervals.
- Recommendations depend on particular judge versions, prompts, API behavior, and compute budgets.
- Midpoints are empirically useful but lack the probabilistic interpretation users may assume.
- Reprompting results show that giving an interval to a judge can create anchoring without correction.
- The repository exposes no visible license or fully pinned execution environment.
- Experiments and proof were not independently reproduced in this review.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add shift-aware replay gates | Deployment | Exchangeability can fail silently | Prevent stale intervals from authorizing decisions | False alarms and recalibration work | Versioned natural/synthetic shift suites |
| Report conditional coverage | Fairness | Marginal validity can hide slice failures | Reveal under-supported groups and tasks | Larger label requirements | Pre-registered slice coverage with multiplicity control |
| Separate method selection data | Evaluation design | Choosing the best interval on test evidence overfits | Cleaner comparative claims | Extra held-out data | Nested calibration/selection/test splits |
| Publish exact environment and licenses | Reproducibility | Repository inventory is not a runnable manifest | Easier independent verification | Maintenance burden | Clean-room rerun from tagged release |
| Compare equal-cost alternatives | Baselines | Repeated judging and human review have different costs | Decision-relevant tradeoff curves | Complex accounting | Coverage-width-cost-review Pareto analysis |
| Evaluate online recalibration | Operations | Static labels age | Controlled adaptation under drift | Leakage and dependence risk | Time-ordered calibration with locked future holdout |

## Potential Implementations

### Evaluation Evidence Registry

- `User`: ML evaluation and governance teams.
- `Goal`: make every automated rating traceable to valid calibration evidence.
- `Core mechanism`: store interval method, endpoints, target coverage, empirical coverage, width, support, versions, and shift state alongside each rating.
- `Required inputs`: judge logits or scores, held-out labels, model/prompt/rubric manifests, slice metadata, and shift telemetry.
- `Outputs`: auditable evidence card and allow/review/recalibrate status.
- `Risk controls`: calibration/test separation, minimum support, access control, privacy minimization, and fail-closed version mismatch.
- `Evaluation`: holdout coverage, slice coverage, width, abstention, review load, and unsupported-decision count.

### Human-Review Capacity Router

- `User`: annotation operations and quality teams.
- `Goal`: allocate scarce review to uncertain or high-cost cases.
- `Core mechanism`: combine interval width with application harm, slice fairness, and reviewer capacity; never route by width alone.
- `Required inputs`: intervals, decision costs, queue capacity, service-level targets, and fairness constraints.
- `Outputs`: prioritized review queue with explicit reasons.
- `Risk controls`: random audit sample, per-slice quotas, appeal path, maximum automation rate, and drift halt.
- `Evaluation`: error caught per review hour, latency, slice outcomes, reviewer agreement, and escalation burden.

### Judge Release Gate

- `User`: platform engineers updating evaluator models or prompts.
- `Goal`: prevent silent calibration regressions.
- `Core mechanism`: replay versioned calibration and shift suites, recompute intervals, and compare coverage-width-cost envelopes with the approved release.
- `Required inputs`: candidate judge/prompt, immutable replay set, prior release evidence, and approval thresholds.
- `Outputs`: pass/fail report with changed slices and invalidated policies.
- `Risk controls`: no production traffic, blinded labels where feasible, independent approval, and no automatic threshold relaxation.
- `Evaluation`: regression detection, false-block rate, reproducibility, and time to recalibration.

## Three Ways to Exercise This Research

1. **Synthetic conformal lab**: Objective: verify split-conformal marginal coverage under known exchangeable noise. Inputs: seeded synthetic predictions and labels. Method: isolate calibration/test sets, form intervals across repeated trials, and compare empirical coverage with the target. Output: coverage-width plots and failure cases. Success criterion: the implementation meets the pre-registered tolerance. Stop condition: any hidden data reuse or undercoverage. Safety boundary: synthetic data only.
2. **Offline judge replay**: Objective: assess one public or approved rating dataset. Inputs: frozen judge outputs/logits, independent human labels, and versioned prompts. Method: compare several conformal methods using nested selection and test splits. Output: coverage, width, MAE, slice support, and review-load report. Success criterion: a method clears coverage and operational-width thresholds without test-set tuning. Stop condition: missing rights, lineage, or support. Safety boundary: no live consequential decisions.
3. **Drift invalidation drill**: Objective: test fail-closed behavior after a judge or prompt update. Inputs: two versioned judges/prompts, locked replay data, and a stub review queue. Method: show that version mismatch invalidates the old interval policy, rerun calibration, and require approval. Output: invalidation/recovery trace. Success criterion: zero decisions use stale evidence. Stop condition: automation bypasses the gate. Safety boundary: sandboxed replay only.

## Example MVP Product

- `Product name`: JudgeInterval Registry.
- `Target user`: ML evaluation, platform, safety, and review-operations teams.
- `Problem`: point ratings hide uncertainty and become stale when judge pipelines change.
- `Core workflow`: register a judge/prompt/rubric version; import approved calibration labels; build candidate intervals; select on validation data; verify on a locked holdout; attach evidence to offline ratings; route uncertain cases; invalidate on version or shift alarms.
- `Data requirements`: frozen logits or rating probabilities, independent human labels, dataset/rubric manifests, slice fields with privacy review, and review-capacity limits.
- `Architecture`: local/offline Python service, immutable object manifest, conformal-method adapters, replay runner, shift/version gate, policy evaluator, Markdown/JSON exporter, and human approval checkpoint.
- `Success metrics`: target holdout and slice coverage, bounded interval width, calibrated abstention, zero stale-policy decisions, deterministic reports, acceptable review load, and complete provenance.
- `Risk controls`: no live automation in MVP; calibration/test isolation; minimum support; encrypted label storage; access logs; fail-closed drift; fairness audit; no medical/legal/financial/punitive use.
- `Limitations`: cannot prove semantic correctness, inherits label bias, depends on exchangeability, may be conservative, and does not solve malicious or correlated evaluator failures.
- `MVP boundary`: offline evidence generation and routing simulation only; no model training, online threshold updates, or automatic consequential decisions.
- `Deployment model`: local CLI or internal batch service.
- `Evaluation plan`: unit tests on known quantiles, seeded coverage simulations, replay regression tests, slice support tests, leakage checks, and reviewer acceptance.
- `Failure modes`: stale versions, label leakage, sparse slices, incorrect token mapping, correlated samples, false shift alarms, queue overload, and misleading midpoint interpretation.
- `Maintenance plan`: pin methods and dependencies, version all manifests, schedule locked replays, monitor support/coverage, and require reapproval after changes.

## Related Research and Reading

### Exactly Three Related DEP Entries

| Entry | Concrete Overlap | Source Basis |
|---|---|---|
| `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md` | Separates expressed uncertainty, factual accuracy, and evaluator-dependent consistency proxies | Inspected source metadata, evidence ledger, mechanism, results, and caveats |
| `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Builds finite-sample intervals for downstream decisions and foregrounds identical-distribution limits | Inspected source metadata, PAC construction, applications, and distribution-shift boundary |
| `.lake-data/DEP-E/DEP-E-20260708-ConMax Reasoning/conmax_reasoning_manuscript.md` | Uses confidence as a resource-control signal and exposes auxiliary-evaluator dependence | Inspected source metadata, dual-confidence method, metrics, and limitations |

### Primary and Near-Primary Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Analyzing Uncertainty of LLM-as-a-Judge | Primary paper | Reviewed work | https://arxiv.org/abs/2509.18658v1 |
| Official implementation | Official code | Reproduction and method inventory | https://github.com/BruceSheng1202/Analyzing_Uncertainty_of_LLM-as-a-Judge |
| A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification | Tutorial paper | Conformal foundations cited by the reviewed work | https://doi.org/10.48550/arXiv.2107.07511 |
| Conformalized Quantile Regression | Primary method paper | CQR baseline | https://doi.org/10.48550/arXiv.1905.03222 |
| G-Eval | Primary evaluation paper | Main judge framework | https://doi.org/10.48550/arXiv.2303.16634 |
| SummEval | Primary benchmark paper | Summarization human ratings | https://doi.org/10.1162/tacl_a_00373 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2509.18658v1 | Identity, metadata, abstract, submission history | 2026-07-16 | Primary record |
| R2 | https://arxiv.org/pdf/2509.18658 | Complete paper review | 2026-07-16 | Verified local copy withheld |
| R3 | https://arxiv.org/html/2509.18658 | Complete paper review and table cross-check | 2026-07-16 | Official full-paper HTML; local copy withheld |
| R4 | https://arxiv.org/e-print/2509.18658 | Equations, tables, prompts, limitations, appendix | 2026-07-16 | Verified local source archive withheld |
| R5 | https://doi.org/10.48550/arXiv.2509.18658 | Persistent arXiv identifier | 2026-07-16 | DOI locator |
| R6 | https://github.com/BruceSheng1202/Analyzing_Uncertainty_of_LLM-as-a-Judge | Official code inventory | 2026-07-16 | Pinned commit; not executed; license not visible |
| R7 | `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md` | Related uncertainty-expression bridge | 2026-07-16 | Repository artifact |
| R8 | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Related finite-sample interval bridge | 2026-07-16 | Repository artifact |
| R9 | `.lake-data/DEP-E/DEP-E-20260708-ConMax Reasoning/conmax_reasoning_manuscript.md` | Related confidence-control bridge | 2026-07-16 | Repository artifact |
| R10 | https://doi.org/10.48550/arXiv.2107.07511 | Conformal background | 2026-07-16 | Near-primary reading |
| R11 | https://doi.org/10.48550/arXiv.1905.03222 | CQR method | 2026-07-16 | Baseline reading |
| R12 | https://doi.org/10.48550/arXiv.2303.16634 | G-Eval framework | 2026-07-16 | Evaluation context |
| R13 | https://doi.org/10.1162/tacl_a_00373 | SummEval benchmark | 2026-07-16 | Dataset context |

## Appendix

### Replication Checklist

- [ ] Pin paper version and official repository commit.
- [ ] Resolve licensing for code and all datasets before reuse.
- [ ] Freeze judge models, endpoints, tokenizers, prompts, decoding, and rating-token rules.
- [ ] Reconstruct SummEval, DialSumm, and ROSCOE labels with auditable split manifests.
- [ ] Keep method selection, calibration, validation, and final testing distinct.
- [ ] Run all nine conformal methods across 30 declared seeds.
- [ ] Verify coverage, width, MSE, MAE, correlation, runtime, and memory.
- [ ] Add slice and distribution-shift evaluations.
- [ ] Record API/model version changes and invalidate stale evidence.
- [ ] Obtain independent review before any consequential deployment.

### Process and Source Inventory

The archive unit began with a valid complete PDF but no full-paper HTML. One bounded official request each supplied the missing full-paper HTML, metadata HTML, and TeX/source archive. The final local verifier confirmed the PDF header/EOF, HTML size/body/document/heading/structure thresholds, a readable 25-entry source archive, and zero partial files. `missing-only` extraction then produced complete PDF, HTML, and source text caches without network use.

The selection used zero-based index 29,719 of 75,776 uniformly sampled paper units. Dedup found no prior research artifact. The public deposit contains only derived Markdown plus the public dedup/index JSON updates; source files are withheld.

### Source-Withholding Confirmation

No PDF, HTML, metadata page, TeX/source archive, extracted text, cache manifest, code snapshot, dataset, or notebook was copied into `.lake-data`, `.reports`, `.logs`, `.staging`, Git history, a pull request, or Slack. Public arXiv and GitHub URLs provide provenance without redistributing source material.
