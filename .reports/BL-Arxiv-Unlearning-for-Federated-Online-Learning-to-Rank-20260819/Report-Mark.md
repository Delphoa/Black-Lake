# Report-Mark: Unlearning for Federated

- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P180`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Unlearning for Federated Online Learning to Rank: A Reproducibility Study* |
| Authors | Tao, Yiling; Wang, Shuyi; Yang, Jiaxi; Zuccon, Guido |
| Identifier | arXiv:2505.12791; DOI:10.48550/arXiv.2505.12791 |
| Submitted / source date | 2025/05/19 |
| Record | https://arxiv.org/abs/2505.12791 |
| Full paper | https://arxiv.org/html/2505.12791 |
| PDF | https://arxiv.org/pdf/2505.12791 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched stateful systems; evidence terms: online learning. |
| Deployment IDs | `BLAD-2200-20260819-9951C2C3`; `BLAD-2200-20260819-9951C2C3-P180` |

## Concise Research Notes

The paper addresses federated, online, rank. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “As a specialized distributed machine learning paradigm, FL enables collaborative training while preserving user privacy. To satisfy privacy-preserving …”. A short evaluation anchor is: “Federated approaches to ranking of search results have recently garnered attention to address users privacy concerns. In FOLTR, …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “Recent legislation introduced across numerous countries is establishing the so called “ the right to be forgotten ”, …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260804-Forget FOLTR/forget_foltr_manuscript.md` - FOLTR Unlearning - DEP-E; overlap: federated, unlearning, rank, online, reproducibility.
2. `.lake-data/DEP-E/DEP-E-20260819-Is Non-IID Data a Threat/is_non_iid_data_a_threat_manuscript.md` - Is Non-IID Data a Threat - DEP-E; overlap: federated, rank, online, unlearning, reproducibility.
3. `.lake-data/DEP-E/DEP-E-20260814-Privacy-Preserving/privacy_preserving_manuscript.md` - Privacy-Preserving - DEP-E; overlap: federated, unlearning, reproducibility.

## Synthesis Note

### Concept Bridge

The selected paper contributes a federated, online, rank perspective. The three related DEPs overlap concretely through federated, online, rank, reproducibility, unlearning. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for federated that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's online mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. FOLTR Unlearning - DEP-E overlaps through federated, unlearning, rank, online, reproducibility, clarifying a neighboring representation or evidence choice.
2. Is Non-IID Data a Threat - DEP-E overlaps through federated, rank, online, unlearning, reproducibility, exposing a complementary evaluation or operating boundary.
3. Privacy-Preserving - DEP-E overlaps through federated, unlearning, reproducibility, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-9951C2C3`; `BLAD-2200-20260819-9951C2C3-P180`.
- Uniform draw index 72,617 of 75,964 units; duplicate exclusions 0; focus exclusions 11; reselections 11.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: stateful systems; terms: online learning.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2505.12791 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2505.12791 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2505.12791 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2505.12791 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260804-Forget%20FOLTR - related DEP: FOLTR Unlearning - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260804-Forget FOLTR/forget_foltr_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20002/DEP-E-20260819-Is%20Non-IID%20Data%20a%20Threat - related DEP: Is Non-IID Data a Threat - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-Is Non-IID Data a Threat/is_non_iid_data_a_threat_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260814-Privacy-Preserving - related DEP: Privacy-Preserving - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260814-Privacy-Preserving/privacy_preserving_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
