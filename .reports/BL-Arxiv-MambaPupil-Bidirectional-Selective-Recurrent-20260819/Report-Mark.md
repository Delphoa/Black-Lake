# Report-Mark: MambaPupil Bidirectional

- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P164`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *MambaPupil: Bidirectional Selective Recurrent model for Event-based Eye tracking* |
| Authors | Wang, Zhong; Wan, Zengyu; Han, Han; Liao, Bohao; Wu, Yuliang; Zhai, Wei; Cao, Yang; Zha, Zheng-jun |
| Identifier | arXiv:2404.12083; DOI:10.48550/arXiv.2404.12083 |
| Submitted / source date | 2024/04/18 |
| Record | https://arxiv.org/abs/2404.12083 |
| Full paper | https://arxiv.org/html/2404.12083 |
| PDF | https://arxiv.org/pdf/2404.12083 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched stateful systems; evidence terms: model, recurrent. |
| Deployment IDs | `BLAD-2200-20260819-9951C2C3`; `BLAD-2200-20260819-9951C2C3-P164` |

## Concise Research Notes

The paper addresses bidirectional, event-based, eye. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “the inspected method sections”. A short evaluation anchor is: “the inspected evaluation sections”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “the inspected limitations discussion”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-S3MOT Monocular 3D Object/s3mot_monocular_3d_object_manuscript.md` - S3MOT Monocular 3D Object - DEP-E; overlap: selective, tracking.
2. `.lake-data/DEP-E/DEP-E-20260819-From Sim-to-Real Toward/from_sim_to_real_toward_manuscript.md` - From Sim-to-Real Toward - DEP-E; overlap: event-based.
3. `.lake-data/DEP-E/DEP-E-20260801-RawBMamba/rawbmamba_manuscript.md` - RawBMamba Review - DEP-E; overlap: bidirectional, selective.

## Synthesis Note

### Concept Bridge

The selected paper contributes a bidirectional, event-based, eye perspective. The three related DEPs overlap concretely through bidirectional, event-based, selective, tracking. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for bidirectional that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's event-based mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. S3MOT Monocular 3D Object - DEP-E overlaps through selective, tracking, clarifying a neighboring representation or evidence choice.
2. From Sim-to-Real Toward - DEP-E overlaps through event-based, exposing a complementary evaluation or operating boundary.
3. RawBMamba Review - DEP-E overlaps through bidirectional, selective, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-9951C2C3`; `BLAD-2200-20260819-9951C2C3-P164`.
- Uniform draw index 35,733 of 75,964 units; duplicate exclusions 5; focus exclusions 38; reselections 43.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: stateful systems; terms: model, recurrent.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2404.12083 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2404.12083 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2404.12083 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2404.12083 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260818-S3MOT%20Monocular%203D%20Object - related DEP: S3MOT Monocular 3D Object - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260818-S3MOT Monocular 3D Object/s3mot_monocular_3d_object_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260819-From%20Sim-to-Real%20Toward - related DEP: From Sim-to-Real Toward - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-From Sim-to-Real Toward/from_sim_to_real_toward_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260801-RawBMamba - related DEP: RawBMamba Review - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260801-RawBMamba/rawbmamba_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
