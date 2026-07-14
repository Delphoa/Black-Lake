# Report-Mark: Quantum Quant Trading

## Source Metadata

| Field | Value |
|---|---|
| Selected paper | *Quantum Quantitative Trading: High-Frequency Statistical Arbitrage Algorithm* |
| Authors | Xi-Ning Zhuang; Zhao-Yun Chen; Yu-Chun Wu; Guo-Ping Guo |
| arXiv | arXiv:2104.14214v1, submitted 2021-04-29 |
| Journal version | *Quantum computational quantitative trading: high-frequency statistical arbitrage algorithm*, New Journal of Physics 24 (2022) 073036 |
| DOI | 10.1088/1367-2630/ac7f26 |
| Subjects | Quantum Physics; Computational Engineering/Finance/Science; Computational Finance; Trading and Market Microstructure |
| Local source state | Repaired and verified complete: full PDF plus full-paper HTML; metadata and TeX source retained locally |
| Source distribution | Source files withheld locally; public URLs and derived analysis only |

Primary records: https://arxiv.org/abs/2104.14214, https://arxiv.org/pdf/2104.14214, https://doi.org/10.1088/1367-2630/ac7f26, and the inspected open-access journal copy at https://inspirehep.net/files/6079bd5e0f489200fe499b61fb425df5.

## Selection and Deduplication

PDFs were enumerated with `rg --files -g "*.pdf"` and grouped by parent directory into 75,774 paper units. PowerShell `Get-Random` selected zero-based index 60,411. Repository markers mapped 156 public arXiv IDs to 62 archive units, leaving 75,712 units eligible by known-ID exclusion. The selected arXiv ID, DOI, normalized title, and slug were absent from Black-Lake logs/reports/deposits, the public dedup index, automation memory, Black-Lake-Data code search, and the preceding-24-hour marker window. Reselections: zero.

## Local Source Integrity

The initial unit had a 222,189-byte PDF but no full-paper HTML, so review stopped for repair. The PDF passed size, `%PDF-` header, and trailing `%%EOF` checks and was preserved. The arXiv HTML endpoint was unavailable; the approved ar5iv fallback produced 1,098,195 bytes, 95,012 body characters, a document marker, 46 headings/sections, and seven paper-structure terms. Metadata HTML and the TeX package were collected locally. The local README, provenance record, summary CSV, and verification JSON were updated; no `.part` file remained.

## Concise Research Notes

The paper separates statistical arbitrage into preselection and verification. VTPA searches portfolio matrices for large condition numbers, treating near-linear dependence as a multicollinearity signal. QCT then applies quantum linear regression in a hybrid Engle-Granger/augmented Dickey-Fuller workflow: quantum coefficient estimation is followed by classical residual construction, another regression, a classical test statistic, and critical-value comparison.

The strongest contribution is the explicit adaptive condition-number screening concept. The strongest limitation is that the claimed advantage is an oracle/query analysis, not an end-to-end experiment. qRAM construction, state preparation, Hamiltonian simulation, measurement, classical output, financial data quality, and modern classical baselines are not jointly costed.

The preprint and journal versions must not be conflated. ArXiv v1 highlights `O(sqrt(d) * kappa_0^2 * log(1/epsilon)^2)` for preselection. The journal abstract and realistic-case analysis add `sqrt(N)`, but the theorem-level query expression remains without it. The journal realistic-case discussion also associates the revised expression with both `10^8` and `10^11`. This review therefore records quantum advantage as a conditional author claim with low practical confidence.

## Evidence and Attribution

| Evidence ID | Evidence | Supports | Assessment |
|---|---|---|---|
| E1 | Complete arXiv v1 PDF and verified full-paper HTML | Algorithms 1-3, theorems, complexity derivations, assumptions, realistic case, and future work | High confidence for faithful reporting; no formal proof verification |
| E2 | Canonical arXiv record | Identity, authors, date, subjects, version, and DOI links | High confidence |
| E3 | Complete 2022 journal paper | Published status, changed headline complexity, qRAM model, qubit estimate, and future-work limits | High confidence for version observation; low for end-to-end advantage |
| E4 | Private local verification record | Complete-source integrity and successful repair | High confidence; source files deliberately withheld |
| E5 | Live repository READMEs | DEP-E filing, contents, attribution, and source-locality policy | High confidence for process only |
| E6-E8 | Exactly three related DEP manuscripts | Quantum-linear-system, time-series-memory, and structured-regression bridges | Medium confidence; contextual rather than validation evidence |

## Related DEP Entries

| Entry | Relevance | Source Basis |
|---|---|---|
| `.lake-data/DEP-E/DEP-E-20260714-Structure Aware Systems/structure-aware-systems.md` | Its review of quantum linear solvers makes condition-number scaling inseparable from state preparation, matrix access, loading, readout, and error. | Related manuscript S12/E10, based on arXiv:2607.08220 and 19-28-qubit Qiskit simulations. |
| `.lake-data/DEP-E/DEP-E-20260710-Deep ESN Memory/deep_esn_memory_manuscript.md` | Both works reason about long time-series state under structural assumptions and expose a gap between theory and broad empirical validation. | Related manuscript based on arXiv:1908.07063, its memory theorem, and synthetic NARMA results. |
| `.lake-data/DEP-E/DEP-E-20260711-Irregular Clipped SR/irregular_clipped_sr_manuscript.md` | Both use structured regression/inverse operations whose value depends on operating regime, conditioning, and approximations. | Related manuscript based on arXiv:2106.01573, OAMP state evolution, and finite-length simulations. |

## Synthesis Note

### Concept Bridge

