---
title: "FGLE Midpoint Scheme - DEP-E"
generated_at: "2026-07-16"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of an implicit midpoint and weighted-shifted Grünwald scheme for a fractional Ginzburg-Landau equation."
source_status: "verified complete v1 PDF and approved ar5iv full-paper HTML inspected; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "arXiv:1601.02301v1, Elsevier publication record, and focused public code search inspected through 2026-07-16"
primary_url: "https://arxiv.org/abs/1601.02301v1"
stable_identifier: "arXiv:1601.02301v1; DOI 10.1016/j.jcp.2016.02.018"
confidence_summary: "High for scheme, theorem, and table transcription; medium for proof interpretation; low for computational-efficiency and physical-generalization claims."
safety_scope: "research analysis and synthetic numerical validation only"
distribution_notes: "Paper files, metadata HTML, caches, and extracted text were not redistributed."
---

# FGLE Midpoint Scheme - DEP-E

## Source Metadata

| ID | Source | Role | Identifier / Version | Public Locator | Status |
|---|---|---|---|---|---|
| S1 | An implicit midpoint difference scheme for the fractional Ginzburg-Landau equation | Primary metadata/PDF | arXiv:1601.02301v1 | https://arxiv.org/abs/1601.02301v1 | Full PDF inspected |
| S2 | ar5iv rendering | Primary full-paper HTML fallback | 1601.02301 | https://ar5iv.labs.arxiv.org/html/1601.02301 | Verified full text inspected |
| S3 | Elsevier record | Publisher metadata | JCP 312, 31-49 | https://doi.org/10.1016/j.jcp.2016.02.018 | Inspected |
| S4 | arXiv DOI | Stable arXiv identifier | 10.48550/arXiv.1601.02301 | https://doi.org/10.48550/arXiv.1601.02301 | Resolved |
| S5 | Global NS Existence | Related DEP | DEP-E-20260712 | `.lake-data/DEP-E/DEP-E-20260712-Global NS Existence/global_ns_existence_manuscript.md` | Inspected |
| S6 | Flag Hardy Operators | Related DEP | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-Flag Hardy Operators/flag_hardy_operators_manuscript.md` | Inspected |
| S7 | Acoustic Phase Retrieval | Related DEP | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md` | Inspected |
| S8 | Black Lake and Black-Lake-Data READMEs | Repository authority | live default branches | https://github.com/Delphoa/Black-Lake ; https://github.com/Delphoa-Labs/Black-Lake-Data | Inspected before writing |

Authors: Pengde Wang and Chengming Huang. Submitted 2016-01-11. The publisher record identifies *Journal of Computational Physics*, volume 312, pages 31-49, published 2016-05-01. The arXiv record links the journal DOI and applies CC BY-NC-SA 4.0. No official code repository was identified in the paper, arXiv record, publisher record, or focused search.

## Evidence Ledger

| ID | Source basis | Evidence class | Supports | Confidence | Limitation |
|---|---|---|---|---|---|
| E1 | S1/S2, Sections 2-3 | Primary method | WSGD fractional operator and implicit midpoint scheme | High | no code audit |
| E2 | S1/S2, Lemmas 2.1-2.7 | Primary analysis | coefficient signs, operator factorization, norm inequalities | Medium-high | imported results and dense derivations not formally checked |
| E3 | S1/S2, Theorems 4.1-4.4 | Primary theory | bound, existence, convergence, uniqueness | High for statements | assumptions differ across theorems |
| E4 | S1/S2, Section 5.1 | Primary implementation | linearized fixed-point-like inner iteration | High | iteration convergence and cost not analyzed |
| E5 | S1/S2, Tables 1-2 | Primary empirical | observed second-order refinement | High for transcription | fractional reference uses same scheme on fine grid |
| E6 | S1/S2, Figures 1-6 | Primary empirical | parameter, nonlocality, and inviscid-limit illustrations | Medium | qualitative synthetic examples |
| E7 | S3/S4 | Publication metadata | journal identity, pages, DOI, date | High | publisher full text not needed |
| E8 | Focused public search | Availability | no official code identified | Medium | unlinked code may exist |
| E9 | S5-S7 | Related processed research | proof, operator, and numerical-validation bridges | Medium | contextual, not evidence for this theorem |
| E10 | Selection, verification, cache, and dedup records | Process evidence | eligibility and source integrity | High | local identifiers omitted publicly |

