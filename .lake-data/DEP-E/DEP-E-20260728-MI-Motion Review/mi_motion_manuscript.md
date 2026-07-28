---
title: "MI-Motion - DEP-E"
generated_at: "2026-07-28 (public-safe date)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of MI-Motion, a benchmark and SocialTGCN baseline for 3D multi-person motion prediction."
source_status: "verified complete local source bundle; original files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-28"
temporal_cutoff: "Paper version v2 and repository context inspected through the public-safe date."
primary_url: "https://arxiv.org/abs/2306.13566"
stable_identifier: "arXiv:2306.13566v2; DOI:10.48550/arXiv.2306.13566"
confidence_summary: "High for source identity and reported tables; medium for method transcription; low for unreplicated generalization and deployment claims."
safety_scope: "offline research, synthetic evaluation, and nonbinding decision support"
distribution_notes: "No PDF, HTML, source archive, cache, extraction, rendering, local path, or machine context is redistributed."
---

# MI-Motion - DEP-E

## Source Metadata

| Field | Value |
|---|---|
| Primary work | *The MI-Motion Dataset and Benchmark for 3D Multi-Person Motion Prediction* |
| Authors | Xiaogang Peng; Xiao Zhou; Yikai Luo; Hao Wen; Yu Ding; Zizhao Wu |
| Version and dates | arXiv:2306.13566v2; submitted 2023-06-23; revised 2023-06-26 |
| DOI | https://doi.org/10.48550/arXiv.2306.13566 |
| Primary URLs | https://arxiv.org/abs/2306.13566; https://arxiv.org/html/2306.13566; https://arxiv.org/pdf/2306.13566 |
| Official project page | https://mi-motion.github.io/ |
| Source state | PDF, metadata HTML, full-paper HTML, and source archive passed local integrity verification; all were withheld locally |
| Code and data status | The project page describes supplementary benchmark code and dataset access; an official public code repository was not established from inspected sources |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | arXiv record | Official metadata | Title, authors, version, dates, abstract, DOI | Identity and stated contribution | High | Abstract is not experiment evidence |
| E2 | Full paper HTML and verified PDF | Primary paper | Dataset construction, SocialTGCN, protocol, Tables 1-8, figures, appendices | Method and author-reported results | High for transcription | No independent reproduction |
| E3 | Official project page | Author project context | Access conditions and supplementary-material statements | Availability context | Medium-high | Does not prove a reproducible public release |
| E4 | InterDance Reactive 3D Dance Gen - DEP-E | Related DEP | Reactive duet interaction and 3D motion-data context | Related synthesis | Medium | Different task and evidence base |
| E5 | LA-Pose Latent Action - DEP-E | Related DEP | Temporal transition representation and relative-pose learning | Related synthesis | Medium | Camera pose differs from body forecasting |
| E6 | RRT-CBF Motion - DEP-E | Related DEP | Multi-agent trajectory and constraint-aware evaluation context | Related synthesis | Medium | Planner, not forecasting baseline |
| E7 | Selection and dedup records | Process evidence | Uniform draw, repository and memory searches, source-gate repair | Eligibility and provenance | High | Metadata-only inventory hit is not a prior DEP |

## Executive Summary

MI-Motion proposes a 3D multi-person motion-prediction dataset and benchmark with five activity scenes, three-to-six-person interactions, and 167k pose frames. The benchmark compares HRI, MRT, TBIFormer, and a proposed lightweight SocialTGCN baseline across short-, long-, and ultra-long-horizon predictions. SocialTGCN combines pose refinement, social-temporal graph convolution, and a temporal-convolution decoder.

The source supports a useful benchmark contribution and competitive results, not uniform model superiority. At 400 ms, SocialTGCN reports strong short-horizon AJPE in Park and Street, while it has worse Special Locations GJPE and RFDE than some comparators. The model's 0.320 G reported FLOPs is lower than each listed comparator, but comparison conditions and end-to-end runtime are not fully characterized.

The synthetic-data access agreement, inconsistent 210/217 sequence descriptions, absence of repeated-seed uncertainty, and lack of an established official public code repository constrain replication and transfer. Source integrity establishes reviewability, not reproducibility or deployment readiness.

## Detailed Summary

### Problem and dataset

