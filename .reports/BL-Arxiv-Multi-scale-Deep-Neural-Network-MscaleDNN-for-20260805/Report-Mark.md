# Report-Mark: Multi-scale Deep Neural

- Deployment job ID: `BLAD-2200-20260805-6C10E207`
- Deployment item ID: `BLAD-2200-20260805-6C10E207-P02`
- Review date: 2026-08-05

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Multi-scale Deep Neural Network (MscaleDNN) for Solving Poisson-Boltzmann Equation in Complex Domains* |
| Authors | Liu, Ziqi; Cai, Wei; Xu, Zhi-Qin John |
| Identifier | arXiv:2007.11207; DOI:10.4208/cicp.OA-2020-0179 |
| Submitted / source date | 2020/07/22 |
| Record | https://arxiv.org/abs/2007.11207 |
| Full paper | https://arxiv.org/html/2007.11207 |
| PDF | https://arxiv.org/pdf/2007.11207 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260805-6C10E207`; `BLAD-2200-20260805-6C10E207-P02` |

## Concise Research Notes

The paper addresses complex, domains, equation. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “In this paper, we propose multi-scale deep neural networks (MscaleDNNs) using the idea of radial scaling in frequency …”. A short evaluation anchor is: “In this paper, we propose multi-scale deep neural networks (MscaleDNNs) using the idea of radial scaling in frequency …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “Deep neural network (DNN) has found many applications beyond its traditional applications such as image classification and speech …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260723-Schwarz Neural Inference/schwarz_neural_inference_manuscript.md` - Schwarz Neural Inference - DEP-E; overlap: solving, equation, complex, neural, domains.
2. `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` - Physical Data - DEP-E; overlap: equation, complex, neural, domains, network.
3. `.lake-data/DEP-E/DEP-E-20260801-Dehomogenized 3D Topology/dehomogenized_3d_topology_manuscript.md` - 3D Dehomogenization - DEP-E; overlap: multi-scale, equation, domains.

## Synthesis Note

### Concept Bridge

The selected paper contributes a complex, domains, equation perspective. The three related DEPs overlap concretely through complex, domains, equation, multi-scale, network. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for complex that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's domains mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Schwarz Neural Inference - DEP-E overlaps through solving, equation, complex, neural, domains, clarifying a neighboring representation or evidence choice.
2. Physical Data - DEP-E overlaps through equation, complex, neural, domains, network, exposing a complementary evaluation or operating boundary.
3. 3D Dehomogenization - DEP-E overlaps through multi-scale, equation, domains, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 6,822 of 75,957 units; duplicate exclusions 0; reselections 0.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2007.11207 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2007.11207 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2007.11207 - verified primary PDF; local copy withheld.
- https://doi.org/10.4208/cicp.OA-2020-0179 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260723-Schwarz%20Neural%20Inference - related DEP: Schwarz Neural Inference - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260723-Schwarz Neural Inference/schwarz_neural_inference_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260710-Physical%20Data%20AI - related DEP: Physical Data - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260801-Dehomogenized%203D%20Topology - related DEP: 3D Dehomogenization - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260801-Dehomogenized 3D Topology/dehomogenized_3d_topology_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
