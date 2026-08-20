# DEP-A-20260819-QuIVer Rethinking ANN Gra

#artificial-intelligence #arXiv #paper-review #model-compression #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.02171v3, *QuIVer: Rethinking ANN Graph Topology via Training-Free Binary Quantization*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.02171-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.02171-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We compare QuIVer against nine baselines on Cohere-1M (768-d), all evaluated on the same hardware (Ryzen 7 7840HS, 32 GB RAM): hnswlib ( malkov2020hnsw, ) (reference C++ HNSW), FAISS HNSW ( johnson2019faiss, ) (IndexHNSWFlat, optimized C++/Python), USearch ( usearch2024, ) (production Rust HNSW), DiskANN Rust ( jayaram2019diskann, ) (float32 Vamana graph, Microsoft’s official Rust rewrite of DiskANN), DiskANN PQ+FP (PQ-navigated Vamana graph with float32 reranking, 96 PQ sub-spaces), DiskANN SSD (disk-resident Vamana graph with per-hop I/O, PQ-96 in RAM, beam_width = = 4, 50K cached nodes), FAISS OPQ+IVF-PQ+Refine ( jegou2011pq, ; ge2013opq, ) (production-grade quantization pipeline), FAISS IVF+RaBitQ+Refine ( gao2023rabitq, ) (IVF1024 with RaBitQ FastScan coarse search and SQ8 reranking, the Pareto-best nprobe and k_factor at each recall level), and DiskANN PQ-only (PQ-navigated graph without float32 reranking, shown only in the Pareto plot). Recent concurrent work δ \delta -EMG ( xiang2025emg, ) provides provable ( 1 / δ ) (1/\delta) -approximation guarantees via monotonic geometric constraints and integrates vector quantization to accelerate distance computation within a graph framework; however, it applies quantization only.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat QuIVer: Rethinking ANN Graph Topology via Training-Free Binary Quantization as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.02171v3
  - Applies to: `2605.02171-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.02171v3
  - Applies to: `2605.02171-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.02171v3
  - Applies to: `2605.02171-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.02171
  - Applies to: `2605.02171-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Wenxuan Xiao
  - arXiv author search: https://arxiv.org/search/?query=Wenxuan%20Xiao&searchtype=author
  - Applies to: the reviewed paper and `2605.02171-whitepaper-review.md`.
- Author: Zhiyou Wang
  - arXiv author search: https://arxiv.org/search/?query=Zhiyou%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2605.02171-whitepaper-review.md`.
- Author: Chengcheng Li
  - arXiv author search: https://arxiv.org/search/?query=Chengcheng%20Li&searchtype=author
  - Applies to: the reviewed paper and `2605.02171-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
