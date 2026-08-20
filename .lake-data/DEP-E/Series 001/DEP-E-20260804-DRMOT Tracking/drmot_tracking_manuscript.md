---
title: "DRMOT - DEP-E"
generated_at: "2026-08-04 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of RGBD referring multi-object tracking, its dataset, and its depth-aware framework."
source_status: "mixed: local source files inspected; public URLs cited; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-04"
temporal_cutoff: "Public paper revision v2 and repository context inspected through 2026-08-04."
primary_url: "https://arxiv.org/abs/2602.04692"
stable_identifier: "arXiv:2602.04692v2; DOI:10.48550/arXiv.2602.04692"
confidence_summary: "High for source transcription; medium for causal attribution and external validity; low for independent reproducibility until the promised implementation release is available."
safety_scope: "Offline, authorized research evaluation only; no control or surveillance deployment."
distribution_notes: "The PDF, full-paper HTML, metadata HTML, archive records, and any source package remain local and are not redistributed."
---

# DRMOT - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public URL | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv metadata record | Primary metadata | HTML | 2602.04692v2 | https://arxiv.org/abs/2602.04692 | Metadata page; not treated as full paper. | 2026-08-04 | Inspected |
| S2 | Full paper | Primary artifact | HTML | 2602.04692v2 | https://arxiv.org/html/2602.04692 | Full-paper rendering inspected; local copy withheld. | 2026-08-04 | Inspected in full |
| S3 | Full paper | Primary artifact | PDF | 2602.04692v2 | https://arxiv.org/pdf/2602.04692 | Local PDF passed integrity gate; file withheld. | 2026-08-04 | Integrity checked |
| S4 | arXiv-issued DOI | Stable identifier | DOI | 10.48550/arXiv.2602.04692 | https://doi.org/10.48550/arXiv.2602.04692 | Identifier only; no separate venue record established. | 2026-08-04 | Inspected |
| S5 | Official DRMOT repository | Implementation locator | GitHub | Public repository state | https://github.com/chen-si-jia/DRMOT | README, asset, and MIT license visible; code/data/weights not yet visible in inspected root. | 2026-08-04 | Inspected |
| S6 | FEMOT Tracking DEP-E | Related processed artifact | Markdown | DEP-E-20260720 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-FEMOT%20Tracking/femot_tracking_manuscript.md | Repository-generated synthesis; not validation of DRMOT. | 2026-08-04 | Inspected |
| S7 | Language-to-Space DEP-E | Related processed artifact | Markdown | DEP-E-20260727 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260727-Language-to-Space/language_to_space_manuscript.md | Repository-generated synthesis; not validation of DRMOT. | 2026-08-04 | Inspected |
| S8 | Pixel-Point Transfer DEP-E | Related processed artifact | Markdown | DEP-E-20260718 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md | Repository-generated synthesis; not validation of DRMOT. | 2026-08-04 | Inspected |

The public artifact intentionally omits local source paths and machine details. The local archive unit contains a validated PDF, full-paper HTML, metadata HTML, and verification/provenance records; the source package was unavailable through the approved acquisition route.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Title, six authors, subjects, submission/revision dates, DOI, abstract, and official code link. | Source identity and temporal scope. | High | Abstract is not sufficient for method or result claims. |
| E2 | S2/S3 | Primary paper | Introduction, related work, DRSet construction, annotation process, split, and dataset statistics. | Problem framing and dataset description. | High for transcription | Author-controlled source; no independent dataset audit. |
| E3 | S2/S3 | Primary paper | Depth-promoted grounding, format/IoU rewards, Qwen2.5-VL-3B input/output, GRPO/LoRA settings, and depth-enhanced OC-SORT equations. | Method reconstruction. | High for transcription | Code was not executed and model artifacts were not available. |
| E4 | S2/S3 | Primary paper | Tables 3–5, HOTA/DetA/AssA metrics, depth ablation, GRPO ablation, and alpha sensitivity. | Author-reported empirical claims. | High for table transcription; medium for generalization | No repeated-seed or independent reproduction. |
| E5 | S5 | Official repository | README release promise, public files, MIT license, and absence of visible executable code/weights in the inspected root. | Reproducibility and availability boundary. | Medium | Repository state can change after access date. |
| E6 | S6 | Related DEP | Multimodal tracking, sensor fusion, association metrics, governance, and failure-slice patterns. | Concept bridge to tracking evaluation. | Medium | Related work does not validate the selected paper. |
| E7 | S7 | Related DEP | Language-to-3D grounding, provenance, abstention, and bounded transfer. | Concept bridge to spatial language. | Medium | Related work does not validate the selected paper. |
| E8 | S8 | Related DEP | Calibrated RGB-D correspondence, projection integrity, modality adapters, and perturbation tests. | Concept bridge to geometry and data quality. | Medium | Related work does not validate the selected paper. |

