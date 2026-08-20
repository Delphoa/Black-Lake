---
title: "Spectrum ML - DEP-E"
generated_at: "2026-08-20"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of Analysis of Spectrum Occupancy Using Machine Learning Algorithms."
source_status: "verified local PDF and full-paper HTML; source files withheld locally"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-20"
temporal_cutoff: "arXiv v1 submitted 2015-03-24; public sources accessed 2026-08-20"
primary_url: "https://arxiv.org/abs/1503.07104"
stable_identifier: "arXiv:1503.07104; DOI:10.48550/arXiv.1503.07104; journal DOI:10.1109/TVT.2015.2487047"
confidence_summary: "Medium-high for source description and reported metrics; lower for external validity because no raw data or code reproduction was available."
safety_scope: "simulation-only research review; no live radio or network authority"
distribution_notes: "Public Markdown cites public URLs; original PDF, HTML, metadata, and source-package material withheld locally."
---

# Spectrum ML - DEP-E

## Source Metadata

| Field | Value |
|---|---|
| Work title | *Analysis of Spectrum Occupancy Using Machine Learning Algorithms* |
| Authors | Freeha Azmat; Yunfei Chen; Nigel Stocks |
| Source platform | arXiv, Computer Science > Networking and Internet Architecture; also Machine Learning |
| Version and date | v1; submitted 2015-03-24 |
| Journal record | *IEEE Transactions on Vehicular Technology*, 65(9), 6853-6860 (2016) |
| Identifiers | arXiv:1503.07104; arXiv DOI: 10.48550/arXiv.1503.07104; journal DOI: 10.1109/TVT.2015.2487047 |
| Primary URLs | https://arxiv.org/abs/1503.07104; https://arxiv.org/html/1503.07104; https://arxiv.org/pdf/1503.07104 |
| Public bibliographic cross-check | https://dblp.org/rec/journals/tvt/AzmatCS16.html |
| Local source files | Verified PDF, full-paper HTML, metadata HTML, and acquisition records retained locally; paths withheld from this public artifact |
| Source package | Unavailable through the brokered redirect policy; not uploaded |
| Official code | No official code repository identified in the inspected source and author/publication records |
| License and usage | Public arXiv metadata and paper URLs cited; redistribution rights for source files were not used |
| Access date | 2026-08-20 |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | https://arxiv.org/abs/1503.07104 | Primary paper metadata | Title, authors, version, abstract, date, subjects, and DOI link | Source identity and abstract-level thesis | High | Abstract is insufficient for detailed empirical claims |
| E2 | https://arxiv.org/html/1503.07104 | Primary full-paper HTML | Measurement setup, occupancy definitions, algorithms, evaluation splits, figures/captions, Table I, outage estimates, and references | Method and results claims | High | HTML conversion may omit layout nuance; no raw data/code |
| E3 | https://arxiv.org/pdf/1503.07104 | Primary paper PDF | PDF header/EOF integrity, page count, text extraction, and cross-check of sections/tables | Source integrity and paper structure | High for identity; medium for layout-dependent extraction | PDF raster rendering was unavailable because Poppler tools were absent |
| E4 | https://doi.org/10.1109/TVT.2015.2487047 | Journal DOI | Publication identity and venue locator | Journal context and version distinction | Medium-high | DOI landing page was not used as full text |
| E5 | https://dblp.org/rec/journals/tvt/AzmatCS16.html | Bibliographic record | Authors, journal, volume, issue, pages, year, DOI, and access status | Publication cross-check | Medium-high | Bibliographic record does not validate experiments |
| E6 | `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md` | Related Black Lake manuscript | Structure-aware wireless ML, delay-Doppler representation, online learning, and simulation boundary | Related conceptual bridge | Medium | Generated related artifact; not independent validation |
| E7 | `.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/joint_sensing_mec_manuscript.md` | Related Black Lake manuscript | Sensing validity, sampling cadence, wireless transmission, AoI, energy, and edge computation | Related resource and freshness bridge | Medium | Generated related artifact; not independent validation |
| E8 | `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md` | Related Black Lake manuscript | Sensing/communication mode selection, fusion quality, power constraints, and simulation-only boundary | Related allocation and authority bridge | Medium | Generated related artifact; not independent validation |

## Executive Summary

