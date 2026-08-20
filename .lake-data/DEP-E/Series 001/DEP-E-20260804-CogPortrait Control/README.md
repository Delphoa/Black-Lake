# DEP-E-20260804-CogPortrait Control

#portrait-animation #fine-grained-control #agent-planning #synthetic-media-safety #video-generation

Public-safe research deposition for source-grounded review of CogPortrait, an arXiv paper proposing hierarchical agent planning, behavior-prototype retrieval, physiological checks, eye-region-aware guidance, and preference refinement for fine-grained portrait animation.

Source files were retained locally and withheld from this public DEP. No PDF, HTML source, metadata page, source archive, extracted text, cache, checkpoint, dataset, or private verification record is included.

## Contents

- `README.md` - public-safe DEP inventory, context, summary, relevance, and attribution.
- `cogportrait_eye_control_manuscript.md` - schema-complete manuscript research artifact with evidence ledger, claims, methodology, limitations, implementations, and replication checklist.

## Summary of Items

- `cogportrait_eye_control_manuscript.md` preserves the paper identity, two-stage method, EMH benchmark, reported HDTF and EMH metrics, ablations, evidence boundaries, safe implementation options, and follow-up questions. It also records the random-selection, source-integrity, cache, and dedup/reselection methodology.
- `README.md` provides the stable public entry point and confirms that original source files remain local and were not uploaded.

## Insights and Relevance

CogPortrait is relevant to Black Lake because it makes the semantic-to-motion interface explicit: high-level intent is turned into temporal events, retrieved behavior prototypes, constrained control channels, and finally video. This connects directly to existing work on preference-aligned portrait motion, intention-conditioned motion planning, and latent video consistency. The main downstream value is a testable plan-to-render ledger that can expose where a failure occurs, while the main governance requirement is consent-aware handling of portraits, voices, source videos, and synthetic outputs.

## Attribution Block

- Source URL: https://arxiv.org/abs/2605.28056
  - Applies to: `README.md` and `cogportrait_eye_control_manuscript.md`.
  - Notes: Canonical public metadata and abstract record.
- Source URL: https://arxiv.org/html/2605.28056
  - Applies to: `cogportrait_eye_control_manuscript.md`.
  - Notes: Full-paper method, benchmark, experiments, ablations, and conclusion evidence.
- Source URL: https://arxiv.org/pdf/2605.28056
  - Applies to: `cogportrait_eye_control_manuscript.md`.
  - Notes: Printed figures, tables, training settings, and metric evidence.
- Source URL: https://doi.org/10.48550/arXiv.2605.28056
  - Applies to: source identity fields in both files.
  - Notes: ArXiv-issued DOI locator.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260721-Hallo4%20Portrait%20Motion/hallo4_portrait_motion_manuscript.md
  - Applies to: related-research context in `cogportrait_eye_control_manuscript.md`.
  - Notes: Live related DEP inspected for portrait-motion and preference-alignment overlap.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260726-MoGIC%20Boosting%20Motion/mogic_boosting_motion_manuscript.md
  - Applies to: related-research context in `cogportrait_eye_control_manuscript.md`.
  - Notes: Live related DEP inspected for intention-to-motion planning overlap.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md
  - Applies to: related-research context in `cogportrait_eye_control_manuscript.md`.
  - Notes: Live related DEP inspected for latent video consistency and evaluation overlap.
