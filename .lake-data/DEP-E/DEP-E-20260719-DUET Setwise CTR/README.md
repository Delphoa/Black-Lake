# DEP-E-20260719-DUET Setwise CTR

#recommender-systems #click-through-rate #pre-ranking #set-wise-modeling #co-training #pseudo-labels #industrial-ml

Public-safe context: deployment job `BLAD-2200-20260719-7D93E819`, item `BLAD-2200-20260719-7D93E819-P10`, preserves a source-first review of arXiv:2510.24369v1. A uniform first draw passed deduplication; its partial local unit was repaired with official full-paper HTML and verified complete. No source file or private execution context is redistributed.

## Contents

- `README.md` — DEP inventory, public-safe context, synthesis, and attribution.
- `duet_setwise_ctr_manuscript.md` — schema-complete manuscript covering set-level attention, dual-model co-training, offline/online evidence, limitations, and implementation paths.

## Summary of Items

The manuscript reconstructs DUET's candidate-history and candidate-candidate linear-attention streams, degree normalization, interactive soft pseudo-labeling, symmetric KL consistency, entire-space objective, 4,500-to-600 production pre-ranking architecture, two offline datasets, component ablations, and a two-week A/B test. It separates source-reported results from reviewer conclusions about calibration, shared error, privacy, drift, long-term welfare, and actual serving cost.

## Insights and Relevance

DUET is valuable as a combined modeling pattern: score a request as a set, learn from unexposed candidates, and serve only one model after peer training. Its ablation suggests co-training contributes more than either the set-wise module or KL term in the reported settings. The related MiNet, Adversarial Label Noise, and DMNN deposits expose the deployment boundary around candidate-conditioned interests, uncertain soft targets, and real hardware efficiency. A responsible implementation should begin in shadow mode with peer-disagreement, calibration, privacy, diversity, and tail-latency gates.

## Attribution Block

- Source URL: https://arxiv.org/abs/2510.24369
  - Applies to: `duet_setwise_ctr_manuscript.md`
  - Notes: Canonical metadata, abstract, authorship, and submission history.
- Source URL: https://arxiv.org/html/2510.24369
  - Applies to: `duet_setwise_ctr_manuscript.md`
  - Notes: Official full-paper HTML for method, experiments, tables, deployment description, and references.
- Source URL: https://arxiv.org/pdf/2510.24369
  - Applies to: `duet_setwise_ctr_manuscript.md`
  - Notes: Validated complete PDF; withheld locally.
- Source URL: https://doi.org/10.48550/arXiv.2510.24369
  - Applies to: `README.md`, `duet_setwise_ctr_manuscript.md`
  - Notes: Persistent identifier.
- Repository source: `.lake-data/DEP-E/DEP-E-20260719-MiNet CTR Transfer/minet_ctr_manuscript.md`
  - Applies to: `duet_setwise_ctr_manuscript.md`
  - Notes: Related industrial CTR and online-evaluation evidence.
- Repository source: `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md`
  - Applies to: `duet_setwise_ctr_manuscript.md`
  - Notes: Related soft-label reliability and calibration evidence.
- Repository source: `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md`
  - Applies to: `duet_setwise_ctr_manuscript.md`
  - Notes: Related conditional-compute and runtime evidence.
- Source files: PDF, official HTML, metadata, extracted text, and caches were withheld locally; no `.source/` directory was created.
