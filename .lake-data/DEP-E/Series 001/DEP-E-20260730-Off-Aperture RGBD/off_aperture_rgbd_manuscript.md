---
title: "Off-Aperture RGBD - DEP-E"
generated_at: "2026-07-30"
artifact_type: "DEP-E research manuscript"
primary_subject: "Off-aperture diffractive encoding for wide-FoV RGBD imaging"
source_status: "Complete verified paper; source files withheld locally"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-30"
temporal_cutoff: "Paper v1 submitted 2025-07-30; public sources inspected through 2026-07-30"
primary_url: "https://arxiv.org/abs/2507.22523"
stable_identifier: "arXiv:2507.22523; DOI:10.48550/arXiv.2507.22523"
distribution_notes: "Original PDF, full-paper HTML, metadata HTML, source-package status records, and repair records remain local and were not redistributed."
---

# Off-Aperture RGBD - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public URL | Status |
|---|---|---|---|---|---|---|
| S1 | *Learned Off-aperture Encoding for Wide Field-of-view RGBD Imaging* | Primary metadata | arXiv abstract | arXiv:2507.22523v1; submitted 2025-07-30 | https://arxiv.org/abs/2507.22523 | Inspected |
| S2 | Complete paper | Primary evidence | PDF | 44,284,252 bytes; valid header and EOF | https://arxiv.org/pdf/2507.22523 | Inspected locally; withheld |
| S3 | Complete paper | Primary evidence | Full-paper HTML | 209,952 bytes; verified document | https://arxiv.org/html/2507.22523 | Inspected locally; withheld |
| S4 | Pixel-Point Transfer DEP-E | Related research | Repository manuscript | DEP-E-20260718-Pixel Point Transfer | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md | Inspected |
| S5 | Stable Diffusion Depth DEP-E | Related research | Repository manuscript | DEP-E-20260718-Stable Diffusion Depth | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-Stable%20Diffusion%20Depth/stable_diffusion_depth_manuscript.md | Inspected |
| S6 | iKalibr Calibration DEP-E | Related research | Repository manuscript | DEP-E-20260714-iKalibr Calibration | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md | Inspected |

**Authors:** Haoyu Wei, Xin Liu, Yuhui Liu, Qiang Fu, Wolfgang Heidrich, Edmund Y. Lam, and Yifan Peng.

**Source integrity:** The random draw initially found a valid PDF without full-paper HTML. A bounded brokered repair added metadata and full-paper HTML without replacing the valid PDF. HTML validation found substantial body text, document markers, section markers, and paper-structure terms; no partial file remained. The optional source package was unavailable through the redirect policy. Source records remain local and no source file is redistributed here.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Title, authors, abstract, date, subjects, DOI, and publication comment | Identity and stated contribution | High | Abstract is insufficient for empirical conclusions |
| E2 | S2-S3 | Primary full paper | Sections 1–8, Fig. 1–10, Table I, references, and limitations | Method, datasets, numerical results, prototypes, and boundaries | High for source reporting | No independent experiment or fabrication reproduction |
| E3 | S2-S3 | Primary empirical evidence | Table I and descriptions of the simple-lens and compound-lens studies | PSNR/MAE comparisons and evaluation design | High for displayed rows | No repeated-seed intervals or complete supplementary table extraction |
| E4 | S2-S3 | Primary limitation evidence | Compute discussion, PSF calibration, haze, halo, and conclusion | Constraints and implementation risk | High | Manufacturing yields and long-term durability are not measured |
| E5 | S4-S6 | Related DEP manuscripts | RGBD correspondence, robust-depth governance, and calibration provenance | Cross-DEP synthesis | Medium | Related artifacts do not validate the optical results |
| E6 | Selection and verification records | Process evidence | Uniform draw, dedup scan, repair, and document checks | Eligibility and source completeness | High | Private operational records are intentionally withheld |

## Executive Summary

The paper proposes placing a learned diffractive optical element away from the aperture plane to provide more angle-dependent, localized control of wavefronts in wide-field-of-view imaging. It combines differentiable ray tracing for refractive optics, least-sampling angular-spectrum propagation for diffraction, and a learned decoder. The intended payoff is better correction of off-axis aberrations while retaining optical encoding that supports both color reconstruction and depth estimation.

