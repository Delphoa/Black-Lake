# Report-Mark: Sparse SSN-PMM

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260719-7D93E819`
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P03`
- Review date: 2026-07-19
- Review type: source-first mathematical optimization research review and implementation synthesis

## Source Metadata

| Field | Value |
|---|---|
| Paper | *A sparse semismooth Newton based proximal majorization-minimization algorithm for nonconvex square-root-loss regression problems* |
| Authors | Peipei Tang; Chengjing Wang; Defeng Sun; Kim-Chuan Toh |
| Stable identifier | arXiv:1903.11460v3 |
| Submission history | Submitted 2019-03-27; revised 2020-05-27 |
| DOI | https://doi.org/10.48550/arXiv.1903.11460 |
| Primary record | https://arxiv.org/abs/1903.11460 |
| Full-paper HTML | https://ar5iv.labs.arxiv.org/html/1903.11460 |
| PDF | https://arxiv.org/pdf/1903.11460 |
| Source package | https://arxiv.org/e-print/1903.11460 |
| Source state | Verified complete after bounded repair with approved ar5iv fallback; all original and extracted source files withheld locally. |
| Deployment job ID | `BLAD-2200-20260719-7D93E819` |
| Deployment item ID | `BLAD-2200-20260719-7D93E819-P03` |

## Concise Research Notes

### Problem

High-dimensional regression benefits from sparsity penalties, but ordinary least-squares tuning depends on the unknown noise scale and convex L1 penalties can bias large coefficients. Square-root loss avoids explicit noise-scale calibration, while nonconvex penalties such as SCAD and MCP reduce shrinkage bias. Combining nonsmooth square-root loss with a difference-of-convex sparsity penalty produces a difficult nonsmooth, nonconvex optimization problem.

### Method

The paper writes the regularized objective as square-root residual loss plus a convex sparsity norm minus a smooth convex correction. Stage I removes the concave correction and adds proximal terms, yielding a generalized elastic-net square-root problem used as a warm start. Stage II linearizes the concave term at each iterate and solves a sequence of convex majorized subproblems.

The key computational step adds a proximal term in the fitted-value space. That term makes the subproblem's dual an explicit unconstrained differentiable problem. A semismooth Newton method solves its nonlinear first-order system, while the generalized Hessian exploits the sparse active structure of the proximal mapping. This is the main algorithmic bridge from a theoretically convenient majorizer to a fast inner solver.

### Theory

The Stage-I analysis gives a sharp oracle inequality for prediction under weakly decomposable norms and explicit assumptions. The inner SSN sequence is stated to converge to the unique dual optimum with local order `1 + rho` when the residual is nonzero. For the outer inexact PMM, every cluster point is d-stationary when the objective is bounded below, the stated regularity assumption holds, and proximal-parameter sequences converge.

Whole-sequence convergence requires either an isolated cluster point or bounded iterates plus local Lipschitz continuity and a Kurdyka-Lojasiewicz property. Under a KL exponent, the paper states finite termination at exponent zero, R-linear convergence for exponents through one-half, and a stated sublinear rate above one-half. These are conditional mathematical results, not global-optimality guarantees.

### Experiments

The MATLAB R2017a experiments use an older dual-core CPU with 4 GB RAM, four synthetic regression designs with 8,000 training and 2,000 validation observations, and feature-expanded LIBSVM/UCI datasets. Convex square-root Lasso comparisons include Flare and primal/dual ADMM. Nonconvex comparisons use SCAD and MCP with parameter 3.7, validation or ten-fold cross-validation for regularization selection, KKT residuals, objective values, runtime, sparsity, MSE, and support recovery.

The authors report that PMM reaches the required accuracy faster than the ADMM alternatives in almost all tested convex cases. For SCAD, PMM is usually faster and reaches better objectives; on one housing dataset ADMM has a lower objective but 68,777 effective nonzeros versus 62 for PMM. For MCP, a corresponding abalone exception has ADMM at a lower objective but 1,039 nonzeros versus 55 for PMM. These examples expose a real multi-metric trade-off rather than a universal ordering.

### Reviewer Interpretation

