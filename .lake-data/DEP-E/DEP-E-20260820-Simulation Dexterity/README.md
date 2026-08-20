# DEP-E-20260820-Simulation Dexterity

#robotics #dexterous-manipulation #simulation #imitation-learning #policy-pretraining

Deposition date: `2026-08-20`

This DEP-E entry is the research artifact produced from `Black-Lake-Data/.lake-data/DEP-20260819-Research Data 2234 D0822`. It reviews the full arXiv v1 manuscript and official project page for *Pre-training Visual Dexterity in Simulation*, while treating all empirical results as source-reported until independently reproduced.

## Contents

- `README.md` - DEP-E manifest, inventory, review boundary, relevance notes, and source attribution.
- `simulation-dexterity.md` - Schema-complete DEP research artifact covering the SPD collection method, policy architecture, experiments, limitations, replication needs, implementation paths, and related research.

No `.source/` directory is included. The paper, dataset, code, videos, and model artifacts were not downloaded or redistributed; public locators are preserved below.

## Summary of Items

- `README.md` records why this active-research entry belongs in DEP-E and preserves the public source chain from the selected source DEP to the primary paper and project page.
- `simulation-dexterity.md` distinguishes paper claims from reviewer interpretation. It records the 75-hour simulation dataset, the 222M-parameter diffusion-transformer policy, five-task physical evaluation, history/action-chunk ablation, evidence limits, and a bounded audit-oriented MVP.

## Insights and Relevance

SPD reframes simulation as a source of human-generated, action-labeled, on-embodiment pre-training data rather than only a place to optimize task-specific reinforcement-learning policies. The most useful mechanism is not simulation alone: aligned embodiment reduces retargeting loss, while visuomotor history lets short action chunks remain reactive without losing temporal coherence. The evidence supports a promising transfer result on five related physical tasks, but does not establish broad out-of-distribution generalization, reproducibility, or deployment readiness. A follow-on review should prioritize release verification, simulator-parameter sensitivity, multi-seed training, and evaluation on dissimilar objects and scenes.

## Attribution Block

- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/tree/e127946890a3fe7d2ffc6d53e2b6e60b14907197/.lake-data/DEP-20260819-Research%20Data%202234%20D0822
  - Applies to: `simulation-dexterity.md` and this README.
  - Notes: Selected source DEP, pinned to the inspected source repository commit.
- Source URL: https://arxiv.org/abs/2608.15917
  - Applies to: `simulation-dexterity.md`.
  - Notes: Canonical arXiv record for v1 metadata and submission history.
- Source URL: https://arxiv.org/html/2608.15917
  - Applies to: `simulation-dexterity.md`.
  - Notes: Full primary manuscript, including methods, experiments, tables, limitations, and appendix.
- Source URL: https://spd.bot/
  - Applies to: `simulation-dexterity.md`.
  - Notes: Official project page inspected for the method overview, model description, evaluation summary, and public media surface.
- Source URL: https://arxiv.org/abs/2410.24164
  - Applies to: `simulation-dexterity.md` related reading.
  - Notes: Canonical record for the flow-model policy context cited by SPD.
- Source URL: https://arxiv.org/abs/2505.21864
  - Applies to: `simulation-dexterity.md` related reading.
  - Notes: Canonical record for a human-hand interface alternative to simulation teleoperation.
- Source URL: https://arxiv.org/abs/2602.16710
  - Applies to: `simulation-dexterity.md` related reading.
  - Notes: Canonical record for large-scale egocentric human-data pre-training.
- Source URL: https://arxiv.org/abs/2304.13705
  - Applies to: `simulation-dexterity.md` related reading.
  - Notes: Canonical record for action chunking and low-cost bimanual imitation learning.
