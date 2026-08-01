# DEP-E-20260801-SD Search Reasoning

#artificial-intelligence #search-augmented-reasoning #self-distillation #reinforcement-learning #retrieval #evaluation

Public-safe context: this DEP-E records a source-first review of arXiv:2605.18299v1, *SD-Search: On-Policy Hindsight Self-Distillation for Search-Augmented Reasoning*. The paper unit was randomly selected, found initially partial, repaired with a bounded public-arXiv archive workflow, and verified complete before synthesis. Local source locations, exact execution times, caches, extracted text, and source files are withheld.

## Contents

- `README.md` - public-safe inventory, context, insights, and attribution.
- `sd_search_reasoning_manuscript.md` - schema-complete manuscript covering the method, evidence, limitations, implementation paths, random selection, cache methodology, dedup validation, and related research.

No `.source/` directory is present. The verified PDF, full-paper HTML, metadata HTML, TeX/source package, extracted text, cache, and repair records remain local and were not deposited.

## Summary of Items

- `README.md` preserves the public submission boundary and explains why the paper matters for retrieval, policy optimization, and distributional training signals.
- `sd_search_reasoning_manuscript.md` reconstructs the hindsight-conditioned student/teacher design, token-level JSD objective, GRPO integration, seven-benchmark evaluation, ablations, five-seed evidence, compute cost, limitations, and bounded MVP implications.

## Insights and Relevance

SD-Search makes query-level credit assignment explicit: a rollout group becomes a training-time evidence object, future masking defines the leakage boundary, and the same policy supplies a privileged teacher distribution. The strongest downstream value is a testable bridge between retrieval evidence budgets, on-policy distribution alignment, and RL stability. The reported gains remain author-reported because no official implementation or independent reproduction was identified.

The deposit connects the paper to three existing Black-Lake records: Token Tax RAG for evidence-access cost, DASD Reasoning for divergence-aware distillation and train/inference mismatch, and GPMD Regularized RL for policy-objective stability. Source files were withheld locally and no public artifact contains operational search prompts, private data, model weights, caches, or executable training code.

## Attribution Block

- Source URL: https://arxiv.org/abs/2605.18299
  - Applies to: `sd_search_reasoning_manuscript.md` and this README.
  - Notes: canonical metadata, authors, date, abstract, subjects, DOI, and license link.
- Source URL: https://arxiv.org/html/2605.18299
  - Applies to: `sd_search_reasoning_manuscript.md`.
  - Notes: official full-paper method, results, ablations, limitations, and appendix evidence; source file withheld.
- Source URL: https://arxiv.org/pdf/2605.18299
  - Applies to: `sd_search_reasoning_manuscript.md`.
  - Notes: verified PDF inspected locally; source file withheld.
- Source URL: https://arxiv.org/e-print/2605.18299
  - Applies to: `sd_search_reasoning_manuscript.md`.
  - Notes: source-package cross-check; archive withheld locally.
- Source URL: https://doi.org/10.48550/arXiv.2605.18299
  - Applies to: persistent paper identity.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260727-Token%20Tax%20RAG/2606.20898-whitepaper-review.md
  - Applies to: related retrieval and evidence-budget synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260725-DASD%20Reasoning/dasd_reasoning_manuscript.md
  - Applies to: related distillation and rollout-mismatch synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md
  - Applies to: related RL objective and stability synthesis.
- Source files: verified local PDF, full-paper HTML, metadata HTML, TeX/source package, extracted text, cache, and repair records.
  - Applies to: source-first review only; all source files were withheld locally and zero source files were uploaded.
