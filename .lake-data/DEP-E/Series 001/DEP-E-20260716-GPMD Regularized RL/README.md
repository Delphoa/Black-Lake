# DEP-E-20260716-GPMD Regularized RL

**Title:** Generalized policy mirror descent review
**Tags:** reinforcement-learning, policy-optimization, mirror-descent, regularization, convergence, source-first-review

Public-safe context: on 2026-07-16, one local arXiv paper unit was selected uniformly from 75,776 unique PDF-parent units and accepted on the first draw after ID, DOI, normalized-title, slug, repository, memory, companion-repository, and 24-hour checks. Its valid PDF lacked full-paper HTML, so an approved ar5iv fallback repaired the unit and passed the mandatory integrity gate. No local path, exact execution timestamp, private cache, or source file appears here.

## Contents

- `gpmd_regularized_rl_manuscript.md` - schema-complete, source-grounded research manuscript.
- `README.md` - deposit context, inventory, synthesis, and attribution.

## Summary of Items

The manuscript reconstructs generalized policy mirror descent for convex, possibly nonsmooth regularizers in discounted tabular MDPs. It records the generalized Bregman/subgradient update, exact and bounded-error convergence claims, synthetic Tsallis/log-barrier experiments, publisher metadata, explicit limitations, random selection, deduplication, repair, cache behavior, and the no-source-upload gate.

## Insights and Relevance

GPMD's main result is a global linear convergence rate for regularized Q/value estimates for every positive learning rate without strong convexity or smoothness. Approximate evaluation and subproblem solutions retain that rate until an error floor. Policy convergence has a stronger convexity condition, and “dimension-free” describes iteration dependence rather than per-iteration state-action, evaluation, or sample cost.

The related deposits expose the next boundary. Mosaic Safety connects MDP signals to runtime monitoring and fallbacks; ConMax shows empirical policy optimization under composite proxy rewards and function approximation; the Black-Lake-Data distributional-RL audit shows learned risk claims can fail environment-ground-truth checks. Together they argue for theorem-aligned implementation tests plus objective-validity audits.

## Attribution Block

- Primary paper: *Policy Mirror Descent for Regularized Reinforcement Learning: A Generalized Framework with Linear Convergence*, Wenhao Zhan, Shicong Cen, Baihe Huang, Yuxin Chen, Jason D. Lee, and Yuejie Chi.
- arXiv: https://arxiv.org/abs/2105.11066v4
- Full paper: https://arxiv.org/pdf/2105.11066 and https://ar5iv.labs.arxiv.org/html/2105.11066
- Publisher: https://epubs.siam.org/doi/10.1137/21M1456789
- DOI: https://doi.org/10.1137/21M1456789 and https://doi.org/10.48550/arXiv.2105.11066
- This deposit is an independent review. Source files, metadata HTML, cache outputs, and extracted text were withheld locally and were not uploaded.
