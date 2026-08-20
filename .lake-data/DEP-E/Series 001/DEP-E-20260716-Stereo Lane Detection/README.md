# DEP-E-20260716-Stereo Lane Detection

#computer-vision #stereo-vision #lane-detection #disparity #autonomous-driving #embedded-systems #research-review

This public-safe DEP-E preserves a source-grounded review of a temporally propagated dense-disparity and vanishing-point approach to multiple-lane detection. The deposit contains generated Markdown only. The reviewed PDF, ar5iv full-paper rendering, official metadata HTML, extracted text, cache records, and local verification records remain withheld in the source archive.

## Contents

- `README.md` - DEP inventory, public-safe context, synthesis, and attribution.
- `stereo_lane_detection_manuscript.md` - schema-complete research manuscript covering the algorithm, evidence, metrics, limitations, implementation relevance, related DEP entries, and workflow provenance.

## Summary of Items

### `README.md`

Records the public-safe purpose, contents, source boundaries, principal findings, and source attribution.

### `stereo_lane_detection_manuscript.md`

Reconstructs BRISK initialization, RANSAC road-model fitting, temporal disparity-range propagation, dynamic-programming vanishing-point estimation, bilateral/Sobel processing, lane visualization, KITTI counts, and runtime claims. It distinguishes author results from reviewer interpretation and preserves random selection, dedup, repair, cache, and no-source-upload evidence.

## Insights and Relevance

The reusable systems idea is to use the previous frame's disparity-derived road model to constrain the next frame's stereo search. The paper reports a roughly 37% disparity-stage runtime reduction while improving total lane-count errors from 47 to 24 across six selected KITTI sequences. This is an interpretable temporal-compute trade: prior geometry narrows future work.

The evidence is preliminary for deployment. The 99% result uses manually counted lanes rather than a standard labeled benchmark, the paper compares chiefly against its own prior pipeline, and the complete implementation still takes 0.21 seconds per 1242-by-375 frame on a single CPU thread. Temporal propagation can also carry a bad road model forward, yet recovery, calibration drift, dropped frames, and adverse conditions are not quantified.

iKalibr adds calibration/timing integrity; HSD FTI-FDet adds field-lighting and embedded-resource evidence; Self Learned IDC shows that perception latency and uncertainty become safety concerns when outputs feed driving control. Together they motivate an offline lane-perception auditor with fixed denominators, temporal-reset tests, device profiling, and explicit abstention.

## Attribution Block

- Primary paper: Han Ma; Yixin Ma; Jianhao Jiao; M. Usman Maqbool Bhutta; Mohammud Junaid Bocus; Lujia Wang; Ming Liu; Rui Fan, *Multiple Lane Detection Algorithm Based on Optimised Dense Disparity Map Estimation*, 2018.
- arXiv record: https://arxiv.org/abs/1808.09128v1
- Full-paper fallback: https://ar5iv.labs.arxiv.org/html/1808.09128
- PDF: https://arxiv.org/pdf/1808.09128
- Publisher DOI: https://doi.org/10.1109/IST.2018.8577122
- arXiv DOI: https://doi.org/10.48550/arXiv.1808.09128
- Review artifact: generated source-grounded analysis; not an author-supplied reproduction.
- Source handling: original source documents, extraction products, and archive records were withheld locally; no source file was uploaded.
- Related Black Lake artifacts: `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md`; `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md`; `.lake-data/DEP-E/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md`.
