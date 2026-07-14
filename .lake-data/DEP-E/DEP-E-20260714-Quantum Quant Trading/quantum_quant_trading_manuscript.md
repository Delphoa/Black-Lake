---
title: "Quantum Quant Trading - DEP-E"
generated_at: "2026-07-14"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of a theoretical quantum workflow for preselecting and testing cointegrated portfolios."
source_status: "verified local source bundle; public URLs only in deposit"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-14"
temporal_cutoff: "arXiv v1 submitted 2021-04-29; journal version published 2022-08-05; sources inspected through 2026-07-14"
primary_url: "https://arxiv.org/abs/2104.14214"
stable_identifier: "arXiv:2104.14214v1; DOI:10.1088/1367-2630/ac7f26"
confidence_summary: "High for source identity and algorithm description; medium for mathematical reporting; low for practical quantum advantage because no implementation, simulation, or trading backtest was supplied."
safety_scope: "research review, synthetic evaluation, and non-executable financial analysis"
distribution_notes: "Source files remain local and were not uploaded; public artifact contains URLs and derived prose only."
---

# Quantum Quant Trading - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | *Quantum Quantitative Trading: High-Frequency Statistical Arbitrage Algorithm* | Primary preprint | PDF and full-paper HTML | arXiv:2104.14214v1 | https://arxiv.org/pdf/2104.14214; https://ar5iv.labs.arxiv.org/html/2104.14214 | Local copies verified and withheld; ar5iv was the approved fallback because arXiv full HTML was unavailable. | 2026-07-14 | Complete paper inspected |
| S2 | arXiv record | Primary metadata | HTML | arXiv:2104.14214v1 | https://arxiv.org/abs/2104.14214 | Canonical title, authors, subjects, date, DOI links, and source links. | 2026-07-14 | Inspected |
| S3 | *Quantum computational quantitative trading: high-frequency statistical arbitrage algorithm* | Published revision | Open-access journal paper | New Journal of Physics 24 (2022) 073036; DOI:10.1088/1367-2630/ac7f26 | https://doi.org/10.1088/1367-2630/ac7f26; https://inspirehep.net/files/6079bd5e0f489200fe499b61fb425df5 | Journal paper states CC BY 4.0; inspected for version-sensitive claims. | 2026-07-14 | Complete published paper inspected |
| S4 | Private archive verification record | Source-integrity evidence | PDF/HTML/metadata/source verification | arXiv:2104.14214 | Public locators in S1-S2; local path withheld | Verified source bundle remains local and is not part of this deposit. | 2026-07-14 | Passed |
| S5 | Black-Lake repository standard | Repository authority | Markdown | default branch at access date | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public filing and source-locality policy. | 2026-07-14 | Fetched and inspected |
| S6 | Structure-Aware Systems DEP-E | Related DEP | Markdown | DEP-E-20260714-Structure Aware Systems | `.lake-data/DEP-E/DEP-E-20260714-Structure Aware Systems/structure-aware-systems.md` | Related context only; includes a condition-number-aware quantum linear solver review. | 2026-07-14 | Inspected |
| S7 | Deep ESN Memory DEP-E | Related DEP | Markdown | DEP-E-20260710-Deep ESN Memory | `.lake-data/DEP-E/DEP-E-20260710-Deep ESN Memory/deep_esn_memory_manuscript.md` | Related context only; covers time-series memory and synthetic evaluation. | 2026-07-14 | Inspected |
| S8 | Irregular Clipped SR DEP-E | Related DEP | Markdown | DEP-E-20260711-Irregular Clipped SR | `.lake-data/DEP-E/DEP-E-20260711-Irregular Clipped SR/irregular_clipped_sr_manuscript.md` | Related context only; covers structured regression decoding and state-evolution tuning. | 2026-07-14 | Inspected |
| S9 | Black-Lake-Data repository standard | Related repository authority | Markdown | default branch at access date | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Inspected for related DEP context and provenance expectations. | 2026-07-14 | Fetched and inspected |

