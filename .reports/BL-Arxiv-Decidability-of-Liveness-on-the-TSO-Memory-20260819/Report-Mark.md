# Report-Mark: Decidability of Liveness

- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P48`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Decidability of Liveness on the TSO Memory Model* |
| Authors | Wang, Chao; Petri, Gustavo; Lv, Yi; Long, Teng; Liu, Zhiming |
| Identifier | arXiv:2107.09930; DOI:10.48550/arXiv.2107.09930 |
| Submitted / source date | 2021/07/21 |
| Record | https://arxiv.org/abs/2107.09930 |
| Full paper | https://arxiv.org/html/2107.09930 |
| PDF | https://arxiv.org/pdf/2107.09930 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched ML memory; evidence terms: memory, model. |
| Deployment IDs | `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P48` |

## Concise Research Notes

The paper addresses decidability, liveness, memory. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “An important property of concurrent objects is whether they support progress – a special case of liveness – …”. A short evaluation anchor is: “To the best of our knowledge, ours are the first decidability and undecidability results for liveness properties on …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “An important property of concurrent objects is whether they support progress – a special case of liveness – …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260710-Deep ESN Memory/deep_esn_memory_manuscript.md` - Deep ESN - DEP-E; overlap: memory.
2. `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` - Physical Data - DEP-E; overlap: memory.
3. `.lake-data/DEP-E/DEP-E-20260721-Stealth Memory Injection/stealth_memory_trust_manuscript.md` - Stealth Memory Trust - DEP-E; overlap: memory.

## Synthesis Note

### Concept Bridge

The selected paper contributes a decidability, liveness, memory perspective. The three related DEPs overlap concretely through memory. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for decidability that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's liveness mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Deep ESN - DEP-E overlaps through memory, clarifying a neighboring representation or evidence choice.
2. Physical Data - DEP-E overlaps through memory, exposing a complementary evaluation or operating boundary.
3. Stealth Memory Trust - DEP-E overlaps through memory, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P48`.
- Uniform draw index 61,801 of 75,964 units; duplicate exclusions 3; focus exclusions 33; reselections 36.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: ML memory; terms: memory, model.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2107.09930 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2107.09930 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2107.09930 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2107.09930 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260710-Deep%20ESN%20Memory - related DEP: Deep ESN - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260710-Deep ESN Memory/deep_esn_memory_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260710-Physical%20Data%20AI - related DEP: Physical Data - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260721-Stealth%20Memory%20Injection - related DEP: Stealth Memory Trust - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260721-Stealth Memory Injection/stealth_memory_trust_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
