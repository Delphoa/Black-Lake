---
title: "ST-NeRF - DEP-E"
generated_at: "2026-08-18 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of editable free-viewpoint video using layered spatio-temporal neural radiance fields."
source_status: "verified local PDF and full-paper HTML; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-18"
temporal_cutoff: "Paper version arXiv:2104.14786v1 and public repository context inspected on 2026-08-18."
primary_url: "https://arxiv.org/abs/2104.14786"
stable_identifier: "arXiv:2104.14786v1; DOI:10.1145/3450626.3459756"
confidence_summary: "High for source identity, method transcription, and printed-table inspection; medium for reported results; low for reproducibility because code and data were not executed."
safety_scope: "Offline research review, synthetic evaluation planning, and nonbinding implementation ideation."
distribution_notes: "Original PDF, full-paper HTML, metadata, extraction cache, repair receipts, and unavailable source package remain local and are not redistributed."
---

# ST-NeRF - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv metadata | Primary identity | HTML | arXiv:2104.14786v1; 30 Apr 2021 | https://arxiv.org/abs/2104.14786 | Public metadata; the record reports CC BY 4.0 for the arXiv HTML rendering. | 2026-08-18 | Inspected |
| S2 | arXiv full paper | Primary artifact | HTML | arXiv:2104.14786v1 | https://arxiv.org/html/2104.14786 | Full-paper HTML verified locally and withheld. | 2026-08-18 | Inspected |
| S3 | arXiv PDF | Primary artifact | PDF | arXiv:2104.14786v1 | https://arxiv.org/pdf/2104.14786 | PDF verified locally and withheld. | 2026-08-18 | Inspected and visually sampled |
| S4 | ACM publication record | Publisher metadata | DOI | ACM TOG 40(4), Article 149, Aug 2021 | https://doi.org/10.1145/3450626.3459756 | Publisher locator; no publisher file was collected. | 2026-08-18 | Inspected |
| S5 | ST-NeRF project page | Author context | HTML | Project page | https://jiakai-zhang.github.io/st-nerf/ | Public project page; it links the test code and partial preprocessed dataset. | 2026-08-18 | Inspected |
| S6 | ST-NeRF implementation | Official implementation | Repository | `DarlingHang/st-nerf`, main | https://github.com/DarlingHang/st-nerf | README, configuration, and demo inspected; execution and data download were out of scope. | 2026-08-18 | Inspected |
| S7 | Controllable Dynamic DEP | Related processed artifact | Markdown | DEP-E | `.lake-data/DEP-E/DEP-E-20260813-Controllable Dynamic/controllable_dynamic_manuscript.md` | Existing public-safe Black Lake manuscript. | 2026-08-18 | Inspected |
| S8 | VideoWeave Geometry DEP | Related processed artifact | Markdown | DEP-E | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Existing public-safe Black Lake manuscript. | 2026-08-18 | Inspected |
| S9 | HERMES World Model DEP | Related processed artifact | Markdown | DEP-E | `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` | Existing public-safe Black Lake manuscript. | 2026-08-18 | Inspected |

Authors: Jiakai Zhang, Xinhang Liu, Xinyi Ye, Fuqiang Zhao, Yanshun Zhang, Minye Wu, Yingliang Zhang, Lan Xu, and Jingyi Yu. The arXiv version is v1, submitted 30 April 2021. The ACM record identifies the work as ACM Transactions on Graphics, volume 40, issue 4, Article 149, with publication in August 2021.

