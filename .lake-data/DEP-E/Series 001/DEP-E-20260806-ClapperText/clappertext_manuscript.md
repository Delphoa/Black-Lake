---
title: "ClapperText - DEP-E"
generated_at: "2026-08-06 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of ClapperText, a benchmark for OCR in degraded archival video."
source_status: "local PDF and full-paper HTML plus public URLs; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-06"
temporal_cutoff: "arXiv:2510.15557v1 and public repository context inspected on 2026-08-06"
primary_url: "https://arxiv.org/abs/2510.15557"
stable_identifier: "arXiv:2510.15557v1; DOI 10.48550/arXiv.2510.15557"
confidence_summary: "High for source identity, dataset design, method description, and transcription of reported tables; medium for practical transfer; low for independent reproducibility because no experiment or dataset run was performed."
safety_scope: "Public scholarly review, licensed-data evaluation planning, and bounded local-only implementation examples."
distribution_notes: "Original PDF, HTML, metadata, source package, cache, extracted text, and local provenance remain private and are not redistributed."
---

# ClapperText - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Reference | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | ClapperText arXiv record | Primary metadata | HTML | arXiv:2510.15557v1 | https://arxiv.org/abs/2510.15557 | Public metadata; source file withheld. | 2026-08-06 | Inspected |
| S2 | ClapperText full paper | Primary artifact | Full-paper HTML | arXiv:2510.15557v1 | https://arxiv.org/html/2510.15557 | Full-paper evidence; local copy withheld. | 2026-08-06 | Inspected |
| S3 | ClapperText PDF | Primary artifact | PDF | arXiv:2510.15557v1; 18 pages noted by arXiv | https://arxiv.org/pdf/2510.15557 | Local PDF passed `%PDF-`/`%%EOF` gate; original withheld. | 2026-08-06 | Integrity checked |
| S4 | arXiv-issued DOI | Stable identity | DOI | 10.48550/arXiv.2510.15557 | https://doi.org/10.48550/arXiv.2510.15557 | Citation locator. | 2026-08-06 | Inspected |
| S5 | linty5/ClapperText | Official implementation and release context | GitHub | Public repository; 5 commits visible | https://github.com/linty5/ClapperText | README states dataset CC BY 4.0 and code MIT; contents not executed. | 2026-08-06 | Inspected |
| S6 | Private local source unit | Selection and integrity provenance | PDF, HTML, metadata, local records | arXiv:2510.15557v1 | Private local archive; path withheld | Kept local; no public source upload. | 2026-08-06 | Complete after repair |
| S7 | SSP Detection - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260711 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260711-SSP%20Oriented%20Detection/ssp_oriented_detection_manuscript.md | Processed context, not primary evidence for ClapperText. | 2026-08-06 | Inspected |
| S8 | VideoWeave - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260709 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md | Processed context, not primary evidence for ClapperText. | 2026-08-06 | Inspected |
| S9 | OMGEval Benchmark - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260717 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md | Processed context, not primary evidence for ClapperText. | 2026-08-06 | Inspected |
| S10 | Black Lake README | Repository authority | Markdown | main | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Live DEP and public-safety rules. | 2026-08-06 | Fetched and read |
| S11 | Black-Lake-Data README | Related repository authority | Markdown | main | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Live raw-data DEP rules; no source files deposited. | 2026-08-06 | Fetched and read |

Paper/work metadata:

- `Full title`: ClapperText: A Benchmark for Text Recognition in Low-Resource Archival Documents.
- `Authors`: Tingyu Lin, Marco Peer, Florian Kleber, and Robert Sablatnig.
- `Platform and date`: arXiv, submitted 2025-10-17; version 1.
- `Venue note`: The arXiv record states accepted at the ICDAR 2025 Workshop on Document Analysis of Low-resource Languages.
- `Subjects`: Computer Vision and Pattern Recognition, Artificial Intelligence, and Image and Video Processing.
- `Research object`: A benchmark dataset and baseline evaluation for printed and handwritten text recognition/detection in degraded archival video.
- `Public implementation context`: The official repository points to dataset and evaluation resources and states dataset CC BY 4.0 and code MIT. The repository README also points to a Zenodo v1.0.0 release; that release was not independently inspected here.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4 | Primary metadata and DOI | Title, authors, date, version, abstract, subject, venue note, DOI, and public locators. | Source identity and high-level problem framing. | High | Metadata does not establish detailed empirical validity. |
| E2 | S2, S3, S6 | Primary full text plus local integrity record | Dataset construction, annotation fields, split design, model lists, metrics, result tables, ablations, conclusion, and source completeness. | Method, dataset, evaluation, reported results, and source-first provenance. | High for transcription | Experiments were not reproduced; PDF content was cross-checked mainly through verified HTML. |
| E3 | S5 | Official repository | README overview, file inventory, public release pointer, and license statements. | Code/data availability context and governance constraints. | Medium-high | Repository contents were not cloned or executed; a pointer is not proof of end-to-end reproduction. |
| E4 | S7 | Existing DEP manuscript | Oriented polygons, spatial partitioning, pseudo-label construction, and detector evaluation. | Related spatial-geometry synthesis. | Medium | Existing synthesis is not primary evidence for ClapperText. |
| E5 | S8 | Existing DEP manuscript | Video-level spatial consistency and geometry-aware evaluation. | Related temporal/video synthesis. | Medium | Existing synthesis is not primary evidence for ClapperText. |
| E6 | S9 | Existing DEP manuscript | Benchmark construction, cultural localization, slice reporting, and evaluation governance. | Related benchmark-design synthesis. | Medium | Existing synthesis is not primary evidence for ClapperText. |
| E7 | S10, S11 | Repository standards | Public DEP naming, contents, attribution, source locality, and stable-deposition rules. | Artifact packaging and public-safety compliance. | High | Process evidence, not paper evidence. |

## Executive Summary

ClapperText introduces a benchmark for OCR in archival film footage, where clapperboards contain structured production metadata but are affected by motion blur, handwriting variation, exposure shifts, occlusion, camera movement, and clutter. The authors report 127 video segments, 9,813 annotated frames, and 94,573 word-level instances, with 67.4% handwritten instances and 1,566 partially occluded instances. Each instance carries transcription, semantic category, text type, occlusion status, and multiple spatial representations, including four-point polygons.

The source’s most important methodological safeguard is video-level separation: 18 training videos, 8 validation videos, and 101 test videos. The paper evaluates six recognition and seven detection models under zero-shot and fine-tuned conditions. Author-reported results show fine-tuning improving recognition and detection, including NRTR (Mod-Trans.) from 69.57% to 75.16% overall recognition accuracy and DBNet++ R50 + DCN from 59.48% to 68.42% detection Hmean at IoU 0.5. The evidence is strong for what the paper reports, but not for independent reproduction or deployment readiness.

Reviewer interpretation: ClapperText is valuable less as a single leaderboard than as a measurement contract connecting archival provenance, temporal leakage control, geometry-aware annotation, occlusion slices, and per-video evaluation. Public reuse must verify dataset release contents, upstream video rights, exact model/configuration versions, and cross-archive generalization before any operational claim.

## Detailed Summary

### Problem and Background

Historical film footage contains text that can support archiving, retrieval, and historical analysis. Clapperboards are semi-structured records of dates, locations, camera operators, and related production information, but their text differs from clean page scans and ordinary scene-text benchmarks. The paper positions existing handwritten, historical-document, natural-scene, subtitle, and traffic-sign datasets as insufficiently representative of the combined degradation and temporal variation in archival film.

### Dataset Construction

The authors select 127 clapperboard-containing segments from more than 300 candidates in the HISTORIAN collection. The videos retain 1440×1080 resolution and 24 FPS. Selection prioritizes visual and semantic diversity while avoiding near-duplicate layouts, styles, and backgrounds. The released benchmark contains 9,813 annotated frames and 94,573 word instances. The paper reports 67.4% handwritten instances and 1,566 partial occlusions.

Each instance includes a word transcription, one of five semantic categories (`Text`, `Date`, `Location`, `Recorded_By`, and `Attribute`), handwritten/printed status, and occlusion status. Spatial annotations include a rotated bounding box, a four-point polygon, and an axis-aligned bounding box. Cropped word images are derived from the rotated boxes for recognition experiments. Partially visible content uses placeholders; adjacent frames can support recovery, and unresolved characters are excluded when they cannot be confidently inferred.

### Annotation Process