## Executive Summary

DRMOT introduces a RGBD Referring Multi-Object Tracking task in which a model must use language plus synchronized RGB and depth to find and track objects matching semantic and spatial constraints. The authors construct DRSet with 187 scenes, 240 language descriptions, and 56 depth-related descriptions, then propose DRTrack: a Qwen2.5-VL-3B grounding stage followed by a depth-enhanced OC-SORT association stage. The source reports HOTA 33.24 for DRTrack versus 15.13 for a zero-shot RGB-language Qwen2.5-VL-3B baseline, with the same RGBD model at 32.68 before GRPO fine-tuning.

The full source supports the paper's mechanism, dataset, and table transcription with high confidence. It does not establish generalization beyond the tested DRSet setting, independent reproducibility, or production readiness. The official repository is a useful public locator but, at inspection, exposes a release promise rather than the promised dataset, executable framework, or weights. The practical value is therefore an auditable research pattern for depth-aware spatial grounding and association, not an autonomous tracking system.

## Detailed Summary

### Problem and background

Referring Multi-Object Tracking extends MOT by selecting objects through natural-language descriptions. The paper argues that RGB-only RMOT struggles with expressions such as “the person closest to the camera,” because 2D appearance does not directly encode the required depth ordering. Occlusion also weakens appearance features and can increase identity switches. DRMOT makes RGB, depth, and language jointly available so that geometric relations can participate in both grounding and temporal association.

### Dataset and annotation

DRSet is built from ARKitTrack RGB-D data and adds language descriptions plus multi-object bounding-box annotations. The source reports 187 scenes, 240 annotated video samples/descriptions, 56 depth-related descriptions, 18 object categories, and a roughly 60/40 video-level split of 141 training samples and 99 evaluation samples. The annotation process has four stages: attribute-table creation, target selection, frame-by-frame language and box annotation, and annotation verification. The authors describe a two-person cross-review of boxes, object IDs, and language.

The dataset spans indoor, outdoor, complex-weather, and nighttime settings. The source reports a human-heavy, non-uniform category distribution, descriptions averaging 31 characters, and sequences concentrated around 100–500 frames with some longer than 1,000 frames. These statistics make the benchmark useful for controlled study, but they also signal that rare categories, long-tail language, and sensor diversity need separate validation.

### DRTrack grounding mechanism

The first stage uses a multimodal large language model with language, RGB, and depth inputs. Depth maps are converted to a three-channel pseudo-RGB representation after metric preservation from millimeters to meters. The model outputs structured text from which bounding boxes are extracted. Geometric-aware GRPO combines a format reward with an IoU reward; the IoU term uses Hungarian matching between predicted and ground-truth boxes.

The implementation details report Qwen2.5-VL-3B-Instruct, GRPO on 10% of the DRSet training data, LoRA rank 64, scaling factor 128, dropout 0.05, learning rate `1e-5`, a frozen vision encoder, four generated responses per sample, one NVIDIA A6000 GPU, batch size 4, and two gradient-accumulation steps. These details support a bounded reconstruction plan but not an executable reproduction because the code and weights were not available in the inspected repository.

### Depth-enhanced association