Source integrity: the initial local unit was partial because its full-paper HTML was missing. A bounded single-paper archive repair fetched the official HTML and refreshed the local README, provenance record, machine-readable summary, verification report, and repair receipt. The final PDF passed the required size, `%PDF-`, and trailing `%%EOF` checks. The final HTML passed the required size, body-character, document-marker, heading, and structure-term checks. The source package was unavailable. All original files and cache outputs remain local.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S2, S3, S4 | Primary paper and publisher metadata | Title, authors, arXiv version, DOI, venue, abstract, full-paper sections, and reference list | Source identity and publication context | High | Version-specific; not an independent reproduction |
| E2 | S2, S3 | Primary method evidence | Scene parsing, 4D label-map tracking, bounding boxes, ST-NeRF deformation/radiance modules, layered sampling, object-aware rendering, layered loss, and motion-aware ray sampling | Mechanism and architecture | High | PDF text has symbol-encoding noise; source package unavailable |
| E3 | S2, S3 | Primary evaluation evidence | Eight indoor scenes, 16 synchronized cameras, synthetic view ablation, training/rendering cost, comparison tables, editing demonstrations, and component ablations | Reported results and operating boundary | Medium-high | Author-reported; no independent rerun |
| E4 | S3 | Visual primary evidence | Printed Table 1 values and bolding inspected on the rendered PDF page | Metric-direction discrepancy | High for transcription | Raw metric files were not available |
| E5 | S5, S6 | Author and official implementation context | Project page, code availability statement, README, environment pins, datasets, demo commands, and configuration | Reproducibility boundary | High for availability; low for reproducibility | Code and data were not executed or downloaded |
| E6 | S7, S8, S9 | Related Black Lake evidence | Dynamic neural appearance, geometry-consistent video, and multi-view spatiotemporal world-model patterns | Cross-DEP synthesis | Medium | Related artifacts do not validate the selected paper |
| E7 | Workflow records | Process evidence | Uniform selection, dedup checks, source repair, cache summary, and public-safe policy | Provenance and eligibility | High | Process evidence is not scientific evidence |

## Executive Summary

The paper introduces ST-NeRF, a layered spatio-temporal neural radiance representation for editable free-viewpoint video of large dynamic scenes. It uses 16 synchronized RGB cameras covering up to 180 degrees, parses performers into tracked 4D label maps and 3D bounding boxes, learns separate continuous space-time functions for entities and background, and reassembles them through object-aware volume rendering. At inference, changing layer bounding boxes or timestamps enables translation, scaling, duplication, transparency changes, hiding, and retiming without additional training.

The source reports eight indoor scenes with two or three performers, 1920x1080 input at 25 fps, 75–350 frames per scene, a single RTX 3090, 12–36 hours of initial training at lower resolution, extra days for high-resolution refinement, and about two minutes to render a 1920x1080 image with three layers. Table 1 prints an `Ours` row of PSNR 33.2161, SSIM 0.9203, MAE 0.1178, and LPIPS 0.2186. Visual inspection confirms those printed values, but the table’s bolding and prose claim broad superiority even though the printed SSIM and MAE are not better than all baselines in the stated directions. The result is therefore preserved as author-reported with a material internal inconsistency.

The strongest transferable idea is the layer boundary: an explicit, inspectable control surface separates scene entities before continuous neural rendering. The strongest limitation is that this control surface depends on accurate human segmentation, tracking, bounding boxes, calibration, and enough cameras. The paper is useful for offline research and synthetic evaluation design, but the review does not establish reproducibility, non-human object generality, or production readiness.

## Detailed Summary

### Problem and Background

Traditional multi-view and mesh-based free-viewpoint video can be expensive, brittle under dynamic motion, or visually limited. Image-based rendering can interpolate views but is vulnerable to occlusion and sparse coverage. Dynamic NeRF extensions model time but do not necessarily expose controllable per-entity editing. The paper targets the combined problem of wide-range dynamic free-viewing plus spatial and temporal manipulation.

### Scene Parsing

The input is a synchronized multi-view RGB sequence. A patch-based multi-view stereo stage estimates coarse depth. A SiamMask tracker and trajectory-prediction network produce per-entity tracklets and 2D masks across views. Shape-from-space-carving uses the masks to create coarse geometry and tight 3D bounding boxes. A depth-based mask-refinement step rejects pixels inconsistent with the previous frame’s depth estimate. The environment is treated as a special layer.

### ST-NeRF Representation

