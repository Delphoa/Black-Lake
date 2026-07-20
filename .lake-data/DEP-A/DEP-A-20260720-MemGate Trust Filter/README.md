# DEP-A-20260720-MemGate Trust Filter

#artificial-intelligence #agent-memory #trust #memory-selection #safety #long-horizon-agents

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.06054v1, *Beyond Similarity: Trustworthy Memory Search for Personal AI Agents*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.06054-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.06054-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: MemGate places a learned gate between semantic retrieval and context injection. Using frozen sentence embeddings and a compact classifier, it rejects memories that are semantically related but contextually inappropriate, targeting cross-domain leakage, sycophancy, tool-call drift, and memory-borne jailbreaks across A-Mem, Mem0, MemOS, and OpenClaw.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat memory admission as policy enforcement with calibrated abstention: retain gate scores, reason codes, tenant and domain labels, and a conservative no-memory fallback, then red-team the gate with adaptive paraphrases and measure utility-risk frontiers rather than one threshold.

## Associated DEP Records

- [DEP-A-20260715-FAIR GraphRAG A Retrieval](../DEP-A-20260715-FAIR%20GraphRAG%20A%20Retrieval/README.md) - direct governed graph retrieval context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.06054v1
  - Applies to: `2606.06054-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.06054v1
  - Applies to: `2606.06054-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.06054v1
  - Applies to: `2606.06054-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.06054
  - Applies to: `2606.06054-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/Kevin-Zh-CS/MemGate
  - Applies to: reproducibility context in `2606.06054-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Jiawen Zhang
  - arXiv author search: https://arxiv.org/search/?query=Jiawen%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.06054-whitepaper-review.md`.
- Author: Kejia Chen
  - arXiv author search: https://arxiv.org/search/?query=Kejia%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2606.06054-whitepaper-review.md`.
- Author: Jiachen Ma
  - arXiv author search: https://arxiv.org/search/?query=Jiachen%20Ma&searchtype=author
  - Applies to: the reviewed paper and `2606.06054-whitepaper-review.md`.
- Author: Yangfan Hu
  - arXiv author search: https://arxiv.org/search/?query=Yangfan%20Hu&searchtype=author
  - Applies to: the reviewed paper and `2606.06054-whitepaper-review.md`.
- Author: Lipeng He
  - arXiv author search: https://arxiv.org/search/?query=Lipeng%20He&searchtype=author
  - Applies to: the reviewed paper and `2606.06054-whitepaper-review.md`.
- Author: Yechao Zhang
  - arXiv author search: https://arxiv.org/search/?query=Yechao%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.06054-whitepaper-review.md`.
- Author: Jian Liu
  - arXiv author search: https://arxiv.org/search/?query=Jian%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2606.06054-whitepaper-review.md`.
- Author: Xiaohu Yang
  - arXiv author search: https://arxiv.org/search/?query=Xiaohu%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2606.06054-whitepaper-review.md`.
- Author: Tianwei Zhang
  - arXiv author search: https://arxiv.org/search/?query=Tianwei%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.06054-whitepaper-review.md`.
- Author: Ruoxi Jia
  - arXiv author search: https://arxiv.org/search/?query=Ruoxi%20Jia&searchtype=author
  - Applies to: the reviewed paper and `2606.06054-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
