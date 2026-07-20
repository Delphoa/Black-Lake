# DEP-E-20260720-FEMOT Tracking

#event-camera #multi-object-tracking #sensor-fusion #computer-vision #benchmark #identity-association #research-review

Public-safe context: job `BLAD-2200-20260720-8636EDC7`, item `BLAD-2200-20260720-8636EDC7-P04`, uniformly selected and reviewed `arXiv:2606.14094v1`. The PDF-only archive unit was repaired to verified complete with official arXiv full-paper HTML before synthesis. Exact execution times, local paths, and all source documents are withheld.

## Contents

- `README.md` - deposit context, inventory, synthesis, source boundary, and attribution.
- `femot_tracking_manuscript.md` - schema-complete review of the FEMOT benchmark, FEMOTR architecture, evidence, limitations, implementation paths, and related DEP synthesis.

No `.source/` exists. No PDF, HTML, dataset, event stream, frame, annotation, model, code, cache, or extracted source text is deposited.

## Summary of Items

FEMOT reports 100 synchronized RGB-event sequences, about 200,000 frames, 14,580 trajectories, 420,000 boxes, and 14 challenge attributes, plus FEMOTR's frequency-domain multimodal fusion and temporal association memory. On FEMOT, the paper reports 48.9 HOTA, 52.0 MOTA, and 62.0 IDF1, with ablations supporting contributions from multimodal inputs, shared multi-scale weights, and frequency-aware fusion.

The manuscript keeps author results distinct from reviewer interpretation. It highlights fixed event accumulation, limited cross-platform evidence, incomplete subject-governance evidence, and weaker DSEC-MOT detection/overall tracking than selected baselines despite strong association.

## Insights and Relevance

The strongest reuse is an offline, challenge-sliced multimodal tracking auditor. iKalibr supplies sensor-time integrity, Stereo Lane Detection supplies temporal-reset testing, and HERMES shows why downstream systems must inherit tracking uncertainty and provenance rather than only trajectories.

## Attribution Block

- https://arxiv.org/abs/2606.14094 - metadata, authors, date, DOI, and source links.
- https://arxiv.org/html/2606.14094 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2606.14094 - verified primary PDF; local copy withheld.
- https://github.com/Event-AHU/FEMOT - author-stated code/data locator; not executed or redistributed.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration - related sensor calibration DEP.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Stereo%20Lane%20Detection - related temporal perception DEP.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model - related multimodal world-model DEP.
- Source files: verified PDF, full-paper HTML, metadata HTML, and integrity records; all withheld locally with zero source-document uploads.
