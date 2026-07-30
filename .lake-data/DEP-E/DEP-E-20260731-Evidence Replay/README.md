# DEP-E-20260731-Evidence Replay

#long-context #evidence-replay #llm-harness #agent-memory #provenance #evaluation #reproducibility #context-governance

Public-safe iterative DEP-E research deposit generated from `DEP-20260706-Tech Intel 1110`. This pass expands the randomly selected ReContext thread and preserves its relationship to the source DEP's earlier memory-and-agent-safety artifact.

## Contents

- `README.md` - DEP inventory, source policy, item summary, relevance, and final Attribution Block.
- `evidence-replay.md` - Schema-complete manuscript covering ReContext's mechanism, results, ablations, efficiency, theory boundary, official implementation surface, broader source lineage, and safe follow-on work.

No `.source/` directory is present. No source PDF, TeX package, repository, dataset, model, benchmark payload, dependency, prompt corpus, or execution trace was collected or deposited.

## Summary of Items

### `evidence-replay.md`

The manuscript begins with the selected source DEP, the prior DEP-E artifact, and the exact earlier Report-Mark lineage. It then expands ReContext through the full v1 paper, a pinned official implementation, the released reproduction configuration, and five primary methodological neighbors.

The main reviewer conclusion is that evidence replay is a useful organization layer but not a trust layer. It can make a small copied evidence set explicit while retaining the full prompt, yet it still needs upstream source governance and downstream outcome verification. The artifact preserves reported gains, task-level exceptions, configuration dependence, runtime cost, theorem assumptions, and reproduction gaps.

## Insights and Relevance

This entry turns a broad memory-safety synthesis into a narrower design boundary for provenance-preserving semantic systems. ReContext's explicit replay pool can become an auditable junction between governed source intake and answer verification, provided each span retains source identity, offsets, version, and selection configuration. The implementation evidence also shows why matched-budget evaluation matters: replay adds little reported GPU memory but requires internal model access, per-task configuration, and extra inference time.

## Attribution Block

- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/tree/b0cb541844ca7eb9cf32407a49fef6d81d6a8310/.lake-data/DEP-20260706-Tech%20Intel%201110
  - Applies to: `evidence-replay.md` and `README.md`.
  - Notes: Selected source DEP, current Report-Mark lineage, and fixed source snapshot.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/e8876bd1e9ebe85e7be041d50f78e5428fb9f089/.lake-data/DEP-E/DEP-E-20260727-Memory%20and%20Agent%20Safety
  - Applies to: `evidence-replay.md`.
  - Notes: Prior DEP-E manuscript and companion README reviewed for iterative context.
- Source URLs: https://arxiv.org/abs/2607.02509; https://arxiv.org/html/2607.02509v1; https://doi.org/10.48550/arXiv.2607.02509
  - Applies to: `evidence-replay.md`.
  - Notes: Newly expanded ReContext canonical record, full paper, and DOI.
- Source URL: https://github.com/Yanjun-Zhao/ReContext/tree/ea14e9e45e9dac7f333b754abf16521bf3a86e4e
  - Applies to: `evidence-replay.md`.
  - Notes: Newly inspected official implementation snapshot; README and reproduction script inspected, not executed.
- Source URLs: https://arxiv.org/abs/2404.06654; https://doi.org/10.48550/arXiv.2404.06654
  - Applies to: `evidence-replay.md`.
  - Notes: RULER long-context evaluation context.
- Source URLs: https://arxiv.org/abs/2307.03172; https://doi.org/10.48550/arXiv.2307.03172
  - Applies to: `evidence-replay.md`.
  - Notes: Lost in the Middle position-sensitivity context.
- Source URLs: https://arxiv.org/abs/2404.14469; https://doi.org/10.48550/arXiv.2404.14469
  - Applies to: `evidence-replay.md`.
  - Notes: SnapKV internal-signal and KV-selection context.
- Source URLs: https://arxiv.org/abs/2310.05736; https://doi.org/10.48550/arXiv.2310.05736
  - Applies to: `evidence-replay.md`.
  - Notes: LLMLingua compression comparison.
- Source URLs: https://arxiv.org/abs/2310.06839; https://doi.org/10.48550/arXiv.2310.06839
  - Applies to: `evidence-replay.md`.
  - Notes: LongLLMLingua long-context compression comparison.
- Source URL: https://arxiv.org/abs/2607.02514
  - Applies to: `evidence-replay.md`.
  - Notes: Prior persistent-state attack context.
- Source URL: https://arxiv.org/abs/2607.01793
  - Applies to: `evidence-replay.md`.
  - Notes: Prior executable safety-testing context.
- Source URL: https://arxiv.org/abs/2607.02116
  - Applies to: `evidence-replay.md`.
  - Notes: Prior context-governance context.
- Source URL: https://arxiv.org/abs/2607.02303
  - Applies to: `evidence-replay.md`.
  - Notes: Prior exact-memory context.
- Source URL: https://arxiv.org/abs/2607.02010
  - Applies to: `evidence-replay.md`.
  - Notes: Prior inducing-KV context.
- Source URL: https://arxiv.org/abs/2607.02374
  - Applies to: `evidence-replay.md`.
  - Notes: Prior memory-drift context.
- Source URL: https://arxiv.org/abs/2607.02175
  - Applies to: `evidence-replay.md`.
  - Notes: Prior consequence-weighted evaluation context; not clinical guidance.
- Source URL: https://arxiv.org/abs/2607.02329
  - Applies to: `evidence-replay.md`.
  - Notes: Prior grounded autonomous-research context.
- Source URL: https://arxiv.org/abs/2607.02444
  - Applies to: `evidence-replay.md`.
  - Notes: Prior formal memory-resource context.
