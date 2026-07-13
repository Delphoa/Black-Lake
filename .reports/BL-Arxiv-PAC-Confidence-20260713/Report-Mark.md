# Report-Mark: PAC Confidence Predictions

Public-safe run date: 2026-07-13

## Source Metadata

| Field | Value |
|---|---|
| Paper | PAC Confidence Predictions for Deep Neural Network Classifiers |
| Authors | Sangdon Park, Shuo Li, Insup Lee, Osbert Bastani |
| Identifier | arXiv:2011.00716v5; DOI: 10.48550/arXiv.2011.00716 |
| Venue | ICLR 2021 Poster |
| Initial submission / inspected revision | 2020-11-02 / 2021-03-17 |
| Primary sources | https://arxiv.org/abs/2011.00716; https://arxiv.org/pdf/2011.00716; https://arxiv.org/html/2011.00716 |
| Venue record | https://openreview.net/forum?id=Qk-Wq5AIjpq |
| Source handling | A private archived PDF and its extracted text were inspected. No source file was copied into this public deposit because redistribution terms were not independently assessed. |
| Evidence boundary | The paper, appendices, tables, figures/captions, arXiv metadata, and OpenReview metadata were inspected; experiments and proofs were not independently reproduced. |

## Concise Research Notes

**Problem.** Modern DNN classifiers often emit overconfident softmax scores. Standard calibration methods can improve average reliability but do not, by themselves, supply finite-sample coverage guarantees for the confidence attached to a particular prediction bin. The paper targets safety-critical decision systems that must know when to use a prediction, defer to a slower model, or activate a safe fallback.

**Method.** The authors partition top-label confidence into `K` histogram bins. Within each bin, correct versus incorrect predictions on a held-out calibration set become Bernoulli observations. A two-sided Clopper-Pearson interval estimates the bin's true correctness probability, and a `delta/K` allocation plus a union bound yields simultaneous PAC coverage over all bins. The output is an interval-valued confidence predictor, not a point calibration score. The authors then derive threshold-selection procedures for a cascading fast/slow DNN and for a perception-based planning shield.

**Evidence and results.** On ImageNet with ResNet101, 20,000 calibration images, 10,000 test images, and 20 bins, the paper reports ECE values of 4.79% for naive softmax, 1.66% for temperature scaling, and 0.99% for the proposed histogram-based point estimate; the proposed interval construction contains empirical accuracy in every shown bin and induces an ECE interval of `[0.0%, 3.76%]`. In the fast-inference experiment, the rigorous cascade reports 23.26% top-1 error versus 22.32% for the slow network, 5.33e9 versus 7.83e9 MACs, and 85.58 versus 214.31 microseconds on CPU. The paper summarizes this as a 32% MAC improvement and 54% runtime improvement while remaining within its desired relative-error bound. In AI Habitat safe planning, the rigorous threshold meets the tested safety-rate target while naive thresholds sometimes fail; success is deliberately sacrificed because the underlying learned policy is safe in only about 30% of rollouts.

**Limitations.** The guarantees assume the calibration and test distributions are identical. They do not cover adversarial examples, unknown covariate shift, sim-to-real transfer, misspecified safe-state or dynamics models, stale observations, or unverified fallback behavior. Clopper-Pearson intervals can be conservative, especially in sparse bins, and binning introduces a resolution-versus-sample-size tradeoff. Reported empirical results are single-paper evidence without an independent rerun, repeated-seed uncertainty, latency tails, or a production safety case.

**Implementation relevance.** The most useful pattern is not “confidence equals safety.” It is a decision gate whose lower or upper confidence bound is compared with an explicit risk budget, with abstention/fallback as a first-class output. This pattern can harden compact visual inspection systems, trajectory anomaly triage, and motion-planning shields, provided shift monitoring, calibration-data governance, fallback verification, and end-to-end assumption audits remain separate gates.

**Reviewer interpretation.** The paper makes a strong conceptual move from point calibration to interval-backed decisions and usefully traces that move into two downstream systems. Its theorem statements are conditional certificates. The practical research opportunity is to preserve that conditionality in telemetry: log bin support, interval width, shift status, fallback availability, and the exact risk budget for every release.

## Evidence and Attribution

