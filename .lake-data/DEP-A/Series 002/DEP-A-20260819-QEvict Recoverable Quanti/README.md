# DEP-A-20260819-QEvict Recoverable Quanti

#artificial-intelligence #arXiv #paper-review #KV-cache #attention #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.05326v1, *QEvict: Recoverable Quantized KV Eviction for Attention-Drift-Robust Long-Context Decoding*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.05326-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.05326-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: With FlashAttention-2, QEvict reduces peak GPU memory from 29.54 29.54 to 20.78 20.78 GB, a 29.7 % 29.7\% reduction. The resulting trade-off is backend dependent: QEvict improves eager decoding efficiency and substantially reduces FlashAttention-2 memory, while fused low-bit attention and routing kernels remain necessary to realize both benefits simultaneously. The recoverable tier therefore reduces the reference attention mass assigned to permanent eviction by 29.1 29.1 percentage points.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat QEvict: Recoverable Quantized KV Eviction for Attention-Drift-Robust Long-Context Decoding as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.05326v1
  - Applies to: `2608.05326-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.05326v1
  - Applies to: `2608.05326-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.05326v1
  - Applies to: `2608.05326-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2608.05326
  - Applies to: `2608.05326-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Ayushman Garg
  - arXiv author search: https://arxiv.org/search/?query=Ayushman%20Garg&searchtype=author
  - Applies to: the reviewed paper and `2608.05326-whitepaper-review.md`.
- Author: Akshita Gupta
  - arXiv author search: https://arxiv.org/search/?query=Akshita%20Gupta&searchtype=author
  - Applies to: the reviewed paper and `2608.05326-whitepaper-review.md`.
- Author: Shaswata Bhattacharya
  - arXiv author search: https://arxiv.org/search/?query=Shaswata%20Bhattacharya&searchtype=author
  - Applies to: the reviewed paper and `2608.05326-whitepaper-review.md`.
- Author: Abhishek Gupta
  - arXiv author search: https://arxiv.org/search/?query=Abhishek%20Gupta&searchtype=author
  - Applies to: the reviewed paper and `2608.05326-whitepaper-review.md`.
- Author: Sandeep Kumar
  - arXiv author search: https://arxiv.org/search/?query=Sandeep%20Kumar&searchtype=author
  - Applies to: the reviewed paper and `2608.05326-whitepaper-review.md`.
- Author: Manoj Kumar
  - arXiv author search: https://arxiv.org/search/?query=Manoj%20Kumar&searchtype=author
  - Applies to: the reviewed paper and `2608.05326-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