The source reports two applications. A simple-lens system reaches approximately 45-degree FoV and reports more than 5 dB PSNR improvement over an on-aperture configuration for the stated off-axis correction task. A compound Cooke-triplet RGBD system reaches approximately 28-degree FoV. Its off-aperture multi-head result is 32.09 dB / 0.033 MAE on Sceneflow, 28.28 / 0.019 on Dualpixel, and 31.42 / 0.027 on Instereo2K, compared with listed near-aperture and U-Net baselines.

The evidence supports a narrow interpretation: DOE position is a useful optical design variable in the paper's simulated and prototype settings. It does not establish broad deployment reliability. The authors separately optimize refractive lenses and the DOE because large-angle double propagation is expensive; measured PSFs require fine-tuning; haze and halo artifacts appear in physical measurements; and semantic depth used during fine-tuning is an imperfect proxy. Practical adoption should therefore pair optical metrics with active-depth evaluation, calibration provenance, and fabrication-tolerance testing.

## Detailed Summary

### Problem and mechanism

Conventional coded apertures place an encoding element on or near the aperture, which gives global wavefront modulation. The paper argues that a DOE positioned between the aperture and sensor can spatially separate angular bundles, allowing more local control at the image plane while preserving enough redirection capability to improve off-axis imaging. The resulting position is a trade-off rather than an endpoint at either plane.

The modeling pipeline first obtains a refractive lens response through differentiable ray tracing. It then applies two-step off-axis wave propagation through the DOE with least-sampling angular spectrum modeling. The squared sensor-plane field yields PSFs; local image patches are convolved with these shift-variant PSFs across depths to generate measurements. This is a hybrid physical model, not a pure neural restoration model.

### Decoder and objectives

The reconstruction network shares a fine-tuned ResNet-18 encoder and gives color and depth their own four-block upsampling decoders with skip connections. The paper explains the separation as a response to an objective conflict: sharp image reconstruction favors PSFs similar across depths, while depth estimation benefits from depth-varying PSFs. Image MSE and perceptual losses, depth loss, and a PSF-energy loss are balanced using dynamic weight averaging.

### Evaluations

For the simple-lens simulation, the paper trains on 26,281 images from FlyingThings3D, Dualpixels, and Instereo2K, then reports test use of 1,000, 684, and 50 images respectively. It simulates approximately 45-degree FoV and reports that off-aperture placement improves quality relative to its on-aperture comparison, including a stated over-5-dB improvement in the conclusion.

For compound RGBD imaging, a pre-optimized Cooke triplet is combined with a DOE after the lens module. The source trains seven angles and tests intermediate angles, employs separate image and depth heads, and compares near-aperture multi-head, off-aperture U-Net, and off-aperture multi-head results. Table I favors the off-aperture multi-head row on all three shown color/depth pairs.

### Physical evidence and limits

The authors build two camera prototypes. PSFs are captured at sampled locations/depths and then used to fine-tune reconstruction. The paper reports indoor and outdoor qualitative results, comparison with an achromatic doublet/restoration baseline and a commercial DSLR lens, and a fixed-exposure pinhole comparison. These establish a physical feasibility signal, not production robustness.

The reported caveats matter: full refractive-plus-DOE end-to-end optimization is omitted for memory/runtime reasons; PSF measurements in the RGBD application exhibit haze attributed to fabrication/assembly; DOE use can create halo artifacts; and a semantic depth model used in fine-tuning may be visually ambiguous. The paper identifies active time-of-flight depth as a more reliable future ground-truth alternative.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Off-aperture DOE placement adds an effective design degree of freedom for wide-FoV imaging. | Author method claim | E2 | The ray-wave model and position analysis directly support the formulation. | High |
| C2 | The simple-lens setting improves off-axis reconstruction by over 5 dB PSNR versus on-aperture encoding. | Author empirical claim | E2-E3 | Source-reported conclusion; supplementary numeric detail was not independently reproduced. | Medium-high |
| C3 | Off-aperture multi-head reconstruction improves the displayed RGBD table rows over the listed alternatives. | Author empirical claim | E3 | Table I supports the three shown rows; it is not a repeated-seed or cross-hardware result. | High for transcription; medium for generalization |
| C4 | Separate decoders help with the tension between all-in-focus color and depth-sensitive PSFs. | Author architecture claim | E2-E3 | Design rationale is clear; the comparison is limited to the paper's U-Net baseline and settings. | Medium |
| C5 | Prototype demonstrations prove real-world wide-FoV RGBD readiness. | Reviewer rejection of overreach | E2-E4 | The prototypes support feasibility, while stated artifacts, calibration dependence, and missing reliability studies limit deployment claims. | High |

