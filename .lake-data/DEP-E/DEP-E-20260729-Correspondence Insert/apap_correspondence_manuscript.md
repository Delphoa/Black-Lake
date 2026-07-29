---
title: "APAP Correspondence - DEP-E"
generated_at: "2026-07-29"
artifact_type: "DEP research artifact and paper report"
primary_subject: "A source-grounded review of correspondence insertion for APAP image stitching under sparse local feature support."
source_status: "verified local source bundle; public URLs only in deposit"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-29"
temporal_cutoff: "arXiv:1608.07997v1 and related DEP records inspected through 2026-07-29"
primary_url: "https://arxiv.org/abs/1608.07997"
stable_identifier: "arXiv:1608.07997v1; DOI 10.48550/arXiv.1608.07997"
confidence_summary: "High for source reporting and mechanism; medium for cross-DEP synthesis; low for independent reproducibility."
safety_scope: "research review and offline, authorized image-geometry evaluation"
distribution_notes: "Generated Markdown and public URLs only; original source files and extraction records are withheld."
---

# APAP Correspondence - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public URL | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Primary paper metadata | Primary source | arXiv metadata | `1608.07997v1`; submitted 2016-08-29 | https://arxiv.org/abs/1608.07997 | arXiv access; redistribution terms not inferred | 2026-07-29 | Inspected |
| S2 | Complete paper and supplement | Primary source | PDF | `arXiv:1608.07997v1` | https://arxiv.org/pdf/1608.07997 | Source file withheld locally | 2026-07-29 | Inspected and integrity-verified |
| S3 | Complete paper HTML | Primary source | full-paper HTML | verified document | https://arxiv.org/html/1608.07997 | Source file withheld locally | 2026-07-29 | Inspected and integrity-verified |
| S4 | Pixel-Point Transfer - DEP-E | Related research | Markdown manuscript | DEP-E-20260718-Pixel Point Transfer | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md | Underlying sources separately attributed | 2026-07-29 | Inspected |
| S5 | iKalibr Calibration - DEP-E | Related research | Markdown manuscript | DEP-E-20260714-iKalibr Calibration | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md | Underlying sources separately attributed | 2026-07-29 | Inspected |
| S6 | HERMES World Model - DEP-E | Related research | Markdown manuscript | DEP-E-20260712-HERMES World Model | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model/hermes_world_model_manuscript.md | Underlying sources separately attributed | 2026-07-29 | Inspected |

The primary paper is an arXiv v1 preprint by William X. Liu and Tat-Jun Chin in `cs.CV`. A separate venue or runnable code release was not established from the inspected primary record. The PDF and full-paper HTML passed the completeness gate before synthesis; the optional source package was unavailable.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Identity, date, subject, abstract, DOI | Source identity and scope | High | Metadata is insufficient for method/results |
| E2 | S2 | Complete paper | Sections 1-5, Equations 2-13, Algorithms 1-2, Figures 1-8 | APAP model, optimization, adaptation loop, visual results | High for reporting | No execution or reproduction |
| E3 | S2-S3 | Complete primary sources | Supplementary Sections 1-4, Figures 9-17, HTML cross-check | Flow failures, additional comparisons, coverage | High for reported content | Visual comparisons are not a controlled benchmark |
| E4 | S4 | Related DEP | Local pixel-point pairing and adapter/contrastive transfer | Correspondence synthesis | Medium | Different modality and task |
| E5 | S5 | Related DEP | Calibration, association, observability, residuals | Calibration synthesis | Medium | Different sensor suite |
| E6 | S6 | Related DEP | Camera-to-BEV tokenizer, renderer, geometry metrics | Representation synthesis | Medium | Different model and setting |

## Executive Summary

APAP uses moving DLT to make image stitching more flexible than a single homography, but this flexibility is bounded by local feature support. The reviewed paper proposes correspondence insertion: detect an under-aligned region, optimize a new image match under the current APAP warp, accept it only when it passes an error condition, and refit the warp. The source calls the resulting method APAP+CI.

The primary paper directly establishes the mechanism and reports visual improvements on selected image pairs. It also reports that dense optical-flow correspondences can remain locally inaccurate enough to distort a spatial warp despite tight RANSAC filtering. One illustrated loop inserted 81 candidates in 65 seconds and accepted 11. These are author-reported observations, not an independently reproduced performance benchmark.

