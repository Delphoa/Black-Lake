# Report-Mark: Security Non resettable

- Deployment job ID: `BLAD-2200-20260721-F7EDC854`
- Deployment item ID: `BLAD-2200-20260721-F7EDC854-P05`
- Review date: 2026-07-21

## Source Metadata

| Field | Value |
|---|---|
| Paper | *On the (In)Security of Non-resettable Device Identifiers in Custom Android Systems* |
| Authors | Dong, Zikan; Wang, Liu; Xu, Guoai; Wang, Haoyu |
| Identifier | arXiv:2502.15270; DOI:10.48550/arXiv.2502.15270 |
| Submitted / source date | 2025/02/21 |
| Record | https://arxiv.org/abs/2502.15270 |
| Full paper | https://arxiv.org/html/2502.15270 |
| PDF | https://arxiv.org/pdf/2502.15270 |
| Source state | Verified complete after one bounded archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260721-F7EDC854`; `BLAD-2200-20260721-F7EDC854-P05` |

## Concise Research Notes

The paper studies identifiers, device, access. The source characterizes IMEI as its central contribution and connects it to android, properties, settings. This review verified the full paper, inspected its method and evaluation narrative, and treats every performance statement as author-reported unless independently reproduced.

The practical value is an evidence-backed research pattern, not a deployment guarantee. Dataset composition, baselines, metrics, ablations, code and data availability, distribution shift, and operational constraints must be checked in the target setting. The review therefore emphasizes bounded offline evaluation, explicit provenance, abstention, and human judgment.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Abstract and introduction | Problem framing around identifiers, device, access | Source framing, not independent validation |
| Method sections | The mechanism associated with IMEI and android, properties, settings | Implementation was not rerun |
| Results and conclusion | Author-reported evaluation and stated implications | Metrics were not independently reproduced |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-XPRINT Traffic Privacy/xprint_traffic_privacy_manuscript.md` - XPRINT Traffic Privacy - DEP-E supplies a related evidence or mechanism lens for the synthesis.
2. `.lake-data/DEP-E/DEP-E-20260711-Telecom AI Roadmap/telecom_ai_roadmap_manuscript.md` - Telecom AI Roadmap - DEP-E supplies a related evidence or mechanism lens for the synthesis.
3. `.lake-data/DEP-E/DEP-E-20260720-Flash Loan Ecosystem/flash_loan_ecosystem_manuscript.md` - Flash Loan Ecosystem Review - DEP-E supplies a related evidence or mechanism lens for the synthesis.

## Synthesis Note

### Concept Bridge

The selected paper contributes a identifiers, device, access perspective. XPRINT Traffic Privacy - DEP-E, Telecom AI Roadmap - DEP-E, and Flash Loan Ecosystem Review - DEP-E provide neighboring views on representation, evaluation, or implementation. Together they support a provenance-first workflow that separates source evidence, reviewer inference, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor that maps each important output to a source, configuration, and uncertainty record.
2. Create a comparison harness that evaluates IMEI against simple baselines under frozen, versioned splits.
3. Add an abstaining review gate that blocks use when provenance, calibration, or shift checks fail.

### Deeper Relationship Observations

1. XPRINT Traffic Privacy - DEP-E overlaps through representation choices and the evidence retained for downstream tasks.
2. Telecom AI Roadmap - DEP-E exposes a complementary mechanism or optimization boundary that the selected work leaves implicit.
3. Flash Loan Ecosystem Review - DEP-E highlights how inductive bias and system constraints shape practical transfer.

### Conceptual Similarities

1. All four artifacts transform raw inputs into intermediate evidence rather than direct truth claims.
2. Each depends on explicit assumptions about data, representation, evaluation, and scope.
3. Each benefits from auditable versioning, negative controls, and failure-aware interpretation.

### MVP Implementations with Code Mock-Ups

1. Evidence map: `record = evaluate(input, config); require(record.provenance)`.
2. Frozen comparison: `scores = compare(baselines, candidate, split_manifest)`.
3. Abstention gate: `decision = review if drift or low_confidence else nonbinding_output`.

### Developer Challenges

1. Reproducing source preprocessing, baselines, and metrics without leakage or silent version drift.
2. Preserving evidence lineage while keeping the evaluation system maintainable and privacy-aware.
3. Designing stable explanations and stop conditions when inputs move outside the tested envelope.

### Author Challenges

1. Publishing enough configuration, data, and ablation detail for independent replication.
2. Separating benchmark improvement from claims of generalization or deployment readiness.
3. Reporting negative results, sensitivity, uncertainty, and failure cases alongside headline metrics.

## Validation Notes

- Uniform draw index 11,417 of 75,776 units; duplicate exclusions 0; reselections 0.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2502.15270 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2502.15270 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2502.15270 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2502.15270 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-XPRINT%20Traffic%20Privacy - related DEP: XPRINT Traffic Privacy - DEP-E.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260711-Telecom%20AI%20Roadmap - related DEP: Telecom AI Roadmap - DEP-E.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260720-Flash%20Loan%20Ecosystem - related DEP: Flash Loan Ecosystem Review - DEP-E.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
