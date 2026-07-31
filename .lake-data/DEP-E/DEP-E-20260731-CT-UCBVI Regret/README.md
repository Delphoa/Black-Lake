# DEP-E-20260731-CT-UCBVI Regret

#reinforcement-learning #continuous-time #ctmdp #regret-bounds #uncertainty #model-based-rl

Public-safe context: a source-grounded review of arXiv:2210.00832v2 and its later publisher record. The original paper documents, metadata, source-package status record, and verification material remain local; no source files are deposited here.

## Contents

- README.md
  - DEP inventory, public-safe context, relevance, and attribution.
- ct_ucbvi_regret_manuscript.md
  - Schema-complete manuscript reviewing CT-UCBVI, evidence, limits, related DEP bridges, and bounded implementation paths.

## Summary of Items

The manuscript records the paper's finite-horizon tabular CTMDP formulation, CT-UCBVI algorithm, source-reported square-root regret results, two-state simulation, reproducibility limits, and the distinction between the 2023 arXiv v2 source and later publisher metadata. It also records the random selection, deduplication, and complete-source verification outcomes without exposing local source locations.

## Insights and Relevance

This DEP is useful for research planning around event-driven model-based RL. Its main transferable lesson is to account separately for uncertainty in transition destinations, dwell-time rates, and finite planning precision. The selected paper supplies regret theory under narrow tabular assumptions; the related GPMD, RRT-CBF, and SIM-MARL entries clarify that practical deployment additionally needs numerical validation, hard constraint checks, reproducibility evidence, and operational monitoring.

## Attribution Block

- Source URL: https://arxiv.org/abs/2210.00832
  - Applies to: ct_ucbvi_regret_manuscript.md
  - Notes: Canonical metadata, arXiv version, author, and identifier record.
- Source URL: https://arxiv.org/pdf/2210.00832
  - Applies to: ct_ucbvi_regret_manuscript.md
  - Notes: Public PDF locator. The inspected copy is held locally and was not uploaded.
- Source URL: https://arxiv.org/html/2210.00832
  - Applies to: ct_ucbvi_regret_manuscript.md
  - Notes: Public full-paper HTML locator. The inspected copy is held locally and was not uploaded.
- Source URL: https://doi.org/10.1287/moor.2022.0283
  - Applies to: ct_ucbvi_regret_manuscript.md
  - Notes: Publisher record used for later-version context; no publisher full text was deposited.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md
  - Applies to: ct_ucbvi_regret_manuscript.md
  - Notes: Related processed DEP entry.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md
  - Applies to: ct_ucbvi_regret_manuscript.md
  - Notes: Related processed DEP entry.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260722-SIM%20MARL%20Power/sim_marl_power_manuscript.md
  - Applies to: ct_ucbvi_regret_manuscript.md
  - Notes: Related processed DEP entry.
