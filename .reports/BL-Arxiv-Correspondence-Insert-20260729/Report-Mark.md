# Report-Mark: APAP Correspondence Insertion

Public-safe review date: 2026-07-29

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Correspondence Insertion for As-Projective-As-Possible Image Stitching* |
| Authors | William X. Liu; Tat-Jun Chin |
| Identifier | arXiv:1608.07997v1; arXiv-issued DOI 10.48550/arXiv.1608.07997 |
| Submitted | 2016-08-29 |
| Subject | Computer Vision and Pattern Recognition (`cs.CV`) |
| Primary URLs | https://arxiv.org/abs/1608.07997; https://arxiv.org/pdf/1608.07997; https://arxiv.org/html/1608.07997 |
| Source state | Complete PDF and full-paper HTML were inspected; metadata, provenance, receipt, and extracted material remain local. No source file is deposited here. |

## Concise Research Notes

### Problem

APAP stitching can express spatially varying projective warps, but only where feature matches sufficiently sample the overlap. The paper targets parallax-heavy, correspondence-poor regions where a local APAP estimate becomes weak and produces misregistration or distortion.

### Method

APAP uses moving DLT to estimate a locally weighted homography for each image location. Correspondence insertion initializes a target-side coordinate from the current warp, refines it with a local intensity-matching objective and Lucas-Kanade-style update, then conditionally appends the candidate match. A data-driven loop selects high-residual, salient, sufficiently distant regions, rejects candidates over an error threshold, and re-estimates the warp after accepted insertions. The combined method is APAP+CI.

### Evidence and Results

The paper and supplement supply qualitative comparisons against APAP, parallax-tolerant stitching, single homographies, and three flow-based correspondence sources. The source reports that dense flow matches can remain locally inaccurate after one-pixel RANSAC filtering; the displayed truck, temple, shopfront, and lobby cases show consequent warp distortions. For one illustrated pair, the adaptation loop inserted 81 candidates in 65 seconds and accepted 11. Rendered figures show inserted points near visible APAP failures and visually improved alignment in selected examples.

### Limitations and Reviewer Interpretation

Evidence is qualitative and image-pair-specific: no standardized dataset, fixed-denominator success rate, uncertainty intervals, repeated-seed analysis, modern learned-matcher comparison, or verified runnable release was established. Reviewer interpretation: the durable contribution is an evidence-driven repair loop for under-supported geometry, but its usefulness depends on photometric assumptions, calibration, saliency, optimization stability, and a trustworthy acceptance gate.

## Evidence and Attribution

| ID | Evidence | Supports | Boundary |
|---|---|---|---|
| E1 | Complete primary paper, Sections 1-5, Algorithms 1-2, Figures 1-8 | APAP model, correspondence search, adaptation loop, comparisons | Primary source; author-reported and not reproduced |
| E2 | Supplementary Sections 1-4 and Figures 9-17 | Flow-based and additional parallax/no-parallax comparisons | Illustrative rather than controlled benchmark |
| E3 | Verified full-paper HTML and rendered PDF pages | Section, equation, algorithm, and figure coverage | Coverage validation, not scientific validation |
| E4 | arXiv metadata | Identity, authors, date, subject, DOI | Not used alone for technical claims |
| E5-E7 | Pixel-Point Transfer, iKalibr Calibration, and HERMES World Model DEP-E manuscripts | Cross-DEP synthesis | Conceptual context, not independent validation |

## Related DEP Entries

Exactly three related entries were inspected:

| Entry | Repository-relative path | Why selected | Source/reference basis |
|---|---|---|---|
| Pixel-Point Transfer - DEP-E | `.lake-data/DEP-E/DEP-E-20260718-Pixel Point Transfer/pixel_point_transfer_manuscript.md` | Both works make local correspondence first-class: APAP+CI inserts image matches, while PPKT uses calibrated pixel-point pairs to transfer local representations. | PPKT projection, contrastive pairing, and evidence ledger; primary basis https://arxiv.org/abs/2104.04687v3 |
| iKalibr Calibration - DEP-E | `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` | It surfaces spatial and temporal calibration assumptions required before residuals can be trusted as geometric evidence. | iKalibr association, observability, residuals, and limits; primary basis https://arxiv.org/abs/2407.11420 |
| HERMES World Model - DEP-E | `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` | It uses a camera-to-BEV-to-point-cloud interface whose downstream geometry similarly depends on preserving usable spatial structure. | HERMES tokenizer, renderer, geometry metrics, and limits; primary basis https://arxiv.org/abs/2501.14729 |

