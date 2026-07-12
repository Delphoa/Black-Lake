# DEP-E-20260712-HERMES World Model

#autonomous-driving #world-models #vision-language #bird-eye-view #point-clouds #multimodal-ai #evaluation #arxiv-review

Public-safe deposition context: This DEP-E entry preserves a source-first review of arXiv:2501.14729, *HERMES: A Unified Self-Driving World Model for Simultaneous 3D Scene Understanding and Generation*. The deposit records date-only selection and deduplication provenance, public URLs, and repository-relative related-entry references. Private source locations, machine details, timezone labels, and exact execution timestamps are withheld. No original source files are redistributed.

## Contents

- `README.md` — DEP inventory, item summaries, research relevance, and final source attribution.
- `hermes_world_model_manuscript.md` — Schema-complete manuscript reviewing HERMES's BEV tokenizer, language-conditioned world queries, point-cloud renderer, evidence, limitations, related deposits, and safe implementation paths.

## Summary of Items

- `README.md` records the DEP-E class, classification tags, public-safe context, complete two-file inventory, source-collection policy, and annotations required for future review.
- `hermes_world_model_manuscript.md` preserves paper metadata, an evidence ledger, the model and training mechanism, reported comparisons and ablations, source/reviewer claim separation, random-selection and dedup validation, exactly three exercise paths, a bounded evaluation MVP, related reading, a replication checklist, and source references.
- No `.source/` directory was created. The locally inspected PDF and extraction cache were not collected into this public deposit; public arXiv, ICCV, and official-code URLs provide provenance.

## Insights and Relevance

HERMES is relevant to Black Lake because it makes a compact geometric state—the Bird's-Eye View—the interface between language-based scene understanding and future 3D generation. Its results suggest that language-conditioned world queries can improve point-cloud prediction relative to separated task models, but its ablations also expose tradeoffs across geometry horizons and language scores. The related VideoWeave deposit extends the geometry-consistency question to generated video, VLM Probing supplies representation-audit methods, and the visual-world-model hallucination finding adds coverage-aware failure analysis. The downstream opportunity is an offline evidence gate that combines geometric, semantic, causal, calibration, and scenario-coverage checks before a world model is used as a simulator or planning research substrate.

## Attribution Block

- Source URL: https://arxiv.org/abs/2501.14729
  - Applies to: `hermes_world_model_manuscript.md`
  - Notes: Primary arXiv metadata, abstract, stable identifier, and source links.
- Source URL: https://arxiv.org/html/2501.14729
  - Applies to: `hermes_world_model_manuscript.md`
  - Notes: Primary full-text evidence for architecture, training, datasets, results, ablations, supplementary details, and limitations.
- Source URL: https://arxiv.org/pdf/2501.14729
  - Applies to: `hermes_world_model_manuscript.md`
  - Notes: Public equivalent of the privately inspected paper PDF; no PDF is redistributed in this DEP.
- Source URL: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_HERMES_A_Unified_Self-Driving_World_Model_for_Simultaneous_3D_Scene_ICCV_2025_paper.html
  - Applies to: `hermes_world_model_manuscript.md`
  - Notes: ICCV 2025 open-access publication context and accepted-paper cross-check.
- Source URL: https://github.com/LMD0311/HERMES
  - Applies to: `hermes_world_model_manuscript.md`
  - Notes: Official code, setup, data/weights, usage, release, and Apache-2.0 license status; code was not executed.
- Repository source: `.lake-data/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`
  - Applies to: `hermes_world_model_manuscript.md`
  - Notes: Related Black Lake artifact on geometry-aware video generation and spatial-consistency evaluation.
- Repository source: `.lake-data/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`
  - Applies to: `hermes_world_model_manuscript.md`
  - Notes: Related Black Lake artifact on multimodal fusion, attention, and representation probes.
- Repository source: `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md`
  - Applies to: `hermes_world_model_manuscript.md`
  - Notes: Related Black-Lake-Data finding on visual-world-model hallucination modes and coverage-aware mitigation, item 6.
