# DEP-A-20260806-HGA Global Attention

#artificial-intelligence #sparse-attention #long-context #hierarchical-routing #memory-tiering #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.30709v1, *Hierarchical Global Attention (HGA)*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.30709-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.30709-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The practical limit for long-context pretrained LLMs is often not only the O ​ ( n 2 ) O(n^{2}) attention computation, but also the dense K/V cache that must remain in accelerator memory. about 1K routed middle tokens for a 64-token block in the current Qwen3 configuration, plus fixed sink/local/current chunks; a two-level chunk–group routing policy combining deterministic attention sinks and recent local chunks with content-routed retrieval from the middle of the context; repository benchmarks showing a + 0.01828 +0.01828 nat copy-only loss gap at 8K tokens and 2.72 × 2.72\times training-step speedup at 12K tokens for a 40M SmallLM; a tiered K/V storage abstraction for RAM-backed inference, in which full historical token K/V lives in host RAM while only a bounded working set occupies VRAM, decoupling GPU memory consumption from context length; a needle-in-a-haystack evaluation on Qwen3-30B-A3B-Instruct-2507-FP8 showing 100% retrieval accuracy at 64K-token context without any fine-tuning. Sparse Transformer, Longformer, and BigBird use fixed sparse patterns or global tokens to reduce attention cost [ 3 , 2 , 15 ] .

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Hierarchical Global Attention (HGA) as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260715-Prompt Compression Wild](../../Series%20001/DEP-A-20260715-Prompt%20Compression%20Wild/README.md) - direct context-compression and task-quality evaluation context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260802-AgentServeSim](../../Series%20001/DEP-A-20260802-AgentServeSim/README.md) - direct LLM-serving workload and systems-evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.30709v1
  - Applies to: `2606.30709-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.30709v1
  - Applies to: `2606.30709-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.30709v1
  - Applies to: `2606.30709-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.30709
  - Applies to: `2606.30709-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/vfedosov77/HierarchicalGlobalAttention
  - Applies to: reproducibility context in `2606.30709-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Woernle Frank
  - arXiv author search: https://arxiv.org/search/?query=Woernle%20Frank&searchtype=author
  - Applies to: the reviewed paper and `2606.30709-whitepaper-review.md`.
- Author: Fedosov Vladimir
  - arXiv author search: https://arxiv.org/search/?query=Fedosov%20Vladimir&searchtype=author
  - Applies to: the reviewed paper and `2606.30709-whitepaper-review.md`.
- Author: Grinenko Artemiy
  - arXiv author search: https://arxiv.org/search/?query=Grinenko%20Artemiy&searchtype=author
  - Applies to: the reviewed paper and `2606.30709-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
