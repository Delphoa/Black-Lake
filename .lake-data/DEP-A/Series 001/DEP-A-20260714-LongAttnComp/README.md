# DEP-A-20260714-LongAttnComp

#arxiv #icml #long-context #context-compression #information-retrieval #code-reasoning #cross-model-transfer #machine-learning

Public-safe whitepaper review of **“LongAttnComp: Cross-Family Context Compression for Long-Context Reasoning,” arXiv:2606.01336v2**. Complete source documents were verified locally and withheld.

Deposition date: 2026-07-14
Stable paper version: arXiv:2606.01336v2

## Contents

- `README.md` — deposition context, complete inventory, relationships, and attribution.
- `2606.01336-whitepaper-review.md` — validated full-paper review and independent re-conceptualization.

## Summary of Items

The README defines this archival record. The 4,359-word review reconstructs the frozen thirteen-layer scorer, trainable cross-attention, chunking, token-budget selection, query parsing, two-stage curriculum, all ten tables and five figures, four target models, Code-Debug, LongBench v2, RULER, efficiency boundaries, and replication requirements. It passed the whitepaper validator and scored 19/20 on the methodology rubric.

## Insights and Relevance

LongAttnComp is a strong learned evidence selector with a portable text interface. The review finds its held-out DeepSeek-R1 code result compelling and its cross-family retention useful, while documenting ordinary accuracy loss against full context on the other target models, distributed-evidence weaknesses, task-specific selection modes, training/evaluation affinity, missing end-to-end latency evidence, a LongBench table inconsistency, and no verified code release.

## Associated DEP Records

- [`DEP-A-20260714-Tail-Aware Adaptive K`](../DEP-A-20260714-Tail-Aware%20Adaptive%20K/README.md) — close conceptual query-adaptive context selection for retrieval-augmented generation; not the same paper or implementation.
- [`DEP-A-20260714-SeCo Semantic Grouping`](../DEP-A-20260714-SeCo%20Semantic%20Grouping/README.md) — close conceptual semantic rather than position-driven context compression; not the same paper or implementation.

No same-paper DEP-A, DEP-E, or Delphoa-Labs record was verified after checking class indexes, DEP records, logs, reports, and the related data repository.

## Attribution Block

- Canonical record/PDF/HTML: https://arxiv.org/abs/2606.01336 · https://arxiv.org/pdf/2606.01336 · https://arxiv.org/html/2606.01336
- DOI: https://doi.org/10.48550/arXiv.2606.01336
- Primary publication record: https://openreview.net/pdf/8c5cd2d078c86a32df600810c5f5945a7f6659e9.pdf
- Benchmarks: https://github.com/OpenBMB/InfiniteBench · https://github.com/NVIDIA/RULER · https://longbench2.github.io/
- Official LongAttnComp code/checkpoint: the paper states that release is planned; no canonical public URL was verified during recorded checks.
- Authors: Mengmeng Ji (https://arxiv.org/search/cs?query=Ji%2C+M&searchtype=author); Ravi Shanker Raju (https://arxiv.org/search/cs?query=Raju%2C+R&searchtype=author); Jonathan Lingjie Li (https://arxiv.org/search/cs?query=Li%2C+J&searchtype=author); Chen Wu (https://arxiv.org/search/cs?query=Wu%2C+C&searchtype=author).
- Applies to both listed Markdown files; complete source documents were verified locally and withheld from the repository.
