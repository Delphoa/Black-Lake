---
title: "FEMOT Tracking Review - DEP-E"
generated_at: "2026-07-20 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of RGB-event multi-object tracking and benchmark design."
source_status: "verified complete local PDF, official full-paper HTML, and metadata HTML inspected; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-20"
temporal_cutoff: "Sources and repository context inspected through the batch invocation."
primary_url: "https://arxiv.org/abs/2606.14094"
stable_identifier: "arXiv:2606.14094v1; DOI:10.48550/arXiv.2606.14094"
deployment_job_id: "BLAD-2200-20260720-8636EDC7"
deployment_item_id: "BLAD-2200-20260720-8636EDC7-P04"
confidence_summary: "High for source transcription; medium for benchmark conclusions; low for cross-platform deployment and subject-governance evidence."
distribution_notes: "No source document, dataset, media, code, cache, extracted text, verification record, or local path is redistributed."
---

# FEMOT Tracking Review - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Metadata | HTML | 2606.14094v1 | https://arxiv.org/abs/2606.14094 | Metadata only. | 2026-07-20 | Inspected |
| S2 | Full paper | Primary | HTML | 2606.14094v1 | https://arxiv.org/html/2606.14094 | Local verified copy withheld. | 2026-07-20 | Inspected in full |
| S3 | PDF | Primary | PDF | 2606.14094v1 | https://arxiv.org/pdf/2606.14094 | Local verified copy withheld. | 2026-07-20 | Integrity checked |
| S4 | Official project | Implementation locator | Repository | public state | https://github.com/Event-AHU/FEMOT | Not executed; rights not inferred. | 2026-07-20 | Locator inspected in paper |
| S5 | iKalibr DEP | Related | Markdown | DEP-E-20260714 | `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` | Synthesis only. | 2026-07-20 | Inspected |
| S6 | Stereo Lane DEP | Related | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-Stereo Lane Detection/stereo_lane_detection_manuscript.md` | Synthesis only. | 2026-07-20 | Inspected |
| S7 | HERMES DEP | Related | Markdown | DEP-E-20260712 | `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` | Synthesis only. | 2026-07-20 | Inspected |
| S8 | Workflow evidence | Process | Private record | `BLAD-2200-20260720-8636EDC7-P04` | Local path withheld | Randomness, dedup, repair, integrity. | 2026-07-20 | Verified |

Authors: Shiao Wang, Xiao Wang, Chao Wang, Yitao Li, Menghao Liu, Bo Jiang, Yaowei Wang, Yonghong Tian, and Jin Tang. Submitted 2026-06-12. Deployment job `BLAD-2200-20260720-8636EDC7`; item `BLAD-2200-20260720-8636EDC7-P04`.

## Evidence Ledger

| ID | Source | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|
| E1 | S1 | Identity, authors, date, DOI | Canonical metadata | High | No result evidence |
| E2 | S2/S3 Sections 1 and 4 | DVS346, 100 sequences, 200K frames, 14.58K trajectories, 0.42M boxes, 14 attributes | Benchmark scale and protocol | High for transcription | No independent label/privacy audit |
| E3 | S2 Section 3 | RGB/event branches, amplitude-phase fusion, temporal memory | Method reconstruction | High | No execution |
| E4 | S2 Section 5 | FEMOT and DSEC-MOT results and ablations | Author performance claims | High for transcription | Author-controlled evaluation |
| E5 | S2 Section 5.6 | Fixed event density and absent language modality | Disclosed limits | High | Not exhaustive |

## Executive Summary

FEMOT combines a large synchronized RGB-event tracking benchmark with FEMOTR, a frequency-aware multimodal transformer. The evidence supports meaningful gains on the proposed benchmark and strong association on DSEC-MOT, but not universal superiority: detection quality remains limiting on DSEC-MOT, capture and sensor diversity are bounded, and privacy/consent governance is not established in the inspected paper. The most responsible derivative is an offline auditor, not an unqualified surveillance deployment.

## Detailed Summary

The benchmark covers people and vehicles across day/night, indoor/outdoor, moving-camera, fast-motion, low-light, overexposure, crowd, scale, and entry/exit conditions. Trained volunteers annotated MOT-style records and multiple verification passes were reported. FEMOTR uses RGB, event, and concatenated features, amplitude/phase attention in the frequency domain, and memory-based temporal interaction. Standard metrics include HOTA, DetA, AssA, MOTA, IDF1, and MOTP via TrackEval.

## Key Claims and Evidence

| Claim | Evidence | Assessment |
|---|---|---|
| FEMOT is a substantial RGB-event MOT benchmark. | E2 | Supported for stated counts; external audit absent. |
| FEMOTR improves the strongest cited FEMOT baseline. | E4: HOTA 44.0 to 48.9; MOTA 45.4 to 52.0; IDF1 54.9 to 62.0. | Supported as author-reported. |
| Fusion and dual modality matter. | E4 ablations: no fusion HOTA 44.0; RGB-only HOTA 42.5 vs 48.9 dual. | Supported within tested setup. |
| General tracking superiority is established. | DSEC-MOT has best AssA 67.8 but lower HOTA/IDF1 than selected baselines. | Not supported universally. |

## Methodology

This review enforced a complete-source gate, read the full paper, cross-checked the PDF, separated author claims from interpretation, traced numerical results to sections/tables, inspected three related DEPs, and recorded uniform selection and repository-wide dedup evidence. It did not execute code, download the benchmark, or replicate experiments.

## Scope, Constraints, and Assumptions

- Scope: benchmark design, fusion architecture, temporal association, metrics, limitations, and responsible implementation.
- Constraint: author-reported results are not independent validation.
- Constraint: code/data availability was located but not audited or redistributed.
- Assumption: public arXiv version v1 is the reviewed version.
- Governance: subject consent, capture notices, retention, demographic coverage, and access controls were not established in inspected evidence.

## Observations

- Frequency decomposition is an explicit hypothesis about complementary low-frequency appearance and high-frequency motion/contour cues.
- HOTA decomposition helps distinguish detection and association, preventing a single aggregate metric from hiding failure modes.
- Frequent entry/exit and scale variation dominate reported attribute counts, making lifecycle and small-object tests important.
- Fixed event accumulation is mismatched to variable motion speed by the authors' own limitation.

## Considerations

Any operational use should require lawful capture, consent/notice review, calibration evidence, dataset-rights review, challenge-sliced performance, abstention on degraded synchronization, provenance, access control, retention limits, and human escalation. Tracking identities across time is sensitive even when biometric recognition is not explicit.

## Strengths

- Paired benchmark and method support controlled comparisons.
- Dataset scale and attribute taxonomy are unusually concrete for RGB-event MOT.
- Standard metrics and ablations expose detection/association contributions.
- DSEC-MOT results include a meaningful negative boundary rather than only wins.

## Weaknesses

- No independent replication or dataset audit.
- One principal sensor/capture ecology limits transfer claims.
- Fixed event accumulation does not adapt to motion density.
- Privacy, consent, demographic, and retention evidence is incomplete.

## Potential Improvements

- Evaluate calibration/timestamp perturbations and missing-modality recovery.
- Adapt event windows to motion and event density with preregistered tests.
- Report compute, latency, energy, and hardware alongside accuracy.
- Add cross-site, cross-sensor, demographic, privacy, and annotation-consistency audits.
- Publish failure slices and confidence-calibrated abstention thresholds.

## Potential Implementations

1. An offline challenge-slice dashboard with immutable run manifests.
2. A sensor-synchronization perturbation harness linked to tracking metrics.
3. A dataset-card validator for consent, rights, capture, retention, and annotation provenance.
4. A downstream world-model gate that passes uncertainty and provenance with tracks.

## Three Ways to Exercise This Research

1. Recalculate metric deltas from published tables and verify every denominator.
2. Sweep bounded frame-event offsets and event accumulation windows on authorized data.
3. Compare RGB-only, event-only, and fused variants across every challenge attribute.

## Example MVP Product

**FEMOT Evidence Gate** is an offline evaluator for authorized RGB-event tracking research. Inputs are user-supplied predictions, references, sensor manifests, and lawful-use attestations; the service never supplies source media. It produces HOTA/DetA/AssA/MOTA/IDF1 slices, synchronization stress tests, identity-switch timelines, calibration alerts, and a signed provenance receipt. Acceptance requires minimum worst-slice performance, bounded offset sensitivity, declared data rights, and zero source redistribution.

## Related Research and Reading

1. iKalibr Calibration - sensor timing/extrinsic integrity before fusion.
2. Stereo Lane Detection - temporal priors, recovery tests, and compute evidence.
3. HERMES World Model - downstream geometric representation and multimodal evidence gates.

## Source References

- https://arxiv.org/abs/2606.14094
- https://arxiv.org/html/2606.14094
- https://arxiv.org/pdf/2606.14094
- https://doi.org/10.48550/arXiv.2606.14094
- https://github.com/Event-AHU/FEMOT
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Stereo%20Lane%20Detection
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model

## Appendix

Selection used uniform index 48,183 from 75,776 unique PDF-parent units enumerated from 75,779 PDFs. Repository, companion-data, memory, 24-hour, and current-job scans produced zero duplicate exclusions and zero reselections. The PDF-only unit was repaired with official full-paper and metadata HTML; all integrity thresholds passed. No source document was staged or uploaded.