Azmat, Chen, and Stocks study spectrum occupancy in cognitive radio networks using radiometer measurements from eight frequency bands between 880 MHz and 2500 MHz collected over approximately four months. The paper thresholds per-frequency-bin measurements into occupancy features, labels primary-user status using occupancy and consecutive-free-bin rules, and compares four supervised algorithms—naive Bayes, decision trees, linear SVM, and linear regression—with an unsupervised hidden Markov model. It then tunes the SVM box constraint with a firefly algorithm and estimates secondary-user outage from predicted free-slot runs (E1-E3).

The central author claim is that the best method depends on the setting and that SVM+FFA can outperform the comparison methods. The reported results support that claim within the inspected scenarios: naive Bayes reaches mean accuracy `0.9493` in the `k=55` comparison; SVM reaches `0.8528` in the `k=192` comparison; SVM+FFA reaches `0.8728` in a 30-day `k=192` comparison and `0.9034` in the 15%/85% split in Table I. The same table reports much higher SVM+FFA computation time than SVM. Reviewer confidence is medium-high for what the paper reports and medium for generalization because raw traces, executable code, repeated-seed uncertainty, and independent reproduction were not available.

## Detailed Summary

### Problem and Context

Cognitive radio networks pair licensed primary users (PUs) with unlicensed secondary users (SUs) that may access unused spectrum without harmful interference. The paper argues that conventional occupancy models rely on assumptions that may not match heterogeneous measurements, motivating a comparison of several machine-learning classifiers. The practical target is not classification alone: predicted PU status is used to estimate whether an SU can find enough consecutive free time slots for transmission (E1, E2).

### Data and System Model

The measurements span 880-2500 MHz and eight named bands. The paper describes roughly four months of data, from 6 February to 18 June 2013, amounting to 131 days or 188,917 minutes. Frequency-bin counts vary by band; the example 925-960 MHz band has 192 bins at 0.18 MHz each, while the 1710-1785 MHz band has 448 bins at 0.167 MHz each. Each time/frequency sample is compared with a dynamic threshold. Occupancy for a time slot is the fraction of occupied bins.

The primary-user label is derived from lower and upper occupancy bounds plus a consecutive-free-bin condition. The paper states that upper occupancy should not be below 75% and lower occupancy should not exceed 40% in its tested setting, but it also shows that the selected range and threshold vary by day and threshold. The resulting feature vector is a binary frequency-bin status vector and the response is occupied or idle.

### Learning Framework

The proposed comparison uses a 15% training and 85% testing split for the main framework. Naive Bayes assumes feature independence, decision trees split the feature space by entropy, linear SVM separates occupied and idle classes with a margin, linear regression uses a stepwise model selected by sum-of-squares error, and HMM models time-series state transitions and emissions. The SVM+FFA variant searches over the SVM box constraint using firefly positions whose brightness is classification accuracy (E2).

### Evaluation and Results

The paper reports several context-dependent comparisons:

- For `k=55`, mean accuracies are LR `0.9257`, SVM `0.9162`, DT `0.8483`, NBC `0.9493`, and HMM `0.4790`. Reported per-iteration computation times are 350.19, 0.092, 0.0136, 0.0045, and 0.0171 seconds respectively.
- For `k=192` over 30 days, trained HMM, HMM, SVM, DT, and NBC reach mean accuracies `0.6816`, `0.4887`, `0.8528`, `0.8392`, and `0.7970`; reported times are `0.0205`, `0.09066`, `0.0135`, `0.0163`, and `0.0095` seconds respectively.
- In the SVM+FFA comparison, mean accuracies are SVM+FFA `0.8728`, SVM `0.8499`, DT `0.7970`, NBC `0.8392`, and HMM `0.4822`.
- Table I reports for a 15%/85% train/test split: DT `0.7612`, SVM `0.8945`, SVM+FFA `0.9034`, HMM `0.4925`, and NBC `0.8714`; the corresponding reported times are `0.0132`, `0.0128`, `3.0412`, `0.0241`, and `0.0084` seconds. For 30%/70%, the accuracies are `0.8028`, `0.9143`, `0.9189`, `0.4841`, and `0.9064`.
- For the reported outage example, expected SU outage is `0.9191`; predicted values are SVM+FFA `0.9264`, SVM `0.9322`, NBC `0.9638`, DT `0.9577`, and HMM `1.0`.

These numbers are source-reported and scenario-specific. The paper does not provide a public reproduction package, confidence intervals, or hardware-normalized runtime protocol, so they should not be interpreted as a current leaderboard.

