# Report-Mark: ClapperText

- Review date: 2026-08-06 (public-safe date; exact execution time withheld).
- Paper: *ClapperText: A Benchmark for Text Recognition in Low-Resource Archival Documents*.
- Identifier: arXiv:2510.15557v1; DOI: https://doi.org/10.48550/arXiv.2510.15557.
- Authors: Tingyu Lin, Marco Peer, Florian Kleber, and Robert Sablatnig.
- Source status: complete local PDF plus full-paper HTML after bounded repair; public artifacts contain URLs only and withhold source files.

## Source Metadata

| ID | Source | Role | Evidence / status |
|---|---|---|---|
| S1 | https://arxiv.org/abs/2510.15557 | Primary metadata | Title, authors, v1 date, abstract, 18-page note, DOI, and public links inspected. |
| S2 | https://arxiv.org/html/2510.15557 | Primary full text | Introduction, dataset construction, annotation process, splits, tables, ablations, detection, conclusion, and references inspected. |
| S3 | https://arxiv.org/pdf/2510.15557 | Primary PDF | Local PDF passed integrity checks; original file withheld. |
| S4 | https://github.com/linty5/ClapperText | Official implementation and release context | README, file inventory, repository license, dataset/code license statements, and Zenodo pointer inspected. |
| S5 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository authority | Live public-safe artifact and DEP rules inspected. |
| S6 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository authority | Live raw-data DEP rules inspected; no source files were deposited there. |

## Selection and Deduplication

`rg --files -g "*.pdf"` found 75,960 PDFs in the local source archive, representing 75,957 unique parent units. After withholding 185 identifier-incomplete units and excluding 587 units whose normalized arXiv IDs matched 1,534 IDs found in Black Lake artifacts or automation memory, 75,185 units remained. A PowerShell `Get-Random` zero-based index 67,887 was drawn uniformly from this frozen pool and selected arXiv:2510.15557. No duplicate reselect, same-paper marker within 24 hours, exact title/slug match, or remote ID/title match was found.

## Source-Integrity Result

The selected unit was initially partial because its valid 4,076,658-byte PDF had no full-paper HTML. One bounded official arXiv HTML request produced a valid 175,381-byte full-paper document; the approved ar5iv fallback was not needed. The HTML contains 42,377 visible body characters, 39 heading markers, six paper-structure terms, and an arXiv document marker. The PDF begins with `%PDF-` and contains trailing `%%EOF`. The metadata `/abs/` page was retained locally as metadata only. The local README, attribution/provenance record, machine summary, and verification report were updated. No `.source/` directory, source package, PDF, HTML, cache, extracted text, or local source record was staged or uploaded.

## Research Notes

ClapperText targets OCR for visually degraded archival video rather than clean scanned pages or modern scene text. The paper selects 127 clapperboard-containing segments from more than 300 HISTORIAN candidates, preserves 1440×1080 resolution at 24 FPS, and annotates 9,813 frames with 94,573 word instances. The instances include transcription, semantic category, handwritten/printed status, occlusion status, rotated boxes, four-point polygons, and axis-aligned boxes. The reported totals are 67.4% handwritten and 1,566 partially occluded instances.

The annotation workflow combines historian transcription with computer-vision labeling and three-stage review. Keyframes are sampled at least five per video, with interpolation and manual verification; the paper reports a maximum 12-frame gap and average 5.58-frame gap. Video-level disjointness is maintained: 18 training videos, 8 validation videos, and 101 test videos. This is important because frame-level random splitting would turn temporal redundancy into leakage.

The benchmark evaluates six recognition models and seven detection models in zero-shot and fine-tuned settings through MMOCR. Recognition uses case-and-symbol-normalized word recognition accuracy; detection uses polygon IoU 0.5 Hmean averaged per video. On non-occluded words, NRTR (Mod-Trans.) rises from 69.57% to 75.16% overall and from 63.35% to 70.68% on handwritten text. NRTR-R31 (1/16) rises from 65.56% to 77.24% overall. For occluded words, the paper reports NRTR moving from 18.06% to 30.14%. In detection, DBNet++ R50 + DCN moves from 59.48% to 68.42% Hmean, while TextSnake R50 + OCLIP reaches 69.63% fine-tuned Hmean at 36.4 FPS versus 9.5 FPS for DBNet++ R50 + DCN. These are author-reported results, not independent reproductions.

