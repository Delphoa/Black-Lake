# Report-Mark: Expert Streaming

- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P489`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Expert Streaming: Accelerating Low-Batch MoE Inference via Multi-chiplet Architecture and Dynamic Expert Trajectory Scheduling* |
| Authors | Ma, Songchen; Li, Hongyi; Zhang, Weihao; Tan, Yonghao; Dong, Pingcheng; Liu, Yu; Liu, Lan; Jiao, Yuzhong; Liu, Xuejiao; Liang, Luhong; Cheng, Kwang-Ting |
| Identifier | arXiv:2603.27624; DOI:10.48550/arXiv.2603.27624 |
| Submitted / source date | 2026/03/29 |
| Record | https://arxiv.org/abs/2603.27624 |
| Full paper | https://arxiv.org/html/2603.27624 |
| PDF | https://arxiv.org/pdf/2603.27624 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched stateful systems; evidence terms: inference, streaming. |
| Deployment IDs | `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P489` |

## Concise Research Notes

The paper addresses expert, accelerating, architecture. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “Mixture-of-Experts (MoE) is a promising approach for edge AI with low-batch inference. Yet, on-device deployments often face limited …”. A short evaluation anchor is: “Comprehensive evaluations on our system demonstrate that our approach not only achieves significant performance gains over state-of-the-art baselines …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “Mixture-of-Experts (MoE) is a promising approach for edge AI with low-batch inference. Yet, on-device deployments often face limited …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Accelerating LLM/accelerating_llm_manuscript.md` - Accelerating LLM - DEP-E; overlap: accelerating, dynamic, inference, architecture.
2. `.lake-data/DEP-E/DEP-E-20260819-Sparse-dLLM Accelerating/sparse_dllm_accelerating_manuscript.md` - Sparse-dLLM Accelerating - DEP-E; overlap: accelerating, dynamic, architecture.
3. `.lake-data/DEP-E/DEP-E-20260819-PISTO Proximal Inference/pisto_proximal_inference_manuscript.md` - PISTO Proximal Inference - DEP-E; overlap: trajectory, inference, architecture.

## Synthesis Note

### Concept Bridge

The selected paper contributes a expert, accelerating, architecture perspective. The three related DEPs overlap concretely through accelerating, architecture, dynamic, inference, trajectory. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for expert that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's accelerating mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Accelerating LLM - DEP-E overlaps through accelerating, dynamic, inference, architecture, clarifying a neighboring representation or evidence choice.
2. Sparse-dLLM Accelerating - DEP-E overlaps through accelerating, dynamic, architecture, exposing a complementary evaluation or operating boundary.
3. PISTO Proximal Inference - DEP-E overlaps through trajectory, inference, architecture, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P489`.
- Uniform draw index 71,996 of 75,964 units; duplicate exclusions 12; focus exclusions 23; reselections 35.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: stateful systems; terms: inference, streaming.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2603.27624 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2603.27624 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2603.27624 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2603.27624 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260819-Accelerating%20LLM - related DEP: Accelerating LLM - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-Accelerating LLM/accelerating_llm_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20002/DEP-E-20260819-Sparse-dLLM%20Accelerating - related DEP: Sparse-dLLM Accelerating - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-Sparse-dLLM Accelerating/sparse_dllm_accelerating_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20002/DEP-E-20260819-PISTO%20Proximal%20Inference - related DEP: PISTO Proximal Inference - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-PISTO Proximal Inference/pisto_proximal_inference_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
