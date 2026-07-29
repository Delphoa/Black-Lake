# DEP-A-20260729-J-Space Workspace

#artificial-intelligence #language-models #mechanistic-interpretability #jacobian-lens #global-workspace #alignment-auditing #model-evaluation

This DEP-A preserves a public-safe, source-grounded review of *Verbalizable Representations Form a Global Workspace in Language Models*. The owning artifact is deliberately limited to that paper's Jacobian-lens method, J-space evidence, alignment implications, counterfactual-reflection experiment, and official reference implementation. It does not carry forward the other papers, products, benchmarks, systems, or governance subjects collected in the broader `DEP-E-20260729-Inspectable Agents` record.

## Contents

- `README.md` - classification, inventory, scope boundary, relevance, and final source attribution.
- `j-space-workspace-review.md` - schema-complete review of the primary paper with an evidence ledger, claim audit, limitations, replication boundary, and bounded implementation paths.

No external source files, model weights, prompts, corpora, activations, benchmark payloads, or repository clones are committed. The primary paper and official implementation were inspected through their public URLs. The implementation is linked for provenance; it is not redistributed.

## Summary of Items

### `README.md`

Defines the cold-storage boundary and records the canonical source locators. It makes explicit that this DEP-A owns one research object rather than the multi-topic evidence set of the source DEP-E.

### `j-space-workspace-review.md`

Reconstructs the paper's method and evidence: the layer-wise averaged Jacobian used to decode residual-stream activations; the sparse, token-aligned J-space; causal swap, steering, clamping, and ablation experiments; the claimed global-workspace-like properties; structural broadcast evidence; alignment-audit case studies; post-training observations; and counterfactual reflection training. It separates reported findings from reviewer inference and preserves material limits, including single-token readouts, post-hoc workspace boundaries, proprietary-model dependence, incomplete task coverage, ambiguous early-layer results, and lack of independent reproduction.

## Insights and Relevance

The study's durable contribution is a causal, vocabulary-aligned observation and intervention surface for intermediate language-model representations. Its experiments support a narrower conclusion than “thought reading”: a small and imperfectly observed representational component is unusually involved in verbal report and flexible internal computation, while substantial automatic processing bypasses it. That makes the J-lens promising for hypothesis generation, model audits, and controlled research, but insufficient as a standalone safety monitor or proof of intent. The associated claims about conscious access are functional analogies, not evidence of subjective experience.

## Relationship to the Source DEP-E

- Source record: [`DEP-E-20260729-Inspectable Agents`](../../DEP-E/DEP-E-20260729-Inspectable%20Agents/README.md).
- Imported research object: *Verbalizable Representations Form a Global Workspace in Language Models* and its official companion implementation.
- Excluded from this DEP-A: GPT-Red, the SWE-Bench Pro audit, STOCKTAKE, modular pretraining, medical and scientific agents, Oracle Agent Memory, HORCRUX, PriEval-Protect, Smart Coverage Goals, the NIST crypto-agility paper, and the source DEP-E's cross-domain product synthesis.
- Classification rationale: this entry freezes a completed review of one identified publication and its public implementation surface for durable retrieval.

## Attribution Block

- Source URL: https://transformer-circuits.pub/2026/workspace/index.html
  - Applies to: `j-space-workspace-review.md` and this README.
  - Notes: Complete primary paper, published in the Transformer Circuits Thread on 2026-07-06 and inspected on 2026-07-29. No paper license was visible in the inspected page, so the source was linked and paraphrased rather than redistributed.
- Source URL: https://www.anthropic.com/research/global-workspace
  - Applies to: `j-space-workspace-review.md`.
  - Notes: Official author-organization summary used as near-primary context, not as a substitute for the paper.
- Source URL: https://github.com/anthropics/jacobian-lens
  - Applies to: `j-space-workspace-review.md`.
  - Notes: Official companion repository inspected for implementation scope, maintenance status, dependencies, synthetic data notes, and reproducibility boundaries.
- Source URL: https://github.com/anthropics/jacobian-lens/blob/main/README.md
  - Applies to: `j-space-workspace-review.md`.
  - Notes: Reference-implementation documentation; inspected blob SHA `296ba6e47e3fc01da6bea94a0c38248ff9e6641a`.
- Source URL: https://github.com/anthropics/jacobian-lens/blob/main/pyproject.toml
  - Applies to: `j-space-workspace-review.md`.
  - Notes: Package metadata for `jlens` version `0.1.0`; inspected blob SHA `facb1859429522ce7a695a3a65970101cbdae4cb`.
- Source URL: https://github.com/anthropics/jacobian-lens/blob/main/LICENSE
  - Applies to: `j-space-workspace-review.md`.
  - Notes: Apache License 2.0 for the companion code and repository-provided synthetic prompt sets; inspected blob SHA `d645695673349e3947e8e5ae42332d0ac3164cd7`.
- Source URL: https://www.neuronpedia.org/jlens
  - Applies to: `j-space-workspace-review.md`.
  - Notes: Public interactive J-lens surface linked by the paper; included as implementation context only and not used to validate the paper's empirical claims.
- Source record: https://github.com/Delphoa/Black-Lake/tree/f91342a701df29adbb2df87886028a11f8095076/.lake-data/DEP-E/DEP-E-20260729-Inspectable%20Agents
  - Applies to: this README and the scope/provenance notes in `j-space-workspace-review.md`.
  - Notes: Upstream multi-topic DEP-E from which the single primary research object was selected. No unrelated research subject or object was imported.