## Executive Summary

The paper studies a one-dimensional nonlinear complex Ginzburg-Landau equation with a fractional Laplacian of order `1 < alpha <= 2`. It truncates the whole-line problem to a finite interval with a homogeneous exterior volume constraint, discretizes time by the implicit midpoint rule, and approximates the Riesz fractional derivative using a second-order weighted and shifted Grünwald difference operator.

The analysis establishes discrete fractional norm inequalities, an `l2_h` a priori bound, existence, and an error estimate `O(tau^2 + h^2)` for sufficiently small time step independent of mesh size. This is the paper's sense of unconditional convergence: no `tau/h` mesh-ratio restriction appears in Theorem 4.3. Uniqueness is narrower; Theorem 4.4 assumes `tau <= C h`. The nonlinear step is solved with an inner linearized iteration whose coefficient matrix is constant across time levels, but convergence, iteration counts, runtime, and scaling are not reported.

Table 1 uses an exact classical (`alpha=2`) solution and reports refinement orders converging to 2.00. Table 2 reports roughly 2.03-2.08 for `alpha=1.3, 1.6, 1.9`, but its reference solution is the same method at `h=0.0125`, `tau=0.0001`. The evidence validates internal consistency more strongly than independent fractional-PDE accuracy or efficiency.

## Detailed Summary

### Problem and Spatial Operator

The model combines time evolution, a dissipative/dispersion coefficient multiplying the fractional Laplacian, a cubic complex nonlinearity, and linear gain or loss. For computation, the whole line is replaced by `(a,b)` and the solution is set to zero outside. The paper assumes the interval is large enough that truncation error is negligible; that truncation error is not included in the displayed `O(tau^2+h^2)` estimate.

The WSGD operator averages shifted Grünwald formulas with weights determined by `alpha`. It achieves second-order consistency for left and right Riemann-Liouville derivatives. Their symmetric combination approximates the Riesz fractional derivative. The analysis develops coefficient sign properties, Fourier symbols, an energy norm, a discrete fractional Gagliardo-Nirenberg inequality, and equivalence to fractional Sobolev seminorms.

### Fully Discrete Scheme

At each time step the method evaluates the fractional operator, linear term, and cubic term at the midpoint average `(u^(n+1)+u^n)/2`, with the time derivative given by the centered difference. This produces a nonlinear system. Section 5 introduces a linearized inner iteration: the current nonlinear magnitude is lagged while the fractional and selected linear terms remain implicit. The resulting matrix does not change with time level, allowing reuse of a factorization in principle.

### Theoretical Results

Theorem 4.1 bounds the discrete `l2_h` norm. When the linear coefficient `gamma <= 0`, the norm is nonincreasing; for positive `gamma`, it is bounded on a fixed finite horizon under a sufficiently small time step. Theorem 4.2 uses Brouwer's fixed-point theorem to establish existence.

Under a smooth exact solution and sufficiently small `tau`, Theorem 4.3 derives `||e^n||_h <= C(tau^2+h^2)` with `C` independent of `tau` and `h`. The proof combines local truncation error, fractional norm estimates, nonlinear bounds, and a discrete Grönwall inequality. Theorem 4.4 proves uniqueness for sufficiently small discretization parameters under `tau <= C h`. Thus existence and convergence are not the same as an unrestricted unique-solve guarantee.

### Numerical Evidence

For `alpha=2`, the method is compared with an analytic solution on `[-16,16]`; coupled refinement from `(tau,h)=(0.02,0.2)` to `(0.00125,0.0125)` lowers `l2_h` error from `5.5462e-3` to `2.1460e-5`, with reported orders from 2.0104 to 2.0001. The infinity-norm results behave similarly.

