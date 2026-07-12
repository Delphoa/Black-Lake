---
title: "PAC Confidence - DEP-E"
generated_at: "2026-07-13"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of PAC interval confidence for DNN classification, fast inference, and safe planning."
source_status: "private source inspected; public URLs only in deposit"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-13"
temporal_cutoff: "arXiv v5 dated 2021-03-17; repository context through 2026-07-13"
primary_url: "https://arxiv.org/abs/2011.00716"
stable_identifier: "arXiv:2011.00716v5; DOI:10.48550/arXiv.2011.00716"
confidence_summary: "High for paper identity and reported results; medium for interpretation; low for independent reproducibility because experiments and proofs were not rerun."
safety_scope: "research review, synthetic evaluation, and decision-gate design only"
distribution_notes: "No paper PDF, dataset, model, or source package is redistributed."
---

# PAC Confidence - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | PAC Confidence arXiv record | Primary metadata | HTML | arXiv:2011.00716v5; DOI 10.48550/arXiv.2011.00716 | https://arxiv.org/abs/2011.00716 | Public record; redistribution rights for source files were not independently assessed | 2026-07-13 | Inspected |
| S2 | PAC Confidence full paper | Primary artifact | PDF | v5, 27 pages | https://arxiv.org/pdf/2011.00716 | Private archive copy inspected; local path withheld and file not deposited | 2026-07-13 | Inspected in full |
| S3 | PAC Confidence HTML | Primary artifact | HTML | public arXiv rendering | https://arxiv.org/html/2011.00716 | Used to cross-check text, tables, and equations | 2026-07-13 | Inspected |
| S4 | ICLR 2021 OpenReview record | Official venue record | HTML | forum Qk-Wq5AIjpq | https://openreview.net/forum?id=Qk-Wq5AIjpq | Venue metadata and abstract | 2026-07-13 | Inspected |
| S5 | RRT-CBF Motion DEP | Related Black Lake artifact | Markdown | DEP-E-20260711 | `.lake-data/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` | Repository context; not evidence for S1-S4 claims | 2026-07-13 | Inspected |
| S6 | HSD FTI-FDet DEP | Related Black Lake artifact | Markdown | DEP-E-20260712 | `.lake-data/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` | Repository context; not evidence for S1-S4 claims | 2026-07-13 | Inspected |
| S7 | CausalTAD Trajectory DEP | Related Black Lake artifact | Markdown | DEP-E-20260711 | `.lake-data/DEP-E-20260711-CausalTAD Trajectory/causaltad_trajectory_manuscript.md` | Repository context; not evidence for S1-S4 claims | 2026-07-13 | Inspected |
| S8 | Black Lake README | Repository authority | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Governs DEP-E naming, contents, attribution, and commit format | 2026-07-13 | Inspected live |
| S9 | Black-Lake-Data README | Related repository authority | Markdown | live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Governs related raw DEP layout and provenance | 2026-07-13 | Inspected live |
| S10 | Selection and extraction record | Processing evidence | Public-safe summary | 75,761 units; index 22,891 | This manuscript, Appendix | Contains no local path or exact execution timestamp | 2026-07-13 | Generated and validated |

Paper/work metadata:

