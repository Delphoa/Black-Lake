# DEP-A-20260816-RAGAL Local Support

#artificial-intelligence #RAG #local-AI #public-sector #retriever-training #privacy

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.18756v1, *RAGAL: A Frugal, Fully Local Retrieval-Augmented Assistant for Technical Support at a Government Agency*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.18756-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.18756-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: RAGAL (“RAG for GAL”, after the Local Action Groups — Grupuri de Ac t , iune Locală — whose activity the agency coordinates) supports the team that maintains the agency’s application ecosystem: it answers questions about procedures and application workflows, retrieves precedents from 15,073 resolved support tickets, and drafts parameterized SQL correction scripts for a technician to review and run. Our contributions are practical rather than algorithmic: An end-to-end account of a fully local, Romanian-language RAG system in pilot production over a dual corpus (normative documents + support tickets), including the engineering decisions that mattered most. Running the golden evaluation end-to-end on the ft-v2 pipeline (same 4B generator as the baseline) passed the regression gate with zero deterministic regressions : documentary-retrieval assertions 4/4, the anti-contamination assertion and the live-lookup interceptor intact, and four generative assertions improved over the stock-retriever baseline — parameterized-SQL drafting on two T2 correction cases and unknown-admission on a discipline probe — consistent with better precedents reaching the context.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat RAGAL: A Frugal, Fully Local Retrieval-Augmented Assistant for Technical Support at a Government Agency as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260814-TurboVec Private RAG](../DEP-A-20260814-TurboVec%20Private%20RAG/README.md) - direct private and resource-aware RAG deployment context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.18756v1
  - Applies to: `2607.18756-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.18756v1
  - Applies to: `2607.18756-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.18756v1
  - Applies to: `2607.18756-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.18756
  - Applies to: `2607.18756-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/danmusetoiu/RAGAL
  - Applies to: reproducibility context in `2607.18756-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Dan Musetoiu
  - arXiv author search: https://arxiv.org/search/?query=Dan%20Musetoiu&searchtype=author
  - Applies to: the reviewed paper and `2607.18756-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