Each dynamic entity and the background are represented by an MLP pair. A deformation module maps a sampled space-time point into a canonical space, while a neural-radiance module predicts density and color using the deformed position, viewing direction, and timestamp. Positional encoding represents space, direction, and time. The separation makes the entity’s explicit pose and implicit geometry/appearance manipulable through the layer’s spatial and temporal inputs.

### Layered Rendering and Training

The renderer composes edited 3D bounding boxes, segments each camera ray at box intersections, samples each valid segment hierarchically, evaluates the corresponding ST-NeRF, merges samples by depth, and integrates density and color with object-aware volume rendering. Training combines coarse/fine RGB reconstruction with a layer-wise occupancy loss. A warm-up adjusts the layer-loss weight, and motion-aware ray sampling corrects the imbalance between large static backgrounds and smaller moving entities. Adam is used with a decaying learning rate; the paper reports 3,000 rays per mini-batch.

### Editing Operations

Spatial affine edits transform an entity’s bounding box and apply the inverse transform to its sampled points and view direction before ST-NeRF evaluation. Temporal retiming selects another timestamp’s bounding box and layer state. Layer composition enables duplication, removal, hiding, transparency adjustment, zooming, relocation, and retiming. The paper demonstrates these operations on dancing, taekwondo, musicians, breaking, superheroes, and K-pop scenes.

### Evaluation and Results

The real dataset contains eight large indoor dynamic scenes, two or three performers, 16 industrial cameras arranged over approximately 180 degrees, 1920x1080 resolution, 25 fps, and 75–350 frames. A synthetic dataset uses 36 virtual cameras over 360 degrees, two virtual characters, and a four-second sequence at 25 fps. Baselines include NeRF, NeRF-T, Neural Volumes, Agisoft PhotoScan, HVR, and Layered Neural Rendering.

The printed Table 1 reports the following values: NeRF 21.7952/0.8755/0.0574/0.2961; NeRF-T 28.2553/0.9243/0.0219/0.2560; Neural Volumes 28.0850/0.9110/0.0243/0.2608; AGI 14.8220/0.8764/0.0839/0.4543; HVR 24.0342/0.9113/0.0247/0.2589; and Ours 33.2161/0.9203/0.1178/0.2186 for PSNR/SSIM/MAE/LPIPS. The rendered page shows `Ours` bolded in all four columns, but the lower-is-better MAE value 0.1178 is larger than every baseline and the higher-is-better SSIM value 0.9203 is below NeRF-T’s 0.9243. The caption also says all four metrics improve. This inconsistency is a validation finding, not a correction.

The ablation table reports complete-model values of PSNR held-out 29.9091, PSNR 30.0502, SSIM 0.8566, MAE 0.0187, and LPIPS 0.2329, outperforming the listed ablations in that synthetic setting. The view-count study reports held-out PSNR 15.9286, 22.1213, 23.2100, and 26.3877 for 4, 8, 12, and 16 views, respectively, while training-view PSNR is higher for the four-view overfit case. This supports the paper’s dependence on sufficient view coverage for novel-view quality.

### Limitations

