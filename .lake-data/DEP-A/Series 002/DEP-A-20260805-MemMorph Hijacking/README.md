# DEP-A-20260805-MemMorph Hijacking

#artificial-intelligence #agent-security #memory-poisoning #tool-hijacking #adversarial-attacks #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.26154v1, *MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.26154-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.26154-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: As shown in Figure 1 , the overall pipeline of MemMorph consists of three stages: potential query modeling, structured memory initialization, and constrained memory optimization. We propose MemMorph, a new attack framework that compromises tool selection by injecting a small number of crafted records into the agent’s long-term memory store. Our main contributions are as follows: We identify long-term memory as a practical and under-explored attack surface for compromising tool selection in LLM agents We propose MemMorph, the first memory poisoning attack targeting agent’s tool-selection featuring structured memory design and block-scoped gradient-projected optimization with end-to-end effectiveness verification.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260717-Agent Memory Systems](../../Series%20001/DEP-A-20260717-Agent%20Memory%20Systems/README.md) - direct agent-memory systems and lifecycle context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260719-Agent Memory Benchmark](../../Series%20001/DEP-A-20260719-Agent%20Memory%20Benchmark/README.md) - direct agent-memory benchmark and evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.26154v1
  - Applies to: `2605.26154-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.26154v1
  - Applies to: `2605.26154-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.26154v1
  - Applies to: `2605.26154-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.26154
  - Applies to: `2605.26154-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Xuanye Zhang
  - arXiv author search: https://arxiv.org/search/?query=Xuanye%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2605.26154-whitepaper-review.md`.
- Author: Yongsen Zheng
  - arXiv author search: https://arxiv.org/search/?query=Yongsen%20Zheng&searchtype=author
  - Applies to: the reviewed paper and `2605.26154-whitepaper-review.md`.
- Author: Zhuqin Xu
  - arXiv author search: https://arxiv.org/search/?query=Zhuqin%20Xu&searchtype=author
  - Applies to: the reviewed paper and `2605.26154-whitepaper-review.md`.
- Author: Kaiyu Zhou
  - arXiv author search: https://arxiv.org/search/?query=Kaiyu%20Zhou&searchtype=author
  - Applies to: the reviewed paper and `2605.26154-whitepaper-review.md`.
- Author: Bowen Shen
  - arXiv author search: https://arxiv.org/search/?query=Bowen%20Shen&searchtype=author
  - Applies to: the reviewed paper and `2605.26154-whitepaper-review.md`.
- Author: Haoran Ou
  - arXiv author search: https://arxiv.org/search/?query=Haoran%20Ou&searchtype=author
  - Applies to: the reviewed paper and `2605.26154-whitepaper-review.md`.
- Author: Tianwei Zhang
  - arXiv author search: https://arxiv.org/search/?query=Tianwei%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2605.26154-whitepaper-review.md`.
- Author: Kwok-Yan Lam
  - arXiv author search: https://arxiv.org/search/?query=Kwok-Yan%20Lam&searchtype=author
  - Applies to: the reviewed paper and `2605.26154-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