| Evidence ID | Inspected evidence | Supports | Confidence and caveat |
|---|---|---|---|
| E1 | arXiv metadata and v5 full text | Identity, authors, revision, method, theorems, experiments, limitations | High for transcription; no independent proof audit |
| E2 | Sections 2-4 and Appendices A-E | Clopper-Pearson histogram construction and downstream error/safety bounds | High for author formulation; conditional on stated distributions and system models |
| E3 | Figures 2-4, Table/Figure 3(c), Sections 5.1-5.3 | ECE, error, MAC, latency, safety, and success claims | High for transcription; low for reproduction |
| E4 | Appendix F.1 | On-distribution boundary and shift directions | High; directly disclosed by authors |
| E5 | OpenReview ICLR 2021 record | Venue, authors, poster status, abstract, publication date | High for venue metadata |
| E6 | Three related DEP manuscripts | Safe-planning, compact-inference, and OOD synthesis | Medium; contextual evidence does not validate the paper |

Source claims are attributed to the authors. Reviewer synthesis and implementation suggestions are labeled as interpretation or proposal. No source code, model, dataset, or benchmark run was inspected, so availability and reproducibility are not inferred.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` — selected because it combines learned or model-based planning with explicit safety constraints and emphasizes that solver latency, stale state, perception error, and fallback behavior sit outside a mathematical barrier claim. Basis: inspected executive summary, boundary conditions, considerations, and source references grounded in arXiv:2410.00343.
2. `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` — selected because it studies compact visual fault detection under deployment constraints and explicitly identifies calibration, per-component false negatives, shift, and fail-safe escalation as missing safety evidence. Basis: inspected method/results tables, limitations, implementation notes, and sources grounded in arXiv:2307.00701 and its publisher record.
3. `.lake-data/DEP-E/DEP-E-20260711-CausalTAD Trajectory/causaltad_trajectory_manuscript.md` — selected because it targets out-of-distribution trajectory anomaly detection, the precise regime where PAC confidence coverage no longer transfers automatically, and calls for calibrated decision thresholds. Basis: inspected causal formulation, ID/OOD result tables, static-confounder limitation, official repository notes, and sources grounded in arXiv:2412.18820.

## Synthesis Note

### Concept Bridge

PAC confidence intervals provide an evidence-bearing interface between a predictor and a downstream decision: a compact detector may be trusted only when the lower correctness bound clears an acceptance threshold; an anomaly score may trigger review only after distribution-shift and calibration checks; and a planner may use a learned proposal only when an upper risk bound fits within a verified fallback envelope. HSD FTI-FDet supplies the edge-inference pressure, CausalTAD supplies the OOD and threshold-governance pressure, and RRT-CBF supplies the system-level safety boundary. Together they suggest a layered design in which statistical confidence, shift detection, constraint enforcement, and safe fallback are independent controls with separate evidence.

### Potential Implementations

1. **PAC-gated rail inspection:** calibrate each component class and site slice, accept only detections whose lower correctness bound exceeds a class-specific threshold, and route the rest to a human review queue.
2. **Shift-aware trajectory triage:** attach calibration intervals to anomaly-score strata, freeze automated thresholds when road/time distributions drift, and require review until a new representative calibration set is approved.
3. **Confidence-bounded motion shield:** admit learned planner proposals only when perception-risk bounds, state freshness, CBF feasibility, and fallback availability all pass their respective gates.

### Deeper Relationship Observations

1. All four works expose a separation between model quality and decision quality: high average accuracy, AUC, or path success does not define a safe operating threshold.
2. The strongest guarantees depend on interfaces—calibration set to confidence interval, confidence interval to action threshold, and action threshold to fallback—so interface telemetry is as important as model telemetry.
3. Distribution shift is a common failure multiplier: it invalidates PAC transfer, changes anomaly baselines, changes visual fault prevalence, and can move robot states outside the planner's verified envelope.

### Conceptual Similarities

1. Each system transforms uncertain learned output into a bounded decision rather than treating a raw score as authoritative.
2. Each benefits from abstention or fallback as an explicit system state instead of forcing a prediction or action.
3. Each needs slice-aware evaluation because aggregate metrics can hide sparse bins, rare faults, unseen routes, or difficult planning states.

### MVP Implementations with Code Mock-Ups

1. **Calibrated edge-inspection gate.** A lower interval bound controls acceptance; sparse or uncertain bins defer to review.

```python
def inspect_gate(bin_record: dict, min_correctness: float = 0.995) -> str:
    if bin_record["count"] < 30:
        return "human_review"
    return "accept" if bin_record["lower_cp"] >= min_correctness else "human_review"