- `Full title`: PAC Confidence Predictions for Deep Neural Network Classifiers.
- `Authors`: Sangdon Park, Shuo Li, Insup Lee, Osbert Bastani.
- `Affiliation shown in paper`: PRECISE Center, University of Pennsylvania.
- `Venue`: International Conference on Learning Representations, ICLR 2021 Poster.
- `Initial arXiv submission`: 2020-11-02.
- `Inspected revision`: arXiv v5 dated 2021-03-17.
- `Subject`: machine learning classification, uncertainty calibration, fast inference, safe planning.
- `Source files deposited`: none; no `.source/` directory was created.
- `Private source note`: a local archive copy of the PDF was used for source-first review, but its location is withheld and the file is not redistributed.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4 | Primary/official metadata | Title, authors, dates, abstract, venue, poster status, identifiers | Bibliographic identity and high-level contribution | High | Metadata cannot validate methods or results |
| E2 | S2, S3, Sections 2 and Appendices A-B | Primary full text | Histogram bins, Bernoulli correctness observations, Clopper-Pearson intervals, `delta/K` allocation, union-bound proofs | PAC confidence-coverage construction | High for author formulation | Proofs were inspected but not independently rederived |
| E3 | S2, S3, Section 3 and Appendices C-D | Primary full text | Error decomposition, threshold search, two-branch optimality theorem | Fast/slow cascade guarantee | High for formulation | Depends on fixed distribution, calibration sample, and model/runtime assumptions |
| E4 | S2, S3, Section 4 and Appendix E | Primary full text | Recoverability classifier, rollout distribution, unsafe-rollout bound, threshold optimization | Safe-planning guarantee | High for formulation | Simulator/model/fallback assumptions were not independently verified |
| E5 | S2, S3, Section 5.1 and Figure 2 | Primary empirical evidence | ImageNet/ResNet101 split, 20 bins, ECE values, coverage intervals | Calibration results | High for transcription | No rerun, seed distribution, or alternative-bin audit |
| E6 | S2, S3, Section 5.2 and Figure 3 | Primary empirical evidence | Error, CPU/GPU time, MACs, desired-error comparison | Fast-inference results | High for transcription | Hardware-specific averages; no latency tails or reproduction |
| E7 | S2, S3, Section 5.3 and Figure 4 | Primary empirical evidence | AI Habitat setup, safety/success outcomes, threshold baselines | Safe-planning results | High for transcription | Simulator-only; underlying policy safe in about 30% of rollouts |
| E8 | S2, S3, Appendix F.1 | Primary limitation | Guarantee transfer requires identical validation and test distributions | Distribution-shift boundary | High | Proposed shift extensions are future directions, not established results |
| E9 | S5-S7 | Related DEP artifacts | Formal planning boundaries, compact visual inference, OOD anomaly detection and calibration needs | Cross-DEP synthesis | Medium | Contextual evidence; no joint experiment exists |
| E10 | S8-S10 | Repository/process evidence | Live deposition rules, random selection, dedup locations and outcomes | Artifact compliance and selection provenance | High | Search coverage depends on current repository indexes and checkout |

## Executive Summary

The paper replaces single-number DNN confidence with an interval whose coverage is backed by a finite calibration set. It bins top-label scores, treats correctness within each bin as a binomial proportion, and applies exact Clopper-Pearson bounds with a simultaneous-coverage correction. The resulting interval predictor is PAC in the authors' stated on-distribution setting. The authors then use lower and upper bounds—not raw softmax scores—to choose early-exit thresholds for a fast/slow classifier cascade and to choose a threshold for a perception-based robot safety shield.

The empirical evidence is promising but conditional. On ImageNet/ResNet101, the proposed construction produces intervals containing empirical accuracy in every displayed bin; its fast-inference cascade reports 32% fewer MACs and 54% lower measured runtime than the slow network while meeting the tested relative-error bound. In AI Habitat, the rigorous shield meets the tested safety-rate target when naive choices sometimes fail. These are author-reported experiments, not independently reproduced outcomes.

The primary limitation is decisive: coverage transfer assumes that calibration and test data follow the same distribution. The method does not automatically handle sensor degradation, new sites, novel routes, changing prevalence, adversarial examples, or sim-to-real shift. It also does not certify the rest of a system. A safe deployment must separately verify data lineage, shift detection, calibration support, action thresholds, fallback readiness, solver behavior, and monitoring.

The three related DEP entries sharpen that boundary. HSD FTI-FDet shows why compact visual systems need calibrated abstention under hardware pressure. CausalTAD shows why OOD regimes and score thresholds require explicit shift handling. RRT-CBF Motion shows that mathematical safety constraints remain conditional on state freshness, dynamics, solver feasibility, and fallback implementation. The synthesis is a layered evidence gate: statistical intervals, shift checks, formal constraints, and safe fallbacks should remain independent, observable controls.

## Detailed Summary

### Problem and Background

DNN classifiers often produce high softmax scores even when wrong. Calibration methods rescale scores so that, for example, predictions assigned confidence near 0.8 are correct about 80% of the time. Average calibration does not necessarily support a particular downstream decision. A safety-critical system needs to know whether the observed calibration data justify trusting a score range, and it must account for finite-sample error.

The paper focuses on top-label confidence. It coarsens the continuum of scores into `K` bins and defines the true confidence for a test example as the correctness probability among examples whose top-label scores fall in the same bin. This gives a finite set of bin parameters that can be estimated simultaneously.

### PAC Confidence-Coverage Method

For each bin, calibration examples supply Bernoulli outcomes: one when the classifier's top label is correct and zero otherwise. The unknown bin correctness rate is a binomial proportion. A Clopper-Pearson interval inverts binomial tail tests to obtain an exact two-sided confidence interval. The method assigns confidence level `delta/K` to each bin and uses a union bound, so with probability at least `1 - delta` over the calibration sample, every bin's true correctness rate lies inside its interval.

