# Report-Mark: RLMF Uncertainty

## Research Record

**Paper:** *Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs*
**Authors:** Gabrielle Kaili-May Liu; Avi Caciularu; Gal Yona; Idan Szpektor; Arman Cohan
**Record:** arXiv:2606.32032v1, https://arxiv.org/abs/2606.32032
**Status:** 2026 preprint; official MIT-licensed code inspected at commit `a087e7a1e49f52aaa701add19cd80699b709fdef`; experiments not rerun
**Selection:** User-directed; no random draw was represented or simulated

## Concise Notes

### Problem

The paper studies faithful calibration: whether an LLM's expressed uncertainty matches an estimate of its own intrinsic confidence. This differs from factual calibration, where confidence should match correctness. The distinction exposes a real failure mode: a model can be correct or statistically calibrated on average while expressing confidence in ways that do not track the stability of its own outputs.

The term “intrinsic confidence” is operational, not metaphysical. It is estimated from the consistency of a sentence with 20 additional sampled responses, with consistency judged by Qwen3-32B. Every interpretation of the results should preserve that dependency.

### Mechanism

RLMF modifies group-relative policy optimization. Each sampled completion contains sentence-level confidence values. A composite reward covers format, correctness, factual calibration, and faithfulness. The model also predicts how faithfully its confidence matched the sampled-consistency target. Agreement between predicted and computed faithful-calibration level produces `Z_g = 1 - (F_pred - F_gold)^2`.

The total advantage is separated into faithfulness and accessory components. For above-group-mean faithfulness completions, the centered faithfulness advantage is multiplied by `1 + Z_g`; below-mean faithfulness completions are not amplified. This restriction prevents good self-assessment from rescuing poor primary-task behavior.

Metacognitive data selection independently ranks training examples by model self-assessment and chooses equal halves from the high and low ends. Stage 2 then maps numerical confidence to human-rated hedge bins and asks a rewriting model to adapt uncertainty language to the user context.

### Evidence

For Llama3.1-8B-Instruct, average cMFG-star rises from 0.60 for the base model to 0.77 under standard RL and 0.84 under RLMF; rewriting yields 0.82. Accuracy is 0.41 under RLMF versus 0.31 for the base model. Standard RL has the lower Brier score, 0.20 versus 0.26 for RLMF, so RLMF does not dominate every calibration measure.

For Qwen3-8B, average cMFG-star is 0.54 for the base model, 0.51 under standard RL, and 0.83 under RLMF and after rewriting. RLMF retains 0.57 accuracy and reports a 0.19 Brier score. Smaller Qwen models reach similarly high reported faithful-calibration averages.

Training on PopQA, SelfAware, HaluEval, or UMWP produces cross-task averages between 0.80 and 0.84 in the main 8B configurations. Metacognitive selection exceeds random and active-learning-style selection for both main models. Extensive appendix ablations support the selected reward form, prompt, no-normalization choice, pre-SFT, 2,000-example size, raw quadratic metacognitive score, piecewise scaling, `k=1`, and `tau=0.10`.

Three expert annotators evaluated 120 cases. RLMF-plus-rewriting wins 98 percent on diversity, 98 percent on naturalness, 95 percent on helpfulness, and 96 percent on contextual suitability versus FUT, with reported Krippendorff alpha 0.93. The rubric intentionally does not score correctness, so this validates linguistic quality more directly than factual preservation or real-user reliance.

### Code and Reproducibility

The official repository documents baseline evaluation, MetaFaith, pre-SFT, metacognitive data selection, RLMF training, checkpoint evaluation, and rewriting. The sample setup uses 32 completions, LoRA rank 64, 2,000 examples, 1,500 steps, `beta=0.1`, and a six-GPU topology: four training GPUs, one rollout server, and one judge. The README states three GPUs as a minimum and shows two additional GPUs for optional concurrent checkpoint evaluation.

