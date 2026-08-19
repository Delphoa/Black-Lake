# DEP-A-20260819-risk KV cache compression

#artificial-intelligence #arXiv #paper-review #KV-cache #model-compression #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.01520v1, *The risk of KV cache compression*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.01520-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.01520-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Specifically, we characterize the minimax risk of KV compression , asking: for a fixed compression budget, how much error is unavoidable for the way a given cache can be probed by future queries? Instead, we deliberately characterize the compression risk through the interaction between caches and softmax attention itself. We seek algorithms that (i) reduce the cost of attention during prefill and autoregressive decoding (ii) reduce cache memory during autoregressive decoding (iii) respect causal masking (iv) attain the minimax-optimal query-agnostic risk (v) attain the query-aware minimax-optimal rate under Section ˜ 5 .

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat The risk of KV cache compression as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.01520v1
  - Applies to: `2607.01520-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.01520v1
  - Applies to: `2607.01520-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.01520v1
  - Applies to: `2607.01520-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2607.01520
  - Applies to: `2607.01520-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Lukas Haverbeck
  - arXiv author search: https://arxiv.org/search/?query=Lukas%20Haverbeck&searchtype=author
  - Applies to: the reviewed paper and `2607.01520-whitepaper-review.md`.
- Author: Carmen Amo Alonso
  - arXiv author search: https://arxiv.org/search/?query=Carmen%20Amo%20Alonso&searchtype=author
  - Applies to: the reviewed paper and `2607.01520-whitepaper-review.md`.
- Author: Andres Felipe Posada-Moreno
  - arXiv author search: https://arxiv.org/search/?query=Andres%20Felipe%20Posada-Moreno&searchtype=author
  - Applies to: the reviewed paper and `2607.01520-whitepaper-review.md`.
- Author: Sebastian Trimpe
  - arXiv author search: https://arxiv.org/search/?query=Sebastian%20Trimpe&searchtype=author
  - Applies to: the reviewed paper and `2607.01520-whitepaper-review.md`.
- Author: Marco Pavone
  - arXiv author search: https://arxiv.org/search/?query=Marco%20Pavone&searchtype=author
  - Applies to: the reviewed paper and `2607.01520-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
