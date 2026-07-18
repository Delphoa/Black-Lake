---
title: "Pixel-Point Transfer - DEP-E"
generated_at: "2026-07-18"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of contrastive pixel-to-point knowledge transfer from pretrained 2D networks into 3D backbones."
source_status: "verified local source bundle; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-18"
temporal_cutoff: "arXiv v3 dated 2021-12-27; public context checked through 2026-07-18"
primary_url: "https://arxiv.org/abs/2104.04687v3"
stable_identifier: "arXiv:2104.04687v3; DOI:10.48550/arXiv.2104.04687"
confidence_summary: "High for source reporting, medium for causal interpretation, and low for independent reproducibility because experiments were not rerun and no official code repository was established."
safety_scope: "non-sensitive research review and synthetic evaluation design"
distribution_notes: "Original PDF, HTML, metadata, TeX/source, extracted text, caches, and verification records remain local and were not redistributed."
---

# Pixel-Point Transfer - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public URL | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | *Learning from 2D: Contrastive Pixel-to-Point Knowledge Transfer for 3D Pretraining* | Primary paper metadata | arXiv abstract/metadata | `2104.04687v3`; 2021-12-27 | https://arxiv.org/abs/2104.04687v3 | arXiv access; redistribution terms not inferred | 2026-07-18 | Inspected |
| S2 | Complete paper | Primary artifact | PDF | SHA-256 `e2c94c8525a96aef366fc431deca5a3f71f0a1a864914c2abdcaf8b8873e6b69` | https://arxiv.org/pdf/2104.04687 | Local file withheld; public URL cited | 2026-07-18 | Inspected and integrity-verified |
| S3 | Complete paper HTML | Primary artifact | ar5iv full-paper HTML | 273,704 bytes; verified document | https://ar5iv.labs.arxiv.org/html/2104.04687 | Fallback rendering; local file withheld | 2026-07-18 | Inspected and integrity-verified |
| S4 | TeX/source package | Primary artifact | Source archive | SHA-256 `94a0f3e7fea825358e58de392e38f30afbdf3729962460d415d99993f651c700`; 21 entries | https://arxiv.org/e-print/2104.04687 | Source package withheld; no redistribution claim | 2026-07-18 | Inspected; inventory readable |
| S5 | Yueh-Cheng Liu publication page | Author context | Website | Current page snapshot | https://liu115.github.io/ | Author-maintained public page | 2026-07-18 | Inspected |
| S6 | HERMES World Model DEP-E | Related processed artifact | Markdown manuscript | `DEP-E-20260712-HERMES World Model` | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model/hermes_world_model_manuscript.md | Repository-generated synthesis | 2026-07-18 | Inspected |
| S7 | CorrKD Missing Modal DEP-E | Related processed artifact | Markdown manuscript | `DEP-E-20260716-CorrKD Missing Modal` | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-CorrKD%20Missing%20Modal/corrkd_missing_modal_manuscript.md | Repository-generated synthesis | 2026-07-18 | Inspected |
| S8 | VideoWeave Geometry DEP-E | Related processed artifact | Markdown manuscript | `DEP-E-20260709-VideoWeave Geometry` | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md | Repository-generated synthesis | 2026-07-18 | Inspected |

**Paper authors:** Yueh-Cheng Liu, Yu-Kai Huang, Hung-Yueh Chiang, Hung-Ting Su, Zhe-Yu Liu, Chin-Tang Chen, Ching-Yu Tseng, and Winston H. Hsu.

**Platform and dates:** arXiv, Computer Vision and Pattern Recognition (`cs.CV`); initial submission 2021-04-10; inspected revision v3 dated 2021-12-27.

**Identifiers:** arXiv `2104.04687v3`; arXiv-issued DOI https://doi.org/10.48550/arXiv.2104.04687. No separate published DOI or proceedings/journal record was established. The author page continues to list the work as an arXiv preprint and exposes no official code link for this item.