Static inspection confirms the central advantage formula and auxiliary-score protocol. A small paper/code discrepancy exists at the threshold boundary: the displayed equation counts `|c-g| < tau`, while code counts `abs(c-g) <= tau`. The code was not executed, and no independent raw-result or checkpoint audit was performed.

### Critical Boundaries

- The target is a sampled-consistency proxy conditioned on decoding and an evaluator, not verified access to a hidden belief state.
- One reported training seed and absent main-table confidence intervals make RL variance unknown.
- The documented workflow selects checkpoints on the in-domain test set, which should be replaced by a validation split.
- Training, selection, checkpointing, and evaluation share metrics and judge infrastructure, creating circularity risk.
- cMFG-star improves bin comparability but should be paired with confidence-support width and bin counts.
- The compact data-selection table reports Qwen3-8B random-selection accuracy as 0.23, while the full appendix table reports 0.53 for the same row.
- Stage 2 can change facts while improving style; the human study does not constitute a full semantic-preservation audit.
- Compute is substantial and no complete token, wall-time, energy, or cost ledger is reported.
- “First,” “state of the art,” and broad metacognitive-awareness language remains author-scoped pending broader search and independent replication.

## Synthesis Note

### Related DEP Entries

1. [PAC Confidence - DEP-E](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence) - finite-sample confidence intervals, support, and distribution-envelope boundaries.
2. [OViP Preference - DEP-E](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference) - on-policy failure-driven preference data and evaluator-loop governance.
3. [ConMax Reasoning - DEP-E](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260708-ConMax%20Reasoning) - confidence-shaped optimization using an auxiliary model to protect reasoning quality.

### Concept Bridge

All four works add a second evidence channel to a primary model decision. PAC Confidence wraps a prediction in finite-sample interval evidence. OViP uses the current model's failures to generate preference evidence. ConMax uses auxiliary confidence to decide whether compressed reasoning remains adequate. RLMF uses self-assessment accuracy to determine how strongly an already-good completion should be reinforced.

The bridge is an **evidence-conditioned control plane**. A task decision should remain primary; confidence, self-assessment, preference, or compression evidence changes whether and how the decision is accepted, trained on, rewritten, or escalated. Each evidence channel must retain provenance and cannot certify properties outside its measurement envelope.

RLMF supplies the learning-time controller, PAC Confidence supplies support-aware statistical boundaries, OViP supplies feedback-loop provenance and disagreement requirements, and ConMax supplies a pattern for keeping confidence subordinate to independently measured task fidelity. A combined architecture would separate six release facts: task correctness, expressed/proxy alignment, finite-sample support, evaluator disagreement, semantic preservation after rewriting, and distribution-shift state.

### Potential Implementations

1. **Support-Aware Uncertainty Release Gate.** Evaluate cMFG-star together with PAC-style confidence intervals, empirical confidence support, accuracy, Brier score, and judge disagreement. Release remains a human decision, and any missing support or detected shift fails closed.
2. **On-Policy Metacognitive Audit Queue.** Use RLMF-style high/low self-assessment strata to choose review examples, while applying OViP-style provenance records to every policy sample, judge result, selection decision, and rewrite. Preserve disagreements instead of collapsing them into one score.
3. **Confidence-Subordinate Training Controller.** Generalize the RLMF/ConMax pattern so auxiliary confidence can scale a learning or compression signal only after an independent task predicate passes. Log both channels and forbid the auxiliary evaluator from becoming the sole release criterion.

### Deeper Relationship Observations

1. **Conditionality is the safety feature.** PAC intervals are useful only under a distributional envelope; OViP negatives are useful only when semantically isolated; ConMax confidence is useful only when answer fidelity survives; RLMF self-assessment is useful only for above-average faithfulness. The condition, not the score alone, carries the governance value.
2. **Every method can create evaluator circularity.** Calibration bins, preference judges, auxiliary reasoners, and consistency judges can all be optimized against. Independent holdouts, evaluator rotation, and disagreement records are common remedies across the four deposits.
3. **Presentation and truth must remain separate.** RLMF's rewriting can improve uncertainty language, ConMax can compress reasoning, and OViP can reduce mentioned hallucinations; each transformation may improve a visible metric while changing evidence content. PAC-style support records and semantic-preservation checks prevent interface improvements from being mistaken for truth improvements.

