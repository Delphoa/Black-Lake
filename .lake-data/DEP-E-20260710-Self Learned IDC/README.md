# Self Learned IDC

#arxiv #autonomous-driving #reinforcement-learning #decision-control #state-representation #traffic-safety #black-lake

Public-safe DEP-E context: this entry preserves a source-grounded review of arXiv:2110.12359, "Self-learned Intelligence for Integrated Decision and Control of Automated Vehicles at Signalized Intersections." The review focuses on dynamic permutation state representation for mixed-traffic intersections, integrated decision and control, simulation evidence, limitations, and related Black-Lake state/control artifacts. No local source files are redistributed in this DEP.

## Contents

- `README.md`: DEP inventory, summary, relevance notes, source policy, and attribution.
- `self_learned_idc_manuscript.md`: Schema-complete manuscript research artifact for the selected arXiv paper.

## Summary of Items

- `README.md` matters because it records the public-safe deposit context, tags, contents, and provenance for future Black-Lake reviewers.
- `self_learned_idc_manuscript.md` matters because it converts the selected paper into a structured research artifact with source metadata, evidence ledger, methodology, claims, limitations, implementation paths, and review backlog.

## Insights and Relevance

The paper is relevant to Black-Lake because it treats state representation as the core reliability interface between perception and action. Dynamic permutation state representation lets a controller reason over a variable number of vehicles, bicycles, and pedestrians while preserving a fixed-dimensional policy/value interface. That connects directly to recurring Black-Lake themes: state as an auditable control object, spatial/world-model consistency, and compact representations for physical systems. The reported simulation results are promising but source-reported only; future work should prioritize reproducibility, stress testing, and failure-case evidence.

## Attribution Block

- Source URL: https://arxiv.org/abs/2110.12359
  - Applies to: `self_learned_idc_manuscript.md`
  - Notes: Primary arXiv metadata, abstract, authors, version, DOI, and source links.
- Source URL: https://arxiv.org/pdf/2110.12359
  - Applies to: `self_learned_idc_manuscript.md`
  - Notes: Public PDF reference; PDF file is not redistributed in this DEP.
- Source URL: https://arxiv.org/e-print/2110.12359
  - Applies to: `self_learned_idc_manuscript.md`
  - Notes: Public arXiv source package used for cache-backed review after local text extraction was unavailable.
- Source URL: https://arxiv.org/html/2110.12359
  - Applies to: `self_learned_idc_manuscript.md`
  - Notes: Public arXiv HTML used for cache-backed metadata and abstract review.
- Source URL: https://doi.org/10.48550/arXiv.2110.12359
  - Applies to: `self_learned_idc_manuscript.md`
  - Notes: Persistent arXiv DOI.
- Repository path: `.lake-data/DEP-E-20260708-Agent State Review/agent_state_review.md`
  - Applies to: related research synthesis in `self_learned_idc_manuscript.md`.
  - Notes: Existing Black-Lake DEP manuscript inspected for state/control overlap.
- Repository path: `.lake-data/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`
  - Applies to: related research synthesis in `self_learned_idc_manuscript.md`.
  - Notes: Existing Black-Lake DEP manuscript inspected for spatial/world-model overlap.
- Repository path: `.lake-data/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md`
  - Applies to: related research synthesis in `self_learned_idc_manuscript.md`.
  - Notes: Existing Black-Lake DEP manuscript inspected for physical-system representation overlap.
