# Report-Mark: FEMOT RGB-Event Tracking

- Deployment job ID: `BLAD-2200-20260720-8636EDC7`
- Deployment item ID: `BLAD-2200-20260720-8636EDC7-P04`
- Review date: 2026-07-20

## Source Metadata

| Field | Value |
|---|---|
| Paper | *FEMOT: Multi-Object Tracking using Frame and Event Cameras* |
| Authors | Shiao Wang; Xiao Wang; Chao Wang; Yitao Li; Menghao Liu; Bo Jiang; Yaowei Wang; Yonghong Tian; Jin Tang |
| Identifier | arXiv:2606.14094v1; DOI:10.48550/arXiv.2606.14094 |
| Submitted | 2026-06-12 |
| Record | https://arxiv.org/abs/2606.14094 |
| Full paper | https://arxiv.org/html/2606.14094 |
| PDF | https://arxiv.org/pdf/2606.14094 |
| Official code/data locator | https://github.com/Event-AHU/FEMOT |
| Source state | Verified complete after bounded official-source repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260720-8636EDC7`; `BLAD-2200-20260720-8636EDC7-P04` |

## Concise Research Notes

FEMOT contributes both a benchmark and FEMOTR, an RGB-event tracker. The benchmark uses a DVS346 camera and contains 100 sequences, about 200,000 frames, 14,580 trajectories, 420,000 boxes, people and vehicles, and 14 challenge attributes. Trained volunteers annotated the data with multiple verification rounds. FEMOTR separates RGB, event, and concatenated branches; decomposes features into amplitude and phase for attention-based fusion; and uses a dynamic temporal interaction module with long-term memory for association.

On FEMOT, the paper reports FEMOTR improving over its strongest cited MeMOTR baseline from 44.0 to 48.9 HOTA, 45.4 to 52.0 MOTA, and 54.9 to 62.0 IDF1. Removing frequency fusion lowers HOTA to 44.0 and IDF1 to 54.9; dual-modal input improves HOTA from 42.5 to 48.9 over the RGB-only variant. On DSEC-MOT, association accuracy reaches 67.8, while HOTA and IDF1 remain below SpikeMOT and Samba. These are author-reported, non-independent results.

Limitations include fixed event accumulation despite motion-dependent density, no language modality, no inspected privacy/consent protocol for public-space subjects, and uncertain transfer beyond the captured environments and sensor stack. Dataset availability is stated, but this review did not download, execute, or audit the code/data release.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Full-paper Sections 1 and 4 | Dataset scale, sensor, categories, attributes, annotation protocol | No independent audit of labels or subject governance |
| Sections 3 and 5 | Architecture, metrics, benchmark and ablation results | Author evaluation; compute and reproducibility not independently verified |
| Section 5.6 | Fixed event-density and missing-language limitations | Other deployment risks are reviewer interpretation |
| Official repository locator | Public implementation/data claim | Repository contents were not executed or redistributed |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` - upstream temporal/spatial calibration for heterogeneous sensors.
2. `.lake-data/DEP-E/DEP-E-20260716-Stereo Lane Detection/stereo_lane_detection_manuscript.md` - interpretable temporal perception and adverse-scene evaluation.
3. `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` - multimodal geometric perception and downstream world-model evidence gates.

## Synthesis Note

### Concept Bridge

FEMOT makes synchronized frame-event evidence a tracking interface; iKalibr provides the calibration integrity that interface depends on, Stereo Lane Detection provides a temporal perception audit pattern, and HERMES shows how tracked geometry may feed a downstream world representation.

### Potential Implementations

1. Build an offline tracker scorecard sliced by the 14 challenge attributes and by RGB-only, event-only, and fused inputs.
2. Add calibration-drift and timestamp-offset perturbations before accepting multimodal tracking results.
3. Wrap trajectory outputs in provenance, uncertainty, retention, and human-review records for bounded research use.

### Deeper Relationship Observations

1. Frequency fusion cannot repair misregistered sensors, making calibration a causal prerequisite rather than a preprocessing detail.
2. Long-term association memory resembles temporal priors in lane perception but can also propagate identity errors.
3. A world model consuming trajectories inherits detector, association, sensor, and dataset-coverage failures.

### Conceptual Similarities

1. All four artifacts treat temporal consistency as an evidence source.
2. Each benefits from explicit coordinate, timing, and provenance contracts.
3. Each requires challenge-sliced evaluation rather than one aggregate score.

### MVP Implementations with Code Mock-Ups

1. Challenge slice gate: `assert min(slice_hota.values()) >= policy.floor`.
2. Calibration perturbation: `audit(track(rgb, shift(event, dt_ms)))` across bounded offsets.
3. Provenance envelope: `receipt = sign({run, sensor_manifest, model_hash, metrics})`.

### Developer Challenges

1. Synchronizing dense frames with asynchronous events without silent temporal leakage.
2. Reproducing annotations, splits, preprocessing, and metric implementations exactly.
3. Separating detection and association failures while preserving privacy and dataset rights.

### Author Challenges

1. Establishing cross-sensor and cross-environment generalization beyond one capture platform.
2. Reporting compute, robustness, privacy, and failure evidence alongside accuracy.
3. Documenting consent, retention, demographic coverage, and public-space governance.

## Validation Notes

- Uniform first draw: index 48,183 of 75,776; duplicate exclusions 0; reselections 0.
- Complete-source gate passed: valid PDF plus official full-paper HTML; metadata alone was not counted.
- Claims are tied to inspected full-paper evidence and separated from reviewer inference.
- Exactly three related DEP entries and three items in every required synthesis subsection are present.
- Public allowlist is Markdown/JSON only. Source files are withheld locally.

## Attribution Block

- https://arxiv.org/abs/2606.14094 - canonical metadata, authors, date, DOI, abstract, public locators.
- https://arxiv.org/html/2606.14094 - full-paper evidence for dataset, method, experiments, and limitations; local copy withheld.
- https://arxiv.org/pdf/2606.14094 - verified primary PDF; local copy withheld.
- https://github.com/Event-AHU/FEMOT - author-stated code and benchmark locator; not executed or redistributed.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration - related calibration evidence.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Stereo%20Lane%20Detection - related temporal perception evidence.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model - related multimodal world-model evidence.
- Source files: verified PDF, official full-paper HTML, metadata HTML, and integrity records; all withheld locally.
