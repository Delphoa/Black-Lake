# DEP-E-20260719-Sparse SSN PMM

#optimization #sparse-regression #semismooth-newton #majorization-minimization #square-root-lasso #nonconvex-regularization #numerical-methods

Public-safe deposition context: `Black Lake Arxiv DEP 2200 x10` job `BLAD-2200-20260719-7D93E819`, item `BLAD-2200-20260719-7D93E819-P03`, uniformly selected and source-first reviewed arXiv:1903.11460v3. The archive unit was repaired from partial to verified complete before synthesis. Local source locations, exact execution times, and all source files are withheld.

## Contents

- `README.md` - inventory, context, summary, source policy, and attribution.
- `sparse_ssn_pmm_manuscript.md` - schema-complete research manuscript covering the two-stage PMM, semismooth Newton dual solver, oracle and convergence results, experiments, limitations, implementation paths, selection/dedup process, integrity gate, and related DEP synthesis.

No `.source/` directory is present. The paper PDF, full-paper HTML fallback, metadata HTML, source package, extracted text, and processing cache remain local and were not deposited.

## Summary of Items

`sparse_ssn_pmm_manuscript.md` reviews a nonsmooth nonconvex square-root regression method that first solves a proximal convex warm-start problem, then linearizes the concave penalty component and solves convex majorizers. An added fitted-value proximal term exposes a differentiable dual, allowing a sparse semismooth Newton inner solver. The manuscript preserves the oracle inequality, d-stationarity and KL-rate boundaries, eight-table numerical study, and distinctions among objective, KKT residual, runtime, sparsity, prediction, and support recovery.

The artifact also records the uniform random draw, cross-repository dedup result, bounded approved-fallback repair, complete-source integrity metrics, cache status, and zero-source-upload gate. It connects the paper to exactly three inspected entries: Noisy Poisson Inference, GPMD Regularized RL, and CAP Rank Sparsity.

## Insights and Relevance

The transferable contribution is the choice of proximal geometry: a carefully added term can turn a difficult primal majorizer into an explicit dual whose generalized Hessian exposes sparse structure. The main caution is that different guarantees attach to different layers. Inner dual convergence, outer d-stationarity, a conditional oracle inequality, and empirical runtime are not interchangeable. Reproduction should preserve residuals, active sets, inner tolerances, outer steps, data transformations, and multi-metric outcomes.

## Source and Distribution Policy

- Source state: verified complete after bounded local repair with approved ar5iv fallback.
- Source documents: withheld locally.
- Public deposit: generated Markdown plus required repository indexes only.
- `.source/`: not created.
- Source uploads: zero.
- Deployment job ID: `BLAD-2200-20260719-7D93E819`.
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P03`.

## Attribution Block

- Source URL: https://arxiv.org/abs/1903.11460
  - Applies to: canonical identity, authors, version, dates, abstract, and DOI locator.
- Source URL: https://ar5iv.labs.arxiv.org/html/1903.11460
  - Applies to: full-paper content in `sparse_ssn_pmm_manuscript.md`.
  - Notes: Approved fallback after official HTML returned 404; verified local file withheld.
- Source URL: https://arxiv.org/pdf/1903.11460
  - Applies to: cross-format full-paper verification; source file withheld.
- Source URL: https://arxiv.org/e-print/1903.11460
  - Applies to: theorem, algorithm, table, and appendix cross-checks; source package withheld.
- Source URL: https://doi.org/10.48550/arXiv.1903.11460
  - Applies to: persistent paper identity.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Noisy%20Poisson%20Inference
  - Applies to: related nonconvex sparse-regression analysis.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL
  - Applies to: related proximal regularization and approximation analysis.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260719-CAP%20Rank%20Sparsity
  - Applies to: related structured optimization and stage-boundary analysis.
- Source files: verified PDF, full-paper HTML fallback, metadata HTML, source package, extracted text, and processing cache.
  - Applies to: source-first review and integrity validation.
  - Notes: All source files were withheld locally; zero source documents were uploaded. Deployment context is job `BLAD-2200-20260719-7D93E819`, item `BLAD-2200-20260719-7D93E819-P03`.