The work forecasts future 3D skeletal motion for multiple interacting people. It describes five scenes: Park, Street, Indoor, Special Locations, and Complex Crowd; 167k frames; 20 keypoints per person; and three to six people per scene. The data pipeline combines interactive action packs, selected marker-based motion capture, Unreal Engine 5 scene construction, and a Blueprint that exports joint coordinates.

The paper states 210 sequences in one location and 217 in another. This artifact preserves the discrepancy rather than selecting a count. The official project page states that the synthetic component requires a data-access agreement, so frictionless public availability must not be assumed.

### Benchmark and method

SocialTGCN has a pose-refine module, social-temporal GCN encoder, and TCN decoder. The benchmark feeds 25 frames and predicts 25 frames for short and long horizons, then autoregressively predicts another 25 frames for ultra-long evaluation. GJPE measures global joint error, AJPE focuses on pose after removing global movement, and RFDE measures root-joint final displacement.

The protocol uses 80% of Park, Street, Indoor, and Special Locations for training and 20% for testing; Complex Crowd is testing-only. The paper compares HRI, MRT, TBIFormer, and SocialTGCN. It also uses power-spectrum entropy and KLD for longer-horizon behavior, with a stated need to interpret entropy together with KLD.

### Results and limits

At 400 ms, SocialTGCN's reported AJPE is 53 mm in Park, 46 mm in Street, 58 mm in Indoor, 134 mm in Special Locations, and 56 mm in Complex Crowd. At that horizon, its Special Locations GJPE is 199 mm versus 189 mm for MRT and TBIFormer; its RFDE is 174 mm versus 144 mm for MRT. Long-horizon rankings are likewise mixed.

The source reports 3.31 M parameters and 0.320 G FLOPs for SocialTGCN, versus 2.83/2.829 for HRI, 7.28/0.382 for MRT, and 5.60/0.597 for TBIFormer. Ablations support contributions from pose-constraint loss and the SocialGCN encoder in the stated setting, but no repeated-seed uncertainty, independent data access, or field robustness evidence was inspected.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | MI-Motion provides a dedicated multi-person 3D motion-prediction dataset and benchmark. | Author claim | E1, E2 | Directly supported by source design and tables. | High |
| C2 | SocialTGCN is lightweight and competitive in the reported benchmark. | Author claim with table support | E2 | Supported in the stated protocol; results are metric- and scene-dependent. | Medium-high |
| C3 | SocialTGCN uniformly outperforms the comparators. | Overbroad interpretation | E2 | Not supported; several Special Locations and long-horizon cells favor another method. | High rejection confidence |
| C4 | The benchmark establishes real-world safe multi-person forecasting. | Unsupported implication | E2, E3 | Rejected: access, split, and safety evidence are insufficient. | High rejection confidence |
| C5 | Related DEP work can guide a modular future evaluation. | Reviewer interpretation | E4-E6 | Plausible synthesis hypothesis; requires a new controlled study. | Medium |

## Methodology

- **Research objective:** Review one randomly selected eligible local arXiv paper and publish a public-safe, source-grounded DEP-E artifact.
- **Sources inspected:** Official metadata, verified PDF and full-paper HTML, official project page, live Black Lake and Black-Lake-Data READMEs, and exactly three related DEP manuscripts.
- **Discovery strategy:** Enumerated 75,781 PDFs with rg --files -g "*.pdf", grouped them into 75,778 parent-directory units, sorted them, and used a uniform PowerShell Get-Random draw at zero-based index 69,830.
- **Inclusion criteria:** Verifiable identity, complete PDF and full-paper HTML, direct relevance, and no prior Arxiv DEP processing.
- **Exclusion criteria:** Prior DEP artifacts, same-paper 24-hour markers, abstract-only or invalid units, source redistribution, and unreplicated deployment conclusions.
- **Random selection and dedup:** The first draw was accepted. Required repository, memory, and Black-Lake-Data searches found no prior processed artifact, DOI/title/slug match, or 24-hour marker. One metadata-only inventory row was not a duplicate. Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.
- **Source repair and verification:** Initial state was partial because HTML was absent. One bounded repair preserved the valid PDF and added metadata HTML, full-paper HTML, and source archive. The final PDF and HTML passed header, trailer, body, document-marker, heading, and structure checks with no partial files.
- **Analytical approach:** Empirical, conceptual, comparative, implementation, safety/ethics, product, and replication analysis.
- **Evidence handling:** Author claims, table evidence, reviewer interpretation, and unsupported implications are labeled separately.
- **Uncertainty handling:** Unreproduced results, access constraints, source inconsistency, and unavailable public-code confirmation remain explicit.

