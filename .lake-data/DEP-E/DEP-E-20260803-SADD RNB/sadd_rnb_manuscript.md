---
title: "SADD RNB - DEP-E"
generated_at: "2026-08-03 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of semi-supervised adaptive discretization integrated with regularized Naive Bayes."
source_status: "verified complete local PDF, approved full-paper HTML fallback, and metadata HTML inspected; source files withheld locally"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-03"
temporal_cutoff: "Public paper and repository evidence inspected through 2026-08-03."
primary_url: "https://arxiv.org/abs/2111.10983"
stable_identifier: "arXiv:2111.10983v3; arXiv DOI:10.48550/arXiv.2111.10983; journal DOI:10.1016/j.eswa.2023.120094"
confidence_summary: "High for source identity, method transcription, and reported tables; medium for protocol interpretation and generalization; low for independent reproducibility."
safety_scope: "public-data, offline, defensive, and reproducibility-oriented research only"
distribution_notes: "Only derived Markdown is public. PDFs, HTML, source packages, caches, extracted text, and verification records remain local."
---

# SADD RNB - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public URL or Local Status | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:2111.10983v3 | https://arxiv.org/abs/2111.10983 | Metadata page; not full-paper evidence | 2026-08-03 | Inspected |
| S2 | arXiv PDF | Primary paper | PDF | arXiv:2111.10983v3 | https://arxiv.org/pdf/2111.10983 | Local copy withheld; not redistributed | 2026-08-03 | Integrity passed and inspected |
| S3 | Approved full-paper rendering | Primary paper | HTML | arXiv:2111.10983v3 | https://ar5iv.labs.arxiv.org/html/2111.10983 | Local fallback copy withheld; not redistributed | 2026-08-03 | Integrity passed and inspected |
| S4 | Expert Systems with Applications record | Publisher context | HTML | DOI:10.1016/j.eswa.2023.120094 | https://www.sciencedirect.com/science/article/pii/S0957417423005961 | Public publisher record | 2026-08-03 | Inspected via public record |
| S5 | arXiv-linked license deed | Usage context | License | CC BY-NC-ND 4.0 | https://creativecommons.org/licenses/by-nc-nd/4.0/ | Attribution, noncommercial, and no-derivatives terms summarized by deed | 2026-08-03 | Recorded |
| S6 | Decentralized SSL DEP | Related synthesis | Markdown | DEP-E-20260720 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260720-Decentralized%20SSL/decentralized_ssl_manuscript.md | Related artifact, not primary validation | 2026-08-03 | Live file inspected |
| S7 | Adversarial Label Noise DEP | Related synthesis | Markdown | DEP-E-20260716 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260716-Adversarial%20Label%20Noise/adversarial_label_noise_manuscript.md | Related artifact, not primary validation | 2026-08-03 | Live file inspected |
| S8 | DUET Setwise CTR DEP | Related synthesis | Markdown | DEP-E-20260719 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260719-DUET%20Setwise%20CTR/duet_setwise_ctr_manuscript.md | Related artifact, not primary validation | 2026-08-03 | Live file inspected |
| S9 | Black Lake repository README and .lake-data README | Process authority | Markdown | main | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Filing and public-source rules | 2026-08-03 | Fetched and read |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Title, authors, v1/v3 dates, categories, abstract, arXiv and journal DOI links | Identity, dates, high-level contribution | High | Abstract is not sufficient for empirical claims |
| E2 | S2 and S3, sections 1-3 | Primary full paper | MDLP problem, pseudo-labeling, adaptive threshold, RNB+ mechanism, complexity, figures and algorithm narrative | Method and mechanism | High for transcription | No independent re-derivation or execution |
| E3 | S2 and S3, sections 4.1-4.5, Tables 3-10 | Primary full paper | 31 UCI datasets, preprocessing, stratified 10-fold protocol, accuracies, gains, significance counts, semi-supervised split | Empirical results | High for transcription | Source-reported; no rerun; multiple-testing and protocol-scope caveats |
| E4 | S4 | Publisher record | Journal, date, DOI, highlights, and corroborating 31-dataset summary | Publication context | High | Full publisher content was not independently downloaded |
| E5 | S5 | License deed | CC BY-NC-ND terms linked from arXiv | Distribution caution | Medium | Legal interpretation requires the full license text |
| E6 | S6-S8 | Related DEP manuscripts | Unlabeled-data handling, soft targets, disagreement, privacy, and deployment gates | Cross-paper synthesis | Medium | Related artifacts are not independent validation of SADD |
| E7 | S9 | Repository rules | DEP-E filing, public attribution, no-source-upload, and publication-index requirements | Artifact governance | High | Process evidence only |

