# DEP-E-20260714-iKalibr Calibration

#robotics #sensor-calibration #multi-sensor-fusion #continuous-time #autonomous-systems #arxiv

This DEP-E preserves a source-grounded review of iKalibr, a targetless offline framework for jointly estimating spatial extrinsics and temporal offsets across resilient integrated inertial sensor suites. The public deposit contains generated Markdown only. The reviewed PDF, official full-paper HTML, metadata page, TeX/source package, extracted text, and cache records remain withheld in the private local source archive.

## Contents

- `README.md` — DEP inventory, public-safe context, synthesis summary, and final source attribution.
- `ikalibr_calibration_manuscript.md` — schema-complete research manuscript covering source metadata, evidence, method, experiments, limitations, implementation paths, related DEP entries, and selection/dedup provenance.

No `.source/` directory exists. Original source files were intentionally not deposited.

## Summary of Items

### `README.md`

Defines the deposit boundary and makes the no-source-upload policy explicit. It maps every public source locator used by the manuscript to the generated artifact.

### `ikalibr_calibration_manuscript.md`

Reviews arXiv:2407.11420v2 and the later IEEE Transactions on Robotics record. It reconstructs iKalibr's dynamic initialization, adaptive continuous-time B-splines, sensor-specific residuals, global factor graph, progressive batch refinement, real-world evaluation, computation profile, and disclosed limitations. It also documents the uniform random selection, repository-wide dedup checks, local source repair, and exactly three related DEP entries.

## Insights and Relevance

iKalibr is best understood as an upstream coordinate-and-time integrity layer for embodied systems. Its unified factor graph links raw IMU, radar, LiDAR, and camera evidence to one reference frame; HERMES, LA-Pose, and Self-Learned IDC show three downstream consumers of that integrity—world modeling, ego-motion representation, and driving control. The paper's strongest value is the coupling of rigorous initialization with heterogeneous continuous-time residuals. Its principal adoption constraints are equally concrete: six-degree-of-freedom excitation, limited physical ground truth, small-field-of-view LiDAR degeneracy, weakly observable IMU intrinsics, and high camera/SfM computation cost.

## Attribution Block

- Source URL: https://arxiv.org/abs/2407.11420
  - Applies to: `ikalibr_calibration_manuscript.md`
  - Notes: Canonical metadata, abstract, version history, arXiv DOI, and public source locators.
- Source URL: https://arxiv.org/html/2407.11420
  - Applies to: `ikalibr_calibration_manuscript.md`
  - Notes: Official full-paper HTML inspected for methods, experiments, limitations, tables, and appendices.
- Source URL: https://arxiv.org/pdf/2407.11420
  - Applies to: `ikalibr_calibration_manuscript.md`
  - Notes: Public equivalent of the verified local PDF; the PDF was not deposited.
- Source URL: https://arxiv.org/e-print/2407.11420
  - Applies to: `ikalibr_calibration_manuscript.md`
  - Notes: Official source-package locator; the source archive and extracted text were not deposited.
- Source URL: https://doi.org/10.48550/arXiv.2407.11420
  - Applies to: `ikalibr_calibration_manuscript.md`
  - Notes: arXiv-issued persistent DOI.
- Source URL: https://doi.org/10.1109/TRO.2025.3532506
  - Applies to: `ikalibr_calibration_manuscript.md`
  - Notes: IEEE Transactions on Robotics publication DOI.
- Source URL: https://github.com/Unsigned-Long/iKalibr
  - Applies to: `ikalibr_calibration_manuscript.md`
  - Notes: Official implementation repository linked by the paper; inspected at public commit `7785ce756290b0113cdaa0ce3037d5e3d6bae0d2`, not executed.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`; `ikalibr_calibration_manuscript.md`
  - Notes: Live repository authority for DEP class, filing, source handling, attribution, and commit rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md`; `ikalibr_calibration_manuscript.md`
  - Notes: Live container and publications-index authority for DEP-E entries.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `ikalibr_calibration_manuscript.md`
  - Notes: Live authority read before using the companion repository for deduplication context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model/hermes_world_model_manuscript.md
  - Applies to: `ikalibr_calibration_manuscript.md`
  - Notes: Related DEP on multi-camera/LiDAR world modeling and shared spatial representation.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-LA-Pose%20Latent%20Action/la_pose_latent_action_manuscript.md
  - Applies to: `ikalibr_calibration_manuscript.md`
  - Notes: Related DEP on driving-video camera pose and latent ego-motion representation.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Self%20Learned%20IDC/self_learned_idc_manuscript.md
  - Applies to: `ikalibr_calibration_manuscript.md`
  - Notes: Related DEP on sensor-informed autonomous-driving decision and control.
- Source URL: https://github.com/ethz-asl/kalibr
  - Applies to: `ikalibr_calibration_manuscript.md`
  - Notes: Official Kalibr repository used as a target-based visual-inertial baseline locator.
- Source URL: https://github.com/APRIL-ZJU/lidar_IMU_calib
  - Applies to: `ikalibr_calibration_manuscript.md`
  - Notes: OA-Calib/LI-Calib repository and dataset locator used as a LiDAR-IMU baseline.
- Source URL: https://arxiv.org/abs/2204.09170
  - Applies to: `ikalibr_calibration_manuscript.md`
  - Notes: Mix-Cal paper locator used as a multi-IMU baseline.
- Source URL: https://doi.org/10.1007/s40864-021-00154-7
  - Applies to: `ikalibr_calibration_manuscript.md`
  - Notes: X-RIO paper locator used as a radar-inertial baseline.