## Synthesis Note

### Concept Bridge

APAP+CI, PPKT, iKalibr, and HERMES each turn incomplete visual observations into a spatial representation that is useful only if its correspondence contract is explicit. APAP+CI expands image matches where warp support is weak; PPKT binds pixels to depth-derived points; iKalibr estimates the coordinate/time relations that make bindings meaningful; HERMES compresses cameras into BEV before rendering geometry. The bridge is an evidence-gated spatial interface, not an assumption that residuals alone identify missing matches.

### Potential Implementations

1. **Correspondence health monitor**: combine APAP residual, saliency, local feature density, calibration age, and optimization change into a reviewable candidate score.
2. **Multi-view geometry audit bench**: replay public or synthetic pairs across matchers while logging accepted/rejected matches, residual maps, and fixed-denominator alignment failures.
3. **BEV correspondence repair adapter**: project image support deficits into BEV confidence regions and request evidence or abstain rather than silently accepting uncertain camera geometry.

### Deeper Relationship Observations

1. **Density is not quality**: many correspondences can still be inaccurate or weakly informative; selection and validation matter as much as count.
2. **Interfaces encode hypotheses**: APAP's local homography, PPKT's adapter, iKalibr's state, and HERMES's BEV tokens determine what spatial structure survives a boundary.
3. **Residuals require a cause model**: high difference can mean missing support, occlusion, dynamics, illumination, calibration error, or nonprojective geometry.

### Conceptual Similarities

1. All four artifacts use explicit spatial correspondences rather than global feature similarity alone.
2. All four use intermediate representations that trade flexibility against regularization and cost.
3. All four need component-level diagnostics because a final image or aggregate score cannot identify the cause of geometric error.

### MVP Implementations with Code Mock-Ups

1. **Candidate evidence gate**

```python
def accept_candidate(*, residual, saliency, distance, calibration_ok):
    if not calibration_ok or saliency < 0.5 or distance < 15:
        return "reject"
    return "review" if residual > 100 else "candidate"
```

2. **Fixed-denominator alignment summary**

```python
def alignment_summary(errors):
    if not errors:
        raise ValueError("record every attempted pair")
    return {"attempts": len(errors), "mean_error": sum(errors) / len(errors),
            "within_3px": sum(error <= 3 for error in errors) / len(errors)}
```

3. **Projection coverage check**

```python
def coverage_ratio(cells, matched_cells):
    cells = set(cells)
    if not cells:
        raise ValueError("overlap grid is required")
    return len(cells.intersection(matched_cells)) / len(cells)
```

These are bounded audit aids for synthetic or authorized image data, not a reconstruction of the paper's implementation.

### Developer Challenges

1. Keep coordinate, image-scale, and warp conventions consistent through feature extraction, MDLT, inverse mapping, refinement, and compositing.
2. Distinguish missing support from calibration drift, occlusion, dynamics, repeated texture, and exposure changes without silently overfitting a residual heuristic.
3. Build fair evaluation with public pairs, stable masks, fixed denominators, no hidden manual repair, reproducible parameters, and measured end-to-end cost.

### Author Challenges

1. Release a runnable implementation with defaults, image pairs, masks, intermediate residual maps, and commands for every figure.
2. Add quantitative registration, perceptual, and failure metrics with repeated trials and modern correspondence baselines.
3. Test ambiguity handling under illumination changes, moving objects, occlusion, miscalibration, and multi-plane scenes.

## Executive Assessment