The paper states that similar-looking entities can confuse color-difference tracking, human segmentation limits the demonstrated object class, severe occlusion can break bounding-box tracking, and information outside tracked boxes may be learned into the background and cause ghosting. It also states that 16 cameras are still needed for wide viewing, that non-rigid and slow-motion edits are unsupported, and that illumination/re-lighting remains future work. The reviewer adds that the release recipe, raw metrics, camera calibration, data terms, and multi-seed uncertainty are insufficient for an independent audit from the public artifacts alone.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | ST-NeRF enables editable free-viewpoint video from a sparse 16-camera setup. | Author architectural claim | E1, E2, E3 | Supported as the proposed system and reported operating point; generality beyond the tested scenes is unverified. | High for source claim |
| C2 | Layered representation disentangles entity position, deformation, and appearance sufficiently for per-entity edits. | Author mechanism claim | E2, E3 | Method design and qualitative edits support the mechanism; no independent implementation test was run. | Medium-high |
| C3 | The complete pipeline outperforms listed baselines on Table 1. | Author empirical claim | E3, E4 | PSNR and LPIPS support a favorable comparison, but the printed SSIM and MAE columns conflict with the prose/caption. | Low-to-medium as a broad claim |
| C4 | Deformation, timestamp input, and layer-wise loss each contribute to the reported synthetic evaluation. | Author ablation claim | E3 | The ablation table supports component sensitivity in the stated setup; interactions and seeds are unknown. | Medium-high |
| C5 | The public repository provides a practical reproduction path. | Reviewer interpretation | E5 | Test code, configs, pretrained outputs, and dataset links improve inspectability, but execution was not performed and full data terms remain separate. | Medium |
| C6 | The layer abstraction is a useful bridge to modern geometry-consistent video and world-model evaluation. | Reviewer interpretation | E6 | Concrete conceptual overlap exists across the three related DEP entries; this is synthesis, not an author claim. | Medium |

## Methodology

- `Research objective`: Review one uniformly selected eligible arXiv paper source-first, preserve its evidence and limits, connect it to exactly three existing DEP entries, and generate a public-safe DEP-E manuscript.
- `Sources inspected`: Repaired local PDF and full-paper HTML, local metadata/provenance and public-safe cache summary, official arXiv metadata and HTML URLs, ACM DOI metadata, author project page, official ST-NeRF repository README/config/demo, live Black Lake README, live Black-Lake-Data README, and exactly three existing Black Lake manuscripts.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, treated each PDF parent as a paper unit, drew a zero-based `Get-Random` index, derived identity from the paper folder and readme, checked the public dedup index, logs, reports, lake-data, automation memory, relevant Black-Lake-Data entries, and recent same-paper markers, then reviewed public primary sources and related DEP content.
- `Inclusion criteria`: The selected unit needed a valid PDF and full-paper HTML after bounded repair; sources were included when they supported identity, method, metrics, limitations, implementation availability, public repository policy, or concrete conceptual overlap.
- `Exclusion criteria`: Prior DEP markers, matching IDs/DOIs/titles/slugs, same-paper recent markers, invalid or unrepaired source units, unsupported code claims, and source-file redistribution were excluded. The initial missing HTML was repaired rather than used as an abstract-only review.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, safety/ethics, and replication analysis.
- `Evidence handling`: Author claims, printed values, visual table observations, reviewer interpretations, and process evidence are separated. Metric directionality was checked against the rendered PDF rather than accepted from bolding or prose alone.
- `Extraction process`: Required preflight reported `pypdf` available and `pdftotext` unavailable. Missing-only extraction produced HTML text with `html-regex` and PDF text with `pypdf`; no source text was produced because the source package was unavailable. A Poppler-rendered page was visually inspected for Table 1.
- `Version control`: Primary paper is pinned to arXiv:2104.14786v1 and DOI 10.1145/3450626.3459756. Official code is referenced by its public repository and current README/config context; it was not executed.
- `Claim selection`: Priority went to the layer abstraction, scene parsing, renderer, training objective, editing operations, data/camera requirements, printed metrics, ablations, limitations, and reproduction boundary.
- `Cross-checking`: Identity was cross-checked across arXiv, the ACM DOI, the project page, and the official repository. Table 1 was checked in PDF text, HTML text, and a rendered PDF page. The printed discrepancy was preserved.
- `Random selection`: Zero-based index 34,230 of 75,964 unique parent-directory units from 75,967 PDFs; first draw accepted; duplicate exclusions 0; reselections 0.
- `Dedup/reselection validation`: No match in the public dedup index, Black Lake logs/reports/lake-data, automation memory, relevant Black-Lake-Data searches, or preceding 24-hour markers.
- `Cache methodology`: Central archive cache, normalized key `2104.14786`, missing-only mode, local repaired paper folder, public-safe summary fields only in this manuscript; local manifest and cache paths withheld.
- `Reviewer stance`: Critical source review, DEP-ready preservation, implementation translation, and bounded replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: ST-NeRF’s source identity, layered representation, training/rendering method, reported evaluation, limitations, code boundary, related-deposit synthesis, and safe implementation implications.
- `Temporal boundary`: Public and local source context inspected on 2026-08-18; primary paper version is arXiv:2104.14786v1.
- `Evidence limits`: No code, pretrained model, dataset, raw prediction, camera calibration, training run, or metric script was executed. The source package was unavailable. PDF text contains symbol-encoding noise.
- `Assumptions`: The arXiv PDF/HTML and ACM record describe the same work; the author project page and `DarlingHang/st-nerf` repository are the intended implementation context because the project page links the repository.
- `Constraints`: Original source locality, license review, privacy, public-safe records, and nonbinding use are mandatory. Dynamic-scene outputs must not be treated as ground truth or safety-certified simulation without separate validation.
- `Out of scope`: Production deployment, real-time claims, dataset redistribution, autonomous control, legal conclusions, and independent reproduction of the reported metrics.
- `Intended use`: Black Lake research deposition, evaluation planning, implementation ideation, and follow-up review.
- `Audience`: Neural rendering researchers, graphics engineers, synthetic-media evaluators, world-model researchers, and artifact reviewers.
- `Depth target`: Full schema-complete manuscript with explicit evidence and reproduction boundaries.
- `Reproducibility boundary`: The public code README and configs provide a starting point, but data access, environment pins, hardware, pretrained artifacts, and execution remain unverified in this review.
- `Operational boundary`: Only offline, authorized, synthetic, or public-data evaluation is contemplated; no generated video should directly drive consequential systems.
- `Data sensitivity`: Public scholarly and repository metadata; source documents and caches remain private.