## Methodology

- `Research objective`: Create a source-grounded DEP-E manuscript on the optical mechanism, evidence, limitations, and implementation relevance.
- `Sources inspected`: Verified local PDF and full-paper HTML, arXiv metadata, the live Black-Lake README and DEP-E filing rules, and exactly three related Black Lake DEP manuscripts.
- `Discovery strategy`: Uniform random selection from unique PDF-parent paper units using `Get-Random`; public arXiv metadata and full-text routes then anchored identity and claims.
- `Inclusion criteria`: One non-duplicated arXiv paper with a valid PDF and a validated full-paper HTML document; related entries required concrete overlap with RGBD geometry, depth evidence, or calibration.
- `Exclusion criteria`: Abstract-only material, invalid/partial documents, unverified code claims, local paths, source files, and unprocessed inventory rows.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, replication, and safety/ethics analysis.
- `Evidence handling`: Major claims are marked as author claims or reviewer interpretation and mapped to E1–E6.
- `Uncertainty handling`: Exact source-reported results are retained where visible; missing replication, uncertainty intervals, and code evidence are stated rather than inferred.
- `Random selection and dedup`: 75,959 PDFs formed 75,956 unique parent units; sorted-unit index 30,138 was drawn uniformly. No matching arXiv ID, DOI, normalized title, slug, processed artifact, or 24-hour marker appeared; 0 reselections were required.

## Scope, Constraints, and Assumptions

- `Scope`: The paper's off-aperture design, reported experiments, related DEP connections, and safe implementation/review paths.
- `Temporal boundary`: Sources were inspected through 2026-07-30; the paper is arXiv v1 from 2025-07-30.
- `Evidence limits`: No code, hardware, dataset, simulation, or calibration sequence was rerun. Supplementary detail was not treated as inspected unless represented in the full paper.
- `Assumptions`: Reported numerical values are transcribed as author-reported evidence; measured active-depth validation is not assumed.
- `Constraints`: Original documents remain local; source redistribution, external hardware control, and safety-critical deployment claims are out of scope.
- `Out of scope`: Camera fabrication, live control, safety certification, cost estimation, and end-to-end reproduction.
- `Intended use`: Research review, experimental design, and evidence-aware implementation planning.

## Observations

- DOE location is a physical representation choice: it decides how much angular specificity is available before neural decoding.
- The multi-head architecture reflects a genuine task tension between color sharpness and depth discriminability.
- The source's physical prototypes are valuable because they expose artifacts absent from idealized optical simulation.
- The highest-impact follow-up is likely a geometry-first validation protocol, not another image-only benchmark.

## Considerations

- Wide-FoV optical gains must be separated from decoder capacity, dataset selection, and calibration quality.
- Depth values used for training or validation need an explicit provenance and uncertainty model, especially when semantic estimates are used.
- Fabrication, mounting, illumination, and sensor tolerances should be versioned experimental variables.
- Any AR/VR, autonomous, or edge-device use needs offline safety and failure testing before control coupling.

## Strengths

- Explicitly explores a physically meaningful DOE placement dimension rather than only optimizing a surface at a fixed plane.
- Combines refractive and diffractive modeling with learned reconstruction.
- Includes both simulations and physical prototypes.
- Reports tabled color and depth comparisons across three datasets and discusses meaningful limitations.

## Weaknesses

- Refractive lenses and DOE are optimized separately, leaving full joint optimization untested in the stated configurations.
- Repeated-run uncertainty, fabrication yield, hardware cost, and inference latency are not established.
- Physical artifacts and semantic-depth ambiguity complicate metric depth conclusions.
- No inspected official implementation or reproducible release surface was established from the arXiv record.

## Potential Improvements

1. Perform a factorial ablation of DOE position, decoder design, refractive optimization, and PSF-calibration strategy with repeated seeds.
2. Add active-depth reference measurements, geometry-error maps, and calibration perturbation tests to every physical evaluation.
3. Report fabrication-batch variation, illumination sweeps, lens/DOE tolerance, latency, memory, and power alongside image metrics.

## Potential Implementations

