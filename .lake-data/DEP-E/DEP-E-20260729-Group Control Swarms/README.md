# DEP-E-20260729-Group Control Swarms

#research #arxiv #robotics #microrobots #swarm-control #motion-planning #group-control #controllability #rrt #control-theory #simulation #evidence-review

Public deposition date: 2026-07-29. This DEP-E preserves a source-grounded review of arXiv:2406.13829v2 and its WAFR/Springer publication context. The artifact distinguishes formal source claims, simulation evidence, reviewer interpretation, and physical-deployment limits.

The private source gate verified a complete PDF and official full-paper HTML before synthesis. The source archive, extracted text, render files, provenance records, and verification evidence remain local. No source document is included in this public DEP and no `.source/` directory was created.

## Contents

- `README.md`
  - DEP inventory, public-safe context, tags, summary, relevance notes, and source attribution.
- `group_control_swarms_manuscript.md`
  - Schema-complete manuscript review covering source metadata, evidence ledger, group-control and controllability mechanisms, reported planning results, limitations, implementation paths, exactly three exercise paths, an example MVP, related research, source references, and a replication appendix.

## Summary of Items

`README.md` defines the public deposit boundary, records that every original source file was withheld locally, and supplies the canonical public locators used by the review.

`group_control_swarms_manuscript.md` reconstructs the paper's group-allocation scheme, switched-system model, position-level small-time local controllability argument, Lie-bracket-inspired motion primitives, and planning/control tradeoff. It preserves the six-robot simulation results while flagging idealized dynamics, missing variance and code, limited scale evidence, a sequential-runtime contradiction, and an RRT footnote-label mismatch.

## Insights and Relevance

The durable contribution is a cross-layer design rule: hardware group structure, primitive expressivity, planner dimensionality, and execution cost form one coupled optimization problem. RRT-CBF adds explicit safety constraints to sampled motion, SAGE-Nav shows how slow planning can feed a fast controller through a bounded waypoint interface, and CrossMaps shows why persistent, confidence-aware world state matters before planning begins. Together the related entries suggest a practical stack of state estimation, plan generation, constraint checking, primitive compilation, execution monitoring, and conservative fallback.

## Attribution Block

- Source URL: https://arxiv.org/abs/2406.13829v2
  - Applies to: `group_control_swarms_manuscript.md`
  - Notes: Canonical title, authors, version history, abstract, subjects, and arXiv DOI.
- Source URL: https://arxiv.org/html/2406.13829v2
  - Applies to: `group_control_swarms_manuscript.md`
  - Notes: Official full-paper evidence for the model, proofs, planning abstraction, simulations, tables, figures, conclusion, and references.
- Source URL: https://arxiv.org/pdf/2406.13829v2
  - Applies to: `group_control_swarms_manuscript.md`
  - Notes: Public locator for the visually inspected PDF; the local source file was withheld.
- Source URL: https://arxiv.org/e-print/2406.13829v2
  - Applies to: `group_control_swarms_manuscript.md`
  - Notes: Public TeX/source endpoint used to inspect exact formulas, table values, and captions; the source archive was withheld locally.
- Source URL: https://doi.org/10.48550/arXiv.2406.13829
  - Applies to: `group_control_swarms_manuscript.md`
  - Notes: Stable arXiv DOI.
- Source URL: https://doi.org/10.1007/978-3-032-09967-9_14
  - Applies to: `group_control_swarms_manuscript.md`
  - Notes: Springer chapter DOI in *Algorithmic Foundations of Robotics XVI, Volume 1*.
- Source URL: https://algorithmic-robotics.org/papers/65_Group_Control_Motion_Planni.pdf
  - Applies to: `group_control_swarms_manuscript.md`
  - Notes: WAFR 2024 public paper record used to confirm proceedings context.
- Source URL: https://link.springer.com/book/10.1007/978-3-032-09967-9
  - Applies to: `group_control_swarms_manuscript.md`
  - Notes: Official proceedings volume record for WAFR 2024 and Springer Proceedings in Advanced Robotics volume 37.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`; `group_control_swarms_manuscript.md`
  - Notes: Live repository layout, DEP, source-handling, attribution, and commit rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md`; `group_control_swarms_manuscript.md`
  - Notes: Live DEP-E filing and publication-index rules.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `group_control_swarms_manuscript.md`
  - Notes: Live related-repository authority inspected before using its `origin/main` surfaces for deduplication.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md
  - Applies to: `group_control_swarms_manuscript.md`
  - Notes: Related DEP evidence for sampling-based motion planning, barrier constraints, execution tracking, and safety boundaries.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav%20Review/sage_nav_manuscript.md
  - Applies to: `group_control_swarms_manuscript.md`
  - Notes: Related DEP evidence for fast/slow navigation planning, waypoint interfaces, replanning, and simulator-to-physical limits.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260722-CrossMaps%20Rover%20Mapping/2606.16935-whitepaper-review.md
  - Applies to: `group_control_swarms_manuscript.md`
  - Notes: Related DEP evidence for rover mapping, persistent semantic state, confidence handling, and navigation evidence gaps.
- Source files: Withheld locally.
  - Applies to: `README.md`; `group_control_swarms_manuscript.md`
  - Notes: No PDF, HTML, metadata page, source archive, extracted source text, render, summary, attribution record, or private verification report was deposited.