This construction is deliberately interval-valued. The trivial interval `[0, 1]` always covers but is useless, so practical value depends on interval width. Width is driven by bin support, desired confidence, and the observed success count. More bins increase resolution but reduce examples per bin; fewer bins improve support but merge predictions with potentially different risks.

Theorem 1 states simultaneous PAC coverage for the proposed predictor. Appendix A gives an alternative PAC formulation allowing an `epsilon` fraction of inputs to miss coverage, and Theorem 5 states that the construction satisfies it as well. The reviewer treats these as author-proved theorems, not independently verified proofs.

### Fast DNN Inference

The first application composes multiple classifier branches. Early branches are faster but less accurate; the final branch is slower and more accurate. The system exits early when confidence clears a threshold. Raw or point-calibrated thresholds can violate a desired relative-error budget because they ignore finite-sample error.

The paper decomposes the cascading classifier's error difference relative to the slow classifier into branch-level disagreement events. It applies confidence intervals to correctness and branch-disagreement probabilities, then chooses thresholds that satisfy an upper bound on relative error. Theorem 2 provides the stated probabilistic error guarantee. For two branches, Theorem 3 states that the selected threshold produces the fastest cascade among cascades meeting the bound, assuming the earlier classifier is faster.

The ImageNet experiment uses ResNet101 and one exit branch placed a quarter of the way into the network. The slow model reports 22.32% top-1 error, 214.31 microseconds CPU time, 2.95 microseconds GPU time, and 7.83e9 MACs. The rigorous cascade reports 23.26% error, 85.58 microseconds CPU, 1.34 microseconds GPU, and 5.33e9 MACs. Histogram binning is faster but reports 24.54% error and misses the desired bound in the shown comparison. The result supports a tradeoff under the tested split; it does not establish device-independent performance or latency tails.

### Safe Planning

The second application uses a DNN to predict whether a robot state is recoverable from visual observation. A learned policy acts only when the predictor treats the state as recoverable; otherwise a backup policy takes over and stops. The authors derive an upper bound on the probability of an unsafe rollout using the rate at which the classifier misses the first unsafe state and the overall probability of unsafe rollouts under the learned policy.

Clopper-Pearson bounds are applied to both factors, and the classifier threshold is maximized subject to an upper bound no greater than the risk budget. Theorem 4 states the resulting safety guarantee over sampled rollout and unsafe-observation calibration sets. The paper explicitly limits the result to its environment model and does not solve sim-to-real transfer.

In AI Habitat, the learned policy is safe in only about 30% of rollouts. The rigorous shield meets the tested target while reducing task success because it falls back often. The evidence illustrates a central system truth: a valid safety gate may expose that the underlying policy is not useful enough, rather than making an unsafe policy both safe and successful.

### Limitations and Boundary Conditions

Appendix F.1 states that validation and test distributions must be identical for the PAC guarantees to transfer. Shift detection, importance weighting, and covariate-shift calibration are proposed directions. Unknown density ratios create another estimation problem whose error would need to be included in any guarantee.

Further reviewer-identified boundaries include sparse-bin conservatism, adaptive binning risk, class/prevalence imbalance, dependence between repeated or correlated samples, calibration-set contamination, hardware-specific timing, missing tail latency, simulator/model mismatch, stale observations, and backup-policy failure. The paper's certificates should therefore be attached to a versioned data-and-system envelope.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Histogram binning plus Clopper-Pearson intervals yields simultaneous PAC confidence coverage over bins. | Author theoretical claim | E2 | Directly formulated and proved in the paper; proof not independently rederived. | High for source reporting; medium for independent verification |
| C2 | Interval bounds can select cascade thresholds that satisfy a desired relative-error budget with high probability. | Author theoretical claim | E3 | Supported under the paper's distribution and model assumptions. | Medium-high |
| C3 | For two branches, the chosen feasible threshold gives the fastest qualifying cascade. | Author theoretical claim | E3 | Conditional on the optimization and earlier branch being faster. | Medium-high |
| C4 | The rigorous cascade improves inference efficiency while meeting the tested error bound. | Author empirical claim | E6 | Tables support the reported test result; no rerun or latency-tail evidence. | High for transcription; low for reproduction |
| C5 | PAC intervals can select a planning-shield threshold satisfying the stated unsafe-rollout budget. | Author theoretical claim | E4 | Conditional on rollout distributions, recoverability labels, dynamics, and backup assumptions. | Medium-high |
| C6 | The safe-planning experiment meets tested safety targets when naive thresholds sometimes fail. | Author empirical claim | E7 | Supported by the reported figures; simulator-only and not reproduced. | High for transcription; low for deployment transfer |
| C7 | The guarantees transfer only when validation and test distributions match. | Author limitation | E8 | Explicit and central; should be treated as a release gate. | High |
| C8 | A layered statistical/shift/formal/fallback gate is a useful cross-DEP architecture. | Reviewer interpretation | E8, E9 | Conceptually aligned across four artifacts but not jointly validated. | Medium |
| C9 | The selected paper was eligible and not previously deposited by this automation. | Process claim | E10 | ID, DOI, title, and slug scans found no duplicate or 24-hour marker. | High |

