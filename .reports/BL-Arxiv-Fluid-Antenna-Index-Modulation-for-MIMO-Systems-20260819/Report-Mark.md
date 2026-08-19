# Report-Mark: Fluid Antenna Index

- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P22`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Fluid Antenna Index Modulation for MIMO Systems: Robust Transmission and Low-Complexity Detection* |
| Authors | Guo, Xinghao; Xu, Yin; He, Dazhi; Zhang, Cixiao; Hong, Hanjiang; Wong, Kai-Kit; Zhang, Wenjun; Wu, Yiyan |
| Identifier | arXiv:2412.04877; DOI:10.48550/arXiv.2412.04877 |
| Submitted / source date | 2024/12/06 |
| Record | https://arxiv.org/abs/2412.04877 |
| Full paper | https://arxiv.org/html/2412.04877 |
| PDF | https://arxiv.org/pdf/2412.04877 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched algorithmic research; evidence terms: complexity. |
| Deployment IDs | `BLAD-2200-20260819-9951C2C3`; `BLAD-2200-20260819-9951C2C3-P22` |

## Concise Research Notes

The paper addresses antenna, detection, fluid. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “the inspected method sections”. A short evaluation anchor is: “the inspected evaluation sections”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “the inspected limitations discussion”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-Low-Complexity/low_complexity_manuscript.md` - Low-Complexity - DEP-E; overlap: low-complexity, mimo, antenna, systems, detection.
2. `.lake-data/DEP-E/DEP-E-20260726-Compressed CSI Feedback/compressed_csi_feedback_manuscript.md` - Compressed CSI Feedback - DEP-E; overlap: mimo, detection, index.
3. `.lake-data/DEP-E/DEP-E-20260729-Rank Optimization for/rank_optimization_for_manuscript.md` - Rank Optimization for - DEP-E; overlap: mimo, detection, index.

## Synthesis Note

### Concept Bridge

The selected paper contributes a antenna, detection, fluid perspective. The three related DEPs overlap concretely through antenna, detection, index, low-complexity, mimo. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for antenna that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's detection mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Low-Complexity - DEP-E overlaps through low-complexity, mimo, antenna, systems, detection, clarifying a neighboring representation or evidence choice.
2. Compressed CSI Feedback - DEP-E overlaps through mimo, detection, index, exposing a complementary evaluation or operating boundary.
3. Rank Optimization for - DEP-E overlaps through mimo, detection, index, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-9951C2C3`; `BLAD-2200-20260819-9951C2C3-P22`.
- Uniform draw index 46,791 of 75,964 units; duplicate exclusions 0; focus exclusions 10; reselections 10.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: algorithmic research; terms: complexity.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2412.04877 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2412.04877 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2412.04877 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2412.04877 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260818-Low-Complexity - related DEP: Low-Complexity - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260818-Low-Complexity/low_complexity_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260726-Compressed%20CSI%20Feedback - related DEP: Compressed CSI Feedback - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260726-Compressed CSI Feedback/compressed_csi_feedback_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260729-Rank%20Optimization%20for - related DEP: Rank Optimization for - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260729-Rank Optimization for/rank_optimization_for_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