Reviewer interpretation: the enduring research pattern is an evidence-gated repair loop for spatial support. Its safe transfer requires cause-aware residual handling, calibration provenance, match acceptance evidence, and fixed-denominator failure reporting; a visually pleasing composite is insufficient proof of geometric correctness.

## Detailed Summary

### Problem and Background

Feature-based panorama pipelines estimate transforms from sparse correspondences and use blending to hide remaining seams. A global homography fails under depth parallax. APAP instead estimates a locally weighted projective transform at each query location, but it still fails where existing correspondences undersample the true warp.

### Method

For a source-side candidate location, the paper initializes a target-side coordinate under the current APAP mapping and minimizes an intensity-matching objective over a local subwindow. Its derivation accounts for the candidate target coordinate changing the locally estimated homography. The outer loop computes overlap residuals, applies seam and saliency constraints, excludes locations near known matches, searches the best candidate, and appends a new pair only if its residual is acceptable. APAP is then re-estimated.

### Evidence and Results

Figures 1 and 5-8 compare APAP+CI with APAP and parallax-tolerant stitching on selected scenes. The supplement adds dense-flow comparisons and further significant/no-significant-parallax cases. The paper reports that optical-flow, Large Displacement Optical Flow, and SIFT Flow produced locally harmful correspondences in its chosen cases despite RANSAC. Reported parameters include a spatial weight scale of 8, a 31 by 31 subwindow, error threshold 100, saliency threshold 0.5, distance threshold 15, and acceptance threshold 1000.

### Limitations

No public fixed protocol, aggregate registration table, confidence interval, repeated-seed study, modern learned-baseline comparison, or verified runnable release was established. Residuals are ambiguous: occlusion, illumination, motion, repeated texture, calibration error, and nonprojective geometry can all resemble missing support. Seam cutting can improve appearance while obscuring registration-only failure.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | CI adds correspondences where APAP is locally under-supported. | Author method claim | E2, Algorithms 1-2 | Directly supported by the documented mechanism. | High |
| C2 | APAP+CI improves alignment on the shown pairs. | Author empirical claim | E2, Figures 1 and 5-8; E3, Figures 9-17 | Supported as selected visual evidence, not as population-level proof. | Medium |
| C3 | Dense flow can harm APAP stitching despite RANSAC. | Author comparative claim | E2, Figure 4; E3, Figures 9-12 | Supports a caution, not a universal verdict on flow. | Medium |
| C4 | Correspondence repair needs calibration and representation diagnostics. | Reviewer interpretation | E4-E6 | Useful cross-DEP inference, not established by the 2016 paper. | Medium |

## Methodology

