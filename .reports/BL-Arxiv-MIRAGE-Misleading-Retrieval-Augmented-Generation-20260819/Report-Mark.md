# Report-Mark: MIRAGE Misleading

- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P375`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *MIRAGE: Misleading Retrieval-Augmented Generation via Black-box and Query-agnostic Poisoning Attacks* |
| Authors | Chen, Tailun; He, Yu; Wang, Yan; Shao, Shuo; Zheng, Haolun; Liu, Zhihao; Li, Jinfeng; Qin, Zhizhen; Chen, Yuefeng; Chu, Zhixuan; Qin, Zhan; Ren, Kui |
| Identifier | arXiv:2512.08289; DOI:10.48550/arXiv.2512.08289 |
| Submitted / source date | 2025/12/09 |
| Record | https://arxiv.org/abs/2512.08289 |
| Full paper | https://arxiv.org/html/2512.08289 |
| PDF | https://arxiv.org/pdf/2512.08289 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched ML memory; evidence terms: retrieval augmented. |
| Deployment IDs | `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P375` |

## Concise Research Notes

The paper addresses attacks, black-box, generation. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “Retrieval-Augmented Generation (RAG) systems enhance LLMs with external knowledge but introduce a critical attack surface: corpus poisoning. While …”. A short evaluation anchor is: “Retrieval-Augmented Generation (RAG) systems enhance LLMs with external knowledge but introduce a critical attack surface: corpus poisoning. While …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “Retrieval-Augmented Generation (RAG) has emerged as a fundamental paradigm for enhancing Large Language Model (LLM) inference, effectively mitigating …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Practical Poisoning/practical_poisoning_manuscript.md` - Practical Poisoning - DEP-E; overlap: poisoning, attacks, retrieval-augmented, generation, misleading.
2. `.lake-data/DEP-E/DEP-E-20260719-DiscourseFlip RAG Risk/discourseflip_rag_risk_manuscript.md` - DiscourseFlip Risk Review; overlap: black-box, retrieval-augmented, generation, poisoning, attacks.
3. `.lake-data/DEP-E/DEP-E-20260819-UniC-RAG Universal/unic_rag_universal_manuscript.md` - UniC-RAG Universal - DEP-E; overlap: attacks, retrieval-augmented, generation, poisoning, misleading.

## Synthesis Note

### Concept Bridge

The selected paper contributes a attacks, black-box, generation perspective. The three related DEPs overlap concretely through attacks, black-box, generation, misleading, poisoning. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for attacks that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's black-box mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Practical Poisoning - DEP-E overlaps through poisoning, attacks, retrieval-augmented, generation, misleading, clarifying a neighboring representation or evidence choice.
2. DiscourseFlip Risk Review overlaps through black-box, retrieval-augmented, generation, poisoning, attacks, exposing a complementary evaluation or operating boundary.
3. UniC-RAG Universal - DEP-E overlaps through attacks, retrieval-augmented, generation, poisoning, misleading, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P375`.
- Uniform draw index 43,711 of 75,964 units; duplicate exclusions 0; focus exclusions 6; reselections 6.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: ML memory; terms: retrieval augmented.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2512.08289 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2512.08289 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2512.08289 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2512.08289 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20002/DEP-E-20260819-Practical%20Poisoning - related DEP: Practical Poisoning - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-Practical Poisoning/practical_poisoning_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260719-DiscourseFlip%20RAG%20Risk - related DEP: DiscourseFlip Risk Review; source basis `.lake-data/DEP-E/DEP-E-20260719-DiscourseFlip RAG Risk/discourseflip_rag_risk_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20002/DEP-E-20260819-UniC-RAG%20Universal - related DEP: UniC-RAG Universal - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-UniC-RAG Universal/unic_rag_universal_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