### Conclusion and Source Boundary

The paper's durable contribution is a connected evaluation pattern: measure occupancy, define a protection-aware label, compare classifiers, optimize a model parameter, and evaluate a downstream outage consequence. Its boundary is equally important: one measurement campaign, a narrow set of bands, hand-selected thresholds and splits, and no public executable reproduction. The arXiv HTML has an explicit sectioned body but no separate conclusion heading; the final claim is carried by the results discussion and abstract.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | The paper compares supervised and unsupervised ML for spectrum occupancy and connects predictions to SU outage. | Author claim | E1, E2 | Directly supported by the abstract, system model, and results sections. | High |
| C2 | The evaluation uses radiometer data from eight bands over approximately four months. | Source metadata / author description | E2, E3 | Directly supported; exact campaign scope is not independently reproduced. | High |
| C3 | SVM+FFA improves reported accuracy over conventional SVM in the tested comparisons. | Author claim / benchmark result | E2 | Supported in the reported scenarios, with a substantial compute-time tradeoff. | High for reported result; medium for generalization |
| C4 | No single classifier is uniformly best across feature widths and settings. | Reviewer interpretation | E2 | Supported by the `k=55` NBC result and `k=192` SVM/SVM+FFA results. | Medium-high |
| C5 | Downstream outage estimates are more decision-relevant than accuracy alone. | Reviewer interpretation | E2, E7, E8 | The paper computes outage, while related work makes resource and sensing costs explicit. | Medium |
| C6 | The work is not independently reproducible from the inspected public artifact set. | Reviewer assessment | E2-E5 | No raw traces, code, repeatability package, or uncertainty analysis was found. | Medium-high |

## Methodology

- `Research objective`: Preserve a source-grounded review of the selected paper, its reported evidence, its limitations, and safe implementation implications.
- `Sources inspected`: Verified local PDF and full-paper HTML; local metadata/provenance records; public arXiv abstract and DOI; public DBLP publication metadata; and exactly three related Black Lake DEP manuscripts.
- `Discovery strategy`: Enumerated the local archive with `rg --files -g "*.pdf"`; normalized unique parent units; used a uniform PowerShell `Get-Random` index; scanned public artifact areas, automation memory, and related inventory for duplicate markers; then inspected primary paper and publication sources.
- `Selection methodology`: 75,967 PDF candidates became 75,964 unique parent-directory paper units after deduplication. The sorted-unit draw selected zero-based index 10,451. The first draw was retained after 0 duplicate exclusions, 0 other exclusions, and 0 reselections.
- `Source-integrity methodology`: The initial unit was classified as partial because full-paper HTML was absent. One bounded brokered single-paper repair was performed. Final verification required PDF size at least 10 KB, `%PDF-` header, trailing `%%EOF`, and full-paper HTML size/body/marker/heading/structure checks.
- `Inclusion criteria`: Primary paper evidence, authoritative publication metadata, and related DEP entries with concrete overlap in wireless state representation, sensing/resource tradeoffs, or joint sensing/communication allocation.
- `Exclusion criteria`: Abstract-only evidence for detailed empirical claims; unverified repositories or code; related entries without a concrete conceptual bridge; and all local source files from public outputs.
- `Analytical approach`: Empirical, comparative, conceptual, implementation, replication, and safety/ethics analysis.
- `Evidence handling`: Major claims receive claim IDs and map to evidence-ledger IDs. Author claims, source metadata, reviewer interpretations, and implementation proposals are labeled separately.
- `Uncertainty handling`: Reported metrics are preserved with their dataset/configuration context; missing raw data, code, uncertainty intervals, visual-rendering capability, and external validation are stated rather than inferred.
- `Extraction process`: Full-paper HTML was structurally parsed for sections and tables; PDF text was cross-checked with a local PDF parser; no raster PDF rendering was available because Poppler tools were not installed.
- `Version control`: The review is pinned to arXiv v1 and the journal record identified by DOI 10.1109/TVT.2015.2487047.
- `Claim selection`: Priority went to the data setup, occupancy label, algorithm comparison, reported metrics, downstream outage calculation, source availability, and deployment boundary.
- `Cross-checking`: Authors, dates, journal details, DOI, title, section structure, and key numeric results were cross-checked across arXiv, the PDF, the HTML, and DBLP.
- `Safety handling`: Implementation examples are synthetic and evaluation-only. No example controls a radio, accesses private traces, or bypasses licensing or authorization.
- `Reviewer stance`: DEP-ready source preservation, critical paper review, implementation translation, and bounded replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: The selected arXiv paper, its public journal identity, reported method/results, three related DEP bridges, and safe follow-on evaluation ideas.
- `Temporal boundary`: ArXiv v1 submitted 2015-03-24 and public source access on 2026-08-20.
- `Evidence limits`: No raw spectrum traces, source package, executable code, repeated-seed results, confidence intervals, or hardware-normalized runtime protocol were available. PDF raster rendering was unavailable.
- `Assumptions`: The extracted HTML formulas and Table I values accurately represent the source; the journal DOI record refers to the same research work; reported time units are seconds as written.
- `Constraints`: Source documents and caches must remain local; public artifacts may contain only generated Markdown and public URLs; live radio or network control is out of scope.
- `Out of scope`: Independent reproduction, regulatory approval, radio-frequency measurement, live spectrum allocation, current classifier benchmarking, or claims about present-day wireless conditions.
- `Intended use`: Research review, future benchmark design, safe implementation ideation, and durable DEP provenance.
- `Audience`: Wireless ML researchers, benchmark engineers, systems reviewers, and product/safety planners.
- `Depth target`: Full manuscript research artifact with evidence ledger and implementation translation.
- `Reproducibility boundary`: A reviewer can reconstruct the paper's conceptual pipeline and reported metrics, but cannot reproduce the original campaign or exact tables without data, code, and parameter details.
- `Operational boundary`: Discuss prediction and simulation only; do not operationalize radio-control or spectrum-access actions.
- `Data sensitivity`: The paper is public, but raw spectrum traces could reveal location, occupancy, or user-behavior information and are therefore withheld.

