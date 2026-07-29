---
title: "J-Space Method Card"
artifact_id: "DEP-A-JSPACE-METHODCARD-20260729"
dep_class: "DEP-A"
profile_id: "j-space-workspace-20260729"
record_object_type: "transformed document"
transformation: "Primary-paper method and limitations normalized into a durable method-card representation."
source_scope: "J-space research only"
generated_at: "2026-07-29"
---

# J-Space Method Card

## Method Identity

| Field | Value |
|---|---|
| Name | Jacobian lens / J-lens |
| Intended research use | Decode and causally test vocabulary-aligned components of intermediate language-model states |
| Primary source | *Verbalizable Representations Form a Global Workspace in Language Models* |
| Public implementation | `anthropics/jacobian-lens`, package `jlens` 0.1.0 |
| Profile status | Source-grounded; not independently reproduced |

## Inputs

- A transformer language model with authorized access to intermediate residual states and gradients.
- A layer selection policy.
- A prompt distribution for fitting the averaged downstream Jacobian.
- Source and future target position policy.
- Vocabulary unembedding and model normalization.
- Tasks and concepts for readout or intervention.

## Transformation

For each layer, estimate an average downstream Jacobian from intermediate residual state to same-or-later final-layer state. Apply the map to a new activation, normalize it, and unembed it into vocabulary coordinates. Rank token directions or fit a sparse nonnegative decomposition to define the active J-space component.

The transformation is first-order and average-context. It should be versioned with the model, tokenizer, prompt-set digest, layer, position policy, normalization, sparsity rule, and dependency environment.

## Supported Operations

| Operation | Purpose | Required control |
|---|---|---|
| Token ranking | Generate hypotheses about verbalizable content | Logit-lens and random-map comparisons |
| Coordinate swap | Test whether one concept direction can replace another | Dose control and matched random direction |
| Injection / steering | Test reportability or downstream use | Baseline prompt and off-target behavior checks |
| Sparse component split | Separate J-space-aligned and residual components | Reconstruction error and sparsity sensitivity |
| Clamping | Test whether an effect is mediated by re-entry into selected coordinates | Clean-pass reference and alternate clamp sets |
| Ablation | Test functional dependence | Random-direction, random-head, and protected-output controls |
| Activation patching | Localize when an intermediate affects behavior | Clean/corrupt counterfactual pair and layer sweep |

## Outputs

- Ranked token directions and scores.
- Sparse component weights and reconstruction diagnostics.
- Intervention outcomes and effect sizes.
- Layer/position trajectories.
- Control comparisons.
- A provenance receipt connecting every output to the model, lens, task, and intervention.

## Assumptions

- The local Jacobian is informative for the intervention magnitude used.
- The fitting prompt distribution captures relevant representation changes.
- Vocabulary directions form a useful human-readable frame.
- Sparse nonnegative decomposition is an appropriate operational constraint.
- The authorized model interface exposes correct activations and gradients.

## Known Limits

- Single-token and bag-of-concepts readouts.
- Context averaging and first-order approximation.
- Overcomplete directions and decomposition non-uniqueness.
- Partly post-hoc workspace boundaries.
- Incomplete task and model coverage.
- Automatic or deliberately non-verbalized processing can bypass the interface.
- No inference from workspace-like function to subjective experience.

## Reproduction Boundary

The public repository provides reference code, package metadata, and synthetic examples under Apache-2.0. The reviewed bundle does not provide the paper's production checkpoints, fitted lenses, fitting corpus, complete prompts, or run artifacts. A public study can reproduce the method on a new open model; it cannot reproduce the exact paper results from the available artifacts alone.

## Safe Use

Use for authorized research, hypothesis generation, and controlled model evaluation. Do not use as a standalone intent detector, deception classifier, access-control decision, employee/user surveillance tool, or consciousness assessment.

## Sources

- https://transformer-circuits.pub/2026/workspace/index.html
- https://github.com/anthropics/jacobian-lens
- https://github.com/anthropics/jacobian-lens/blob/main/README.md
- https://github.com/anthropics/jacobian-lens/blob/main/pyproject.toml
- https://github.com/anthropics/jacobian-lens/blob/main/LICENSE