The second stage starts from OC-SORT with a constant-velocity Kalman filter and the velocity-direction-consistency prior. For each detection and track prediction, the method extracts mean depth inside the bounding box and defines depth similarity as `S_D = exp(-DeltaD / sigma)`. It combines that score with 2D IoU as `S_RGBD = alpha * IoU + (1 - alpha) * S_D`, then forms an association cost using `C = -(S_RGBD + lambda * VDC)`. The reported settings are `alpha=0.9` and `lambda=0.3`.

This design makes the geometry bridge explicit: depth is used as an identity cue while IoU remains the dominant spatial cue. That choice is important for implementation because an erroneous depth map should not automatically override a well-localized track.

### Experiments and results

The paper reports HOTA, DetA, AssA, DetRe, DetPr, AssRe, AssPr, and LocA. In Table 3, the reported HOTA values are 0.98 for TransRMOT, 2.37 for TempRMOT, 15.13 for zero-shot Qwen2.5-VL-3B with RGB-language input, and 33.24 for fine-tuned DRTrack with RGB-depth-language input. DRTrack also reports DetA 32.35, AssA 34.97, DetRe 38.48, DetPr 58.13, AssRe 37.92, AssPr 74.23, and LocA 78.16.

The ablation compares the same Qwen model with RGB-language input at HOTA 15.13, RGB-depth-language input without RL fine-tuning at 32.68, and the final GRPO model at 33.24. The fusion-weight study reports HOTA 29.84 at `alpha=0`, 33.24 at `alpha=0.9`, and 32.88 at `alpha=1.0`. The source therefore supports a strong within-setting depth contribution and a smaller additional GRPO gain. It does not isolate all effects of prompts, model choice, data volume, compute, and association parameters.

### Limitations and conclusion

The paper presents DRMOT and DRSet as a new benchmark and DRTrack as a state-of-the-art baseline in the reported setting. The conclusion is source-supported for that setting. Reviewer-level limits are more consequential for reuse: the dataset is compact, depth-language coverage is a minority of descriptions, annotation and sensor governance evidence is limited, the implementation release was not yet visible, and no external or cross-sensor validation was inspected. The correct transfer claim is “promising depth-aware benchmark and baseline,” not “ready for autonomous or surveillance deployment.”

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | RGB-only RMOT is insufficient for some depth-dependent spatial descriptions and severe occlusion cases. | Author problem claim | E2 | Supported as the source's motivation; the magnitude of the problem depends on scene and language distribution. | Medium-high |
| C2 | DRSet provides an RGB-D-language benchmark with 187 scenes, 240 descriptions, and 56 depth-related descriptions. | Author dataset claim | E2 | Directly supported by dataset sections and tables. | High |
| C3 | DRTrack's two-stage design combines MLLM grounding with depth-aware OC-SORT association. | Author method claim | E3 | Equations, settings, and pipeline description support the reconstruction. | High |
| C4 | DRTrack reaches HOTA 33.24 versus 15.13 for the selected zero-shot RGB-language baseline. | Author empirical claim | E4 | Table 3 and ablation text support the reported comparison. | High for transcription; medium for causal attribution |
| C5 | Adding depth accounts for most of the reported improvement, while GRPO adds a smaller increment in the tested configuration. | Reviewer interpretation | E4 | The 15.13 → 32.68 → 33.24 ablation sequence supports this interpretation, but does not control every confound. | Medium |
| C6 | The public implementation is independently reproducible today. | Unsupported implication | E5 | Not established: the inspected README promises future release of data, code, and weights. | High rejection confidence |

## Methodology