Historians first produce shot-level transcriptions using metadata and visual inspection. A computer-vision team then annotates frames with CVAT. The paper describes an initial annotator, a second reviewer, and a third auditor, with disagreements resolved by consensus. At least five keyframes are labeled per video; interpolated frames are manually checked. The maximum reported gap is 12 frames and the average gap is 5.58 frames.

### Splits and Evaluation Protocol

The train/validation/test split is video-disjoint: 18 training videos, 8 validation videos, and 101 test videos. This prevents adjacent frames from the same segment appearing in both training and test sets. The benchmark evaluates six recognition models—CRNN, MASTER, NRTR, RobustScanner, SAR, and SVTR—and seven detection models—DBNet, DBNet++, FCENet, Mask R-CNN, PANet, PSENet, and TextSnake.

Experiments use MMOCR and official pretrained weights for zero-shot evaluation. Fine-tuning uses only the 18-video training split, validation on 8 videos, and testing on 101 videos. Training samples up to 20 frames per video per epoch, allows up to 36 epochs, and early-stops after 18 epochs without improvement. Recognition uses case-and-symbol-normalized word recognition accuracy. Detection matches polygons at IoU 0.5, reports Hmean per video, and averages across test videos.

### Recognition Results

The paper reports a strong domain gap between conventional scene-text benchmarks and ClapperText. NRTR-R31 (1/8) exceeds 94% on regular text benchmarks but records 67.46% zero-shot accuracy on ClapperText and 72.66% after fine-tuning. On non-occluded ClapperText words, NRTR (Mod-Trans.) rises from 69.57% to 75.16% overall, from 63.35% to 70.68% on handwritten text, and from 81.04% to 84.08% on printed text. The paper reports NRTR (Mod-Trans.) improving on partially occluded words from 18.06% to 30.14%; occluded instances are excluded from the conventional non-occluded comparison table.

The authors’ qualitative examples show that fine-tuning helps with unusual handwriting and some occlusion, while language-aware models may substitute semantically plausible words for unfamiliar names or abbreviations. This illustrates a tradeoff: language priors can help recognition but can also produce confident semantic normalization when visual evidence is weak.

### Detection Results and Ablations

On the detection task, DBNet++ R50 + DCN improves from 59.48% zero-shot to 68.42% fine-tuned Hmean, while TextSnake R50 + OCLIP reaches 69.63% fine-tuned Hmean. The paper reports 36.4 FPS for TextSnake R50 + OCLIP versus 9.5 FPS for DBNet++ R50 + DCN at batch size 1, making throughput part of the deployment discussion rather than an afterthought. Qualitative cases show TextSnake over-grouping or missing small fields and DBNet++ false positives on background text.

The recognition augmentation ablation reports 68.44% validation accuracy with geometric transforms, rescaling, and color jitter versus 66.18% with none; removing geometry gives 66.84%. The detection ablation reports Hmean increasing from 65.82% without augmentation to 72.45% with the strongest cropping/scaling configuration. These results are useful hypotheses for follow-on evaluation, but they remain bounded by one dataset and one training protocol.

### Conclusion and Novelty Boundary

The paper’s primary novelty is the benchmark’s combination of culturally significant archival video, word-level OCR labels, temporal variation, semantic categories, occlusion states, and rotated spatial annotations. The model architectures are representative baselines rather than a single new OCR architecture. The durable research contribution is therefore the dataset/evaluation design and its explicit low-resource boundary, not a claim that any listed model is universally best.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | ClapperText contains 127 video segments, 9,813 annotated frames, and 94,573 word-level instances, with high handwritten content and partial occlusion. | Author claim | E2 | Directly supported by the paper’s abstract, dataset section, and table. | High |
| C2 | The benchmark uses polygon/box, semantic, handwriting, and occlusion annotations suitable for recognition and detection. | Author claim supported by method | E2 | Directly supported by annotation-process and dataset descriptions. | High |
| C3 | Video-level disjoint splits are necessary for credible evaluation because frames are temporally related. | Reviewer interpretation grounded in protocol | E2 | The split is source-supported; the leakage rationale is reviewer analysis of the sampling design. | High |
| C4 | Fine-tuning improves recognition, including handwritten and occluded cases, under the reported setup. | Author empirical claim | E2 | Table values and prose support the direction and examples; no independent rerun was performed. | High for transcription; medium for generalization |
| C5 | Fine-tuning improves detection Hmean, and throughput differs materially among strong models. | Author empirical claim | E2 | Reported tables support the metrics and FPS values; deployment validity remains untested. | High for transcription; medium for transfer |
| C6 | The benchmark exposes domain shift from conventional scene-text datasets. | Author claim and reviewer interpretation | E2 | The reported regular-benchmark versus ClapperText comparison supports the claim within the tested models. | Medium-high |
| C7 | Public code and data resources are available for follow-on work. | Repository-supported availability claim | E3 | The official README provides code/release pointers and licenses, but a public pointer does not prove a complete reproducible environment. | Medium |