All four artifacts can be read as studies of structure-dependent computation. Quantum quantitative trading tries to avoid exhaustive regression by testing spectral structure first. The quantum-linear-solver DEP asks when matrix structure preserves favorable conditioning. Deep ESN work treats temporal memory as an architecture-bounded resource. Irregular clipping uses an explicit state model to tune a mixture of nonlinear preprocessors. Across them, asymptotic or theoretical gains remain credible only inside a measured regime defined by access cost, spectra, memory, noise, and finite-size behavior.

### Potential Implementations

1. `Versioned quantum-cost ledger`: map every complexity factor to oracle access, loading, arithmetic, measurement, and classical post-processing, with evidence locations for v1 and the journal paper.
2. `Synthetic spectral triage benchmark`: generate matrices with controlled eigenvalue distributions and measure threshold recall, false negatives, and average work without financial execution.
3. `Hybrid cointegration calibration lab`: inject controlled regression error into synthetic integrated series and measure how ADF decisions change across lag and precision settings.

### Deeper Relationship Observations

1. The selected paper intentionally searches for ill-conditioning, yet the quantum primitives it relies on become more expensive as conditioning worsens; the signal and the computational hazard are the same variable.
2. Deep ESN and irregular-clipping deposits both pair analytical state models with synthetic finite-size evidence, highlighting the missing middle layer in the selected paper between proof and deployment.
3. The journal's added `sqrt(N)` term mirrors the broader quantum-linear-solver lesson that data access cannot be erased by reporting only solver-query complexity.

### Conceptual Similarities

1. Each related entry uses a structural proxy—condition number, reservoir memory, or state evolution—to reduce a larger search or inference problem.
2. Each result is regime-dependent and becomes weaker when assumptions about spectra, dynamics, noise, or access no longer hold.
3. Each benefits from separating a fast screening/model stage from a slower verification stage with explicit failure and uncertainty reporting.

### MVP Implementations with Code Mock-ups

1. `Complexity Claim Gate` — rejects a speedup claim until access, solver, measurement, and classical terms are recorded.

```python
REQUIRED_COSTS = {"data_access", "quantum_solver", "measurement", "classical_post"}

def claim_is_auditable(cost_terms: dict[str, str]) -> bool:
    return REQUIRED_COSTS.issubset(cost_terms) and all(cost_terms[key] for key in REQUIRED_COSTS)
```

2. `Spectral Candidate Lab` — performs safe classical thresholding on synthetic condition numbers.

```python
def preselect(condition_numbers: list[float], threshold: float) -> list[int]:
    if threshold <= 1:
        raise ValueError("threshold must exceed one")
    return [index for index, value in enumerate(condition_numbers) if value >= threshold]
```

3. `Version Delta Check` — makes changed headline terms visible instead of silently merging paper versions.

```python
def changed_terms(preprint: set[str], journal: set[str]) -> dict[str, list[str]]:
    return {
        "added": sorted(journal - preprint),
        "removed": sorted(preprint - journal),
    }
```

Dependencies: Python 3.9+ only. These snippets use synthetic metadata or numbers, perform no trading, and are illustrative rather than production-ready.

### Developer Challenges

1. Preserve mathematical notation and version identity through PDF/HTML extraction without silently normalizing inconsistent formulas.
2. Build synthetic benchmarks whose known spectra and cointegration ground truth remain numerically stable across precision settings.
3. Prevent a research audit tool from being misrepresented as a trading engine, profitability model, or quantum-hardware readiness claim.

### Author Challenges

1. Reconcile the preprint/journal `sqrt(N)` difference and the journal's `10^8` versus `10^11` realistic-case magnitudes.
2. Validate eigenvalue and condition-number distributions on representative portfolio matrices and report preselection recall.
3. Supply circuit/resource estimates, simulation or hardware evidence, and competitive modern classical baselines for the full hybrid pipeline.

## Validation Notes

- The manuscript contains YAML front matter, an H1 matching the YAML title, and all required schema headings.
- Manuscript title length: 29 characters, within the 40-character limit.
- The three related DEP entries above are the only related repository entries selected for synthesis.
- The Synthesis Note contains three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP implementations with three Python mock-ups, three developer challenges, and three author challenges.
- The log contains three next-review questions and three challenges.
- Source-integrity gate passed after bounded repair; no abstract-only synthesis was performed.
- No local absolute path, username, machine name, local timezone label, or exact local execution timestamp is present.
- No source file was collected for public redistribution, and no `.source/` directory was created.

## Attribution Block

- Source URL: https://arxiv.org/abs/2104.14214
  - Applies to: `Report-Mark.md`
  - Notes: Canonical metadata and version history.
- Source URL: https://arxiv.org/pdf/2104.14214
  - Applies to: `Report-Mark.md`
  - Notes: Complete arXiv v1 paper reviewed locally; source file withheld.
- Source URL: https://ar5iv.labs.arxiv.org/html/2104.14214
  - Applies to: `Report-Mark.md`
  - Notes: Verified full-paper HTML fallback reviewed locally; source file withheld.
- Source URL: https://doi.org/10.1088/1367-2630/ac7f26
  - Applies to: `Report-Mark.md`
  - Notes: Published-paper identifier and version context.
- Source URL: https://inspirehep.net/files/6079bd5e0f489200fe499b61fb425df5
  - Applies to: `Report-Mark.md`
  - Notes: Open-access complete journal paper used for version comparison.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-Structure%20Aware%20Systems/structure-aware-systems.md
  - Applies to: `Report-Mark.md`
  - Notes: Related condition-number/quantum-linear-system context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Deep%20ESN%20Memory/deep_esn_memory_manuscript.md
  - Applies to: `Report-Mark.md`
  - Notes: Related time-series-memory context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Irregular%20Clipped%20SR/irregular_clipped_sr_manuscript.md
  - Applies to: `Report-Mark.md`
  - Notes: Related structured-regression context.
