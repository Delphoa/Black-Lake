# Report-Mark: HERMES World Model

## Source Metadata

| Field | Value |
|---|---|
| Paper | *HERMES: A Unified Self-Driving World Model for Simultaneous 3D Scene Understanding and Generation* |
| Authors | Xin Zhou, Dingkang Liang, Sifan Tu, Xiwu Chen, Yikang Ding, Dingyuan Zhang, Feiyang Tan, Hengshuang Zhao, Xiang Bai |
| Affiliations | Huazhong University of Science and Technology; MEGVII Technology; Mach Drive; The University of Hong Kong |
| arXiv | 2501.14729 |
| DOI marker | 10.48550/arXiv.2501.14729 |
| Venue | IEEE/CVF International Conference on Computer Vision (ICCV) 2025 |
| Initial submission | 2025-01-24 |
| Primary URL | https://arxiv.org/abs/2501.14729 |
| Accepted paper | https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_HERMES_A_Unified_Self-Driving_World_Model_for_Simultaneous_3D_Scene_ICCV_2025_paper.html |
| Official code | https://github.com/LMD0311/HERMES |
| Code license | Apache-2.0 |
| Local evidence | PDF and provenance readme inspected; location withheld and files not redistributed |
| Access date | 2026-07-12 |

## Concise Research Notes

### Problem

Driving world models usually predict future scenes but do not explicitly explain or answer questions about the current environment. Driving vision-language models can describe and reason about scenes but usually do not generate their geometric evolution. HERMES asks whether both functions can share a compact spatial representation and exchange information inside one model.

### Method

HERMES converts six camera views into a Bird's-Eye View (BEV) representation using an OpenCLIP ConvNeXt-L image backbone and single-frame BEVFormer v2. A downsampling block compresses the BEV to 50 by 50, or 2,500 tokens, before projection into an InternVL2-derived 1.8B-parameter language model. Text prompts and BEV tokens support scene descriptions and visual question answering.

For generation, groups of world queries are initialized from max-pooled BEV features and augmented with future ego-motion and frame embeddings. Because later tokens can attend to earlier text and BEV tokens, the queries receive language-conditioned scene information through causal attention. A current-to-future cross-attention link expands the sparse queries into future BEV states. A shared signed-distance-function renderer then reconstructs the current point cloud and predicts point clouds up to three seconds ahead.

Training has three stages: tokenizer/render learning, BEV-text alignment and refinement, and joint understanding/generation training. The text branch uses next-token prediction, while point-cloud depth uses a weighted L1 loss. Supplementary details report 32 NVIDIA H20 GPUs, AdamW, and a 36-epoch final stage.

### Evidence and Results

- On the full validation comparison, HERMES reports Chamfer distances of 0.59, 0.78, 0.95, and 1.17 at 0–3 seconds. ViDAR reports 1.12, 1.38, and 1.73 at 1–3 seconds, making the 3-second reduction about 32.4%.
- HERMES reports METEOR 0.384, ROUGE 0.327, and CIDEr 0.741. OmniDrive reports 0.380, 0.326, and 0.686, so the relative CIDEr improvement is about 8.0%.
- Compared with a separated unification baseline, HERMES improves generation from 0.60/0.84/1.08/1.37 to 0.59/0.78/0.95/1.17 while keeping similar understanding scores.
- The world-query ablation reports a roughly 10% reduction in 3-second Chamfer distance, alongside a roughly 1% CIDEr decrease, indicating a real multi-task tradeoff rather than a uniform gain.
- A 50 by 50 BEV improves 0-second generation and CIDEr relative to 25 by 25, but its 3-second value is slightly worse, exposing a horizon-dependent tradeoff.
- Supplementary NuScenes-QA results report 61.9% accuracy, versus 59.5% for CenterPoint+MCAN and 59.2% for OmniDrive.

These are author-reported results. The paper and official implementation were inspected, but no experiment was rerun.

### Limitations