The durable contribution is solver architecture: choose a majorizer whose added proximal geometry makes the dual analytically tractable, then exploit semismooth and sparse structure in the inner Newton system. The experiments support efficiency on the tested hardware and datasets but do not supply modern baselines, repeated-run uncertainty, energy/memory profiles, or independent reproduction. D-stationarity is an appropriate first-order endpoint for a nonsmooth nonconvex objective, not evidence of global optimality or statistically correct support.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Limits |
|---|---|---|---|---|
| E1 | Canonical arXiv record and DOI | Identity, authors, version, dates, subject areas | High | Metadata does not validate theory or experiments. |
| E2 | Verified PDF, full-paper HTML fallback, and source package | Complete method, proofs, algorithms, tables, conclusion, appendix | High for transcription | Proofs were inspected, not independently rederived. |
| E3 | Oracle and convergence theorems | Conditional prediction bound, d-stationarity, KL rates | High for source report | Assumptions and local endpoint matter; no global optimum. |
| E4 | Tables 1-8 and numerical section | Runtime, KKT, objective, sparsity, MSE, support comparisons | High for reported values | No rerun, uncertainty, or current-hardware benchmark. |
| E5 | Private integrity and extraction records | Random draw, dedup, repair, complete-source gate, cache | High | Private source locations withheld. |
| E6 | Noisy Poisson Inference DEP | SCAD/MCP and local-solver statistical boundary | Medium | Different likelihood and inference objective. |
| E7 | GPMD Regularized RL DEP | Proximal regularization and approximate-optimization errors | Medium | Convex tabular policy problem, not regression. |
| E8 | CAP Rank Sparsity DEP | Convex inner decomposition plus heuristic outer allocation | Medium | Model compression, not estimator theory. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Noisy Poisson Inference/noisy_poisson_inference_manuscript.md`
   - Relevance: both papers use SCAD/MCP-like amenable nonconvex penalties for sparse high-dimensional regression and distinguish stationary/local solutions from global optimality. The Poisson review adds inference calibration and multistart governance absent from a runtime-only comparison.
   - Source basis: inspected penalty geometry, local statistical theory, ADMM-like optimization, optimization boundary, and reproduction checklist.
2. `.lake-data/DEP-E/DEP-E-20260716-GPMD Regularized RL/gpmd_regularized_rl_manuscript.md`
   - Relevance: GPMD adapts proximal/Bregman geometry to a regularizer and explicitly propagates approximate evaluation and optimization errors into an error floor. Sparse SSN-PMM similarly depends on inexact subproblem controls, but targets d-stationarity under nonconvexity rather than global contraction in a convex tabular setting.
   - Source basis: inspected method, exact/approximate convergence, regularizer assumptions, error-floor theorem, and limitations.
3. `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md`
   - Relevance: CAP's RPCA stage uses convex low-rank-plus-sparse decomposition with ADMM, followed by a heuristic nonconvex allocation. It supplies a useful comparison between a certifiable inner stage and an outer decision whose convergence and cost accounting require separate receipts.
   - Source basis: inspected RPCA objective, ADMM updates, budget allocation, convergence boundary, ablations, and systems caveats.

## Synthesis Note

### Concept Bridge

The four records show that “regularized optimization” is not one guarantee. Sparse SSN-PMM builds convex majorized subproblems inside a nonconvex outer loop; Noisy Poisson Inference proves statistical properties only for a suitable local solution; GPMD obtains global contraction because its tabular objective and regularizers remain convex; CAP has a convex decomposition followed by heuristic allocation. A trustworthy implementation must therefore record which stage is convex, what residual certifies it, what outer endpoint is proved, and whether that endpoint supports the statistical or product claim.

### Potential Implementations

1. **Solver receipt harness:** wrap each PMM iteration with objective, KKT residual, step norm, active-set size, inner Newton residual, line-search result, and stop reason.
2. **Nonconvex stability lab:** run SCAD/MCP regression from deterministic warm starts and controlled perturbations, then compare support, prediction, objective, and d-stationarity rather than selecting by objective alone.
3. **Geometry-aware optimizer registry:** describe each algorithm by loss, regularizer, convex/nonconvex stage, prox availability, convergence endpoint, approximation tolerance, and hardware cost.

### Deeper Relationship Observations

1. A faster inner solver matters only when outer accuracy requirements are aligned; oversolving early majorizers can waste work, while loose late solves can invalidate convergence conditions.
2. Statistical oracle language and numerical stationarity are separate: an accurately solved local objective can still miss the support regime assumed by the theorem.
3. Sparsity is both a statistical prior and a linear-algebra resource; active-set shrinkage can reduce Newton-system cost, but reported nonzeros depend on threshold definitions.

### Conceptual Similarities

1. Sparse SSN-PMM and Noisy Poisson Inference use nonconvex sparsity penalties and local/stationary theoretical endpoints.
2. Sparse SSN-PMM and GPMD construct updates around regularizer-compatible proximal geometry and quantify inexact optimization.
3. Sparse SSN-PMM and CAP separate a structured inner optimization stage from a broader outer procedure with weaker global guarantees.

### MVP Implementations with Code Mock-Ups

1. **Iteration receipt**

```python
def receipt(k, objective, kkt, step, inner_residual, active):
    return {"iteration": k, "objective": objective, "kkt": kkt,
            "step_norm": step, "inner_residual": inner_residual,
            "active_features": active}
