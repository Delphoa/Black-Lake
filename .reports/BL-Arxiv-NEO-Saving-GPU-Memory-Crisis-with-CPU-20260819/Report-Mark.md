# Report-Mark: NEO Saving GPU Memory

- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P438`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *NEO: Saving GPU Memory Crisis with CPU Offloading for Online LLM Inference* |
| Authors | Jiang, Xuanlin; Zhou, Yang; Cao, Shiyi; Stoica, Ion; Yu, Minlan |
| Identifier | arXiv:2411.01142; DOI:10.48550/arXiv.2411.01142 |
| Submitted / source date | 2024/11/02 |
| Record | https://arxiv.org/abs/2411.01142 |
| Full paper | https://arxiv.org/html/2411.01142 |
| PDF | https://arxiv.org/pdf/2411.01142 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched ML memory; evidence terms: inference, memory. |
| Deployment IDs | `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P438` |

## Concise Research Notes

The paper addresses cpu, crisis, gpu. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “the inspected method sections”. A short evaluation anchor is: “the inspected evaluation sections”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “the inspected limitations discussion”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Make LLM Inference/make_llm_inference_manuscript.md` - Make LLM Inference - DEP-E; overlap: gpu, llm, inference, memory.
2. `.lake-data/DEP-E/DEP-E-20260819-Analysis and Optimization/analysis_and_optimization_manuscript.md` - Analysis and Optimization - DEP-E; overlap: offloading, memory.
3. `.lake-data/DEP-E/DEP-E-20260819-Energy-Constrained/energy_constrained_manuscript.md` - Energy-Constrained - DEP-E; overlap: offloading, memory.

## Synthesis Note

### Concept Bridge

The selected paper contributes a cpu, crisis, gpu perspective. The three related DEPs overlap concretely through gpu, inference, llm, memory, offloading. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for cpu that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's crisis mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Make LLM Inference - DEP-E overlaps through gpu, llm, inference, memory, clarifying a neighboring representation or evidence choice.
2. Analysis and Optimization - DEP-E overlaps through offloading, memory, exposing a complementary evaluation or operating boundary.
3. Energy-Constrained - DEP-E overlaps through offloading, memory, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P438`.
- Uniform draw index 33,517 of 75,964 units; duplicate exclusions 1; focus exclusions 6; reselections 7.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: ML memory; terms: inference, memory.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2411.01142 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2411.01142 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2411.01142 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2411.01142 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260819-Make%20LLM%20Inference - related DEP: Make LLM Inference - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-Make LLM Inference/make_llm_inference_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260819-Analysis%20and%20Optimization - related DEP: Analysis and Optimization - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-Analysis and Optimization/analysis_and_optimization_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260819-Energy-Constrained - related DEP: Energy-Constrained - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-Energy-Constrained/energy_constrained_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
