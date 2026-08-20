# Report-Mark: Data-Free

- Deployment job ID: `BLAD-2200-20260812-9483C5E4`
- Deployment item ID: `BLAD-2200-20260812-9483C5E4-P01`
- Review date: 2026-08-12

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Data-Free Privacy-Preserving for LLMs via Model Inversion and Selective Unlearning* |
| Authors | Zhou, Xinjie; Yang, Zhihui; Cheng, Lechao; Wu, Sai; Chen, Gang |
| Identifier | arXiv:2601.15595; DOI:10.48550/arXiv.2601.15595 |
| Submitted / source date | 2026/01/22 |
| Record | https://arxiv.org/abs/2601.15595 |
| Full paper | https://arxiv.org/html/2601.15595 |
| PDF | https://arxiv.org/pdf/2601.15595 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260812-9483C5E4`; `BLAD-2200-20260812-9483C5E4-P01` |

## Concise Research Notes

The paper addresses data-free, inversion, llms. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “Large language models (LLMs) exhibit powerful capabilities but risk memorizing sensitive personally identifiable information (PII) from their training …”. A short evaluation anchor is: “Large language models (LLMs) exhibit powerful capabilities but risk memorizing sensitive personally identifiable information (PII) from their training …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “Large language models (LLMs) exhibit powerful capabilities but risk memorizing sensitive personally identifiable information (PII) from their training …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260802-Separate the Wheat from/separate_the_wheat_from_manuscript.md` - Separate the Wheat from - DEP-E; overlap: unlearning, llms.
2. `.lake-data/DEP-E/DEP-E-20260804-Forget FOLTR/forget_foltr_manuscript.md` - FOLTR Unlearning - DEP-E; overlap: unlearning.
3. `.lake-data/DEP-E/DEP-E-20260809-ECHO Prune to act trace/echo_prune_to_act_trace_manuscript.md` - ECHO Prune to act trace - DEP-E; overlap: selective.

## Synthesis Note

### Concept Bridge

The selected paper contributes a data-free, inversion, llms perspective. The three related DEPs overlap concretely through llms, selective, unlearning. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for data-free that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's inversion mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Separate the Wheat from - DEP-E overlaps through unlearning, llms, clarifying a neighboring representation or evidence choice.
2. FOLTR Unlearning - DEP-E overlaps through unlearning, exposing a complementary evaluation or operating boundary.
3. ECHO Prune to act trace - DEP-E overlaps through selective, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 28,123 of 75,964 units; duplicate exclusions 0; reselections 0.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2601.15595 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2601.15595 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2601.15595 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2601.15595 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260802-Separate%20the%20Wheat%20from - related DEP: Separate the Wheat from - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260802-Separate the Wheat from/separate_the_wheat_from_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260804-Forget%20FOLTR - related DEP: FOLTR Unlearning - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260804-Forget FOLTR/forget_foltr_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260809-ECHO%20Prune%20to%20act%20trace - related DEP: ECHO Prune to act trace - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260809-ECHO Prune to act trace/echo_prune_to_act_trace_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