## Methodology

- `Research objective`: Preserve a source-grounded review of PAC interval confidence and synthesize it with exactly three existing DEP entries covering safe planning, efficient visual inference, and OOD anomaly decisions.
- `Sources inspected`: the 27-page arXiv v5 PDF, public arXiv metadata and HTML, OpenReview venue record, live Black Lake and Black-Lake-Data READMEs, current automation memory, repository dedup markers, and exactly three related DEP manuscripts.
- `Discovery strategy`: enumerate PDFs with `rg --files -g "*.pdf"`, normalize parent directories as paper units, draw a uniform zero-based `Get-Random` index, inspect adjacent metadata, then cross-check public primary sources.
- `Inclusion criteria`: sources that establish paper identity, expose method/results/limitations, govern deposition, support duplicate detection, or provide concrete conceptual overlap.
- `Exclusion criteria`: duplicate papers, same-paper artifacts or archive markers within 24 hours, secondary summaries when primary text was available, unrelated DEP entries, and unverified implementation claims.
- `Analytical approach`: empirical, conceptual, comparative, implementation, safety/ethics, product research, replication, and provenance review.
- `Evidence handling`: evidence IDs distinguish author theory, empirical results, limitations, reviewer synthesis, and process evidence. Numerical claims were checked in both extracted PDF text and public arXiv HTML.
- `Uncertainty handling`: theorems remain author claims unless rederived; experiments remain author-reported unless rerun; missing code/data, source redistribution rights, seeds, tail latency, and shift evidence remain visible.
- `Extraction process`: source-processing preflight found pypdf available; missing-only extraction produced full PDF text. Local HTML and source-package inputs were unavailable. Public arXiv HTML supplied a separate full-text cross-check.
- `Version control`: paper pinned to arXiv v5 dated 2021-03-17; repository rules read from live default branches on the access date.
- `Claim selection`: prioritize the interval construction, downstream threshold mechanisms, exact reported metrics, and the on-distribution limitation.
- `Cross-checking`: metadata checked between arXiv and OpenReview; results checked between private PDF extraction and public HTML; related-entry claims checked in the deposited manuscripts and their source tables.
- `Safety handling`: implementation ideas are bounded to offline evaluation, human review, safe fallback, and synthetic/public-safe examples. No physical system certification is claimed.
- `Reviewer stance`: critical paper report, DEP-ready preservation, system-boundary analysis, product translation, and replication planning.
- `Random selection`: 75,761 PDF candidates and 75,761 unique parent-directory paper units; uniform zero-based selected index 22,891.
- `Dedup validation`: searched Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and Black-Lake-Data for arXiv ID, DOI, title, and slug; exclusions 0 and reselections 0.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:2011.00716v5, its ICLR venue record, core theory, experiments, limitations, and exactly three related DEP bridges.
- `Temporal boundary`: primary paper pinned to 2021-03-17; public and repository sources accessed through 2026-07-13.
- `Evidence limits`: no proof assistant, mathematical rederivation, source-code audit, dataset download, model execution, experiment rerun, or hardware benchmark was performed.
- `Assumptions`: the archived PDF corresponds to arXiv v5; public HTML accurately renders the paper; related DEP manuscripts accurately preserve their cited source reviews.
- `Constraints`: public-safe output, no local path disclosure, no source redistribution without established permission, no production safety claim, and no automation of consequential decisions.
- `Out of scope`: medical decision deployment, physical robot certification, adversarial robustness, sim-to-real proof, legal compliance, and exhaustive comparison to conformal prediction literature.
- `Intended use`: DEP deposition, research review, evaluation design, release-gate planning, and safe prototype ideation.
- `Audience`: uncertainty researchers, ML systems engineers, safety reviewers, robotics engineers, edge-AI teams, and Black Lake maintainers.
- `Depth target`: schema-complete manuscript report with implementation and replication guidance.
- `Reproducibility boundary`: readers can trace claims to public sources, but cannot reproduce the experiments from this artifact alone.
- `Operational boundary`: confidence intervals may inform offline or supervised gates; they must not be interpreted as independent certification of an end-to-end system.
- `Data sensitivity`: public scholarly metadata and repository artifacts; any future operational imagery, trajectories, or patient data would require separate governance.

