# Report-Mark: Dirty Road Can Attack

- Deployment job ID: `BLAD-2200-20260818-D85F5742`
- Deployment item ID: `BLAD-2200-20260818-D85F5742-P05`
- Review date: 2026-08-18

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Dirty Road Can Attack: Security of Deep Learning based Automated Lane Centering under Physical-World Attack* |
| Authors | Sato, Takami; Shen, Junjie; Wang, Ningfei; Jia, Yunhan Jack; Lin, Xue; Chen, Qi Alfred |
| Identifier | arXiv:2009.06701; DOI:10.48550/arXiv.2009.06701 |
| Submitted / source date | 2020/09/14 |
| Record | https://arxiv.org/abs/2009.06701 |
| Full paper | https://arxiv.org/html/2009.06701 |
| PDF | https://arxiv.org/pdf/2009.06701 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260818-D85F5742`; `BLAD-2200-20260818-D85F5742-P05` |

## Concise Research Notes

The paper addresses attack, automated, centering. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “Automated Lane Centering (ALC) systems are convenient and widely deployed today, but also highly security and safety critical. …”. A short evaluation anchor is: “We evaluate our attack on a production ALC using 80 scenarios from real-world driving traces. The results show …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “Automated Lane Centering (ALC) systems are convenient and widely deployed today, but also highly security and safety critical. …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Stereo Lane Detection/stereo_lane_detection_manuscript.md` - Stereo Lane Detection - DEP-E; overlap: lane, road, under.
2. `.lake-data/DEP-E/DEP-E-20260809-From Similarity to/from_similarity_to_manuscript.md` - From Similarity to - DEP-E; overlap: attack, security, under.
3. `.lake-data/DEP-E/DEP-E-20260810-DexMimicGen Automated/dexmimicgen_automated_manuscript.md` - DexMimicGen Automated - DEP-E; overlap: automated, under.

## Synthesis Note

### Concept Bridge

The selected paper contributes a attack, automated, centering perspective. The three related DEPs overlap concretely through attack, automated, lane, road, security. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for attack that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's automated mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Stereo Lane Detection - DEP-E overlaps through lane, road, under, clarifying a neighboring representation or evidence choice.
2. From Similarity to - DEP-E overlaps through attack, security, under, exposing a complementary evaluation or operating boundary.
3. DexMimicGen Automated - DEP-E overlaps through automated, under, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 7,759 of 75,964 units; duplicate exclusions 1; reselections 1.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2009.06701 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2009.06701 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2009.06701 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2009.06701 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Stereo%20Lane%20Detection - related DEP: Stereo Lane Detection - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260716-Stereo Lane Detection/stereo_lane_detection_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260809-From%20Similarity%20to - related DEP: From Similarity to - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260809-From Similarity to/from_similarity_to_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260810-DexMimicGen%20Automated - related DEP: DexMimicGen Automated - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260810-DexMimicGen Automated/dexmimicgen_automated_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