**Local paths:** Withheld from this public artifact by policy. Source identity is preserved through public URLs, byte counts, hashes, and verification results.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Title, authors, subject, version history, abstract, arXiv DOI | Identity and temporal scope | High | Abstract does not establish detailed empirical claims |
| E2 | S2-S4 | Primary full paper and source | Method equations, architecture, dataset setup, tables, supplement, pseudocode, figure captions | Mechanism, experiments, results, and internal consistency checks | High for source reporting | Local integrity does not imply scientific reproduction |
| E3 | S2-S4, Table III and included ScanNet table | Primary empirical evidence | S3DIS and ScanNet rows | Transfer gains and task dependence | High for table transcription | Author-reported validation results; no repeated-seed intervals |
| E4 | S2-S4, SUN RGB-D and ablation tables | Primary empirical evidence | Detection rows, PPNCE/PPKD comparison, teacher ablation | Loss and teacher comparisons | High for table transcription | Compute and tuning budgets are not fully decomposed |
| E5 | S4 source text and supplement | Primary reproducibility evidence | Hyperparameters, one-seed statement, pseudocode, dataset/split details | Partial reconstruction boundary | Medium-high | No full training implementation, environment, or checkpoints |
| E6 | S5 | Author context | Current venue label and visible links | Preprint and code-availability status | Medium-high | Page is time-sensitive and not an archival code search |
| E7 | S6-S8 | Related DEP artifacts | Spatial transfer, contrastive distillation, feature adaptation, evaluation constraints | Cross-DEP synthesis | Medium | Related works do not validate PPKT |
| E8 | Selection and local verification records | Process evidence | Random draw, dedup results, hashes, document checks | Provenance and source completeness | High | Private paths and exact execution time intentionally withheld |

## Executive Summary

The paper proposes contrastive pixel-to-point knowledge transfer (PPKT), a pretraining method that transfers semantic structure from a frozen 2D network into a sparse 3D network. Aligned RGB-D frames and camera intrinsics create pixel-point correspondences. A learned upsampling feature projection restores high-level 2D features to pixel resolution, a 3D projection head maps point features into the same embedding space, and a point-pixel NCE objective pulls each point toward its matching pixel while contrasting it with other pixels.

In the authors' indoor RGB-D experiments, PPKT improves S3DIS semantic segmentation and SUN RGB-D/ScanNet object detection over training from scratch and the listed PointContrast baseline. The clearest displayed gains are S3DIS mean IoU 68.28 versus 65.16 from scratch, ScanNet detection 59.67 versus 56.50 at IoU 0.25 and 38.90 versus 34.54 at IoU 0.5, and SUN RGB-D detection 57.26 versus 55.21 at IoU 0.25. Full-data ScanNet semantic segmentation changes only from 69.49 to 69.56, while the paper reports a larger gap under 15% labels. This supports a constraint-aware interpretation: the transferred prior is more useful for detection and label-scarce fine-tuning than for a saturated same-dataset segmentation setting.

Confidence is high that this artifact accurately reports the inspected source, medium that local correspondence plus contrastive learning explains the observed gains, and low for independent reproducibility or broad generalization. The source describes one matched random seed, does not expose a complete official code repository, uses ScanNet for both pretraining and some fine-tuning, and reports inconsistent improvement arithmetic in two narrative passages. The practical contribution is best treated as an auditable transfer pattern—correspondence, adapter, relational objective, constrained evaluation—rather than a universal recipe.

## Detailed Summary

### Problem and Background

Supervised pretraining is routine in 2D vision because large labeled image datasets and mature backbones provide reusable representations. Equivalent 3D pretraining is harder: point-cloud datasets are smaller, labeling 3D scenes is expensive, sensors vary, and many sparse 3D networks are trained from scratch. PointContrast had already shown that point-to-point contrastive pretraining could initialize 3D networks from unlabeled 3D data. The paper argues that pure 3D self-supervision leaves semantic knowledge from mature 2D networks unused.

A pilot ScanNet study trains a 2D FCN for semantic segmentation and aggregates its multi-view predictions back into 3D. ImageNet pretraining raises 2D mIoU from 45.38 to 51.13 and 3D mIoU from 40.46 to 45.27. The pilot does not prove that a 3D network can inherit this knowledge, but it motivates a transfer method that operates on the physical correspondence between an RGB pixel and a depth-derived 3D point.

### Mechanism

Let the RGB image and aligned depth map define a back-projection function. The function produces a single-view point cloud and can also lift an image feature map into features attached to those points. The 2D teacher is a pretrained ResNet. The 3D student is SR-UNet34, a sparse encoder-decoder with pointwise output suitable for semantic segmentation and compatible with VoteNet-style detection heads.

Common image backbones produce semantically rich but spatially coarse final feature maps. PPKT adds an upsampling feature projection layer (UPL) to increase the 2D feature resolution and map its channels into the shared embedding width. A 3D projection layer maps the student's per-point features into that width. Back-projection then aligns each restored pixel feature with its corresponding point feature.