## Executive Summary

The paper proposes Semi-supervised Adaptive Discriminative Discretization (SADD) to address a practical tension in Naive Bayes: coarse bins improve likelihood estimation but can erase class-discriminative information. SADD first creates pseudo-labels for unlabeled examples with k-nearest neighbors, then lowers the MDLP split barrier through a sample-size-dependent sigmoid threshold. The resulting interval map is integrated with regularized Naive Bayes as RNB+.

The source reports 31 UCI benchmark datasets, stratified 10-fold cross-validation, and 82.07 mean accuracy for SADD versus 78.96 for MDLP in the main comparison. In the paper’s 40%-labeled semi-supervised setting, SADD averages 80.83 versus 77.28 for MDLP. These are credible source-reported results with high transcription confidence, but not independently reproduced. The most important boundary is protocol semantics: the method narrative explicitly derives a discretization scheme using unlabeled testing covariates, so the reported advantage must be labeled transductive unless a strict-inductive reimplementation confirms otherwise.

## Detailed Summary

### Problem Context

Naive Bayes is attractive for compact and efficient classification, but numeric features with many distinct values can produce unreliable likelihood estimates. Discretization groups values into intervals so that class-conditional frequencies have more support. Coarse discretization, however, can merge values that separate classes. The paper identifies early stopping in MDLP as a source of this information loss and seeks a balance between discrimination and generalization.

### Method

SADD has three main elements:

1. A k-nearest-neighbor classifier with Euclidean distance generates pseudo-labels for unlabeled examples. The paper tunes k by grid search on one of nine training folds used as validation.
2. A recursive, greedy, per-attribute split procedure selects the cut point with maximum information gain. MDLP’s threshold is modified to theta-tilde = sigmoid(N/N0) times theta, with N0 set empirically to 2000. This lowers the threshold especially for small sample counts without reducing it to zero.
3. The discretized attributes are passed into regularized Naive Bayes. The integrated classifier is named RNB+, and the regularized attribute-weighting design is intended to preserve the discrimination/generalization trade-off after discretization.

The paper reports O(m n log n) time for m attributes and n samples. Its main framework description says that unlabeled testing samples can participate in pseudo-labeling and discretization. That is a transductive design choice, not automatically a defect, but it changes the evaluation claim and must be reported separately from a training-only production pipeline.

### Experimental Design

The paper compares SADD against MDLP, CAIM, CACC, ChiMerge, Equal-Width, Equal-Frequency, PKID, and FFD, then compares RNB+ and SADD-augmented versions of other Naive Bayes classifiers. The benchmark comprises 31 UCI datasets with mixed numeric/categorical features, 150 to 21,048 instances in the displayed dataset inventory, 4 to 520 attributes, and some missing values imputed by numerical means or categorical modes.

Accuracy is evaluated with stratified 10-fold cross-validation. One of nine training folds is used as a validation set for k selection. The paper reports one-tailed t-tests at p = 0.05 and mean plus/minus standard-deviation values in its tables. A separate semi-supervised experiment labels 40% of training samples and treats the remainder as unlabeled.

### Results

In the main discretization comparison, the paper reports mean accuracies of 82.07 for SADD, 78.96 for MDLP, 79.27 for CAIM, 79.07 for CACC, 76.58 for ChiMerge, 78.81 for Equal-Width, 77.86 for Equal-Frequency, 78.58 for PKID, and 78.10 for FFD. The source describes the SADD-minus-MDLP average difference as 3.11 percentage points. SADD outperforms MDLP on all 31 datasets, with 19 of those gains marked statistically significant.

In the semi-supervised comparison, the source reports mean accuracies of 80.83 for SADD and 77.28 for MDLP, with CAIM at 79.30, CACC at 78.59, and ChiMerge at 75.93. In the RNB-family comparison, the table reports 82.73 for RNB and 84.89 for RNB+, a 2.16-point difference. The largest displayed SADD-over-MDLP gains include Bupa at 12.49 points, Movement at 15.67 points, and Vowel at 16.67 points.