## Observations

- `Observed pattern`: The method's value comes from changing the output type from a point score to an interval that can be composed with a decision budget.
- `Technical implication`: Bin support and interval width should be release telemetry. A narrow-looking score without support information is insufficient evidence.
- `Observed pattern`: In both applications, the downstream guarantee is built from multiple estimated events, not merely classifier calibration.
- `Contradiction or tension`: The empirical plots show strong results, while the formal guarantee remains deliberately narrow and on-distribution. Product language must preserve that difference.
- `Cross-source pattern`: HSD FTI-FDet, CausalTAD, and RRT-CBF each identify a different boundary that a confidence interval alone cannot solve: hardware/rare-fault evidence, distribution shift, and dynamic/solver/fallback integrity.
- `Reviewer hypothesis`: A versioned decision-evidence card that joins calibration coverage, shift status, system constraints, and fallback health would prevent many guarantee-composition errors.
- `Open question`: Can simultaneous coverage be preserved under adaptive bins, online recalibration, and estimated covariate-shift weights without making intervals operationally unusable?

## Considerations

Statistical coverage is not semantic correctness. A bin may be calibrated while grouping materially different classes, sites, users, or hazards. Slice-aware support and cost-sensitive risk budgets are needed when false negatives have different consequences.

Calibration data are production dependencies. Leakage from model training, repeated correlated observations, stale samples, or unreviewed label changes can invalidate inference. Data manifests should record source, time window, split logic, class prevalence, and approval state.

Abstention creates operational load. A conservative interval may be statistically appropriate but overwhelm human reviewers or trigger excessive robot stops. Systems must measure review capacity, fallback success, user delay, and failure when fallback is unavailable.

Distribution shift must fail closed. A shift detector cannot prove that coverage still holds; it can only signal that prior calibration evidence may no longer apply. Automatic decisions should pause until recalibration or another approved envelope is established.

Safety-critical use requires independent verification of sensors, timing, dynamics, constraints, and fallback. Statistical and formal guarantees should be linked in an assumption registry, not collapsed into a single “safe” label.

## Strengths

- The method is simple, inspectable, and model-agnostic once a fixed classifier and held-out calibration set exist.
- Exact binomial intervals make finite-sample uncertainty explicit rather than hiding it behind an average calibration score.
- The union-bound construction yields a clear simultaneous-coverage statement over bins.
- Two downstream applications demonstrate how interval bounds enter actual threshold optimization rather than stopping at a reliability diagram.
- The paper reports concrete accuracy, compute, latency, safety, and success tradeoffs.
- Appendices expose proofs, implementation details, ablations, sample-size effects, and the on-distribution limitation.
- The safe-planning experiment honestly shows that stronger safety can reduce success when the underlying policy is unsafe.

## Weaknesses

- The central guarantee does not transfer automatically under distribution shift, adversarial input, or sim-to-real mismatch.
- Fixed histogram bins trade resolution against support and can be conservative or unstable in sparse regions.
- Clopper-Pearson intervals are exact but often conservative, which may create avoidable abstention.
- The experiments were not independently reproduced and do not report repeated-seed uncertainty.
- Runtime evidence is hardware-specific and average-based; p95/p99 latency and fallback overhead are absent.
- The safe-planning guarantee relies on simulator dynamics, recoverability labels, rollout distributions, and a functional backup policy.
- The paper does not provide a complete production governance design for calibration refresh, shift alarms, or decision appeals.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Compare simultaneous interval families | Statistics | Clopper-Pearson can be conservative | Lower abstention at matched coverage | Approximation or dependence errors | Pre-registered coverage simulation and held-out tests across sparse bins |
| Add adaptive-bin validity accounting | Calibration | Fixed bins waste support or resolution | Better local discrimination | Data-dependent bins can invalidate naive intervals | Split calibration for bin selection versus interval estimation |
| Add class- and cost-conditional bounds | Decision safety | Aggregate top-label correctness hides asymmetric harm | Risk budgets aligned to consequences | More samples and multiple-testing burden | Per-class coverage and cost-weighted decision curves |
| Add explicit shift gate | Robustness | Coverage assumes matching distributions | Prevent silent use outside the evidence envelope | False alarms and recalibration load | Synthetic and natural shift suites with fail-closed acceptance tests |
| Propagate density-ratio uncertainty | Covariate shift | Estimated importance weights add error | More honest shifted-coverage bounds | Wider intervals and model complexity | Coverage tests with known synthetic ratios and estimated ratios |
| Report latency tails and fallback cost | Systems | Mean speed can hide deadline misses | Deployable performance evidence | More measurement infrastructure | p50/p95/p99 timing, queue, energy, and fallback benchmarks |
| Release pinned reproduction artifacts | Reproducibility | Public results are difficult to audit without exact configs | Faster independent validation | Maintenance and storage burden | Fresh-environment rerun matching every reported table |

