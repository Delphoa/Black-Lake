# DEP-A-20260726-MRMMIA Memory Attack

#artificial-intelligence #agent-memory #membership-inference #privacy #security-evaluation #chat-agents

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.27825v1, *MRMMIA: Membership Inference Attacks on Memory in Chat Agents*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.27825-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.27825-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: MRMMIA attacks agent memory by generating multiple recall probes and aggregating membership signals from responses or internal observations. It covers black-, gray-, and white-box access and targets both Mem0 and MemGPT-style memory backends.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat recall as a privacy budget: rate-limit semantically redundant probes, test canary memories at fixed FPR, and measure attack utility after deletion, summarization, and encrypted-memory defenses.

## Associated DEP Records

- [DEP-A-20260716-OpsMem Dual Memory Reason](../DEP-A-20260716-OpsMem%20Dual%20Memory%20Reason/README.md) - direct agent memory and reasoning context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.27825v1
  - Applies to: `2605.27825-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.27825v1
  - Applies to: `2605.27825-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.27825v1
  - Applies to: `2605.27825-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.27825
  - Applies to: `2605.27825-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/DPLab-UVA/cea-mia
  - Applies to: reproducibility context in `2605.27825-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Chen, Kai
  - arXiv author search: https://arxiv.org/search/?query=Chen%2C%20Kai&searchtype=author
  - Applies to: the reviewed paper and `2605.27825-whitepaper-review.md`.
- Author: Pang, Yan
  - arXiv author search: https://arxiv.org/search/?query=Pang%2C%20Yan&searchtype=author
  - Applies to: the reviewed paper and `2605.27825-whitepaper-review.md`.
- Author: Wang, Tianhao
  - arXiv author search: https://arxiv.org/search/?query=Wang%2C%20Tianhao&searchtype=author
  - Applies to: the reviewed paper and `2605.27825-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
