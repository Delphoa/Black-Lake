---
title: "AVA Robustness - DEP-E"
generated_at: "2026-07-22"
artifact_type: "DEP research artifact"
primary_subject: "structured photometric adversarial robustness"
source_status: "verified local sources inspected and withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-22"
temporal_cutoff: "2026-07-22"
primary_url: "https://arxiv.org/abs/2105.05558"
stable_identifier: "arXiv:2105.05558; DOI:10.24963/ijcai.2021/145"
confidence_summary: "High for bibliographic and transcribed table facts; moderate for comparative interpretation; low for untested physical-realizability and human-imperceptibility claims."
safety_scope: "defensive robustness evaluation; non-operational attack discussion"
distribution_notes: "Derived public-safe prose only; source files withheld locally."
---

# AVA Robustness - DEP-E

## Source Metadata

| Field | Record |
|---|---|
| Primary title | *AVA: Adversarial Vignetting Attack against Visual Recognition* |
| Authors | Binyu Tian; Felix Juefei-Xu; Qing Guo; Xiaofei Xie; Xiaohong Li; Yang Liu |
| arXiv record | [arXiv:2105.05558](https://arxiv.org/abs/2105.05558) |
| Publisher record | [IJCAI 2021 proceedings](https://www.ijcai.org/proceedings/2021/145) |
| DOI | [10.24963/ijcai.2021/145](https://doi.org/10.24963/ijcai.2021/145) |
| Venue/pages | IJCAI 2021 Main Track, 1046-1053 |
| Submitted | 2021-05-12 |
| Review access date | 2026-07-22 |
| Local integrity state | Complete after bounded repair: verified PDF plus verified full-paper HTML |
| Redistribution | Original PDF, HTML, source package, extracted text, caches, and renders withheld locally |

The inspected evidence set included the complete eight-page paper, full-paper HTML, source representation, arXiv metadata, official IJCAI metadata and BibTeX, figures, tables, and focused implementation searches. An arXiv abstract page was treated as metadata only. Full-paper HTML was missing initially, so a verified ar5iv fallback was acquired before synthesis; the valid PDF was preserved.

## Evidence Ledger

| ID | Evidence | Role | Claims supported | Confidence / caveat |
|---|---|---|---|---|
| E1 | Complete PDF and rendered pages | Primary | Equations, figures, tables, hyperparameters, results, limitations visible in the paper | High for transcription; authored claims remain unreplicated |
| E2 | Full-paper HTML and source representation | Primary | Searchable method text, table source, prose/Table 2 comparison, revision residue | High; used to cross-check rather than override the rendered paper |
| E3 | [arXiv abstract record](https://arxiv.org/abs/2105.05558) | Primary metadata | Title, authors, submission date, subjects, public identifiers | High |
| E4 | [Official IJCAI record](https://www.ijcai.org/proceedings/2021/145) | Primary metadata | Venue, pages, author list, publisher DOI and BibTeX | High |
| E5 | [Papers with Code record](https://paperswithcode.com/paper/ava-adversarial-vignetting-attack-against) and focused searches | Secondary locator | No implementation located | Moderate; absence from searches is not proof that no private or later code exists |
| E6 | [Feature Denoising DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-Feature%20Denoising/feature_denoising_manuscript.md) | Related synthesis | Defense-side comparison and matched adversarial evaluation | Derived repository analysis |
| E7 | [ViT Semantic Robustness DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-ViT%20Semantic%20Robustness/vit_semantic_robustness_manuscript.md) | Related synthesis | Separation of numerical perturbation bounds from semantic/perceptual validation | Derived repository analysis |
| E8 | [Adversarial Label Noise DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Adversarial%20Label%20Noise/adversarial_label_noise_manuscript.md) | Related synthesis | Threat-model and objective dependence, calibration, held-out evaluation | Derived repository analysis |

Random selection used a uniform random integer over 75,777 unique parent paper units derived from 75,780 PDF paths. The accepted zero-based index was 13,681. The first draw passed exact identifier, DOI, normalized-title, slug, public-index, repository, automation-memory, recent-worktree, related-data, and 24-hour-marker checks; duplicate exclusions and reselections were zero.

The extraction layer was checked before review. The cache began as a miss. After source repair, a `missing-only` extraction used the verified local PDF, full-paper HTML, and source package, producing a cached record through `pypdf`, HTML-regex, and `tarfile` fallbacks. No network fetch was used during cache extraction. These process statements describe provenance, not scientific evidence.

## Executive Summary

AVA proposes adversarial image transformations that look like optical vignetting. It decomposes a vignette into off-axis illumination, geometry, and sensor-tilt factors. RI-AVA optimizes a small set of bounded physical parameters; RA-AVA adds a spatially tunable geometric field inside a learned region, regularized toward the physical reference. The expanded degrees of freedom make RA-AVA much stronger in the authors' white-box experiments.

The evidence is promising but narrower than the headline framing. RA-AVA reaches roughly 97-99% reported white-box success on DEV and leads every displayed CIFAR-10 transfer cell, yet leads only 16 of the 36 displayed cross-model transfer comparisons overall. Zero-DCE provides only partial recovery on Tiny ImageNet. BRISQUE, NIQE, and visual examples do not establish human imperceptibility or physical-camera realizability. An unresolved discrepancy between the prose and Table 2 further argues for machine-readable, version-bound result reporting.

For implementation, the most defensible product is not an attack generator but an optical-robustness evidence gate: a system that runs approved photometric stress tests, checks table/prose consistency, records perceptual and semantic controls, and withholds broad claims until physical, human, and reproducibility evidence is present.

## Detailed Summary

### Problem framing

Conventional adversarial examples often optimize additive pixel noise under an `L_p` budget. AVA instead asks whether a transformation motivated by lens vignetting can create a natural-looking failure mode. This widens the threat surface from local pixel differences to structured spatial illumination.

### Vignetting model

The paper writes the multiplicative field as `V = A ⊙ G ⊙ T`. `A` models off-axis illumination with a radial dependence controlled by inverse focal length; `G` approximates geometric vignetting; and `T` models a tilted sensor through angular parameters. Applying the field elementwise produces a vignetted image.

### RI-AVA and RA-AVA

RI-AVA keeps the analytic factors and tunes four bounded physical parameters—equivalent to inverse focal length, geometric attenuation, tilt magnitude, and tilt angle—using signed-gradient updates. RA-AVA relaxes `G` to be elementwise tunable inside a closed curve. A level-set representation, Heaviside mask, and regularization toward the analytic field define the adjustable region and its prior. The extra freedom improves reported success but makes physical realizability less obvious.

### Evaluation

The experiments cover DEV, CIFAR-10, and Tiny ImageNet with ResNet-50, EfficientNet-B0, DenseNet-121, and MobileNet-V2. The paper reports attack success rate plus BRISQUE and NIQE, and compares against MIFGSM, C&W L2, TIMIFGSM, Wasserstein perturbations, and cAdv. It uses 40 attack iterations and gives parameter bounds and per-parameter step sizes.

In white-box DEV evaluation, RA-AVA reports 96.77%, 98.34%, 99.22%, and 99.18% success. On CIFAR-10 the four values are 35.95%, 74.15%, 45.80%, and 84.66%; on Tiny ImageNet they are 69.44%, 90.23%, 76.98%, and 96.92%. These heterogeneous values warn against summarizing performance with a single universal rate.

In the transfer table, RA-AVA is highest in every CIFAR-10 cell, four Tiny ImageNet cells, and no DEV cells. The reviewer count is therefore 16 of 36 displayed comparisons. This count is derived from Table 2 and is not a separate experiment.

The Tiny ImageNet defense experiment applies Zero-DCE. Under RA-AVA, accuracy changes from 19.72% to 29.40% for ResNet-50, 4.47% to 12.96% for EfficientNet-B0, 14.60% to 24.81% for DenseNet-121, and 0.71% to 10.24% for MobileNet-V2. Those gains leave accuracy well below the clean baselines of 66.06%, 57.83%, 65.33%, and 49.40%.

### Record discrepancy

The prose says DEV examples crafted on ResNet-50 transfer at 37.21%, 40.75%, and 40.89%, with BRISQUE 11 and NIQE 37.04. Table 2 and its source report 20.27%, 21.59%, and 23.97%, with BRISQUE 21.33 and NIQE 46.92. Commented source values point to editing history but do not resolve which record was intended. Both are retained as conflicting primary-paper records.

## Key Claims and Evidence

| Claim | Evidence | Assessment |
|---|---|---|
| Structured vignetting can cause classifier failures. | E1-E2, Table 1 | Supported within the tested digital setup. |
| RA-AVA is stronger than RI-AVA. | E1-E2, Table 1 | Strongly supported for displayed white-box results; added flexibility confounds physicality. |
| RA-AVA transfers across models. | E1-E2, Table 2 | Supported, but it leads only 16/36 displayed cells; cAdv dominates DEV and many Tiny ImageNet cells. |
| Outputs are imperceptible. | E1 figures, BRISQUE/NIQE | Not established; no blinded human perceptual study. |
| The attack is physically realizable. | E1 analytic inspiration | Not established by an end-to-end camera experiment. |
| Zero-DCE defends against RA-AVA. | E1-E2, Table 3 | Partial support: recovery occurs, but defended accuracy remains far below clean accuracy. |
| Results are readily reproducible. | E1-E5 | Weak support; no official code, environment, seeds, uncertainty, or complete training recipe located. |

## Methodology

1. Enumerate local PDF records, collapse them to parent paper units, and make one uniform random draw.
2. Reject any draw that collides by identifier, DOI, normalized title, slug, prior artifacts, memory, related data, active recent worktrees, or a same-paper marker within 24 hours.
3. Classify source integrity before review. Require both a valid PDF and full-paper HTML; repair and reverify a partial unit before synthesis.
4. Run extractor preflight and `missing-only` cache population, preferring verified local sources.
5. Inspect the complete paper, source representation, figures, tables, official metadata, and implementation evidence.
6. Separate authored claims, reviewer arithmetic, inference, and missing evidence in the ledger.
7. Inspect exactly three related DEP-E manuscripts for concrete conceptual overlap.
8. Generate only public-safe derived prose and validate schema, counts, code syntax, paths, and the source-upload allowlist.

No model was attacked, no attack implementation was executed, and no result was experimentally reproduced.

## Scope, Constraints, and Assumptions

- Scope is the 2021 paper and public records inspected by the temporal cutoff.
- Reported results are the authors' evidence, not independently verified performance.
- The transfer-cell count assumes the maximum displayed success rate is the relevant comparison.
- Visual inspection confirms document legibility and qualitative content, not human imperceptibility.
- The ar5iv rendering is an access fallback; bibliographic authority remains with arXiv and IJCAI.
- Focused searches can establish only that no implementation was located.
- Original sources remain local and are not redistributed under this package.
- Dual-use risk limits proposed implementations to defensive assessment and evidence governance.

## Observations

1. RA-AVA's spatial field is the main empirical lever; low-dimensional RI-AVA is consistently weaker in Table 1.
2. Performance is dataset-dependent: DEV is near saturation while CIFAR-10 includes much lower values.
3. Transfer behavior is not uniformly dominant; the strongest pattern is CIFAR-10, not the full matrix.
4. No-reference image-quality metrics and classification success answer different questions.
5. The prose/Table 2 discrepancy is large enough to affect comparative interpretation.
6. Zero-DCE demonstrates partial restoration, but one non-adaptive defense is too narrow for a defense claim.
7. An analytic transform does not guarantee that an optimized high-dimensional instance can be produced optically.

## Considerations

A modern evaluation should include robust and non-convolutional architectures, multiple resolutions, calibration, adaptive defenses, restoration-aware attacks, seed-level uncertainty, and matched benign vignette controls. Human participants should assess visibility, naturalness, and semantic preservation under a preregistered protocol. Any physical claim should specify lens, sensor, display or scene, illumination, capture pipeline, and repeatability. Security reporting should distinguish an authorized lab stress test from an operational evasion tool.

## Strengths

- Introduces a structured photometric threat grounded in an interpretable image-formation decomposition.
- Separates a low-dimensional physical-parameter baseline from a more expressive regional formulation.
- Evaluates four architectures across three datasets in white-box and transfer settings.
- Reports image-quality metrics with attack success and includes a preliminary restoration defense.
- Provides equations, optimization steps, parameter bounds, and step sizes.

## Weaknesses

- “Imperceptible” lacks human-subject evidence; BRISQUE and NIQE are insufficient proxies.
- “Physical” lacks an end-to-end optical realization, especially for RA-AVA's flexible field.
- The prose and Table 2 contain materially conflicting DEV values.
- Reproduction lacks code, environment, weights, full recipes, seeds, uncertainty, and compute accounting.
- Generalization is limited by the 2021 model set, three datasets, and one non-adaptive defense.

## Potential Improvements

1. Publish version-bound machine-readable tables and automatically test prose/table consistency.
2. Release code, lockfiles, checkpoints, data splits, seeds, compute/runtime records, and per-run outputs.
3. Add confidence intervals, statistical comparisons, budgets, and sensitivity analyses.
4. Conduct blinded perceptual studies with prespecified power and agreement measures.
5. Validate realizability through controlled optical acquisition.
6. Evaluate modern CNNs and transformers, feature denoising, robust training, adaptive restoration-aware attacks, and calibration.
7. Separate benign distribution-shift robustness from adversarial worst-case robustness using matched controls.

## Potential Implementations

1. **Optical robustness audit harness:** an authorized service that sweeps benign vignettes and approved stress cases, then reports accuracy, calibration, restoration response, and perceptual evidence.
2. **Result provenance validator:** a continuous-integration check that binds narrative claims to structured result cells and flags divergent values.
3. **Robustness evidence card:** a release gate recording threat coverage, seeds, uncertainty, human studies, physical tests, code/environment availability, and adaptive-defense status.

## Three Ways to Exercise This Research

1. **Reanalysis exercise:** encode Tables 1-3 as structured data, reproduce reviewer arithmetic, and audit each comparative sentence against its result cells.
2. **Benign-control exercise:** apply non-adversarial synthetic vignettes over a prespecified grid to measure ordinary photometric sensitivity before worst-case testing.
3. **Defense-triage exercise:** compare no preprocessing, Zero-DCE-like restoration, and representation denoising on authorized data while measuring accuracy, calibration, and false recovery.

## Example MVP Product

### Product name

**Optical Robustness Evidence Gate**

### User and problem

A model assurance engineer needs to decide whether a vision release has credible evidence against structured illumination failures. Existing dashboards may show attack success but omit perceptual, semantic, reproducibility, and physical-validation status.

### Core workflow

1. Register model, dataset, approved threat families, benign controls, and defense configurations.
2. Import signed, machine-readable evaluation results rather than source images or attack implementations.
3. Verify required cells, seeds, uncertainty, and prose/table consistency.
4. Display a dataset-by-model-by-threat coverage matrix with calibration and restoration deltas.
5. Hold broad imperceptibility or physicality claims until human-study and camera-test evidence is linked.

### Inputs and outputs

Inputs are evaluation summaries, provenance records, model identifiers, approved protocol metadata, and reviewer evidence links. Outputs are a coverage matrix, mismatch report, missing-evidence list, and release decision with an auditable rationale.

### Acceptance criteria

- Every reported claim resolves to a versioned result cell or an explicitly labeled inference.
- Required model/dataset/threat combinations have seed-level results and uncertainty.
- Benign-control and adversarial results are separated.
- Human and physical evidence are required for the corresponding broad claims.
- No original paper source or operational attack artifact is stored in the public report.

### Safety and failure modes

The MVP stores derived evidence, not attack-generating code or source images. It can still encourage checklist compliance without scientific validity, so reviewer override reasons and evidence quality remain visible. Missing fields produce a hold, not a guessed pass. The product does not certify security; it records the bounded basis for a release decision.

## Related Research and Reading

1. [Feature Denoising for Improving Adversarial Robustness — DEP-E review](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-Feature%20Denoising/feature_denoising_manuscript.md): representation-level defense counterpart and ablation model.
2. [ViT Semantic Robustness — DEP-E review](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-ViT%20Semantic%20Robustness/vit_semantic_robustness_manuscript.md): semantic/perceptual bridge for bounded image changes.
3. [Adversarial Label Noise — DEP-E review](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Adversarial%20Label%20Noise/adversarial_label_noise_manuscript.md): threat-objective alignment, calibration, and held-out evaluation.

These three entries were selected for concrete conceptual overlap, not by a fixed related-entry index.

## Source References

1. Binyu Tian, Felix Juefei-Xu, Qing Guo, Xiaofei Xie, Xiaohong Li, and Yang Liu. “AVA: Adversarial Vignetting Attack against Visual Recognition.” IJCAI 2021. [arXiv](https://arxiv.org/abs/2105.05558) · [publisher page](https://www.ijcai.org/proceedings/2021/145) · [DOI](https://doi.org/10.24963/ijcai.2021/145)
2. Public full-paper endpoints used for provenance: [arXiv PDF](https://arxiv.org/pdf/2105.05558) · [arXiv source](https://arxiv.org/e-print/2105.05558) · [ar5iv full-paper rendering](https://ar5iv.labs.arxiv.org/html/2105.05558)
3. [Papers with Code paper record](https://paperswithcode.com/paper/ava-adversarial-vignetting-attack-against), used only as a secondary implementation locator.

## Appendix

### A. Selected hyperparameters reported by the paper

| Item | Reported value |
|---|---|
| Attack iterations | 40 |
| Step sizes for inverse focal length / geometric attenuation | 0.0125 / 0.0125 |
| Step sizes for tilt magnitude / tilt angle | 0.01 / 0.01 |
| Step size for tunable geometric field | 0.0125 |
| Bounds for inverse focal length / geometric attenuation | 0.5 / 0.5 |
| Bounds for tilt magnitude / tilt angle | π/6 / π/6 |
| Norm / regional parameter | infinity norm / `z = 1.0` |
| Regularization weights | all reported as 1 |

### B. Confidence and unresolved questions

Confidence is high that the bibliographic metadata, equations, displayed values, and discrepancy are faithfully recorded. Confidence is moderate that the comparative interpretation generalizes beyond the displayed tables. Confidence is low for human imperceptibility, physical realizability, or effectiveness against modern defended systems because those were not established by the inspected evidence.

The highest-value next evidence would be a corrected machine-readable Table 2, a reproducible implementation with seed-level outputs, a blinded perceptual protocol, and a controlled camera realization. Until then, AVA is best treated as a historically important structured digital robustness probe rather than a demonstrated physical attack system.