For fractional orders 1.3, 1.6, and 1.9, a fine-grid numerical solution from the same method supplies the reference. The three coarser levels report orders around 2.03-2.08. Additional figures qualitatively examine gain/loss, fractional-order effects, and approach to the fractional Schrödinger limit as dissipative coefficients decrease. No baseline method, repeated run, solver residual history, runtime, memory, or hardware record is supplied.

## Key Claims and Evidence

| Claim | Type | Evidence | Assessment | Confidence |
|---|---|---|---|---|
| The WSGD spatial operator is second-order consistent. | Theory | E1/E2 | Stated and developed through symbol/weight analysis. | Medium-high |
| The numerical solution is bounded. | Theory | E3 | Theorem 4.1, with different behavior for `gamma` sign. | High for statement |
| A discrete solution exists. | Theory | E3 | Brouwer argument in Theorem 4.2. | High for statement |
| The `l2_h` error is `O(tau^2+h^2)` without a mesh-ratio restriction. | Theory | E3 | Theorem 4.3 requires smoothness and small `tau`, but no `tau(h)` relation. | High for statement |
| The scheme is uniquely solvable without step coupling. | Implication | E3 | Not supported; uniqueness theorem assumes `tau <= C h`. | Low |
| Numerical evidence confirms second order. | Empirical | E5 | Strong for `alpha=2`; fractional cases are self-convergence. | Medium-high |
| The method is computationally efficient. | Operational claim | E4-E6 | Constant matrix helps, but no timing, complexity, or comparator. | Low |
| First random draw was eligible. | Process | E10 | ID, both DOIs, title, slug, artifacts, memory, companion, and 24-hour scans clear. | High |

## Methodology

- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, treated unique PDF parent directories as paper units, and chose a uniform zero-based index with PowerShell `Get-Random`.
- `Source integrity`: Classified the unit before review. The valid PDF lacked full-paper HTML. Official arXiv HTML was unavailable after bounded retries, so the approved ar5iv fallback was fetched and validated for bytes, body text, document markers, headings, and paper-structure terms; metadata remained metadata only.
- `Cache methodology`: Ran `document_source_processing.py extract-arxiv` in `missing-only` mode with the central archive cache. The miss became `cached` in about 6.3 seconds using `pypdf` and `html-regex`; no source package was collected.
- `Deduplication`: Scanned Black Lake logs, reports, DEP-E paths, staging index, automation memory, relevant Black-Lake-Data content, exact/base arXiv ID, journal DOI, normalized title, slug, and 24-hour markers. No match occurred; no reselection was needed.
- `Review`: Inspected the complete paper's scheme, lemma chain, Theorems 4.1-4.4, iterative algorithm, Tables 1-2, figures, conclusion, publisher metadata, and focused code search. No proof or numerical result was reproduced.
- `Related synthesis`: Selected exactly three inspected deposits for concrete overlap in nonlinear-PDE proof architecture, nonlocal-operator verification, and synthetic inverse-problem validation.
- `Distribution`: Public artifacts contain original review prose and derived status JSON only. PDF, HTML, metadata, cache, and extracted text remain local.

## Scope, Constraints, and Assumptions

- The PDE is one-dimensional with `1 < alpha <= 2`, positive dissipative/cubic real coefficients, smooth-solution assumptions for convergence, and a finite time horizon.
- The whole-line problem is truncated to a finite interval with zero exterior data; truncation error is assumed negligible, not quantified in the theorem or tables.
- The convergence constant and sufficiently small time-step threshold are not operationally calibrated.
- Uniqueness adds `tau <= C h`, even though the convergence theorem avoids a mesh-ratio restriction.
- Fractional-order numerical accuracy is measured against a finer run of the same scheme.
- No implementation, runtime, memory, hardware, or solver-convergence evidence was found.

## Observations

- The paper's strongest reusable contribution is the discrete functional-analysis bridge, not merely the midpoint stencil.
- “Unconditional” is theorem-specific: it describes the convergence estimate's lack of a `tau/h` relation, not every property of every numerical solve.
- Existence through Brouwer does not show that the proposed inner iteration converges to that solution.
- A time-invariant coefficient matrix could support factorization reuse, but the fractional operator may still be dense and costly.
- The exact `alpha=2` table is stronger evidence than the fractional self-reference table.
- Qualitative wave plots illustrate model behavior but do not validate a physical system.