### Limitations and Reproducibility

The paper does not establish that pseudo-labels are correct; it uses them as a structural signal for partitioning. The main description’s use of unlabeled test covariates makes strict inductive comparison an open validation task. The evaluation is broad within UCI but does not establish performance on modern tabular suites, distribution shift, calibration, fairness, class imbalance, memory, latency, or energy. A one-tailed p = 0.05 test across many datasets and comparisons also warrants a multiple-comparison and dataset-dependence audit. The inspected public sources describe MATLAB and KEEL components but do not establish a complete official code/configuration release.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | SADD lowers the MDLP split threshold adaptively to retain more discriminative intervals. | Author method claim | E2, sections 3.1-3.3 and threshold equations | Directly supported by the full-paper method description. | High |
| C2 | SADD averages 82.07 versus 78.96 for MDLP in the main 31-dataset comparison. | Author empirical result | E3, Table 4 | Table-backed source report; not independently reproduced. | High for transcription |
| C3 | SADD averages 80.83 versus 77.28 for MDLP when 40% of training samples are labeled. | Author empirical result | E3, Table 7 | Table-backed source report; protocol is distinct from the main comparison. | High for transcription |
| C4 | SADD retains more discriminative information than MDLP on datasets where MDLP collapses features into one interval. | Author interpretation | E3, Table 6 and section 4.3 | Plausible mechanism supported by interval-count and gain tables. | Medium-high |
| C5 | The reported main-framework advantage is directly portable to strict-inductive deployment. | Reviewer interpretation | E2-E3 | Not established because the framework describes using unlabeled testing covariates. | Low |
| C6 | RNB+ improves the listed regularized Naive Bayes result from 82.73 to 84.89. | Author empirical result | E3, Table 9 | Direct table transcription; no independent reproduction. | High for transcription |

## Methodology

- Research objective: preserve and assess the paper’s SADD/RNB+ contribution, reported evidence, protocol boundaries, limitations, and safe implementation implications.
- Sources inspected: local valid PDF, repaired full-paper HTML fallback, arXiv metadata page, publisher record, arXiv-linked license deed, live Black Lake README files, and exactly three live related DEP manuscripts.
- Discovery strategy: enumerate local PDF candidates with rg, group unique parent directories, draw a uniform random index, scan public and private dedup evidence, inspect local source metadata, and inspect public primary-source pages.
- Inclusion criteria: first-drawn paper unit with a valid identity and no prior Arxiv DEP artifact, followed by a successful PDF/full-paper HTML source gate.
- Exclusion criteria: duplicate or recent paper markers, invalid or abstract-only source units, incomplete PDF/HTML, and public source-file publication.
- Analytical approach: empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication-oriented review.
- Evidence handling: assign evidence IDs, tie claims to source sections or tables, distinguish author claims from reviewer interpretations, and preserve uncertainty where results were not reproduced.
- Uncertainty handling: mark transductive scope, pseudo-label reliability, multiple-testing concerns, unavailable code, and source-package unavailability explicitly.
- Source-integrity method: the first unit state was partial because full-paper HTML was absent. One bounded broker-mediated repair added metadata/full-paper HTML; final PDF and HTML thresholds passed. The optional source package remained local-only/unavailable.
- Selection and dedup validation: 75,960 PDFs, 75,957 unique parent units, uniform index 54,225, zero duplicate exclusions, zero other identity exclusions, zero reselections, and no same-paper 24-hour marker.

## Scope, Constraints, and Assumptions

