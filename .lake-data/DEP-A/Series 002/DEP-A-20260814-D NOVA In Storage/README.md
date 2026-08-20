# DEP-A-20260814-D NOVA In Storage

#computer-architecture #retrieval-augmented-generation #in-storage-computing #vector-search #3D-NAND #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.17538v1, *D-NOVA: In-Storage Retrieval Accelerator via Dual-Bound 3D NAND-Optimized Similarity Search with Vector Adaptation*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.17538-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.17538-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: D-NOVA is a highly parallel in-storage retrieval architecture that embeds search functionality deeply into the memory array with negligible peripheral hardware changes. Although recent in-storage accelerators aim to reduce data movement, they still rely on host or embedded processors outside the memory, where nearly 70% of the total retrieval time is spent. D-NOVA is up to 41.7× faster and 71× more energy-efficient than a CPU baseline, and achieves 12.13× higher throughput while being up to 1.26× more energy-efficient than state-of-the-art in-storage RAG accelerators, demonstrating the potential of fully in-storage vector search for scalable RAG acceleration.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Operate in-storage retrieval as a hardware-software approximation pipeline: preserve vector adaptation, NAND sensing bounds, candidate stages, recall, endurance, and host work, then test whether system gains survive device variation and equal-recall baselines.

## Associated DEP Records

- [DEP-A-20260725-RAR Reranking Intake](../../Series%20001/DEP-A-20260725-RAR%20Reranking%20Intake/README.md) - direct retrieval representation, reranking, and evaluation context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260804-KernelFlume Serving](../../Series%20001/DEP-A-20260804-KernelFlume%20Serving/README.md) - direct LLM-serving latency and systems-efficiency context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.17538v1
  - Applies to: `2607.17538-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.17538v1
  - Applies to: `2607.17538-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.17538v1
  - Applies to: `2607.17538-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.17538
  - Applies to: `2607.17538-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Chang Eun Song
  - arXiv author search: https://arxiv.org/search/?query=Chang%20Eun%20Song&searchtype=author
  - Applies to: the reviewed paper and `2607.17538-whitepaper-review.md`.
- Author: Sumukh Pinge
  - arXiv author search: https://arxiv.org/search/?query=Sumukh%20Pinge&searchtype=author
  - Applies to: the reviewed paper and `2607.17538-whitepaper-review.md`.
- Author: Tianqi Zhang
  - arXiv author search: https://arxiv.org/search/?query=Tianqi%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.17538-whitepaper-review.md`.
- Author: Sung Eun Kim
  - arXiv author search: https://arxiv.org/search/?query=Sung%20Eun%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2607.17538-whitepaper-review.md`.
- Author: Tajana S. Rosing
  - arXiv author search: https://arxiv.org/search/?query=Tajana%20S.%20Rosing&searchtype=author
  - Applies to: the reviewed paper and `2607.17538-whitepaper-review.md`.
- Author: Mingu Kang
  - arXiv author search: https://arxiv.org/search/?query=Mingu%20Kang&searchtype=author
  - Applies to: the reviewed paper and `2607.17538-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
