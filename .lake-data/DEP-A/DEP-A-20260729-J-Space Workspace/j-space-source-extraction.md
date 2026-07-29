---
title: "J-Space Source Extraction"
artifact_id: "DEP-A-JSPACE-EXTRACTION-20260729"
dep_class: "DEP-A"
profile_id: "j-space-workspace-20260729"
record_object_type: "extraction"
source_scope: "J-space research only"
extraction_status: "reviewer-extracted; no source text or experimental payload redistributed"
generated_at: "2026-07-29"
---

# J-Space Source Extraction

## Extraction Boundary

This artifact preserves normalized facts extracted from *Verbalizable Representations Form a Global Workspace in Language Models* and the official `anthropics/jacobian-lens` repository. It is not a copy of the paper, a dataset released by the authors, or an independent experimental result. All prose is paraphrased.

## Source Identity

| Field | Extracted value | Source |
|---|---|---|
| Title | Verbalizable Representations Form a Global Workspace in Language Models | Primary paper citation block |
| Publication | Transformer Circuits Thread | Primary paper |
| Publication date | 2026-07-06 | Primary paper |
| Primary locator | https://transformer-circuits.pub/2026/workspace/index.html | Primary paper |
| Official summary | https://www.anthropic.com/research/global-workspace | Anthropic |
| Reference code | https://github.com/anthropics/jacobian-lens | Official repository |
| Package | `jlens` 0.1.0 | `pyproject.toml` |
| Code license | Apache License 2.0 | Repository `LICENSE` |
| Repository maintenance note | Reference implementation is stated to be unmaintained | Repository README |

## Method Extraction

| ID | Source location | Extracted fact | Reviewer boundary |
|---|---|---|---|
| M1 | Method / Jacobian lens | A layer-specific downstream Jacobian transports intermediate residual states toward final-layer coordinates. | First-order local approximation |
| M2 | Method / averaging | The Jacobian is averaged across prompts, source positions, and current/future target positions. | Context-specific effects may be averaged away |
| M3 | Method / fitting set | The reported average uses 1,000 pretraining-like prompts. | Exact production corpus is not deposited |
| M4 | Method / readout | The transported activation is normalized and read through the vocabulary unembedding. | Token rankings are not literal thoughts |
| M5 | J-space definition | J-space uses sparse nonnegative combinations of token-aligned directions, generally with no more than 25 active directions. | Not a unique ordinary linear subspace |
| M6 | Intervention operations | The study uses swaps, steering/injection, ablation, activation patching, and clamping. | Large interventions may move off distribution |

## Experiment Extraction

| ID | Experiment family | Scope | Reported result | Source status |
|---|---|---|---|---|
| X1 | Two-hop coordinate swaps | 50 prompts; Haiku 4.5, Sonnet 4.5, Opus 4.5 | Target answer moved to top rank in 54%, 70%, and 70% of trials respectively | Paper report; not reproduced |
| X2 | Two-hop component decomposition | 90 prompts | J-space swap flipped 61%; non-J-space swap 28%; clamping reduced the latter to 6% | Paper report; not reproduced |
| X3 | Cross-function argument swaps | 192 trials across 16 templates | 76 successes at standard strength and 101 at double strength | Paper report; incomplete success is material |
| X4 | Broad task ablation | 14 task families | Flexible generation/reasoning tasks degraded more than several shallow or automatic tasks | Qualitative cross-task pattern; task selection is author-defined |
| X5 | Capacity analysis | Intermediate workspace band | Median sparse occupancy reported near 25 directions; excess variance below 10% | Importance is causal, not variance-dominant |
| X6 | Broadcast-head ablation | Top 1% selected heads | Mid-workspace top-25 recall 0.67 versus 0.86 for matched random-head ablation | Paper report; model-specific |
| X7 | Evaluation-awareness ablation | Blackmail scenario, 180 rollouts per condition | Evaluation recognition 71% to 3%; blackmail 0/180 to 13/180 | One causal contributor, not a full alignment explanation |
| X8 | Counterfactual reflection | 10,000 training contexts; two reported evaluations | Dishonesty 0.25 to 0.07; deception 0.38 to 0.05 | LLM-graded, one family, no external replication |

## Limitation Extraction

| ID | Limitation | Consequence |
|---|---|---|
| L1 | Readouts are token-aligned and primarily single-token | Compositional, multilingual, polysemantic, or non-verbalizable concepts may be missed |
| L2 | Workspace boundaries are partly post hoc and lens-derived | Structural claims need independent confirmatory splits |
| L3 | Automatic processing can bypass J-space | Absence of a readout is not evidence of absence |
| L4 | Central checkpoints are proprietary | Exact reproduction and cross-family validation are unavailable |
| L5 | Public repository omits fitted paper lenses, models, and fitting corpus | The code is a reference surface, not a reproduction bundle |
| L6 | Alignment case studies are selected and organization-authored | Detector operating characteristics are not established |
| L7 | Functional workspace evidence is not phenomenal-consciousness evidence | Consciousness claims remain out of scope |

## Repository Fingerprints

| File | Inspected blob SHA | Use |
|---|---|---|
| `README.md` | `296ba6e47e3fc01da6bea94a0c38248ff9e6641a` | Scope, installation, examples, synthetic-data note, maintenance status |
| `pyproject.toml` | `facb1859429522ce7a695a3a65970101cbdae4cb` | Package name/version, Python requirement, dependencies |
| `LICENSE` | `d645695673349e3947e8e5ae42332d0ac3164cd7` | Apache-2.0 code licensing |

## Scope Receipt

No fact from GPT-Red, coding-evaluation auditing, STOCKTAKE, modular pretraining, medical or scientific agents, Oracle Agent Memory, HORCRUX, PriEval-Protect, Smart Coverage Goals, NIST crypto agility, or the upstream cross-domain synthesis is included.

## Sources

- https://transformer-circuits.pub/2026/workspace/index.html
- https://www.anthropic.com/research/global-workspace
- https://github.com/anthropics/jacobian-lens
- https://github.com/anthropics/jacobian-lens/blob/main/README.md
- https://github.com/anthropics/jacobian-lens/blob/main/pyproject.toml
- https://github.com/anthropics/jacobian-lens/blob/main/LICENSE