- Scope: the SADD/RNB+ method, source-reported evaluation, protocol semantics, reproducibility, related DEP synthesis, and bounded implementation planning.
- Temporal boundary: public evidence inspected through 2026-08-03; reviewed arXiv version is v3, revised 2023-04-05.
- Evidence limits: no independent code execution, no source-package inspection because it was unavailable through the broker redirect policy, no dataset download, and no rerun of the 31-dataset tables.
- Assumptions: the publisher record corresponds to the reviewed arXiv work; the reported plus/minus values are accuracy summaries over the stated folds; the public full-paper fallback faithfully renders the reviewed paper.
- Constraints: source files remain local; public artifacts must be safe for redistribution; implementation examples use synthetic or offline inputs; no production or high-impact classification decision is authorized by this review.
- Out of scope: legal clearance for source redistribution, clinical or financial deployment, claims of universal tabular superiority, and independent significance-test reanalysis.
- Intended use: DEP deposition, research triage, reproducibility planning, safe MVP ideation, and future strict-inductive validation.
- Audience: tabular-ML researchers, ML platform engineers, benchmark maintainers, and model-risk reviewers.
- Reproducibility boundary: a reviewer can retrieve the cited public sources and reconstruct the conceptual protocol, but cannot reproduce the paper’s complete tables from this artifact alone.

## Observations

- Observed pattern: the largest source-reported gains occur on datasets where MDLP assigns many attributes to one interval, supporting the paper’s information-loss explanation.
- Technical implication: a discretizer should expose cut-point count, bin support, and training-versus-unlabeled provenance as first-class metrics.
- Contradiction or tension: the paper frames pseudo-labeling as semi-supervised but its main figure describes unlabeled testing samples; that is transductive and should not be silently compared with training-only pipelines.
- Reviewer hypothesis: SADD’s strongest benefit may be concentrated on small or high-dimensional tables where MDLP’s threshold is most likely to stop early.
- Open question: confidence-gated pseudo-labeling may reduce harmful boundary changes while also removing the unlabeled-data signal that makes SADD useful.

## Considerations

- Adoption: a team must choose transductive or inductive semantics before comparing results.
- Statistical validity: dataset-level dependence, repeated tuning, one-tailed tests, and multiple comparisons need an explicit analysis plan.
- Data governance: pseudo-labeling and unlabeled covariates can encode sensitive population structure; use purpose limitation, retention limits, and aggregate audit logs.
- Operations: interval maps are versioned preprocessing artifacts. Drift in feature distributions or missingness can invalidate them before the classifier’s weights visibly fail.
- Fairness and calibration: accuracy averages can hide minority-class or probability-quality regressions; report class-wise recall, log loss, expected calibration error, and abstention.
- Cost: the stated O(m n log n) complexity does not replace measurements of fitting time, inference time, memory, and retraining cost.

## Strengths

- Targets a concrete and interpretable failure mode in a widely used classifier family.
- Uses a clear algorithmic control knob rather than an opaque end-to-end model.
- Evaluates across 31 public datasets, multiple discretization families, and multiple Naive Bayes weightings.
- Includes interval-count analysis that connects accuracy changes to a proposed mechanism.
- Provides an explicit semi-supervised setting rather than presenting unlabeled data only as motivation.

## Weaknesses

- The transductive use of unlabeled testing covariates complicates strict-inductive interpretation.
- Pseudo-label error, confidence, and class-imbalance effects are not fully audited.
- Public evidence does not establish a complete code/configuration/seed release for reproduction.
- UCI accuracy averages do not cover calibration, drift, fairness, compute, or modern tabular tasks.
- The statistical-testing presentation does not visibly resolve multiple-comparison or dataset-dependence concerns.
- Mean/mode imputation and heterogeneous benchmark preprocessing can influence results independently of the discretizer.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost or Risk | Validation Approach |
|---|---|---|---|---|---|
| Add strict-inductive and transductive arms | Protocol | Separate information access from algorithmic gain | Clearer claim boundary | Two pipelines and matched folds | Reproduce Tables 4 and 7 under both arms |
| Add confidence gating and abstention | Pseudo-labeling | Reduce propagation of weak kNN labels | Better calibration and minority robustness | Fewer usable unlabeled rows | Sweep thresholds and report coverage-risk curves |
| Use corrected hierarchical statistical analysis | Inference | Control dataset dependence and many comparisons | More defensible uncertainty | More complex analysis | Report paired fold deltas, correction, and effect sizes |
| Expand benchmark and metrics | Generalization | UCI accuracy is narrow | Better deployment relevance | Dataset and compute cost | Modern public tabular suite with log loss, ECE, latency, memory |
| Release exact preprocessing and code | Reproducibility | MATLAB/KEEL descriptions are not a complete executable spec | Independent validation | Packaging and maintenance | Rebuild every displayed table from a pinned environment |