## Scope, Constraints, and Assumptions

- **Scope:** arXiv:2306.13566v2, its dataset and benchmark design, results, limitations, and bounded research translation.
- **Temporal boundary:** Public paper version v2 and source context inspected through the public-safe artifact date.
- **Evidence limits:** No experiment, benchmark, data download, or code execution was performed. Reported scores are not independently verified.
- **Assumptions:** The canonical arXiv record identifies the reviewed version and the project page accurately describes access context.
- **Constraints:** Original source documents remain local; public artifacts omit source files, local paths, machine details, timezones, and exact execution timestamps.
- **Out of scope:** Dataset-rights determination, production deployment, consequential monitoring, and safety certification.
- **Intended use:** Research review, benchmark planning, reproducibility design, and safe offline implementation exploration.

## Observations

- **Observed pattern:** GJPE, AJPE, and RFDE do not move together, so a single aggregate claim hides global-versus-local error tradeoffs.
- **Observed pattern:** Special Locations and Complex Crowd reveal more challenging global-motion conditions than simple average performance would show.
- **Technical implication:** A future benchmark should report per-scene counts, uncertainty, collision/proximity metrics, and static-pose-collapse indicators beside pose error.
- **Contradiction or tension:** The paper states both 210 and 217 sequences; a source version manifest is needed before treating either count as canonical.
- **Open question:** Transfer under changes to authored/captured interactions, scene distribution, and access controls is not established.

## Considerations

Any derivative should respect data-access terms, identity and representation risks, and the distinction between predicting motion and controlling or judging people. Implementations should default to synthetic or authorized data, minimize personal identifiers, preserve provenance, avoid biometric identification, and keep outputs nonbinding. Evaluation should include access review, leakage checks, repeatable splits, confidence intervals, calibration, failure analysis, and human oversight for sensitive use.

## Strengths

- Concrete multi-person benchmark framing rather than independent single-person tracks.
- Separate local pose, global joint error, and root-trajectory measures.
- Short-, long-, and ultra-long-horizon evaluation plus ablations and qualitative examples.
- Complete paper source with visually reviewed figures and tables.

## Weaknesses

- Internally inconsistent 210 and 217 sequence counts.
- Constrained access and authored/synthetic components limit frictionless independent replication.
- No repeated-seed uncertainty, confidence intervals, or statistical tests were found.
- Testing-only Complex Crowd leaves cross-scene generalization uncertain.
- No official public code repository was established from inspected primary sources.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Versioned dataset manifest | Provenance | Resolve count and access ambiguity | Auditable data identity | Release governance | Reconcile every sequence and scene |
| Repeated-seed cross-scene studies | Evaluation | Test robustness beyond one split | Credible transfer bounds | More compute | Report intervals and held-out scenes |
| Reproducible baseline package | Reproducibility | Tables alone cannot reproduce results | Independent comparison | Maintenance | Clean-environment rerun |
| Interaction-safety diagnostics | Responsible use | Low error can still imply unsafe proximity | Better evaluation | Geometry labels | Compare clearance and plausibility slices |

## Potential Implementations

1. **Multi-person benchmark auditor:** validate authorized manifests before scoring GJPE, AJPE, RFDE, and per-scene uncertainty.
2. **Interaction plausibility sandbox:** compare synthetic interaction-aware and independent-person forecasts for proximity, drift, and static-pose collapse.
3. **Forecast-to-constraint evidence gate:** pass synthetic forecast summaries to a non-actuating monitor that emits clearance or abstention evidence.

## Three Ways to Exercise This Research

1. **Manifest-first replay:** use a synthetic mini-dataset with declared joint order, scenes, and horizons; succeed when a fixed scorecard repeats; stop if metadata or split integrity is missing.
2. **Metric disagreement study:** construct trajectories with accurate local pose but drifting roots; succeed when GJPE, AJPE, and RFDE expose the distinction; stop before human-subject or biometric data is used.
3. **Constraint-aware forecast simulation:** provide synthetic interacting trajectories to a non-actuating clearance monitor; succeed when it records safe, uncertain, and abstained cases; stop on missing geometry or authorization.