## Observations

- `Observed pattern`: Classifier rankings change with feature width and evaluation context; `k=55` favors NBC while `k=192` favors SVM or SVM+FFA.
- `Technical implication`: A benchmark should report downstream outage, calibration, runtime, and protection-cost measures alongside accuracy.
- `Contradiction or tension`: SVM+FFA improves reported accuracy but increases computation time by orders of magnitude in Table I, making the best research score potentially unattractive for constrained edge systems.
- `Boundary condition`: Threshold and occupancy-split choices are selected from campaign-specific distributions, so transfer to another receiver or band is unproven.
- `Open question`: Whether the apparent periodicity in some bands can be exploited by a temporal model without increasing false alarms or privacy exposure is not resolved.
- `Reviewer hypothesis`: A representation that preserves band relationships and temporal context may reduce the need for expensive parameter search, but this requires a controlled comparison rather than an assumption.

## Considerations

The system sits near a safety and regulatory boundary. A false idle prediction can increase interference risk, while a false occupied prediction can reduce spectrum utilization. Any implementation should therefore expose calibrated confidence and abstention, preserve audit logs without raw sensitive traces, and keep proposal generation separate from authorization and radio actuation.

Data governance matters even when the source paper is public. Longitudinal spectrum measurements can encode location, site activity, or user behavior. Public benchmarks should prefer synthetic or redacted traces, document collection permissions, and control retention. A deployment should monitor receiver calibration, threshold drift, band changes, seasonal variation, and class imbalance.

The paper's computation-time comparison is useful but incomplete without hardware, implementation language, parallelism, and measurement protocol. Product decisions should treat the reported times as within-paper indicators, not cross-platform service-level estimates.

## Strengths

- Connects measurement, classification, and downstream SU outage rather than reporting accuracy in isolation.
- Compares multiple model families and includes an unsupervised temporal baseline instead of assuming one algorithmic paradigm.
- Makes threshold selection and occupancy-label construction visible, which exposes important transfer assumptions.
- Reports both accuracy and computation time, enabling an initial accuracy/complexity tradeoff discussion.
- Provides a concrete bridge from a research metric to a systems consequence that can be tested in a sandbox.

## Weaknesses