## Observations

- `Observed pattern`: Treating each dynamic entity as a separate neural layer creates an explicit control surface between scene decomposition and rendering.
- `Technical implication`: The representation can support editing only where parsing, tracking, box geometry, and temporal correspondence remain reliable; control granularity is coupled to upstream perception quality.
- `Evidence tension`: The paper’s qualitative editing story is coherent, but the printed Table 1’s metric ordering conflicts with its bolding and superiority prose, demonstrating why raw tables and metric direction must be audited.
- `Cross-source pattern`: The related DEP set shows a progression from explicit layered neural scene control to geometry-consistent video latents and multi-view world-model state, but no one artifact proves the others’ empirical claims.
- `Open question`: Whether a layer contract can be generalized from human performers to arbitrary objects without replacing the human-specific parsing stage.

## Considerations

Use of ST-NeRF-like systems raises dataset consent, performer privacy, and licensing concerns because multi-view capture can encode identifiable people and environments. A public reproduction should use authorized or synthetic data, document camera calibration and capture consent, minimize raw media retention, and publish only derived metrics or demonstrations permitted by the source terms.

Operationally, the representation is expensive: the paper reports hours to days of training and around two minutes per 1920x1080 three-layer render. A product or benchmark should measure latency, memory, energy, and failure recovery separately from visual quality. Scene decomposition failures can yield plausible-looking but wrong occlusion, identity, or geometry, so provenance and abstention should be first-class outputs.

The official repository improves inspectability but does not prove reproducibility. The README pins an older PyTorch/CUDA environment, points to walking and taekwondo data, and includes demo commands. A clean-room run would still need verified dataset access, checkpoint hashes, exact configuration, dependency lock, GPU budget, expected outputs, and metric scripts.

## Strengths

- The layer abstraction unifies controllable editing with a continuous dynamic scene representation.
- The method makes the control path explicit: parse, anchor, deform, sample, render, then edit.
- The evaluation spans qualitative edits, baseline comparisons, component ablations, and camera-count sensitivity.
- The paper discloses important upstream failure conditions instead of presenting the renderer as universally robust.
- The project page and official repository expose a concrete code/data boundary for follow-up work.

## Weaknesses

