# Report-Mark: Selective Weak

- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P464`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Selective Weak Supervision for Neural Information Retrieval* |
| Authors | Zhang, Kaitao; Xiong, Chenyan; Liu, Zhenghao; Liu, Zhiyuan |
| Identifier | arXiv:2001.10382; DOI:10.1145/3366423.3380131 |
| Submitted / source date | 2020/01/28 |
| Record | https://arxiv.org/abs/2001.10382 |
| Full paper | https://arxiv.org/html/2001.10382 |
| PDF | https://arxiv.org/pdf/2001.10382 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched ML memory; evidence terms: neural, retrieval. |
| Deployment IDs | `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P464` |

## Concise Research Notes

The paper addresses information, neural, retrieval. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “This work addresses the discrepancy between weak supervision methods and the needs of relevance matching, to liberate Neu-IR …”. A short evaluation anchor is: “This paper democratizes neural information retrieval to scenarios where large scale relevance training signals are not available. We …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “Without large scale relevance labels, the effectiveness of Neu-IR is more ambivalent ( Yang et al. 2019 ) …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Beyond Model Base/beyond_model_base_manuscript.md` - Beyond Model Base - DEP-E; overlap: retrieval, neural, weak.
2. `.lake-data/DEP-E/DEP-E-20260812-Data-Free/data_free_manuscript.md` - Data-Free - DEP-E; overlap: selective, information, weak.
3. `.lake-data/DEP-E/DEP-E-20260819-DecEx-RAG Boosting/decex_rag_boosting_manuscript.md` - DecEx-RAG Boosting - DEP-E; overlap: supervision, retrieval, weak.

## Synthesis Note

### Concept Bridge

The selected paper contributes a information, neural, retrieval perspective. The three related DEPs overlap concretely through information, neural, retrieval, selective, supervision. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for information that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's neural mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Beyond Model Base - DEP-E overlaps through retrieval, neural, weak, clarifying a neighboring representation or evidence choice.
2. Data-Free - DEP-E overlaps through selective, information, weak, exposing a complementary evaluation or operating boundary.
3. DecEx-RAG Boosting - DEP-E overlaps through supervision, retrieval, weak, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P464`.
- Uniform draw index 58,678 of 75,964 units; duplicate exclusions 9; focus exclusions 29; reselections 38.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: ML memory; terms: neural, retrieval.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2001.10382 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2001.10382 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2001.10382 - verified primary PDF; local copy withheld.
- https://doi.org/10.1145/3366423.3380131 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260819-Beyond%20Model%20Base - related DEP: Beyond Model Base - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-Beyond Model Base/beyond_model_base_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260812-Data-Free - related DEP: Data-Free - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260812-Data-Free/data_free_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260819-DecEx-RAG%20Boosting - related DEP: DecEx-RAG Boosting - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-DecEx-RAG Boosting/decex_rag_boosting_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
