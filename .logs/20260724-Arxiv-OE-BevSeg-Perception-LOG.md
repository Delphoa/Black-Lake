# Arxiv DEP Job Log: OE-BevSeg Perception

## Public-Safe Run Summary

- Deposit date: 2026-07-24.
- Selected paper: Jian Sun, Yuqi Dai, Chi-Man Vong, Qing Xu, Shengbo Eben Li, Jianqiang Wang, Lei He, and Keqiang Li, *OE-BevSeg: An Object Informed and Environment Aware Multimodal Framework for Bird's-eye-view Vehicle Semantic Segmentation*.
- arXiv: https://arxiv.org/abs/2407.13137.
- Journal DOI: https://doi.org/10.1109/TITS.2025.3558146.
- Official implementation inspected: https://github.com/SunJ1025/OE-BevSeg/commit/ccd4a0876899ad993bee769692330181d5f66503.
- Source policy: the complete paper bundle, extracted text, cache, integrity records, and temporary page renders were withheld locally; no source file or `.source/` directory was uploaded.

## Random Selection

- Method: enumerate local PDFs with `rg --files -g "*.pdf"`, treat each unique PDF parent directory as one paper unit, and select one zero-based index uniformly with PowerShell `Get-Random`.
- PDF count: 75,780.
- Unique parent-paper units: 75,777.
- Selected zero-based index: 20,731.
- Duplicate exclusions: 0.
- Reselections: 0.
- Acceptance: first draw accepted.

## Dedup Validation

No matching arXiv ID, publisher DOI, normalized title, slug, prior Arxiv DEP log/report/deposit, dedup-index entry, automation-memory entry, substantive Black-Lake-Data result, or same-paper marker within 24 hours was found. One author-inventory row was metadata only and did not count as a research deposit.

## Source Integrity and Cache

- Initial source state: `partial`; the PDF was valid, but full-paper HTML was missing.
- Repair: one bounded official arXiv companion-bundle attempt completed without retries or partial files.
- Final source state: `complete`.
- PDF verification: 8,611,139 bytes; valid header and trailing EOF; 14 pages.
- Full-paper HTML verification: 698,205 bytes; 102,901 body characters; document marker present; five heading/section markers; five paper-structure terms.
- Additional local artifacts: metadata HTML and an 18-entry valid TeX/source archive.
- Cache: initial miss to `cached` in missing-only mode.
- Extractors: `pypdf`, HTML extraction, and `tarfile` succeeded.
- Fallback: `pdftotext` unavailable; `pypdf` succeeded.
- Cache outputs: 57,733 PDF-text bytes, 93,976 HTML-text bytes, and 97,727 source-text bytes.

## Review Outcome

The paper reports 52.6 IoU for camera-only BEV vehicle segmentation, 58.0 with radar, and 65.3 with LiDAR. The strongest evidence supports the printed table values and range-conditioned gains. The main constraints are cross-method comparison confounds, no repeated-seed uncertainty, a 62.27M-to-80.37M parameter increase for the full Table II row, no end-to-end resource evidence, no calibration/sensor-fault stress, and a public repository that does not expose a paper-matched executable recipe from the inspected scripts and dependencies.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` - shared six-camera BEV representation for 3D understanding and future generation.
2. `.lake-data/DEP-E/DEP-E-20260718-Stable Diffusion Depth/stable_diffusion_depth_manuscript.md` - nuScenes adverse-condition slicing and robustness-evidence boundaries.
3. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` - spatial/temporal calibration provenance for camera/radar/LiDAR fusion.

## Output Paths

- `.logs/20260724-Arxiv-OE-BevSeg-Perception-LOG.md`
- `.logs/20260724-Arxiv-OE-BevSeg-Perception-PHASE-LOG.md`
- `.reports/BL-Arxiv-OE-BevSeg-Perception-20260724/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260724-OE-BevSeg Perception/README.md`
- `.lake-data/DEP-E/DEP-E-20260724-OE-BevSeg Perception/oe_bevseg_perception_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. Does Bi-Surround Scan retain its gain against matched-parameter forward, bidirectional, cross-scan, and shuffled-order baselines across repeated seeds?
2. How do the radar and LiDAR gains change under measured extrinsic/time error, sensor dropout, stale frames, rain, night, and long-range occlusion?
3. Can the authors publish a paper-matched environment, split manifest, configuration, checkpoint, expected-output bundle, and resource profile that executes all three modality paths?

## Challenges

1. The paper's scene-split wording and released scripts do not expose one exact, paper-matched reproduction lineage.
2. Aggregate IoU and selected figures do not establish uncertainty, condition coverage, calibration robustness, or live-vehicle safety.
3. Mamba's efficiency motivation is unsupported by end-to-end latency, memory, energy, or throughput, while the full model materially increases parameters.
