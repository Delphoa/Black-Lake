# DEP-E-20260730-Epsilon Prox Affine

#convex-optimization #proximal-operators #operator-splitting #optimization-compilers #scientific-computing

DEP class: `DEP-E`

Subject title: Convex programming with fast proximal and linear operators

Public-safe context: This deposit records a source-first review of arXiv `1511.04815v1`. The selected local archive unit initially lacked full-paper HTML, so review paused until a bounded repair produced verified complete HTML and refreshed private provenance records. All original and extracted source files remain local; exact local paths, execution time, timezone, and machine identity are withheld.

## Contents

- `README.md`
  - DEP inventory, public-safe context, item summaries, insights, source policy, and attribution.
- `epsilon_prox_affine_manuscript.md`
  - Schema-complete manuscript review covering the Epsilon prox-affine intermediate representation, compiler passes, ADMM-based solver, operator library, numerical evidence, limitations, and implementation paths.

No `.source/` directory is present. The PDF, full-paper HTML, metadata HTML, TeX/source package, extracted material, validation records, and page renders were inspected locally and were not uploaded.

## Summary of Items

`epsilon_prox_affine_manuscript.md` preserves the paper's identity, evidence ledger, mechanism, compiler/solver architecture, benchmark results, claim boundaries, source-integrity repair, random selection and dedup methodology, three related DEP bridges, implementation proposals, safe exercises, an MVP concept, and a reproduction-oriented appendix. It separates author claims from reviewer interpretation and does not represent the 2015 benchmarks as independently reproduced or current production performance.

## Insights and Relevance

Epsilon's durable idea is not merely "use ADMM." It is to retain problem structure in a richer compiler intermediate representation so that specialized proximal and linear operators remain available to a generic solver. The three related DEP entries show the same design pattern at different scales: SSN-PMM exposes a differentiable dual for a specialized inner solve, CAP maps a convex decomposition to thresholding operators under ADMM, and GPMD makes the regularizer itself define update geometry. Together they suggest an optimization-runtime design centered on typed atoms, transformation receipts, operator compatibility, and residual-aware validation. The transfer boundary is substantial: the paper reports strong source-era speedups, but lacks disclosed hardware, seeds, repeated-run uncertainty, modern baselines, and a currently accessible implementation in this review.

## Attribution Block

- Source URL: https://arxiv.org/abs/1511.04815
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: Canonical metadata, authors, version, abstract context, and source locators. The abstract page was not treated as full-paper evidence.
- Source URL: https://arxiv.org/pdf/1511.04815
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: Complete PDF inspected locally; source file withheld.
- Source URL: https://ar5iv.labs.arxiv.org/html/1511.04815
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: Approved full-paper HTML fallback inspected after the official HTML endpoint was unavailable; local copy withheld.
- Source URL: https://arxiv.org/e-print/1511.04815
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: TeX/source package inspected locally for equations, benchmark table, and conclusion; source archive withheld.
- Source URL: https://doi.org/10.48550/arXiv.1511.04815
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: Persistent arXiv-issued DOI.
- Source URL: https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: License record visible from the canonical arXiv entry; it does not authorize source upload by this automation.
- Source URL: https://zicokolter.com/publications/
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: Author-maintained publication record confirming the preprint and linking Epsilon software.
- Source URL: https://github.com/mwytock/epsilon
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: Paper-linked implementation locator; inaccessible during this review, so code was not inspected or executed.
- Source URL: https://proceedings.mlr.press/v48/wangh16.html
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: Primary proceedings record for the authors' follow-up on epigraph projections.
- Source URL: https://web.stanford.edu/~boyd/papers/admm_distr_stats.html
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: Primary author-hosted ADMM reference used for methodological context.
- Source URL: https://web.stanford.edu/~boyd/papers/prox_algs.html
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: Primary author-hosted proximal-algorithms reference.
- Source URL: https://web.stanford.edu/~boyd/papers/block_splitting.html
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: Primary author-hosted graph-form and block-splitting reference.
- Source URL: https://arxiv.org/abs/1705.00772
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: Primary arXiv record for a semismooth Newton follow-up on generic convex programming.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260719-Sparse%20SSN%20PMM/sparse_ssn_pmm_manuscript.md
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: Related DEP evidence for prox-structured semismooth Newton optimization.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260719-CAP%20Rank%20Sparsity/cap_rank_sparsity_manuscript.md
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: Related DEP evidence for ADMM, singular-value thresholding, and sparse thresholding.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md
  - Applies to: `epsilon_prox_affine_manuscript.md`
  - Notes: Related DEP evidence for convex regularizer geometry and generalized Bregman updates.
