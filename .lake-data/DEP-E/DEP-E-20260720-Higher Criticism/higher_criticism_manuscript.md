---
title: "Higher Criticism Tests - DEP-E"
generated_at: "2026-07-20 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "A source-grounded review of higher-criticism and Berk-Jones global tests for sparse mixtures."
source_status: "verified complete local PDF, fallback full-paper HTML, and metadata HTML inspected; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-20"
temporal_cutoff: "Sources and repository context inspected through the batch invocation."
primary_url: "https://arxiv.org/abs/1411.1437"
stable_identifier: "arXiv:1411.1437v3; DOI:10.1214/15-AOS1312"
deployment_job_id: "BLAD-2200-20260720-8636EDC7"
deployment_item_id: "BLAD-2200-20260720-8636EDC7-P01"
confidence_summary: "High for identity and source-reported method/results; medium for transfer beyond the simulated regimes; low for dependent or misspecified p-values."
safety_scope: "offline statistical evaluation, multiplicity control, simulation validation, and human-reviewed scientific decisions"
distribution_notes: "No PDF, HTML, repair record, extracted text, cache, code, or local path is redistributed."
---

# Higher Criticism Tests - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Canonical arXiv record | Metadata | HTML | arXiv:1411.1437v3 | https://arxiv.org/abs/1411.1437 | Metadata only; not full-paper evidence. | 2026-07-20 | Inspected. |
| S2 | Full-paper rendering | Primary paper | HTML | arXiv:1411.1437v3 | https://ar5iv.labs.arxiv.org/html/1411.1437 | Verified fallback local copy withheld. | 2026-07-20 | Inspected in full. |
| S3 | Paper PDF | Primary paper | PDF | arXiv:1411.1437v3 | https://arxiv.org/pdf/1411.1437 | Verified local copy withheld. | 2026-07-20 | Integrity checked and cross-read. |
| S4 | Journal DOI | Publication identity | DOI | 10.1214/15-AOS1312 | https://doi.org/10.1214/15-AOS1312 | Persistent journal locator. | 2026-07-20 | Resolved through arXiv metadata. |
| S5 | PAC Confidence DEP | Related | Markdown | DEP-E-20260713 | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Related synthesis only. | 2026-07-20 | Inspected. |
| S6 | Kernel Equivalence DEP | Related | Markdown | DEP-E-20260719 | `.lake-data/DEP-E/DEP-E-20260719-Kernel Equivalence/kernel_equivalence_manuscript.md` | Related synthesis only. | 2026-07-20 | Inspected. |
| S7 | Noisy Poisson Inference DEP | Related | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-Noisy Poisson Inference/noisy_poisson_inference_manuscript.md` | Related synthesis only. | 2026-07-20 | Inspected. |
| S8 | Selection, repair, and integrity | Process evidence | Private records | `BLAD-2200-20260720-8636EDC7-P01` | Local path withheld | Randomness, dedup, integrity, and locality only. | 2026-07-20 | Verified. |

Authors: Jian Li and David Siegmund. Submitted 2014-11-05; v3 revised 2015-06-03; published in *Annals of Statistics* 43(3), 1323-1350. Deployment job `BLAD-2200-20260720-8636EDC7`; item `BLAD-2200-20260720-8636EDC7-P01`.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4 | Metadata | Identity, version, dates, journal and DOI links. | Canonical record. | High | No result validation. |
| E2 | S2, S3 | Complete paper | Definitions, approximations, proofs, simulation designs, tables, applications, discussion. | Method and reported findings. | High for transcription | No independent proof or numerical reproduction. |
| E3 | S2 Section 2, Table 1 | Primary paper | Approximate tail probabilities compared with simulations. | Practical significance calibration. | High for source report | Selected sample sizes and thresholds. |
| E4 | S2 Section 3, Table 2 | Primary paper | Sparse Gaussian-mixture power under varied prevalence/effect. | Statistic trade-offs. | High for source report | Mainly independent Gaussian mixtures. |
| E5 | S2 Section 4, Tables 3-6 | Primary paper | Lower confidence bounds and interval-scan experiments. | Application behavior. | High for source report | Synthetic or model-dependent evidence. |
| E6 | S5-S7 | Related DEP evidence | Confidence, hypothesis direction, misspecification, Type-I calibration. | Cross-DEP synthesis. | Medium | Different statistical objects and domains. |
| E7 | S8 | Private process evidence | Uniform reselection, dedup, bounded repair, integrity, source locality. | Deployment validity. | High | Paths and exact timestamps withheld. |

## Executive Summary

Li and Siegmund study global tests that detect an excess of small $p$-values when only a sparse fraction of hypotheses is false. They derive accurate significance approximations for original and modified higher criticism and for original and modified Berk-Jones statistics, compare those approximations with simulation, and examine power, lower confidence bounds on the number of false hypotheses, and interval detection.

The source does not support a universal winner. Original higher criticism can be strongest for extremely rare mixtures at ordinary significance levels, but its threshold rises sharply as the significance budget becomes stringent. Berk-Jones variants generally perform better across broader prevalence regimes and in large multiple-comparison problems. Confidence is high in this transcription of the complete paper and medium in transfer beyond independent, calibrated $p$-values and the studied models.

## Detailed Summary

### Problem and Vocabulary

Under the global null, ordered $p$-values should behave like uniform order statistics. Higher criticism standardizes the difference between an observed order statistic and its null expectation; Berk-Jones uses a likelihood-ratio-style divergence. Each statistic scans a range of order indices and rejects when the observed boundary crossing is sufficiently extreme. The minimum index matters: allowing the first order statistic increases sensitivity to extremely rare signals but also increases threshold instability.

### Approximation Mechanism

The paper translates each statistic's rejection event into crossing a curved boundary by uniform order statistics. Its analytic approximation decomposes the crossing probability by the last crossing location and combines binomial probabilities with a derivative correction. The authors give detailed proofs for original higher criticism and modified Berk-Jones, with extensions for the other variants.

### Significance Validation

Table 1 compares the analytic approximations with Monte Carlo values over several sample sizes and tail probabilities. The discussion finds classical Darling-Erdos approximations slow to converge and especially problematic for original higher criticism in the small-$p$ tail. This explains why finite-sample calibration cannot be inferred from asymptotic consistency alone.

### Power

The power analysis uses Gaussian mixtures and a transformed uniform-order-statistic problem. A hybrid calculation combines the analytic approximation for later order statistics with Noe's recursion for early ones. For $n=1000$ and significance 0.01, analytic and 10,000-run simulation values agree to two significant figures: HC versus MBJ is 0.68 versus 0.90 at $(\delta,p)=(2.5,0.02)$ and 0.89 versus 0.87 at $(4,0.005)$. Broader simulations show the HC advantage is concentrated at extremely small nonnull fractions; Berk-Jones variants dominate across much of the remaining range and at very small significance levels.

### Applications

For lower confidence bounds on the number of false nulls, modified HC and MBJ trade places as signal strength and prevalence change. The interval-scan study mimics copy-number variation with synthetic data and a large family of candidate intervals. At global level 0.05, the reported simulated/analytic thresholds are 20.0/21.5 for HC, 9.3/9.1 for MHC, and 5.98/5.98 for MBJ. The source warns that approximation quality may not persist for larger interval lengths.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | The proposed approximations are practically accurate over the displayed finite-sample regimes. | Author claim | E3, E5 | Supported by close simulation comparisons in the selected tables; not universal. | High for displayed regimes |
| C2 | Berk-Jones variants usually have stronger practical power except in extremely rare-mixture corners. | Author claim | E4 | Supported across the reported Gaussian-mixture grid and discussion. | Medium-high |
| C3 | Original HC can become weak at very small global significance levels. | Author claim | E3-E5 | Mechanistically consistent with its rapidly increasing threshold and application results. | High |
| C4 | Production use should report a sensitivity surface across variants and tuning. | Reviewer interpretation | E3-E6 | Reasonable because power rankings change with prevalence, effect, threshold, and minimum index. | Medium |
| C5 | A global rejection does not identify which hypotheses are false. | Source-supported interpretation | E2 | Explicitly separated from localization in the introduction. | High |

## Methodology

- `Research objective`: preserve the paper's finite-sample significance and power contribution and translate it into auditable implementation boundaries.
- `Sources inspected`: canonical arXiv metadata, verified full-paper HTML, verified PDF, journal DOI metadata, and three related Black Lake manuscripts.
- `Discovery strategy`: uniform local archive draw; identity/DOI/title/slug dedup; bounded source repair; full-paper section/table extraction; related-DEP keyword and concept search.
- `Inclusion criteria`: direct method, proof, simulation, application, limitation, and closely related calibration evidence.
- `Exclusion criteria`: abstract-only inference, unverified code/data availability, and unrelated author-inventory records.
- `Analytical approach`: empirical, conceptual, comparative, implementation, replication, and statistical-governance analysis.
- `Evidence handling`: author claims, reported numerical evidence, reviewer interpretation, and private process evidence are labeled separately.
- `Uncertainty handling`: unrerun proofs/simulations, dependence, discretization, and external-validity gaps remain explicit.
- `Extraction process`: headings, prose, formulas, tables, discussion, appendix, and references were inspected from the complete HTML and cross-checked against PDF integrity.
- `Version control`: arXiv v3 and stable DOI identities are recorded.

## Scope, Constraints, and Assumptions

- `Scope`: global sparse-mixture testing, significance approximation, reported power, lower confidence bounds, and interval-scan implications.
- `Temporal boundary`: paper v3 and repository context available on 2026-07-20.
- `Evidence limits`: no simulation code, raw outputs, or independent proof verification; local source files are not redistributed.
- `Assumptions`: the reported simulations and tables accurately reflect the source's stated procedures.
- `Constraints`: validity depends on $p$-value calibration, dependence structure, statistic definition, index range, multiplicity family, and numerical stability.
- `Out of scope`: causal claims, clinical conclusions, production certification, and localization of individual false hypotheses.
- `Intended use`: DEP preservation, statistical review, implementation planning, and replication backlog.
- `Audience`: statisticians, ML evaluators, anomaly-detection engineers, and scientific-software reviewers.
- `Reproducibility boundary`: formulas and designs are preserved; numerical reproduction still requires an implementation and independent test harness.

## Observations

- `Observed pattern`: power rankings change materially with the nonnull fraction and global significance budget.
- `Technical implication`: the minimum scanned order index is an operational tuning parameter, not an incidental constant.
- `Contradiction or tension`: asymptotic rare-signal optimality does not guarantee superior finite-sample power under stringent multiplicity.
- `Open question`: how robust are the approximations under dependent, discrete, or estimated $p$-values?
- `Reviewer hypothesis`: a versioned multi-statistic sensitivity report will be more reliable than selecting one aggregation rule globally.

## Considerations

Individual $p$-values must be valid for the deployed null and dependency structure before any aggregate test is meaningful. Multiple-comparison families must be fixed before thresholding. Extreme-tail calculations need stable numerics and simulation cross-checks. Repeated tuning on the same data creates selection bias. In scientific or clinical workflows, global rejection should trigger confirmatory analysis and localization procedures rather than an automatic substantive claim.

## Strengths

- The paper joins theory, finite-sample approximation, simulation, and two application patterns.
- It compares four closely related statistics under a common framework, making the source of power trade-offs legible.
- It reports concrete disagreement regimes rather than presenting asymptotic consistency as sufficient practical evidence.
- The appendix exposes proof conditions and boundary issues needed for technical review.

## Weaknesses

- Simulations emphasize independent Gaussian mixtures; dependent and discrete tests are not established.
- Code and raw simulation outputs were not available from the inspected source set, limiting numerical reproducibility.
- Some application evidence is synthetic and uses bounded repetitions, so biological or operational transfer is not validated.
- Approximation accuracy at more extreme interval lengths and multiplicity structures remains uncertain.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish reference code and seeds | Reproducibility | Extreme tails are numerically delicate. | Independent verification and regression tests. | Maintenance burden. | Reproduce every table cell within declared tolerance. |
| Add dependence/discreteness studies | External validity | Real $p$-values are often correlated or discrete. | Clearer operating envelope. | Large design space. | Block, factor, permutation, and discrete-null simulations. |
| Report tuning sensitivity | Governance | $k_0$, $k_1$, alpha, and variant change conclusions. | Prevents cherry-picked decisions. | More complex UX. | Predeclared grid and immutable sensitivity report. |
| Separate discovery and localization | Scientific interpretation | Global rejection does not identify signals. | Reduces overclaiming. | Requires follow-up method. | Confirmatory split or selective-inference evaluation. |

## Potential Implementations

1. **Multi-statistic audit CLI**
   - `User`: statistical reviewer.
   - `Goal`: compare HC/MHC/BJ/MBJ decisions on one locked $p$-value vector.
   - `Core mechanism`: compute all variants, threshold receipts, and disagreement flags.
   - `Required inputs`: calibrated $p$-values, family definition, alpha, index range, threshold source.
   - `Outputs`: statistics, decisions, sensitivity grid, and provenance receipt.
   - `Risk controls`: immutable input hash, simulation validation, no automatic localization.
   - `Evaluation`: reproduce paper scenarios and synthetic null coverage.
2. **Threshold validation service**
   - `User`: scientific platform team.
   - `Goal`: reject analytic thresholds unsupported in the requested regime.
   - `Core mechanism`: compare approximation with bounded Monte Carlo and cached validated envelopes.
   - `Required inputs`: statistic, $n$, alpha, dependence model, repetitions, seed policy.
   - `Outputs`: threshold, uncertainty, approximation error, approval status.
   - `Risk controls`: retry ceiling, compute budget, multiple-seed checks.
   - `Evaluation`: null Type-I error within declared tolerance.
3. **Sparse-signal planning notebook**
   - `User`: experiment designer.
   - `Goal`: choose a predeclared rule from plausible prevalence/effect ranges.
   - `Core mechanism`: simulate power surfaces and highlight variant disagreement.
   - `Required inputs`: null/alternative generator, sample sizes, prevalence grid, multiplicity budget.
   - `Outputs`: power surface, expected detection regime, stop conditions.
   - `Risk controls`: synthetic/public data only; no post-hoc rule selection on evaluation data.
   - `Evaluation`: held-out scenario coverage and preregistration audit.

## Three Ways to Exercise This Research

1. `Null calibration exercise`: generate independent uniform $p$-values, compare analytic and Monte Carlo thresholds for all four variants, output Type-I error and stop if tolerance is exceeded.
2. `Sparse-mixture power map`: use synthetic Gaussian mixtures over a preregistered prevalence/effect grid, output power and disagreement heatmaps, and stop before interpreting any one grid as universal.
3. `Multiplicity stress test`: embed each statistic in synthetic interval scans with rising family size, output global false-positive and power curves, and stop when simulation error or compute budget exceeds its limit.

## Example MVP Product

- `Product name`: SparseTest Receipt.
- `Target user`: research engineer reviewing many-test anomaly or discovery pipelines.
- `Problem`: aggregation choices and multiplicity thresholds are often hidden behind one global decision.
- `Core workflow`: ingest a locked $p$-value vector and preregistered family; compute four statistics; validate thresholds against a bounded simulation cache; emit decisions, sensitivity, and caveats.
- `Data requirements`: synthetic calibration data or authorized aggregate $p$-values; no raw personal data required.
- `Architecture`: local CLI, deterministic statistic library, threshold cache, Monte Carlo worker, Markdown/JSON receipt generator.
- `Success metrics`: correct paper-scenario values, controlled synthetic-null error, deterministic receipts, explicit disagreement display.
- `Risk controls`: no automatic localization, immutable inputs, dependence warning, alpha-family approval, bounded simulations, human review.
- `Limitations`: cannot repair invalid individual $p$-values, prove causal effects, or guarantee power outside validated regimes.
- `MVP boundary`: no clinical decision automation and no adaptive threshold selection on evaluation data.
- `Evaluation plan`: unit tests, table-reproduction tests, null-coverage tests, dependence stress tests, and reviewer acceptance.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Donoho and Jin (2004) | Foundational paper | Higher-criticism detection boundary and sparse-mixture framing. | https://doi.org/10.1214/009053604000000265 |
| Berk and Jones (1979) | Foundational paper | Likelihood-ratio goodness-of-fit statistic underlying BJ variants. | https://doi.org/10.1007/BF00533553 |
| Meinshausen and Rice (2006) | Methodological neighbor | Lower confidence bounds for the proportion of false nulls. | https://doi.org/10.1214/009053605000000741 |
| Jager and Wellner (2007) | General theory | Large-sample family connecting tail and center-sensitive goodness-of-fit tests. | https://doi.org/10.1214/009053606000001208 |
| PAC Confidence DEP | Related Black Lake review | Finite-sample probability statements and calibration boundaries. | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/` |
| Kernel Equivalence DEP | Related Black Lake review | Hypothesis direction, margins, and normal/bootstrap calibration. | `.lake-data/DEP-E/DEP-E-20260719-Kernel Equivalence/` |
| Noisy Poisson Inference DEP | Related Black Lake review | Misspecification-aware tests and finite-sample Type-I behavior. | `.lake-data/DEP-E/DEP-E-20260716-Noisy Poisson Inference/` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/1411.1437 | Identity, abstract, versions, DOI, journal link. | 2026-07-20 | Metadata only. |
| R2 | https://ar5iv.labs.arxiv.org/html/1411.1437 | Complete method, results, discussion, appendix, tables, references. | 2026-07-20 | Verified local copy withheld. |
| R3 | https://arxiv.org/pdf/1411.1437 | Primary PDF and cross-format evidence. | 2026-07-20 | Verified local copy withheld. |
| R4 | https://doi.org/10.1214/15-AOS1312 | Published article identity. | 2026-07-20 | Journal DOI. |
| R5 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence | Related confidence/calibration synthesis. | 2026-07-20 | Repository context. |
| R6 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260719-Kernel%20Equivalence | Related hypothesis-direction synthesis. | 2026-07-20 | Repository context. |
| R7 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Noisy%20Poisson%20Inference | Related misspecification/Type-I synthesis. | 2026-07-20 | Repository context. |

## Appendix

### Selection, Deduplication, and Integrity

- Uniform accepted draw: one-based index 16,762 of 75,776 unique units from 75,779 PDFs.
- Reselection: one earlier unit failed the complete-source gate; duplicate exclusions 0; current-job duplicate exclusions 0.
- Dedup surfaces: Black Lake artifacts/index, automation memory, relevant Black-Lake-Data records, current-job set, and public-safe 24-hour markers.
- Accepted source gate: PDF 295,092 bytes with valid header/EOF; fallback HTML 2,859,259 bytes with 134,924 body characters, 180 document markers, 38 headings, and 60 structure terms.
- Source locality: all PDF, HTML, metadata, repair records, and caches were withheld. No `.source/` exists and zero source documents were uploaded.

### Replication Checklist

- Implement the four exact statistic definitions and index constraints.
- Reproduce analytic thresholds and Table 1 simulation comparisons.
- Reproduce Section 3 Gaussian-mixture power with declared seeds and uncertainty.
- Stress dependent and discrete $p$-values outside the paper's core assumptions.
- Preserve configuration, input hash, statistic version, threshold provenance, and null-coverage report.
