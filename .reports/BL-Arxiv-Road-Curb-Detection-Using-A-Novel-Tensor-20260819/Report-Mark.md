# Report-Mark: Road Curb Detection Using

- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P386`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Road Curb Detection Using A Novel Tensor Voting Algorithm* |
| Authors | Zhu, Yilong; Han, Dong; Xue, Bohuan; Jiao, Jianhao; Zou, Zuhao; Liu, Ming; Fan, Rui |
| Identifier | arXiv:1911.12937; DOI:10.48550/arXiv.1911.12937 |
| Submitted / source date | 2019/11/29 |
| Record | https://arxiv.org/abs/1911.12937 |
| Full paper | https://arxiv.org/html/1911.12937 |
| PDF | https://arxiv.org/pdf/1911.12937 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched algorithmic research; evidence terms: algorithm. |
| Deployment IDs | `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P386` |

## Concise Research Notes

The paper addresses algorithm, curb, detection. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “Road curb detection is very important and neces-sary for autonomous driving because it can improve the safety and …”. A short evaluation anchor is: “Road curb detection is very important and neces-sary for autonomous driving because it can improve the safety and …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “However, most of the algorithms require some expen-sive Lidar, such as, Velodyne HDL-64-E, StreetMapper, and RIEGL VMX-250. These …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md` - Multi-Point ISAC - DEP-E; overlap: voting, algorithm, detection.
2. `.lake-data/DEP-E/DEP-E-20260818-Mask Proposal Voting/mask_proposal_voting_manuscript.md` - Mask Proposal Voting - DEP-E; overlap: voting, detection.
3. `.lake-data/DEP-E/DEP-E-20260819-A Novel Learning/a_novel_learning_manuscript.md` - A Novel Learning - DEP-E; overlap: novel, algorithm, detection.

## Synthesis Note

### Concept Bridge

The selected paper contributes a algorithm, curb, detection perspective. The three related DEPs overlap concretely through algorithm, detection, novel, voting. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for algorithm that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's curb mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Multi-Point ISAC - DEP-E overlaps through voting, algorithm, detection, clarifying a neighboring representation or evidence choice.
2. Mask Proposal Voting - DEP-E overlaps through voting, detection, exposing a complementary evaluation or operating boundary.
3. A Novel Learning - DEP-E overlaps through novel, algorithm, detection, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P386`.
- Uniform draw index 6,776 of 75,964 units; duplicate exclusions 2; focus exclusions 16; reselections 18.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: algorithmic research; terms: algorithm.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/1911.12937 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/1911.12937 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/1911.12937 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.1911.12937 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260716-Multi-Point%20ISAC - related DEP: Multi-Point ISAC - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260818-Mask%20Proposal%20Voting - related DEP: Mask Proposal Voting - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260818-Mask Proposal Voting/mask_proposal_voting_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260819-A%20Novel%20Learning - related DEP: A Novel Learning - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-A Novel Learning/a_novel_learning_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
