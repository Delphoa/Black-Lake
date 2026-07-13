# DEP-E-20260713-LA-Pose Latent Action

#camera-pose #latent-actions #self-supervised-learning #autonomous-driving #video-pretraining #3d-vision

This public-safe DEP-E deposit reviews LA-Pose, a two-stage framework that learns latent actions from unlabeled driving video and reuses those representations for metric camera-pose estimation with limited labeled 3D data. The deposit separates source-reported evidence from reviewer interpretation and records the method, benchmark results, limitations, related Black-Lake artifacts, and bounded implementation paths.

## Contents

- `README.md` — deposition context, complete inventory, item summaries, insights, and source attribution.
- `la_pose_latent_action_manuscript.md` — schema-complete source-first manuscript review, evidence ledger, claims map, methodology, implementation translations, MVP, and replication notes.

No `.source/` directory is included. A private archive PDF was inspected but not collected for redistribution; public equivalents are linked below.

## Summary of Items

- `README.md` makes the package auditable by naming every deposited item, clarifying the source policy, and preserving public source URLs.
- `la_pose_latent_action_manuscript.md` reviews arXiv:2604.27448 and the official project page. It covers inverse/forward-dynamics pretraining, the pose head, training data and compute, Waymo and PandaSet evaluation, ablations, rare-motion failures, evidence limitations, and downstream evaluation concepts.

## Insights and Relevance

LA-Pose is notable because it treats inverse-dynamics latent actions as a geometry representation rather than only as a control or generation interface. Its reported results suggest that motion structure learned from raw video can reduce dependence on labeled 3D data, while its ablations warn that larger latent spaces and end-to-end fine-tuning can weaken transfer or out-of-distribution generalization. The related HERMES, VideoWeave, and Self Learned IDC deposits place this result in a broader design space spanning world models, geometry-aware video latents, learned driving-state representations, and the need for coverage-aware evaluation before deployment.

## Attribution Block

- Source URL: https://arxiv.org/abs/2604.27448
  - Applies to: `la_pose_latent_action_manuscript.md`
  - Notes: Primary arXiv metadata, abstract, authors, identifier, and submission date.
- Source URL: https://arxiv.org/pdf/2604.27448
  - Applies to: `la_pose_latent_action_manuscript.md`
  - Notes: Public equivalent of the primary paper PDF inspected for method, experiments, tables, limitations, and supplementary material.
- Source URL: https://doi.org/10.48550/arXiv.2604.27448
  - Applies to: `la_pose_latent_action_manuscript.md`
  - Notes: Stable arXiv DOI marker.
- Source URL: https://la-pose.github.io/
  - Applies to: `la_pose_latent_action_manuscript.md`
  - Notes: Official project page used for method presentation, authorship, CVPR 2026 citation, interactive latent-space description, and public demos.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model/hermes_world_model_manuscript.md
  - Applies to: `la_pose_latent_action_manuscript.md`
  - Notes: Related processed artifact on driving world models and geometry-aware future prediction.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md
  - Applies to: `la_pose_latent_action_manuscript.md`
  - Notes: Related processed artifact on latent geometry guidance for video generation.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Self%20Learned%20IDC/self_learned_idc_manuscript.md
  - Applies to: `la_pose_latent_action_manuscript.md`
  - Notes: Related processed artifact on learned driving-state representations and constrained control.
