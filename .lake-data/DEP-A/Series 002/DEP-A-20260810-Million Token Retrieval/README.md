# DEP-A-20260810-Million Token Retrieval

#artificial-intelligence #long-context #retrieval #benchmarking #million-token-context #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.01538v1, *Can Language Models Actually Retrieve In-Context? Drowning in Documents at Million Token Scale*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.01538-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.01538-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Leveraging the natural alignment between queries and their gold documents, we find that the transformer usually assigns the highest pre-softmax attention score to the gold document even at million-token scale, but the aggregate contribution of irrelevant documents to the softmax denominator grows faster with corpus size, causing the normalized attention mass on the gold document to collapse ( section 4 ). More broadly, they identify attention dilution as the primary bottleneck at million-token scale: while simple interventions can substantially mitigate its effects, it remains a fundamental challenge for scalable in-context retrieval. In this work, we present the first systematic study of in-context retrieval on two scales practical retrievers demand: million-token corpora and length-generalization far beyond training-time sizes.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Can Language Models Actually Retrieve In-Context? Drowning in Documents at Million Token Scale as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260717-Constrained LongEval](../../Series%20001/DEP-A-20260717-Constrained%20LongEval/README.md) - direct long-context retrieval evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.01538v1
  - Applies to: `2607.01538-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.01538v1
  - Applies to: `2607.01538-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.01538v1
  - Applies to: `2607.01538-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.01538
  - Applies to: `2607.01538-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://huggingface.co/datasets/rlhn/rlhn-680K
  - Applies to: reproducibility context in `2607.01538-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Siddharth Gollapudi
  - arXiv author search: https://arxiv.org/search/?query=Siddharth%20Gollapudi&searchtype=author
  - Applies to: the reviewed paper and `2607.01538-whitepaper-review.md`.
- Author: Nilesh Gupta
  - arXiv author search: https://arxiv.org/search/?query=Nilesh%20Gupta&searchtype=author
  - Applies to: the reviewed paper and `2607.01538-whitepaper-review.md`.
- Author: Prasann Singhal
  - arXiv author search: https://arxiv.org/search/?query=Prasann%20Singhal&searchtype=author
  - Applies to: the reviewed paper and `2607.01538-whitepaper-review.md`.
- Author: Sewon Min
  - arXiv author search: https://arxiv.org/search/?query=Sewon%20Min&searchtype=author
  - Applies to: the reviewed paper and `2607.01538-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
