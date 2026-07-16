---
title: "CorrKD Missing Modal - DEP-E"
generated_at: "2026-07-16 (date-only public marker)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of correlation-decoupled knowledge distillation for multimodal sentiment analysis under incomplete modalities."
source_status: "verified local PDF, official full-paper HTML, metadata HTML, and source package; public URLs only in deposit"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "arXiv v2 revised 2024-06-10; official CVPR and code-availability context checked through 2026-07-16"
primary_url: "https://arxiv.org/abs/2404.16456v2"
stable_identifier: "arXiv:2404.16456v2; DOI 10.48550/arXiv.2404.16456"
confidence_summary: "High for identity and source-reported method/tables; medium for comparative interpretation; low for independent reproduction and natural-missingness generalization."
safety_scope: "consent-based offline research only; no consequential emotion or sentiment inference"
distribution_notes: "Generated Markdown and public URLs only; all source files, media, extracted text, and caches withheld locally."
---

# CorrKD Missing Modal - DEP-E

## Source Metadata

| ID | Source | Role | Identifier | Public locator | Status / Notes |
|---|---|---|---|---|---|
| S1 | arXiv record | metadata | arXiv:2404.16456v2 | https://arxiv.org/abs/2404.16456v2 | Inspected; v1 2024-04-25, v2 2024-06-10 |
| S2 | arXiv bundle | primary paper | PDF, HTML, TeX/source | https://arxiv.org/pdf/2404.16456; https://arxiv.org/html/2404.16456; https://arxiv.org/e-print/2404.16456 | Private verified copies fully inspected; none redistributed |
| S3 | CVF open access | venue record | CVPR 2024, 12458-12468 | https://openaccess.thecvf.com/content/CVPR2024/html/Li_Correlation-Decoupled_Knowledge_Distillation_for_Multimodal_Sentiment_Analysis_with_Incomplete_Modalities_CVPR_2024_paper.html | Official metadata inspected |
| S4 | arXiv DOI | persistent ID | 10.48550/arXiv.2404.16456 | https://doi.org/10.48550/arXiv.2404.16456 | Verified |
| S5 | cache summary | process evidence | schema 1.0, `cached` | source URLs in S1-S2 | PDF/HTML/source extraction succeeded; local details withheld |
| S6 | Black Lake authority | deposition rules | live main | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Fetched/read before batch writing |
| S7 | AV Emotion Fusion | related DEP | DEP-E-20260713 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-AV%20Emotion%20Fusion/av_emotion_fusion_manuscript.md | Inspected |
| S8 | VLM Probing | related DEP | DEP-E-20260712 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md | Inspected |
| S9 | KDFlow LLM Distill | related DEP | DEP-E-20260712 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-KDFlow%20LLM%20Distill/kdflow_llm_distill_manuscript.md | Inspected |

The ten authors are Mingcheng Li, Dingkang Yang, Xiao Zhao, Shuaibing Wang, Yan Wang, Kun Yang, Mingyang Sun, Dongliang Kou, Ziyun Qian, and Lihua Zhang. CVPR records the paper in its 2024 proceedings at pages 12458-12468. No official CorrKD implementation was linked by the paper, arXiv, or CVPR page, and targeted searches found no declared implementation.

## Evidence Ledger

| ID | Evidence | Supports | Confidence | Limitations |
|---|---|---|---|---|
| E1 | S1, S3, S4 metadata | identity, authors, dates, venue, pages | High | not empirical validation |
| E2 | S2 Sections 3 and equations | teacher/student flow, SCD, CPD, RCD, total objective | High for reporting | not independently implemented |
| E3 | S2 Section 4, tables and figures | datasets, baselines, conditions, ablations, results | High for transcription; medium for inference | seed-level results unavailable |
| E4 | S2 implementation details | feature extractors, hyperparameters, five seeds | Medium-high | incomplete environment/split manifest |
| E5 | S5 | complete source gate and cache coverage | High | extracted text can be noisy |
| E6 | S7-S9 | cross-DEP conceptual overlap | Medium-high | does not validate CorrKD |
| E7 | dedup/process scans | first-draw eligibility | High | depends on indexed public text |

## Executive Summary