## Potential Implementations

1. Leakage-aware SADD benchmark: an offline evaluator that fits pseudo-labeling and cut points inside folds, labels results as transductive or inductive, and reports accuracy, calibration, bin counts, and compute.
2. Confidence-gated tabular classifier: a local preprocessing service that freezes schema and interval maps, rejects unsupported bins, logs aggregate pseudo-label confidence, and emits an abstain signal for uncertain rows.
3. Drift-aware interval registry: a versioned registry that tracks cut-point changes, bin occupancy, missingness, calibration, and rollback decisions without storing raw records.

## Three Ways to Exercise This Research

1. Strict-inductive reproduction: use public tabular data, fixed folds, training-only cut points, and a baseline MDLP implementation. Output paired fold metrics and a success criterion of confirming, narrowing, or rejecting the reported SADD advantage. Stop if preprocessing touches held-out labels or unapproved data.
2. Synthetic threshold stress test: generate labeled and unlabeled numeric features with controlled class overlap, compare MDLP and SADD across sample sizes, and measure bin count, accuracy, log loss, and calibration. Stop when the synthetic distribution no longer matches the stated hypothesis.
3. Drift and confidence audit: replay a public dataset with controlled covariate shift, vary pseudo-label confidence thresholds, and output coverage-risk and retraining curves. Stop before using private or high-impact records.

## Example MVP Product

- Product name: IntervalGuard Tabular Review.
- Target user: an ML platform or model-risk team evaluating compact Naive Bayes classifiers.
- Problem: discretization changes can silently trade likelihood stability for lost discrimination, especially when unlabeled data enters the preprocessing path.
- Core workflow: register a schema; fit an explicitly labeled inductive or transductive preprocessing policy; produce interval maps; run fold-isolated benchmark and calibration checks; monitor drift; emit a promotion or rollback receipt.
- Data requirements: public or authorized tabular data, labels for evaluation, schema and missingness definitions, fixed folds, and aggregate telemetry.
- Architecture: local preprocessing runner, immutable fold manifest, SADD/MDLP/RNB baselines, calibration module, drift monitor, signed Markdown/JSON receipt, and human approval gate.
- Success metrics: paired accuracy delta, log-loss delta, expected calibration error, minority-class recall, bin-support violations, p95 transform latency, and reproducibility of displayed table rows.
- Risk controls: no raw-row logging, training-only data for inductive mode, explicit transductive labels, privacy review, minimum-bin support, abstention, version pinning, and rollback.
- Limitations: the MVP does not prove broad superiority, does not reproduce the paper’s full implementation without source code/configuration, and does not authorize high-impact automated decisions.

## Related Research and Reading

| Item | Type | Relevance | URL or Identifier |
|---|---|---|---|
| Fayyad and Irani, Multi-interval discretization of continuous-valued attributes for classification learning | Direct baseline | MDLP threshold and early-stopping context | Cited as the MDLP baseline in the primary paper |
| Bondu, Boullé, and Lemaire, A non-parametric semi-supervised discretization method | Methodological neighbor | Semi-supervised discretization without collapsing unlabeled structure into a generic pseudo-label claim | Cited in the primary paper |
| UCI Machine Learning Repository | Benchmark source | The paper’s 31-dataset evaluation base | https://archive.ics.uci.edu/ |
| Decentralized SSL DEP-E | Related Black Lake artifact | Unlabeled data, representation exchange, privacy and systems boundaries | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260720-Decentralized%20SSL/decentralized_ssl_manuscript.md |
| Adversarial Label Noise DEP-E | Related Black Lake artifact | Soft targets, target mismatch, calibration, and uncertainty | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260716-Adversarial%20Label%20Noise/adversarial_label_noise_manuscript.md |
| DUET Setwise CTR DEP-E | Related Black Lake artifact | Peer pseudo-labels, correlated error, disagreement telemetry, and release gates | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260719-DUET%20Setwise%20CTR/duet_setwise_ctr_manuscript.md |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2111.10983 | Identity, authors, version dates, abstract, DOI links | 2026-08-03 | Metadata only |
| R2 | https://arxiv.org/pdf/2111.10983 | PDF integrity and primary paper | 2026-08-03 | Local copy inspected; not uploaded |
| R3 | https://ar5iv.labs.arxiv.org/html/2111.10983 | Full methods, equations, tables, experiments, conclusion, and references | 2026-08-03 | Local fallback inspected; not uploaded |
| R4 | https://www.sciencedirect.com/science/article/pii/S0957417423005961 | Journal record, DOI, date, highlights, abstract, and publisher context | 2026-08-03 | Public publisher record |
| R5 | https://doi.org/10.1016/j.eswa.2023.120094 | Stable journal identifier | 2026-08-03 | DOI locator |
| R6 | https://creativecommons.org/licenses/by-nc-nd/4.0/ | License deed linked from arXiv | 2026-08-03 | Distribution caution |
| R7 | https://archive.ics.uci.edu/ | Benchmark repository context | 2026-08-03 | The paper identifies UCI as the dataset source |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260720-Decentralized%20SSL/decentralized_ssl_manuscript.md | Related synthesis | 2026-08-03 | Live file inspected |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260716-Adversarial%20Label%20Noise/adversarial_label_noise_manuscript.md | Related synthesis | 2026-08-03 | Live file inspected |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260719-DUET%20Setwise%20CTR/duet_setwise_ctr_manuscript.md | Related synthesis | 2026-08-03 | Live file inspected |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository filing and source-locality rules | 2026-08-03 | Live README read before writing |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E naming, publication index, and attribution requirements | 2026-08-03 | Live README read before writing |