The paper explicitly leaves autonomous-driving perception tasks and future image generation for later work. Its evidence is concentrated on nuScenes-derived benchmarks, point-cloud Chamfer distance, caption overlap metrics, and mostly open-loop evaluation. The paper does not establish closed-loop planning safety, calibration under distribution shift, object-level error severity, or robustness to rare road events. It uses ground-truth future ego-motion for controlled prediction comparisons, which narrows what can be concluded about an end-to-end deployed system.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Caveat |
|---|---|---|---|---|
| E1 | Locally inspected PDF text for arXiv:2501.14729 | Full architecture, tables, training details, ablations, limitations | High for reporting | Extraction has character artifacts; experiments not rerun |
| E2 | https://arxiv.org/abs/2501.14729 and https://arxiv.org/html/2501.14729 | Identity, authors, date, method, metrics, supplementary text | High | Author-provided primary source |
| E3 | ICCV 2025 open-access paper | Accepted-paper status and cross-check of method/results | High | Publication is not independent replication |
| E4 | https://github.com/LMD0311/HERMES | Code, guides, checkpoints/data release claims, Apache-2.0 license | Medium-high | Repository was inspected at README level; execution not attempted |
| E5 | Three inspected DEP entries | Cross-DEP synthesis | Medium | Related material does not validate HERMES's empirical claims |

Source claims are paraphrased from E1–E4. Product and implementation ideas below are reviewer interpretations.

## Related DEP Entries

1. [VideoWeave Geometry manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md)
   - Repository path: `.lake-data/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`
   - Relevance: VideoWeave treats geometry as a latent consistency signal for generated video, while HERMES makes BEV geometry the shared interface between language understanding and point-cloud evolution. Both argue that appearance-only generation is insufficient for world-model use.
   - Source basis: The related manuscript's inspected Executive Summary, Detailed Summary, evidence ledger, and observations, grounded in arXiv full text.
2. [VLM Probing manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md)
   - Repository path: `.lake-data/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`
   - Relevance: VALUE's layer, head, modality, and mismatch probes offer a concrete audit pattern for testing where HERMES's BEV, text, and world-query information actually fuse.
   - Source basis: The related manuscript's inspected Executive Summary, probe results, evidence ledger, and observations.
3. [Visual world-model hallucination finding](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260628-Tech%20Intel%200102/daily_research_findings_2026-06-28_0102.md)
   - Repository path: `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md`
   - Relevance: Item 6 describes perceptual, action-marginalized, and scene-diverging hallucinations plus coverage-aware sampling. Those categories complement HERMES's aggregate Chamfer and caption metrics with failure-mode and data-coverage diagnostics.
   - Source basis: The inspected Overall Synthesis and item 6, which cite arXiv:2606.27326 as the primary record.

## Synthesis Note

### Concept Bridge

HERMES supplies a geometric-language bridge for autonomous-driving world models: BEV compresses multi-view observations, language-model attention enriches future queries, and a renderer turns future latent states back into point clouds. VideoWeave broadens the same principle to latent geometry in video generation. VLM Probing contributes tools for checking whether the claimed cross-modal transfer is localized and robust. The visual-world-model hallucination finding adds coverage and divergence diagnostics that aggregate metrics miss. Together, the four artifacts suggest a research stack with three layers: spatially grounded generation, representation-level auditing, and coverage-aware failure detection.

### Potential Implementations

1. A BEV world-model evaluation harness that reports horizon-wise geometry, caption/VQA quality, object-level misses, calibration, and scenario coverage in one versioned result bundle.
2. A world-query causal audit that masks, patches, or permutes query groups and text context to measure whether language-conditioned information changes future geometry in the expected regions.
3. A synthetic-scene coverage planner that prioritizes rare weather, occlusion, vulnerable-road-user, and unusual-ego-motion cases where the model's uncertainty or divergence score is highest.

### Deeper Relationship Observations

1. HERMES and VideoWeave both move geometry into the model's internal state, but HERMES decodes point clouds as the target whereas VideoWeave discards geometry latents after distillation; this makes their validation obligations complementary.
2. VLM Probing warns that visible attention patterns are descriptive rather than causal, so HERMES's world-query mechanism needs intervention-based validation before its gains can be attributed to language-to-geometry transfer.
3. The hallucination finding reframes HERMES's remaining errors as a coverage problem: a good average Chamfer distance can coexist with scene-diverging failures concentrated in rare or poorly sampled conditions.

### Conceptual Similarities

1. All four works treat internal representations as structured interfaces rather than undifferentiated feature vectors.
2. Each separates surface output quality from a deeper reliability dimension: geometry, fusion, causal transfer, or coverage.
3. Each motivates controlled comparisons or ablations as the minimum evidence for a claimed mechanism.

### MVP Implementations with Code Mock-Ups

1. `Horizon geometry summary` — aggregate non-negative per-scene Chamfer values without hiding the worst horizon.