- `Research objective`: Preserve the selected paper's source-grounded identity, mechanism, evidence, limitations, and safe implementation relevance in a public DEP-E artifact.
- `Sources inspected`: Official arXiv metadata and full-paper HTML, locally verified PDF and HTML, official DRMOT GitHub README and license, the live Black-Lake and Black-Lake-Data READMEs, and exactly three live related Black Lake DEP manuscripts.
- `Discovery strategy`: Enumerated the local archive with `rg --files -g "*.pdf"`; formed unique PDF-parent units; selected uniformly with a zero-based `Get-Random` index; then used arXiv and official-repository pages for source-first review.
- `Inclusion criteria`: One paper unit with a valid PDF and full-paper HTML, no prior Arxiv DEP artifact, no same-paper recent marker, and enough full-text evidence for methods, results, limitations, and implementation analysis.
- `Exclusion criteria`: Prior processed artifacts, duplicate stable keys, missing/invalid full-paper documents, abstract-only evidence, local-source redistribution, and unsupported claims of code/data availability.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: Evidence IDs map claims to primary source sections or public repository records; author claims, reviewer interpretations, and rejected implications are labeled separately.
- `Uncertainty handling`: No independent execution, dataset download, model download, or reproduction was performed; unavailable source-package and code status remain explicit.
- `Random selection and dedup`: `75,960` PDFs yielded `75,957` unique units. Sorted-unit index `25,503` was drawn uniformly; duplicate, other, and same-paper-within-24-hours exclusions were all `0`; no reselect was needed. The first draw began as a partial source unit and was completed by one bounded local archive repair before review.

## Scope, Constraints, and Assumptions

- `Scope`: Paper identity, DRSet design, DRTrack mechanism, reported experiments, limitations, three related DEP bridges, and bounded offline implementation ideas.
- `Temporal boundary`: Public paper revision v2 and repository state inspected through `2026-08-04`.
- `Evidence limits`: Results are author-reported; no code, weights, dataset, or independent benchmark run was available; figures were used through full-paper HTML captions/text rather than a separate visual reproduction study.
- `Assumptions`: The current arXiv record and its linked full-paper HTML identify the reviewed revision; displayed table values are transcribed as reported, not normalized into a new benchmark.
- `Constraints`: Source files remain local; redistribution rights for paper files/data are not assumed; examples are offline, bounded, and authorized-use only.
- `Out of scope`: Autonomous control, surveillance deployment, biometric identification, raw-scene redistribution, dataset licensing decisions, and claims of peer-reviewed acceptance or production readiness.
- `Intended use`: Research review, reproducibility planning, safe benchmark design, and DEP deposition.
- `Audience`: Computer-vision researchers, multimodal data engineers, benchmark maintainers, and safety reviewers.
- `Reproducibility boundary`: A reader can inspect the public paper, equations, tables, and official repository statement, but cannot reproduce the full method from the inspected public repository state alone.
- `Operational boundary`: The artifact discusses tracking and association conceptually and through toy validators only; it does not provide live-camera or consequential-decision automation.
- `Data sensitivity`: Public paper metadata plus potentially sensitive RGB-D scene content; source scenes are not deposited.

## Observations

- `Observed pattern`: Depth contributes twice: it changes the interpretation of spatial language during grounding and provides a geometric cue during identity association.
- `Observed pattern`: The reported depth ablation jump from 15.13 to 32.68 HOTA is larger than the GRPO increment from 32.68 to 33.24, suggesting that modality access may be the dominant within-setting factor.
- `Technical implication`: The alpha sweep keeps IoU primary at 0.9, so an implementation should treat depth as a calibrated supporting cue rather than an unconditional override.
- `Technical implication`: A minority of depth-related descriptions makes coverage auditing necessary; a strong aggregate score can still hide weak performance on the task subset that requires depth.
- `Contradiction or tension`: The paper emphasizes broad 3D-aware tracking, but the compact, human-heavy dataset and limited public implementation constrain claims of external validity.
- `Open question`: How do noisy, missing, or misregistered depth maps affect grounding and association separately?
- `Reviewer hypothesis`: The most reusable research object is an evidence-carrying RGBD tracking benchmark contract, not a single model checkpoint.

## Considerations

Depth maps can encode people, homes, workplaces, and spatial layouts. Any replication must use lawful, authorized data with access control, retention limits, and human review. Public artifacts should contain aggregate metrics and stable URLs, not raw scenes, frames, annotations, or identifiers.

Benchmark claims need slice coverage: depth-related versus appearance-only language, one versus many targets, rare categories, occlusion, lighting, sequence length, missing depth, and calibration perturbation. Report HOTA components and identity-switch behavior alongside aggregate HOTA. A system should abstain or fall back when depth is stale, invalid, or outside calibration bounds.