The ablations point to augmentation and geometry as practical levers. Recognition accuracy for NRTR-R31 (1/16) is 68.44% with all augmentations versus 66.18% with none; removing geometry transformations gives 66.84%. For detection, the paper reports an increase from 65.82% Hmean without augmentation to 72.45% with the strongest cropping/scaling choice. The conclusion remains bounded: fine-tuning helps, but degraded handwriting, occlusion, visual noise, domain shift, and limited supervision remain open problems.

## Evidence and Attribution

| Evidence | Attribution | Reviewer use |
|---|---|---|
| Dataset counts, split, annotation fields, model list, metrics, tables, and ablations | S2, cross-checked against S1 abstract | Source claims and quantitative transcription. |
| PDF/full-paper-HTML completeness | S3 plus local verification result | Source-integrity gate only; not a claim that experiments were reproduced. |
| Public code/data pointers and license statements | S4 | Availability and governance context; repository existence is not treated as reproduction proof. |
| Deposition rules | S5-S6 | Public-safe packaging and attribution requirements. |

## Related DEP Entries

1. [SSP Detection - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-SSP%20Oriented%20Detection/ssp_oriented_detection_manuscript.md) — concrete overlap in rotated/oriented box geometry, spatial partitioning, pseudo-label boundaries, and detector evaluation. Its source basis is the existing Black Lake manuscript; it contextualizes rather than validates ClapperText.
2. [VideoWeave - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md) — concrete overlap in video-level variation, spatial consistency, and evaluation beyond per-frame visual quality. Its source basis is the existing Black Lake manuscript.
3. [OMGEval Benchmark - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md) — concrete overlap in benchmark construction, culturally situated data, slice reporting, licensing, and evaluation governance. Its source basis is the existing Black Lake manuscript.

## Synthesis Note

### Concept Bridge

ClapperText turns a culturally specific, temporally redundant archive into a benchmark by aligning provenance-rich annotation, leakage-resistant video splits, geometry-aware labels, and task-specific evaluation. The bridge to the related DEP cluster is a reusable evidence pattern: SSP supplies spatial structure, VideoWeave supplies temporal/geometric consistency thinking, and OMGEval supplies benchmark governance and culturally situated measurement. The transferable idea is not a claim that these systems are interchangeable; it is that robust research artifacts should preserve what is being measured, how the unit of independence is defined, and what context is lost when outputs are reduced to a single score.

### Potential Implementations

1. **Licensed archival OCR regression runner.** A dataset lead imports a versioned, licensed manifest; the runner enforces video-level splits, runs recognition and polygon detection baselines, reports per-video and per-slice metrics, and refuses deployment claims when source or license metadata is incomplete.
2. **Temporal annotation quality assistant.** An archivist reviews low-confidence, occluded, or rapidly changing word instances through adjacent frames. The tool proposes evidence links across frames but requires human confirmation and stores every correction with annotation version, reviewer, and source rights.
3. **Heritage retrieval indexing pipeline.** A search engineer combines OCR text, semantic field labels, polygon coordinates, timestamps, and confidence into a provenance-aware index. It supports retrieval and audit views while keeping raw video access-controlled and exporting only licensed derivatives.

### Deeper Relationship Observations

1. ClapperText and SSP both make geometry a first-class supervision object: a polygon or rotated box is not merely a display overlay but a contract that shapes training targets, matching, and error analysis.
2. ClapperText’s strict video-level split and VideoWeave’s emphasis on temporal/spatial consistency point to the same evaluation risk: many nearby frames can create a misleadingly large sample count while preserving a small number of independent scenes.
3. ClapperText’s archival and cultural specificity and OMGEval’s localization workflow suggest that benchmark relevance is partly a governance property: semantic categories, source history, and annotation decisions must travel with the score.

### Conceptual Similarities

1. All four artifacts treat domain shift as a central object of study rather than an incidental failure mode.
2. All four use structured intermediate evidence—polygons, geometry latents, localized items, or versioned benchmark slices—to make model behavior inspectable.
3. All four benefit from separating source-supported results from reviewer interpretation and from independent reproduction claims.

### MVP Implementations with Code Mock-ups

1. **Leakage-safe video split checker.** A bounded manifest check prevents frame-level leakage by requiring a single split per video.

   ```python
   from collections import defaultdict

   def validate_video_splits(rows):
       seen = defaultdict(set)
       for row in rows:
           seen[row["video_id"]].add(row["split"])
       bad = {video: splits for video, splits in seen.items() if len(splits) != 1}
       if bad:
           raise ValueError(f"video leakage candidates: {sorted(bad)}")
       return {"videos": len(seen), "status": "pass"}
   ```

