# DEP-E-20260719-MA-VLM PNU Moderation

#machine-learning #vision-language-models #content-moderation #self-training #weak-supervision #pnu-learning #model-governance

Public-safe deposition context: `Black Lake Arxiv DEP 2200 x10` job `BLAD-2200-20260719-7D93E819`, item `BLAD-2200-20260719-7D93E819-P01`, uniformly selected and source-first reviewed arXiv:2511.13759v1 on 2026-07-19. The archive unit was repaired from partial to verified complete before synthesis. Local source locations, exact execution times, and all source files are withheld.

## Contents

- `README.md` — inventory, context, summary, relationships, source policy, and attribution.
- `ma_vlm_pnu_moderation_manuscript.md` — schema-complete research manuscript covering the paper's mechanism, evidence, limitations, implementation paths, selection/dedup process, integrity gate, and related DEP synthesis.

No `.source/` directory is present. The paper PDF, full-paper HTML, metadata HTML, source package, extracted text, and processing cache remain local and were not deposited.

## Summary of Items

`ma_vlm_pnu_moderation_manuscript.md` reviews a low-resource offensive-content framework in which a lightweight CLIP classifier, a strict-moderator VLM persona, and a lenient-user VLM persona jointly route unlabeled samples. Consensus examples receive soft pseudo-labels; disagreements remain unlabeled and contribute through a customized PNU loss. The manuscript records four benchmark tasks, reported Macro-F1 results, prompt and loss ablations, official-code availability, and the distinction between source claims and reviewer interpretation.

The artifact also preserves the uniform random draw, cross-repository dedup result, bounded repair, complete-source integrity metrics, cache status, and zero-source-upload gate. It connects the paper to exactly three inspected Black Lake entries: OViP Preference, Adversarial Label Noise, and RLMF Uncertainty.

## Insights and Relevance

The most reusable mechanism is to preserve disagreement as an explicit training state instead of forcing a hard pseudo-label. This aligns with other Black Lake work on model-specific feedback, soft distributional targets, and conditional use of self-evaluation signals. The major unresolved issue is governance: two role prompts from one VLM are not independent annotators, aggregate Macro-F1 does not establish fairness, and a development-set revert loop can overfit its own gate. A safe implementation should remain offline, weight model-produced labels below human labels, audit subgroup and disagreement strata, and require human authorization before any moderation consequence.

## Source and Distribution Policy

- Source state: verified complete after bounded local repair.
- Source documents: withheld locally.
- Public deposit: generated Markdown plus required repository indexes only.
- `.source/`: not created.
- Source uploads: zero.
- Deployment job ID: `BLAD-2200-20260719-7D93E819`.
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P01`.

## Attribution Block

- Source URL: https://arxiv.org/abs/2511.13759
  - Applies to: `ma_vlm_pnu_moderation_manuscript.md` and this README.
  - Notes: Canonical metadata and abstract page; metadata only, not the full paper.
- Source URL: https://arxiv.org/html/2511.13759
  - Applies to: `ma_vlm_pnu_moderation_manuscript.md`.
  - Notes: Official full-paper HTML inspected locally; source file withheld.
- Source URL: https://arxiv.org/pdf/2511.13759
  - Applies to: `ma_vlm_pnu_moderation_manuscript.md`.
  - Notes: Verified PDF inspected locally; source file withheld.
- Source URL: https://arxiv.org/e-print/2511.13759
  - Applies to: `ma_vlm_pnu_moderation_manuscript.md`.
  - Notes: Official source package used for equations and table cross-checks; source file withheld.
- Source URL: https://doi.org/10.48550/arXiv.2511.13759
  - Applies to: persistent paper identity in both files.
- Source URL: https://github.com/Social-AI-Studio/MA-VLM
  - Applies to: official implementation availability and reproducibility boundary.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference
  - Applies to: related VLM feedback-loop analysis.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Adversarial%20Label%20Noise
  - Applies to: related soft-label and uncertainty analysis.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-RLMF%20Uncertainty
  - Applies to: related feedback-gating and proxy-governance analysis.
- Source files: verified paper PDF, full-paper HTML, metadata HTML, source package, extracted text, and processing cache.
  - Applies to: source-first review and integrity validation.
  - Notes: All source files were withheld locally; zero source documents were uploaded. Deployment context is job `BLAD-2200-20260719-7D93E819`, item `BLAD-2200-20260719-7D93E819-P01`.