The MLLM stage introduces model-license, prompt-version, output-format, and compute dependencies. The tracker stage introduces sensor synchronization, depth-scale, occlusion, and association-threshold dependencies. Treating either as invisible preprocessing would weaken the evidence chain. The official release promise is not evidence that the future artifacts will have a permissive dataset license or production-suitable governance.

## Strengths

- The paper defines a concrete task where the role of depth is semantically testable rather than merely adding another sensor channel.
- DRSet connects RGB, depth, language, boxes, identities, and video-level splits in one benchmark contract.
- The annotation process and two-person review are described with enough structure to motivate an audit plan.
- DRTrack's grounding and association stages expose interpretable mechanisms and tunable geometric parameters.
- The depth and GRPO ablations provide a useful first decomposition of where the reported gain originates.
- The source includes tables, equations, prompts, and an annotation-format appendix rather than only an abstract-level claim.

## Weaknesses

- The dataset has only 240 descriptions and 56 depth-related descriptions, so rare spatial-language behavior may be underrepresented.
- Category distribution is reported as non-uniform and human-heavy; broad generalization is not established.
- No independent replication, repeated-seed intervals, calibration perturbation study, or cross-sensor evaluation was inspected.
- The public repository state does not yet provide the promised executable framework, dataset, or weights.
- The comparison conflates multiple choices—Qwen model, prompts, depth encoding, GRPO, LoRA, OC-SORT, and data selection—so causal attribution is incomplete.
- Privacy, consent, retention, demographic coverage, and dataset-access governance are not sufficiently documented for consequential use.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release code, prompts, weights, dataset manifest, and evaluator | Reproducibility | The current public repository is not executable | Independent verification | Release and maintenance burden | Clean-room setup from pinned commands and hashes |
| Add multi-seed and cross-sensor tests | Generalization | One setting cannot establish stability | Variance and transfer evidence | Additional data and compute | At least three seeds plus held-out sensor/scene splits |
| Corrupt depth and calibration systematically | Robustness | Depth is a key causal input | Failure thresholds and fallback policy | Experimental matrix size | Noise, holes, scale, pose, and timestamp sweeps |
| Expand depth-language coverage and rare categories | Dataset quality | 56 depth-related descriptions may not cover language diversity | Better long-tail evaluation | Annotation effort and quality control | Stratified coverage and inter-annotator agreement |
| Separate grounding from association metrics | Causal diagnosis | HOTA can hide stage-specific failures | Better debugging and model selection | More logging and evaluator work | Report box grounding, ID switches, DetA, AssA, and calibration jointly |
| Add governance documentation | Responsible use | RGB-D tracking can be sensitive | Safer access and deployment decisions | Policy and review cost | Dataset card, consent/rights audit, retention and access controls |

## Potential Implementations

### 1. Offline RGBD Tracking Evidence Gate

- `User`: Authorized computer-vision researchers.
- `Goal`: Compare RGB-only, RGBD, and RGBD-plus-GRPO variants without exporting raw scenes.
- `Core mechanism`: Ingest predictions, aggregate annotations, calibration summaries, depth-quality flags, and split manifests; compute HOTA components and identity-switch slices.
- `Required inputs`: Licensed/authorized data, evaluator version, calibration ID, modality manifest, and fixed prompts.
- `Outputs`: Public-safe evidence card, failure slices, metric table, and provenance receipt.
- `Risk controls`: Local-only raw data, no live camera, no control output, and human review of sensitive slices.
- `Evaluation`: Synthetic corruption tests, held-out scenes, missing-depth tests, and matched compute.

### 2. Spatial-Language Coverage Auditor

- `User`: Dataset maintainers and benchmark reviewers.
- `Goal`: Detect whether a benchmark actually tests depth-dependent language and long-tail spatial relations.
- `Core mechanism`: Classify descriptions by depth dependence, object count, category, occlusion, relation type, and sequence length; compare train/test coverage.
- `Required inputs`: Aggregate annotation metadata, language labels, split manifest, and annotation-agreement summaries.
- `Outputs`: Coverage matrix, gap list, and release-readiness report.
- `Risk controls`: Process labels and counts only; no raw frame or identity export.
- `Evaluation`: Injected-coverage regression tests, reviewer agreement, and held-out description families.