Authors: Xi-Ning Zhuang, Zhao-Yun Chen, Yu-Chun Wu, and Guo-Ping Guo. The arXiv record lists Quantum Physics, Computational Engineering/Finance/Science, Computational Finance, and Trading and Market Microstructure. The preprint was submitted on 2021-04-29. The revised journal article was received in March 2022, accepted in July 2022, and published on 2022-08-05.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary preprint | Introduction, problem formulation, Algorithms 1-3, Theorems 1 and 3, Lemmas 2 and 4-6, realistic-case analysis, conclusion, and references. | Mechanism, assumptions, query bounds, hybrid workflow, and disclosed future work. | High for source reporting | arXiv v1 is not the final journal version; equations were reviewed but not formally rederived. |
| E2 | S2 | Canonical metadata | Title, authors, submission date, categories, arXiv DOI, related journal DOI, and source links. | Stable identity and version pinning. | High | Abstract alone does not validate technical claims. |
| E3 | S3 | Published primary paper | Revised problem statement, journal headline complexity, realistic-case numbers, qRAM assumption, qubit estimate, and future-work statements. | Publication status and material differences from v1. | High for reporting | No independent reproduction; the published realistic-case section contains inconsistent displayed magnitudes. |
| E4 | S4 | Local integrity record | PDF size/header/EOF; full-paper HTML size/body/markers/structure; metadata/source collection; zero partials. | Complete-source gate and repair evidence. | High | Source files are intentionally withheld, so only the public-safe verification summary is exposed here. |
| E5 | S5 and S9 | Repository standards | Containerized DEP-E location, README contract, publication index, source-locality requirement, and attribution rules. | Artifact structure and submission policy. | High | Process evidence only. |
| E6 | S6 | Related DEP | Quantum linear-system condition-number analysis, small Qiskit simulations, and state-preparation/loading caveats. | Direct conceptual bridge to conditional quantum advantage. | Medium | Different application domain and source set. |
| E7 | S7 | Related DEP | Reservoir memory theorem, NARMA evaluation, incomplete series derivation, and no-code limitation. | Time-series state and theory-to-experiment bridge. | Medium | Classical recurrent model, not quantum finance. |
| E8 | S8 | Related DEP | Structured regression code, OAMP state evolution, operating-point tuning, and finite-length simulation limits. | Regression, conditioning, and regime-validation bridge. | Medium | Communications decoding differs from cointegration testing. |

## Executive Summary

The paper proposes a two-stage quantum statistical-arbitrage workflow. Variable Time Preselection Algorithm (VTPA) uses repeated eigenvalue/condition-number comparison to retain portfolios whose price matrices appear highly multicollinear. Quantum Cointegration Test (QCT) then uses quantum linear regression inside a hybrid Engle-Granger/augmented Dickey-Fuller pipeline to estimate cointegration coefficients and test residual stationarity.

The intellectual contribution is a conditional complexity argument, not an empirical trading system. The preselection analysis depends on oracle access to price matrices stored in qRAM, normalized/Hermitian matrix transformations, eigenvalue-distribution assumptions, a chosen condition-number threshold, and a willingness to miss some cointegrated portfolios. QCT returns to classical matrix multiplication, residual construction, test-statistic calculation, and critical-value comparison. No circuit simulation, hardware execution, market backtest, transaction-cost analysis, or official implementation was found in the inspected sources.

Version pinning materially changes the headline. ArXiv v1 presents a preselection term of `O(sqrt(d) * kappa_0^2 * log(1/epsilon)^2)`. The 2022 journal abstract and realistic-case section add a `sqrt(N)` factor, yielding `O(sqrt(dN) * kappa_0^2 * log(1/epsilon)^2)`, while the theorem-level query expression remains written without that loading factor. The journal realistic-case discussion also displays both `10^8` and `10^11` for the revised expression. These inconsistencies do not invalidate the conceptual algorithms, but they prevent the artifact from treating the advertised speedup as a settled end-to-end result.