## Potential Implementations

1. `PAC-Calibrated Edge Inspection Gate`
   - `User`: rail or industrial visual-inspection team.
   - `Goal`: accept compact-detector outputs only when class/site-specific evidence clears a risk threshold.
   - `Core mechanism`: maintain Clopper-Pearson intervals per approved score bin and component slice; compare the lower bound with an acceptance threshold.
   - `Required inputs`: versioned detector scores, adjudicated calibration labels, site/component metadata, shift aggregates, review capacity.
   - `Outputs`: accept/review decision, interval, support count, shift state, model/calibration versions.
   - `Risk controls`: human review, no automatic actuation, minimum-support gate, fail-closed shift policy, immutable evidence record.
   - `Evaluation`: per-component coverage, false negatives, review load, calibration drift, and p95 latency.

2. `Shift-Aware Trajectory Decision Card`
   - `User`: mobility anomaly-model reviewer.
   - `Goal`: prevent OOD anomaly scores from becoming uncalibrated consequential decisions.
   - `Core mechanism`: combine score-bin intervals with region/time/route shift tests and freeze automation when the evidence envelope changes.
   - `Required inputs`: de-identified aggregate scores, adjudicated labels, map/time version, calibration manifest, shift metrics.
   - `Outputs`: release card, calibrated review threshold, unsupported slices, refresh recommendation.
   - `Risk controls`: aggregation thresholds, privacy review, human appeal, no punitive default, versioned retention policy.
   - `Evaluation`: coverage by ID/OOD slice, false-positive burden, shift detection delay, and recalibration recovery.

3. `Layered Motion-Shield Evidence Gate`
   - `User`: robotics safety and controls team.
   - `Goal`: make learned planner proposals conditional on both statistical evidence and formal/runtime constraints.
   - `Core mechanism`: require PAC perception-risk bounds, fresh state, feasible CBF/QP constraints, bounded solve time, and ready fallback before action release.
   - `Required inputs`: calibrated perception scores, state age, constraint margins, solver status, fallback health, risk budget.
   - `Outputs`: learned action or safe fallback, with an assumption and evidence trace.
   - `Risk controls`: simulator-only MVP, hard deadlines, fallback-first behavior, supervised testing, no physical deployment claim.
   - `Evaluation`: violations, missed deadlines, fallback success, interval coverage, and assumption-breach detection.

## Three Ways to Exercise This Research

1. `Synthetic interval coverage lab`: Objective: verify finite-sample coverage across known Bernoulli bins. Inputs: seeded synthetic bin probabilities and sample sizes. Method: generate repeated calibration samples, compute intervals, and measure simultaneous coverage. Output: coverage-versus-width report. Success criterion: observed coverage meets the declared target within a pre-registered tolerance. Stop condition: reject the implementation if any parameter regime undercovers. Safety boundary: synthetic data only.
2. `Early-exit replay benchmark`: Objective: test the error-speed decision mechanism without production traffic. Inputs: public or approved classifier logits, labels, and measured branch runtimes. Method: split bin selection/calibration/test data, choose thresholds from intervals, and replay decisions across seeds. Output: error, MAC, p50/p95/p99 latency, interval width, and abstention curves. Success criterion: every reported speed point includes verified error coverage and versioned inputs. Stop condition: do not generalize beyond the tested distribution. Safety boundary: offline replay only.
3. `Shift-and-fallback drill`: Objective: verify fail-closed behavior when calibration evidence becomes stale. Inputs: synthetic corruptions or approved shifted slices, a shift signal, and a stub fallback. Method: inject shifts, confirm automation pauses, recalibrate on a separate approved set, and rerun coverage tests. Output: alarm delay, unsupported decisions prevented, fallback load, and recovery evidence. Success criterion: no decision is released while shift or fallback gates are invalid. Stop condition: halt if labels, rights, or fallback capacity are insufficient. Safety boundary: no physical actuation or consequential user action.