## Methodology

- `Research objective`: Preserve the selected paper’s source identity, mechanism, benchmark design, reported evidence, limitations, implementation relevance, and provenance in a public-safe DEP manuscript.
- `Sources inspected`: Local selected-paper metadata and verified PDF/full-paper HTML; public arXiv metadata, full-paper HTML, PDF and DOI locators; official ClapperText GitHub README/license context; live Black Lake and Black-Lake-Data READMEs; and exactly three related Black Lake DEP manuscripts.
- `Discovery strategy`: Enumerated the local archive with `rg --files -g "*.pdf"`; treated each PDF parent directory as one paper unit; derived normalized arXiv IDs; scanned repository artifacts and automation memory for ID markers; searched exact ID/title/slug markers in both repositories; drew a uniform index with PowerShell `Get-Random`; repaired and verified the selected unit before review.
- `Inclusion criteria`: Include the complete selected paper after the source gate, primary method/dataset/evaluation evidence, official implementation context, repository governance, and related DEP entries with concrete overlap in geometry, video consistency, or benchmark governance.
- `Exclusion criteria`: Withhold identifier-incomplete units, prior-owned papers, source files from public outputs, unreproduced claims as verified facts, and unrelated entries found only through broad keyword search. Do not treat the `/abs/` page as full paper evidence.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety and ethics, product research, and replication analysis.
- `Evidence handling`: Assign evidence IDs, map claims to source IDs, label author claims versus reviewer interpretation, preserve exact reported metrics with evaluation context, and mark repository availability as context rather than reproduction proof.
- `Uncertainty handling`: Preserve missing source-package collection, unexecuted code/data, unavailable independent metrics, licensing boundaries, temporal-correlation risk, and cross-archive generalization gaps.
- `Extraction process`: Read the verified full-paper HTML and its tables/captions through public and local copies; inspect the local PDF for integrity and source identity. PDF visual/text extraction tooling was unavailable for substantive extraction in this run, so the HTML is the main full-text evidence surface.
- `Version control`: Review is pinned to arXiv:2510.15557v1 and the public repository context visible on 2026-08-06. No source package or mutable code checkout was used as a reproduction environment.
- `Claim selection`: Prioritize problem, dataset scale, annotation semantics, split design, benchmark metrics, ablations, limitations, licenses, and transfer implications.
- `Cross-checking`: Cross-check paper abstract, HTML tables, conclusion, local source-integrity record, and official repository README; do not harmonize reported values with unverified external runs.
- `Safety handling`: Keep archival media and derived source documents local; discuss licensed/synthetic/public examples only; do not infer personal identity, historical truth, or operational reliability from OCR outputs.
- `Reviewer stance`: DEP-ready preservation, source-grounded paper report, implementation brief, product translation, safety review, and bounded replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: Paper identity, dataset construction, annotation mechanism, split/evaluation design, reported recognition/detection results, ablations, limitations, related DEP synthesis, and bounded implementations.
- `Temporal boundary`: Public sources and repository context inspected on 2026-08-06; paper version is arXiv v1 submitted 2025-10-17.
- `Evidence limits`: No dataset/video files, model weights, source package, or executable code were collected into the public DEP; no experiment was reproduced; the official Zenodo pointer was not independently inspected; PDF content was not substantively extracted outside the full-paper HTML.
- `Assumptions`: The arXiv v1 HTML corresponds to the selected local PDF; table values in the HTML accurately transcribe the paper; repository license statements are current as observed and require rechecking before redistribution.
- `Constraints`: Source-document locality, public-safe Markdown allowlisting, license review, no private paths or exact local timestamps, and no high-consequence use of uncalibrated OCR outputs.
- `Out of scope`: Production OCR deployment, archival cataloging decisions, identity inference, recovery of historical facts from noisy text, training or benchmarking on restricted media, and claims of peer-review or deployment readiness beyond public metadata.
- `Intended use`: Research review, DEP preservation, evaluation planning, reproducibility backlog, and safe MVP ideation.
- `Audience`: OCR researchers, dataset/annotation leads, archive engineers, evaluation maintainers, and reviewers of public-safe research artifacts.
- `Depth target`: Source-grounded manuscript report with empirical transcription, comparative synthesis, implementation planning, and replication boundaries.
- `Reproducibility boundary`: The paper describes a plausible recipe, but valid reproduction requires the exact dataset release, source rights, preprocessing, MMOCR version, pretrained weights, configuration, hardware, seed policy, and expected-output checks.
- `Operational boundary`: Examples are local-only, synthetic, or licensed-data evaluation patterns; they do not authorize access to archival repositories or personal data.
- `Data sensitivity`: Public scholarly metadata plus historically sourced visual material whose redistribution, cultural handling, and upstream rights require separate review.