CorrKD addresses missing language, audio, or visual input in multimodal sentiment analysis by distilling a complete-modality teacher into an incomplete-modality student. Teacher and student share the same network structure but different parameters. The teacher is trained on complete inputs and frozen. Modality Random Missing replaces selected frame features with zero vectors and can remove whole modalities for student training; only the student runs at inference.

Three objectives transfer different relationships. Sample-level Contrastive Distillation pulls same-sample teacher/student representations together and separates cross-sample pairs. Category-guided Prototype Distillation aligns each sample's cosine-similarity pattern to mini-batch category prototypes. Response-disentangled Consistency Distillation separates target and non-target probabilities and maximizes teacher/student mutual-information estimates for each response part. These join task cross-entropy without reported weighting coefficients.

Experiments use MOSI, MOSEI, and IEMOCAP; Glove, COVAREP, and Facet features; random frame drops and six whole-modality availability patterns; seven baselines; and five seeds. CorrKD reports the best missing-condition average in the MOSI/MOSEI table, but not every individual condition or complete-modality result. On MOSI, its average is 74.69 weighted F1 versus GCNet's 73.84; complete-modality Self-MM is 84.64 versus CorrKD's 83.94.

Reviewer assessment: the ablations support that all three added components matter in the tested MOSI protocol, but they do not show that “correlation decoupling” uniquely causes the gain. Missingness is synthetic, loss and tuning budgets differ, seed uncertainty is absent, and code/splits are unavailable. Natural sensor loss, transcript failure, privacy withholding, speaker/session shift, fairness, calibration, and consequential-use risk remain open.

## Detailed Summary

### Problem and Input Model

Each sample has language, audio, and visual sequences. Intra-modality missingness removes frame-level features; inter-modality missingness removes complete streams. The task is utterance-level sentiment or emotion classification. Zero replacement makes the experiment reproducible but introduces a conspicuous artificial token that may differ from natural dropout, asynchrony, silence, occlusion, or privacy-driven absence.

### Encoder and Teacher/Student Flow

Each modality passes through temporal convolution, positional encoding, and a Transformer encoder. Encoded streams are concatenated and globally averaged into a joint representation. The teacher is first trained on complete samples and frozen. Complete samples feed the teacher while masked copies feed the student. At inference, the teacher is removed.

### Sample-Level Contrastive Distillation

For a mini-batch, the loss minimizes distance between student and teacher representations of the same sample and uses a margin to separate a student representation from other samples' teacher representations. The formulation depends on batch composition, margin `eta`, embedding scale, and pair count. Large or biased batches can change the effective supervision.

### Category-Guided Prototype Distillation

Each category prototype is the mini-batch mean representation for that label. Teacher and student calculate sample-to-prototype cosine matrices, and CPD minimizes their difference. This transfers within- and between-category geometry. The paper does not specify behavior when a class is absent from a batch, and small-class prototypes may be noisy.

### Response-Disentangled Consistency Distillation

Softmax responses are split into the target probability and remaining non-target probabilities. The method estimates teacher/student mutual information with a Jensen-Shannon-based statistical network and maximizes it for each response part. This aims to prevent a confident target probability from suppressing non-target boundary knowledge. The estimator architecture and sampling details are not sufficient for exact independent reconstruction.

### Experimental Design

MOSI has 2,199 clips, MOSEI 22,856, and the selected IEMOCAP subset 4,453. MOSI/MOSEI report positive-versus-negative weighted F1; IEMOCAP reports per-class F1 for happy, sad, angry, and neutral. Language uses 300-dimensional Glove features, audio uses 74-dimensional COVAREP, and visual uses 35 Facet action-unit features.

The authors report PyTorch on NVIDIA V100, Adam, dataset-specific learning rates, batch sizes, epochs, attention heads, and margins; embedding dimension is 40. Hyperparameters are selected on validation data. Results average five seeds, but individual values, standard deviations, tests, code, and exact environment are unavailable.

### Results and Ablations

Under whole-modality patterns, CorrKD leads the reported missing-condition averages: 74.69 on MOSI and 74.02 on MOSEI, compared with GCNet at 73.84 and 73.54. CorrKD is not best in every column. It trails Self-MM on complete MOSI (83.94 versus 84.64) and DMD on complete MOSEI (82.16 versus 84.78).