## Example MVP Product

- `Product name`: CoverageGate.
- `Target user`: ML evaluation engineers and safety reviewers deploying classifiers behind a human or verified fallback.
- `Problem`: Raw confidence and average calibration metrics do not show whether a particular decision threshold has adequate finite-sample support.
- `Core workflow`: import versioned scores and labels; validate split/data manifests; construct fixed or pre-approved bins; compute simultaneous confidence intervals; test coverage on a separate holdout; attach shift and fallback status; export an allow/review/reject decision card.
- `Data requirements`: public, synthetic, or governance-approved calibration labels; score-bin assignments; slice metadata with minimum counts; runtime aggregates; shift metrics; no raw secrets or unnecessary personal data.
- `Architecture`: local/offline batch CLI, immutable input manifest, deterministic interval engine, coverage test runner, shift/fallback adapters, Markdown/JSON evidence exporter, and human approval step.
- `Success metrics`: declared simultaneous coverage, interval width, abstention/review load, per-slice false-negative rate, zero unsupported automated decisions, deterministic reruns, and complete provenance.
- `Risk controls`: offline-only MVP; allowlisted inputs; minimum bin support; calibration/test separation; fail-closed shift and fallback checks; no physical actuation; no medical, legal, financial, or punitive decisions.
- `Limitations`: cannot prove end-to-end safety, cannot solve unknown shift, inherits label error, may be conservative, and depends on representative calibration data.
- `MVP boundary`: confidence evidence and decision-card generation only; no model training, data acquisition, online control, or automatic threshold deployment.
- `Deployment model`: local CLI or notebook in an approved evaluation environment.
- `Evaluation plan`: seeded unit tests against known binomial cases, coverage simulations, split-leakage checks, corruption drills, and independent review of exported assumptions.
- `Failure modes`: sparse bins, contaminated calibration data, adaptive-bin leakage, correlated samples, mislabeled slices, stale shift thresholds, unavailable fallback, and human-review overload.
- `Maintenance plan`: version interval methods, refresh calibration only through approved manifests, monitor coverage and abstention, and require re-review after model/data/threshold changes.

## Related Research and Reading

Exactly three DEP entries were selected for synthesis:

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| RRT-CBF Motion - DEP-E | Related Black Lake DEP | Connects learned motion planning to explicit barrier constraints and exposes state, solver, latency, dynamics, and fallback assumptions that remain outside classifier calibration | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md |
| HSD FTI-FDet - DEP-E | Related Black Lake DEP | Supplies a resource-constrained visual safety setting where compact inference needs calibrated abstention, per-component risk, shift testing, and human escalation | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260712-HSD%20FTI-FDet/hsd_fti_fdet_manuscript.md |
| CausalTAD Trajectory - DEP-E | Related Black Lake DEP | Supplies an OOD anomaly-detection setting that tests the paper's on-distribution boundary and motivates shift-aware calibration and review thresholds | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260711-CausalTAD%20Trajectory/causaltad_trajectory_manuscript.md |

Additional primary or near-primary reading:

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| PAC Confidence Predictions for Deep Neural Network Classifiers | Primary reviewed paper | Main interval construction and applications | https://arxiv.org/abs/2011.00716 |
| ICLR 2021 OpenReview record | Official venue record | Publication and peer-review venue context | https://openreview.net/forum?id=Qk-Wq5AIjpq |
| On Calibration of Modern Neural Networks | Primary baseline paper | Temperature scaling and ECE context used by the reviewed paper | https://proceedings.mlr.press/v70/guo17a.html |
| Conformal prediction under covariate shift | Primary related paper | Shift-aware coverage direction cited in the reviewed limitation discussion | https://arxiv.org/abs/1904.06019 |
| A Kernel Two-Sample Test | Primary related paper | Distribution-shift detection direction cited in Appendix F.1 | https://jmlr.org/papers/v13/gretton12a.html |

