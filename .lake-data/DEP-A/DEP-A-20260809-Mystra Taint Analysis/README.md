# DEP-A-20260809-Mystra Taint Analysis

#software-security #dynamic-taint-analysis #virtual-machines #program-analysis #information-flow #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.12308v2, *Mystra: Declarative Dynamic Taint Analysis via Shadow Virtual Machine*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.12308-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.12308-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We present the Shadow VM, a parallel virtual machine that tracks taint alongside a host runtime (Figure 2 ). Orso (2007) Dytan: a generic dynamic taint analysis framework . Mössenböck (2020) Multi-language dynamic taint analysis in a polyglot virtual machine .

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Mystra: Declarative Dynamic Taint Analysis via Shadow Virtual Machine as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.12308v2
  - Applies to: `2607.12308-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.12308v2
  - Applies to: `2607.12308-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.12308v2
  - Applies to: `2607.12308-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.12308
  - Applies to: `2607.12308-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/MM0n5Ter/Mystra
  - Applies to: reproducibility context in `2607.12308-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Zhuohao Zhang
  - arXiv author search: https://arxiv.org/search/?query=Zhuohao%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.12308-whitepaper-review.md`.
- Author: Junkun Liu
  - arXiv author search: https://arxiv.org/search/?query=Junkun%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.12308-whitepaper-review.md`.
- Author: Rui Yang
  - arXiv author search: https://arxiv.org/search/?query=Rui%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2607.12308-whitepaper-review.md`.
- Author: Yinzhi Cao
  - arXiv author search: https://arxiv.org/search/?query=Yinzhi%20Cao&searchtype=author
  - Applies to: the reviewed paper and `2607.12308-whitepaper-review.md`.
- Author: Ziyang Li
  - arXiv author search: https://arxiv.org/search/?query=Ziyang%20Li&searchtype=author
  - Applies to: the reviewed paper and `2607.12308-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
