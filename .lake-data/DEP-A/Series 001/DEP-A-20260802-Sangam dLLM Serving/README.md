# DEP-A-20260802-Sangam dLLM Serving

#artificial-intelligence #diffusion-language-models #LLM-serving #scheduling #disaggregation #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.04206v1, *Sangam: Efficiently Serving Diffusion LLMs with the AR Stack*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.04206-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.04206-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We design a deficit token-budget scheduler which mitigates prefill-decode interference in colocated serving for dLLMs without relying on chunked prefill, which bidirectional attention precludes ( § 4.1 ). We implement Sangam and evaluate colocated, static disaggregated, and hybrid serving on two open-weight dLLMs and two trace-driven workloads, showing the regimes where each mode is effective and explaining why by identifying prefill/decode partitioning and prefill/decode interference as the two fundamental factors ( § 6.3 ). Before introducing challenges for serving dLLMs using AR serving stack, we briefly explain the key techniques.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Sangam: Efficiently Serving Diffusion LLMs with the AR Stack as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260715-Elastic dLLM Position Pre](../DEP-A-20260715-Elastic%20dLLM%20Position%20Pre/README.md) - direct diffusion-language-model decoding and cache context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260802-AgentServeSim](../DEP-A-20260802-AgentServeSim/README.md) - direct LLM-serving workload and systems-evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.04206v1
  - Applies to: `2607.04206-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.04206v1
  - Applies to: `2607.04206-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.04206v1
  - Applies to: `2607.04206-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.04206
  - Applies to: `2607.04206-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/UT-InfraAI/sangam
  - Applies to: reproducibility context in `2607.04206-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Nitin Kedia
  - arXiv author search: https://arxiv.org/search/?query=Nitin%20Kedia&searchtype=author
  - Applies to: the reviewed paper and `2607.04206-whitepaper-review.md`.
- Author: Saurabh Agarwal
  - arXiv author search: https://arxiv.org/search/?query=Saurabh%20Agarwal&searchtype=author
  - Applies to: the reviewed paper and `2607.04206-whitepaper-review.md`.
- Author: Myungjin Lee
  - arXiv author search: https://arxiv.org/search/?query=Myungjin%20Lee&searchtype=author
  - Applies to: the reviewed paper and `2607.04206-whitepaper-review.md`.
- Author: Aditya Akella
  - arXiv author search: https://arxiv.org/search/?query=Aditya%20Akella&searchtype=author
  - Applies to: the reviewed paper and `2607.04206-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