- The evidence is concentrated in one measurement campaign, eight bands, and a small set of day/band settings.
- Raw data, code, exact preprocessing, parameter files, and repeatability details are not available in the inspected artifact set.
- No repeated-seed uncertainty, confidence intervals, calibration curves, class-balance analysis, or cross-location validation is reported.
- The temporal train/test split and threshold selection may make performance sensitive to drift and campaign-specific structure.
- The paper has no explicit separate conclusion section in the HTML, and the PDF/abstract page page-count metadata differs; these are provenance/format cautions rather than substantive errors.
- The SVM+FFA accuracy gain comes with a large computation-time increase in Table I, but energy and latency budgets are not analyzed.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish redacted or synthetic traces and preprocessing | Reproducibility | Exact inputs are needed to replay labels and splits | Independent reproduction | Privacy and licensing review | Hash datasets, publish schemas, replay Table I |
| Add repeated seeds and confidence intervals | Statistical validity | Point means hide instability | More credible ranking | More compute | Paired bootstrap or repeated temporal folds |
| Add cross-band and cross-location tests | Generalization | Current campaign may be narrow | Transfer evidence | New data collection | Hold out receivers, bands, and time periods |
| Report calibration and abstention | Safety | Accuracy does not express uncertainty | Safer operator decisions | Calibration data and monitoring | Reliability diagrams and protection-cost curves |
| Compare temporal and structure-aware baselines | Modeling | HMM and flat vectors may underuse structure | Better accuracy/complexity frontier | More implementation work | Fixed protocol against SVM+FFA and baselines |
| Normalize runtime and energy | Systems | Reported seconds lack hardware context | Deployment-relevant tradeoff | Instrumentation burden | Versioned hardware/software benchmark |

## Potential Implementations

1. **Benchmark pipeline**
   - `User`: Research teams and benchmark maintainers.
   - `Goal`: Reproduce classifier rankings on synthetic or authorized traces.
   - `Core mechanism`: Thresholded occupancy features, fixed temporal splits, version-pinned classifiers, calibration, and outage metrics.
   - `Required inputs`: Synthetic band matrices, thresholds, labels, split definitions, seeds, and model configurations.
   - `Outputs`: Metrics table, calibration plot, outage estimate, runtime record, and evidence ledger.
   - `Risk controls`: No live radio access; synthetic/default data; leakage tests; artifact hashes; reviewable configs.
   - `Evaluation`: Replay tests, cross-band holdouts, repeated seeds, and expected-value checks.

2. **Local operator monitor**
   - `User`: Authorized spectrum engineers.
   - `Goal`: Surface occupancy confidence and drift without exposing raw traces or issuing control commands.
   - `Core mechanism`: Local feature extraction, calibrated classifier, abstention policy, drift detector, and redacted summaries.
   - `Required inputs`: Authorized receiver summaries, calibration metadata, band map, and policy thresholds.
   - `Outputs`: Confidence dashboards, drift warnings, and review queues.
   - `Risk controls`: Local-only processing, role-based access, retention limits, no actuation API, and human review.
   - `Evaluation`: Shadow-mode replay, false-alarm and missed-occupancy costs, calibration checks, and incident drills.

3. **Simulation-gated allocation advisor**
   - `User`: Wireless planning and research teams.
   - `Goal`: Compare allocation proposals under predicted occupancy, sensing quality, power, and outage constraints.
   - `Core mechanism`: Classifier outputs feed a digital twin or hardware-in-the-loop evaluator that ranks proposals.
   - `Required inputs`: Versioned occupancy predictions, detector uncertainty, power budget, topology, and authorization policy.
   - `Outputs`: Ranked proposals, feasibility evidence, rollback plan, and unresolved conflicts.
   - `Risk controls`: No direct radio authority; sandbox first; approval gate; stale-data rejection; auditable provenance.
   - `Evaluation`: Synthetic scenarios, held-out traces, fault injection, and safety review.

4. **Privacy-preserving spectrum research dataset builder**
   - `User`: Academic or industrial research groups.
   - `Goal`: Create usable benchmark data without publishing sensitive site or user patterns.
   - `Core mechanism`: Aggregate, redact, synthesize, and hash traces while retaining evaluation-relevant occupancy structure.
   - `Required inputs`: Authorized measurements, privacy policy, retention rules, and a synthetic-data generator.
   - `Outputs`: Public schema, synthetic benchmark, privacy report, and provenance ledger.
   - `Risk controls`: Disclosure review, coarse geospatial/time resolution, access controls, and no raw-data export.
   - `Evaluation`: Utility/privacy tradeoff tests and attack-oriented re-identification review conducted only on synthetic or authorized data.

## Three Ways to Exercise This Research