## Observations

- `Observed pattern`: The benchmark is low-resource in independent videos, not in raw annotation count. Thousands of frames and words are nested inside 127 segments, so video-level independence is more informative than row count.
- `Observed pattern`: Fine-tuning helps handwritten recognition more strongly than printed recognition in the reported slices, suggesting that the dominant transfer barrier is visual style and degradation rather than only language modeling.
- `Technical implication`: Rotated boxes, four-point polygons, semantic categories, and occlusion labels enable error analysis that distinguishes localization, transcription, and semantic-field failures.
- `Technical implication`: Per-video macro-averaging prevents long segments from dominating, but it changes how a deployment estimate should be interpreted; frame-weighted and video-weighted scores should be reported separately.
- `Contradiction or tension`: The official repository advertises dataset and evaluation resources while also labeling parts of its contents as forthcoming. Availability, completeness, and reproducibility should remain separate fields.
- `Open question`: How much improvement comes from temporal context and adjacent-frame recovery versus static fine-tuning on more varied frames?
- `Reviewer hypothesis`: Confidence-aware abstention plus semantic-field constraints could reduce plausible-but-wrong substitutions for names, abbreviations, and partially occluded characters.

## Considerations

Archival-source governance is central. The paper and official repository state dataset/code licensing, but upstream HISTORIAN footage and any derived frames require a separate rights, provenance, and cultural-heritage review. A system should keep raw media access-controlled, record source and annotation versions, and publish only permitted derivatives.

Evaluation should preserve video-level disjointness, per-video aggregation, and explicit slices for handwritten, printed, semantic category, and occlusion status. A single aggregate WRA or Hmean can conceal failures in names, dates, locations, and partially visible text. Repeated seeds, confidence intervals, annotation agreement, and cross-archive tests are needed before interpreting a gain as robust.

Operational deployments should show confidence, abstain on unsupported recovery, retain the original image region, and allow human correction. Background text, false positives, semantic substitution, and temporal duplication are predictable failure modes. Throughput claims should include hardware, batch size, model version, preprocessing, and quality thresholds rather than relying on the FPS table alone.

## Strengths

- The dataset targets a real gap between clean scene-text benchmarks and degraded archival video.
- Video-level split design directly addresses temporal leakage risk.
- Annotation fields combine spatial geometry, semantics, handwriting, and occlusion, enabling multi-task and slice-level analysis.
- The paper reports both recognition and detection, including ablations and throughput context.
- The official repository provides a public code/data pointer and visible license statements, which creates a concrete follow-on path even though reproduction was not performed.

## Weaknesses