The paper's specific contribution is credible and useful: it adds a mathematically described correspondence-search step to an APAP warp when the existing match set does not support the required local deformation.[^paper] Its deeper value is not a claim that more correspondences always fix stitching. Rather, it operationalizes an iterative hypothesis: a spatial residual can indicate a place where adding one validated local constraint may improve a regularized warp. The primary paper supports that hypothesis for its selected examples; it does not support a broad accuracy, real-time, or robustness guarantee.[^pdf]

## Problem Framing

The underlying problem is not merely visual blending. A stitch may look plausible after seam cutting while still having incorrect geometry. APAP+CI prioritizes alignment across the overlap before compositing, but it relies on brightness constancy, candidate search quality, and feature/mask choices. That makes its evidence boundary especially relevant for downstream imaging systems: a residual is a diagnostic prompt, not a proof that the correction is safe.

## Technical Reconstruction

APAP estimates a separate locally weighted homography for each query point; nearby matches receive greater influence. CI selects a source candidate, predicts its target coordinate under that current warp, and improves the target coordinate using the paper's local intensity objective. The important implementation dependency is circular: changing the candidate target coordinate changes the match set used by the local homography, so the Jacobian includes both image and warp terms. The outer loop then uses masks and thresholds to keep candidate insertion selective. This is a proposal-corrector system with a regularized geometric model, not a generic dense-registration algorithm.[^html]

## Experimental Design

The evidence includes selected image pairs, visual comparisons, and supplementary cases. The paper compares original APAP, parallax-tolerant stitching, and flow-derived correspondence inputs, applying seam selection in the depth-parallax cases. Reported settings provide a partial reconstruction surface, but the source does not supply complete experimental manifests, standardized splits, blind evaluation, repeated random trials, or uncertainty estimates. The review did not download data, run code, reconstruct the image pairs, or independently reproduce any figure.

## Results

The displayed visual evidence is consistent with the narrow conclusion that APAP+CI can repair some visibly under-supported regions. The truck, temple, shopfront, lobby, lawn, break-room, building, arch, and stage examples show the paper's intended failure modes: local APAP distortion or discontinuity is presented beside an output with inserted correspondence markers. The 81-candidate, 11-accepted, 65-second observation is an example-specific implementation indication rather than a system-level latency claim. The review therefore treats the source as promising qualitative evidence, not a ranking of stitching methods.

**Paper-reported claim:** the displayed image pairs improve after correspondence insertion. **Reviewer inference:** the mechanism is promising for under-supported local geometry, but the evidence does not establish a general success rate or identify every cause of improvement.

## Ablations

The paper contrasts method families but does not provide a full causal ablation of candidate selection, optimization, saliency, seam masking, distance threshold, acceptance threshold, and recomputation schedule. It also does not quantify whether rejected candidates were harmful, whether inserted pairs were geometrically correct, or whether the final result depends on seam cutting. A decisive ablation would hold initial matches and blending fixed, vary one repair component at a time, and report error over every attempted region.

## Claim-by-Claim Vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| APAP+CI improves the shown difficult stitches. | Main and supplementary figures compare source-reported outputs. | Supported under the displayed conditions; no aggregate or independent replication was inspected. |
| Dense flow correspondence is unsuitable for accurate APAP stitching. | The selected dense-flow examples contain local distortions after RANSAC. | Promising but limited; the paper does not test modern learned matching or all validation policies. |
| Inserting local constraints preserves useful APAP regularization. | The mechanism and qualitative examples are documented. | Mechanistically plausible and source-supported, but not proven across arbitrary scenes or parameter choices. |

## External Context

Pixel-Point Transfer makes a related point in a different modality: the local correspondence and its adapter determine what structure can transfer between pixels and points, rather than a generic global similarity score.[^ppkt] iKalibr highlights a precondition omitted by a pure image residual: spatial and temporal calibration must be observable and valid before correspondence evidence can support a geometric conclusion.[^ikalibr] HERMES similarly relies on a camera-to-BEV spatial interface before rendering point-cloud geometry. These records deepen the engineering context but do not validate APAP+CI's results.

## Implications

