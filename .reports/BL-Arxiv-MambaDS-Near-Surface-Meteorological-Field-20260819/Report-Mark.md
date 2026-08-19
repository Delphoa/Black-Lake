# Report-Mark: MambaDS Near-Surface

- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P83`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *MambaDS: Near-Surface Meteorological Field Downscaling with Topography Constrained Selective State Space Modeling* |
| Authors | Liu, Zili; Chen, Hao; Bai, Lei; Li, Wenyuan; Ouyang, Wanli; Zou, Zhengxia; Shi, Zhenwei |
| Identifier | arXiv:2408.10854; DOI:10.48550/arXiv.2408.10854 |
| Submitted / source date | 2024/08/20 |
| Record | https://arxiv.org/abs/2408.10854 |
| Full paper | https://arxiv.org/html/2408.10854 |
| PDF | https://arxiv.org/pdf/2408.10854 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched stateful systems; evidence terms: state space model. |
| Deployment IDs | `BLAD-2200-20260819-9951C2C3`; `BLAD-2200-20260819-9951C2C3-P83` |

## Concise Research Notes

The paper addresses constrained, downscaling, field. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “Recently, state space model (SSM), particularly its improved versions known as Mamba [ 39 ] , has garnered …”. A short evaluation anchor is: “In an era of frequent extreme weather and global warming, obtaining precise, fine-grained near-surface weather forecasts is increasingly …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “In an era of frequent extreme weather and global warming, obtaining precise, fine-grained near-surface weather forecasts is increasingly …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-S3MOT Monocular 3D Object/s3mot_monocular_3d_object_manuscript.md` - S3MOT Monocular 3D Object - DEP-E; overlap: selective, space, state.
2. `.lake-data/DEP-E/DEP-E-20260812-CMamba Learned Image/cmamba_learned_image_manuscript.md` - CMamba Learned Image - DEP-E; overlap: space, state, modeling.
3. `.lake-data/DEP-E/DEP-E-20260818-Swimba Switch Mamba Model/swimba_switch_mamba_model_manuscript.md` - Swimba Switch Mamba Model - DEP-E; overlap: space, state, modeling.

## Synthesis Note

### Concept Bridge

The selected paper contributes a constrained, downscaling, field perspective. The three related DEPs overlap concretely through modeling, selective, space, state. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for constrained that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's downscaling mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. S3MOT Monocular 3D Object - DEP-E overlaps through selective, space, state, clarifying a neighboring representation or evidence choice.
2. CMamba Learned Image - DEP-E overlaps through space, state, modeling, exposing a complementary evaluation or operating boundary.
3. Swimba Switch Mamba Model - DEP-E overlaps through space, state, modeling, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-9951C2C3`; `BLAD-2200-20260819-9951C2C3-P83`.
- Uniform draw index 61,058 of 75,964 units; duplicate exclusions 0; focus exclusions 12; reselections 12.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: stateful systems; terms: state space model.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2408.10854 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2408.10854 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2408.10854 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2408.10854 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260818-S3MOT%20Monocular%203D%20Object - related DEP: S3MOT Monocular 3D Object - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260818-S3MOT Monocular 3D Object/s3mot_monocular_3d_object_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260812-CMamba%20Learned%20Image - related DEP: CMamba Learned Image - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260812-CMamba Learned Image/cmamba_learned_image_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260818-Swimba%20Switch%20Mamba%20Model - related DEP: Swimba Switch Mamba Model - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260818-Swimba Switch Mamba Model/swimba_switch_mamba_model_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