- `Research objective`: preserve a source-grounded account of APAP correspondence insertion and translate it into bounded audit concepts.
- `Sources inspected`: complete repaired PDF, full-paper HTML, arXiv metadata, supplement, and exactly three related DEP-E manuscripts: Pixel-Point Transfer, iKalibr Calibration, and HERMES World Model.
- `Discovery strategy`: the original selection used `rg --files -g "*.pdf"`; 75,781 PDFs collapsed to 75,778 paper units and a uniform PowerShell `Get-Random` selected zero-based index 35,283. PDF/HTML extraction, page rendering, section/algorithm/figure coverage, and repository inspection followed.
- `Inclusion criteria`: complete primary evidence, canonical public locators, and DEP records with concrete overlap in correspondence, calibration, or spatial representation.
- `Exclusion criteria`: abstract-only claims, unverified code claims, unavailable source-package content, and secondary sources as proof of primary technical claims.
- `Analytical approach`: empirical, conceptual, comparative, implementation, and replication-oriented.
- `Evidence handling`: author claims remain author claims; visual evidence is bounded; reviewer synthesis is labeled; all local source files remain withheld.
- `Uncertainty handling`: no result is described as independently reproduced. The prior source-blocked memory record is treated as an explicit continuation after substantive repair, not a duplicate public deposit.
- `Dedup/reselection validation`: `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, and related Black-Lake-Data records were searched by ID, DOI, title, and slug. Published-artifact exclusions 0; reselections 0; public 24-hour cutoff 2026-07-28.

## Scope, Constraints, and Assumptions

- `Scope`: one preprint's mechanism, displayed evidence, source-disclosed constraints, and three DEP bridges.
- `Temporal boundary`: arXiv v1 and related DEP records through 2026-07-29.
- `Evidence limits`: no source package, code, dataset archive, or full numeric benchmark protocol was inspected; visual results were not rerun.
- `Assumptions`: verified PDF and HTML represent the same arXiv v1 work; public URLs are durable locators.
- `Constraints`: source files, caches, rendering, provenance, and system context remain local.
- `Out of scope`: production deployment, surveillance, navigation authorization, and independent reproduction.
- `Intended use`: research review, correspondence-audit design, and safe offline planning.

## Observations

- `Observed pattern`: CI uses residual evidence but constrains it with saliency, seam selection, distance, and acceptance thresholds; it is not merely adding matches.
- `Technical implication`: local flexibility can coexist with projective regularization when the set is selectively expanded.
- `Contradiction or tension`: both dense flow and photometric correspondence search depend on assumptions that can fail under ambiguity.
- `Reviewer hypothesis`: a modern repairer should model residual cause, calibration status, texture uniqueness, and geometric consistency jointly.

## Considerations

Visually seamless imagery can hide geometry error in mapping, inspection, and mixed-reality work. An operational implementation should retain input provenance, calibration state, match ledger, residual maps, and abstention reasons; it should report registration and blending separately. Use is appropriate for offline, authorized evaluation, not as a safety or identity decision signal.

## Strengths

- A concrete derivation for inserting a match into a local projective model.
- Inspectable Algorithms 1-2 rather than an unspecified adaptive heuristic.
- Supplementary cases that broaden the visual record.
- Explicit projective regularization rather than an unconstrained dense warp.

## Weaknesses

- Primarily qualitative results without aggregate, fixed-denominator metrics.
- Unisolated contribution of CI versus preprocessing, seam cutting, and tuning.
- Untested robustness to dynamics, lighting, calibration error, and broad domain shift.
- No verified runnable artifact for reproduction.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Cause-aware candidate model | Acceptance | Residuals have multiple causes | Fewer harmful insertions | Added complexity | Compare against residual-only gating on labeled slices |
| Geometric uncertainty output | Estimation | A final composite conceals weak support | Explicit abstention zones | Calibration may fail | Measure error/calibration by support level |
| Public protocol and artifacts | Reproducibility | Visual pairs limit comparison | Stronger regressions | Curation/licensing work | Publish pairs, masks, parameters, seeds, metrics |

## Potential Implementations

### 1. Correspondence repair workbench

- `User`: vision researcher or imaging engineer.
- `Goal`: identify where a spatial warp lacks trustworthy support.
- `Core mechanism`: combine residual, saliency, feature-density, calibration, and candidate-ledger layers.
- `Required inputs`: authorized image pairs, initial matches, masks, optional calibration metadata.
- `Outputs`: accepted/rejected matches, warp-difference map, and abstention zones.
- `Risk controls`: local-only processing, source provenance, no identity inference, manual confirmation before publishing composites.
- `Evaluation`: held-out reprojection and fixed-denominator failure metrics.

### 2. Calibration-aware matcher

- `User`: robotics or 3D perception team.
- `Goal`: prevent calibration mismatch from appearing as missing visual support.
- `Core mechanism`: join calibration validity with local correspondence evidence.
- `Required inputs`: synchronized authorized sensors, calibration marker, matches.
- `Outputs`: match set with calibration-related rejection reasons.
- `Risk controls`: offline only; no control commands.
- `Evaluation`: controlled temporal/extrinsic perturbations and false-repair rate.

### 3. BEV residual review adapter

- `User`: world-model evaluator.
- `Goal`: locate camera-to-BEV regions lacking spatial support.
- `Core mechanism`: project image support/residual maps into BEV confidence regions and abstain when necessary.
- `Required inputs`: multi-view features, BEV transform, coverage mask.
- `Outputs`: coverage-conditioned geometry score and review map.
- `Risk controls`: public or synthetic datasets; no driving-control integration.
- `Evaluation`: geometry error and confidence calibration with/without gate.

## Three Ways to Exercise This Research

1. **Synthetic homography stress test**: use synthetic or authorized pairs with known transforms and missing-match regions. Success is lower held-out reprojection error without lower coverage; stop when candidate acceptance destabilizes.
2. **Residual-cause labeling study**: label residual regions as ambiguity, occlusion, illumination, dynamics, calibration error, or missing support. Success is improved rejection precision; stop if labels are unreliable.
3. **Cross-DEP interface audit**: perturb synthetic calibration in pixel-point and camera-to-BEV pipelines. Success is surfacing known perturbations before downstream scoring; stop before real-world control use.

## Example MVP Product

- `Product name`: Match Ledger
- `Target user`: computer-vision engineer reviewing panorama or multi-view alignment.
- `Problem`: a final composite hides whether local geometry is supported by reliable matches.
- `Core workflow`: ingest authorized pairs and matches; estimate support/residual maps; generate candidate evidence cards; require approval or abstention; export a report.
- `Data requirements`: public, synthetic, or authorized images; points; optional calibration metadata.
- `Architecture`: match adapter, APAP-compatible warp module, residual analyzer, rule gate, evidence ledger, static report renderer.
- `Success metrics`: held-out reprojection error, fixed-denominator failure rate, rejection precision, coverage, runtime, reviewer agreement.
- `Risk controls`: local-only default, retained originals, no silent overwrite, no identity/surveillance function, manual review for sharing.
- `Limitations`: not a replacement for calibrated reconstruction; residuals remain ambiguous; no navigation authorization.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Pixel-Point Transfer - DEP-E | Related DEP | Local, physically grounded correspondence and adapter/contrastive transfer | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md |
| iKalibr Calibration - DEP-E | Related DEP | Calibration and association conditions shaping correspondence validity | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md |
| HERMES World Model - DEP-E | Related DEP | Camera-derived BEV and point-cloud geometry interface | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model/hermes_world_model_manuscript.md |
| APAP with Moving DLT | Direct baseline | Defines the APAP warp CI augments | https://doi.org/10.1109/CVPR.2013.439 |
| Parallax-tolerant image stitching | Direct baseline | Contrasting local-alignment and seam-selection strategy | https://doi.org/10.1109/CVPR.2014.422 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/1608.07997 | Identity, date, subject, DOI | 2026-07-29 | Canonical record |
| R2 | https://arxiv.org/pdf/1608.07997 | Paper, equations, algorithms, figures, supplement | 2026-07-29 | Reviewed locally and withheld |
| R3 | https://arxiv.org/html/1608.07997 | HTML coverage and verification | 2026-07-29 | Reviewed locally and withheld |
| R4 | https://arxiv.org/e-print/1608.07997 | Source-package locator | 2026-07-29 | Unavailable; not deposited |
| R5 | https://doi.org/10.48550/arXiv.1608.07997 | Stable DOI | 2026-07-29 | Identity only |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md | Pixel-point synthesis | 2026-07-29 | Related DEP only |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md | Calibration synthesis | 2026-07-29 | Related DEP only |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model/hermes_world_model_manuscript.md | BEV/point-cloud synthesis | 2026-07-29 | Related DEP only |

## Appendix

### Coverage Ledger

| Item | Coverage | Key evidence | Caveat |
|---|---|---|---|
| Main Sections 1-5 | Inspected | Motivation, model, search, adaptation, results, conclusion | No independent run |
| Equations 2-13 | Inspected | Local homography, weighted DLT, intensity objective, update | Not independently rederived |
| Algorithms 1-2 | Inspected | Correspondence optimizer and adaptation loop | Defaults not executed |
| Figures 1-8 | Inspected and selected pages rendered | Main qualitative comparisons | No numeric geometry ground truth |
| Supplement / Figures 9-17 | Inspected and selected pages rendered | Flow and further comparison evidence | Illustrative, not population benchmark |

### Source-Integrity and Public-Safety Record

- The repaired source state contains a complete PDF and verified full-paper HTML. The PDF has 20 pages; the HTML passed body, marker, heading, and structural-term gates.
- The optional source package was unavailable. No missing response was treated as success.
- No original source file, cache, render, local path, username, machine detail, local timezone, or exact execution timestamp appears in this public manuscript.
