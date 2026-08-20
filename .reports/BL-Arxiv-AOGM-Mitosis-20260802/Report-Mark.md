# Report-Mark: AOGM Mitosis Evaluation

- Public-safe run date: `2026-08-02`
- Paper: *Limitation of Acyclic Oriented Graphs Matching as Cell Tracking Accuracy Measure when Evaluating Mitosis*
- Identifier: `arXiv:2012.12084v1`; DOI `10.48550/arXiv.2012.12084`
- Authors: Ye Chen; Yuankai Huo
- Source state: complete local PDF and full-paper HTML verified after bounded repair; source files withheld from public outputs.

## Source Metadata

| Field | Value |
|---|---|
| Primary work | *Limitation of Acyclic Oriented Graphs Matching as Cell Tracking Accuracy Measure when Evaluating Mitosis* |
| Authors | Ye Chen; Yuankai Huo |
| arXiv record | [arXiv:2012.12084](https://arxiv.org/abs/2012.12084) |
| Version/date | v1; submitted 2020-12-22 |
| Subjects | Computer Vision and Pattern Recognition; Image and Video Processing; Quantitative Methods |
| DOI | [10.48550/arXiv.2012.12084](https://doi.org/10.48550/arXiv.2012.12084) |
| Primary paper locators | [PDF](https://arxiv.org/pdf/2012.12084); [official HTML locator](https://arxiv.org/html/2012.12084); [verified full-paper fallback](https://ar5iv.labs.arxiv.org/html/2012.12084) |
| Source package | Unavailable from the inspected archive repair; no source archive was deposited |
| Public source policy | PDF, full-paper HTML, metadata HTML, extraction cache, verification companions, and local paths remain withheld |
| Review evidence | Full six-page PDF, verified full-paper HTML, metadata page, and rendered page images were inspected; no experiment was rerun |

## Concise Research Notes

### Problem

The paper studies whether acyclic oriented graphs matching (AOGM), a graph-edit metric used in cell-tracking evaluation, measures mitosis-aware tracking quality in the way its lower-is-better score suggests. Generic multi-object tracking metrics do not naturally represent cell division, so AOGM is used to compare detected cell vertices and temporal edges with a reference graph. The authors identify cases where a correct cell-level mitosis linkage can receive a worse AOGM score than a prediction that omits the linkage.

### Method

The authors first explain AOGM as a weighted sum of false-negative vertices, false-positive vertices, missed splits, redundant edges, missing edges, and edges with wrong semantics. The weights transcribed in the paper are `w_NS=5`, `w_FN=10`, `w_FP=1`, `w_ED=1`, `w_EA=1.5`, and `w_EC=1.5`. They then use two evidence settings:

1. A simulated reference graph with seven mitosis events from `t0` to `t9`, compared with two predictions that keep the same vertices but differ in whether mitosis links are added.
2. An empirical check on the `Fluo-N2DH-GOWT1-01` video from the ISBI Cell Tracking Challenge, using a FairMOT-based detector/tracker and a simple post-processing linkage rule for likely mother-daughter cells.

### Evidence and results

In the simulation, the prediction without mitosis links has AOGM `124.5`, while the graph with cell-level consistent links has AOGM `133.5`. The paper interprets the larger score as a metric failure because the linked graph contains more meaningful mitosis structure. In the empirical figure, the three shown events likewise have lower scores without links than with links: `4` versus `4.5`, `15` versus `16`, and `24.5` versus `25.5`. These values are source-reported, not independently reproduced in this review.

### Limitations

The empirical study centers on one video and one detector/tracker baseline, and the linkage rule is a heuristic based on temporal proximity and center-point distance. The paper does not introduce or evaluate a replacement metric across multiple datasets, cell types, acquisition conditions, or error costs. The source package was unavailable in the archive repair, and no code, data, or result reproduction was performed for this run.

### Implementation relevance

The practical lesson is metric governance: a benchmark must test whether its score ordering agrees with the domain behavior that reviewers actually value. A cell-tracking evaluation should report graph-edit quality together with event-level detection quality, uncertainty or confidence intervals, slice coverage, and explicit review/fallback states. A lower scalar score should not be allowed to erase a clinically or scientifically meaningful event without an accompanying event-aware measure.

### Reviewer interpretation

The paper is strongest as a compact counterexample to metric validity. It does not show that AOGM is useless for every cell-tracking error; it shows that its fixed edge costs can reverse the intended ranking in particular mitosis configurations. The follow-on question is therefore not simply “which metric wins?” but “which set of metrics and uncertainty bounds preserves the desired ordering across the error modes that matter?”

## Evidence and Attribution

| Evidence ID | Inspected evidence | Supports | Confidence and caveat |
|---|---|---|---|
| E1 | arXiv metadata page and DOI record | Identity, authors, date, subject categories, v1 status, and public locators | High for source metadata |
| E2 | Full paper, Introduction and Methods | MOT/cell-tracking distinction, AOGM purpose, formula, and stated weights | High for transcription; author claim until independently checked |
| E3 | Full paper, Figure 1 and surrounding text | Examples where linked mitosis graphs receive larger scores | High for visual/text interpretation; no independent graph calculation |
| E4 | Full paper, Figure 2 and Simulation section | Seven-event simulation and AOGM `124.5` versus `133.5` comparison | High for source reporting; not rerun |
| E5 | Full paper, Figure 3 and Empirical Validation/Results | FairMOT setup, one video, three events, and score pairs `4/4.5`, `15/16`, `24.5/25.5` | High for source reporting; one dataset/video and heuristic linkage |
| E6 | Full paper, Conclusions | Proposal for modified AOGM or complementary mitosis precision/recall | High for source reporting; replacement not evaluated in the paper |
| E7 | Related DEP manuscripts | Benchmark measurement envelopes, interval-valued judging, PAC confidence, shift assumptions, and abstention patterns | Medium; contextual synthesis only, not validation of the selected paper |
| E8 | Black Lake live READMEs and process records | DEP filing, public-source, source-withholding, random-selection, and publication-index requirements | High for process compliance; not research evidence |

The selected paper is the primary evidence for all paper-specific claims. Related DEP entries are used only for conceptual synthesis. Source documents were inspected locally and withheld; no PDF, HTML, metadata page, source archive, extraction cache, or local path is redistributed.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md` ([public file](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md)) — selected because OMGEval treats benchmark validity as more than a single score: language/cultural localization, judge-human comparison, uneven capability categories, and limited coverage all define a measurement envelope. Basis: reviewed DEP README and manuscript, grounded in [arXiv:2402.13524](https://arxiv.org/abs/2402.13524).
2. `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md` ([public file](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260716-Judge%20Conformal/llm_judge_conformal_manuscript.md)) — selected because it converts a point judge score into an interval with calibration, coverage, width, and review-routing implications. That pattern is a direct conceptual candidate for uncertainty-aware graph and event metrics. Basis: reviewed DEP README and manuscript, grounded in [arXiv:2509.18658](https://arxiv.org/abs/2509.18658).
3. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` ([public file](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md)) — selected because its finite-sample confidence intervals, support-aware bins, distribution-shift boundary, abstention, and fallback logic show how a metric can become a bounded decision interface. Basis: reviewed DEP Report-Mark and manuscript, grounded in [arXiv:2011.00716](https://arxiv.org/abs/2011.00716).

## Synthesis Note

### Concept Bridge

The selected paper and the three related DEP entries share a measurement problem: a scalar score can look precise while failing to preserve the behavior a system owner actually cares about. AOGM makes graph edits measurable but can penalize a correct mother-daughter relationship. OMGEval shows that benchmark scores depend on construct coverage, localization, judge behavior, and human agreement. Judge Conformal adds interval-valued uncertainty to a point evaluation. PAC Confidence adds finite-sample support, shift assumptions, and abstention to a confidence signal.

Together they suggest a cell-tracking evaluation stack with four layers: an event-aware graph score, an independent event-quality score, an uncertainty/support envelope, and an operational decision state such as accept, review, or fallback. The bridge is conceptual rather than empirical: none of the related DEP entries has been jointly tested with AOGM in this run.

### Potential Implementations

1. **Event-aware dual scorecard.** Keep AOGM for graph-edit comparability, but report mitosis precision, mitosis recall, missed-split rate, delayed-daughter rate, and merge/split errors as separate dimensions. Require a release decision to pass both graph fidelity and event fidelity rather than selecting the lowest AOGM alone.
2. **Interval-valued tracking evaluation.** Use a versioned calibration set of annotated trajectories to estimate uncertainty bounds for AOGM components and event metrics. Report point estimates, interval width, support counts, and a review state; do not present a narrow score as a universal certificate.
3. **Shift-aware benchmark gate.** Partition evaluation by video, cell density, frame gap, mitosis pattern, and acquisition condition. Freeze automated acceptance when support is sparse or shift is detected, then route uncertain cases to human review or an explicitly verified fallback metric.

### Deeper Relationship Observations

1. **The ordering is the real contract.** A metric is useful only when its ranking of predictions matches domain priorities across relevant error modes. AOGM's counterexample, OMGEval's localization concerns, and the confidence DEP intervals all expose failures that are hidden by a single average.
2. **Uncertainty belongs at the interface.** Calibration, coverage, judge agreement, and support are not decorative metadata. They determine whether a score can safely drive a release, comparison, or review decision.
3. **Shift turns metric validity into a lifecycle problem.** A score can behave acceptably on one dataset and fail under new acquisition conditions, language/culture, model versions, or sparse event types. The benchmark therefore needs monitoring and recalibration, not only a one-time leaderboard.

### Conceptual Similarities

1. All four artifacts separate the measured signal from the decision made from that signal.
2. All four support slice-aware analysis because aggregate scores can hide rare or structurally different cases.
3. All four imply that abstention, human review, or a bounded fallback is preferable to forcing a misleadingly precise result.

### MVP Implementations with Code Mock-Ups

1. **Dual event-aware scorecard.** Preserve AOGM but block acceptance when event quality falls below its declared threshold.

```python
def release_tracking(aogm, mitosis_precision, mitosis_recall,
                     max_aogm, min_precision, min_recall):
    graph_ok = aogm <= max_aogm
    event_ok = (mitosis_precision >= min_precision and
                mitosis_recall >= min_recall)
    return "accept" if graph_ok and event_ok else "review"
```

2. **Support-aware interval gate.** Treat uncertainty width and calibration support as first-class release inputs.

```python
def metric_gate(lower, upper, support, min_support, min_lower):
    if support < min_support:
        return "review"
    return "accept" if lower >= min_lower else "review"
```

3. **Shift-aware evaluation mode.** Stop automatic acceptance when the evaluated slice is outside its validated support envelope.

```python
def evaluation_mode(shift_score, shift_limit, interval_width, width_limit):
    shifted = shift_score > shift_limit
    uncertain = interval_width > width_limit
    return "review_only" if shifted or uncertain else "automated_compare"
```

These snippets are bounded decision sketches, not validated biomedical software. They use no patient data, do not control a tracker, and require domain-specific calibration, testing, review, and governance before use.

### Developer Challenges

1. Build a versioned metric harness that computes AOGM, event-level scores, support counts, intervals, and slice reports from the same immutable graph inputs.
2. Test whether calibration remains valid under delayed daughters, missed splits, merges, frame gaps, density changes, and acquisition shifts without leaking labels across train/calibration/test partitions.
3. Make review and fallback states observable and fail closed when the metric envelope is unsupported, while keeping source provenance and privacy boundaries auditable.

### Author Challenges

1. Evaluate a modified or complementary AOGM across multiple Cell Tracking Challenge videos, cell types, and error regimes, with event-level precision/recall and ranking agreement as primary outcomes.
2. Add confidence intervals or bootstrap/conformal support analysis for graph and mitosis metrics, and report when sparse event counts make the ranking unstable.
3. Release a reproducible synthetic graph generator and public evaluation harness that lets future work test metric reversals, alternative edge costs, and clinically meaningful utility orderings.

## Validation Notes

- Random selection used `rg --files -g "*.pdf"`, `75,960` PDFs, `75,957` unique parent units, and uniform zero-based index `9,254`; the draw was produced by `Get-Random`, not manual choice.
- The initial source unit was partial because full-paper HTML was missing. A bounded brokered repair produced a verified full-paper fallback; the final PDF was `3,065,829` bytes and the full-paper HTML was `59,563` bytes with readable body text, document markers, headings, and six structural terms. No partial files remained.
- Dedup searched live Black Lake `.logs`, `.reports`, `.lake-data`, automation memory, and related Black-Lake-Data context by ID, DOI, normalized title, and slug. Exclusions and reselections were both zero; the public 24-hour cutoff was `2026-08-01`.
- The full six-page PDF and full-paper HTML were inspected, including Figures 1-3. No code, dataset, or metric reproduction was performed.
- Public-output allowlist and sanitization checks must cover only the generated log, Report-Mark, DEP README, DEP manuscript, and required publication-index row. No source files or `.source/` directory are included.

## Attribution Block

- Source URL: https://arxiv.org/abs/2012.12084
  - Applies to: paper identity, authors, version, subjects, abstract, DOI, and public source locators.
- Source URL: https://arxiv.org/pdf/2012.12084
  - Applies to: full paper, formula, figures, simulation, empirical validation, results, and conclusion.
  - Notes: Verified local PDF inspected; file withheld from the public repository.
- Source URL: https://arxiv.org/html/2012.12084
  - Applies to: official full-paper HTML locator and public source provenance.
  - Notes: The official HTML endpoint was attempted; the verified full-paper rendering used for the local integrity gate was the approved public fallback below.
- Source URL: https://ar5iv.labs.arxiv.org/html/2012.12084
  - Applies to: verified full-paper HTML rendering used for section-level review.
  - Notes: Local copy withheld; it is not treated as an abstract page.
- Source URL: https://doi.org/10.48550/arXiv.2012.12084
  - Applies to: persistent identification of the reviewed arXiv work.
- Repository file: `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md
  - Applies to: benchmark measurement-envelope synthesis; source basis https://arxiv.org/abs/2402.13524.
- Repository file: `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260716-Judge%20Conformal/llm_judge_conformal_manuscript.md
  - Applies to: interval-valued evaluation, calibration, coverage, and review-routing synthesis; source basis https://arxiv.org/abs/2509.18658.
- Repository file: `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md
  - Applies to: finite-sample confidence, support, shift, abstention, and fallback synthesis; source basis https://arxiv.org/abs/2011.00716.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: repository layout, public-source policy, DEP contents, logs, reports, and commit convention.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: DEP-E filing location, naming, README requirements, and publication-index maintenance.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: related-repository context and source-provenance boundary.
- Source files withheld: validated PDF, verified full-paper HTML, metadata HTML, source-integrity companions, and private extraction artifacts.
  - Applies to: all paper-specific notes and validation statements above.
  - Notes: No source file was uploaded, staged, committed, attached, or sent to Slack.
