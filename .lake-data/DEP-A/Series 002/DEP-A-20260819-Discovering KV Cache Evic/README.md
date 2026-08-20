# DEP-A-20260819-Discovering KV Cache Evic

#artificial-intelligence #arXiv #paper-review #KV-cache #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.14555v1, *Discovering KV Cache Eviction Policies via LLM-Guided Program Evolution*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.14555-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.14555-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We present CacheCraft , a program-evolution methodology that evolves prefill-stage KV eviction rules as editable program text. CacheCraft exposes a compact KVPress (Jegou and others, 2025 ) policy module with two entry points, score_tokens and select_tokens_to_keep ; gates candidates through a three-stage cascade evaluator with strict output invariants; and drives mutations with OpenEvolve (Sharma and others, 2025 ) , an LLM-guided code-evolution engine in the lineage of FunSearch (Romera-Paredes et al. The search loop has four steps: formulate the editable policy interface and reward; seed the search with a benchmark-credible prior; evolve candidate programs using an LLM-guided code-evolution engine; and validate surviving policies on held-out benchmark subsets before full evaluation.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat Discovering KV Cache Eviction Policies via LLM-Guided Program Evolution as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.14555v1
  - Applies to: `2608.14555-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.14555v1
  - Applies to: `2608.14555-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.14555v1
  - Applies to: `2608.14555-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2608.14555
  - Applies to: `2608.14555-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Pratik Poudel
  - arXiv author search: https://arxiv.org/search/?query=Pratik%20Poudel&searchtype=author
  - Applies to: the reviewed paper and `2608.14555-whitepaper-review.md`.
- Author: Yanzhao Wu
  - arXiv author search: https://arxiv.org/search/?query=Yanzhao%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2608.14555-whitepaper-review.md`.
- Author: Sumit Jha
  - arXiv author search: https://arxiv.org/search/?query=Sumit%20Jha&searchtype=author
  - Applies to: the reviewed paper and `2608.14555-whitepaper-review.md`.
- Author: Jason Liu
  - arXiv author search: https://arxiv.org/search/?query=Jason%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2608.14555-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
