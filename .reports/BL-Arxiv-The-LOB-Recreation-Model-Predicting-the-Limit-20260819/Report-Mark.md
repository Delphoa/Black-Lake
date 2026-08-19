# Report-Mark: The LOB Recreation Model

- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P255`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *The LOB Recreation Model: Predicting the Limit Order Book from TAQ History Using an Ordinary Differential Equation Recurrent Neural Network* |
| Authors | Shi, Zijian; Chen, Yu; Cartlidge, John |
| Identifier | arXiv:2103.01670; DOI:10.48550/arXiv.2103.01670 |
| Submitted / source date | 2021/03/02 |
| Record | https://arxiv.org/abs/2103.01670 |
| Full paper | https://arxiv.org/html/2103.01670 |
| PDF | https://arxiv.org/pdf/2103.01670 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched stateful systems; evidence terms: recurrent neural. |
| Deployment IDs | `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P255` |

## Concise Research Notes

The paper addresses book, differential, equation. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “However, most prior work assumes that full LOB data is available for model training, but unfortunately this is …”. A short evaluation anchor is: “In an order-driven financial market, the price of a financial asset is discovered through the interaction of orders …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “In an order-driven financial market, the price of a financial asset is discovered through the interaction of orders …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Quantum Recurrent Neural/quantum_recurrent_neural_manuscript.md` - Quantum Recurrent Neural - DEP-E; overlap: differential, recurrent, neural.
2. `.lake-data/DEP-E/DEP-E-20260819-Predicting Long-Term/predicting_long_term_manuscript.md` - Predicting Long-Term - DEP-E; overlap: predicting, recurrent, network, neural.
3. `.lake-data/DEP-E/DEP-E-20260818-Multi-Path Feedback/multi_path_feedback_manuscript.md` - Multi-Path Feedback - DEP-E; overlap: recurrent, neural, network.

## Synthesis Note

### Concept Bridge

The selected paper contributes a book, differential, equation perspective. The three related DEPs overlap concretely through differential, network, neural, predicting, recurrent. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for book that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's differential mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Quantum Recurrent Neural - DEP-E overlaps through differential, recurrent, neural, clarifying a neighboring representation or evidence choice.
2. Predicting Long-Term - DEP-E overlaps through predicting, recurrent, network, neural, exposing a complementary evaluation or operating boundary.
3. Multi-Path Feedback - DEP-E overlaps through recurrent, neural, network, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P255`.
- Uniform draw index 56,412 of 75,964 units; duplicate exclusions 1; focus exclusions 3; reselections 4.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: stateful systems; terms: recurrent neural.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2103.01670 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2103.01670 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2103.01670 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2103.01670 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260819-Quantum%20Recurrent%20Neural - related DEP: Quantum Recurrent Neural - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-Quantum Recurrent Neural/quantum_recurrent_neural_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260819-Predicting%20Long-Term - related DEP: Predicting Long-Term - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-Predicting Long-Term/predicting_long_term_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260818-Multi-Path%20Feedback - related DEP: Multi-Path Feedback - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260818-Multi-Path Feedback/multi_path_feedback_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
