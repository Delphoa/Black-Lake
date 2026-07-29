---
title: "J-Space Research Report"
artifact_id: "DEP-E-JSPACE-REPORT-20260729"
dep_class: "DEP-E"
profile_id: "j-space-workspace-20260729"
record_object_type: "research report"
source_scope: "J-space research only"
status: "open research agenda"
generated_at: "2026-07-29"
---

# J-Space Research Report

## Research Question

What does the inspected evidence establish about a vocabulary-aligned, workspace-like interface in language models, and what evidence is still required before the method can support repeatable model auditing?

## Findings

| ID | Finding | Evidence status | Decision relevance |
|---|---|---|---|
| F1 | The Jacobian lens is a context-averaged, first-order map from intermediate residual states toward final-layer vocabulary coordinates. | Directly specified by the primary paper. | Treat readouts as an approximation, not a literal transcript of hidden computation. |
| F2 | Sparse J-space components can exert more causal influence on selected reports and two-hop answers than the larger non-J-space remainder. | Supported by swaps, decomposition, and clamping in the paper. | Preserve causal controls in any replication; readable rankings alone are insufficient. |
| F3 | Selected flexible tasks are more sensitive to J-space ablation than several automatic tasks. | Supported within the authors' task battery. | A no-signal result cannot be treated as absence of cognition or risk. |
| F4 | Intermediate capacity and broadcast signatures are consistent with a functional global workspace. | Supported as an analogy by layer, capacity, MLP, and attention evidence. | Do not convert the analogy into a consciousness claim. |
| F5 | Alignment case studies show that some strategic or situational representations can be exposed and causally manipulated. | Demonstrated in selected organization-authored cases. | The method is a research signal, not a calibrated monitor. |
| F6 | The public code is an implementation reference, not a complete reproduction package. | Confirmed by official repository documentation. | Independent validation needs open models, new fitted lenses, public tasks, and pinned build receipts. |

## Quantitative Anchors

- The primary analysis averages the Jacobian over 1,000 pretraining-like prompts.
- Sparse J-space decompositions generally use at most 25 active token directions.
- In a ninety-prompt component experiment, J-space swaps flipped 61% of answers, non-J-space swaps flipped 28%, and clamping reduced the latter to 6%.
- Across 192 cross-function swaps, standard-strength interventions succeeded in 76 cases and double-strength interventions in 101.
- In the evaluation-awareness case, explicit recognition fell from 71% to 3% after ablation, while blackmail changed from 0/180 to 13/180 rollouts.
- Counterfactual reflection training used 10,000 partial agentic contexts. Reported dishonesty changed from 0.25 to 0.07 in one evaluation and deception from 0.38 to 0.05 in another.

All figures are reported source results, not independently reproduced measurements.

## Evidence Status

### Supported in the inspected source

- The lens and sparse decomposition are concretely defined.
- Multiple causal interventions connect the observed component to selected behavior.
- The paper preserves negative results and automatic-processing bypasses.
- Public reference code and an Apache-2.0 license exist.

### Bounded or unresolved

- Cross-family and cross-language generalization.
- Stability across model updates and fine-tuning regimes.
- Phrase-level, distributed, and intentionally obfuscated concepts.
- Monitoring recall, precision, specificity, and robustness.
- Independent reproduction of the proprietary-model results.
- Whether workspace-like function predicts anything about subjective experience.

## Research Decisions

1. Keep J-space readouts as one evidence channel within a multi-method evaluation.
2. Require intervention controls before promoting a decoded concept into a mechanistic claim.
3. Build the first replication on an open model and synthetic/public tasks.
4. Record negative and missing results in the same schema as positive findings.
5. Prohibit autonomous enforcement or intent labels in the initial implementation.

## Next Research Pass

| Priority | Question | Minimum evidence | Stop condition |
|---|---|---|---|
| P0 | Can the lens be fit reproducibly on an open model? | Pinned environment, public prompts, deterministic build manifest, and repeated lens statistics | Stop if repeated builds do not agree within a predeclared tolerance |
| P0 | Do swaps outperform matched random-direction controls? | Pre-registered two-hop tasks, effect sizes, uncertainty, and clamping | Stop if effects do not separate from controls |
| P1 | Does a workspace band transfer across model families? | At least three open families and normalized layer comparisons | Do not generalize if band definitions require family-specific post-hoc adjustment |
| P1 | Can monitoring performance be calibrated? | Blinded synthetic scenarios with positive, negative, and ambiguous cases | Stop short of deployment if false negatives remain unbounded |
| P2 | Do phrase- or feature-level bases improve coverage? | Causal mediation comparison against token directions | Reject added complexity if interpretability improves without causal fidelity |

## Scope Receipt

This report covers only the J-space paper, Anthropic's official summary, the official `jacobian-lens` repository, and the linked Neuronpedia surface. It imports no claim, object, or synthesis from the other research subjects in the original Inspectable Agents manuscript.

## Sources

- https://transformer-circuits.pub/2026/workspace/index.html
- https://www.anthropic.com/research/global-workspace
- https://github.com/anthropics/jacobian-lens
- https://www.neuronpedia.org/jlens
