# Report-Mark: Vulseye Detect Smart

- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P60`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Vulseye: Detect Smart Contract Vulnerabilities via Stateful Directed Graybox Fuzzing* |
| Authors | Liang, Ruichao; Chen, Jing; Wu, Cong; He, Kun; Wu, Yueming; Cao, Ruochen; Du, Ruiying; Liu, Yang; Zhao, Ziming |
| Identifier | arXiv:2408.10116; DOI:10.48550/arXiv.2408.10116 |
| Submitted / source date | 2024/08/19 |
| Record | https://arxiv.org/abs/2408.10116 |
| Full paper | https://arxiv.org/html/2408.10116 |
| PDF | https://arxiv.org/pdf/2408.10116 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched stateful systems; evidence terms: stateful. |
| Deployment IDs | `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P60` |

## Concise Research Notes

The paper addresses contract, detect, directed. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “To address these challenges, we propose Vulseye , a stateful directed graybox fuzzer for smart contracts guided by …”. A short evaluation anchor is: “To address these challenges, we propose Vulseye , a stateful directed graybox fuzzer for smart contracts guided by …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “Smart contracts, the cornerstone of decentralized applications, have become increasingly prominent in revolutionizing the digital landscape. However, vulnerabilities …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260817-ORFuzz Fuzzing the Other/orfuzz_fuzzing_the_other_manuscript.md` - ORFuzz Fuzzing the Other - DEP-E; overlap: fuzzing.
2. `.lake-data/DEP-E/DEP-E-20260717-Smart Coverage Goals/smart_coverage_goals_manuscript.md` - Smart Coverage Goals - DEP-E; overlap: smart, contract.
3. `.lake-data/DEP-E/DEP-E-20260819-Construction and/construction_and_manuscript.md` - Construction and - DEP-E; overlap: smart, stateful.

## Synthesis Note

### Concept Bridge

The selected paper contributes a contract, detect, directed perspective. The three related DEPs overlap concretely through contract, fuzzing, smart, stateful. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for contract that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's detect mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. ORFuzz Fuzzing the Other - DEP-E overlaps through fuzzing, clarifying a neighboring representation or evidence choice.
2. Smart Coverage Goals - DEP-E overlaps through smart, contract, exposing a complementary evaluation or operating boundary.
3. Construction and - DEP-E overlaps through smart, stateful, showing how implementation assumptions affect practical transfer.

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

- Deployment IDs validated: `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P60`.
- Uniform draw index 75,677 of 75,964 units; duplicate exclusions 6; focus exclusions 55; reselections 62.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: stateful systems; terms: stateful.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2408.10116 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2408.10116 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2408.10116 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2408.10116 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260817-ORFuzz%20Fuzzing%20the%20Other - related DEP: ORFuzz Fuzzing the Other - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260817-ORFuzz Fuzzing the Other/orfuzz_fuzzing_the_other_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260717-Smart%20Coverage%20Goals - related DEP: Smart Coverage Goals - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260717-Smart Coverage Goals/smart_coverage_goals_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260819-Construction%20and - related DEP: Construction and - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-Construction and/construction_and_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
