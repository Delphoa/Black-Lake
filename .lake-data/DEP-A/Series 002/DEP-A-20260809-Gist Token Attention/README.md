# DEP-A-20260809-Gist Token Attention

#artificial-intelligence #sparse-attention #gist-tokens #long-context #model-efficiency #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2604.20920v2, *Simplified Sparse Attention via Gist Tokens*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2604.20920-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2604.20920-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We present Simplified Sparse Attention (SSA), a framework that bridges learnable gist-based context compression with sparse attention through a selective unfolding mechanism. To that end, we introduce Simplified Sparse Attention (SSA) , which interleaves gist tokens during continued pretraining and then uses these gist tokens to perform sparse attention during decoding. Since the query is scored only against the gist tokens, we avoid the memory-bandwidth cost associated with naive scoring against the full KV cache, without requiring the auxiliary KV cache approach used by sparse attention methods.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Simplified Sparse Attention via Gist Tokens as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260717-Constrained LongEval](../../Series%20001/DEP-A-20260717-Constrained%20LongEval/README.md) - direct long-context compression and evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2604.20920v2
  - Applies to: `2604.20920-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2604.20920v2
  - Applies to: `2604.20920-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2604.20920v2
  - Applies to: `2604.20920-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2604.20920
  - Applies to: `2604.20920-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/yuzhenmao/simplified-sparse-attention/
  - Applies to: reproducibility context in `2604.20920-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://doi.org/10.1145/3786335.3813221
  - Applies to: reproducibility context in `2604.20920-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Yuzhen Mao
  - arXiv author search: https://arxiv.org/search/?query=Yuzhen%20Mao&searchtype=author
  - Applies to: the reviewed paper and `2604.20920-whitepaper-review.md`.
- Author: Michael Y. Li
  - arXiv author search: https://arxiv.org/search/?query=Michael%20Y.%20Li&searchtype=author
  - Applies to: the reviewed paper and `2604.20920-whitepaper-review.md`.
- Author: Emily B. Fox
  - arXiv author search: https://arxiv.org/search/?query=Emily%20B.%20Fox&searchtype=author
  - Applies to: the reviewed paper and `2604.20920-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
