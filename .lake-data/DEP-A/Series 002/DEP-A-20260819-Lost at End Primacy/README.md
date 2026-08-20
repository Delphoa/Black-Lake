# DEP-A-20260819-Lost at End Primacy

#artificial-intelligence #arXiv #paper-review #RAG #multimodal #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.16494v3, *Lost at the End: Primacy Bias in Multimodal Retrieval-Augmented Question Answering*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.16494-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.16494-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: 1 1 1 Code and protocol: https://github.com/WeMWish/lost_at_the_end_code The probe is a gold-position protocol (§ 3 ) that holds everything bit-identical within question except the gold passage’s prompt slot, so the position effect is a within-prompt permutation that admits exact paired-bootstrap inference, isolating the reader’s response to position from confounds in retrieval, scoring, and prompt composition. We use primacy bias for the reader’s systematic preference for evidence early in its prompt over otherwise-identical evidence at later positions: gold-at-first beats gold-at-last by 16 to 26 pp on every reader-by-benchmark cell (one reader paired with one benchmark; six in total), with no recency rebound on five of six (§ 4.1 ), and a text-only ablation on the same readers shows the multimodal setting amplifies an already-present text-mode primacy 2.2 to 4.5 times (§ 4.2 ). Describe the issue below: Abstract 1 Introduction 2 Related Work 3 Probing Protocol 4.1 Primacy, Not U-Shape 4.2 Modality Amplifies the Effect 4.3 The Locus Is Prompt Slot 0 4.4 Retrieval-Side Fixes Don’t Help 5 Conclusion References A Pre-registered Methodology Notes B Subset Construction and Audits C Statistical Methodology D Scoring Sensitivity E.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Lost at the End: Primacy Bias in Multimodal Retrieval-Augmented Question Answering as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.16494v3
  - Applies to: `2606.16494-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.16494v3
  - Applies to: `2606.16494-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.16494v3
  - Applies to: `2606.16494-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.16494
  - Applies to: `2606.16494-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Jieyuan Liu
  - arXiv author search: https://arxiv.org/search/?query=Jieyuan%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2606.16494-whitepaper-review.md`.
- Author: Jianyang Gu
  - arXiv author search: https://arxiv.org/search/?query=Jianyang%20Gu&searchtype=author
  - Applies to: the reviewed paper and `2606.16494-whitepaper-review.md`.
- Author: Shijie Chen
  - arXiv author search: https://arxiv.org/search/?query=Shijie%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2606.16494-whitepaper-review.md`.
- Author: Jefferson Chen
  - arXiv author search: https://arxiv.org/search/?query=Jefferson%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2606.16494-whitepaper-review.md`.
- Author: Zhen Wang
  - arXiv author search: https://arxiv.org/search/?query=Zhen%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.16494-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