For sampled aligned pairs, point-pixel NCE forms a similarity matrix. The diagonal contains physical correspondences; off-diagonal elements act as negatives. Cross-entropy over the diagonal labels attracts corresponding point/pixel features and separates mismatched pairs. The 2D backbone remains frozen, while the UPL, 3D backbone, and 3D projection are optimized. The design transfers local structure into the full 3D encoder-decoder rather than reducing each scene to a single global representation.

### Data and Training

The pretraining corpus is approximately 100,000 RGB-D frames from ScanNet, obtained by subsampling every twenty-fifth frame across 1,513 scans and 707 distinct spaces. Default PPKT uses ImageNet-pretrained ResNet50 layer-4 features, SR-UNet34, 128-dimensional projected features, temperature 0.04, 2.5 cm voxels, 480 by 640 images, momentum SGD at learning rate 0.5 with weight decay `1e-4`, and 60,000 iterations on one V100 GPU with batch size 24. Two-dimensional augmentation includes horizontal flip and random resize; 3D augmentation includes scaling, rotation, and elastic distortion.

The same pretrained 3D weights initialize all downstream tasks. S3DIS segmentation uses Area 5 validation, one V100, batch 32, and 15,000 iterations. SUN RGB-D detection uses the official split, ten common classes, one V100, batch 64, and 180 epochs. ScanNet segmentation uses 949/525 train/validation scenes for model selection and evaluates on the original validation set, with four V100 GPUs and 15,000 iterations. ScanNet detection follows the cited VoteNet/PointContrast preprocessing and training protocol.

### Results and Ablations

On S3DIS, PPKT reports mean accuracy 75.19 and mean IoU 68.28. PointContrast reports 73.97/66.86, while scratch reports 73.24/65.16. Global KD, global CRD, and global L2 transfer do not match PPKT's mean IoU. This comparison supports the authors' position that local transfer and encoder-decoder pretraining matter, but it does not isolate UPL capacity, negative sampling, teacher strength, or extra compute individually.

On SUN RGB-D, PPKT reports 57.26 at `mAP@0.25` and 33.92 at `mAP@0.5`. It leads the listed rows at 0.25 but not at 0.5, where CRD reports 34.30. On ScanNet detection, PPKT reports 59.67/38.90, leading PointContrast's 58.30/36.26 and scratch's 56.50/34.54. Full-data ScanNet segmentation barely changes, but the authors report that PPKT's advantage grows as the labeled fine-tuning fraction falls to 50%, 30%, and 15%.

The backbone ablation reports a +1.73 mean-IoU gain for SR-UNet18 and +3.12 for SR-UNet34 on S3DIS. The loss/teacher ablation reports ADE20K PPNCE at 58.03 `mAP@0.25`, ADE20K pixelwise KD at 56.07, default ImageNet PPNCE at 57.26, and scratch at 55.21. A MoCo-pretrained ResNet50 teacher is nearly tied with the supervised ImageNet teacher on the two detection tasks, indicating that labeled teacher pretraining is not a necessary property of the transfer mechanism.

### Internal Consistency

Displayed tables and narrative claims are not fully consistent. The S3DIS table difference is 68.28 minus 65.16, or 3.12 points, while one result paragraph says 3.34. The SUN RGB-D table difference is 57.26 minus 55.21, or 2.05 points, while one paragraph says 2.28. A per-class S3DIS table rounds the final mean IoU to 68.27. This artifact uses table values for derived arithmetic and retains the conflicting prose as a source limitation.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Local pixel-point contrastive transfer can initialize a 3D backbone from a pretrained 2D network without labels in the transfer corpus. | Author method claim | E2, E5 | The source implements the mechanism in equations and pseudocode. “Without labels” applies to transfer data, not necessarily the teacher's original training. | High for mechanism |
| C2 | UPL makes coarse high-level 2D features usable at point granularity. | Author architectural claim | E2 | The layer addresses a real shape mismatch; its isolated contribution is not fully separated from the rest of PPKT in the reviewed tables. | Medium-high |
| C3 | PPKT improves S3DIS segmentation and SUN RGB-D/ScanNet detection over scratch. | Author empirical claim | E3, E4 | Displayed tables support the claim in the tested protocols, with metric-specific exceptions and no independent reproduction. | Medium-high |
| C4 | Local transfer is more effective than the listed global 2D-to-3D baselines. | Author comparative claim | E3, E4 | PPKT leads the central mean-IoU and `mAP@0.25` rows, but architecture coverage and tuning budgets complicate causal attribution. | Medium |
| C5 | PPKT is most useful for larger students or limited labeled fine-tuning. | Author empirical interpretation | E3, E4 | Backbone and label-fraction ablations support the pattern within the study; no external-domain confirmation is provided. | Medium |
| C6 | A self-supervised 2D teacher can replace the supervised ImageNet teacher. | Author ablation claim | E4 | MoCo and supervised teachers are approximately tied on two detection metrics; broader teacher families are untested. | Medium-high |
| C7 | Correspondence, adapter, and relational objective form a reusable transfer pattern. | Reviewer interpretation | E2, E7 | Mechanistically coherent and echoed by related DEP entries, but not itself an author-tested generalization. | Medium |