1. **Synthetic classifier replay**: Generate multi-band binary occupancy matrices, reserve a chronological test segment, compare NBC/SVM/SVM+FFA-inspired tuning against a transparent baseline, and report accuracy, calibration, runtime, and stop when the protocol is stable across at least three seeds.
2. **Outage-oriented evaluation**: Feed predicted free/occupied sequences into the paper's consecutive-free-slot metric using synthetic data, compare outage error against accuracy, and stop before any interface capable of radio or network actuation is introduced.
3. **Structure and drift study**: Create synthetic periodic and non-periodic band patterns, hold out a changed pattern or receiver profile, compare flat-bin and temporal/structure-aware features, and stop if the experiment cannot distinguish representation gain from threshold leakage.

## Example MVP Product

- `Product name`: Spectrum Opportunity Sandbox
- `Target user`: Wireless research and planning teams working with synthetic or authorized receiver summaries.
- `Problem`: Classifier accuracy alone does not show whether a spectrum opportunity is safe, calibrated, computationally feasible, or useful for downstream outage decisions.
- `Core workflow`: Import a versioned synthetic/authorized summary; validate schema, band, threshold, and freshness; generate occupancy features; run pinned baseline classifiers; estimate outage; display uncertainty, runtime, drift, and a non-actionable review report.
- `Data requirements`: Synthetic default traces; optional authorized aggregate measurements; calibration metadata; band identifiers; threshold and split configuration; seed; model version; and retention classification.
- `Architecture`: Local ingestion and validation layer; feature/label builder; sandboxed model runner; calibration and outage evaluator; evidence-ledger writer; static report UI. No radio-control or external-network actuation component.
- `Success metrics`: Reproducible replay rate; calibration error; outage-estimation error; cross-pattern generalization; runtime per batch; privacy-review pass rate; and zero unauthorized-action paths.
- `Risk controls`: Synthetic-by-default inputs, local processing, role separation, stale-data rejection, explicit abstention, immutable configs, audit logs without raw traces, and human review.
- `Limitations`: It cannot establish real-world spectrum safety, replace regulatory analysis, infer current occupancy from unvalidated data, or reproduce the paper without its original campaign and code.
- `MVP boundary`: Benchmark and review only; no live sensing, transmission, allocation, or automated actuation.
- `Deployment model`: Local CLI/notebook or isolated internal service with offline artifacts.
- `Evaluation plan`: Unit tests for feature/label transformations; seeded synthetic replay; calibration and outage checks; leakage tests; privacy review; and adversarial stale-input cases.
- `Failure modes`: Threshold leakage, drift, class imbalance, stale calibration, misread band metadata, overconfident predictions, and users mistaking a proposal for authorization.
- `Maintenance plan`: Version model/config dictionaries, refresh synthetic scenarios, review thresholds and calibration, monitor dependency changes, and require a safety review before any scope expansion.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| 2D-RC: Two-Dimensional Neural Network Approach for OTFS Symbol Detection | Related Black Lake manuscript | Structure-aware wireless ML and online learning under channel geometry | `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md` |
| Joint Optimization of Sensing and Computation for Status Update in Mobile Edge Computing Systems | Related Black Lake manuscript | Sensing validity, sampling, transmission, freshness, and energy tradeoffs | `.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/joint_sensing_mec_manuscript.md` |
| Multi-Point Integrated Sensing and Communication: Fusion Model and Functionality Selection | Related Black Lake manuscript | Joint sensing/communication allocation, detector quality, and power constraints | `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md` |
| Machine learning-based spectrum occupancy prediction: a comprehensive survey | Later survey context | Broader spectrum-occupancy prediction landscape; not used to validate the selected paper's metrics | https://www.frontiersin.org/journals/communications-and-networks/articles/10.3389/frcmn.2025.1482698/full |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| S1 | https://arxiv.org/abs/1503.07104 | Metadata, abstract, authors, date, subjects, version, and DOI | 2026-08-20 | Primary metadata page; abstract-only evidence not used for detailed results |
| S2 | https://arxiv.org/html/1503.07104 | Full text, method, data, algorithms, figures/captions, results, Table I, and references | 2026-08-20 | Full-paper HTML inspected locally; local copy withheld |
| S3 | https://arxiv.org/pdf/1503.07104 | PDF identity, integrity, page/text cross-check | 2026-08-20 | Local PDF verified and withheld |
| S4 | https://doi.org/10.48550/arXiv.1503.07104 | Persistent arXiv-issued DOI | 2026-08-20 | Identifier locator |
| S5 | https://doi.org/10.1109/TVT.2015.2487047 | Journal publication identity | 2026-08-20 | Journal DOI locator |
| S6 | https://dblp.org/rec/journals/tvt/AzmatCS16.html | Authors, journal, volume, issue, pages, year, DOI | 2026-08-20 | Independent bibliographic cross-check |
| S7 | https://www.frontiersin.org/journals/communications-and-networks/articles/10.3389/frcmn.2025.1482698/full | Later survey context and related vocabulary | 2026-08-20 | Context only; not independent validation |
| S8 | `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md` | Related wireless ML bridge | 2026-08-20 | Repository-relative path; public generated artifact |
| S9 | `.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/joint_sensing_mec_manuscript.md` | Related sensing/resource bridge | 2026-08-20 | Repository-relative path; public generated artifact |
| S10 | `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md` | Related joint sensing/communication bridge | 2026-08-20 | Repository-relative path; public generated artifact |
| S11 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Output repository rules and source-withholding policy | 2026-08-20 | Live README read before writing |
| S12 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository DEP and attribution context | 2026-08-20 | Live README read before writing |

