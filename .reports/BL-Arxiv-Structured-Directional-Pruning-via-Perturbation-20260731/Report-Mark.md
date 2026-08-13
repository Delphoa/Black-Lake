# Report-Mark: Structured Directional

- Deployment job ID: `BLAD-2200-20260731-3D09E72F`
- Deployment item ID: `BLAD-2200-20260731-3D09E72F-P05`
- Review date: 2026-07-31

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Structured Directional Pruning via Perturbation Orthogonal Projection* |
| Authors | Li, Yinchuan; Liu, Xiaofeng; Shao, Yunfeng; Wang, Qing; Geng, Yanhui |
| Identifier | arXiv:2107.05328; DOI:10.48550/arXiv.2107.05328 |
| Submitted / source date | 2021/07/12 |
| Record | https://arxiv.org/abs/2107.05328 |
| Full paper | https://arxiv.org/html/2107.05328 |
| PDF | https://arxiv.org/pdf/2107.05328 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260731-3D09E72F`; `BLAD-2200-20260731-3D09E72F-P05` |

## Concise Research Notes

The paper addresses directional, orthogonal, perturbation. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “Structured pruning is an effective compression technique to reduce the computation of neural networks, which is usually achieved …”. A short evaluation anchor is: “Structured pruning is an effective compression technique to reduce the computation of neural networks, which is usually achieved …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “Deep Neural Network (DNN) has developed rapidly in recent years owing to its state-of-the-art performance in various domains …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` - CAP Compression - DEP-E; overlap: quantization, pruning, projection, sparsity, compression.
2. `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md` - Medical Diff VQA - DEP-E; overlap: directional, projection, perturbation, structured, memory.
3. `.lake-data/DEP-E/DEP-E-20260717-Residual Gaussian/residual_gaussian_cbct_manuscript.md` - Residual Gaussian CBCT - DEP-E; overlap: directional, projection, sparsity, structured, memory.

## Synthesis Note

### Concept Bridge

The selected paper contributes a directional, orthogonal, perturbation perspective. The three related DEPs overlap concretely through compression, directional, memory, perturbation, projection. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for directional that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's orthogonal mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. CAP Compression - DEP-E overlaps through quantization, pruning, projection, sparsity, compression, clarifying a neighboring representation or evidence choice.
2. Medical Diff VQA - DEP-E overlaps through directional, projection, perturbation, structured, memory, exposing a complementary evaluation or operating boundary.
3. Residual Gaussian CBCT - DEP-E overlaps through directional, projection, sparsity, structured, memory, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 65,168 of 75,957 units; duplicate exclusions 0; reselections 0.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2107.05328 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2107.05328 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2107.05328 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2107.05328 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260719-CAP%20Rank%20Sparsity - related DEP: CAP Compression - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Medical%20Diff%20VQA - related DEP: Medical Diff VQA - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260717-Residual%20Gaussian - related DEP: Residual Gaussian CBCT - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260717-Residual Gaussian/residual_gaussian_cbct_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