## Methodology

- `Research objective`: Preserve the paper's mechanism, evidence, limitations, and implementation relevance as a schema-complete DEP-E manuscript.
- `Sources inspected`: Verified PDF, full-paper HTML, metadata HTML, TeX/source package, supplement, included tables, pseudocode, figure captions, author publication page, repository READMEs, publication index, automation memory, and exactly three related DEP manuscripts.
- `Discovery strategy`: Enumerated local PDFs with `rg`, treated unique PDF parents as paper units, resolved arXiv IDs from adjacent records, used uniform rejection sampling, scanned dedup sources by stable identifiers/title/slug, inspected local full text source-first, and checked public primary/author records.
- `Inclusion criteria`: Evidence had to establish source identity, expose full method/results/limitations, document source integrity or repository rules, or provide concrete overlap in spatial representation transfer, contrastive teacher/student alignment, or feature adaptation.
- `Exclusion criteria`: Abstract-only content was excluded from empirical support; secondary summaries were discovery-only; unverified code repositories and papers merely mentioned as background were not treated as evidence.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, and replication analysis.
- `Evidence handling`: Major claims map to evidence IDs; source claims, table arithmetic, reviewer interpretation, and related-DEP synthesis are labeled separately.
- `Uncertainty handling`: Missing code/checkpoints, single-seed evidence, dataset overlap, unresolved arithmetic discrepancies, and non-executed experiments remain explicit.
- `Extraction process`: Read full HTML and TeX source, inspected table rows and supplement text, inventoried source archive entries, and verified PDF/HTML structure and hashes before synthesis.
- `Version control`: Paper evidence is pinned to arXiv v3; public repository authority was read from the live default branch.
- `Claim selection`: Prioritized the transfer mechanism, dataset/task coverage, headline tables, ablations, contradictions, and implementation boundaries.
- `Cross-checking`: Recomputed simple table differences and compared narrative numbers against displayed rows.
- `Safety handling`: Examples use synthetic or authorized inputs and do not expose local paths or source documents.
- `Reviewer stance`: Source-grounded summary, critique, replication planning, product translation, and DEP-ready preservation.

## Scope, Constraints, and Assumptions

- `Scope`: PPKT's 2D-to-3D transfer mechanism, indoor RGB-D experiments, result tables, ablations, evidence quality, related DEP concepts, and bounded implementation paths.
- `Temporal boundary`: Paper v3 dated 2021-12-27; public code/venue and repository context checked through 2026-07-18.
- `Evidence limits`: Training was not rerun; datasets and checkpoints were not downloaded; no official full implementation repository or independent replication was established.
- `Assumptions`: Displayed table cells are treated as the best source for arithmetic when prose conflicts; the verified source package corresponds to the inspected v3 paper.
- `Constraints`: Public artifact sanitization, source-file non-redistribution, compute limits, dataset terms, and the privacy implications of real RGB-D scenes.
- `Out of scope`: Production robotics deployment, safety certification, outdoor LiDAR validation, legal review of datasets, and claims about current state of the art.
- `Intended use`: DEP deposition, research review, replication planning, cross-modal system design, and evaluation-backlog creation.
- `Audience`: 3D vision researchers, multimodal engineers, representation-learning reviewers, robotics teams, and Black Lake maintainers.
- `Depth target`: Full manuscript report with implementation and evidence translation.
- `Reproducibility boundary`: Source equations, pseudocode, tables, and many settings are available; exact environment, code, checkpoints, all split manifests, and tuning history are not.
- `Operational boundary`: The artifact may guide offline synthetic or authorized experiments, not consequential perception decisions.
- `Data sensitivity`: Public research documents; any real RGB-D replication data remains subject to its dataset license and privacy/governance controls.

## Observations

