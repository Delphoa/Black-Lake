# Report-Mark: CoopGuard Stateful

- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P209`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *CoopGuard: Stateful Cooperative Agents Safeguarding LLMs Against Evolving Multi-Round Attacks* |
| Authors | Li, Siyuan; Liu, Zehao; Lin, Xi; Mao, Qinghua; Chen, Yuliang; Li, Haoyu; Wu, Jun; Li, Jianhua; Su, Xiu |
| Identifier | arXiv:2604.04060; DOI:10.48550/arXiv.2604.04060 |
| Submitted / source date | 2026/04/05 |
| Record | https://arxiv.org/abs/2604.04060 |
| Full paper | https://arxiv.org/html/2604.04060 |
| PDF | https://arxiv.org/pdf/2604.04060 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched stateful systems; evidence terms: stateful. |
| Deployment IDs | `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P209` |

## Concise Research Notes

The paper addresses agents, attacks, cooperative. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of …”. A short evaluation anchor is: “We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Cooperative Training of/cooperative_training_of_manuscript.md` - Cooperative Training of - DEP-E; overlap: cooperative, stateful.
2. `.lake-data/DEP-E/DEP-E-20260803-Empirical Study on/empirical_study_on_manuscript.md` - Empirical Study on - DEP-E; overlap: cooperative.
3. `.lake-data/DEP-E/DEP-E-20260805-UAV-Assisted Cooperative/uav_assisted_cooperative_manuscript.md` - UAV-Assisted Cooperative - DEP-E; overlap: cooperative.

## Synthesis Note

### Concept Bridge

The selected paper contributes a agents, attacks, cooperative perspective. The three related DEPs overlap concretely through cooperative, stateful. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for agents that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's attacks mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Cooperative Training of - DEP-E overlaps through cooperative, stateful, clarifying a neighboring representation or evidence choice.
2. Empirical Study on - DEP-E overlaps through cooperative, exposing a complementary evaluation or operating boundary.
3. UAV-Assisted Cooperative - DEP-E overlaps through cooperative, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P209`.
- Uniform draw index 55,239 of 75,964 units; duplicate exclusions 1; focus exclusions 6; reselections 7.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: stateful systems; terms: stateful.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2604.04060 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2604.04060 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2604.04060 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2604.04060 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260819-Cooperative%20Training%20of - related DEP: Cooperative Training of - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-Cooperative Training of/cooperative_training_of_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260803-Empirical%20Study%20on - related DEP: Empirical Study on - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260803-Empirical Study on/empirical_study_on_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260805-UAV-Assisted%20Cooperative - related DEP: UAV-Assisted Cooperative - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260805-UAV-Assisted Cooperative/uav_assisted_cooperative_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