```

2. **Multistart comparison**

```python
def compare_runs(runs):
    return sorted(runs, key=lambda r: (r["kkt"] > 1e-6, r["validation_error"], r["nnz"]))
```

3. **Conservative stopping gate**

```python
def converged(history, kkt_tol=1e-6, step_tol=1e-8):
    if len(history) < 2:
        return False
    return history[-1]["kkt"] <= kkt_tol and history[-1]["step_norm"] <= step_tol
```

### Developer Challenges

1. Implementing generalized Jacobian products and sparse active-set linear solves without silent densification or ill-conditioning.
2. Coordinating inner tolerances, outer proximal parameters, line searches, and stopping rules so runtime gains do not break the inexact-convergence assumptions.
3. Reproducing dataset expansion, feature scaling, nonzero thresholds, cross-validation, and baseline termination on modern numerical libraries.

### Author Challenges

1. Separating benefits of the majorization geometry, warm start, SSN solver, sparse algebra, and parameter schedule through matched ablations.
2. Demonstrating robustness across seeds, heavy-tailed noise, correlated designs, high-dimension-low-sample regimes, and additional structured penalties.
3. Publishing implementation, environment, complete tables, convergence traces, and uncertainty sufficient for independent reproduction and modern baseline comparison.

## Validation Notes

- Deployment job ID: `BLAD-2200-20260719-7D93E819`.
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P03`.
- Random selection: uniform one-based index 47,418 of 75,776 candidate units; first draw accepted.
- Dedup validation: no arXiv ID, DOI, normalized-title, slug, artifact, memory, companion-repository, current-job, or preceding-24-hour same-paper marker; duplicate exclusions 0; reselections 0.
- Source validation: initial partial state repaired to verified complete with an approved ar5iv full-paper fallback after official HTML returned 404. PDF and HTML passed all byte, marker, structure, and truncation checks before synthesis.
- Cache validation: PDF, HTML, and source-package extraction all succeeded; cache status `cached`.
- Research depth: complete paper text, eight tables, algorithms, theorem statements/proofs, appendix/source, canonical metadata, and three related DEP manuscripts were inspected. No proof or experiment was independently reproduced.
- Related DEP count: exactly three.
- Synthesis cardinality: exactly three potential implementations, three deeper observations, three conceptual similarities, three code-mock MVPs, three developer challenges, and three author challenges.
- Public sanitization: passed subject to final pre-commit scan.
- Source locality: PDF, full-paper HTML, metadata HTML, source package, extracted text, and cache remain local. No `.source/` directory was created and no source file is eligible for staging.

## Attribution Block

- Source URL: https://arxiv.org/abs/1903.11460
  - Applies to: source identity, authors, dates, version, abstract, subjects, and DOI locator.
- Source URL: https://ar5iv.labs.arxiv.org/html/1903.11460
  - Applies to: complete full-paper rendering, method, theory, experiments, tables, conclusion, and appendix; source file withheld locally.
- Source URL: https://arxiv.org/pdf/1903.11460
  - Applies to: cross-format full-paper verification; source file withheld locally.
- Source URL: https://arxiv.org/e-print/1903.11460
  - Applies to: theorem, algorithm, table, and appendix cross-checks; source file withheld locally.
- Source URL: https://doi.org/10.48550/arXiv.1903.11460
  - Applies to: persistent paper identity.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Noisy%20Poisson%20Inference
  - Applies to: nonconvex sparse-regression synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL
  - Applies to: proximal regularization and approximate-convergence synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260719-CAP%20Rank%20Sparsity
  - Applies to: structured convex/heuristic stage synthesis.
- Source files: verified PDF, full-paper HTML fallback, metadata HTML, source package, extracted text, and processing cache.
  - Applies to: complete-paper review and integrity validation.
  - Notes: all source files were withheld locally; zero source documents were uploaded. Deployment context is job `BLAD-2200-20260719-7D93E819`, item `BLAD-2200-20260719-7D93E819-P03`.