```python
def horizon_summary(rows):
    if not rows:
        raise ValueError("at least one scene is required")
    horizons = sorted(rows[0])
    if any(sorted(row) != horizons for row in rows):
        raise ValueError("all scenes must share horizons")
    means = {h: sum(row[h] for row in rows) / len(rows) for h in horizons}
    return {"means": means, "worst_horizon": max(means, key=means.get)}
```

2. `World-query ablation check` — compare a baseline and intervention on aligned aggregate metrics.

```python
def ablation_delta(baseline, intervention):
    required = {"chamfer_3s", "cider"}
    if set(baseline) != required or set(intervention) != required:
        raise ValueError("expected chamfer_3s and cider")
    return {
        "chamfer_change": intervention["chamfer_3s"] - baseline["chamfer_3s"],
        "cider_change": intervention["cider"] - baseline["cider"],
    }
```

3. `Coverage-aware release gate` — reject a checkpoint when any approved scenario slice is missing or exceeds its failure-rate limit.

```python
def coverage_gate(slice_failures, limits):
    missing = sorted(set(limits) - set(slice_failures))
    exceeded = {
        name: slice_failures[name]
        for name, limit in limits.items()
        if name in slice_failures and slice_failures[name] > limit
    }
    return {"accepted": not missing and not exceeded, "missing": missing, "exceeded": exceeded}
```

The sketches operate on synthetic or aggregate metrics, avoid raw sensor data, and are illustrative rather than deployment-ready.

### Developer Challenges

1. Aligning camera, BEV, language, query, ego-motion, and point-cloud coordinates while preserving deterministic evaluation across model revisions.
2. Building object- and scenario-level diagnostics that remain comparable when datasets, sensor configurations, or prediction horizons change.
3. Running causal ablations efficiently enough to become a release gate for a model whose reported training uses substantial accelerator resources.

### Author Challenges

1. Demonstrating that world-query improvements arise from meaningful language-conditioned geometry rather than additional parameters or shared optimization effects.
2. Extending evidence beyond nuScenes-derived benchmarks to rare events, distribution shift, closed-loop planning, and safety-critical calibration.
3. Reporting artifact versions, seeds, checkpoint hashes, processed-data provenance, and evaluation scripts tightly enough for independent reproduction.

## Validation Notes

- Uniform random selection used zero-based index 69,210 over 75,761 unique PDF-parent units.
- Dedup context contained 363 unique arXiv IDs; 67 candidate units matched an observed ID. No ID, DOI marker, normalized-title, or slug match was found for arXiv:2501.14729.
- No same-paper marker was found in the preceding 24 hours; duplicate rejections and reselections were both zero.
- `pypdf` extracted 76,272 bytes of text; methods, results, ablations, training details, and limitations were inspected.
- Exactly three related DEP entries were inspected and used.
- Exactly three potential implementations, deeper relationship observations, conceptual similarities, MVP mock-ups, developer challenges, and author challenges appear in the Synthesis Note.
- No original source files were collected into the report or DEP.
- Public content intentionally excludes local paths, home identifiers, machine names, timezone labels, and exact execution timestamps.

## Attribution Block

- Source URL: https://arxiv.org/abs/2501.14729
  - Applies to: title, authors, submission date, abstract, stable identifier, and high-level claims.
  - Notes: Primary public arXiv record.
- Source URL: https://arxiv.org/html/2501.14729
  - Applies to: architecture, methods, datasets, metrics, tables, ablations, supplementary training details, and limitations.
  - Notes: Primary full-text evidence.
- Source URL: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_HERMES_A_Unified_Self-Driving_World_Model_for_Simultaneous_3D_Scene_ICCV_2025_paper.html
  - Applies to: ICCV 2025 acceptance and accepted-paper cross-check.
  - Notes: Computer Vision Foundation open-access publication page.
- Source URL: https://github.com/LMD0311/HERMES
  - Applies to: official code, release material, setup guides, and Apache-2.0 license status.
  - Notes: Repository inspected for availability; code was not executed.
- Repository source: `.lake-data/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`
  - Applies to: related-entry geometry and world-model synthesis.
  - Notes: Existing Black Lake manuscript.
- Repository source: `.lake-data/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`
  - Applies to: related-entry representation-audit synthesis.
  - Notes: Existing Black Lake manuscript.
- Repository source: `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md`
  - Applies to: related-entry world-model hallucination and coverage synthesis.
  - Notes: Existing Black-Lake-Data research finding, item 6.