MOSI ablations reduce the missing-condition average from 74.69 to 72.46 without SCD, 71.81 without CPD, and 73.27 when RCD is replaced by KL. These comparisons support component contribution within one protocol. They do not control for training compute, objective weighting, teacher advantage, or independent hyperparameter tuning.

The source notes language dominance: language-only is stronger than audio-only or visual-only, and modality combinations containing language often perform best. This can reflect useful linguistic signal, transcript/dataset bias, feature-quality imbalance, or weaker non-language sensors.

## Key Claims and Evidence

| Claim | Evidence | Calibration |
|---|---|---|
| CorrKD improves robustness under simulated missingness. | curves and inter-modality tables | Supported for tested masks/datasets; not natural failure |
| Cross-sample transfer matters. | `w/o SCD` MOSI ablation | Component association, not unique causal mechanism |
| Prototype geometry matters. | `w/o CPD` largest average drop | Source-supported in one dataset/protocol |
| Response disentanglement beats KL replacement. | `w/o RCD` row | Narrow objective comparison; estimator details incomplete |
| Language dominates. | uni/bimodal table patterns | Descriptive and dataset-dependent |

## Methodology

The source-first workflow uniformly drew zero-based index 52,075 from 75,776 unique PDF-parent units enumerated with `rg`. Dedup checked IDs, DOI, normalized title, slug, repository artifacts, memory, active work, and the companion repository; the first draw was eligible.

The unit began `partial`: a valid 1,273,346-byte PDF but no full-paper HTML. Bounded official arXiv repair added 511,017-byte HTML with 79,155 body characters, 23 headings, five structure terms, metadata HTML, and a 13-entry source archive; zero partials remained. Local provenance records were updated. The missing central cache was backfilled in `missing-only` mode in 1.013 seconds via `pypdf`, `html-regex`, and `tarfile`, producing 52,926, 75,382, and 115,172 text bytes.

Review covered TeX, HTML, PDF text, formulas, tables, figures/captions, official CVPR metadata, code availability, and exactly three related DEP manuscripts. No experiment or code was executed.

## Scope, Constraints, and Assumptions

- Inputs are pre-extracted, word-aligned language/audio/visual features rather than raw streaming sensors.
- Missingness is simulated with zero vectors or whole-stream removal.
- Train/validation/test split lineage is inherited from source datasets and not independently audited.
- Batch composition affects contrastive negatives and category prototypes.
- Five-seed averaging is reported without dispersion or significance tests.
- Teacher and student share architecture; teacher privilege comes from complete inputs and pretraining.
- No natural missingness, cross-dataset transfer, calibration, subgroup, or field evaluation is reported.
- Emotion/sentiment inference is consent-sensitive and unsuitable for consequential decisions here.

## Observations

1. CorrKD transfers relational structure rather than attempting pixel/audio/text reconstruction.
2. The strongest MOSI ablation drop is associated with prototype distillation.
3. Complete-modality performance is not uniformly improved, showing a robustness trade-off.
4. Language dominance makes “multimodal” gains condition-dependent.
5. Zero masks can become shortcuts unless corruption mechanisms vary.

## Considerations

- Use group-disjoint speaker/session splits before masking.
- Preserve mask manifests and generate descendants only after splitting.
- Report per-seed intervals and paired condition tests.
- Add burst, timing, corruption, device, and not-missing-at-random failures.
- Audit transcript leakage and modality contribution with interventions.
- Gate any public artifact against raw media, identity, or consequential-use leakage.

## Strengths

- Covers both partial-stream and entire-stream absence.
- Separates transfer into sample, category, and response relationships.
- Evaluates three established datasets and seven baselines.
- Reports multiple missing conditions and component ablations.
- Uses teacher-free student inference.

## Weaknesses

- No official implementation, split manifest, checkpoints, or raw seed results.
- Synthetic zero missingness may be easy to detect and unlike deployment failures.
- Several gains are small and lack uncertainty.
- Ablations do not equalize compute and tuning budgets.
- Prototype and MI-estimator edge cases are under-specified.
- No privacy, fairness, calibration, consent, or consequential-use analysis.

## Potential Improvements

