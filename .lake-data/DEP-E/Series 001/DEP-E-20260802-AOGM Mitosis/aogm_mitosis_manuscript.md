---
title: "AOGM Mitosis - DEP-E"
generated_at: "2026-08-02"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of AOGM validity for mitosis-aware cell tracking evaluation."
source_status: "complete local PDF and full-paper HTML verified; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-02"
temporal_cutoff: "arXiv:2012.12084v1 submitted 2020-12-22; repository context inspected 2026-08-02"
primary_url: "https://arxiv.org/abs/2012.12084"
stable_identifier: "arXiv:2012.12084v1; DOI 10.48550/arXiv.2012.12084"
confidence_summary: "High for source identity, document integrity, and transcription of the reported score reversals; medium for generality because the empirical evidence centers on one video and heuristic linkage; low for reproduction because no code or dataset was rerun."
safety_scope: "offline research evaluation, synthetic graph testing, calibration audit, and bounded review planning"
distribution_notes: "No PDF, HTML, metadata page, source archive, extracted text, cache, local path, patient data, or private execution detail is redistributed."
---

# AOGM Mitosis - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:2012.12084v1; DOI 10.48550/arXiv.2012.12084 | https://arxiv.org/abs/2012.12084 | Metadata and public source locators | 2026-08-02 | Inspected |
| S2 | Complete paper | Primary artifact | PDF and full-paper HTML | v1; six pages | https://arxiv.org/pdf/2012.12084 and https://ar5iv.labs.arxiv.org/html/2012.12084 | Verified local copies withheld | 2026-08-02 | Inspected in full |
| S3 | Official full-paper locator | Primary source locator | HTML | arXiv HTML endpoint | https://arxiv.org/html/2012.12084 | Official endpoint attempted; approved fallback used for verified full text | 2026-08-02 | Inspected as locator |
| S4 | Source package | Primary artifact | TeX/source archive | arXiv:2012.12084 | https://arxiv.org/e-print/2012.12084 | Unavailable in repair; no source archive deposited | 2026-08-02 | Unavailable |
| S5 | OMGEval Benchmark - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260717 | `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md` | Repository synthesis context only | 2026-08-02 | Inspected |
| S6 | Judge Conformal - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md` | Repository synthesis context only | 2026-08-02 | Inspected |
| S7 | PAC Confidence - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260713 | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Repository synthesis context only | 2026-08-02 | Inspected |
| S8 | Black Lake governance | Deposition authority | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md and https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Filing, public-source, and index rules | 2026-08-02 | Inspected live |
| S9 | Black-Lake-Data governance | Companion authority | Markdown | live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related-context source boundary | 2026-08-02 | Inspected live |

Paper/work metadata:

- `Full title`: Limitation of Acyclic Oriented Graphs Matching as Cell Tracking Accuracy Measure when Evaluating Mitosis.
- `Authors`: Ye Chen; Yuankai Huo.
- `Initial submission`: 2020-12-22.
- `Subjects`: Computer Vision and Pattern Recognition; Image and Video Processing; Quantitative Methods.
- `Source files`: validated PDF, full-paper HTML, and metadata HTML were inspected locally and withheld; the source package was unavailable.
- `Public source policy`: no `.source/` directory, source document, extraction cache, or local path is included.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Official metadata | Title, authors, v1 status, date, subject categories, DOI, abstract, and locators | Source identity and scope | High | Metadata is not result evidence |
| E2 | S2-S3, Introduction and Methods | Primary paper | MOT/cell-tracking distinction, AOGM purpose, graph-edit components, and weights | Problem and mechanism | High for transcription | Method is source-reported; not independently formalized here |
| E3 | S2, Figure 1 and surrounding text | Primary paper and visual evidence | Cases where added mitosis links increase AOGM despite meaningful event structure | Metric-validity counterexample | High for visual/text interpretation | No independent graph calculation |
| E4 | S2, Figure 2 and Simulation | Primary paper and visual evidence | Seven mitosis events, shared vertices, and AOGM `124.5` without links versus `133.5` with links | Simulation result | High for transcription | Not rerun |
| E5 | S2, Figure 3 and Empirical Validation/Results | Primary paper and visual evidence | FairMOT baseline, one video, three mitosis events, and score pairs `4/4.5`, `15/16`, `24.5/25.5` | Empirical result | High for transcription | One video, one baseline, heuristic linkage |
| E6 | S2, Conclusions | Primary paper | Suggestion to modify AOGM or add mitosis precision/recall | Follow-on direction | High for transcription | Replacement not evaluated |
| E7 | S5-S7 | Related DEP artifacts | Measurement envelope, calibration, interval uncertainty, shift, abstention, and fallback concepts | Cross-DEP synthesis | Medium | Conceptual relation; no joint experiment |
| E8 | S8-S9 and process records | Governance/process evidence | Random draw, dedup scan, repair gate, public output, source withholding, and index maintenance | Deposition compliance | High | Operational evidence, not paper evidence |

## Executive Summary

The paper argues that AOGM, a graph-edit metric for cell tracking, can rank a mitosis-aware prediction worse than a prediction that omits the mitosis links. This matters because cell division is a domain event that generic multi-object tracking metrics do not naturally encode. AOGM is intended to reward a graph that matches reference vertices and temporal relationships, but its fixed costs for extra or missing edges can make a meaningful mother-daughter linkage increase the lower-is-better score.

The authors support the claim with a simulated seven-event graph and an empirical check on one ISBI Cell Tracking Challenge video using FairMOT plus a simple linkage post-processing rule. The reported simulation scores are `124.5` without mitosis links and `133.5` with links. The three empirical event comparisons also favor no links by AOGM: `4` versus `4.5`, `15` versus `16`, and `24.5` versus `25.5`. These are author-reported values, not independently reproduced results.

The durable research lesson is not that AOGM should be discarded. It is that a metric needs a validity envelope: the score must be checked against event-level behavior, uncertainty, slice support, and shift conditions before it controls a benchmark ranking or release decision. The three related DEP entries provide complementary patterns for that envelope: OMGEval emphasizes construct and judge coverage, Judge Conformal turns point scores into calibrated intervals, and PAC Confidence makes support, distribution assumptions, abstention, and fallback explicit.

## Detailed Summary

### Problem Context

Multi-object tracking detects objects and associates them across frames. Cell tracking shares that structure but adds mitosis, where a mother cell can produce daughter cells, plus domain-specific events such as delayed daughter appearance, disappearance, collision, and merge. The paper frames this difference as a reason that standard MOT metrics such as MOTA, ID switches, and IDF1 are not sufficient for cell tracking.

### AOGM Mechanism

AOGM is presented as a weighted sum of false-negative vertices (`FN`), false-positive vertices (`FP`), missed splits (`NS`), redundant edges (`ED`), missing edges (`EA`), and edges with wrong semantics (`EC`):

`AOGM = w_NS NS + w_FN FN + w_FP FP + w_ED ED + w_EA EA + w_EC EC`.

The paper lists `w_NS=5`, `w_FN=10`, `w_FP=1`, `w_ED=1`, `w_EA=1.5`, and `w_EC=1.5`. The authors use these costs to show how an added linkage can incur edge penalties that outweigh the semantic benefit of connecting a mother and daughter.

### Simulation

The simulation uses a reference graph with seven mitosis events from `t0` to `t9` and compares two computed graphs with the same number of vertices. One graph leaves mitosis links out; the other adds cell-level mitosis links. Because the vertex and split counts are held constant, the reported difference comes from edge terms. The paper reports AOGM `124.5` without links and `133.5` with links, then interprets the higher score as an inversion of the desired ranking.

### Empirical Validation

The empirical setting uses the `Fluo-N2DH-GOWT1-01` video from the ISBI Cell Tracking Challenge. The paper describes 91 frames and three mitosis events. FairMOT is adapted for detection and tracking, then a simple post-processing rule links a newly appearing cell or cells to a recently disappeared cell when the temporal and center-point conditions are met. In the displayed results, adding mitosis links increases AOGM for all three events: `4` to `4.5`, `15` to `16`, and `24.5` to `25.5`.

### Limitations and Interpretation

The empirical evidence is narrow: one video, one tracking baseline, and one heuristic linkage rule. The paper demonstrates a failure mode, but it does not compare a replacement metric across multiple datasets or quantify the trade-off between graph fidelity and event utility. It suggests modified AOGM or complementary mitosis precision and recall, leaving the design and validation of those alternatives open.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Cell tracking needs evaluation that represents mitosis, not only generic object association. | Author problem claim | E1-E2 | Directly supported by the paper's task comparison and framing. | High |
| C2 | AOGM is a weighted graph-edit metric with explicit vertex, split, and edge costs. | Author method claim | E2 | Formula and weights are visible in the Methods section. | High for transcription |
| C3 | In the paper's simulation, adding meaningful mitosis links raises AOGM from `124.5` to `133.5`. | Author-reported result | E3-E4 | Directly supported by Figure 2 and surrounding text; not independently rerun. | High for transcription |
| C4 | In the displayed empirical examples, linked results score worse than unlinked results. | Author-reported result | E5 | Supported by Figure 3 and Results; generality beyond the shown video is not established. | High for transcription; medium for generality |
| C5 | AOGM is invalid for all cell-tracking evaluation. | Unsupported generalization | No evidence for universal invalidity | Rejected; the paper establishes a failure mode, not total invalidity. | High rejection confidence |
| C6 | Metric validity should be paired with event quality, uncertainty, support, and shift checks. | Reviewer interpretation | E3-E8 | A synthesis hypothesis grounded in the counterexample and related DEP patterns. | Medium |
| C7 | A public full-paper source and local integrity pass prove reproducibility. | Unsupported implication | E1, E8 | Rejected; source completeness supports review provenance, not result reproduction. | High rejection confidence |

## Methodology

- `Research objective`: Preserve the selected paper's problem, mechanism, reported evidence, limitations, and safe implementation implications, then connect them to exactly three related DEP entries.
- `Sources inspected`: Official arXiv metadata, DOI locator, verified six-page PDF, verified full-paper HTML fallback, metadata HTML, local source-integrity companions, live Black Lake READMEs, and three related DEP manuscripts/README records.
- `Discovery strategy`: Enumerated local PDF candidates with `rg --files -g "*.pdf"`; collapsed parent directories to paper units; used uniform `Get-Random`; scanned live repository and automation-memory evidence for deduplication; repaired the selected source unit before review; inspected full text and rendered PDF pages; selected related DEPs by concrete evaluation overlap.
- `Random selection`: `75,960` PDF candidates; `75,957` unique parent-directory units; uniform zero-based index `9,254`; no manual substitution.
- `Deduplication and eligibility`: Live `Black-Lake/.logs`, `.reports`, `.lake-data`, automation memory, and related `Black-Lake-Data` context were searched for arXiv ID, DOI, normalized title, slug, automation markers, DEP-E entries, and 24-hour markers. Public cutoff was `2026-08-01`; exclusions `0`; reselections `0`.
- `Source-integrity gate`: The selected unit initially lacked full-paper HTML. A bounded single-paper repair preserved the valid PDF and acquired a verified full-paper fallback. Final gates required a PDF of at least 10 KB with `%PDF-` and `%%EOF`, and HTML of at least 5 KB with at least 2,000 body characters, a document marker, two heading markers, and two paper-structure terms. All passed; no partial files remained.
- `Inclusion criteria`: Primary paper sections, figures, formulas, results, conclusions, source metadata, and related DEP material with concrete overlap in metric validity, evaluation, calibration, uncertainty, shift, or abstention.
- `Exclusion criteria`: Abstract-only evidence, unsupported universal claims, source-file redistribution, unverified reproducibility, unsafe biomedical deployment, and related records without a clear conceptual bridge.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: Source claims, author-reported values, reviewer interpretations, derived proposals, and unsupported implications are labeled separately and mapped to evidence IDs.
- `Uncertainty handling`: The paper's narrow empirical scope, unavailable source package, lack of independent reproduction, metric reversal boundary, and related-DEP conceptual status remain explicit.
- `Artifact type`: DEP-ready research artifact combining a paper review, metric critique, cross-DEP synthesis, implementation brief, and bounded replication backlog.

## Scope, Constraints, and Assumptions

- `Scope`: AOGM's mitosis-related metric behavior, the selected paper's evidence, three related DEP evaluation patterns, and safe follow-on research design.
- `Temporal boundary`: Primary paper v1 submitted 2020-12-22; public repository and related DEP context inspected on 2026-08-02.
- `Evidence limits`: No source package, code execution, dataset access, metric reimplementation, or independent reproduction was completed. The empirical paper evidence centers on one video and one heuristic linkage setup.
- `Assumptions`: The arXiv record and DOI identify the reviewed version; public repository paths identify the related DEP manuscripts; the displayed score pairs are transcribed correctly from the paper.
- `Constraints`: Source files remain local; no patient data or biomedical control loop is created; any implementation must use authorized or synthetic data; benchmark scores must not be treated as clinical evidence.
- `Out of scope`: Clinical deployment, autonomous cell-tracking decisions, claims that AOGM is universally invalid, and legal or medical conclusions.
- `Intended use`: Research review, evaluation design, synthetic replication planning, and provenance-aware benchmark governance.
- `Reproducibility boundary`: The paper's full text and figures are inspectable; reproducing its results requires the original data, tracker configuration, linkage implementation, and metric code.

## Observations

- Metric design can create perverse rankings when edge costs do not reflect the semantics of eventful trajectories.
- A single scalar can hide which graph edits caused a score change; component-level reporting is necessary for diagnosis.
- The paper's use of one video and one heuristic linkage is enough to show a failure mode but not enough to establish prevalence.
- Related evaluation DEPs converge on a common pattern: support, calibration, judge agreement, and shift status should accompany the score.
- Source completeness and repository provenance improve auditability but do not substitute for a rerun.

## Considerations

Any follow-on evaluation should report both graph-edit fidelity and event fidelity. It should preserve video-level and cell-level splits, avoid leaking trajectories across calibration and test partitions, and record support counts for rare mitosis patterns. A review-only state is safer than an automatic acceptance when intervals are wide, calibration support is sparse, or acquisition shift is detected. If outputs influence medical research decisions, the system should remain nonbinding and include human review, provenance, access control, and rollback procedures.

## Strengths

- Identifies a concrete and intelligible metric reversal rather than making only an abstract criticism.
- Uses both a controlled graph simulation and a real-video example.
- Makes the AOGM components and weights visible enough for follow-on analysis.
- Connects the critique to a practical suggestion for modified AOGM or mitosis precision/recall.
- Provides a useful test case for broader benchmark and calibration governance.

## Weaknesses

- The empirical scope is one video and one tracker/linkage setup.
- The linkage rule is heuristic and may itself introduce the graph differences being measured.
- No replacement metric is defined, implemented, or compared across conditions.
- Results were not independently reproduced in this review.
- The source package was unavailable, and no executable artifact was verified.

## Potential Improvements

| Improvement | Target | Rationale | Validation approach |
|---|---|---|---|
| Event-aware companion metrics | Mitosis quality | Separate event detection from generic graph edits | Report precision, recall, missed/delayed daughter, merge, and split rates per slice |
| Component-level score reporting | Interpretability | Show which AOGM terms drive a ranking | Publish the full error vector and sensitivity to each weight |
| Multi-condition benchmark | Generality | Test whether reversals persist across video and cell conditions | Use versioned datasets with video/site/cell-level splits |
| Calibration and shift envelope | Decision safety | Prevent unsupported scores from controlling acceptance | Report support, interval width, distribution checks, and review load |
| Synthetic graph replication | Reproducibility | Make metric reversals easy to test without sensitive data | Release a small graph generator with fixed expected scores |

## Potential Implementations

1. **Event-aware metric dashboard.** Add mitosis precision/recall and delay-aware event utility beside AOGM, then require both graph and event thresholds for a release comparison.
2. **Calibration-backed score report.** Use a public or synthetic calibration set to produce uncertainty intervals for AOGM components and event metrics, including support counts and a review-only state.
3. **Shift-aware benchmark runner.** Evaluate per-video and per-condition slices, detect unsupported shifts, and stop automated ranking when calibration or reviewer capacity is insufficient.

## Three Ways to Exercise This Research

1. **Synthetic graph reproduction:** generate the paper's seven-event graph and confirm the reported direction of the `124.5` versus `133.5` comparison before testing alternative edge costs.
2. **Multi-slice metric audit:** compare AOGM, mitosis precision/recall, and delay-aware utility across authorized or synthetic slices for frame gaps, merges, density, and daughter timing.
3. **Calibration and abstention study:** estimate score intervals on a held-out calibration split, inject controlled shift, and measure coverage, ranking stability, abstention load, and reviewer utility.

## Example MVP Product

- `Product name`: Event-Aware Tracking Evaluation Gate.
- `Target user`: Cell-tracking researcher, benchmark maintainer, or biomedical-imaging evaluation reviewer.
- `Problem`: A single graph metric can reward a prediction that omits a meaningful mitosis event and can hide unsupported or shifted slices.
- `Core workflow`: Load an authorized versioned graph manifest, compute AOGM plus event metrics, attach support and uncertainty, run slice and shift checks, and emit `accept`, `review`, or `fallback` for nonbinding research comparison.
- `Data requirements`: Synthetic or authorized cell-tracking graphs, event labels, versioned split manifest, metric configuration, calibration records, and reviewer-capacity metadata; no patient-identifying data is required for the MVP.
- `Architecture`: Local graph loader, metric component calculator, event scorer, calibration/interval module, slice and shift analyzer, audit store, and review UI.
- `Success metrics`: Agreement with domain-preferred ranking, event recall/precision, interval coverage, ranking stability under perturbation, abstention/review load, reproducible run rate, and provenance completeness.
- `Risk controls`: Source and data authorization checks, local-only processing, no clinical control, human review for unsupported slices, fail-closed shift gates, immutable manifests, and rollbackable configurations.
- `Limitations`: The MVP cannot establish clinical validity, cannot replace expert review, and cannot assume that calibration transfers across microscopes, cell types, laboratories, or annotation policies.

## Related Research and Reading

| Item | Type | Relevance | Public locator / repository path |
|---|---|---|---|
| OMGEval Benchmark - DEP-E | Related DEP | Measurement envelope, construct coverage, localization, judge-human agreement, and benchmark governance | `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md`; source basis https://arxiv.org/abs/2402.13524 |
| Judge Conformal - DEP-E | Related DEP | Interval-valued evaluation, calibration, coverage, width, and review routing | `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md`; source basis https://arxiv.org/abs/2509.18658 |
| PAC Confidence - DEP-E | Related DEP | Finite-sample confidence, support limits, distribution shift, abstention, and fallback | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`; source basis https://arxiv.org/abs/2011.00716 |

