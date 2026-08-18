# DEP-A-20260819-LOCKS Page Local Compact

#artificial-intelligence #arXiv #paper-review #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.24555v1, *LOCKS: Page-Local Compact Key Summaries for Efficient Long-Context Decoding*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.24555-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.24555-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Attention keys are locally low-rank though globally high-rank: a page’s own rank- 8 8 eigenbasis captures most of its key energy, making it a high-fidelity compact surrogate for the page’s attention mass, so reconstructed-LSE selection from a tenth-of-KV resident summary tracks the read-every-key oracle down to the smallest budgets, because the carrier pages that decide tasks survive. Each link can fail; § 3 exhibits rival summaries failing at different links, and the page-local representation is the one for which every link holds, theoretically through attention-output error (Thm. Discard entries before the query that will use them exists, namely attention-frequency heuristics [ 74 , 33 ] , sink-and-window structure [ 61 ] , adaptive head budgets [ 16 ] , reconstruction-scored eviction [ 28 ] , and synthesis into compact surrogates [ 77 ] ; DuoAttention keeps a full cache only for retrieval heads, giving streaming heads a constant-length window instead [ 60 ] ; and R-KV [ 4 ] evicts redundancy-scored entries during reasoning decode, committing periodically rather than once.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat LOCKS: Page-Local Compact Key Summaries for Efficient Long-Context Decoding as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.24555v1
  - Applies to: `2607.24555-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.24555v1
  - Applies to: `2607.24555-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.24555v1
  - Applies to: `2607.24555-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.24555
  - Applies to: `2607.24555-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Junsung Hwang
  - arXiv author search: https://arxiv.org/search/?query=Junsung%20Hwang&searchtype=author
  - Applies to: the reviewed paper and `2607.24555-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