| Implementation | Core mechanism | Inputs | Evaluation | Guardrails |
|---|---|---|---|---|
| DOE position ledger | Simulated PSF/reconstruction sweep across physically mountable locations | Synthetic optics, measured tolerances, versioned scene set | PSNR, geometry error, repeatability | Offline simulation only; no source files or hardware-control automation |
| RGBD artifact auditor | Compare reconstruction/depth outputs with independent reference and artifact masks | Authorized scenes, active-depth reference, calibration manifest | MAE, edge error, halo rate, coverage | Quarantine disagreement; no autonomous control |
| Calibration-aware benchmark | Perturb pose/timing to map optical and downstream sensitivity | Public/authorized test set and frozen evaluator | Degradation curves and failure thresholds | Bounded synthetic perturbations; no live vehicle use |

## Three Ways to Exercise This Research

1. Build a toy ray-wave position sweep with synthetic scenes, then publish only aggregate metrics and configuration hashes.
2. Capture a small authorized calibration target set, compare PSF-derived depth with active depth, and manually inspect the worst artifact cases.
3. Run a frozen reconstruction benchmark under bounded camera-pose and illumination perturbations to identify where the claimed benefit disappears.

## Example MVP Product

- `Product name`: Optics-to-Geometry Evidence Card
- `Target user`: Computational-imaging researcher evaluating a compact RGBD prototype.
- `Problem`: Image quality alone can hide depth bias, calibration drift, and fabrication artifacts.
- `Core workflow`: Ingest a public-safe experiment manifest and aggregate reconstruction/depth metrics; compare each run with reference thresholds; emit pass/warn/fail findings with linked calibration and PSF versions.
- `Data requirements`: Authorized aggregate PSF/reconstruction/depth statistics, calibration summaries, scene labels, and version identifiers; no raw source papers or sensitive scenes.
- `Architecture`: Local parser, schema validator, metric rules, static report generator, and immutable provenance store.
- `Success metrics`: Complete manifest coverage, deterministic report generation, and detection of injected artifact/calibration failures.
- `Risk controls`: Offline only; no live optical actuation, vehicle connection, private-image upload, or safety certification label.
- `Limitations`: Cannot replace physical metrology, active-depth sensing, or independent peer review.

## Related Research and Reading

| Item | Relationship | Locator |
|---|---|---|
| Pixel-Point Transfer DEP-E | RGBD correspondence and calibrated geometry bridge | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md |
| Stable Diffusion Depth DEP-E | Depth robustness and geometry-preservation audit bridge | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-Stable%20Diffusion%20Depth/stable_diffusion_depth_manuscript.md |
| iKalibr Calibration DEP-E | Spatial-temporal camera calibration and uncertainty bridge | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md |
| Hybrid refractive-diffractive lens design | Direct methodological context cited by the paper | https://doi.org/10.1145/3680528.3687692 |
| Least-sampling angular spectrum method | Direct off-axis propagation context cited by the paper | https://doi.org/10.1364/OPTICA.495220 |

## Source References

- Wei, H., Liu, X., Liu, Y., Fu, Q., Heidrich, W., Lam, E. Y., and Peng, Y. *Learned Off-aperture Encoding for Wide Field-of-view RGBD Imaging*. arXiv:2507.22523, 2025. https://arxiv.org/abs/2507.22523
- Full-paper HTML: https://arxiv.org/html/2507.22523
- PDF: https://arxiv.org/pdf/2507.22523
- DOI: https://doi.org/10.48550/arXiv.2507.22523
- Related DEP: Pixel-Point Transfer. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md
- Related DEP: Stable Diffusion Depth. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-Stable%20Diffusion%20Depth/stable_diffusion_depth_manuscript.md
- Related DEP: iKalibr Calibration. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md

## Appendix

### Local source-integrity summary

The locally retained paper unit is complete. The PDF is above the 10 KB minimum, begins with `%PDF-`, and ends with `%%EOF`. The full-paper HTML exceeds 5 KB and 2,000 body characters, contains article/main/LaTeXML-style document markers, has more than two section/heading markers, and includes Introduction, Methods, Results, Discussion, Conclusion, and References. Metadata HTML was retained as metadata only. No source file is present in this public DEP.

### Table I transcription

| Dataset | Near-aperture + multi-head | Off-aperture + U-Net | Off-aperture + multi-head |
|---|---:|---:|---:|
| Sceneflow | 31.00 dB / 0.037 MAE | 25.27 / 0.046 | 32.09 / 0.033 |
| Dualpixel | 27.95 / 0.025 | 23.69 / 0.027 | 28.28 / 0.019 |
| Instereo2K | 30.51 / 0.032 | 26.06 / 0.124 | 31.42 / 0.027 |