- The evidence is one curated historical collection; transfer to other archives, languages, scripts, cameras, and preservation conditions is not established.
- Eighteen training videos are a narrow supervision base, even though frame and word counts are large.
- The paper does not provide the independent repeated-seed, confidence-interval, and annotator-agreement evidence needed for strong uncertainty claims.
- Temporal redundancy can make apparent sample size exceed effective sample size, and the review did not independently audit every split or frame interval.
- Language-aware models can produce plausible substitutions for unfamiliar names or abbreviations; semantic correctness is not guaranteed by WRA.
- Repository visibility and license statements do not by themselves establish a fully reproducible release, data-rights chain, or deployment safety.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish immutable split and annotation manifests | Reproducibility | Prevents silent video/frame membership drift. | Exact split recreation and auditability. | Maintenance and release overhead. | Hash manifests and compare against paper totals. |
| Add repeated seeds and uncertainty intervals | Evaluation | Single reported values hide variance. | More reliable model comparisons. | Compute and statistical design. | Bootstrap by video and report seed distributions. |
| Add cross-archive and temporal holdouts | Generalization | One source collection may encode style-specific shortcuts. | Shift evidence and failure taxonomy. | Requires licensed external archives. | Hold out archive, camera era, and video segment families. |
| Report human agreement and correction burden | Annotation | Consensus workflow is described but not quantified. | Better label-confidence calibration. | Reviewer time and privacy governance. | Double-annotate slices and publish agreement/error categories. |
| Evaluate temporal OCR with abstention | Method and safety | Adjacent frames may recover occlusion but also amplify leakage or hallucination. | Safer recovery and clearer temporal value. | More complex models and audit logs. | Compare static, adjacent-frame, and abstaining systems on held-out videos. |

## Potential Implementations

### 1. Licensed Archival OCR Regression Runner

- `User`: Dataset or evaluation lead.
- `Goal`: Compare recognition/detection baselines on a versioned, licensed archive slice.
- `Core mechanism`: Enforce one split per video, run static baselines, compute per-video and slice metrics, and retain prediction-to-region evidence links.
- `Required inputs`: Licensed dataset manifest, video IDs, annotations, model/config versions, and metric definitions.
- `Outputs`: Versioned scorecard, per-video errors, occlusion/handwriting slices, and reproducibility report.
- `Risk controls`: License checks, local-only media access, no identity inference, confidence/abstention, and human review for catalog updates.
- `Evaluation`: Split validation, leakage scan, repeated seeds, bootstrap intervals, and cross-archive holdout.

### 2. Temporal Annotation Quality Assistant

- `User`: Archivist or annotation reviewer.
- `Goal`: Prioritize uncertain and occluded instances for human correction without silently filling missing text.
- `Core mechanism`: Link adjacent licensed frames, surface candidate evidence, and store reviewer-confirmed changes as versioned annotations.
- `Required inputs`: Frame sequence, polygon labels, confidence scores, occlusion flags, and reviewer identity/role.
- `Outputs`: Review queue, correction record, unresolved-character record, and audit summary.
- `Risk controls`: No automatic publication, no raw media export, access-controlled review, explicit abstention, and reversible annotation versions.
- `Evaluation`: Measure correction precision, reviewer time, false recovery rate, and performance on held-out occlusion cases.

### 3. Heritage Retrieval Index with Provenance

- `User`: Archive search engineer.
- `Goal`: Make permitted clapperboard metadata searchable while preserving source and annotation context.
- `Core mechanism`: Index OCR text, semantic field, polygon, time/frame reference, confidence, and provenance as separate fields.
- `Required inputs`: Licensed derivatives, annotation manifest, OCR outputs, rights metadata, and retention policy.
- `Outputs`: Search results with evidence snippets, confidence, source reference, and human-correction status.
- `Risk controls`: Rights-aware access, metadata minimization, redaction of restricted fields, source-link retention, and no autonomous historical conclusions.
- `Evaluation`: Retrieval precision/recall, field-specific error rates, rights-policy tests, and user correction outcomes.

## Three Ways to Exercise This Research

1. **Synthetic split audit**: Objective—test leakage controls. Inputs—a small synthetic set of frame records with repeated `video_id` values. Method—run a checker that rejects any video appearing in more than one split and report video-level counts. Output—a pass/fail manifest. Success criterion—every video belongs to exactly one split. Stop condition—stop if any record lacks a stable video ID or split.
2. **Licensed toy OCR comparison**: Objective—measure the difference between static and adjacent-frame evidence. Inputs—an authorized, non-sensitive toy image sequence with synthetic occlusions and labels. Method—compare a static recognizer, an adjacent-frame heuristic, and an abstaining variant under fixed video-level holdouts. Output—per-video WRA, occlusion recovery, abstention rate, and error examples. Success criterion—improvement is reported with uncertainty and no split leakage. Stop condition—stop if rights, labels, or reproducibility metadata are incomplete.
3. **Provenance-aware review queue**: Objective—exercise human-in-the-loop correction. Inputs—synthetic predictions with confidence, occlusion flags, polygon coordinates, and source-version identifiers. Method—prioritize low-confidence/occluded items, require reviewer confirmation, and export only derived aggregate statistics. Output—a reversible correction log and quality summary. Success criterion—every correction links to a reviewer and source version. Stop condition—stop before export if a raw source frame or private identifier would leave the local boundary.

