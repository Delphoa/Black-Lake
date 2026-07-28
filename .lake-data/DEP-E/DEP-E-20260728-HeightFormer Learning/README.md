# DEP-E-20260728-HeightFormer Learning

#heightformer #height #prediction #research-review

Public-safe context: job `BLAD-2200-20260728-EB036F17`, item `BLAD-2200-20260728-EB036F17-P07`, uniformly selected `arXiv:2503.10777`. The archive unit reached a verified complete PDF-plus-full-paper-HTML state before review after one bounded local archive repair. Local paths, exact execution times, source documents, datasets, and executable research artifacts are withheld.

## Contents

- `README.md` - context, inventory, source boundary, synthesis, and attribution.
- `heightformer_learning_manuscript.md` - schema-complete review of the paper, its evidence, limitations, and bounded implementation paths.

No `.source/` exists. No PDF, HTML, source archive, cache, extracted source text, dataset, model, credential, or executable artifact is deposited.

## Summary of Items

The paper studies heightformer, height, prediction, voxel. Its abstract frames the contribution as follows: Roadside vision centric 3D object detection has received increasing attention in recent years. It expands the perception range of autonomous vehicles, enhances the road safety. Previous methods focused on predicting per-pixel height rather than depth, making significant gains in roadside visual perception. While it is limited by the perspective property of near-large and far-small on image features, making it difficult for network to understand real dimension of objects in the 3D world. BEV features and voxel features present the real distribution of objects in 3D world compared to the image features. However, BEV features tend to lose details due to the lack of explicit height information, and voxel features are computationally expensive. Inspired by this insight, an efficient framework learning height prediction in voxel features via transformer is proposed, dubbed HeightFormer. It groups the voxel features into local height sequences, and utilize attention mechanism to obtain height distribution prediction. Subsequently, the local height sequences are reassembled to generate accurate 3D features. The proposed method is applied to two large-scale roadside benchmarks, DAIR-V2X-I and Rope3D. Extensive experiments are performed and the HeightFormer outperforms the state-of-the-art methods in roadside vision centric 3D object detection task. The full paper was inspected beyond the abstract, including introduction, method, evaluation, limitations/discussion, conclusion, and references. Reported results remain author claims unless independently reproduced.

## Insights and Relevance

The three related DEPs connect the selected work to UAV Visual Localization - DEP-E, OE-BevSeg Perception - DEP-E, and Stereo Lane Detection - DEP-E. Their concrete shared concepts include 3D roadside perception, height-aware geometry, visual localization, stereo and BEV evidence. The combined implementation lesson is to preserve provenance, establish baseline parity, probe failure boundaries, and make downstream use review-gated when evidence is incomplete.

## Attribution Block

- https://arxiv.org/abs/2503.10777 - official metadata and public source locators.
- https://arxiv.org/html/2503.10777 - verified full paper; local copy withheld.
- https://arxiv.org/pdf/2503.10777 - verified PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2503.10777 - durable paper identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-UAV%20Visual%20Localization - related DEP: UAV Visual Localization - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260716-UAV Visual Localization/uav_visual_localization_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260724-OE-BevSeg%20Perception - related DEP: OE-BevSeg Perception - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260724-OE-BevSeg Perception/oe_bevseg_perception_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Stereo%20Lane%20Detection - related DEP: Stereo Lane Detection - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260716-Stereo Lane Detection/stereo_lane_detection_manuscript.md`.
- Source files: PDF, full-paper HTML, metadata HTML, integrity records, and local companions; all withheld locally with zero source-document uploads.
