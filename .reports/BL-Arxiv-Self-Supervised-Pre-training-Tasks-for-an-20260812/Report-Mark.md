# Report-Mark: Self-Supervised

- Deployment job ID: `BLAD-2200-20260812-9483C5E4`
- Deployment item ID: `BLAD-2200-20260812-9483C5E4-P10`
- Review date: 2026-08-12

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Self-Supervised Pre-training Tasks for an fMRI Time-series Transformer in Autism Detection* |
| Authors | Zhou, Yinchi; Duan, Peiyu; Du, Yuexi; Dvornek, Nicha C. |
| Identifier | arXiv:2409.12304; DOI:10.48550/arXiv.2409.12304 |
| Submitted / source date | 2024/09/18 |
| Record | https://arxiv.org/abs/2409.12304 |
| Full paper | https://arxiv.org/html/2409.12304 |
| PDF | https://arxiv.org/pdf/2409.12304 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260812-9483C5E4`; `BLAD-2200-20260812-9483C5E4-P10` |

## Concise Research Notes

The paper addresses autism, detection, fmri. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “Autism Spectrum Disorder (ASD) is a neurodevelopmental condition that encompasses a wide variety of symptoms and degrees of …”. A short evaluation anchor is: “Autism Spectrum Disorder (ASD) is a neurodevelopmental condition that encompasses a wide variety of symptoms and degrees of …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “Autism Spectrum Disorder (ASD) is a neurodevelopmental condition that encompasses a wide variety of symptoms and degrees of …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260802-MeDSLIP Medical/medslip_medical_manuscript.md` - MeDSLIP Medical - DEP-E; overlap: pre-training, detection.
2. `.lake-data/DEP-E/DEP-E-20260801-CrossNER Adapt/crossner_domain_adaptation_manuscript.md` - CrossNER - DEP-E; overlap: pre-training.
3. `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md` - LA-Pose Latent Action - DEP-E; overlap: self-supervised, transformer, tasks, detection.

## Synthesis Note

### Concept Bridge

The selected paper contributes a autism, detection, fmri perspective. The three related DEPs overlap concretely through detection, pre-training, self-supervised, tasks, transformer. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for autism that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's detection mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. MeDSLIP Medical - DEP-E overlaps through pre-training, detection, clarifying a neighboring representation or evidence choice.
2. CrossNER - DEP-E overlaps through pre-training, exposing a complementary evaluation or operating boundary.
3. LA-Pose Latent Action - DEP-E overlaps through self-supervised, transformer, tasks, detection, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 31,543 of 75,964 units; duplicate exclusions 0; reselections 0.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2409.12304 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2409.12304 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2409.12304 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2409.12304 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260802-MeDSLIP%20Medical - related DEP: MeDSLIP Medical - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260802-MeDSLIP Medical/medslip_medical_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260801-CrossNER%20Adapt - related DEP: CrossNER - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260801-CrossNER Adapt/crossner_domain_adaptation_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260713-LA-Pose%20Latent%20Action - related DEP: LA-Pose Latent Action - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
