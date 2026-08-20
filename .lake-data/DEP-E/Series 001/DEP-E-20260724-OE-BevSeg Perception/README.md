# DEP-E-20260724-OE-BevSeg Perception

#bird-eye-view #semantic-segmentation #autonomous-driving #sensor-fusion #mamba #computer-vision #nuScenes #calibration #reproducibility #source-first-research

This public-safe DEP-E preserves a source-grounded review of OE-BevSeg, a camera/radar/LiDAR framework for bird's-eye-view vehicle semantic segmentation. The selected local paper unit was repaired from a valid-PDF-only state to a verified complete PDF/full-paper-HTML/source bundle before review. All original source documents, extracted text, caches, verification records, and temporary page renders remain local and were not uploaded. No `.source/` directory is included.

## Contents

- `README.md` - deposit inventory, context, synthesis, source policy, and attribution.
- `oe_bevseg_perception_manuscript.md` - schema-complete manuscript covering paper identity, evidence, method, results, limitations, official code, related DEP synthesis, implementation paths, and a replication checklist.

## Summary of Items

### `oe_bevseg_perception_manuscript.md`

The manuscript reviews the Environment-aware BEV Compressor, Bi-Surround Scan, Center-Informed Object Enhancement, multi-task losses, and camera/radar/LiDAR fusion. It preserves the paper's 52.6 camera-only IoU, 58.0 radar-fusion IoU, 65.3 LiDAR-fusion IoU, component/range ablations, training setup, selected qualitative evidence, and later IEEE DOI.

The review distinguishes printed evidence from reviewer interpretation. It records that the full Table II model grows from 62.27M to 80.37M parameters, that comparisons use nonuniform architectures and recipes, and that no repeated-seed, uncertainty, calibration-error, sensor-fault, latency, memory, energy, or closed-loop evidence is supplied. It also inspects the official repository at a pinned commit and identifies gaps between the paper recipe and the released sample scripts/dependencies/multimodal path.

### `README.md`

This file provides a public-safe deposit boundary, item inventory, source-withholding statement, relationship summary, and annotated source URLs.

## Insights and Relevance

OE-BevSeg's durable design pattern is the combination of a shared BEV coordinate frame, range-aware global sequence modeling, object-centric auxiliary supervision, and optional multi-sensor fusion. The range table supports the paper's motivation more directly than its aggregate headline because the method improves every displayed distance interval, including the difficult 35-50 m band. The largest numerical gains, however, come from adding radar or LiDAR, making calibration and sensor-health provenance first-class concerns.

Exactly three related Black Lake entries sharpen that boundary. HERMES World Model extends the shared six-camera BEV representation into scene understanding and future point-cloud generation. Stable Diffusion Depth supplies a same-dataset analogue for adverse-condition slicing and the difference between curated visuals and aggregate robustness evidence. iKalibr Calibration supplies the spatial/temporal calibration layer that camera/radar/LiDAR fusion presupposes. Together they motivate an offline BEV evidence gate that combines range and condition slices, calibration perturbations, resource telemetry, release-to-paper checks, and fail-closed unsupported states before any live-system consideration.

## Attribution Block

- Source URL: https://arxiv.org/abs/2407.13137
  - Applies to: `oe_bevseg_perception_manuscript.md`
  - Notes: Canonical arXiv metadata for title, authors, date, subject, and abstract.
- Source URL: https://arxiv.org/pdf/2407.13137
  - Applies to: `oe_bevseg_perception_manuscript.md`
  - Notes: Public equivalent of the locally verified complete PDF; the file was withheld.
- Source URL: https://arxiv.org/html/2407.13137
  - Applies to: `oe_bevseg_perception_manuscript.md`
  - Notes: Official full-paper HTML used for source-first cross-checking; the local file was withheld.
- Source URL: https://arxiv.org/e-print/2407.13137
  - Applies to: `oe_bevseg_perception_manuscript.md`
  - Notes: Public source-package endpoint used for table and method inspection; the local archive was withheld.
- Source URL: https://doi.org/10.1109/TITS.2025.3558146
  - Applies to: `oe_bevseg_perception_manuscript.md`
  - Notes: IEEE journal DOI.
- Source URL: https://ieeexplore.ieee.org/document/10964637
  - Applies to: `oe_bevseg_perception_manuscript.md`
  - Notes: IEEE publication record.
- Source URL: https://github.com/SunJ1025/OE-BevSeg/commit/ccd4a0876899ad993bee769692330181d5f66503
  - Applies to: `oe_bevseg_perception_manuscript.md`
  - Notes: Pinned official implementation surface; code was inspected but not executed.
- Source URL: https://www.nuscenes.org/
  - Applies to: `oe_bevseg_perception_manuscript.md`
  - Notes: Dataset authority; no dataset files were collected.
- Repository file: `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md`
  - Applies to: `oe_bevseg_perception_manuscript.md`
  - Notes: Related DEP on a shared six-camera BEV interface for 3D understanding and future generation; primary basis https://arxiv.org/abs/2501.14729.
- Repository file: `.lake-data/DEP-E/DEP-E-20260718-Stable Diffusion Depth/stable_diffusion_depth_manuscript.md`
  - Applies to: `oe_bevseg_perception_manuscript.md`
  - Notes: Related DEP on nuScenes adverse-condition evaluation; primary basis https://arxiv.org/abs/2403.05056.
- Repository file: `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md`
  - Applies to: `oe_bevseg_perception_manuscript.md`
  - Notes: Related DEP on camera/radar/LiDAR spatiotemporal calibration; primary basis https://arxiv.org/abs/2407.11420.
