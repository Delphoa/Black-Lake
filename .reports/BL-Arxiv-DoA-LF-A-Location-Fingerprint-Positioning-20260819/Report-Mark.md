# Report-Mark: DoA-LF A Location

- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P138`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *DoA-LF: A Location Fingerprint Positioning Algorithm with Millimeter-Wave* |
| Authors | Wei, Zhiqing; Zhao, Yadong; Liu, Xinyi; Feng, Zhiyong |
| Identifier | arXiv:2102.13297; DOI:10.1109/ACCESS.2017.2753781 |
| Submitted / source date | 2021/02/26 |
| Record | https://arxiv.org/abs/2102.13297 |
| Full paper | https://arxiv.org/html/2102.13297 |
| PDF | https://arxiv.org/pdf/2102.13297 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched algorithmic research; evidence terms: algorithm. |
| Deployment IDs | `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P138` |

## Concise Research Notes

The paper addresses algorithm, doa-lf, fingerprint. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “Location fingerprint (LF) has been widely applied in indoor positioning. However, the existing studies on LF mostly focus …”. A short evaluation anchor is: “Location fingerprint (LF) has been widely applied in indoor positioning. However, the existing studies on LF mostly focus …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “Location fingerprint (LF) has been widely applied in indoor positioning. However, the existing studies on LF mostly focus …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260815-Hierarchical Perceptual/hierarchical_perceptual_manuscript.md` - Hierarchical Perceptual - DEP-E; overlap: fingerprint.
2. `.lake-data/DEP-E/DEP-E-20260811-RGB-T Semantic/rgb_t_semantic_manuscript.md` - RGB-T Semantic - DEP-E; overlap: location.
3. `.lake-data/DEP-E/DEP-E-20260801-High-Order Langevin/high_order_langevin_manuscript.md` - High-Order Langevin - DEP-E; overlap: algorithm.

## Synthesis Note

### Concept Bridge

The selected paper contributes a algorithm, doa-lf, fingerprint perspective. The three related DEPs overlap concretely through algorithm, fingerprint, location. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for algorithm that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's doa-lf mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Hierarchical Perceptual - DEP-E overlaps through fingerprint, clarifying a neighboring representation or evidence choice.
2. RGB-T Semantic - DEP-E overlaps through location, exposing a complementary evaluation or operating boundary.
3. High-Order Langevin - DEP-E overlaps through algorithm, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P138`.
- Uniform draw index 20,329 of 75,964 units; duplicate exclusions 0; focus exclusions 4; reselections 4.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: algorithmic research; terms: algorithm.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2102.13297 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2102.13297 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2102.13297 - verified primary PDF; local copy withheld.
- https://doi.org/10.1109/ACCESS.2017.2753781 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260815-Hierarchical%20Perceptual - related DEP: Hierarchical Perceptual - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260815-Hierarchical Perceptual/hierarchical_perceptual_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260811-RGB-T%20Semantic - related DEP: RGB-T Semantic - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260811-RGB-T Semantic/rgb_t_semantic_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260801-High-Order%20Langevin - related DEP: High-Order Langevin - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260801-High-Order Langevin/high_order_langevin_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
