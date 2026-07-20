# DEP-E-20260719-MiNet CTR Transfer

#recommender-systems #click-through-rate #cross-domain-learning #attention #behavioral-data #privacy #online-evaluation

Public-safe context: deployment job `BLAD-2200-20260719-7D93E819`, item `BLAD-2200-20260719-7D93E819-P07`, preserves a source-first review of arXiv:2008.02974v1. The first random unit failed the complete-source gate and was privately rejected; this replacement passed after an approved ar5iv repair. No original source or private execution context is redistributed.

## Contents

- `README.md` - DEP inventory, context, relevance, and attribution.
- `minet_ctr_manuscript.md` - schema-complete manuscript covering model design, offline/online evidence, limitations, privacy, and implementation paths.

## Summary of Items

The manuscript reconstructs MiNet's long-term cross-domain, short-term source, and short-term target interest signals; item- and interest-level attention; joint learning; two offline datasets; attention/component ablations; and a source-reported production A/B test. It separates architecture and reported results from reviewer conclusions about calibration, privacy, route drift, causal interpretation, and long-term outcomes.

## Insights and Relevance

MiNet demonstrates a reusable pattern: fuse persistent and recent signals from multiple domains while allowing the candidate to control their weights. Its own ablation shows that component usefulness changes by dataset. The related OViP, DMNN, and XPRINT deposits sharpen the deployment boundary around feedback loops, conditional routing, and the privacy of behavior sequences. A responsible implementation should begin with frozen offline evaluation and privacy-minimized telemetry, not direct targeting.

## Attribution Block

- Source URL: https://arxiv.org/abs/2008.02974
  - Applies to: `minet_ctr_manuscript.md`
  - Notes: Canonical metadata, abstract, authorship, and submission history.
- Source URL: https://ar5iv.labs.arxiv.org/html/2008.02974
  - Applies to: `minet_ctr_manuscript.md`
  - Notes: Approved full-paper HTML fallback for method, experiments, tables, ablations, deployment report, and references.
- Source URL: https://arxiv.org/pdf/2008.02974
  - Applies to: `minet_ctr_manuscript.md`
  - Notes: Validated complete PDF; withheld locally.
- Source URL: https://doi.org/10.48550/arXiv.2008.02974
  - Applies to: `README.md`, `minet_ctr_manuscript.md`
  - Notes: Persistent identifier.
- Repository source: `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md`
  - Applies to: `minet_ctr_manuscript.md`
  - Notes: Related preference and feedback-loop evidence.
- Repository source: `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md`
  - Applies to: `minet_ctr_manuscript.md`
  - Notes: Related routing and runtime evidence.
- Repository source: `.lake-data/DEP-E/DEP-E-20260716-XPRINT Traffic Privacy/xprint_traffic_privacy_manuscript.md`
  - Applies to: `minet_ctr_manuscript.md`
  - Notes: Related behavioral privacy evidence.
- Source files: PDF, fallback HTML, metadata, extracted text, and caches were withheld locally; no `.source/` directory was created.
