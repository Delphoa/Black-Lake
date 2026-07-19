# DEP-E-20260718-Stable Diffusion Depth

#computer-vision #monocular-depth #robustness #stable-diffusion #self-training #knowledge-distillation #autonomous-driving #research-review

- DEP class: DEP-E.
- Deposition date: 2026-07-18.
- Subject title: Stealing Stable Diffusion Prior for Robust Monocular Depth Estimation.
- Public-safe context: Source-first review of arXiv:2403.05056v1, its official project page, and its official repository. The verified PDF, full-paper and metadata HTML, TeX/source, extracted text, cache, and integrity records remain local and withheld; review-page renderings were removed after inspection.
- Source policy: No `.source/` directory was created. No original source file is included or authorized for upload.

## Contents

- `README.md`
  - DEP inventory, public-safe context, source policy, item summaries, research relevance, and complete attribution.
- `stable_diffusion_depth_manuscript.md`
  - Schema-complete manuscript covering the GDT generator, DINOv2-DPT teacher/student system, losses, experiments, equation ambiguity, repository availability, implementation paths, and reproducibility boundaries.

## Summary of Items

`stable_diffusion_depth_manuscript.md` reconstructs a two-stage robustness strategy. GDT turns day-clear frames into depth-conditioned night/rain examples using BLIP-2, MiDaS/PatchFusion, Stable Diffusion 1.5, ControlNet, and IP-Adapter. A day-clear teacher then supervises a DINOv2-DPT student trained on original and translated frames, with semantic alignment and a photometric reliability mask.

The manuscript preserves Tables 1-3 and the visual evidence in Figures 3-6 while distinguishing author-reported results from reviewer interpretation. It records a material ambiguity: Equation 5 evaluates true exactly where teacher photometric error exceeds student error, but Equation 6 multiplies that mask into the distillation loss even though the prose says unreliable teacher pixels should be filtered. The official repository contains documentation and images but no executable code or weights at the pinned revision, so this conflict cannot be resolved from implementation evidence.

## Insights and Relevance

The durable design idea is to use a powerful generator as an offline condition-expansion engine, then transfer the resulting robustness into a smaller perception model. That is useful beyond depth estimation, but the transfer is safe only when geometry preservation, synthetic-domain coverage, label reliability, and downstream calibration are independently measured. The three related DEPs make that boundary concrete: UAV Visual Localization shows how DINOv2 features can bridge visual domains but still need abstention and fixed-denominator metrics; VideoWeave treats geometry as a validation target for diffusion outputs; Stereo Lane Detection shows that driving-scene geometry and relative improvements are not substitutes for adverse-condition, calibration, latency, and recovery evidence.

No source file was uploaded. Public arXiv and repository URLs below provide traceability while all source documents and derivatives remain withheld locally.

## Attribution Block

- Source URL: https://arxiv.org/abs/2403.05056
  - Applies to: `stable_diffusion_depth_manuscript.md`.
  - Notes: Primary title, authors, submission/version, subject, arXiv DOI, abstract, project, and code locator; abstract alone was not used for detailed claims.
- Source URL: https://arxiv.org/pdf/2403.05056
  - Applies to: `stable_diffusion_depth_manuscript.md`.
  - Notes: Complete paper, figures, tables, equations, and references; downloaded file remained local.
- Source URL: https://arxiv.org/html/2403.05056
  - Applies to: `stable_diffusion_depth_manuscript.md`.
  - Notes: Official full-paper HTML used for source-first review; downloaded file remained local.
- Source URL: https://arxiv.org/e-print/2403.05056
  - Applies to: `stable_diffusion_depth_manuscript.md`.
  - Notes: TeX/source used to verify equations and exact table values; archive remained local.
- Source URL: https://doi.org/10.48550/arXiv.2403.05056
  - Applies to: `stable_diffusion_depth_manuscript.md`.
  - Notes: arXiv-issued DOI identity.
- Source URL: https://hitcslj.github.io/ssd/
  - Applies to: `stable_diffusion_depth_manuscript.md`.
  - Notes: Official project overview and visual-method context.
- Source URL: https://github.com/hitcslj/SSD
  - Applies to: `stable_diffusion_depth_manuscript.md`.
  - Notes: Official repository availability audit at commit `a5b11b77e33d3faf7d6f35d501f6fd27d0f65137`.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md` and `stable_diffusion_depth_manuscript.md`.
  - Notes: Live repository filing, attribution, source-locality, and submission authority.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md` and `stable_diffusion_depth_manuscript.md`.
  - Notes: Live DEP-E container and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `stable_diffusion_depth_manuscript.md`.
  - Notes: Related-repository authority inspected for dedup and related-context validation.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-UAV%20Visual%20Localization/uav_visual_localization_manuscript.md
  - Applies to: `stable_diffusion_depth_manuscript.md`.
  - Notes: Related DEP source for DINOv2, robust visual matching, localization metrics, and abstention boundaries.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md
  - Applies to: `stable_diffusion_depth_manuscript.md`.
  - Notes: Related DEP source for diffusion priors, geometry consistency, and synthetic-media validation.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Stereo%20Lane%20Detection/stereo_lane_detection_manuscript.md
  - Applies to: `stable_diffusion_depth_manuscript.md`.
  - Notes: Related DEP source for driving-scene geometry, adverse-condition gaps, calibration, latency, and recovery.
- Source URL: https://arxiv.org/abs/2304.07193
  - Applies to: `stable_diffusion_depth_manuscript.md` related reading.
  - Notes: DINOv2 primary research record.
- Source URL: https://openaccess.thecvf.com/content/ICCV2023/html/Gasperini_Robust_Monocular_Depth_Estimation_under_Challenging_Conditions_ICCV_2023_paper.html
  - Applies to: `stable_diffusion_depth_manuscript.md` related reading.
  - Notes: md4all baseline and self-training context.
- Source URL: https://arxiv.org/abs/2112.10752
  - Applies to: `stable_diffusion_depth_manuscript.md` related reading.
  - Notes: Latent Diffusion/Stable Diffusion foundation.
- Source URL: https://arxiv.org/abs/2302.05543
  - Applies to: `stable_diffusion_depth_manuscript.md` related reading.
  - Notes: ControlNet spatial-conditioning foundation.
- Source URL: https://arxiv.org/abs/2308.06721
  - Applies to: `stable_diffusion_depth_manuscript.md` related reading.
  - Notes: IP-Adapter image-prompt conditioning foundation.
- Source URL: https://www.nuscenes.org/
  - Applies to: `stable_diffusion_depth_manuscript.md`.
  - Notes: nuScenes dataset authority.
- Source URL: https://robotcar-dataset.robots.ox.ac.uk/
  - Applies to: `stable_diffusion_depth_manuscript.md`.
  - Notes: Oxford RobotCar dataset authority.