### Conceptual Similarities

1. Each method transforms a scalar model output into a governed decision by attaching additional evidence.
2. Each method depends on a versioned measurement procedure whose validity can fail under shift or evaluator error.
3. Each method benefits from a fail-closed path that retains the original artifact and routes uncertain cases to review.

### MVP Implementations

1. **Release Card Evaluator**

```python
def evaluate(card):
    gates = {
        "held_out": card.held_out_test,
        "accuracy": card.accuracy_delta >= -0.01,
        "faithfulness": card.faithfulness_ci_low >= card.floor,
        "support": card.support_width >= card.min_support,
        "judge": card.judge_disagreement <= card.max_disagreement,
        "rewrite": card.changed_claims == 0,
    }
    return {"decision": "human_review" if all(gates.values()) else "reject", "gates": gates}
```

This local-only evaluator consumes aggregate evidence and never returns automatic production approval.

2. **Metacognitive Provenance Record**

```json
{
  "example_id": "public-fixture-0042",
  "policy_version": "model-hash",
  "sample_count": 20,
  "intrinsic_proxy": {"method": "semantic-consistency", "judge": "judge-hash"},
  "expressed_confidence": 0.42,
  "predicted_faithfulness": 0.55,
  "computed_faithfulness": 0.50,
  "selection_stratum": "low-self-assessment",
  "review_state": "queued"
}
```

This schema keeps the three confidence concepts distinct and makes selection auditable.

3. **Confidence-Subordinate Controller**

```yaml
primary_predicate:
  metric: task_fidelity
  rule: ">= validated_floor"
auxiliary_signal:
  metric: metacognitive_agreement
  action: scale_positive_gain_only
guards:
  - independent_evaluator
  - minimum_support
  - no_test_set_selection
  - preserve_original_artifact
fallback: human_review
```

This declarative controller can govern training, compression, or rewriting without allowing confidence to replace task evidence.

### Developer Challenges

1. Reproduce the method against pinned TRL, vLLM, model, dataset, prompt, and judge versions while controlling six-to-eight GPU orchestration and recording complete cost telemetry.
2. Implement estimator and judge adapters that preserve disagreement, expose support, and prevent training/evaluation leakage without making the pipeline prohibitively expensive.
3. Build semantic-preservation tests for rewriting that catch entity, value, negation, causal, scope, and recommendation-strength changes across diverse domains.

### Author Challenges

1. Demonstrate the central effect across multiple seeds with checkpoint selection on validation data and untouched final test sets.
2. Establish construct validity by showing that RLMF gains transfer across independent intrinsic-confidence estimators and evaluators rather than one consistency pipeline.
3. Measure calibrated user reliance and factual preservation after rewriting, including failure cases where natural hedging increases persuasion without increasing correctness.

## Bottom Line

RLMF is a technically concrete and unusually well-documented proposal for making self-assessment affect learning priority. Its strongest evidence is the consistent faithful-calibration improvement across the tested open-weight models and the ablations supporting conditional advantage scaling. Its largest unresolved question is whether the gain represents transferable metacognitive monitoring or adaptation to a shared consistency-and-judge proxy. The correct next step is a held-out, multi-seed, cross-proxy reproduction with support-aware reporting and a factual-preservation audit for rewriting.

## Source References

- https://arxiv.org/abs/2606.32032
- https://arxiv.org/html/2606.32032
- https://arxiv.org/pdf/2606.32032
- https://arxiv.org/e-print/2606.32032
- https://doi.org/10.48550/arXiv.2606.32032
- https://github.com/yale-nlp/RLMF
- https://aclanthology.org/2025.emnlp-main.1505/
- https://arxiv.org/abs/2409.12180
- https://aclanthology.org/2023.emnlp-main.557/

No paper source file, local cache path, secret, or exact private execution timestamp is included in this report.
