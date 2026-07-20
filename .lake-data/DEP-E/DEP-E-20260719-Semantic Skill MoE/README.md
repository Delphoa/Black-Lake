# DEP-E-20260719-Semantic Skill MoE

#robotics #diffusion-policy #mixture-of-experts #semantic-routing #compositional-transfer #simulation #safety

Public-safe context: deployment job `BLAD-2200-20260719-7D93E819`, item `BLAD-2200-20260719-7D93E819-P08`, preserves a source-first review of arXiv:2605.23477v1. The local archive was repaired from partial to verified complete before review. Original sources and private execution context remain local.

## Contents

- `README.md` - DEP inventory, context, safety boundary, relevance, and attribution.
- `semantic_skill_moe_manuscript.md` - schema-complete manuscript covering offline semantic labels, skill-conditioned sparse routing, experiments, limits, and simulation-first implementation paths.

## Summary of Items

The manuscript reconstructs SMoDP's VLM-generated offline skill annotations, lightweight predictor, chunk-consistent expert routing, dual contrastive alignment, simulation benchmarks, few-shot transfer, 80 real-robot rollouts, ablations, and noise sensitivity. It separates source-reported success from reviewer requirements for annotation audit, rare-skill coverage, independent admissibility, failure severity, and physical safety.

## Insights and Relevance

Semantic skill structure can make sparse experts more reusable and interpretable, especially in low-data transfer. It cannot by itself decide whether an action is physically safe. DMNN adds route-stability evidence, LA-Pose adds latent-action transfer and rare-motion boundaries, and RRT-CBF adds explicit motion admissibility. The near-term artifact is therefore an offline simulator audit and safety-supervisor interface, not a deployable robot policy.

## Attribution Block

- Source URL: https://arxiv.org/abs/2605.23477
  - Applies to: `semantic_skill_moe_manuscript.md`
  - Notes: Canonical metadata, abstract, authorship, and submission history.
- Source URL: https://arxiv.org/html/2605.23477
  - Applies to: `semantic_skill_moe_manuscript.md`
  - Notes: Primary evidence for method, experiments, tables, appendices, and limitations.
- Source URL: https://arxiv.org/pdf/2605.23477
  - Applies to: `semantic_skill_moe_manuscript.md`
  - Notes: Validated complete PDF; withheld locally.
- Source URL: https://doi.org/10.48550/arXiv.2605.23477
  - Applies to: `README.md`, `semantic_skill_moe_manuscript.md`
  - Notes: Persistent identifier.
- Repository source: `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md`
  - Applies to: `semantic_skill_moe_manuscript.md`
  - Notes: Related conditional-routing evidence.
- Repository source: `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md`
  - Applies to: `semantic_skill_moe_manuscript.md`
  - Notes: Related latent-action evidence.
- Repository source: `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md`
  - Applies to: `semantic_skill_moe_manuscript.md`
  - Notes: Related safety-constrained motion evidence.
- Source files: PDF, HTML, metadata, extracted text, and caches were withheld locally; no `.source/` directory was created.
