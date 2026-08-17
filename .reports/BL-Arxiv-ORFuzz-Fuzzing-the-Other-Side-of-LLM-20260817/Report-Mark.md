# Report-Mark: ORFuzz Fuzzing the Other

- Deployment job ID: `BLAD-2200-20260817-2C1A830E`
- Deployment item ID: `BLAD-2200-20260817-2C1A830E-P05`
- Review date: 2026-08-17

## Source Metadata

| Field | Value |
|---|---|
| Paper | *ORFuzz: Fuzzing the "Other Side" of LLM Safety -- Testing Over-Refusal* |
| Authors | Zhang, Haonan; Wang, Dongxia; Liu, Yi; Chen, Kexin; Wang, Jiashui; Ying, Xinlei; Liu, Long; Wang, Wenhai |
| Identifier | arXiv:2508.11222; DOI:10.1109/ASE63991.2025.00156 |
| Submitted / source date | 2025/08/15 |
| Record | https://arxiv.org/abs/2508.11222 |
| Full paper | https://arxiv.org/html/2508.11222 |
| PDF | https://arxiv.org/pdf/2508.11222 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260817-2C1A830E`; `BLAD-2200-20260817-2C1A830E-P05` |

## Concise Research Notes

The paper addresses fuzzing, llm, orfuzz. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “Large Language Models (LLMs) have been found to show over-refusal problems—erroneously rejecting benign queries due to overly conservative …”. A short evaluation anchor is: “Large Language Models (LLMs) have been found to show over-refusal problems—erroneously rejecting benign queries due to overly conservative …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “Large Language Models (LLMs) have been found to show over-refusal problems—erroneously rejecting benign queries due to overly conservative …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md` - KDFlow LLM Distill - DEP-E; overlap: llm, side, other, testing, safety.
2. `.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav Review/sage_nav_manuscript.md` - SAGE-Nav Review - DEP-E; overlap: llm, other, testing, safety.
3. `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md` - Document Fraud LLM - DEP-E; overlap: llm, other, safety.

## Synthesis Note

### Concept Bridge

The selected paper contributes a fuzzing, llm, orfuzz perspective. The three related DEPs overlap concretely through llm, other, safety, side, testing. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for fuzzing that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's llm mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. KDFlow LLM Distill - DEP-E overlaps through llm, side, other, testing, safety, clarifying a neighboring representation or evidence choice.
2. SAGE-Nav Review - DEP-E overlaps through llm, other, testing, safety, exposing a complementary evaluation or operating boundary.
3. Document Fraud LLM - DEP-E overlaps through llm, other, safety, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 61,904 of 75,964 units; duplicate exclusions 0; reselections 0.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2508.11222 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2508.11222 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2508.11222 - verified primary PDF; local copy withheld.
- https://doi.org/10.1109/ASE63991.2025.00156 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260712-KDFlow%20LLM%20Distill - related DEP: KDFlow LLM Distill - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav%20Review - related DEP: SAGE-Nav Review - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav Review/sage_nav_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260715-Document%20Fraud%20LLM - related DEP: Document Fraud LLM - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