### 3. Correspondence and Association Stress Harness

- `User`: Multimodal tracking engineers.
- `Goal`: Identify when depth or calibration errors destabilize identity association.
- `Core mechanism`: Apply bounded synthetic depth noise, holes, scale drift, pose error, and timestamp offsets; sweep alpha/lambda and record stage-specific degradation.
- `Required inputs`: Authorized aggregate predictions, calibration model, depth statistics, and fixed evaluation seeds.
- `Outputs`: Degradation curves, safe operating envelope, fallback recommendation, and machine-readable validation summary.
- `Risk controls`: Synthetic-first evaluation, no autonomous action, and stop thresholds for invalid calibration.
- `Evaluation`: Recovery behavior, association precision/recall, identity-switch counts, and deterministic replay.

## Three Ways to Exercise This Research

1. `Synthetic depth-language grounding`: Objective - verify that a toy tracker resolves “closest” and “farthest” relations using known depth; Inputs - synthetic RGB boxes, depth planes, and bounded descriptions; Method - compare RGB-only and RGBD selection under controlled occlusion; Output - grounding accuracy and abstention table; Success criterion - depth-dependent cases improve without degrading appearance-only cases; Stop condition - stop when the test requires real person data or live sensors.
2. `Association perturbation sweep`: Objective - map the stability of the RGBD similarity; Inputs - synthetic detections, tracks, IoU values, and depth deltas; Method - sweep alpha, depth noise, missing values, and VDC disagreement; Output - identity-switch and association-cost curves; Success criterion - a predeclared safe envelope is visible; Stop condition - stop on unbounded parameter search or unclear metric definitions.
3. `Public-safe benchmark audit`: Objective - test whether a review package is reproducible from metadata without exposing source scenes; Inputs - split manifest, calibration IDs, evaluator version, aggregate predictions, and paper URLs; Method - validate coverage, required fields, and metric denominators; Output - evidence ledger and release-readiness report; Success criterion - every reported metric has a source and scope; Stop condition - stop if rights, provenance, or split identity are unresolved.

## Example MVP Product

- `Product name`: RGBD Grounding Evidence Card.
- `Target user`: Researchers and benchmark maintainers working with authorized RGB-D data.
- `Problem`: Aggregate tracking scores can hide depth-specific grounding failures, invalid calibration, and identity instability.
- `Core workflow`: Register source URLs and versioned manifests; validate modality and calibration fields; run local metric and perturbation checks; generate a public-safe Markdown evidence card.
- `Data requirements`: Synthetic data by default; optional authorized aggregate predictions, depth-quality summaries, calibration IDs, language-category labels, split hashes, and metric outputs. Raw frames remain local.
- `Architecture`: Local CLI, schema validator, coverage analyzer, perturbation runner, HOTA/association calculator, provenance ledger, and Markdown exporter.
- `Success metrics`: Required-field coverage, injected-error detection rate, deterministic rerun rate, per-slice metric completeness, and abstention correctness.
- `Risk controls`: Local-only processing, no raw-scene upload, no person identification, no live control interface, declared data rights, and human review for sensitive data.
- `Limitations`: An evidence card cannot establish model quality beyond its supplied data, cannot replace annotation audits, and cannot prove real-world safety.
- `MVP boundary`: One frozen evaluator, synthetic RGBD scenes, aggregate outputs, and report-only results.
- `Deployment model`: Local CLI or notebook.
- `Evaluation plan`: Unit tests for coverage and depth corruption, three deterministic smoke cases, and manual review of the worst failure slice.
- `Failure modes`: Stale calibration, missing depth, language-label leakage, scene overlap, metric denominator drift, and false confidence from aggregate scores.
- `Maintenance plan`: Pin evaluator versions, retain immutable manifests, review data rights on each update, and regenerate only from versioned inputs.

## Related Research and Reading

