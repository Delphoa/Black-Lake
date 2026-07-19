# DEP-E-20260719-CAP Rank Sparsity

#llm #model-compression #low-rank #sparsity #pruning #rpca #resource-allocation #inference #research

DEP class: DEP-E

Deposition date: 2026-07-19

Subject title: Large Language Model Compression with Global Rank and Sparsity Optimization

This public-safe DEP-E entry preserves a source-grounded review of arXiv:2505.03801v3, an ICLR 2026 poster paper. The selected archive unit passed the mandatory complete-source gate after missing full-paper HTML was repaired. Original PDF, HTML, metadata, TeX/source, rendered pages, caches, and verification records remain in the private local archive and are not included here.

## Contents

- `README.md`
  - DEP inventory, public-safe context, item summaries, synthesis relevance, and final source attribution.
- `cap_rank_sparsity_manuscript.md`
  - Schema-complete manuscript covering CAP's RPCA decomposition, probabilistic global resource allocation, reported results, evidence limits, implementation paths, selection/dedup evidence, exactly three related DEP entries, and the local source-integrity receipt.

No `.source/` directory is present because source deposition and redistribution were not authorized.

## Summary of Items

### `README.md`

This file records what was deposited and why, states the source-locality boundary, and maps every public source URL to the generated manuscript. It is the entry point for downstream reviewers and agents.

### `cap_rank_sparsity_manuscript.md`

The manuscript reviews CAP, a two-stage method that decomposes each LLM weight matrix into low-rank and sparse components through robust principal component analysis, then learns global Bernoulli retention probabilities under a parameter budget. It preserves the paper's comparative results, calibration and hardware conditions, appendix ablations, and stated hardware limitation. It also records reviewer-identified gaps in statistical reporting, implementation availability, and the cost accounting used when rank directions and sparse entries compete for one budget. No experiment was rerun.

## Insights and Relevance

CAP's durable contribution is a structured decision surface: first separate global low-rank structure from sparse local refinements, then allocate capacity globally instead of applying uniform layer thresholds. The three related DEP entries make that idea more operational. The Efficient FM Survey locates low-rank decomposition and pruning within a full model-to-system efficiency lifecycle; STAR-KV shows that adaptive rank allocation needs compatible kernels before nominal compression becomes throughput; QUOTA shows why two compression mechanisms should be optimized jointly under a shared sensitivity budget. Together they motivate cost-aware allocation, matched-budget evaluation, and runtime-specific acceptance gates rather than headline compression ratios alone.

## Attribution Block

- Source URL: https://arxiv.org/abs/2505.03801
  - Applies to: `cap_rank_sparsity_manuscript.md`.
  - Notes: Canonical metadata, authors, version history, subjects, DOI, license, and artifact locators.
- Source URL: https://arxiv.org/pdf/2505.03801
  - Applies to: `cap_rank_sparsity_manuscript.md`.
  - Notes: Public equivalent of the verified local PDF used for full-paper and visual review; not redistributed.
- Source URL: https://arxiv.org/html/2505.03801
  - Applies to: `cap_rank_sparsity_manuscript.md`.
  - Notes: Official full-paper HTML used for method, result, limitation, and appendix inspection; not redistributed.
- Source URL: https://arxiv.org/e-print/2505.03801
  - Applies to: `cap_rank_sparsity_manuscript.md`.
  - Notes: TeX/source package used locally for equations, tables, appendices, and bibliography checks; not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2505.03801
  - Applies to: `cap_rank_sparsity_manuscript.md`.
  - Notes: Persistent arXiv DOI.
- Source URL: https://iclr.cc/virtual/2026/poster/10008795
  - Applies to: `cap_rank_sparsity_manuscript.md`.
  - Notes: Official ICLR 2026 poster listing and author attribution.
- Source URL: https://openreview.net/forum?id=ZaPmQ0NHs4
  - Applies to: `cap_rank_sparsity_manuscript.md`.
  - Notes: Official OpenReview forum locator; interactive review content was challenge-gated during inspection.
- Source URL: https://qianqiaoai.github.io/
  - Applies to: `cap_rank_sparsity_manuscript.md`.
  - Notes: Author-maintained publication context; no result claim imported and no code link was shown for this paper.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`, `cap_rank_sparsity_manuscript.md`.
  - Notes: Live repository authority for layout, naming, attribution, source locality, and submission.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md`, `cap_rank_sparsity_manuscript.md`.
  - Notes: Live DEP-E filing and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `cap_rank_sparsity_manuscript.md`.
  - Notes: Live companion-repository authority read before deduplication and related-context use.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Efficient%20FM%20Survey/efficient_fm_survey_manuscript.md
  - Applies to: `cap_rank_sparsity_manuscript.md`.
  - Notes: Related DEP entry for the architecture-algorithm-system efficiency taxonomy.
- Source URL: https://arxiv.org/abs/2401.08092
  - Applies to: `cap_rank_sparsity_manuscript.md`.
  - Notes: Primary paper reviewed by the Efficient FM Survey DEP.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-STAR-KV%20Ranks/2606.08382-whitepaper-review.md
  - Applies to: `cap_rank_sparsity_manuscript.md`.
  - Notes: Related DEP entry for adaptive low-rank allocation and kernel realization.
- Source URL: https://arxiv.org/abs/2606.08382v1
  - Applies to: `cap_rank_sparsity_manuscript.md`.
  - Notes: Primary paper reviewed by the STAR-KV Ranks DEP.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-QUOTA%20Joint%20Compression/2604.17320-whitepaper-review.md
  - Applies to: `cap_rank_sparsity_manuscript.md`.
  - Notes: Related DEP entry for joint compression allocation under a shared budget.
- Source URL: https://arxiv.org/abs/2604.17320v1
  - Applies to: `cap_rank_sparsity_manuscript.md`.
  - Notes: Primary paper reviewed by the QUOTA Joint Compression DEP.