## Appendix

### Selection and Deduplication Validation

- PDF enumeration used rg --files -g "*.pdf".
- Candidate count: 75,960 PDFs; 75,957 unique parent units.
- Uniform draw: zero-based index 54,225 from the sorted unique units.
- Dedup result: first draw accepted; zero duplicate exclusions, zero other identity exclusions, zero reselections, and no same-paper 24-hour marker.
- Keys checked: arXiv ID and base ID, DOI, normalized title, slug, prior logs/reports/DEP-E artifacts, automation memory, and relevant Black Lake-Data entries.

### Source-Integrity Validation

- Initial state: partial because full-paper HTML was missing although the existing PDF was valid.
- Repair: one bounded broker-mediated attempt; official arXiv HTML routes returned 404 and the approved ar5iv fallback was saved.
- Final PDF: 782,656 bytes, %PDF- header, trailing %%EOF.
- Final HTML: 703,223 bytes, 82,918 body characters after removing scripts/styles, document marker present, 53 heading markers, and 7 paper-structure terms.
- Source package: unavailable through redirect policy.
- Local metadata, provenance, machine-readable summary, verification report, and acquisition receipt were updated.
- Public locality: no source document, cache, extraction, or verification file is included; no .source directory is created.

### Reviewer Notes

The publisher record and arXiv record agree on the paper identity and high-level contribution. The full-paper source adds the decisive method and table evidence. The review does not treat the reported accuracy gains as general deployment guarantees, and it keeps the transductive protocol question visible for future reproduction.

## Attribution Block

- Source URL: https://arxiv.org/abs/2111.10983
  - Applies to: this manuscript.
  - Notes: Public metadata and citation; source files withheld locally.
- Source URL: https://arxiv.org/pdf/2111.10983
  - Applies to: this manuscript.
  - Notes: Local PDF inspected; not uploaded.
- Source URL: https://ar5iv.labs.arxiv.org/html/2111.10983
  - Applies to: this manuscript.
  - Notes: Local full-paper HTML fallback inspected; not uploaded.
- Source URL: https://www.sciencedirect.com/science/article/pii/S0957417423005961
  - Applies to: publication context and corroborating abstract.
  - Notes: Publisher record.
- Source URL: https://creativecommons.org/licenses/by-nc-nd/4.0/
  - Applies to: distribution note.
  - Notes: License deed linked from arXiv.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260720-Decentralized%20SSL/decentralized_ssl_manuscript.md
  - Applies to: related research synthesis.
  - Notes: Live related DEP inspected.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260716-Adversarial%20Label%20Noise/adversarial_label_noise_manuscript.md
  - Applies to: related research synthesis.
  - Notes: Live related DEP inspected.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260719-DUET%20Setwise%20CTR/duet_setwise_ctr_manuscript.md
  - Applies to: related research synthesis.
  - Notes: Live related DEP inspected.