Reviewer confidence is high that the algorithms and assumptions are represented faithfully, medium that the asymptotic derivations have been transcribed without loss, and low that the paper establishes deployable advantage. The most useful downstream action is an assumption-and-cost audit on synthetic matrices, not live or simulated trading.

## Detailed Summary

### Problem Context

Statistical arbitrage seeks securities whose prices move together over a formation interval, verifies a stable long-run relation, and then monitors deviations. The paper uses multicollinearity as a preselection signal and cointegration as the stronger statistical property required for a mean-reverting spread. Its motivating scale uses thousands of stocks and high-frequency observations, making exhaustive portfolio regressions appear expensive.

Multicollinearity and cointegration are related but not interchangeable. A large condition number indicates sensitivity and near-linear dependence in a matrix; cointegration requires a stationary linear combination of individually non-stationary time series. The authors therefore place a statistical verification stage after condition-number preselection.

### Data and Access Model

The method assumes a portfolio pool `P`, price matrices with `d` stocks over `N` time samples, and a standard quantum oracle that maps stock/time indices to stored price values. The matrix is assumed available in qRAM and transformed into a real symmetric block matrix suitable for HHL-style routines. Matrix normalization and balanced/well-behaved linear-regression inputs are part of the theoretical model.

These assumptions are central costs, not implementation details. A query-complexity improvement can coexist with expensive data loading, state preparation, fault-tolerant arithmetic, repeated measurement, and classical output reconstruction. The source does not supply an end-to-end resource estimate covering those stages.

### Variable-Time Preselection

The Quantum Condition Number Comparison Algorithm (QCNCA/QCNC) uses phase-estimation-style tests to detect eigenvalues smaller than `1/kappa_0`. Finding such a component yields a lower bound suggesting condition number at least `kappa_0`. Under a uniform eigenvalue-density assumption and `kappa >= 2 kappa_0`, the paper bounds success probability and repeats the procedure to raise confidence.

VTPA evaluates increasing thresholds `kappa_j = 2^j`. Clock and stop registers remove low-condition-number matrices early, so later, more expensive tests apply to fewer candidates. The average query bound depends on the distribution `P_j` over condition-number buckets. Under the source's illustrative uniform assumption over `log(kappa)`, the theorem reports `O(sqrt(d) * kappa_0^2 * log(1/epsilon)^2)` for preselection. The algorithm is explicitly heuristic: it can miss cointegrated portfolios because its goal is to find some candidates rather than enumerate all of them.

### Quantum Cointegration Test

QCT follows the two-regression structure of an Engle-Granger test. Quantum linear regression first estimates coefficients for a candidate portfolio. Classical multiplication and subtraction construct predicted values and residuals. A second regression uses time, lagged residuals, and residual differences for an augmented Dickey-Fuller statistic. Classical logic then computes the statistic and compares it with a critical-value table.

The paper supplies a composite complexity expression for the two regression stages plus the `dN` residual-construction term, with dependence on variable count, lag length, condition numbers, and precision. It also attempts to bound error propagation from the first regression into the second. Because residual extraction and the final statistical decision are classical, QCT is best understood as a hybrid algorithm rather than a fully quantum pipeline.

### Evidence and Claimed Advantage

ArXiv v1 estimates roughly `N = 1.2 x 10^7` half-second observations across a trading year and around 8,000 U.S. stocks. It contrasts a classical `O(N^2 d)` benchmark with a much smaller theoretical preselection term at `kappa_0 = 1000`. The journal revision adds `sqrt(N)` to the overall preselection expression and estimates more than 50 qubits for the proposed VTPA structure, while saying simulation is difficult and leaving circuit simplification/simulation to future work.

These are scenario calculations, not experiments. There are no empirical eigenvalue distributions for real portfolio matrices, no measured qRAM build/access cost, no comparison against modern classical screening/approximation baselines, and no market-quality evaluation. Transaction costs, asynchronous quotes, multiple testing, structural breaks, slippage, and market impact are outside the presented evidence.

### Version Difference

