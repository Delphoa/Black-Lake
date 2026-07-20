# DEP-E-20260720-AR-Drag Motion

#video-generation #autoregressive-video #diffusion-models #motion-control #reinforcement-learning #grpo #kv-cache #synthetic-media #research

DEP class: DEP-E

Deposition date: 2026-07-20

Subject title: Real-Time Motion-Controllable Autoregressive Video Diffusion

## Public-Safe Context

This DEP-E entry preserves a source-grounded review of arXiv:2510.08131v3, an ICLR 2026 poster paper. The randomly selected archive unit initially had a complete PDF but no full-paper HTML. Review paused while a bounded repair preserved the valid PDF, acquired official full-paper HTML and companion metadata/source artifacts, and passed the complete-source gate. All PDF, HTML, metadata, TeX/source, extracted text, renders, caches, and verification records remain local and are not included here.

## Contents

- `README.md`
  - DEP inventory, public-safe context, item summaries, relevance notes, and final attribution.
- `ar_drag_motion_manuscript.md`
  - Schema-complete manuscript covering AR-Drag's motion-conditioned distillation, Self-Rollout, GRPO, selective stochasticity, reward design, experiments, limitations, random selection, deduplication, source integrity, implementation paths, and related research.

No `.source/` directory is present because source upload and redistribution were not authorized.

## Summary of Items

### `README.md`

This file records the DEP identity and source-locality boundary, inventories all public files, and maps the public sources and exactly three related DEP entries to the generated manuscript.

### `ar_drag_motion_manuscript.md`

The manuscript reviews a 1.3B-parameter frame-wise autoregressive video diffusion model. AR-Drag first learns motion conditioning in a bidirectional teacher, distills a three-step causal student, and uses Self-Rollout so later frames train on fully generated model history. It then applies GRPO with one selectively stochastic denoising step and a composite aesthetic/trajectory reward.

On the paper's 206-clip author-curated benchmark, Table 1 reports 0.44-second first-frame latency on one H20, FID 28.98, FVD 187.49, aesthetic quality 4.07, motion smoothness 0.9948, and motion consistency 4.37. These are author-reported point estimates. The manuscript preserves the teacher tradeoff, RL and Self-Rollout ablations, evaluator dependence, physical-plausibility limitation, incomplete data provenance, narrow latency boundary, safety concerns, and missing independent reproduction.

## Insights and Relevance

AR-Drag's durable idea is to repair the training transition graph before optimizing it: model-generated history becomes causal context, and stochastic exploration is limited to keep long-horizon policy gradients tractable. VideoWeave shows a parallel training-time transfer of geometry structure into a few-step generator. PackForcing and ISPA expose the next systems boundary: autoregressive history must also be governed as a bounded, auditable resource. Together, these records suggest a research agenda that evaluates motion quality, geometry, cache state, latency, privacy, and long-stream failure on one controlled frontier.

The entry is useful for benchmark design and product gating, not as proof of production readiness. Any implementation should use consented media, independent motion evaluators, end-to-end latency traces, session-isolated caches, provenance/disclosure controls, repeated-run uncertainty, and explicit fallbacks for invalid or non-physical trajectories.

## Attribution Block

- Source URL: https://arxiv.org/abs/2510.08131
  - Applies to: `ar_drag_motion_manuscript.md`.
  - Notes: Official title, authors, version history, subject, DOI, license, abstract, and source locators.
- Source URL: https://arxiv.org/html/2510.08131
  - Applies to: `ar_drag_motion_manuscript.md`.
  - Notes: Official full-paper source for method, equations, algorithms, experiments, results, ablations, limitations, ethics, and appendix.
- Source URL: https://arxiv.org/pdf/2510.08131
  - Applies to: `ar_drag_motion_manuscript.md`.
  - Notes: Canonical PDF used for visual verification of tables, figures, algorithms, and layout; file withheld locally.
- Source URL: https://arxiv.org/e-print/2510.08131
  - Applies to: `ar_drag_motion_manuscript.md`.
  - Notes: TeX/source locator used for local source inspection; archive withheld locally.
- Source URL: https://doi.org/10.48550/arXiv.2510.08131
  - Applies to: `README.md`, `ar_drag_motion_manuscript.md`.
  - Notes: arXiv-issued DOI.
- Source URL: https://kesenzhao.github.io/AR-Drag.github.io/
  - Applies to: `ar_drag_motion_manuscript.md`.
  - Notes: Official project page for pipeline and qualitative/streaming context; no result was independently reproduced.
- Source URL: https://iclr.cc/virtual/2026/poster/10011557
  - Applies to: `README.md`, `ar_drag_motion_manuscript.md`.
  - Notes: Official ICLR 2026 Poster record.
- Source URL: https://openreview.net/forum?id=4Q55RwYte9
  - Applies to: `ar_drag_motion_manuscript.md`.
  - Notes: OpenReview forum locator; interactive content was challenge-gated.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`, `ar_drag_motion_manuscript.md`.
  - Notes: Live repository authority for layout, attribution, source locality, and submission.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md`, `ar_drag_motion_manuscript.md`.
  - Notes: Live DEP-E filing and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `ar_drag_motion_manuscript.md`.
  - Notes: Live companion-repository authority used for context and deduplication.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md
  - Applies to: `ar_drag_motion_manuscript.md`.
  - Notes: Related DEP entry for geometry-aware few-step video diffusion.
- Source URL: https://arxiv.org/abs/2606.14162
  - Applies to: `ar_drag_motion_manuscript.md`.
  - Notes: Primary paper reviewed by the VideoWeave DEP.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-PackForcing%20Video/2603.25730-whitepaper-review.md
  - Applies to: `ar_drag_motion_manuscript.md`.
  - Notes: Related DEP entry for bounded autoregressive-video KV history.
- Source URL: https://arxiv.org/abs/2603.25730v1
  - Applies to: `ar_drag_motion_manuscript.md`.
  - Notes: Primary paper reviewed by the PackForcing DEP.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-ISPA%20Video%20Memory/2607.00712-whitepaper-review.md
  - Applies to: `ar_drag_motion_manuscript.md`.
  - Notes: Related DEP entry for instance-specific absorption of autoregressive-video history.
- Source URL: https://arxiv.org/abs/2607.00712v1
  - Applies to: `ar_drag_motion_manuscript.md`.
  - Notes: Primary paper reviewed by the ISPA DEP.
- Source-file policy:
  - Applies to: the complete DEP entry.
  - Notes: No PDF, HTML, metadata, source archive, extracted text, render, cache, verification record, or `.source/` directory was uploaded or committed.