For implementation, the paper supports a conservative repair architecture: preserve all initial matches, compute a candidate-evidence card, reject ambiguous residuals, log every acceptance/rejection, and separate geometric metrics from seam/blending metrics. This would make the method more auditable and safer to evaluate on public, synthetic, or otherwise authorized data. It should not be used as an unattended decision component in safety-critical navigation or identity-sensitive image workflows.

## Replication and Falsification Agenda

First, rebuild the full pipeline with frozen image pairs, feature extraction, MDLT settings, masks, thresholds, and compositing rules. Second, evaluate every candidate region with a fixed denominator and a geometric reference, measuring acceptance precision, coverage, and visual distortion separately. Third, compare against contemporary matchers under illumination, occlusion, dynamic-scene, calibration, and repeated-texture shifts. A failed replication would be an inability to reproduce improvement while holding blending and initial correspondence inputs fixed.

## Table and Figure Coverage Ledger

| Coverage item | Source role | Review finding |
|---|---|---|
| Figures 1-4 | Main-paper mechanism and flow comparison | Inspected; they illustrate support failure, adaptation components, and flow-derived distortion. |
| Figures 5-8 | Main-paper qualitative comparisons | Inspected; APAP+CI is shown with inserted points near visual failure regions. |
| Figures 9-17 | Supplementary comparisons | Inspected; they broaden the examples but remain non-aggregate evidence. |
| Algorithms 1-2 and Equations 2-13 | Technical reconstruction | Inspected; no independent rederivation or implementation execution occurred. |

## Durable Restatement

Correspondence insertion is best remembered as selective geometric evidence repair: when a locally regularized warp lacks support, seek one auditable constraint rather than blindly increasing warp freedom. The source shows this can help on chosen panorama examples. Future work must establish when a residual really indicates missing support, when it indicates a different cause, and whether a repair improves geometry for the full attempted workload.

## Source and Evidence Notes

The reviewed source is a complete 20-page PDF with supplementary material plus verified full-paper HTML. The paper's methods, equations, algorithms, figures, and supplement were inspected; no source code, checkpoint, dataset, or result was run. Primary source documents and all local derivative materials remain withheld. Related DEP entries were read for synthesis only and are not independent experimental confirmation.

## Footnotes

[^paper]: Primary record: https://arxiv.org/abs/1608.07997
[^pdf]: Complete paper and supplement: https://arxiv.org/pdf/1608.07997
[^html]: Verified full-paper HTML: https://arxiv.org/html/1608.07997
[^ppkt]: Pixel-Point Transfer DEP-E: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md
[^ikalibr]: iKalibr Calibration DEP-E: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md

## Validation Notes

- The original unit was source-blocked because full-paper HTML was absent. A bounded brokered repair preserved the valid PDF and produced verified metadata and full-paper HTML before review.
- The PDF has 20 pages, including supplementary material. Visual inspection covered the overview, objective, adaptation algorithm, flow comparison, and supplementary comparisons.
- Full-paper HTML passed size, body-character, document-marker, heading, and structure-term gates. Source package acquisition was unavailable and is recorded rather than inferred.
- No local path, username, machine name, local timezone, exact execution timestamp, PDF, HTML, source archive, cache, extracted text, or image appears in this report.

## Attribution Block

- Source URL: https://arxiv.org/abs/1608.07997
  - Applies to: paper identity, authors, date, subject, and arXiv DOI.
- Source URL: https://arxiv.org/pdf/1608.07997
  - Applies to: complete paper, algorithms, equations, figures, supplement, and comparisons; source file withheld locally.
- Source URL: https://arxiv.org/html/1608.07997
  - Applies to: verified full-paper HTML coverage; source file withheld locally.
- Source URL: https://arxiv.org/e-print/1608.07997
  - Applies to: canonical source-package locator; package was unavailable and was not deposited.
- Source URL: https://doi.org/10.48550/arXiv.1608.07997
  - Applies to: arXiv-issued DOI identity.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md
  - Applies to: pixel-point correspondence synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md
  - Applies to: calibration and association synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model/hermes_world_model_manuscript.md
  - Applies to: camera-to-BEV and point-cloud representation synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: repository filing, attribution, and local-source withholding rules.
