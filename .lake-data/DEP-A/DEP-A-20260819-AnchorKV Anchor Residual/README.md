# DEP-A-20260819-AnchorKV Anchor Residual

#artificial-intelligence #arXiv #paper-review #KV-cache #model-compression #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.02901v1, *AnchorKV: Anchor-Residual KV Cache Compression*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.02901-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.02901-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Section 2 reviews prior compression methods, Section 3 presents AnchorKV, and Section 4 evaluates it at matched byte budgets against eviction and quantization baselines, ablates each component, and reports runtime and memory. We profile AnchorKV at a 20 × 20\times target (Llama-3.1-8B-Instruct, bf16, one 80 GiB A100; baseline is the full cache under PyTorch SDPA, memory excluding weights). AnchorKV decodes with the decode_attention_compact kernel, which reads the compressed tensors of Table 1 directly and never rebuilds the dense cache.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat AnchorKV: Anchor-Residual KV Cache Compression as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.02901v1
  - Applies to: `2608.02901-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.02901v1
  - Applies to: `2608.02901-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.02901v1
  - Applies to: `2608.02901-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2608.02901
  - Applies to: `2608.02901-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Malik Khalaf
  - arXiv author search: https://arxiv.org/search/?query=Malik%20Khalaf&searchtype=author
  - Applies to: the reviewed paper and `2608.02901-whitepaper-review.md`.
- Author: Yara Shamshoum
  - arXiv author search: https://arxiv.org/search/?query=Yara%20Shamshoum&searchtype=author
  - Applies to: the reviewed paper and `2608.02901-whitepaper-review.md`.
- Author: Nitzan Hodos
  - arXiv author search: https://arxiv.org/search/?query=Nitzan%20Hodos&searchtype=author
  - Applies to: the reviewed paper and `2608.02901-whitepaper-review.md`.
- Author: Yuval Sieradzki
  - arXiv author search: https://arxiv.org/search/?query=Yuval%20Sieradzki&searchtype=author
  - Applies to: the reviewed paper and `2608.02901-whitepaper-review.md`.
- Author: Assaf Schuster
  - arXiv author search: https://arxiv.org/search/?query=Assaf%20Schuster&searchtype=author
  - Applies to: the reviewed paper and `2608.02901-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