| Item | Type | Relevance | Public URL / Identifier |
|---|---|---|---|
| FEMOT Tracking DEP-E | Related Black Lake research | Multimodal tracking, association metrics, synchronization, and governance-aware evaluation. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-FEMOT%20Tracking/femot_tracking_manuscript.md |
| Language-to-Space DEP-E | Related Black Lake research | Language-driven 3D spatial grounding and bounded transfer. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260727-Language-to-Space/language_to_space_manuscript.md |
| Pixel-Point Transfer DEP-E | Related Black Lake research | Calibrated RGB-D correspondence and geometry integrity. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md |
| ReFGPT | Related RMOT research cited by the paper | Training-free, language-guided referring multi-object tracking context. | https://arxiv.org/abs/2504.09195 |
| ReaMOT | Related reasoning-based tracking cited by the paper | Reasoning-driven tracking benchmark and framework context. | https://arxiv.org/abs/2505.20381 |
| Official DRMOT repository | Implementation locator | Release status, license, and future code/data availability statement. | https://github.com/chen-si-jia/DRMOT |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2602.04692 | Identity, authors, dates, abstract, revision, DOI, and official links. | 2026-08-04 | Primary metadata. |
| R2 | https://arxiv.org/html/2602.04692 | Full-paper method, dataset, experiments, appendix, and references. | 2026-08-04 | Primary full-paper HTML; local copy withheld. |
| R3 | https://arxiv.org/pdf/2602.04692 | PDF integrity and cross-checking. | 2026-08-04 | Primary PDF; local copy withheld. |
| R4 | https://doi.org/10.48550/arXiv.2602.04692 | Stable arXiv-issued DOI. | 2026-08-04 | Identifier source. |
| R5 | https://github.com/chen-si-jia/DRMOT | Official README, release promise, visible files, and MIT license. | 2026-08-04 | Code/data/weights not visible in inspected root. |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-FEMOT%20Tracking/femot_tracking_manuscript.md | Multimodal tracking and association bridge. | 2026-08-04 | Related processed artifact. |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260727-Language-to-Space/language_to_space_manuscript.md | Language-to-space bridge. | 2026-08-04 | Related processed artifact. |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md | RGB-D correspondence and calibration bridge. | 2026-08-04 | Related processed artifact. |
| R9 | https://arxiv.org/abs/2504.09195 | ReFGPT related reading cited in the paper. | 2026-08-04 | Related reading only. |
| R10 | https://arxiv.org/abs/2505.20381 | ReaMOT related reading cited in the paper. | 2026-08-04 | Related reading only. |

## Appendix

### A. Selection, Deduplication, and Source-Gate Receipt

- Enumeration: `rg --files -g "*.pdf"`.
- Candidate PDFs: `75,960`.
- Unique parent units: `75,957`.
- Uniform draw: sorted-unit zero-based index `25,503` using `Get-Random`.
- Acceptance: first draw; duplicate exclusions `0`; other exclusions `0`; same-paper-within-24-hours markers `0`; reselections `0`.
- Initial source state: partial because full-paper HTML was absent.
- Repair: one bounded brokered single-paper acquisition; existing valid PDF preserved.
- Final PDF: `28,646,000` bytes; `%PDF-`; trailing `%%EOF`.
- Final full-paper HTML: `180,925` bytes; `50,391` body characters; document marker; `65` heading/section markers; `7` structure terms.
- Metadata/provenance/summary/verification records: updated locally.
- Source package: unavailable through redirect policy.
- Public output: no source files, cache, extracted text, local paths, or `.source/` directory.

### B. Metric Reconciliation

| Comparison | Reported HOTA | Interpretation |
|---|---:|---|
| RGB-language Qwen2.5-VL-3B | 15.13 | Zero-shot baseline in Table 3 and ablation. |
| RGB-depth-language Qwen2.5-VL-3B | 32.68 | Depth input without GRPO. |
| Final DRTrack | 33.24 | Depth input plus GRPO and depth-enhanced OC-SORT. |
| Depth-only association (`alpha=0`) | 29.84 | Sensitivity boundary; depth should not replace IoU. |
| IoU-only association (`alpha=1`) | 32.88 | Slightly below the reported `alpha=0.9` setting. |

This manuscript is a source-grounded review and public-safe research artifact. It does not claim independent execution, dataset redistribution, model availability, or production readiness.
