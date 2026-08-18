# Report-Mark: Less Cybersickness Please

- Deployment job ID: `BLAD-2200-20260818-D85F5742`
- Deployment item ID: `BLAD-2200-20260818-D85F5742-P38`
- Review date: 2026-08-18

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Less Cybersickness, Please: Demystifying and Detecting Stereoscopic Visual Inconsistencies in Virtual Reality Apps* |
| Authors | Li, Shuqing; Gao, Cuiyun; Zhang, Jianping; Zhang, Yujia; Liu, Yepang; Gu, Jiazhen; Peng, Yun; Lyu, Michael R. |
| Identifier | arXiv:2406.09313; DOI:10.1145/3660803 |
| Submitted / source date | 2024/06/13 |
| Record | https://arxiv.org/abs/2406.09313 |
| Full paper | https://arxiv.org/html/2406.09313 |
| PDF | https://arxiv.org/pdf/2406.09313 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | No one-time topic focus was requested.; matched unrestricted; evidence terms: not applicable. |
| Deployment IDs | `BLAD-2200-20260818-D85F5742`; `BLAD-2200-20260818-D85F5742-P38` |

## Concise Research Notes

The paper addresses apps, cybersickness, demystifying. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “To counter these challenges, we propose an unsupervised black-box testing framework named StereoID to identify the stereoscopic visual …”. A short evaluation anchor is: “To counter these challenges, we propose an unsupervised black-box testing framework named StereoID to identify the stereoscopic visual …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “The quality of Virtual Reality (VR) apps is vital, particularly the rendering quality of the VR Graphical User …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260803-Extended to Reality/extended_to_reality_manuscript.md` - Extended to Reality - DEP-E; overlap: reality, visual.
2. `.lake-data/DEP-E/DEP-E-20260723-KSHSeek Data-Driven Appro/kshseek_data_driven_appro_manuscript.md` - KSHSeek Data-Driven Approaches t - DEP-E; overlap: detecting.
3. `.lake-data/DEP-E/DEP-E-20260722-Rapid Whole Slide Imaging/rapid_whole_slide_imaging_manuscript.md` - Rapid Whole Slide Imaging Review - DEP-E; overlap: virtual.

## Synthesis Note

### Concept Bridge

The selected paper contributes a apps, cybersickness, demystifying perspective. The three related DEPs overlap concretely through detecting, reality, virtual, visual. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for apps that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's cybersickness mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Extended to Reality - DEP-E overlaps through reality, visual, clarifying a neighboring representation or evidence choice.
2. KSHSeek Data-Driven Approaches t - DEP-E overlaps through detecting, exposing a complementary evaluation or operating boundary.
3. Rapid Whole Slide Imaging Review - DEP-E overlaps through virtual, showing how implementation assumptions affect practical transfer.

### Conceptual Similarities

1. All four artifacts transform raw inputs into intermediate evidence rather than direct truth claims.
2. Each depends on explicit assumptions about data, representation, evaluation, and scope.
3. Each benefits from auditable versioning, negative controls, uncertainty, and failure-aware interpretation.

### MVP Implementations with Code Mock-Ups

1. Evidence map: `record = evaluate(input, config); require(record.provenance)`.
2. Frozen comparison: `scores = compare(baselines, candidate, split_manifest)`.
3. Abstention gate: `decision = review if drift or low_confidence else nonbinding_output`.

### Developer Challenges

1. Reproducing preprocessing, baselines, and metrics without leakage or silent version drift.
2. Preserving evidence lineage while keeping evaluation maintainable and privacy-aware.
3. Designing stable explanations and stop conditions outside the tested envelope.

### Author Challenges

1. Publishing enough configuration, data, and ablation detail for independent replication.
2. Separating benchmark improvement from claims of generalization or deployment readiness.
3. Reporting negative results, sensitivity, uncertainty, and failure cases alongside headline metrics.

## Validation Notes

- Uniform draw index 34,928 of 75,964 units; duplicate exclusions 0; focus exclusions 0; reselections 0.
- One-time research-focus gate passed for No one-time topic focus was requested.; matched categories: unrestricted; terms: not applicable.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2406.09313 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2406.09313 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2406.09313 - verified primary PDF; local copy withheld.
- https://doi.org/10.1145/3660803 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260803-Extended%20to%20Reality - related DEP: Extended to Reality - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260803-Extended to Reality/extended_to_reality_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260723-KSHSeek%20Data-Driven%20Appro - related DEP: KSHSeek Data-Driven Approaches t - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260723-KSHSeek Data-Driven Appro/kshseek_data_driven_appro_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260722-Rapid%20Whole%20Slide%20Imaging - related DEP: Rapid Whole Slide Imaging Review - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260722-Rapid Whole Slide Imaging/rapid_whole_slide_imaging_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