## Example MVP Product

- **Product name:** Motion Benchmark Evidence Gate.
- **Target user:** Research engineer or reviewer evaluating multi-person motion predictors.
- **Problem:** Benchmark reports can obscure data/split drift, metric disagreement, and unreplicated claims.
- **Core workflow:** Load an authorized manifest, validate scene and coordinate contracts, run fixed metrics, compare baselines, generate failure slices, and emit a review receipt.
- **Data requirements:** Synthetic or authorized 3D joint trajectories, scene labels, and a versioned split manifest.
- **Architecture:** Local manifest validator, trajectory normalizer, metric engine, baseline adapter, failure-slice reporter, and append-only evidence store.
- **Success metrics:** Reproducible runs, zero split leakage, per-scene coverage, and reviewer-detected configuration errors.
- **Risk controls:** Offline processing, data minimization, no identity recognition, no surveillance deployment, retention limits, and human review.
- **Limitations:** Does not reproduce MI-Motion results, validate data rights, model social intent, or certify physical safety.

## Related Research and Reading

| Item | Type | Relevance | URL or repository reference |
|---|---|---|---|
| InterDance: Reactive 3D Dance Generation with Realistic Duet Interactions | Related DEP and paper | Interactive 3D body-motion and duet-reaction context | .lake-data/DEP-E/DEP-E-20260723-InterDance Reactive 3D Da/interdance_reactive_3d_da_manuscript.md; https://arxiv.org/abs/2412.16982 |
| LA-Pose: Learning Latent Actions for Camera Pose Estimation | Related DEP and paper | Temporal latent representations for motion and pose | .lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md; https://arxiv.org/abs/2604.27448 |
| RRT-CBF Based Motion Planning | Related DEP and paper | Multi-agent trajectory constraints and safety evaluation | .lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md; https://arxiv.org/abs/2410.00343 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2306.13566 | Metadata, authors, dates, DOI, abstract | 2026-07-28 | Metadata only |
| R2 | https://arxiv.org/html/2306.13566 | Dataset, method, protocol, tables, appendices | 2026-07-28 | Full paper inspected; local copy withheld |
| R3 | https://arxiv.org/pdf/2306.13566 | Visual figures and tables, PDF integrity | 2026-07-28 | Full PDF inspected; local copy withheld |
| R4 | https://mi-motion.github.io/ | Dataset access and supplementary-material context | 2026-07-28 | Official project page |
| R5 | https://doi.org/10.48550/arXiv.2306.13566 | Persistent identifier | 2026-07-28 | arXiv-issued DOI |
| R6 | .lake-data/DEP-E/DEP-E-20260723-InterDance Reactive 3D Da/interdance_reactive_3d_da_manuscript.md | Related interactive-motion synthesis | 2026-07-28 | Repository-derived artifact |
| R7 | .lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md | Related latent-motion synthesis | 2026-07-28 | Repository-derived artifact |
| R8 | .lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md | Related trajectory-safety synthesis | 2026-07-28 | Repository-derived artifact |

## Appendix

### Selection, Deduplication, and Source-Integrity Record

- Selection used a uniform random index over 75,778 sorted paper units derived from 75,781 PDF candidates. The selected index was 69,830.
- The first draw passed duplicate checks. Searches covered required Black Lake paths, automation memory, and current Black-Lake-Data main. The metadata-only inventory hit was not a deposited review.
- Initial source state was partial. The preserved PDF passed size, header, and EOF checks. Repair added companion files only after bounded transfers and validation.
- Final full-paper HTML passed required gates: size above 5 KB, body text above 2,000 characters, document marker, at least two heading markers, and at least two structure terms. No partial files remain.
- No source file, metadata HTML, PDF, TeX archive, cache, extracted text, or rendering was staged, copied, or uploaded. No .source directory was created.

### Reproduction Checklist

1. Obtain authorized data access and preserve source-version, scene, and sequence manifests.
2. Freeze joint order, coordinate system, frame rate, input/output horizons, and person-count handling.
3. Recreate all baselines under the same split and report per-scene denominators, repeated seeds, uncertainty, runtime, and energy.
4. Audit global drift, interaction plausibility, collision/proximity outcomes, static-pose collapse, and access constraints before transfer claims.