## Appendix

### Source-Integrity and Dedup Validation

| Check | Result |
|---|---|
| PDF size | 422,127 bytes; above the 10 KB threshold |
| PDF signature | Begins with `%PDF-1.4` |
| PDF trailer | Contains trailing `%%EOF` |
| Full-paper HTML size | 223,505 bytes; above the 5 KB threshold |
| HTML body | 45,083 characters after removing scripts/styles |
| HTML document markers | `article`, `main`, `ltx_document`, and `ltx_page_main` present |
| HTML headings | 71 section/heading markers |
| Paper-structure terms | Six classes found: Introduction, Methods/Method, Results, Discussion, References |
| Partial files | Zero `.part` files |
| Selection | Uniform sorted-unit draw, index 10,451 of 75,964 units |
| Dedup | 0 matches by arXiv ID, DOI, normalized title, slug, prior artifact, memory, or 24-hour marker |
| Reselection | 0 reselections; first draw retained after repair |
| Public source upload | None; no `.source/` directory |

### Review Boundary

The local source unit was complete before review after one bounded repair. The source package was unavailable through the brokered redirect policy. The public artifact records the result without revealing local absolute paths, usernames, machine names, local timezone labels, exact local execution timestamps, or source-file contents.

## Attribution Block

- Source URL: https://arxiv.org/abs/1503.07104
  - Applies to: this manuscript.
  - Notes: Primary metadata, abstract, authors, date, subject, version, and identifier.
- Source URL: https://arxiv.org/html/1503.07104
  - Applies to: this manuscript.
  - Notes: Full-paper method, data, algorithms, results, figures/captions, table values, and references; local copy withheld.
- Source URL: https://arxiv.org/pdf/1503.07104
  - Applies to: this manuscript.
  - Notes: Primary PDF inspected for integrity and cross-checked; local copy withheld.
- Source URL: https://doi.org/10.48550/arXiv.1503.07104
  - Applies to: this manuscript.
  - Notes: Persistent arXiv-issued DOI.
- Source URL: https://doi.org/10.1109/TVT.2015.2487047
  - Applies to: this manuscript.
  - Notes: Journal publication locator.
- Source URL: https://dblp.org/rec/journals/tvt/AzmatCS16.html
  - Applies to: this manuscript.
  - Notes: Independent bibliographic cross-check.
- Source URL: https://www.frontiersin.org/journals/communications-and-networks/articles/10.3389/frcmn.2025.1482698/full
  - Applies to: `Related Research and Reading`.
  - Notes: Later survey context only; not validation evidence for the selected paper's results.
- Repository file: `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md`
  - Applies to: related research, evidence ledger, and synthesis.
  - Notes: Conceptual bridge; not independent validation.
- Repository file: `.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/joint_sensing_mec_manuscript.md`
  - Applies to: related research, evidence ledger, and synthesis.
  - Notes: Conceptual bridge; not independent validation.
- Repository file: `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md`
  - Applies to: related research, evidence ledger, and synthesis.
  - Notes: Conceptual bridge; not independent validation.
- Source-file policy: original PDF, full-paper HTML, metadata HTML, acquisition receipts, caches, extracted text, and unavailable source package remain local.
  - Applies to: the entire manuscript.
  - Notes: No source file was uploaded, staged, committed, copied, or attached; no public `.source/` directory was created.