The published work has a changed title, reorganized exposition, a real-data illustration of PEP/KO comovement, updated references/affiliations, and the added `sqrt(N)` factor in its headline complexity. Within the journal text, Theorem 1 still isolates a query bound without `sqrt(N)`, suggesting that the extra term represents access or broader pipeline cost. The realistic-case section then associates the revised form with both `10^8` and `10^11`. A future reviewer should reconcile these expressions directly from the authors' intended cost model before using them in comparative claims.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | A variable-time sequence of condition-number tests can preselect high-condition-number matrices while stopping easier cases early. | Author theoretical claim | E1, E3 | The construction and proof outline are explicit; correctness was not independently formalized. | Medium-high |
| C2 | Under the stated uniform-distribution assumptions, preselection has a quadratic dependence on `kappa_0` and sublinear dependence on portfolio width. | Author complexity claim | E1, E3 | Supported as a theorem-level query claim, conditional on the oracle and distribution model. | Medium |
| C3 | Quantum linear regression can be inserted into a hybrid two-stage cointegration test with bounded error propagation. | Author theoretical claim | E1, E3 | The algorithm and bound are stated; practical state/output costs and statistical calibration are not demonstrated. | Medium |
| C4 | The approach establishes quantum advantage for realistic high-frequency statistical arbitrage. | Author conclusion | E1, E3 | Only conditionally supported by asymptotic scenario analysis; not established end to end or empirically. | Low |
| C5 | The journal revision adds `sqrt(N)` to the headline preselection complexity and contains inconsistent numeric magnitudes in the realistic-case discussion. | Reviewer version observation | E1, E3 | Directly visible when the complete versions are compared. | High |
| C6 | No practical implementation or market evidence is supplied by the inspected sources. | Negative evidence | E1-E3 | The papers explicitly leave simulation/circuit simplification as future work and provide no backtest. | High |
| C7 | Related Black Lake work supports an audit emphasis on conditioning, structured state, and regime-sensitive validation. | Reviewer synthesis | E6-E8 | Concrete conceptual overlap exists, but related entries do not validate this paper. | Medium |

## Methodology

- `Research objective`: Preserve a source-first, schema-complete review that distinguishes the paper's theoretical algorithms from evidence of practical quantum or financial advantage.
- `Sources inspected`: Verified local arXiv v1 PDF, verified full-paper HTML fallback, local metadata and TeX source, canonical arXiv record, complete 2022 open-access journal paper, live Black-Lake and Black-Lake-Data READMEs, and exactly three related Black Lake manuscripts.
- `Discovery strategy`: Enumerated local PDFs with `rg --files -g "*.pdf"`, grouped by parent directory, selected zero-based index 60,411 uniformly from 75,774 units using `Get-Random`, then applied duplicate rejection checks.
- `Inclusion criteria`: Included sources that identify the paper, expose complete methods/results/limitations, pin material version differences, define deposition policy, or supply concrete overlap in quantum linear systems, time-series state, and structured regression decoding.
- `Exclusion criteria`: Abstract-only pages were not accepted as full-paper evidence. Generic arXiv recommendation/code widgets, secondary commentary, and unverified trading claims were excluded. Source files were withheld locally.
- `Analytical approach`: Empirical-evidence audit, conceptual analysis, comparative version review, implementation analysis, financial safety, product research, and replication planning.
- `Evidence handling`: Author claims, equations, scenario estimates, negative evidence, reviewer interpretation, and related-DEP synthesis are separately labeled. The journal paper is not silently substituted for arXiv v1.
- `Uncertainty handling`: Unreproduced derivations and cost assumptions receive medium or low confidence; the `sqrt(N)` and numeric inconsistencies are preserved rather than reconciled by guesswork.
- `Extraction process`: Full PDF text and full-paper HTML sections were inspected across introduction, methods, algorithms, proofs, realistic-case analysis, conclusion, appendices, and references. Published-paper figures/captions and data-availability statements were also inspected.
- `Random-selection validation`: The selected ID/title/DOI/slug were absent from public artifacts, memory, dedup index, Black-Lake-Data search, and 24-hour markers. The first draw was eligible; reselections were zero.