```

2. **Shift-aware recalibration lock.** A public-safe aggregate shift signal disables automated decisions before coverage is re-estimated.

```python
def release_mode(shift_score: float, shift_limit: float, coverage_ok: bool) -> str:
    if shift_score > shift_limit or not coverage_ok:
        return "review_only"
    return "calibrated_triage"
```

3. **Layered planner shield.** Statistical risk is necessary but not sufficient; freshness, constraint feasibility, and fallback readiness are co-gates.

```python
def shield(p_risk_upper, budget, state_fresh, cbf_feasible, fallback_ready):
    safe_to_propose = p_risk_upper <= budget and state_fresh and cbf_feasible
    return "learned_action" if safe_to_propose and fallback_ready else "safe_fallback"
```

### Developer Challenges

1. Build a versioned calibration service that exposes bin counts, interval widths, coverage tests, and abstention load without logging sensitive examples.
2. Prove through tests that shift alarms, stale state, solver infeasibility, or unavailable reviewers always fail closed at the orchestration layer.
3. Report end-to-end latency tails and decision-risk slices, not only mean model latency or aggregate accuracy.

### Author Challenges

1. Extend PAC confidence prediction to detected or bounded covariate shift with finite-sample accounting for density-ratio estimation error.
2. Compare exact Clopper-Pearson intervals with less conservative simultaneous-coverage methods under sparse, adaptive, and class-imbalanced bins.
3. Release a pinned reproduction package that ties theorem parameters, dataset splits, thresholds, runtime measurements, and safety-planning assumptions to executable experiments.

## Validation Notes

- Random selection used all 75,761 PDF parent-directory paper units and uniform zero-based index 22,891; randomness was produced by `Get-Random`, not manual choice.
- Dedup searched Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and Black-Lake-Data by arXiv ID, DOI, normalized title, and slug. Exclusions and reselections were both zero; no same-paper marker was found within the 24-hour window evaluated through 2026-07-12.
- The private extraction cache used pypdf on the 27-page PDF. Local HTML and source packages were unavailable; public arXiv HTML supplied an independent full-text view.
- Quantitative claims were cross-checked between extracted PDF text and public arXiv HTML. No experimental rerun or proof rederivation was performed.
- The three related entries were selected for distinct, concrete overlap: formal safe planning, efficient safety-critical visual inference, and OOD/shift-aware thresholding.
- No source files were deposited. Public URLs and a withheld-local-source note preserve provenance without exposing local context.
- Submission gates require schema validation, exact-count checks, code syntax checks, repository-relative path review, and a scan for local paths, usernames, timezone labels, and precise local timestamps.

## Attribution Block

- Source URL: https://arxiv.org/abs/2011.00716
  - Applies to: source identity, authors, abstract, arXiv history, and public full-text navigation.
  - Notes: Primary arXiv record for the reviewed paper.
- Source URL: https://arxiv.org/pdf/2011.00716
  - Applies to: method, theorems, experimental tables/figures, conclusions, and Appendix F.1 limitations.
  - Notes: Primary arXiv v5 PDF; a private archive copy was inspected but not deposited and its local path is withheld.
- Source URL: https://arxiv.org/html/2011.00716
  - Applies to: cross-check of full-text claims, numerical results, and limitation language.
  - Notes: Public arXiv HTML rendering.
- Source URL: https://doi.org/10.48550/arXiv.2011.00716
  - Applies to: stable paper identification.
  - Notes: DOI resolver for the arXiv work.
- Source URL: https://openreview.net/forum?id=Qk-Wq5AIjpq
  - Applies to: ICLR 2021 poster status, authors, abstract, keywords, and venue dates.
  - Notes: Official venue record.
- Repository file: `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md
  - Applies to: formal safe-planning and system-boundary synthesis.
- Repository file: `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HSD%20FTI-FDet/hsd_fti_fdet_manuscript.md
  - Applies to: efficient visual inference, calibration, and fail-safe inspection synthesis.
- Repository file: `.lake-data/DEP-E/DEP-E-20260711-CausalTAD Trajectory/causaltad_trajectory_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-CausalTAD%20Trajectory/causaltad_trajectory_manuscript.md
  - Applies to: OOD, shift monitoring, anomaly threshold, and calibration synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: repository layout, DEP-E naming, README, attribution, and commit standards.
  - Notes: Live repository authority inspected before writing.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: related-repository dedup and provenance context.
  - Notes: Live related-repository authority inspected before relying on its search scope.
