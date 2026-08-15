# DEP-A-20260816-Windowed MTP

#artificial-intelligence #speculative-decoding #multi-token-prediction #KV-cache #long-context #SGLang

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.21535v1, *Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.21535-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.21535-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Closest to us, LongSpec [Yang et al., 2026 ] and SpecExtend [Cha et al., 2026 ] also accelerate long-context SD: LongSpec trains a dedicated draft with a constant-size KV cache and hybrid tree attention (dense targets, ≤ 64 {\leq}64 K), while SpecExtend is training-free and drop-in but relies on a separate draft model with a cross-model retrieval KV policy, evaluated at shorter long-context regimes than the 1M we target. RoPE [Su et al., 2024 ] with position interpolation [Chen et al., 2023b ] and YaRN [Peng et al., 2023 ] enables the million-token contexts we study; to show the tax and its fix are not RoPE-specific, we also evaluate a Mamba2-hybrid [Gu and Dao, 2023 , Dao and Gu, 2024 ] whose attention uses no position embedding (NoPE). (The 2K and 4K points are statistically tied: at 1M the draft window is a negligible fraction of the target’s full-attention verify, so doubling it from 2K to 4K moves per-token latency by well under a microsecond.) Both directions away from it are worse—shrinking to 1K is too tight for retrieval and loses acceptance ( 4.74 → 3.79 4.74\to 3.79 ), while growing the window back toward full context pays the draft’s 𝒪 ​ ( S ) \mathcal{O}(S) context tax for no accuracy gain (native is both slower and.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260812-KVBuffer Serving](../DEP-A-20260812-KVBuffer%20Serving/README.md) - direct decode-time KV-cache serving context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.21535v1
  - Applies to: `2607.21535-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.21535v1
  - Applies to: `2607.21535-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.21535v1
  - Applies to: `2607.21535-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.21535
  - Applies to: `2607.21535-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/avalliappan-nvidia/windowed-mtp-b200
  - Applies to: reproducibility context in `2607.21535-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://zenodo.org/records/21522902
  - Applies to: reproducibility context in `2607.21535-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Alagappan Valliappan
  - arXiv author search: https://arxiv.org/search/?query=Alagappan%20Valliappan&searchtype=author
  - Applies to: the reviewed paper and `2607.21535-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
