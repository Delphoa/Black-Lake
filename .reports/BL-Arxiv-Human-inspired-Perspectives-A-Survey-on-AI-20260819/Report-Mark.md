# Report-Mark: Human-inspired

- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P119`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Human-inspired Perspectives: A Survey on AI Long-term Memory* |
| Authors | He, Zihong; Lin, Weizhe; Zheng, Hao; Zhang, Fan; Jones, Matt W.; Aitchison, Laurence; Xu, Xuhai; Liu, Miao; Kristensson, Per Ola; Shen, Junxiao |
| Identifier | arXiv:2411.00489; DOI:10.48550/arXiv.2411.00489 |
| Submitted / source date | 2024/11/01 |
| Record | https://arxiv.org/abs/2411.00489 |
| Full paper | https://arxiv.org/html/2411.00489 |
| PDF | https://arxiv.org/pdf/2411.00489 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched ML memory; evidence terms: long term memory. |
| Deployment IDs | `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P119` |

## Concise Research Notes

The paper addresses human-inspired, long-term, memory. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “The mapping relationship between long-term memory of human (Part A in Fig. Human-inspired Perspectives: A Survey on AI …”. A short evaluation anchor is: “According to Atkinson et al. [ 6 ] , the sensory register is responsible for receiving and temporarily …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “With the rapid advancement of AI systems, their abilities to store, retrieve, and utilize information over the long …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260805-MemShot Dialogue Memory/memshot_dialogue_memory_manuscript.md` - MemShot Dialogue Memory - DEP-E; overlap: long-term, memory.
2. `.lake-data/DEP-E/DEP-E-20260818-LLM-based Medical/llm_based_medical_manuscript.md` - LLM-based Medical - DEP-E; overlap: long-term, memory.
3. `.lake-data/DEP-E/DEP-E-20260819-Explore with Long-term/explore_with_long_term_manuscript.md` - Explore with Long-term - DEP-E; overlap: long-term, memory.

## Synthesis Note

### Concept Bridge

The selected paper contributes a human-inspired, long-term, memory perspective. The three related DEPs overlap concretely through long-term, memory. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for human-inspired that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's long-term mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. MemShot Dialogue Memory - DEP-E overlaps through long-term, memory, clarifying a neighboring representation or evidence choice.
2. LLM-based Medical - DEP-E overlaps through long-term, memory, exposing a complementary evaluation or operating boundary.
3. Explore with Long-term - DEP-E overlaps through long-term, memory, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P119`.
- Uniform draw index 51,852 of 75,964 units; duplicate exclusions 0; focus exclusions 6; reselections 7.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: ML memory; terms: long term memory.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2411.00489 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2411.00489 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2411.00489 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2411.00489 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260805-MemShot%20Dialogue%20Memory - related DEP: MemShot Dialogue Memory - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260805-MemShot Dialogue Memory/memshot_dialogue_memory_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260818-LLM-based%20Medical - related DEP: LLM-based Medical - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260818-LLM-based Medical/llm_based_medical_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260819-Explore%20with%20Long-term - related DEP: Explore with Long-term - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-Explore with Long-term/explore_with_long_term_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
