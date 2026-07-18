# DEP-A-20260718-Jet Long Bifocal RoPE

#artificial-intelligence #long-context #RoPE #KV-cache #FlashAttention #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.07740v2, *Jet-Long: Efficient Long-Context Extension with Dynamic Bifocal RoPE*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.07740-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.07740-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Jet-Long uses a RoPE-faithful local window and a remote window whose integer grouping factor grows analytically with current sequence length. Remote positions are aliased into the pretrained range; correction rotations preserve the original KV cache during decode, and inclusion-exclusion combines local and remote prefill attention.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: deploy dynamic bifocal RoPE with a context-length and task-aware validation policy that logs G transitions, retrieval failures, short-context identity, kernel path, and fallback when aliasing risk is high.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.07740v2
  - Applies to: `2607.07740-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.07740v2
  - Applies to: `2607.07740-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.07740v2
  - Applies to: `2607.07740-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.07740
  - Applies to: `2607.07740-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/jet-ai-projects/jet-long
  - Applies to: reproducibility context in `2607.07740-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Haozhan Tang
  - arXiv author search: https://arxiv.org/search/?query=Haozhan%20Tang&searchtype=author
  - Applies to: the reviewed paper and `2607.07740-whitepaper-review.md`.
- Author: Zerui Wang
  - arXiv author search: https://arxiv.org/search/?query=Zerui%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.07740-whitepaper-review.md`.
- Author: Yuxian Gu
  - arXiv author search: https://arxiv.org/search/?query=Yuxian%20Gu&searchtype=author
  - Applies to: the reviewed paper and `2607.07740-whitepaper-review.md`.
- Author: Song Han
  - arXiv author search: https://arxiv.org/search/?query=Song%20Han&searchtype=author
  - Applies to: the reviewed paper and `2607.07740-whitepaper-review.md`.
- Author: Han Cai
  - arXiv author search: https://arxiv.org/search/?query=Han%20Cai&searchtype=author
  - Applies to: the reviewed paper and `2607.07740-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