- `Observed pattern`: Local PPKT improves the central S3DIS and detection metrics, while global teacher/student baselines are weaker in those rows.
- `Observed pattern`: Full-data same-dataset ScanNet segmentation shows almost no gain; the reported benefit becomes clearer under label scarcity and detection objectives.
- `Technical implication`: The physical alignment operator and UPL are part of the learning hypothesis. Calibration and resolution cannot be treated as neutral preprocessing.
- `Contradiction or tension`: Two narrative improvement values disagree with their tables, and one table differs by 0.01 from the main S3DIS value.
- `Contradiction or tension`: PPKT leads SUN RGB-D at `mAP@0.25` but not `mAP@0.5`, so “best detection performance” is threshold-dependent.
- `Open question`: How robust is correspondence learning to depth holes, pose error, occlusion, moving objects, or asynchronous sensors?
- `Open question`: How many contrastive negatives are false negatives because different pixels/points share the same semantic class or object?
- `Reviewer hypothesis`: PPKT's largest durable value is the design rule that modality transfer should occur at the downstream task's spatial unit, with an explicit adapter and correspondence audit.

## Considerations

Aligned RGB-D is not free supervision. It requires calibrated sensors, depth validity, synchronized observations, and a visibility policy. A product or benchmark should log projection coverage, duplicate pixels, occlusion conflicts, missing depth, pose uncertainty, and augmentation-induced misalignment. Without these records, a model can appear to test representation learning while actually testing the quality of a hidden geometry pipeline.

Contrastive learning also creates semantic risks. The source labels only the matched pixel as positive; other pixels in the sampled set are negatives even when they depict the same object or class. False-negative rates can change with batch size, scene composition, subsampling, and feature resolution. Alternatives include multi-positive objectives, object/region grouping, uncertainty-weighted pairs, or debiased contrastive estimates, but each changes the method and must be evaluated independently.

Deployment claims require broader evidence. Indoor ScanNet/S3DIS/SUN RGB-D do not establish outdoor LiDAR performance, cross-sensor transfer, long-range sparsity, adverse weather, dynamic-scene robustness, or safety-critical calibration. The teacher can also transfer dataset bias. Evaluation should therefore separate representation gain, task accuracy, calibration, rare-class behavior, domain shift, and resource cost.

Real scene data may contain people, homes, workplaces, or identifiable spatial layouts. Replication should use dataset-provided governance, access controls, retention rules, and output review. An MVP can begin with synthetic geometry or public toy scenes and export only aggregate evidence cards.

## Strengths

- The paper identifies a concrete missing resource—mature 2D semantic representations—and connects it to a costly 3D training problem.
- The transfer mechanism is geometrically interpretable: each positive pair has a physical pixel-point correspondence.
- UPL directly addresses the spatial-resolution mismatch between high-level image features and per-point 3D outputs.
- Evaluation spans semantic segmentation and object detection across S3DIS, SUN RGB-D, and ScanNet.
- Baselines include pure 3D contrastive pretraining and several global 2D-to-3D transfer objectives.
- Ablations cover student capacity, point-pixel loss, 2D teacher dataset/type, label fraction, and a self-supervised teacher.
- The source package includes readable pseudocode and supplementary training details rather than only a final PDF.

## Weaknesses

- No complete official implementation repository, checkpoint bundle, or executable reproduction path was established.
- One matched random seed is described; uncertainty intervals and seed sensitivity are absent.
- ScanNet is used in pretraining and later ScanNet fine-tuning, limiting claims about domain transfer.
- The aligned indoor RGB-D setting excludes many realistic camera-LiDAR, outdoor, dynamic, or poorly calibrated conditions.
- Narrative improvement numbers conflict with displayed table arithmetic.
- False-negative behavior, projection uncertainty, and correspondence errors are not isolated.
- The comparison does not fully separate the value of local alignment, UPL capacity, objective choice, total compute, and tuning budget.
- The default teacher inherits supervised ImageNet history, so “no labels” needs phase-specific wording.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release code, environments, checkpoints, splits, and table commands | Reproducibility | Source package is insufficient for exact execution | Independent verification and easier extension | Maintenance and dataset-link burden | Clean-room rerun from documented commands |
| Report at least five seeds with paired confidence intervals | Statistics | One seed cannot distinguish stable gains from run variance | More credible comparisons | Additional GPU time | Paired bootstrap or seed-level intervals |
| Use disjoint pretraining/fine-tuning scene domains | Generalization | ScanNet overlap obscures transfer | Stronger domain-transfer evidence | New data preprocessing | Cross-dataset and held-out-building protocols |
| Perturb calibration, depth, pose, and synchronization | Robustness | Correspondence is the key supervision channel | Quantified failure boundary | More experimental matrix | Controlled corruption curves and recovery tests |
| Measure multi-positive and false-negative-aware losses | Objective | Same-object/class pairs may be mislabeled as negatives | Better semantic structure and stability | Requires region/label proxies | Matched-compute ablations and retrieval probes |
| Reconcile all narrative/table arithmetic | Reporting | Current inconsistencies reduce trust | Clearer audit trail | Minimal | Automated table-to-claim checks |
| Add resource and energy accounting | Systems | Extra pretraining can be expensive | Honest cost/benefit decisions | Instrumentation | GPU-hours, memory, energy, and downstream gain ledger |