Synthesis: the reviewed paper supplies finite-sample decision bounds; HSD FTI-FDet supplies the efficient visual-inference target; CausalTAD supplies the distribution-shift and threshold-governance challenge; RRT-CBF Motion supplies the formal constraint and fallback layer. This is reviewer synthesis, not a jointly validated architecture.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2011.00716 | Paper identity, metadata, abstract, version navigation | 2026-07-13 | Primary arXiv record |
| R2 | https://arxiv.org/pdf/2011.00716 | Full method, theorems, results, appendices, limitations | 2026-07-13 | Primary v5 PDF; private copy inspected but not deposited |
| R3 | https://arxiv.org/html/2011.00716 | Full-text and numerical cross-check | 2026-07-13 | Public arXiv rendering |
| R4 | https://doi.org/10.48550/arXiv.2011.00716 | Stable paper identifier | 2026-07-13 | DOI resolver |
| R5 | https://openreview.net/forum?id=Qk-Wq5AIjpq | ICLR 2021 poster status, authors, abstract, dates | 2026-07-13 | Official venue record |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md | Safe-planning and system-boundary synthesis | 2026-07-13 | Related DEP 1 of 3 |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260712-HSD%20FTI-FDet/hsd_fti_fdet_manuscript.md | Efficient visual inference and calibrated escalation synthesis | 2026-07-13 | Related DEP 2 of 3 |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260711-CausalTAD%20Trajectory/causaltad_trajectory_manuscript.md | OOD, shift, and anomaly-threshold synthesis | 2026-07-13 | Related DEP 3 of 3 |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Target repository deposition rules | 2026-07-13 | Live default-branch authority |
| R10 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository layout and dedup context | 2026-07-13 | Live default-branch authority |
| R11 | https://proceedings.mlr.press/v70/guo17a.html | Calibration baseline context | 2026-07-13 | Near-primary related reading; not used for reviewed-paper metrics |
| R12 | https://arxiv.org/abs/1904.06019 | Covariate-shift coverage direction | 2026-07-13 | Related reading cited by reviewed paper |
| R13 | https://jmlr.org/papers/v13/gretton12a.html | Shift-detection direction | 2026-07-13 | Related reading cited by reviewed paper |
| R14 | This manuscript, Appendix | Random selection, dedup, extraction, and validation record | 2026-07-13 | Public-safe process evidence |

## Appendix

### Public-Safe Selection and Dedup Record

- Enumeration command family: `rg --files -g "*.pdf"` against the private archive root.
- Candidate PDFs: 75,761.
- Unique parent-directory paper units: 75,761.
- Random selection: uniform `Get-Random` draw, zero-based index 22,891.
- Selected identifier: arXiv:2011.00716.
- Selected title: PAC Confidence Predictions for Deep Neural Network Classifiers.
- Dedup keys: arXiv ID, DOI, normalized title, and `PAC-Confidence` slug.
- Scan locations: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and Black-Lake-Data.
- 24-hour marker window: evaluated through the public-safe cutoff date 2026-07-12.
- Duplicate exclusions: 0.
- Reselections: 0.
- Outcome: eligible on the first random draw.

### Extraction Record

- Extractor preflight order: pdftotext, fitz, pypdf, PyPDF2, pdfminer, HTML, source package.
- Selected extractor: pypdf; pdftotext was unavailable.
- PDF result: complete text extraction from the 27-page paper.
- Local HTML: unavailable.
- Local source package: unavailable.
- Public HTML: inspected through the arXiv rendering.
- Cache status: partial because PDF text succeeded while local HTML/source-package text was absent.
- Public-deposit policy: no cache file, PDF, source package, or local path is included.

### Replication Checklist

- [ ] Pin paper revision, dataset manifest, ResNet101 weights, preprocessing, and branch architecture.
- [ ] Separate bin selection, calibration, and final test data.
- [ ] Reimplement Clopper-Pearson edge cases and simultaneous `delta/K` accounting with unit tests.
- [ ] Reproduce reliability diagrams, ECE intervals, and sample-size ablations across multiple seeds.
- [ ] Reproduce the cascade threshold search and report error, MACs, p50/p95/p99 latency, and energy.
- [ ] Reproduce AI Habitat rollout construction, recoverability labels, unsafe-state definitions, and fallback behavior.
- [ ] Stress covariate, label, prevalence, corruption, and sensor-quality shifts.
- [ ] Verify fail-closed behavior when shift, state freshness, solver, or fallback gates fail.
- [ ] Report negative results and any parameter regime with empirical undercoverage.
- [ ] Keep all production or physical-system claims out of scope until independently reviewed.

### Source Inventory

- Primary source inspected: private archived PDF corresponding to arXiv:2011.00716v5; local location withheld.
- Public primary sources: arXiv abstract, PDF, HTML, DOI resolver, and OpenReview record.
- Related repository sources: exactly three Black Lake DEP manuscripts listed in `## Related Research and Reading`.
- Deposited source files: none.
