# DEP-E-20260804-RPDG Incremental Grad

#optimization #convex-optimization #finite-sum #incremental-gradient #primal-dual #randomized-algorithms #bregman

Public-safe DEP-E research deposit for *An optimal randomized incremental gradient method* by Guanghui Lan and Yi Zhou. The deposit reviews the complete paper, separates theorem statements from reviewer interpretation, and translates its finite-sum primal-dual mechanism into bounded evaluation and implementation ideas.

Original source documents and local verification material were withheld. No `.source/` directory was created, and no PDF, HTML, TeX/source archive, receipt, cache, rendering, or extracted source text is included.

## Contents

- `README.md` - DEP inventory, context, summary, insights, source-locality statement, and source attribution.
- `rpdg_incremental_gradient_manuscript.md` - schema-complete manuscript review with evidence ledger, claim map, methodology, limitations, implementation paths, exercise plans, MVP concept, related DEP synthesis, references, and validation appendix.

## Summary of Items

### `README.md`

Defines the DEP scope and makes the source-handling boundary explicit. It inventories every file in this DEP and annotates every public source URL used by the generated manuscript.

### `rpdg_incremental_gradient_manuscript.md`

Reviews the paper's deterministic primal-dual gradient method and randomized one-component extension. It preserves the authors' strongly convex upper bound, their model-specific lower bound, and their perturbation/smoothing extensions while highlighting initialization cost, stored per-component state, parameter knowledge, prox costs, and the absence of experiments or an official implementation.

## Insights and Relevance

The reusable idea is a separation of costs. RPDG reduces component-gradient evaluations by updating one dual component at a time, but it does not make initialization, proximal subproblems, per-component state, aggregation, parameter estimation, or verification disappear. The three related DEPs sharpen that lesson from different directions: Epsilon preserves proximal/affine structure to lower runtime costs that oracle counts omit; Local Stochastic Bilevel emphasizes stochastic-gradient complexity and variance reduction; and GPMD shows how regularizer-generated Bregman geometry yields convergence claims whose practical value still depends on evaluation accuracy. Together they motivate a gradient-budget laboratory that reports oracle calls, wall time, memory, prox work, and certificate quality rather than advertising a single asymptotic count.

## Attribution Block

- Source URL: https://arxiv.org/abs/1507.02000
  - Applies to: `rpdg_incremental_gradient_manuscript.md` and `README.md`.
  - Notes: Canonical title, authors, version history, subjects, abstract, and public source locators. Abstract metadata was not treated as the complete paper.
- Source URL: https://arxiv.org/pdf/1507.02000
  - Applies to: `rpdg_incremental_gradient_manuscript.md`.
  - Notes: Full method, algorithms, theorems, proofs, extensions, conclusion, and visual checks. The verified PDF remained local.
- Source URL: https://ar5iv.labs.arxiv.org/html/1507.02000
  - Applies to: `rpdg_incremental_gradient_manuscript.md`.
  - Notes: Approved full-paper HTML fallback used for searchable cross-checking. The file remained local.
- Source URL: https://arxiv.org/e-print/1507.02000
  - Applies to: `rpdg_incremental_gradient_manuscript.md` source-status record.
  - Notes: The bounded acquisition attempt did not produce a source package.
- Source URL: https://doi.org/10.48550/arXiv.1507.02000
  - Applies to: `rpdg_incremental_gradient_manuscript.md` and `README.md`.
  - Notes: Persistent arXiv identity.
- Source URL: https://doi.org/10.1007/s10107-017-1173-0
  - Applies to: `rpdg_incremental_gradient_manuscript.md` and `README.md`.
  - Notes: Published article identity in Mathematical Programming.
- Source URL: https://optimization-online.org/?p=13502
  - Applies to: `rpdg_incremental_gradient_manuscript.md`.
  - Notes: Author-deposited technical-report context and update record.
- Source URL: https://dblp.org/rec/journals/mp/LanZ18
  - Applies to: `rpdg_incremental_gradient_manuscript.md`.
  - Notes: Bibliographic cross-check for venue, volume, pages, and year.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260730-Epsilon%20Prox%20Affine/epsilon_prox_affine_manuscript.md
  - Applies to: `rpdg_incremental_gradient_manuscript.md` related-DEP analysis.
  - Notes: Proximal-operator and structure-preserving solver relationship; processed research artifact only.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260728-Local%20Stochastic%20Bilevel/local_stochastic_bilevel_manuscript.md
  - Applies to: `rpdg_incremental_gradient_manuscript.md` related-DEP analysis.
  - Notes: Stochastic-gradient complexity and variance-reduction relationship; processed research artifact only.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md
  - Applies to: `rpdg_incremental_gradient_manuscript.md` related-DEP analysis.
  - Notes: Bregman geometry and convergence relationship; processed research artifact only.