## Potential Implementations

### 1. Correspondence Integrity Gate

- `User`: Multimodal and robotics data engineers.
- `Goal`: Detect invalid pixel-point supervision before training.
- `Core mechanism`: Reproject points, measure in-frame coverage, depth agreement, duplicates, occlusion conflicts, and perturbation stability.
- `Required inputs`: Synthetic or authorized RGB-D frames, calibration, poses, and versioned preprocessing settings.
- `Outputs`: Pair-quality ledger, failure slices, visual overlays, and pass/fail policy result.
- `Risk controls`: Local-only processing for sensitive scenes, no raw-frame export, strict dataset terms, and configurable redaction.
- `Evaluation`: Synthetic ground truth, controlled calibration errors, and reviewer agreement on sampled overlays.

### 2. Cross-Modal Transfer Bench

- `User`: Representation-learning researchers.
- `Goal`: Attribute performance to correspondence, adapter, objective, teacher, and compute.
- `Core mechanism`: Run matched global KD, local L2, local contrastive, adapter-free, UPL, and multi-positive variants across fixed splits and seeds.
- `Required inputs`: Licensed small datasets, pinned teachers/students, split manifests, and compute budget.
- `Outputs`: Quality, calibration, retrieval, robustness, resource, and variance tables.
- `Risk controls`: No deployment claims, explicit data governance, budget ceilings, and automatic arithmetic checks.
- `Evaluation`: Predeclared metrics, paired seeds, confidence intervals, and held-out domains.

### 3. Sparse-Label 3D Bootstrapper

- `User`: Teams with a small labeled 3D corpus and abundant aligned sensor data.
- `Goal`: Test whether a pretrained 2D teacher reduces the labeled 3D requirement.
- `Core mechanism`: Pretrain a compact 3D backbone with audited local pairs, then fine-tune at multiple label fractions.
- `Required inputs`: Authorized aligned scenes, teacher license, calibration, labels for controlled subsets, and compute caps.
- `Outputs`: Label-efficiency curves, rare-class metrics, calibration, resource report, and model card.
- `Risk controls`: Offline use, human review, privacy controls, and no safety-critical deployment.
- `Evaluation`: Disjoint-scene splits, label-fraction curves, matched scratch/PointContrast baselines, and domain-shift tests.

## Three Ways to Exercise This Research

1. `Synthetic projection audit`: Objective - validate the correspondence assumption; inputs - a small synthetic cube/plane scene with known camera intrinsics and depth; method - project points, introduce controlled pose/depth errors, and measure valid/duplicate/occluded pairs; output - a calibration robustness card; success - errors are detected before pair quality falls below a chosen threshold; stop - if the test requires real private scene data.
2. `Frozen-feature retrieval probe`: Objective - test whether aligned pixel and point features share local structure; inputs - public toy RGB-D frames and fixed pretrained encoders; method - compute pair similarities without training, compare matched versus mismatched retrieval, and audit same-object false negatives; output - retrieval and gap distributions; success - matched retrieval exceeds a predeclared baseline with visible failure slices; stop - on unclear data terms or unbounded GPU demand.
3. `Matched-budget micro-ablation`: Objective - isolate global versus local transfer; inputs - a small licensed dataset, one compact 2D teacher, one compact 3D student, and fixed compute; method - compare scratch, global L2, local L2, and local contrastive variants across at least three seeds; output - quality/variance/resource table; success - a local method improves a predeclared target without exceeding budget; stop - if splits overlap unexpectedly or arithmetic validation fails.

## Example MVP Product

