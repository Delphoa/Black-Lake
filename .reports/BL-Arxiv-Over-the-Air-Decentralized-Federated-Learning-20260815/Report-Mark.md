# Report-Mark: Over-the-Air

- Deployment job ID: `BLAD-2200-20260815-A0637DE9`
- Deployment item ID: `BLAD-2200-20260815-A0637DE9-P04`
- Review date: 2026-08-15

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Over-the-Air Decentralized Federated Learning* |
| Authors | Shi, Yandong; Zhou, Yong; Shi, Yuanming |
| Identifier | arXiv:2106.08011; DOI:10.48550/arXiv.2106.08011 |
| Submitted / source date | 2021/06/15 |
| Record | https://arxiv.org/abs/2106.08011 |
| Full paper | https://arxiv.org/html/2106.08011 |
| PDF | https://arxiv.org/pdf/2106.08011 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260815-A0637DE9`; `BLAD-2200-20260815-A0637DE9-P04` |

## Concise Research Notes

The paper addresses decentralized, federated, over-the-air. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “In this paper, we consider decentralized federated learning (FL) over wireless networks, where over-the-air computation (AirComp) is adopted …”. A short evaluation anchor is: “In this paper, we consider decentralized federated learning (FL) over wireless networks, where over-the-air computation (AirComp) is adopted …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “In this paper, we consider decentralized federated learning (FL) over wireless networks, where over-the-air computation (AirComp) is adopted …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260729-Decoupled Training with/decoupled_training_with_manuscript.md` - Decoupled Training with - DEP-E; overlap: federated.
2. `.lake-data/DEP-E/DEP-E-20260804-Forget FOLTR/forget_foltr_manuscript.md` - FOLTR Unlearning - DEP-E; overlap: federated.
3. `.lake-data/DEP-E/DEP-E-20260814-Federated Learning with/federated_learning_with_manuscript.md` - Federated Learning with - DEP-E; overlap: federated.

## Synthesis Note

### Concept Bridge

The selected paper contributes a decentralized, federated, over-the-air perspective. The three related DEPs overlap concretely through federated. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for decentralized that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's federated mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Decoupled Training with - DEP-E overlaps through federated, clarifying a neighboring representation or evidence choice.
2. FOLTR Unlearning - DEP-E overlaps through federated, exposing a complementary evaluation or operating boundary.
3. Federated Learning with - DEP-E overlaps through federated, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 12,861 of 75,964 units; duplicate exclusions 0; reselections 0.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2106.08011 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2106.08011 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2106.08011 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2106.08011 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260729-Decoupled%20Training%20with - related DEP: Decoupled Training with - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260729-Decoupled Training with/decoupled_training_with_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260804-Forget%20FOLTR - related DEP: FOLTR Unlearning - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260804-Forget FOLTR/forget_foltr_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260814-Federated%20Learning%20with - related DEP: Federated Learning with - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260814-Federated Learning with/federated_learning_with_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