## Example MVP Product

- `Product name`: ArchiveText Audit Board.
- `Target user`: Small archive digitization and OCR evaluation teams.
- `Problem`: OCR quality varies across handwritten, printed, blurred, and partially occluded archival frames, while benchmark leakage and provenance gaps make scores hard to trust.
- `Core workflow`: Import a licensed manifest; validate video-disjoint splits; run approved recognition/detection baselines; queue low-confidence and occluded cases; show per-video and slice metrics; export a public-safe audit report.
- `Data requirements`: Licensed frame/video derivatives, polygon and transcription annotations, semantic categories, occlusion/handwriting flags, model/config manifests, and rights metadata.
- `Architecture`: Local-only manifest validator, batch inference adapters, polygon/word metric service, confidence/abstention layer, review queue, immutable audit log, and Markdown/JSON report exporter.
- `Success metrics`: Split-validation pass rate, per-video metric reproducibility, occlusion recovery precision, reviewer correction time, abstention calibration, and retrieval/error-analysis usefulness.
- `Risk controls`: Local media storage, rights gate, no identity inference, restricted raw-frame views, reversible corrections, human approval, confidence display, and no automatic catalog publication.
- `Limitations`: MVP does not claim historical truth, broad archive generalization, production throughput, or complete recovery of unreadable text.
- `MVP boundary`: Synthetic or explicitly licensed data only; one recognition adapter, one polygon detector adapter, and no cloud inference by default.
- `Deployment model`: Local CLI plus browser-local review dashboard.
- `Evaluation plan`: Unit tests for split leakage and polygon coordinate conventions; synthetic occlusion tests; fixed public toy benchmark; human review of a licensed pilot; and reproducibility review of manifests/configs.
- `Failure modes`: Temporal duplication, background-text false positives, semantically plausible substitutions, malformed polygons, confidence miscalibration, license metadata drift, and reviewer over-trust.
- `Maintenance plan`: Version source/annotation/model manifests, rerun split and license checks on every update, archive metric definitions, and require human approval for public report generation.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| ClapperText | Primary paper | Benchmark, annotation, split, metrics, and reported results. | https://arxiv.org/abs/2510.15557 |
| ClapperText official repository | Implementation/release | Code, dataset pointer, license context, and release notes. | https://github.com/linty5/ClapperText |
| SSP Detection - DEP-E | Related Black Lake artifact | Rotated/oriented geometry, spatial partitioning, and detection evaluation. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260711-SSP%20Oriented%20Detection/ssp_oriented_detection_manuscript.md |
| VideoWeave - DEP-E | Related Black Lake artifact | Video-level variation and geometry-consistency evaluation. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md |
| OMGEval Benchmark - DEP-E | Related Black Lake artifact | Culturally situated benchmark construction, slices, and evaluation governance. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md |
| Zenodo release pointer | Dataset locator | The official repository points to a v1.0.0 dataset release; independently inspect before use. | https://doi.org/10.5281/zenodo.17366963 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2510.15557 | E1, paper identity, authors, date, abstract, DOI, and venue note. | 2026-08-06 | Public metadata; `/abs/` is metadata only. |
| R2 | https://arxiv.org/html/2510.15557 | E2, full-paper method, dataset, annotations, splits, tables, ablations, and conclusion. | 2026-08-06 | Public full-paper HTML; local copy withheld. |
| R3 | https://arxiv.org/pdf/2510.15557 | E2, primary PDF integrity and source identity. | 2026-08-06 | Original PDF withheld from public DEP. |
| R4 | https://doi.org/10.48550/arXiv.2510.15557 | E1, stable identifier. | 2026-08-06 | arXiv-issued DOI. |
| R5 | https://github.com/linty5/ClapperText | E3, official implementation/release and license context. | 2026-08-06 | Repository contents not executed. |
| R6 | Private local archive unit for arXiv:2510.15557v1 | E2, E6, selection and complete-source verification. | 2026-08-06 | Path, files, hashes, and exact local execution context withheld from public artifact. |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260711-SSP%20Oriented%20Detection/ssp_oriented_detection_manuscript.md | E4, related spatial-geometry synthesis. | 2026-08-06 | Existing processed DEP; not primary evidence for ClapperText. |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md | E5, related video/geometry synthesis. | 2026-08-06 | Existing processed DEP; not primary evidence for ClapperText. |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md | E6, related benchmark/governance synthesis. | 2026-08-06 | Existing processed DEP; not primary evidence for ClapperText. |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | E7, public artifact and DEP rules. | 2026-08-06 | Live README fetched and read. |
| R11 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | E7, related raw-data DEP and source-file rules. | 2026-08-06 | Live README fetched and read; no raw source deposited. |