- Human segmentation and tracking assumptions limit object generality and make failures upstream of the neural renderer.
- The 16-camera capture requirement and per-scene training cost constrain scale and deployment.
- The public reproduction boundary is incomplete: code exists, but data, environment, pretrained artifacts, and exact expected outputs were not validated here.
- The source’s Table 1 contains an unresolved metric-direction inconsistency affecting broad comparative claims.
- No multi-seed uncertainty, cross-dataset generalization, calibration, lighting robustness, or non-rigid-object evaluation was reported in the inspected sections.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish raw predictions and metric scripts | Evaluation integrity | Resolve Table 1 ambiguity and enable recomputation | Auditable comparisons | Release and maintenance burden | Recompute all table columns with explicit up/down directions |
| Replace human-only parsing with object-agnostic segmentation | Generality | Extend layers beyond performers | Broader scene coverage | More tracking ambiguity | Synthetic object benchmarks plus held-out real scenes |
| Add uncertainty and abstention to layer tracking | Robustness | Prevent confident edits when decomposition fails | Safer editing behavior | More model complexity | Occlusion, similar-color, lighting, and camera-dropout sweeps |
| Benchmark sparse-view and lighting stress | Operating boundary | Quantify camera and illumination dependence | Better deployment decisions | Larger capture/evaluation matrix | 16/12/8/4-view and controlled-light ablations |

## Potential Implementations

1. **Layered video review harness** — User: graphics researcher. Goal: compare layer decomposition, novel-view quality, and edit fidelity on synthetic scenes. Inputs: authorized multi-view frames, calibration, masks, and layer metadata. Outputs: per-layer renders, PSNR/SSIM/LPIPS, occlusion checks, and provenance. Risk controls: synthetic/public data only, no consequential use, and explicit abstention when tracking confidence is low.
2. **Offline scene-editing workstation** — User: visual-effects artist or media researcher. Goal: preview safe translation, duplication, retiming, hide/show, and transparency edits. Inputs: a pinned ST-NeRF checkpoint and licensed capture. Outputs: non-final preview video plus an edit manifest. Risk controls: watermark previews, preserve source provenance, and require human review before export.
3. **Geometry-consistency gate for generated video** — User: synthetic-media evaluator. Goal: test whether edited or generated clips preserve identity, depth ordering, temporal continuity, and camera consistency. Inputs: synthetic reference layers, generated frames, and camera trajectories. Outputs: slice metrics, failure clips, and a release recommendation. Risk controls: offline evaluation only and no claim of simulation fidelity without independent evidence.

## Three Ways to Exercise This Research

1. **Synthetic layer composition**: Build two simple animated shapes and a background, assign bounding boxes, apply translation/duplication/retiming metadata, and compare expected versus rendered ordering. Success is exact layer identity and temporal alignment; stop on ambiguous occlusion or missing provenance.
2. **Public-code smoke test**: Use the official walking demo only with authorized released data, a pinned environment, and no networked or consequential output. Success is a deterministic demo artifact matching the repository’s expected directory structure; stop if data terms, checkpoints, or dependency versions cannot be verified.
3. **Metric-direction audit**: Create a synthetic table with known higher-is-better and lower-is-better metrics, run a validator, and ensure bolding follows direction rather than source formatting. Success is a machine-readable discrepancy report; stop before treating a disputed metric as evidence of superiority.

## Example MVP Product