## Considerations

A reproduction should separately audit spatial consistency, temporal consistency, nonlinear-solver convergence, domain truncation, and end-to-end cost. Use manufactured solutions for fractional orders where possible, an independent spectral or finite-element solver, domain-size sweeps, and residual/error budgets that distinguish iteration error from discretization error.

System evaluation should report operator storage, matrix structure, factorization cost, per-step iteration count, residual tolerance, wall-clock time, peak memory, and scaling with grid size. Fast Toeplitz/FFT or preconditioned solvers should be compared under matched accuracy. Proof review should map every imported lemma, smoothness hypothesis, constant, and theorem-specific step restriction.

## Strengths

- Combines a second-order temporal rule with a second-order fractional spatial approximation.
- Develops discrete norm inequalities suited to the nonlocal operator.
- Separates a priori boundedness, existence, convergence, and uniqueness into explicit results.
- Includes an implementable linearized inner solve and notes matrix reuse.
- Uses an analytic exact solution for the classical-order convergence table.

## Weaknesses

- The uniqueness theorem requires a mesh-ratio relation absent from the headline convergence phrasing.
- Whole-line truncation error and exterior-boundary sensitivity are not quantified.
- Fractional accuracy uses a same-method fine-grid surrogate rather than independent truth.
- The inner iteration has no convergence theorem, iteration-count table, or failure analysis.
- “Efficiency” is unsupported by runtime, complexity, memory, hardware, or baseline measurements.
- No official code or reproducible environment was identified.

## Potential Improvements

1. Publish code, exact parameters, factorization/iteration details, stopping rules, and reproducible tables/figures.
2. Prove or empirically bound convergence of the inner nonlinear iteration and characterize failure regimes.
3. Quantify domain-truncation and exterior-boundary error alongside time/space discretization error.
4. Use manufactured fractional solutions and independent spectral/FEM references with repeated precision studies.
5. Compare dense, Toeplitz/FFT, preconditioned, and accelerated implementations with time/memory scaling.
6. State theorem-specific meanings of unconditional stability, convergence, existence, and uniqueness explicitly.

## Potential Implementations

| Implementation | Purpose | Required evidence | Main risk | Acceptance signal |
|---|---|---|---|---|
| Convergence audit harness | Separate `tau`, `h`, iteration, and truncation error | manufactured solutions and multiple solvers | correlated reference error | stable second-order slopes independently |
| Proof dependency ledger | Track hypotheses and theorem-specific restrictions | formula-preserving source and expert review | false proof confidence | every claim mapped to dependencies |
| Fractional solver profiler | Test matrix/FFT/preconditioner options | code, grids, hardware metadata | accuracy-cost mismatch | lower cost at matched residual/error |

## Three Ways to Exercise This Research

### 1. Reproduce the Classical Table

- Implement the stated WSGD/midpoint scheme and analytic `alpha=2` test.
- Match the five `(tau,h)` pairs and `1e-14` inner tolerance.
- Report `l2_h` and infinity errors, slopes, residuals, and precision sensitivity.

### 2. Build an Independent Fractional Check

- Choose a manufactured fractional solution with a computable forcing term.
- Compare the scheme against an independent spectral or FEM implementation.
- Sweep time step, grid, domain extent, and solver tolerance independently.

### 3. Audit Solver Realization

- Log fixed-point residuals, iterations, factorization reuse, wall time, peak memory, and failure cases.
- Compare direct dense, structured Toeplitz/FFT, and preconditioned iterative solvers.
- Verify quality/cost frontiers across `alpha`, nonlinearity, and grid size.

## Example MVP Product

### Fractional PDE Evidence Bench

