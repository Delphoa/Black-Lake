# Report-Mark: Learning Large

- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P80`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Learning Large Neighborhood Search Policy for Integer Programming* |
| Authors | Wu, Yaoxin; Song, Wen; Cao, Zhiguang; Zhang, Jie |
| Identifier | arXiv:2111.03466; DOI:10.48550/arXiv.2111.03466 |
| Submitted / source date | 2021/11/01 |
| Record | https://arxiv.org/abs/2111.03466 |
| Full paper | https://arxiv.org/html/2111.03466 |
| PDF | https://arxiv.org/pdf/2111.03466 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched algorithmic research; evidence terms: integer programming. |
| Deployment IDs | `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P80` |

## Concise Research Notes

The paper addresses integer, neighborhood, policy. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “We propose a deep reinforcement learning (RL) method to learn large neighborhood search (LNS) policy for integer programming …”. A short evaluation anchor is: “We propose a deep reinforcement learning (RL) method to learn large neighborhood search (LNS) policy for integer programming …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “We propose a deep reinforcement learning (RL) method to learn large neighborhood search (LNS) policy for integer programming …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Dynamic Partial Removal A/dynamic_partial_removal_a_manuscript.md` - Dynamic Partial Removal A - DEP-E; overlap: neighborhood, search.
2. `.lake-data/DEP-E/DEP-E-20260710-BEAGLE Learner/beagle_learner_manuscript.md` - BEAGLE Learner - DEP-E; overlap: programming, search, policy.
3. `.lake-data/DEP-E/DEP-E-20260727-Language-to-Space/language_to_space_manuscript.md` - Language-to-Space - DEP-E; overlap: programming.

## Synthesis Note

### Concept Bridge

The selected paper contributes a integer, neighborhood, policy perspective. The three related DEPs overlap concretely through neighborhood, policy, programming, search. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for integer that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's neighborhood mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Dynamic Partial Removal A - DEP-E overlaps through neighborhood, search, clarifying a neighboring representation or evidence choice.
2. BEAGLE Learner - DEP-E overlaps through programming, search, policy, exposing a complementary evaluation or operating boundary.
3. Language-to-Space - DEP-E overlaps through programming, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P80`.
- Uniform draw index 18,243 of 75,964 units; duplicate exclusions 1; focus exclusions 7; reselections 8.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: algorithmic research; terms: integer programming.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2111.03466 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2111.03466 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2111.03466 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2111.03466 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260819-Dynamic%20Partial%20Removal%20A - related DEP: Dynamic Partial Removal A - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-Dynamic Partial Removal A/dynamic_partial_removal_a_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260710-BEAGLE%20Learner - related DEP: BEAGLE Learner - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260710-BEAGLE Learner/beagle_learner_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260727-Language-to-Space - related DEP: Language-to-Space - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260727-Language-to-Space/language_to_space_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