- `Product name`: Layered Scene Evidence Gate.
- `Target user`: Neural-rendering researcher, graphics engineer, or media review lead.
- `Problem`: Editable dynamic-scene outputs can look plausible while layer identity, occlusion, or metric claims are wrong.
- `Core workflow`: Ingest a public-safe manifest, validate layer metadata and source versions, render bounded synthetic edits, compute direction-aware metrics, surface failures, and require reviewer sign-off.
- `Data requirements`: Authorized or synthetic multi-view frames, calibration metadata, layer masks/bounding boxes, timestamps, checkpoint hashes, and metric definitions.
- `Architecture`: Local manifest loader, scene/layer validator, renderer adapter, metric-direction checker, failure ledger, and review report generator.
- `Success metrics`: Layer identity accuracy, edit consistency, view/temporal quality, metric reproducibility, failure detection rate, and reviewer time-to-decision.
- `Risk controls`: No raw source upload, local-only sensitive processing, synthetic defaults, access control, watermarked outputs, abstention on tracking uncertainty, and no autonomous actuation.
- `Limitations`: It cannot repair incorrect source decompositions or establish real-world visual fidelity from aggregate metrics.
- `MVP boundary`: Offline synthetic evaluation and authorized demos only; no production capture pipeline.
- `Evaluation plan`: Deterministic smoke tests, held-out camera views, occlusion and lighting perturbations, metric-direction unit tests, and manual review.
- `Failure modes`: Missing calibration, identity swaps, ghosting, unsupported object classes, time-index drift, GPU resource exhaustion, and misleading table claims.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Controllable Dynamic - DEP-E | Related DEP | Direct overlap in dynamic neural 3D representation and controllable appearance editing. | `.lake-data/DEP-E/DEP-E-20260813-Controllable Dynamic/controllable_dynamic_manuscript.md`; https://arxiv.org/abs/2309.11009 |
| VideoWeave Geometry - DEP-E | Related DEP | Connects video generation to implicit geometry latents and explicit spatial-consistency metrics. | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`; https://arxiv.org/abs/2606.14162 |
| HERMES World Model - DEP-E | Related DEP | Connects multi-view spatial representations to temporal 3D prediction and world-model evaluation. | `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md`; https://arxiv.org/abs/2501.14729 |
| NeRF | Foundational method | Provides the neural radiance-field baseline extended by ST-NeRF. | https://arxiv.org/abs/2003.08934 |
| Multi-View Neural Human Rendering | Related method and code context | The official repository credits this work as a code source and conceptual neighbor. | https://github.com/wuminye/NHR |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2104.14786 | Identity, abstract, authors, version, license context | 2026-08-18 | Public metadata; local copy withheld |
| R2 | https://arxiv.org/html/2104.14786 | Full method, evaluation, limitations, and references | 2026-08-18 | Verified full-paper HTML; not redistributed |
| R3 | https://arxiv.org/pdf/2104.14786 | PDF integrity, figures, and visual Table 1 inspection | 2026-08-18 | Verified PDF; not uploaded |
| R4 | https://doi.org/10.1145/3450626.3459756 | ACM venue and publication metadata | 2026-08-18 | DOI locator |
| R5 | https://jiakai-zhang.github.io/st-nerf/ | Project page, code locator, partial data statement | 2026-08-18 | Author context |
| R6 | https://github.com/DarlingHang/st-nerf | Official README, environment, configs, demo, and data boundary | 2026-08-18 | Inspected; not executed |
| R7 | `.lake-data/DEP-E/DEP-E-20260813-Controllable Dynamic/controllable_dynamic_manuscript.md` | Related dynamic neural 3D synthesis | 2026-08-18 | Existing Black Lake artifact |
| R8 | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Related geometry-consistent video synthesis | 2026-08-18 | Existing Black Lake artifact |
| R9 | `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` | Related multi-view spatiotemporal world model | 2026-08-18 | Existing Black Lake artifact |

## Appendix

- Selection provenance: 75,967 PDFs; 75,964 unique parent units; zero-based draw 34,230; first draw accepted; duplicate exclusions 0; reselections 0.
- Source-gate provenance: initial partial unit repaired once; final PDF and full-paper HTML passed all required checks; source package unavailable.
- Cache provenance: initial miss, missing-only local extraction, final `cached`; `pypdf` and `html-regex` succeeded; source text absent.
- Dedup provenance: no match in the public pointer, local artifacts, automation memory, relevant Black-Lake-Data search, or recent same-paper window.
- Public-output policy: only generated Markdown/log/index artifacts are intended for repository submission; no `.source/` directory is created.