The cross-DEP relationship is a reviewer synthesis, not a claim that the four papers share datasets, code, or experimental results. The selected paper supplies the metric-reversal case; the related DEPs supply adjacent design patterns for measurement envelopes and bounded decisions.

## Source References

| ID | Reference | Supports | Access date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2012.12084 | Identity, abstract, authors, date, subjects, and source links | 2026-08-02 | Primary metadata |
| R2 | https://arxiv.org/pdf/2012.12084 | Formula, weights, figures, simulation, empirical validation, results, and conclusion | 2026-08-02 | Verified local copy withheld |
| R3 | https://arxiv.org/html/2012.12084 | Official full-paper locator | 2026-08-02 | Endpoint attempted; not counted as the local fallback artifact |
| R4 | https://ar5iv.labs.arxiv.org/html/2012.12084 | Full-paper rendering used for section-level review | 2026-08-02 | Verified local copy withheld |
| R5 | https://doi.org/10.48550/arXiv.2012.12084 | Persistent paper identifier | 2026-08-02 | arXiv-issued DOI |
| R6 | `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md` | Benchmark measurement-envelope synthesis | 2026-08-02 | Public repository file; source basis https://arxiv.org/abs/2402.13524 |
| R7 | `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md` | Interval-valued evaluation and calibration synthesis | 2026-08-02 | Public repository file; source basis https://arxiv.org/abs/2509.18658 |
| R8 | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Finite-sample confidence, shift, and abstention synthesis | 2026-08-02 | Public repository file; source basis https://arxiv.org/abs/2011.00716 |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository layout and public-source rules | 2026-08-02 | Live authority |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication-index rules | 2026-08-02 | Live authority |
| R11 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository context | 2026-08-02 | Live authority |

## Appendix

- `Selection record`: `rg --files -g "*.pdf"`; `75,960` PDFs; `75,957` unique parent units; uniform zero-based index `9,254`; exclusions `0`; reselections `0`.
- `Source-integrity record`: initial partial due to missing full-paper HTML; bounded repair passed PDF and full-paper HTML gates; source package unavailable; no partial files remained.
- `Public-output record`: no PDF, HTML, metadata page, source archive, extracted text, cache, local path, or `.source/` directory was staged or uploaded.
- `Validation boundary`: schema and public-safety checks were performed; code, data, experiments, and metric calculations were not independently reproduced.