## Scope, Constraints, and Assumptions

- `Scope`: Paper identity, algorithm mechanism, complexity assumptions, source-reported scenario analysis, version differences, limitations, and safe implementation/replication paths.
- `Temporal boundary`: arXiv v1 from 2021 and the published 2022 revision, inspected through the public date marker 2026-07-14.
- `Evidence limits`: No theorem prover, circuit simulator, quantum hardware, trading dataset, code repository, or independent replication was used.
- `Assumptions`: The review assumes the public journal DOI and arXiv record refer to versions of the same underlying work; any cost-model reconciliation must remain version-pinned.
- `Constraints`: Source locality, repository allowlist, financial non-advice, public-safe paths, and no executable trading logic.
- `Out of scope`: Portfolio recommendations, live-market execution, profitability forecasts, legal/regulatory advice, and claims of fault-tolerant hardware readiness.
- `Intended use`: Research review, assumption auditing, synthetic replication planning, and future quantum-algorithm evaluation.
- `Audience`: Quantum algorithms researchers, numerical linear algebra reviewers, quantitative-finance researchers, and research engineers.
- `Reproducibility boundary`: The logical workflow can be emulated classically on synthetic data; the claimed quantum advantage cannot be reproduced from the inspected artifacts alone.

## Observations

- `Observed pattern`: The proposal converts an undesirable numerical property—ill-conditioning—into a screening signal, then pays condition-number-dependent cost to detect it.
- `Technical implication`: Fast matrix queries are not equivalent to a fast end-to-end trading pipeline when input loading, residual extraction, and test calibration remain material.
- `Contradiction or tension`: Preselection seeks large condition numbers as evidence of multicollinearity, while quantum linear-system routines generally become more expensive and less stable as condition numbers grow.
- `Version observation`: The journal revision appears to recognize an `N`-dependent cost absent from v1's headline, but its theorem and realistic-case numbers are not fully harmonized.
- `Open question`: The empirical distribution of eigenvalues and condition numbers across candidate portfolios could dominate average performance, yet it is assumed rather than measured.
- `Reviewer hypothesis`: The most transferable contribution may be adaptive condition-number triage, independent of any trading application, if evaluated with explicit false-negative and access-cost accounting.

## Considerations

- Financial datasets are non-stationary, asynchronous, affected by corporate actions, and subject to multiple-testing bias; a cointegration flag is not a profitability guarantee.
- High-frequency deployment requires latency, transaction-cost, slippage, market-impact, risk-limit, and compliance analysis absent from the paper.
- qRAM, fault-tolerant Hamiltonian simulation, precision management, repeated measurements, and classical output reconstruction could overwhelm query-level gains.
- A condition-number threshold creates a recall/precision tradeoff. The source accepts missed portfolios, so any evaluation must report coverage rather than only successful finds.
- Synthetic research tools should avoid order placement, brokerage integration, or performance marketing. Outputs should be diagnostics and evidence ledgers.
- Published-version equations and numeric estimates need author clarification or independent derivation before citation in comparative performance tables.

## Strengths

- The paper connects quantum linear algebra to a clearly decomposed statistical workflow rather than proposing an undifferentiated black box.
- It makes condition-number and precision dependence visible and supplies formal statements for preselection and the hybrid cointegration test.
- Variable-time stopping is conceptually aligned with heterogeneous candidate difficulty.
- The authors acknowledge missed candidates, distribution sensitivity, simulation difficulty, and future circuit work.
- The published article is open access, enabling direct version comparison and audit.

## Weaknesses

