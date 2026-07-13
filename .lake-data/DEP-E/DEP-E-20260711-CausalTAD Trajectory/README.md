# CausalTAD Trajectory

#arxiv #trajectory-anomaly-detection #causal-inference #out-of-distribution #spatial-ai #road-networks #online-detection #black-lake

Public-safe DEP-E context: this entry preserves a source-grounded review of arXiv:2412.18820v1, "CausalTAD: Causal Implicit Generative Model for Debiased Online Trajectory Anomaly Detection." The review focuses on causal adjustment for road-preference bias, ID/OOD trajectory evaluation, online scoring, empirical limits, reproducibility, and related Black-Lake evidence. No local source files are redistributed.

## Contents

- `README.md`: DEP inventory, public-safe context, summary, relevance, and provenance.
- `causaltad_trajectory_manuscript.md`: Schema-complete manuscript research artifact for the selected paper.

## Summary of Items

- `README.md` records the deposit scope, tags, file inventory, source policy, and final attribution needed for durable review.
- `causaltad_trajectory_manuscript.md` provides source metadata, an evidence ledger, detailed method/results analysis, limitations, implementation paths, an MVP concept, related DEP synthesis, and a replication checklist.

## Insights and Relevance

CausalTAD is relevant to Black-Lake because it shows how a seemingly reasonable anomaly likelihood can encode spurious route-popularity structure and fail on unseen source-destination pairs. Its proposed correction joins causal inference, variational generative modeling, road-network constraints, and constant-time online updates. The paper reports strong ID and OOD gains, but the evidence remains bounded by synthetic anomaly labels, a static road-preference assumption, unreproduced experiments, and a dataset-description mismatch between the paper and public code README. The deposit therefore preserves both the technical contribution and the verification work still required.

## Attribution Block

- Source URL: https://arxiv.org/abs/2412.18820
  - Applies to: `causaltad_trajectory_manuscript.md`
  - Notes: Primary metadata, abstract, authors, version, DOI, and venue comment.
- Source URL: https://arxiv.org/html/2412.18820
  - Applies to: `causaltad_trajectory_manuscript.md`
  - Notes: Public full-text HTML used for method and result review.
- Source URL: https://arxiv.org/e-print/2412.18820
  - Applies to: `causaltad_trajectory_manuscript.md`
  - Notes: Public TeX source package used for table- and limitation-level inspection; not redistributed.
- Source URL: https://arxiv.org/pdf/2412.18820
  - Applies to: `causaltad_trajectory_manuscript.md`
  - Notes: Canonical public PDF reference; the PDF is not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2412.18820
  - Applies to: `causaltad_trajectory_manuscript.md`
  - Notes: Persistent arXiv DOI.
- Source URL: https://github.com/LwbXc/CausalTAD
  - Applies to: `causaltad_trajectory_manuscript.md`
  - Notes: Author code repository README used for implementation and reproducibility context; no repository files were collected.
- Repository path: `.lake-data/DEP-E/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md`
  - Applies to: related road-system and online-decision synthesis.
  - Notes: Existing Black-Lake DEP manuscript inspected.
- Repository path: `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md`
  - Applies to: related debiasing and distribution-shift synthesis.
  - Notes: Existing Black-Lake DEP manuscript inspected.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260707-Tech%20Intel%201103/daily_research_findings_2026-07-07_1103.md
  - Applies to: related structure-aware spatial evaluation synthesis.
  - Notes: Existing Black-Lake-Data DEP finding inspected.
