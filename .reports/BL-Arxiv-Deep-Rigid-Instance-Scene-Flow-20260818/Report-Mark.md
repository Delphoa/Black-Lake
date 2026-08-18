# Report-Mark: Deep Rigid Instance Scene

- Deployment job ID: `BLAD-2200-20260818-D85F5742`
- Deployment item ID: `BLAD-2200-20260818-D85F5742-P44`
- Review date: 2026-08-18

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Deep Rigid Instance Scene Flow* |
| Authors | Ma, Wei-Chiu; Wang, Shenlong; Hu, Rui; Xiong, Yuwen; Urtasun, Raquel |
| Identifier | arXiv:1904.08913; DOI:10.48550/arXiv.1904.08913 |
| Submitted / source date | 2019/04/18 |
| Record | https://arxiv.org/abs/1904.08913 |
| Full paper | https://arxiv.org/html/1904.08913 |
| PDF | https://arxiv.org/pdf/1904.08913 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | No one-time topic focus was requested.; matched unrestricted; evidence terms: not applicable. |
| Deployment IDs | `BLAD-2200-20260818-D85F5742`; `BLAD-2200-20260818-D85F5742-P44` |

## Concise Research Notes

The paper addresses flow, instance, rigid. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “With these problems in mind, we develop a novel deep rigid instance scene flow (DRISF) model that takes …”. A short evaluation anchor is: “In this paper we tackle the problem of scene flow estimation in the context of self-driving. We leverage …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “Optical flow is traditionally posed as an energy minimization task. It dates back to Horn and Schunck horn1981determining …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260811-Periodic Vibration/periodic_vibration_manuscript.md` - Periodic Vibration - DEP-E; overlap: scene, flow.
2. `.lake-data/DEP-E/DEP-E-20260810-Free Energy Surface/free_energy_surface_manuscript.md` - Free Energy Surface - DEP-E; overlap: flow.
3. `.lake-data/DEP-E/DEP-E-20260818-Unveil Inversion and/unveil_inversion_and_manuscript.md` - Unveil Inversion and - DEP-E; overlap: flow.

## Synthesis Note

### Concept Bridge

The selected paper contributes a flow, instance, rigid perspective. The three related DEPs overlap concretely through flow, scene. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for flow that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's instance mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Periodic Vibration - DEP-E overlaps through scene, flow, clarifying a neighboring representation or evidence choice.
2. Free Energy Surface - DEP-E overlaps through flow, exposing a complementary evaluation or operating boundary.
3. Unveil Inversion and - DEP-E overlaps through flow, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 14,652 of 75,964 units; duplicate exclusions 0; focus exclusions 0; reselections 0.
- One-time research-focus gate passed for No one-time topic focus was requested.; matched categories: unrestricted; terms: not applicable.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/1904.08913 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/1904.08913 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/1904.08913 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.1904.08913 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260811-Periodic%20Vibration - related DEP: Periodic Vibration - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260811-Periodic Vibration/periodic_vibration_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260810-Free%20Energy%20Surface - related DEP: Free Energy Surface - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260810-Free Energy Surface/free_energy_surface_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260818-Unveil%20Inversion%20and - related DEP: Unveil Inversion and - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260818-Unveil Inversion and/unveil_inversion_and_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
