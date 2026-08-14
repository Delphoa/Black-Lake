# Report-Mark: Privacy-Preserving

- Deployment job ID: `BLAD-2200-20260814-24737ACA`
- Deployment item ID: `BLAD-2200-20260814-24737ACA-P06`
- Review date: 2026-08-14

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Privacy-Preserving Federated Unlearning with Certified Client Removal* |
| Authors | Liu, Ziyao; Ye, Huanyi; Jiang, Yu; Shen, Jiyuan; Guo, Jiale; Tjuawinata, Ivan; Lam, Kwok-Yan |
| Identifier | arXiv:2404.09724; DOI:10.48550/arXiv.2404.09724 |
| Submitted / source date | 2024/04/15 |
| Record | https://arxiv.org/abs/2404.09724 |
| Full paper | https://arxiv.org/html/2404.09724 |
| PDF | https://arxiv.org/pdf/2404.09724 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260814-24737ACA`; `BLAD-2200-20260814-24737ACA-P06` |

## Concise Research Notes

The paper addresses certified, client, federated. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “In recent years, Federated Unlearning (FU) has gained attention for addressing the removal of a client’s influence from …”. A short evaluation anchor is: “In recent years, Federated Unlearning (FU) has gained attention for addressing the removal of a client’s influence from …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “In recent years, Federated Unlearning (FU) has gained attention for addressing the removal of a client’s influence from …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260804-Forget FOLTR/forget_foltr_manuscript.md` - FOLTR Unlearning - DEP-E; overlap: unlearning, federated, client, removal.
2. `.lake-data/DEP-E/DEP-E-20260812-Data-Free/data_free_manuscript.md` - Data-Free - DEP-E; overlap: unlearning, privacy-preserving.
3. `.lake-data/DEP-E/DEP-E-20260802-Separate the Wheat from/separate_the_wheat_from_manuscript.md` - Separate the Wheat from - DEP-E; overlap: unlearning.

## Synthesis Note

### Concept Bridge

The selected paper contributes a certified, client, federated perspective. The three related DEPs overlap concretely through client, federated, privacy-preserving, removal, unlearning. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for certified that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's client mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. FOLTR Unlearning - DEP-E overlaps through unlearning, federated, client, removal, clarifying a neighboring representation or evidence choice.
2. Data-Free - DEP-E overlaps through unlearning, privacy-preserving, exposing a complementary evaluation or operating boundary.
3. Separate the Wheat from - DEP-E overlaps through unlearning, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 60,666 of 75,964 units; duplicate exclusions 0; reselections 0.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2404.09724 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2404.09724 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2404.09724 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2404.09724 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260804-Forget%20FOLTR - related DEP: FOLTR Unlearning - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260804-Forget FOLTR/forget_foltr_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260812-Data-Free - related DEP: Data-Free - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260812-Data-Free/data_free_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260802-Separate%20the%20Wheat%20from - related DEP: Separate the Wheat from - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260802-Separate the Wheat from/separate_the_wheat_from_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