- The advantage is theoretical and conditional on qRAM/oracle access; no end-to-end resource analysis is provided.
- The uniform eigenvalue/log-condition-number assumptions are not validated on market matrices.
- The classical baseline is coarse and does not cover modern randomized, incremental, approximate, parallel, or GPU-based screening methods.
- No circuit, hardware, code, backtest, or independent replication supports the practical claim.
- The pipeline mixes quantum and classical stages without measuring transfer, readout, or residual-construction costs.
- Version-sensitive headline formulas and inconsistent numeric magnitudes reduce auditability.
- Statistical-arbitrage validity is not tested under transaction costs, structural breaks, data snooping, or out-of-sample evaluation.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish a versioned cost ledger | Complexity | Separate qRAM build, state preparation, queries, arithmetic, measurement, and classical post-processing. | Makes end-to-end comparisons auditable. | Requires hardware assumptions and careful notation. | Reconcile every term across v1 and journal equations. |
| Measure real spectral distributions | Preselection model | Replace uniform assumptions with empirical condition/eigenvalue histograms. | Reveals average-case regime and false-negative behavior. | Market data choices can bias results. | Use multiple public, time-split datasets with no trading claims. |
| Strengthen classical baselines | Comparative evidence | `O(N^2d)` alone is insufficient for modern practice. | Identifies where quantum methods might still matter. | Engineering effort and benchmark sensitivity. | Compare randomized SVD, sketching, incremental regression, and GPU solvers. |
| Build a classical emulator | Reproducibility | Validate control flow, thresholds, and error propagation before quantum execution. | Exposes statistical and version errors cheaply. | Does not validate quantum speed. | Synthetic matrices with known rank, condition number, and cointegration. |
| Add financial validity gates | Application scope | Cointegration and profit are distinct. | Prevents misleading implementation claims. | Requires careful non-advice framing. | Out-of-sample stationarity, costs, break tests, and multiple-testing controls. |
| Resolve published inconsistencies | Documentation | `sqrt(N)` and `10^8`/`10^11` differences affect the central claim. | Improves citation reliability. | May require author correspondence. | Produce a line-by-line derivation and erratum request if needed. |

## Potential Implementations

1. `Quantum Advantage Assumption Auditor`
   - `User`: Quantum algorithm reviewer.
   - `Goal`: Turn a claimed complexity into a versioned ledger of access, conditioning, precision, measurement, and classical costs.
   - `Core mechanism`: Structured claim parsing plus human-verified cost categories.
   - `Required inputs`: Paper version, equations, oracle model, parameter ranges, and baseline definition.
   - `Outputs`: Assumption matrix, unresolved terms, and reproducibility checklist.
   - `Risk controls`: No investment recommendations; every claim linked to a source/version.
   - `Evaluation`: Two reviewers independently reproduce the ledger and reconcile differences.

2. `Synthetic Spectral Triage Lab`
   - `User`: Numerical linear algebra or quantum-finance researcher.
   - `Goal`: Test how VTPA-like thresholds behave under controlled eigenvalue distributions.
   - `Core mechanism`: Generate synthetic matrices with known spectra, apply classical condition-number screening, and measure candidate recall/cost buckets.
   - `Required inputs`: Matrix sizes, spectrum families, noise, thresholds, and target recall.
   - `Outputs`: Bucket histograms, false-negative rates, and cost sensitivity plots.
   - `Risk controls`: Synthetic data only; no live prices or order execution.
   - `Evaluation`: Recover known condition-number classes and report failure boundaries.

3. `Hybrid Cointegration Reproduction Notebook`
   - `User`: Research engineer.
   - `Goal`: Emulate the paper's two-regression logic on synthetic integrated series.
   - `Core mechanism`: Classical coefficient estimation, residual construction, ADF calibration, and injected approximation error.
   - `Required inputs`: Synthetic random walks, known cointegration vectors, lag rules, and error budgets.
   - `Outputs`: Detection accuracy, calibration curves, and error-propagation checks.
   - `Risk controls`: Educational synthetic output; no profitability claims.
   - `Evaluation`: Type-I error and power against controlled null/alternative cases.

## Three Ways to Exercise This Research

