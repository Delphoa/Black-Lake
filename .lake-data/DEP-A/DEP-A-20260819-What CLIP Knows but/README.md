# DEP-A-20260819-What CLIP Knows but

#artificial-intelligence #arXiv #paper-review #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.23271v1, *What CLIP Knows but Cannot Say: Recovering Negation from Frozen Intermediate Features*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.23271-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.23271-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: This improves negation understanding but risks degrading the broad representations that make CLIP useful, precisely because it forces negation into an embedding space that provably cannot accommodate it [ 22 , 51 ] . PeakPatch requires no parser at all: the ECN’s learned cross-attention reads negation signals directly from CLIP’s intermediate token sequences, handling all negation forms (explicit, implicit, morphological) without external parsing. This directly motivates PeakPatch: lightweight correction modules that read negation signals from intermediate layers where prior mechanistic analyses localize them [ 38 ] , sidestep the impossibility theorem [ 22 ] by operating outside the joint embedding space, and apply corrections at both the embedding and score levels—all while keeping CLIP frozen.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat What CLIP Knows but Cannot Say: Recovering Negation from Frozen Intermediate Features as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.23271v1
  - Applies to: `2607.23271-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.23271v1
  - Applies to: `2607.23271-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.23271v1
  - Applies to: `2607.23271-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2607.23271
  - Applies to: `2607.23271-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Official code, data, project, or publisher source: https://stevencylu.github.io/PeakPatch
  - Applies to: reproducibility context in `2607.23271-whitepaper-review.md`.
  - Notes: primary-source availability does not establish independent reproduction.
- Author: Chen-Yi Lu
  - arXiv author search: https://arxiv.org/search/?query=Chen-Yi%20Lu&searchtype=author
  - Applies to: the reviewed paper and `2607.23271-whitepaper-review.md`.
- Author: Yueh-Shao Chen
  - arXiv author search: https://arxiv.org/search/?query=Yueh-Shao%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2607.23271-whitepaper-review.md`.
- Author: Somali Chaterji
  - arXiv author search: https://arxiv.org/search/?query=Somali%20Chaterji&searchtype=author
  - Applies to: the reviewed paper and `2607.23271-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
