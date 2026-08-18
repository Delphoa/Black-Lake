# DEP-A-20260819-Attention Amnesia Hybrid

#artificial-intelligence #arXiv #paper-review #attention #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.11052v1, *Attention Amnesia in Hybrid LLMs: When CoT Fine-Tuning Breaks Long-Range Recall, and How to Fix It*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.11052-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.11052-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Empirical studies suggest that long-range recall in hybrid models depends disproportionately on a set of softmax-attention layers, whereas most remaining layers can be replaced by recurrent mechanisms with minimal degradation ( wang2025systematicanalysishybridlinear ; chen2026hybridlinearattentionright ; jelassi2024repeat ) . Since long-context recall in distilled hybrid models depends heavily on a small number of retained softmax-attention layers, such query-key drift can disproportionately disrupt retrieval. Softmax-attention layers ℓ ∈ L attn \ell\in{L}_{\mathrm{attn}} are the sole locus of long-range recall in a hybrid model.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Attention Amnesia in Hybrid LLMs: When CoT Fine-Tuning Breaks Long-Range Recall, and How to Fix It as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.11052v1
  - Applies to: `2606.11052-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.11052v1
  - Applies to: `2606.11052-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.11052v1
  - Applies to: `2606.11052-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.11052
  - Applies to: `2606.11052-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/LARK-AI-Lab/QK-Restore
  - Applies to: reproducibility context in `2606.11052-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Xinyu Zhou
  - arXiv author search: https://arxiv.org/search/?query=Xinyu%20Zhou&searchtype=author
  - Applies to: the reviewed paper and `2606.11052-whitepaper-review.md`.
- Author: Boyu Zhu
  - arXiv author search: https://arxiv.org/search/?query=Boyu%20Zhu&searchtype=author
  - Applies to: the reviewed paper and `2606.11052-whitepaper-review.md`.
- Author: Yi Xu
  - arXiv author search: https://arxiv.org/search/?query=Yi%20Xu&searchtype=author
  - Applies to: the reviewed paper and `2606.11052-whitepaper-review.md`.
- Author: Zhiwei Li
  - arXiv author search: https://arxiv.org/search/?query=Zhiwei%20Li&searchtype=author
  - Applies to: the reviewed paper and `2606.11052-whitepaper-review.md`.
- Author: Yingfa Chen
  - arXiv author search: https://arxiv.org/search/?query=Yingfa%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2606.11052-whitepaper-review.md`.
- Author: Huiming Wang
  - arXiv author search: https://arxiv.org/search/?query=Huiming%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.11052-whitepaper-review.md`.
- Author: Zhijiang Guo
  - arXiv author search: https://arxiv.org/search/?query=Zhijiang%20Guo&searchtype=author
  - Applies to: the reviewed paper and `2606.11052-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
