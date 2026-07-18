# DEP-E-20260718-SpOctA Accelerator

#3d-sparse-convolution #point-cloud #hardware-accelerator #octree #sparsity #memory-efficiency #research-review

- DEP class: DEP-E.
- Deposition date: 2026-07-18.
- Subject title: SpOctA: A 3D Sparse Convolution Accelerator with Octree-Encoding-Based Map Search and Inherent Sparsity-Aware Processing.
- Public-safe context: Source-first review of arXiv:2308.09249v1 and its ICCAD 2023 publication record. The complete PDF, full-paper HTML, metadata HTML, TeX/source package, extracted text, caches, and verification records were inspected locally and withheld from publication.
- Source policy: No `.source/` directory was created. No original source file is included or authorized for upload.

## Contents

- `README.md`
  - DEP inventory, source policy, item summaries, research relevance, and complete URL attribution.
- `spocta_accelerator_manuscript.md`
  - Schema-complete manuscript review with source metadata, evidence ledger, architecture and evaluation analysis, claim assessment, limitations, implementation paths, exactly three practical exercises, an MVP concept, related reading, and source-locality appendix.

## Summary of Items

`spocta_accelerator_manuscript.md` reviews SpOctA's two-core design. OCTENT maps octree-encoded voxel coordinates into bank-safe parallel table queries and overlaps map search with execution. SPAC gathers nonzero inputs, supports multiple dataflows, and applies non-uniform weight caching based on vertical kernel-use skew. The manuscript preserves the authors' synthesis/simulation results while labeling them as author-reported and separating them from reviewer interpretation.

The manuscript also records the uniform random selection and cross-repository deduplication method, the source-integrity repair, the full-paper validation metrics, and the no-source-upload gate. It connects the paper to exactly three inspected Black Lake entries: Efficient FM Survey, Physical Data AI, and HERMES World Model.

## Insights and Relevance

The durable insight is a representation-to-hardware co-design pattern. Octree digits become a bank schedule, activation zeros become avoidable work only through gather/arrange hardware, and measured kernel-plane frequency becomes a selective cache policy. The three related DEPs extend this pattern into a review contract: count the resource and its denominator, keep model/digital evidence distinct from physical hardware claims, and bind accelerator efficiency to 3D task quality and safety-relevant workload slices. SpOctA is therefore useful both as an accelerator case study and as a template for evaluating whether irregular sparsity has been converted into real, auditable system savings.

## Attribution Block

- Source URL: https://arxiv.org/abs/2308.09249
  - Applies to: `spocta_accelerator_manuscript.md`.
  - Notes: Primary arXiv metadata, authors, version, subject, acceptance note, and abstract; abstract alone was not used for method/result claims.
- Source URL: https://arxiv.org/pdf/2308.09249
  - Applies to: `spocta_accelerator_manuscript.md`.
  - Notes: Primary complete paper, figures, tables, and evaluation evidence; downloaded file remained local.
- Source URL: https://ar5iv.labs.arxiv.org/html/2308.09249
  - Applies to: `spocta_accelerator_manuscript.md`.
  - Notes: Verified full-paper fallback used after the official arXiv HTML endpoint was unavailable; downloaded file remained local.
- Source URL: https://arxiv.org/e-print/2308.09249
  - Applies to: `spocta_accelerator_manuscript.md`.
  - Notes: TeX/source package used for section, algorithm, and evaluation inspection; downloaded archive remained local.
- Source URL: https://doi.org/10.48550/arXiv.2308.09249
  - Applies to: `spocta_accelerator_manuscript.md`.
  - Notes: arXiv DOI identity.
- Source URL: https://doi.org/10.1109/ICCAD57390.2023.10323728
  - Applies to: `spocta_accelerator_manuscript.md`.
  - Notes: Published ICCAD DOI identity.
- Source URL: https://ieeexplore.ieee.org/document/10323728
  - Applies to: `spocta_accelerator_manuscript.md`.
  - Notes: IEEE publication locator; page body was unavailable to the browser.
- Source URL: https://lvdongxu.github.io/
  - Applies to: `spocta_accelerator_manuscript.md`.
  - Notes: Author-maintained ICCAD publication listing and pages 1-9 metadata.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md` and `spocta_accelerator_manuscript.md`.
  - Notes: Live repository filing, attribution, source-locality, and commit authority.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md` and `spocta_accelerator_manuscript.md`.
  - Notes: Live DEP-E container and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `spocta_accelerator_manuscript.md`.
  - Notes: Related-repository authority read before dedup and related-context use.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Efficient%20FM%20Survey/efficient_fm_survey_manuscript.md
  - Applies to: `spocta_accelerator_manuscript.md`.
  - Notes: Related DEP source for resource accounting, sparse execution, and operational-envelope discipline.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Physical%20Data%20AI/physical_data_ai_manuscript.md
  - Applies to: `spocta_accelerator_manuscript.md`.
  - Notes: Related DEP source for representation-substrate and hardware-evidence discipline.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model/hermes_world_model_manuscript.md
  - Applies to: `spocta_accelerator_manuscript.md`.
  - Notes: Related DEP source for 3D point-cloud workload and autonomous-driving evaluation context.
- Source URL: https://arxiv.org/abs/1904.08755
  - Applies to: `spocta_accelerator_manuscript.md` related reading.
  - Notes: Minkowski sparse-convolution context cited by the reviewed paper.
- Source URL: https://doi.org/10.3390/s18103337
  - Applies to: `spocta_accelerator_manuscript.md` related reading.
  - Notes: SECOND model publication used by the reviewed evaluation.
- Source URL: http://www.scan-net.org/
  - Applies to: `spocta_accelerator_manuscript.md` related reading.
  - Notes: ScanNet dataset locator.
- Source URL: http://semantic-kitti.org/
  - Applies to: `spocta_accelerator_manuscript.md` related reading.
  - Notes: SemanticKITTI dataset locator.
- Source URL: https://www.cvlibs.net/datasets/kitti/
  - Applies to: `spocta_accelerator_manuscript.md` related reading.
  - Notes: KITTI dataset locator.
- Source URL: https://www.nuscenes.org/
  - Applies to: `spocta_accelerator_manuscript.md` related reading.
  - Notes: nuScenes dataset locator.