2. **Per-video OCR score aggregation.** This keeps long videos from dominating the benchmark and exposes slice-level coverage.

   ```python
   from collections import defaultdict

   def per_video_mean(records, score_key="correct"):
       buckets = defaultdict(list)
       for record in records:
           buckets[record["video_id"]].append(float(record[score_key]))
       means = {video: sum(values) / len(values) for video, values in buckets.items()}
       return {"per_video": means, "macro_mean": sum(means.values()) / len(means)}
   ```

3. **Occlusion-aware review queue.** This toy queue prioritizes auditable human review and never mutates source media.

   ```python
   def review_queue(predictions, threshold=0.55):
       return sorted(
           (p for p in predictions if p["confidence"] < threshold or p["occluded"]),
           key=lambda p: (not p["occluded"], p["confidence"]),
       )
   ```

### Developer Challenges

1. Preserve video-level independence, temporal provenance, polygon coordinate conventions, and model/version manifests across data loaders and evaluation code.
2. Reproduce the reported MMOCR baselines without silently changing pretrained weights, augmentation schedules, sampling policy, normalization, or per-video aggregation.
3. Build access control, license checks, confidence/abstention behavior, and source-preserving audit trails into the pipeline before adding throughput-oriented optimization.

### Author Challenges

1. Publish or pin the exact dataset release, annotation manifests, video membership, preprocessing, checkpoints, and environment needed to reconcile the paper with the public repository and Zenodo pointer.
2. Extend evidence with repeated seeds, confidence intervals, independent annotator agreement, held-out archives, and cross-domain tests that separate generalization from memorization of visual style.
3. Evaluate temporal modeling and persistent occlusion explicitly, including failure taxonomies for handwriting, non-lexical names, background text, and culturally specific metadata.

## Validation Notes

- Manuscript contract: generated separately with the `manuscript-research-document` skill and its `2026-07-07-expanded` artifact schema.
- Exact-count checks: three related DEP entries, three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP/code mock-ups, three developer challenges, and three author challenges.
- Source gate: complete PDF/full-paper HTML pair verified before review; metadata page not counted as full paper; no `.source/` directory created.
- Public-safety scan: no local absolute paths, usernames, drive letters, machine names, local timezone labels, exact run times, source bytes, caches, extracted text, or source archives appear in this report.
- Submission allowlist: only generated `.logs`, `.reports`, and `.lake-data` Markdown artifacts may be staged.

## Attribution Block

- Source URL: https://arxiv.org/abs/2510.15557
  - Applies to: Report-Mark.md and the generated DEP manuscript.
  - Notes: Public metadata, authors, date, DOI, abstract, and paper locator.
- Source URL: https://arxiv.org/html/2510.15557
  - Applies to: Report-Mark.md and the generated DEP manuscript.
  - Notes: Public full-paper method, dataset, evaluation, tables, ablations, and conclusion evidence.
- Source URL: https://arxiv.org/pdf/2510.15557
  - Applies to: Report-Mark.md and the generated DEP manuscript.
  - Notes: Public primary PDF; local copy was used for integrity verification and withheld from the public repository.
- Source URL: https://doi.org/10.48550/arXiv.2510.15557
  - Applies to: Paper identity and stable citation.
  - Notes: arXiv-issued DOI.
- Source URL: https://github.com/linty5/ClapperText
  - Applies to: Availability, repository, and license context.
  - Notes: Official repository README states dataset CC BY 4.0 and code MIT; no repository contents were executed.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-SSP%20Oriented%20Detection/ssp_oriented_detection_manuscript.md
  - Applies to: Related DEP synthesis.
  - Notes: Existing Black Lake processed artifact; not primary evidence for ClapperText.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md
  - Applies to: Related DEP synthesis.
  - Notes: Existing Black Lake processed artifact; not primary evidence for ClapperText.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md
  - Applies to: Related DEP synthesis.
  - Notes: Existing Black Lake processed artifact; not primary evidence for ClapperText.
- Source file: none.
  - Applies to: Public artifact set.
  - Notes: Original PDF, full-paper HTML, metadata HTML, source package, cache, extracted text, and local provenance files were withheld locally and were not uploaded.