- `Product name`: PairBridge Audit Lab.
- `Target user`: 3D vision researchers and multimodal data engineers.
- `Problem`: Pixel-point transfer pipelines can hide calibration errors, false negatives, dataset overlap, and unsupported performance arithmetic.
- `Core workflow`: Register public or authorized source metadata; ingest calibration and precomputed features; audit correspondence; run small matched-budget transfer variants; compute label-efficiency and robustness slices; export a public-safe evidence card and DEP-ready Markdown.
- `Data requirements`: Synthetic scenes by default; optional licensed RGB-D scenes, calibration, split manifests, precomputed features, task labels for bounded subsets, and source/version metadata.
- `Architecture`: Local CLI, source registry, correspondence validator, feature-pair store, experiment runner, metric/arithmetic checker, policy file, and Markdown/JSON exporter.
- `Success metrics`: Complete provenance rate, invalid-pair detection recall on synthetic corruptions, seed coverage, split-overlap detection, table-to-claim consistency, and reproducible report generation.
- `Risk controls`: Local-only raw data, hash-based provenance, no face/identity analysis, dataset-license checks, GPU/disk ceilings, human approval for non-synthetic data, and no production-control output.
- `Limitations`: Does not reproduce PPKT without released code/checkpoints; toy experiments cannot establish deployment readiness; pair metrics may not predict downstream utility.
- `MVP boundary`: One compact teacher/student pair, one synthetic or public toy dataset, offline analysis, and report-only output.
- `Deployment model`: Local CLI or notebook with deterministic configuration.
- `Evaluation plan`: Unit tests for projection and arithmetic, synthetic corruption tests, three-seed smoke experiment, held-out scene check, and manual review of failure overlays.
- `Failure modes`: Incorrect calibration conventions, stale feature versions, hidden scene overlap, class imbalance, semantically false negatives, nondeterministic kernels, and misleading aggregate metrics.
- `Maintenance plan`: Pin dependencies, version dataset/split manifests, retain immutable evidence cards, and review teacher/model licenses on every upgrade.

Illustrative audit logic:

```python
def validate_run(record):
    required = {"source_id", "teacher", "student", "split_hash", "seeds", "metrics"}
    missing = sorted(required - set(record))
    if missing:
        return {"ok": False, "reason": f"missing: {missing}"}
    if len(set(record["seeds"])) < 3:
        return {"ok": False, "reason": "fewer than three unique seeds"}
    if record.get("scene_overlap", 0) > 0:
        return {"ok": False, "reason": "pretrain/fine-tune scene overlap"}
    return {"ok": True, "reason": "audit fields complete"}
```

Dependencies for a runnable system would include a pinned geometry library and ML framework; the snippet itself uses only built-in Python types. It is an audit example, not production training code.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| PointContrast | Direct 3D pretraining baseline | Point-level contrastive pretraining used as the main pure-3D comparator | https://arxiv.org/abs/2007.10985 |
| Contrastive Representation Distillation | Methodological neighbor | Relational teacher/student contrastive transfer behind a global baseline family | https://arxiv.org/abs/1910.10699 |
| A Unified Point-Based Framework for 3D Segmentation | Prior author work | Back-projects image features into 3D and motivates local multimodal fusion | https://arxiv.org/abs/1908.00478 |
| CrossPoint | Follow-on cross-modal 3D pretraining | Learns image/point and intra-point correspondences for point-cloud understanding | https://openaccess.thecvf.com/content/CVPR2022/html/Afham_CrossPoint_Self-Supervised_Cross-Modal_Contrastive_Learning_for_3D_Point_Cloud_Understanding_CVPR_2022_paper.html |
| Image-to-Point Masked Autoencoders | Follow-on 2D-to-3D transfer | Uses pretrained 2D models to guide 3D masked autoencoding | https://arxiv.org/abs/2212.06785 |
| HERMES World Model DEP-E | Related Black Lake research | Shared camera/BEV representation for 3D understanding and point-cloud generation | `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` |
| CorrKD Missing Modal DEP-E | Related Black Lake research | Same-sample contrastive and prototype relation transfer between teacher and student | `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md` |
| VideoWeave Geometry DEP-E | Related Black Lake research | Feature adapter plus geometry/video joint modeling and distillation | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2104.04687v3 | Identity, authors, dates, subject, abstract, version | 2026-07-18 | Primary metadata |
| R2 | https://arxiv.org/pdf/2104.04687 | Complete paper, figures, tables | 2026-07-18 | Local file inspected and withheld |
| R3 | https://ar5iv.labs.arxiv.org/html/2104.04687 | Complete paper HTML | 2026-07-18 | Verified fallback after official HTML failed document gate |
| R4 | https://arxiv.org/e-print/2104.04687 | TeX source, supplement, included tables, pseudocode | 2026-07-18 | Local package inspected and withheld |
| R5 | https://doi.org/10.48550/arXiv.2104.04687 | Stable arXiv DOI | 2026-07-18 | arXiv-issued DOI |
| R6 | https://liu115.github.io/ | Author-maintained venue and link context | 2026-07-18 | Lists work as arXiv preprint; no code link visible for item |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository and source-withholding rules | 2026-07-18 | Live default-branch README inspected |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E and publication-index rules | 2026-07-18 | Live default-branch README inspected |
| R9 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related-repository layout and dedup context | 2026-07-18 | Live default-branch README inspected |
| R10 | `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` | 3D representation concept bridge | 2026-07-18 | Existing processed artifact |
| R11 | `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md` | Contrastive distillation concept bridge | 2026-07-18 | Existing processed artifact |
| R12 | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Adapter and latent-distillation concept bridge | 2026-07-18 | Existing processed artifact |