1. Release pinned code, features, masks, splits, checkpoints, configs, and seed tables.
2. Split by speaker/session before generating masks and verify descendant lineage.
3. Evaluate structured and natural missingness plus cross-dataset transfer.
4. Report paired uncertainty, calibration, and subgroup results per condition.
5. Isolate teacher privilege, loss count, compute, and tuning budget.
6. Probe modality dominance and shortcuts with causal interventions.
7. Document consent, retention, privacy, and prohibited-use boundaries.

## Potential Implementations

### Missingness Matrix Runner

Creates versioned masks for frame blocks, bursts, delayed streams, whole streams, and conditional absence; runs pinned baselines and produces per-condition, per-seed evidence.

### Distillation Relationship Auditor

Compares task-only, conventional KD, SCD, CPD, RCD, and matched-compute combinations while logging batch composition, prototype coverage, estimator behavior, calibration, and representation probes.

### Consent-Bounded Research Workbench

Runs only on authorized datasets, strips identities/raw media from outputs, exports aggregate metrics, supports human review, and contains no live or consequential inference interface.

## Three Ways to Exercise This Research

1. `Mask-mechanism challenge`: compare zero, noise, contiguous burst, delayed, and whole-stream masks on a small licensed dataset; succeed when manifests replay exactly; stop if split descendants can leak.
2. `Matched-budget ablation`: compare loss combinations under equal steps and tuning budgets; succeed with paired seed intervals; stop if teacher/student versions are unpinned.
3. `Modality-shortcut probe`: mask transcript cues and perturb audio/visual evidence independently; succeed when behavioral and representation changes agree; stop before any consequential user inference.

## Example MVP Product

**Missing Modality Evidence Lab** is an offline runner for one authorized audiovisual dataset and one teacher/student architecture. It registers speaker/session-disjoint splits, generates versioned masks, trains matched-budget variants across seeds, computes condition-level F1 and calibration, runs modality probes, and exports a public-safe evidence card. It never exports raw media or produces decisions about real people.

## Related Research and Reading

### Exactly Three Related DEP Entries

1. [AV Emotion Fusion](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-AV%20Emotion%20Fusion/av_emotion_fusion_manuscript.md) - same IEMOCAP/audio-video domain and fusion/corruption boundary.
2. [VLM Probing](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md) - representation fusion, modality importance, leakage, and intervention probes.
3. [KDFlow LLM Distill](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-KDFlow%20LLM%20Distill/kdflow_llm_distill_manuscript.md) - teacher/student dataflow, parity, resource, and versioning controls.

### Primary and Near-Primary Reading

- CorrKD primary paper: https://arxiv.org/abs/2404.16456v2
- CVPR open-access record: https://openaccess.thecvf.com/content/CVPR2024/html/Li_Correlation-Decoupled_Knowledge_Distillation_for_Multimodal_Sentiment_Analysis_with_Incomplete_Modalities_CVPR_2024_paper.html
- Contrastive Representation Distillation: https://arxiv.org/abs/1910.10699
- Decoupled Knowledge Distillation: https://arxiv.org/abs/2203.08679

## Source References

1. Li et al. CorrKD. https://arxiv.org/abs/2404.16456v2
2. Full PDF. https://arxiv.org/pdf/2404.16456
3. Full HTML. https://arxiv.org/html/2404.16456
4. Source package. https://arxiv.org/e-print/2404.16456
5. CVPR record. https://openaccess.thecvf.com/content/CVPR2024/html/Li_Correlation-Decoupled_Knowledge_Distillation_for_Multimodal_Sentiment_Analysis_with_Incomplete_Modalities_CVPR_2024_paper.html
6. arXiv DOI. https://doi.org/10.48550/arXiv.2404.16456
7. Black Lake authority. https://github.com/Delphoa/Black-Lake/blob/main/README.md

## Appendix

### Replication Checklist

- Pin raw-feature versions and speaker/session splits.
- Generate masks only after splitting and retain manifests.
- Pin teacher/student code, weights, feature dimensions, and loss weights.
- Define absent-category behavior for prototypes and MI-estimator sampling.
- Publish all seed values, intervals, calibration, subgroup, and condition metrics.
- Compare matched-compute task-only and conventional-KD controls.

### Source-Withholding Confirmation

No PDF, HTML, metadata page, TeX/source archive, media, figure, cache, extracted source text, or local archive path is deposited. Only generated public-safe Markdown and public URLs are published.