1. `Complexity reconciliation`: Objective—rederive v1 and journal headline expressions; inputs—the two complete versions and a cost-category template; steps—map theorem/query terms to loading and post-processing, recompute the realistic example, and flag unmatched terms; output—a versioned equation ledger; success criterion—every factor has a source location or is marked unresolved; stop condition—any step requires guessing an unstated hardware model.
2. `Spectral assumption stress test`: Objective—replace uniform assumptions with controlled alternatives; inputs—synthetic matrices with uniform, clustered, heavy-tailed, and adversarial spectra; steps—measure threshold recall and work by condition bucket; output—sensitivity curves; success criterion—results reproduce known matrix condition classes; stop condition—numerical precision makes the ground truth unreliable.
3. `Cointegration error sandbox`: Objective—test the two-regression error path; inputs—synthetic I(1) series with known cointegration and injected coefficient noise; steps—construct residuals, run ADF-style decisions, and sweep lag/precision; output—calibration and power tables; success criterion—null and alternative behavior are separated within stated error bands; stop condition—outputs are interpreted as trade recommendations.

## Example MVP Product

- `Product name`: QSA Assumption Auditor
- `Target user`: Quantum algorithms researcher, technical reviewer, or research program manager.
- `Problem`: Quantum-advantage claims often mix query bounds with unstated loading, conditioning, measurement, and classical costs.
- `Core workflow`: Import a paper's versioned claims; record oracle/data model; classify each complexity term; compare preprint and publication; attach evidence locations; run consistency checks; export a public-safe review.
- `Data requirements`: Paper metadata, equations, parameter definitions, declared baseline, hardware/oracle assumptions, and optional synthetic benchmark results. No market credentials or private trading data.
- `Architecture`: Local Markdown parser, structured claim ledger, deterministic validation rules, optional symbolic math checks, and static report generator.
- `Success metrics`: 100% of headline factors mapped to evidence; zero unresolved version substitutions; reviewer agreement on cost categories; reproducible numeric example or explicit failure.
- `Risk controls`: Source/version pinning, no brokerage APIs, no performance promises, synthetic examples by default, and mandatory uncertainty labels.
- `Limitations`: Cannot prove theorem correctness or hardware advantage; symbolic extraction may misread formulas; final judgments require expert review.
- `MVP boundary`: One paper family and one classical baseline at a time; no automated investment or trading functionality.
- `Deployment model`: Local-only CLI or notebook that emits Markdown and JSON ledgers.
- `Evaluation plan`: Use the v1/journal discrepancy as a regression case, then test two unrelated quantum-linear-system papers.
- `Failure modes`: Formula glyph loss, silent version conflation, omitted access costs, and false precision in scenario estimates.

## Related Research and Reading

### Exactly Three Related Black Lake Entries

| Entry | Concrete Overlap | Source Basis |
|---|---|---|
| `.lake-data/DEP-E/DEP-E-20260714-Structure Aware Systems/structure-aware-systems.md` | Its quantum-linear-solver review centers condition-number scaling and explicitly retains state-preparation, matrix-access, loading, readout, and error caveats—the same boundary needed here. | Complete related manuscript; its S12/E10 basis is arXiv:2607.08220 and small Qiskit simulations. |
| `.lake-data/DEP-E/DEP-E-20260710-Deep ESN Memory/deep_esn_memory_manuscript.md` | Both works model long time-series state and derive capacity/complexity under structural assumptions, while leaving important architecture claims only partly validated. | Complete related manuscript; arXiv:1908.07063 theory and NARMA simulations. |
| `.lake-data/DEP-E/DEP-E-20260711-Irregular Clipped SR/irregular_clipped_sr_manuscript.md` | Both use structured linear regression/inverse operations, condition-sensitive iterative logic, and regime-specific tuning; the related work shows how state evolution can be paired with finite-length tests. | Complete related manuscript; arXiv:2106.01573 and IEEE ITW DOI record. |