## Appendix

### A. Random Selection and Deduplication

- Enumeration command: `rg --files -g "*.pdf"`.
- PDF count: 75,777.
- Unique paper-unit count: 75,776.
- Used primary IDs: 384.
- Units excluded by used ID: 156.
- Units excluded for missing safe identifier: 185.
- Locally eligible units: 75,435.
- Uniform rejection-sampling draw: zero-based raw index 42,044.
- Draw count: one; reselections: zero.
- Stable-key result: no prior synthesis by arXiv ID, arXiv DOI, normalized title, or slug; no same-paper marker in the preceding 24 hours.
- Related-repository note: metadata inventory presence was distinguished from a prior research artifact.

### B. Source-Integrity Receipt

| Artifact class | Verification |
|---|---|
| PDF | 1,563,716 bytes; `%PDF-` header; trailing `%%EOF`; SHA-256 `e2c94c8525a96aef366fc431deca5a3f71f0a1a864914c2abdcaf8b8873e6b69` |
| Full-paper HTML | 273,704 bytes; 60,602 body characters; document marker; 76 headings/sections; six structure terms; SHA-256 `219d8a2e7b90aa8a46f1b564400fd1ebcbb6363a1f7d2cda1c12d1a430f41147` |
| Metadata HTML | 43,765 bytes; provenance only; not counted as the paper |
| Source package | 1,795,790 bytes; 21 readable entries; SHA-256 `94a0f3e7fea825358e58de392e38f30afbdf3729962460d415d99993f651c700` |
| Partial state | Zero `.part` files after bounded repair |

### C. Result Reconciliation

| Result | Displayed Values | Derived Difference | Conflicting Narrative |
|---|---|---|---|
| S3DIS mean IoU | 68.28 PPKT; 65.16 scratch | +3.12 | One paragraph says +3.34; per-class table shows 68.27 |
| SUN RGB-D `mAP@0.25` | 57.26 PPKT; 55.21 scratch | +2.05 | One paragraph says +2.28 |
| ScanNet detection `mAP@0.25` | 59.67 PPKT; 56.50 scratch | +3.17 | Consistent with narrative |
| ScanNet detection `mAP@0.5` | 38.90 PPKT; 34.54 scratch | +4.36 | Consistent with narrative |

### D. Replication Checklist

- [ ] Obtain the authors' exact training repository or reconstruct it from source pseudocode with explicit deviation notes.
- [ ] Pin ResNet50 and SR-UNet34 implementations, pretrained weights, sparse-convolution library, CUDA/cuDNN, and projection-head definitions.
- [ ] Version ScanNet frame subsampling, calibration, depth filtering, scene splits, and all downstream preprocessing.
- [ ] Reproduce point-pixel pair generation and audit duplicates, occlusion, invalid depth, and augmentation alignment.
- [ ] Run scratch, PointContrast, global KD, global CRD, global L2, PPKT, and component ablations under matched compute.
- [ ] Use at least five seeds and report paired intervals, calibration, and per-class/task slices.
- [ ] Separate ScanNet-overlap experiments from cross-dataset transfer.
- [ ] Reconcile generated tables with all narrative improvement claims automatically.
- [ ] Record GPU-hours, memory, energy where available, checkpoints, failures, and data-license constraints.

No source file was uploaded, committed, attached, or copied into this DEP. Public attribution uses canonical URLs; the verified source bundle remains local.