- `Purpose`: determine whether a fractional-PDE scheme's theorem, numerical implementation, and cost claims agree.
- `Inputs`: symbolic scheme record, manufactured/exact cases, parameter grids, solver backends, theorem assumptions, tolerances, and domain extents.
- `Core mechanism`: run orthogonal refinement studies, independent-reference comparisons, residual tracking, and theorem-assumption checks while separating error sources.
- `Outputs`: convergence plots, proof-dependency graph, truncation/iteration/discretization ledger, runtime-memory curves, and failure-case archive.
- `Evaluation`: recovered order, independent-solver agreement, residual-to-error relation, domain sensitivity, and cost at matched accuracy.
- `Safety boundary`: scientific research aid only; numerical agreement is not a formal proof or physical validation.

## Related Research and Reading

1. [Global NS Existence](../DEP-E-20260712-Global%20NS%20Existence/global_ns_existence_manuscript.md) - shares nonlinear-PDE a priori estimates, existence/uniqueness distinctions, smoothness assumptions, imported proof dependencies, and the boundary between source review and proof verification.
2. [Flag Hardy Operators](../DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md) - shares nonlocal-operator norm bounds, geometry-compatible discretization/reconstruction, imported lemmas, and the danger of treating finite-grid demonstrations as theorem certificates.
3. [Acoustic Phase Retrieval](../DEP-E-20260716-Acoustic%20Phase%20Retrieval/acoustic_phase_retrieval_manuscript.md) - supplies a concrete standard for synthetic PDE experiments: independent forward solvers, mesh-error separation, mismatch ladders, calibration, runtime, and uncertainty.

## Source References

1. Wang, P., and Huang, C. *An implicit midpoint difference scheme for the fractional Ginzburg-Landau equation*. arXiv:1601.02301v1. https://arxiv.org/abs/1601.02301v1
2. Full-paper PDF. https://arxiv.org/pdf/1601.02301
3. Approved full-paper HTML fallback. https://ar5iv.labs.arxiv.org/html/1601.02301
4. Wang and Huang, *Journal of Computational Physics* 312 (2016), 31-49. https://doi.org/10.1016/j.jcp.2016.02.018
5. arXiv DOI. https://doi.org/10.48550/arXiv.1601.02301
6. Global NS Existence DEP-E. `.lake-data/DEP-E/DEP-E-20260712-Global NS Existence/global_ns_existence_manuscript.md`
7. Flag Hardy Operators DEP-E. `.lake-data/DEP-E/DEP-E-20260716-Flag Hardy Operators/flag_hardy_operators_manuscript.md`
8. Acoustic Phase Retrieval DEP-E. `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md`

## Appendix

### Selected Quantitative Record

| Case | Coarse `(tau,h)` | Fine `(tau,h)` | `l2_h` error change | Reported order range | Evidence boundary |
|---|---|---|---|---|---|
| `alpha=2` exact | `(0.02,0.2)` | `(0.00125,0.0125)` | `5.5462e-3` to `2.1460e-5` | 2.0104 to 2.0001 | analytic reference |
| `alpha=1.3` | `(0.02,0.2)` | `(0.005,0.05)` | `1.2966e-2` to `7.5488e-4` | 2.0275 to 2.0749 | same-scheme fine reference |
| `alpha=1.6` | `(0.02,0.2)` | `(0.005,0.05)` | `1.0519e-2` to `6.0393e-4` | 2.0444 to 2.0780 | same-scheme fine reference |
| `alpha=1.9` | `(0.02,0.2)` | `(0.005,0.05)` | `6.7430e-3` to `3.9052e-4` | 2.0346 to 2.0753 | same-scheme fine reference |

### Provenance and Distribution

- Random draw: uniform zero-based index 47,945 among 75,776 unique paper units; first draw accepted.
- Source gate: valid PDF plus verified full-paper HTML after approved fallback; metadata HTML never counted as paper content.
- Cache: missing-only extraction changed miss to cached in about 6.3 seconds; source package absent.
- Dedup: exact/base arXiv ID, both DOIs, normalized title, slug, artifact, memory, companion-repository, and 24-hour scans clear.
- Distribution: no PDF, HTML, metadata, source archive, cache, extracted text, or local archive reference is included in the repository.
