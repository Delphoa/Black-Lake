# Auditing Conditional Quantum Advantage

## A whitepaper-grade archival intake review of the Quantum Quant Trading DEP-E record

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260714-Quantum Quant Trading`  
**Source commit:** `398f692812550135476e8d560be1d2a01fa2982e`  
**Paired task indicator:** `BL-DEPPAIR-20260715-18DFEF21`  
**Direction:** `DEP-E -> DEP-A`  
**Review date:** 2026-07-15  
**Review scope:** complete two-file repository record; complete arXiv v1 and publication context; algorithm, complexity, assumptions, version differences, financial evidence boundary, re-conceptualization, and falsification agenda  
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes  
**Reproduction boundary:** no theorem prover, circuit simulator, quantum hardware, code, market data, backtest, or trading system was used.

---

## Executive assessment

The selected DEP-E contains a README and a long manuscript reviewing *Quantum Quantitative Trading: High-Frequency Statistical Arbitrage Algorithm*. Both tracked files were read completely. The record reconstructs a two-stage proposal: variable-time condition-number preselection for candidate portfolios, followed by a hybrid quantum/classical cointegration test using quantum linear regression around an Engle–Granger/augmented-Dickey–Fuller workflow. It also compares arXiv v1 with the 2022 New Journal of Physics revision, surfaces changed complexity language and inconsistent magnitudes, and separates theoretical query claims from deployable trading evidence.

The complete ten-page arXiv v1 PDF was inspected directly from title through algorithms, theorems, proofs, realistic-case analysis, conclusion, and references.[^paper] Canonical metadata and the journal DOI were checked.[^record][^journal] The source is complete rather than abstract-only. The arXiv paper reports a headline reduction from a classical `O(N^2 d)` benchmark to a preselection expression proportional to `sqrt(d) * kappa_0^2 * log(1/epsilon)^2`. The journal discussion adds a `sqrt(N)` factor to the broader headline while theorem-level query expressions remain differently scoped. The DEP-E also records `10^8` and `10^11` magnitudes in the journal realistic-case discussion. These version and scope differences are material.

The durable contribution is not a demonstrated trading speedup. It is a framework for **conditional advantage auditing**. The claimed acceleration depends on qRAM/oracle access, matrix normalization, spectral and condition-number distributions, high thresholds, balanced/well-behaved regression inputs, precision, measurements, classical residual construction, and willingness to miss some cointegrated portfolios. No source implementation, quantum simulation, hardware run, market backtest, transaction-cost study, modern classical baseline suite, or end-to-end resource estimate was supplied.

The paper’s conceptual move is interesting: use ill-conditioning, usually a numerical burden, as a multicollinearity signal and stop easy candidates early. Yet condition number also drives quantum linear-system cost. The method searches for precisely the regime that makes its subroutines expensive. Variable-time stopping may control average cost if most portfolios are easy, but that premise is assumed rather than empirically measured on market matrices.

Bottom line: the DEP-E is a careful archival review of a theoretical proposal. It should be preserved as an assumption-rich quantum-algorithm case study with a hybrid statistical workflow, not as evidence for profitable or practical high-frequency trading.

### Principal strengths

- The proposed workflow separates broad preselection from stricter cointegration testing.
- Condition-number and precision dependence are visible rather than hidden.
- Variable-time stopping explicitly models heterogeneous candidate difficulty.
- The DEP-E preserves preprint/publication differences instead of silently merging them.
- Missing implementation, hardware, simulation, and market evidence are treated as central boundaries.

### Principal qualifications

1. qRAM/oracle access and state preparation are assumed, not costed end to end.
2. Spectral and condition-number distributions are theoretical assumptions, not market measurements.
3. The classical benchmark is coarse and excludes modern approximate, randomized, incremental, parallel, and GPU approaches.
4. The cointegration test returns to classical residual construction and statistical decisions.
5. Cointegration is not profitability; transaction costs, multiple testing, breaks, slippage, and market impact are absent.

---

## 1. The problem and research question

Statistical arbitrage searches for groups of non-stationary price series whose linear combination is stationary. A typical workflow screens many candidate portfolios, estimates regression coefficients, constructs residuals, and applies a unit-root test. High-frequency observations make matrices long, and the number of possible portfolios grows combinatorially.

The paper asks whether quantum condition-number estimation and quantum linear regression can reduce the computational burden. Multicollinearity is used as a loose preselection proxy: a price matrix with a large condition number may contain nearly dependent columns and therefore may be worth a cointegration test. The stronger statistical decision remains a two-regression hybrid workflow.

The research question has two levels. At the theorem level, can a variable-time quantum procedure identify high-condition-number matrices under specified oracle and distribution assumptions? At the application level, does that query advantage survive data loading, state preparation, measurement, classical post-processing, statistical calibration, modern baselines, and market frictions? The source addresses the first partially and the second only through scenario estimates.

Multicollinearity and cointegration must not be conflated. Ill-conditioning describes sensitivity and near linear dependence in a finite matrix. Cointegration describes a stationary combination of integrated time series. Preselection can trade recall for cost and may miss genuine cointegrated portfolios.

---

## 2. Technical reconstruction

### 2.1 Data and oracle model

A candidate portfolio has `d` stocks and `N` time observations. Prices are assumed queryable through a quantum oracle/qRAM-style loading operation. The matrix is normalized and embedded into a real symmetric/Hermitian form suitable for phase-estimation and linear-system procedures. Several regression inputs are assumed balanced or well behaved.

These assumptions define the complexity model. Query access is not the same as building qRAM from streaming market data. State preparation, fault-tolerant arithmetic, precision, repeated measurement, and extracting classical outputs can dominate. The paper does not provide a hardware-specific end-to-end ledger.

### 2.2 Condition-number comparison

The condition-number comparison subroutine uses phase-estimation-like logic to detect eigenvalue components below `1/kappa_0`. If such a component is observed with sufficient probability, the matrix is treated as having a condition number at least near the threshold. Repetition raises confidence.

The success analysis relies on how the input state overlaps small-eigenvalue components and on an eigenvalue-density assumption. A matrix may be ill-conditioned yet have little amplitude on the relevant eigenspace. Precision and threshold choice affect both cost and detection.

### 2.3 Variable-time preselection

Thresholds grow geometrically, `kappa_j = 2^j`. Clock and stop registers allow low-condition-number matrices to terminate earlier while harder candidates proceed. The average complexity depends on the distribution of candidates across condition-number buckets. The paper illustrates a uniform distribution in log condition number and derives a preselection cost proportional to `sqrt(d) * kappa_0^2 * log(1/epsilon)^2` at theorem/query scope.

Variable-time behavior is the most reusable algorithmic idea. It matches computational effort to apparent difficulty. It does not remove worst-case dependence or guarantee that financial candidate distributions satisfy the assumed bucket model.

### 2.4 Quantum cointegration test

For a surviving portfolio, quantum linear regression estimates coefficients. Classical matrix multiplication and subtraction produce predicted values and residuals. A second regression uses time, lagged residual, and differenced residual terms in an augmented-Dickey–Fuller-like equation. Classical logic computes the statistic and compares it with a critical value.

The workflow is hybrid. Outputting classical coefficients and residuals incurs cost. Statistical validity requires lag selection, critical-value calibration, error propagation, and control of approximation error. The paper gives bounds but no empirical calibration or circuit implementation.

### 2.5 Guarantee boundary

Theorems are conditional on input access, distributions, precision, and subroutine assumptions. They do not guarantee profit, complete discovery, hardware speedup, or superiority to all classical methods. The paper explicitly accepts that preselection can miss candidates and leaves circuit simplification/simulation to future work.

---

## 3. Source inventory and integrity assessment

The source record contains exactly `README.md` and `quantum_quant_trading_manuscript.md`. The README supplies identity, tags, two-file inventory, source withholding, summary, relevance, and final attribution. The manuscript contains metadata, nine sources, eight evidence groups, algorithm and version reconstruction, claims, methodology, constraints, observations, improvements, implementations, exercises, an MVP, related reading, references, integrity notes, and replication checklist.

The inventory matches tracked contents at the source commit. No PDF, HTML, source archive, cache, code, data, notebook, circuit, model, or `.source` directory is present. The source record distinguishes arXiv v1, the 2022 journal revision, repository standards, and related DEP context.

Direct inspection confirmed the ten-page arXiv v1 PDF, four authors, submission date, algorithms 1–3, theorems and lemmas, condition-number proof material, hybrid QLR/ADF construction, realistic-case calculation, qubit estimate, conclusion, and references. The journal DOI resolves the published identity; the DEP-E reports complete inspection of an open-access journal copy and records material differences. The present run did not redistribute either paper.

The DEP-E’s private PDF/HTML/source verification is treated as repository-reported process evidence. Direct PDF inspection independently establishes that the primary preprint is complete. The journal version difference is preserved rather than merged into one formula.

---

## 4. Architecture and operational pipeline

The proposed system loads candidate price matrices, runs fixed or progressive condition-number preselection, applies the quantum cointegration test to survivors, and returns flags and coefficients. A real research pipeline would then need multiple-testing control, time-split validation, transaction-cost modeling, risk constraints, and out-of-sample monitoring. Those stages are absent.

An advantage audit should split costs into data acquisition/cleaning, qRAM construction, state preparation, oracle calls, Hamiltonian simulation or block encoding, amplitude amplification, measurements, coefficient extraction, residual computation, statistical testing, and classical orchestration. Every term should be versioned and tied to hardware assumptions.

No trading system should be built from this artifact. Safe exercises use synthetic matrices and synthetic integrated time series. Outputs should be condition-number, detection, and cost diagnostics, not orders or profit predictions.

---

## 5. Independent re-conceptualization

### 5.1 Adaptive numerical triage

Reviewer inference: strip away finance and the method becomes adaptive triage for a population of matrices. Cheap threshold tests reject easy cases; expensive routines focus on hard cases. This can be useful wherever difficulty has a measurable proxy and the goal tolerates false negatives.

The analogy breaks when the proxy is poorly correlated with the true property. High condition number is not cointegration. Triage quality requires recall, precision, and downstream consequence measurement.

### 5.2 Assumption ledger for quantum advantage

The paper is also a test case for separating query complexity from end-to-end cost. A durable review should map each asymptotic factor to data access, conditioning, precision, measurement, and post-processing. Unmapped factors remain unresolved rather than disappearing into a headline.

### 5.3 Transferable principle

The transferable principle is **treat input access as part of the algorithm**. Any claimed quantum advantage over data-heavy classical systems must include how data becomes a quantum state and how useful classical decisions emerge.

---

## 6. Experimental design and evidence reconstructed

There is no experiment in the conventional empirical sense. The paper provides algorithms, proofs, and a realistic-case scenario. It considers roughly 8,000 stocks and approximately `1.2 x 10^7` half-second observations over a trading year, with three-stock combinations on the order of `10^9`. It assumes fewer than about 1,000 promising multicollinear cases and uses `kappa_0 = 1000` in the scenario.

The classical benchmark is stated as `O(N^2 d)`. The quantum estimate uses the preselection expression and argues a large asymptotic gap. The preprint estimates more than 50 qubits for the variable-time structure and says simulation is difficult. No empirical market matrix is used to validate the assumed spectral distribution, false-negative rate, or candidate prevalence.

The design lacks modern classical baselines, circuit compilation, physical error correction, data-loading cost, measurement repetitions, and empirical statistical power. It also lacks a market backtest. These omissions define the evidence boundary; they are not minor follow-up details.

---

## 7. Results and quantitative audit

The “result” is a conditional complexity comparison. ArXiv v1’s headline gives preselection scaling with `sqrt(d)`, quadratic `kappa_0`, and squared logarithmic precision, without an explicit `sqrt(N)` in the headline. The journal version introduces `sqrt(N)` at broader scope. The theorem-level query expression and the total pipeline expression therefore need separate labels.

The realistic case contrasts about `10^18` for the coarse classical expression with approximately `10^8` for the preprint quantum preselection example. The DEP-E reports that the journal realistic-case section also contains `10^11` associated with the revised expression. Without a line-by-line cost derivation, these numbers should not be repeated as a settled speedup.

Condition-number dependence is severe: `kappa_0^2` in preselection and higher powers in quantum linear regression. Large condition number is both target signal and cost driver. Precision further increases work. The paper’s average-case advantage relies on most candidate matrices terminating early.

No quantitative result reports classification recall, cointegration false positives, ADF calibration under approximation, execution latency, qRAM cost, classical transfer cost, or financial return. The assessment is **theoretically interesting and conditional; practical advantage and financial utility not established**.

---

## 8. Ablations and causal evidence

No empirical ablations are reported. Theoretical sensitivity appears through condition-number buckets, precision, and distribution assumptions. The paper does not compare fixed versus progressive preselection on synthetic matrices, or quantum-inspired versus randomized classical triage.

A minimal causal program would generate matrices with known spectra, run classical emulations of the threshold logic, and measure recall and work per bucket. Then synthetic I(1) series with known cointegration could test how coefficient approximation changes ADF type-I error and power.

Alternative classical baselines should include randomized SVD, sketching, iterative least squares, approximate condition estimation, incremental/windowed regression, parallel/GPU solvers, and screening based on financial structure. The original `O(N^2 d)` comparator is insufficient for current decisions.

---

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| Variable-time tests can stop low-condition candidates early. | Algorithms and correctness/complexity analysis. | Supported as conditional theoretical construction. | Requires oracle, overlap, precision, and distribution assumptions. |
| Preselection has quadratic dependence on `kappa_0` and sublinear width dependence. | Theorem/query expression. | Supported at stated scope. | Data-loading and broader `N` costs are separate. |
| Quantum linear regression can enter a cointegration workflow. | Hybrid algorithm and error discussion. | Supported as proposal. | Classical residual/statistic stages and practical costs remain. |
| The method establishes quantum advantage for realistic trading. | Scenario calculation only. | Overstated. | No end-to-end resources, hardware, modern baselines, or empirical data. |
| The journal adds a `sqrt(N)` factor to the headline. | Version comparison recorded by DEP-E. | Strongly supported as version observation. | Theorem and pipeline scopes must be reconciled. |
| More than 50 qubits are needed in the scenario. | Preprint realistic-case discussion. | Supported as a rough author estimate. | Logical/physical qubit and fault-tolerance costs are not developed. |
| High condition number identifies cointegration. | Used as preselection proxy. | Not established as equivalence. | False negatives and false positives must be measured. |
| The proposal supports profitable trading. | No backtest or market evidence. | Not established. | Cointegration is not profit and market frictions are absent. |

---

## 10. External primary-source context

The canonical arXiv record identifies v1, four authors, categories spanning quantum physics and computational finance, full-text links, and the journal DOI.[^record] The complete PDF establishes the algorithmic and theorem structure. The New Journal of Physics DOI identifies the published revision.[^journal]

Foundational context includes HHL-style linear systems, quantum data fitting, variable-time amplitude amplification, and classical Engle–Granger cointegration. These support ingredients, not the end-to-end trading claim. This review does not independently rederive them.

The DEP-E connects the paper with Structure Aware Systems, Deep ESN Memory, and Irregular Clipped SR. The connections emphasize condition-number-aware quantum solvers, time-series memory assumptions, and structured regression/state evolution. They are contextual and do not validate the selected proposal.

---

## 11. Research notes and critical considerations

Input loading is the primary unresolved systems issue. Streaming, cleaning, adjusting, and synchronizing high-frequency prices into qRAM cannot be assumed free. Update frequency, coherence, precision, and error correction matter.

The statistical problem is nonstationary. Structural breaks, changing constituents, asynchronous quotes, corporate actions, missing data, and microstructure noise alter cointegration tests. Multiple portfolio search creates severe data-snooping risk. A mathematical speedup does not solve statistical validity.

The high-condition-number proxy is paradoxical. It selects matrices that make linear solvers less stable and more expensive. A useful system must report the distribution of accepted/rejected condition numbers and total cost, not only survivor performance.

Version control is essential. The preprint and journal headline expressions differ. Cost categories should distinguish query, loading, preprocessing, post-processing, and complete pipeline. Numeric scenarios must be reproducible from declared inputs.

Financial safety requires explicit non-advice boundaries. No brokerage API, live data credential, order placement, performance marketing, or portfolio recommendation belongs in an MVP based on this evidence.

---

## 12. Potential implications

Scientifically, the paper motivates variable-time methods for heterogeneous matrix populations. The idea may transfer better to synthetic numerical workloads than to trading.

For quantum-algorithm evaluation, the review demonstrates why an assumption ledger should accompany asymptotic claims. Oracle, state preparation, condition number, precision, measurement, output, and classical baselines must be visible.

For quantitative research, a safe contribution is a synthetic benchmark of spectral triage and cointegration error propagation. It can clarify regimes without implying investment performance.

For governance, version differences and unsupported application language should trigger claim review before funding or product decisions. The absence of code or experiments is a decision-relevant fact.

---

## 13. Falsifiable hypotheses

### Hypothesis 1: empirical spectra erase much average-case benefit

**Proposition:** Realistic matrix spectra will produce more high-cost candidates than the assumed log-uniform distribution.  
**Motivating evidence:** The distribution is assumed, not measured.  
**Predicted observation:** Work per candidate and false negatives exceed scenario estimates.  
**Falsifier:** Multiple public time-split datasets match or improve the assumed cost distribution.  
**Minimum test:** Public adjusted price matrices, no trading outputs, and transparent preprocessing.

### Hypothesis 2: modern classical screening narrows the gap

**Proposition:** Randomized/iterative classical methods will substantially outperform the `O(N^2 d)` reference in relevant regimes.  
**Motivating evidence:** The comparator is coarse.  
**Predicted observation:** End-to-end classical time grows far slower than the quoted benchmark.  
**Falsifier:** Strong baselines remain near the stated scaling after tuning.  
**Minimum test:** Synthetic and public matrices with equal accuracy and recall targets.

### Hypothesis 3: approximation changes ADF calibration

**Proposition:** Regression approximation error will alter type-I error and power near critical boundaries.  
**Motivating evidence:** QCT passes approximate coefficients into residual and ADF stages.  
**Predicted observation:** Decision error increases nonlinearly with coefficient error and lag choice.  
**Falsifier:** Calibration remains stable across the declared precision range.  
**Minimum test:** Synthetic integrated series with known null/alternative.

---

## 14. Deployment and governance considerations

Appropriate use is theoretical review, synthetic numerical experiments, and assumption auditing. Poor fit includes live trading, portfolio selection, profitability claims, or unsupervised financial decisions.

Required safeguards include version-pinned equations, complete cost categories, synthetic/public data only, strong classical baselines, false-negative reporting, no brokerage integration, non-advice labeling, independent mathematical review, and public-safe aggregate outputs. Any future market study needs legal, compliance, data-rights, and risk review.

---

## 15. Replication and falsification agenda

First, rederive preprint and journal complexity expressions line by line. Map every factor to query, loading, state preparation, measurement, output, and classical work. Recompute `10^8` and `10^11` examples from declared parameters and flag unresolved terms.

Second, implement a classical emulator of condition-number comparison and variable-time bucket logic. Use synthetic matrices with uniform, clustered, heavy-tailed, and adversarial spectra. Measure recall, false positives, false negatives, work, and numerical stability.

Third, emulate the hybrid cointegration path on synthetic I(1) series with known cointegrating vectors. Inject coefficient approximation error, vary lags and precision, and measure ADF type-I error and power.

Fourth, compare modern classical baselines under equal recall and accuracy. Include data loading and output costs for all methods. Do not use one asymptotic expression as a proxy for engineered performance.

Fifth, only after the above, define hardware resource models for block encoding/qRAM, fault tolerance, logical/physical qubits, circuit depth, and measurement. No financial interpretation is needed to evaluate the algorithm.

The highest-priority falsifier is an end-to-end ledger showing that state preparation, high-condition-number dependence, measurement, and classical post-processing eliminate the query advantage in all plausible regimes.

---

## 16. Durable restatement

> The paper proposes variable-time quantum preselection of ill-conditioned portfolio matrices followed by a hybrid quantum linear-regression cointegration test. Its complexity advantage is conditional on powerful data access and distribution assumptions, and its preprint and journal headlines require careful scope reconciliation. It supplies no implementation, hardware result, backtest, or evidence of profit.

The durable artifact is an audit of conditional quantum advantage: preserve the algorithms and formulas, but make input access, conditioning, precision, output costs, classical alternatives, statistical validity, and application evidence explicit before repeating a speedup claim.

---

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment | Boundary |
|---|---|---|---|
| DEP-E README | inventory, source policy, version warning, attribution | Sections 3 and 10 | repository metadata |
| Manuscript metadata/evidence | preprint/journal identities and related DEPs | Sections 3 and 10 | related records contextual |
| Paper Introduction | quantum-finance motivation and problem | Section 1 | application claims calibrated |
| Problem formulation | multicollinearity/cointegration and matrices | Sections 1–2 | proxy distinction retained |
| Algorithms 1–2 | fixed/progressive statistical-arbitrage workflows | Sections 2 and 4 | not executed |
| Algorithm 3 / QCNC | threshold comparison | Section 2 | oracle assumptions explicit |
| Theorems 1 and 3; Lemmas 2, 4–6 | correctness, complexity, QLR/error | Sections 2 and 7 | not independently proved |
| Variable-time proof | clock/stop registers and bucket cost | Sections 2 and 8 | distribution assumed |
| QCT equations | QLR, residuals, ADF statistic | Section 2 | hybrid classical stages retained |
| Realistic-case analysis | N, d, kappa, candidate counts, qubits | Sections 6–7 | scenario, not experiment |
| Conclusion | claimed advantage and future simulation | Sections 11 and 16 | application claim narrowed |
| References | HHL, QLR, VTAA, econometrics | Section 10 | context only |
| Journal version comparison | `sqrt(N)` and magnitude differences | Sections 7 and 11 | DEP-E reports full journal inspection |
| DEP proposals/MVP | assumption auditor and synthetic labs | Sections 12–15 | reviewer proposals |
| DEP integrity appendix | PDF/HTML/source checks | Appendix B | private files withheld |

The ten-page preprint has no empirical tables or figures requiring separate quantitative coverage; its core evidence is algorithms, theorem/lemma statements, proofs, equations, and the realistic-case calculation, all accounted for above.

---

## Appendix B. Source and evidence notes

### Primary reviewed artifact

The complete source record `.lake-data/DEP-E/DEP-E-20260714-Quantum Quant Trading` at commit `398f692812550135476e8d560be1d2a01fa2982e` was inspected.[^dep][^provenance] Both tracked Markdown files were read in full. No source file was modified, moved, copied, renamed, or reclassified.

### Directly inspected primary evidence

- https://arxiv.org/abs/2104.14214
- https://arxiv.org/pdf/2104.14214
- https://doi.org/10.1088/1367-2630/ac7f26
- https://inspirehep.net/files/6079bd5e0f489200fe499b61fb425df5
- https://github.com/Delphoa/Black-Lake/commit/398f692812550135476e8d560be1d2a01fa2982e

### Evidence boundary

The complete DEP-E, canonical metadata, and complete ten-page arXiv v1 PDF were inspected. The DEP-E’s detailed journal-version comparison was reviewed; no theorem, circuit, code, hardware, market dataset, or backtest was independently reproduced. No source document was committed. Paper reports, version observations, reviewer inference, and hypotheses are labeled separately.

### Provenance pair

`BL-DEPPAIR-20260715-18DFEF21` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. Intake/deposition become complete only after atomic submission with both ledger rows.

---

## Footnotes

[^paper]: Zhuang et al., “Quantum Quantitative Trading: High-Frequency Statistical Arbitrage Algorithm,” arXiv:2104.14214v1, complete PDF at https://arxiv.org/pdf/2104.14214.
[^record]: Canonical metadata and version links: https://arxiv.org/abs/2104.14214.
[^journal]: Published New Journal of Physics record: https://doi.org/10.1088/1367-2630/ac7f26.
[^dep]: Source DEP-E: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-Quantum%20Quant%20Trading.
[^provenance]: Selection source commit: https://github.com/Delphoa/Black-Lake/commit/398f692812550135476e8d560be1d2a01fa2982e.