## Appendix

### Selection and Deduplication Validation

| Check | Result |
|---|---|
| PDF enumeration | 75,960 PDFs via `rg --files -g "*.pdf"`. |
| Parent-unit grouping | 75,957 unique PDF parent directories. |
| Normalized modern IDs | 75,772 units; 185 identifier-incomplete units withheld. |
| Prior-ID scan | 1,534 normalized IDs found in Black Lake artifacts and automation memory; 587 matching units excluded. |
| Frozen eligible pool | 75,185 units. |
| Uniform draw | PowerShell `Get-Random`, zero-based index 67,887. |
| Reselection and recent marker checks | 0 duplicate reselections; 0 same-paper markers within 24 hours. |
| Exact selected-paper search | No `2510.15557` or `ClapperText` match in Black Lake, Black-Lake-Data search, or automation memory. |

### Complete-Source Verification

- The selected unit was classified partial because the PDF existed but full-paper HTML was missing.
- A bounded official arXiv HTML repair completed before substantive review; ar5iv fallback was not needed.
- PDF gate passed: at least 10 KB, `%PDF-` header, trailing `%%EOF`.
- Full-paper HTML gate passed: at least 5 KB, at least 2,000 visible body characters after script/style removal, article/main/LaTeXML document marker, at least two section/heading markers, and at least two structure terms.
- Metadata `/abs/` page was retained as metadata only and never counted as full paper.
- Local README, attribution/provenance, machine summary, and verification report were updated.
- No PDF, HTML, metadata, source archive, cache, extracted source text, or `.source/` directory appears in the public artifact set.

### Replication Checklist

- Pin the dataset/release and verify rights for source video and derived images.
- Verify video-disjoint train/validation/test membership and hash the manifests.
- Pin MMOCR, pretrained weights, model configs, preprocessing, sampling, early-stopping, normalization, and seed policy.
- Reproduce per-video WRA/Hmean before comparing frame-weighted alternatives.
- Report handwritten, printed, semantic-category, and occlusion slices with uncertainty intervals.
- Add a cross-archive holdout and a temporal-context ablation without adjacent-frame leakage.
- Record model outputs, false positives, semantically plausible substitutions, and reviewer correction burden.

## Attribution Block

- Source URL: https://arxiv.org/abs/2510.15557
  - Applies to: this manuscript.
  - Notes: Public metadata, authors, date, abstract, venue note, and citation locator.
- Source URL: https://arxiv.org/html/2510.15557
  - Applies to: this manuscript.
  - Notes: Public full-paper evidence for method, dataset, evaluation, results, and limitations.
- Source URL: https://arxiv.org/pdf/2510.15557
  - Applies to: this manuscript.
  - Notes: Public primary PDF; local copy was integrity-checked and withheld.
- Source URL: https://doi.org/10.48550/arXiv.2510.15557
  - Applies to: stable paper identity.
  - Notes: arXiv-issued DOI.
- Source URL: https://github.com/linty5/ClapperText
  - Applies to: official code/data/license context.
  - Notes: Dataset and code rights require separate review before reuse; no repository contents were executed.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260711-SSP%20Oriented%20Detection/ssp_oriented_detection_manuscript.md
  - Applies to: related research synthesis.
  - Notes: Existing processed DEP; not primary evidence for ClapperText.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md
  - Applies to: related research synthesis.
  - Notes: Existing processed DEP; not primary evidence for ClapperText.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md
  - Applies to: related research synthesis.
  - Notes: Existing processed DEP; not primary evidence for ClapperText.
- Source file: none.
  - Applies to: public DEP artifact.
  - Notes: Original PDF, full-paper HTML, metadata HTML, source package, cache, extracted text, and local provenance records remain local and were not uploaded.
