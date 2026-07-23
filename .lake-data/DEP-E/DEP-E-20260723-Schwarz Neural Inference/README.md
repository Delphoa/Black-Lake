# DEP-E-20260723-Schwarz Neural Inference

**Tags:** #neural-operators #pde-solving #domain-decomposition #geometry-generalization #scientific-machine-learning #numerical-analysis #research-review

This DEP-E package contains a public-safe, source-first review of *Operator Learning with Domain Decomposition for Geometry Generalization in PDE Solving*. It focuses on Schwarz Neural Inference, the reported geometry-transfer evidence, the boundary between error reduction and computational advantage, the convergence theorem's assumptions and proof gap, and implementation evidence from the official repository. A verified local PDF, official full-paper HTML, and TeX/source package were inspected before synthesis. All original source files, extracted text, caches, provenance records, and inspection renders were withheld locally and were not uploaded.

## Contents

- `README.md` - package inventory, context, summary, relevance, and attribution.
- `schwarz_neural_inference_manuscript.md` - schema-complete research manuscript with an evidence ledger, critical review, implementation paths, MVP design, related research, and source references.

No `.source/` directory is included because the source-paper integrity gate requires original paper files and derived extraction caches to remain local.

## Summary of Items

The manuscript records a uniform random selection from 75,777 paper units, a no-collision dedup check, a partial-to-complete archive repair, and a cache miss-to-cached extraction. It reconstructs the local-operator training and additive-Schwarz-style inference loop, checks the main error table, examines the runtime appendix, records the official code revision, and distinguishes a valid uniform tracking bound from the proof's unsupported convergence conclusion.

## Insights and Relevance

SNI is strong evidence that domain decomposition can improve the geometry transfer of a local neural operator on the paper's tested two-dimensional problems. It is not yet evidence of computational acceleration: the paper's own small-domain benchmark reports SNI far slower than both optimized FEM and direct GNOT, even after improved initialization. The practical opportunity is therefore an auditable hybrid solver that reports equation scope, partition quality, subdomain shift, interface residuals, iteration behavior, matched-error cost, and classical fallback.

The review connects SNI to exactly three existing DEP-E deposits: Physical Data AI for PDE-prior/domain-fit reasoning, Global NS Existence for theorem and boundary-assumption discipline, and FGLE Midpoint Scheme for numerical convergence, solver, reference-error, and runtime separation.

## Attribution Block

Primary research: Jianing Huang, Kaixuan Zhang, Youjia Wu, and Ze Cheng, *Operator Learning with Domain Decomposition for Geometry Generalization in PDE Solving*, ICLR 2026, [arXiv:2504.00510](https://arxiv.org/abs/2504.00510), [DOI:10.48550/arXiv.2504.00510](https://doi.org/10.48550/arXiv.2504.00510), [official ICLR record](https://iclr.cc/virtual/2026/poster/10010246), and [official code repository](https://github.com/questionstorer/sni). This DEP-E package is an independent research review and does not imply author endorsement. Source documents remain under their original terms, were retained locally, and were not uploaded or redistributed.