### External Primary Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Harrow, Hassidim, and Lloyd, *Quantum algorithm for linear systems of equations* | Foundational quantum algorithm | Basis for the linear-system/oracle model used by the paper. | https://doi.org/10.1103/PhysRevLett.103.150502 |
| Wiebe, Braun, and Lloyd, *Quantum Algorithm for Data Fitting* | Quantum regression | Direct precursor to quantum least-squares fitting. | https://doi.org/10.1103/PhysRevLett.109.050505 |
| Engle and Granger, *Co-integration and Error Correction* | Econometrics | Classical foundation for the two-step cointegration test. | https://doi.org/10.2307/1913236 |
| Ambainis, *Variable time amplitude amplification and quantum algorithms for linear algebra problems* | Quantum algorithms | Foundation for variable-time acceleration. | https://doi.org/10.4230/LIPIcs.STACS.2012.636 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2104.14214 | Canonical preprint metadata and version history. | 2026-07-14 | Inspected; abstract not used alone for technical claims. |
| R2 | https://arxiv.org/pdf/2104.14214 | Complete arXiv v1 paper. | 2026-07-14 | Verified local PDF withheld from public deposit. |
| R3 | https://ar5iv.labs.arxiv.org/html/2104.14214 | Complete full-paper HTML fallback. | 2026-07-14 | Verified local HTML withheld; `/abs/` was not treated as the paper. |
| R4 | https://doi.org/10.1088/1367-2630/ac7f26 | Published-paper identifier. | 2026-07-14 | New Journal of Physics 24 (2022) 073036. |
| R5 | https://inspirehep.net/files/6079bd5e0f489200fe499b61fb425df5 | Complete open-access published paper. | 2026-07-14 | Used for version comparison, journal equations, and limitations. |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository filing and source-locality policy. | 2026-07-14 | Live default-branch file fetched before writing. |
| R7 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository provenance policy. | 2026-07-14 | Live default-branch file inspected. |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-Structure%20Aware%20Systems/structure-aware-systems.md | Related condition-number/quantum-solver context. | 2026-07-14 | Related context, not selected-paper validation. |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Deep%20ESN%20Memory/deep_esn_memory_manuscript.md | Related time-series memory context. | 2026-07-14 | Related context, not selected-paper validation. |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Irregular%20Clipped%20SR/irregular_clipped_sr_manuscript.md | Related structured-regression context. | 2026-07-14 | Related context, not selected-paper validation. |

## Appendix

### Selection and Dedup Record

- Candidate units: 75,774 unique PDF-parent paper units.
- Random method: uniform zero-based `Get-Random` draw after `rg --files` enumeration; rejection sampling only for duplicates.
- Selected index: 60,411.
- Known public arXiv IDs before deposit: 156.
- Archive units matching known public IDs: 62.
- Reselections: 0.
- Same-paper result: arXiv ID, DOI, normalized title, slug, and preceding-24-hour markers absent from all required checks.

### Source Integrity Record

- Initial state: valid PDF, missing full-paper HTML; review stopped.
- Repair: preserved PDF; collected approved ar5iv full-paper HTML fallback, arXiv metadata HTML, and TeX source locally.
- PDF gate: 222,189 bytes, `%PDF-` header, trailing `%%EOF`—passed.
- HTML gate: 1,098,195 bytes, 95,012 body characters, document marker, 46 heading/section markers, seven structure terms—passed.
- Local records: README, attribution/provenance record, summary CSV, and verification JSON updated.
- Partials: zero.
- Public-source gate: no PDF, HTML, source archive, cache, extracted source text, or local path is included in this DEP.

### Replication Checklist

- [ ] Reconcile preprint and journal complexity factors from first principles.
- [ ] Recompute both journal realistic-case magnitudes.
- [ ] Define qRAM construction and query assumptions.
- [ ] Generate synthetic matrices with controlled spectra and condition numbers.
- [ ] Measure preselection recall, false negatives, and work per bucket.
- [ ] Reproduce the hybrid cointegration logic with synthetic I(1) series.
- [ ] Add modern classical randomized/iterative baselines.
- [ ] Keep all outputs diagnostic and non-executable for trading.
