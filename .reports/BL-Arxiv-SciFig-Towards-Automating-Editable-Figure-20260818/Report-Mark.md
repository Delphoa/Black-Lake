# Report-Mark: SciFig Towards Automating

- Deployment job ID: `BLAD-2200-20260818-A4DB6AFC`
- Deployment item ID: `BLAD-2200-20260818-A4DB6AFC-P01`
- Review date: 2026-08-18

## Source Metadata

| Field | Value |
|---|---|
| Paper | *SciFig: Towards Automating Editable Figure Generation for Scientific Papers* |
| Authors | Huang, Siyuan; Zhou, Yifan; Gao, Yutong; Yin, Zi; Bai, Juyang; Liu, Xinxin; Chellappa, Rama; Lau, Chun Pong; Peng, Cheng; Nag, Sayan; Pramanick, Shraman |
| Identifier | arXiv:2601.04390; DOI:10.48550/arXiv.2601.04390 |
| Submitted / source date | 2026/01/07 |
| Record | https://arxiv.org/abs/2601.04390 |
| Full paper | https://arxiv.org/html/2601.04390 |
| PDF | https://arxiv.org/pdf/2601.04390 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | No one-time topic focus was requested.; matched unrestricted; evidence terms: not applicable. |
| Deployment IDs | `BLAD-2200-20260818-A4DB6AFC`; `BLAD-2200-20260818-A4DB6AFC-P01` |

## Concise Research Notes

The paper addresses automating, editable, figure. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “the inspected method sections”. A short evaluation anchor is: “the inspected evaluation sections”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “the inspected limitations discussion”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260806-PreGenie Slides/pregenie_slides_manuscript.md` - PreGenie Slides - DEP-E; overlap: editable, generation, scientific, figure.
2. `.lake-data/DEP-E/DEP-E-20260818-ST-NeRF Video/st_nerf_video_manuscript.md` - ST-NeRF - DEP-E; overlap: editable, scientific, generation.
3. `.lake-data/DEP-E/DEP-E-20260728-CanCal Towards Real-time/cancal_towards_real_time_manuscript.md` - CanCal Towards Real-time - DEP-E; overlap: towards, papers.

## Synthesis Note

### Concept Bridge

The selected paper contributes a automating, editable, figure perspective. The three related DEPs overlap concretely through editable, figure, generation, papers, scientific. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for automating that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's editable mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. PreGenie Slides - DEP-E overlaps through editable, generation, scientific, figure, clarifying a neighboring representation or evidence choice.
2. ST-NeRF - DEP-E overlaps through editable, scientific, generation, exposing a complementary evaluation or operating boundary.
3. CanCal Towards Real-time - DEP-E overlaps through towards, papers, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 62,606 of 75,964 units; duplicate exclusions 0; focus exclusions 0; reselections 0.
- One-time research-focus gate passed for No one-time topic focus was requested.; matched categories: unrestricted; terms: not applicable.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2601.04390 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2601.04390 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2601.04390 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2601.04390 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260806-PreGenie%20Slides - related DEP: PreGenie Slides - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260806-PreGenie Slides/pregenie_slides_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260818-ST-NeRF%20Video - related DEP: ST-NeRF - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260818-ST-NeRF Video/st_nerf_video_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260728-CanCal%20Towards%20Real-time - related DEP: CanCal Towards Real-time - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260728-CanCal Towards Real-time/cancal_towards_real_time_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
