# DEP-A-20260714-CompressKV Semantic Heads

#arxiv #kv-cache #cache-compression #long-context #attention-heads #semantic-retrieval #grouped-query-attention #resource-efficiency #language-model-inference #machine-learning

This cold-storage artifact preserves a public-safe, whitepaper-grade full-paper review of **“CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference,” arXiv:2606.24467v1**. The review reconstructs semantic retrieval-head identification, layer-error-based budget allocation, reported LongBench and NIAH results, ablations, integrations, systems evidence, limitations, external primary-source checks, and an independent re-conceptualization. The canonical record’s administrator note about substantial overlap with the same authors’ earlier arXiv:2508.02401 paper is preserved as a material provenance qualification. The source paper was verified from a locally archived complete PDF and full-paper HTML; source documents remain local and are withheld from this repository.

Deposition date: 2026-07-14
Stable paper version: arXiv:2606.24467v1

## Contents

- `README.md` — deposition inventory, context, relationships, and final source attribution.
- `2606.24467-whitepaper-review.md` — validated public-safe full-paper review and independent re-conceptualization.

## Summary of Items

### `README.md`

Defines the DEP-A scope, identifies the stable paper version and earlier overlapping record, inventories every file, explains the entry’s relevance, links the strongest corresponding DEP context, and records the public sources and complete author attribution used for verification.

### `2606.24467-whitepaper-review.md`

Reconstructs the offline semantic retrieval-head score, online observation-window token selection, error-aware layer allocation, four-model LongBench evaluation, NIAH retrieval results, causal head masking, component and head-count ablations, efficiency profiling, compatibility with sparse prefilling and quantization, evidence boundaries, deployment safeguards, falsifiable hypotheses, and replication priorities. Its ledger covers every numbered paper table, figure, and central equation.

## Insights and Relevance

The durable design insight is to use functionally selected internal model signals as memory controllers rather than averaging indiscriminately over all attention heads. CompressKV separates position relevance, layer vulnerability, and physical storage, making each controller replaceable. The evidence supports a favorable memory–quality trade-off in the tested settings, while the review preserves the main limitations: answer-conditioned offline calibration, graph-only systems results, no uncertainty estimates, irreversible eviction, and no direct energy, carbon, or cost measurement. The newer arXiv record is treated as part of the same CompressKV research lineage as arXiv:2508.02401, not independent corroboration.

## Associated DEP Records

- [Delphoa-Labs/Black-Lake-Data DEP-20260702-Tech Intel 0103](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260702-Tech%20Intel%200103) — close conceptual work for SeKV, a contemporaneous hierarchical and reconstructive KV-cache alternative. It is not the same paper and does not validate CompressKV.

No same-paper DEP-A, DEP-E, or Delphoa-Labs/Black-Lake-Data record was verified for arXiv:2606.24467 or the overlapping arXiv:2508.02401 after checking the live class indexes, DEP READMEs, logs, and reports by arXiv ID, DOI, title, method, benchmark, and implementation.

## Attribution Block

- Source URL: https://arxiv.org/abs/2606.24467
  - Applies to: `2606.24467-whitepaper-review.md`
  - Notes: Canonical arXiv record for v1, including title, complete authorship, submission history, public source links, administrator overlap note, and arXiv-issued DOI.
- Source URL: https://arxiv.org/pdf/2606.24467
  - Applies to: `2606.24467-whitepaper-review.md`
  - Notes: Canonical public PDF locator. A complete 14-page PDF was verified locally and withheld from the repository.
- Source URL: https://arxiv.org/html/2606.24467
  - Applies to: `2606.24467-whitepaper-review.md`
  - Notes: Canonical full-paper HTML locator. Complete full-paper HTML was verified locally and withheld from the repository.
- Source URL: https://doi.org/10.48550/arXiv.2606.24467
  - Applies to: `2606.24467-whitepaper-review.md`
  - Notes: arXiv-issued DOI for the canonical reviewed record.
- Source URL: https://arxiv.org/abs/2508.02401
  - Applies to: `README.md` and `2606.24467-whitepaper-review.md`
  - Notes: Same-author earlier CompressKV record explicitly linked by the canonical administrator overlap note; used to preserve research-lineage provenance.
- Source URL: https://doi.org/10.48550/arXiv.2508.02401
  - Applies to: `README.md` and `2606.24467-whitepaper-review.md`
  - Notes: arXiv-issued DOI for the earlier overlapping record.
- Source URL: https://github.com/TUDa-HWAI/CompressKV
  - Applies to: `2606.24467-whitepaper-review.md`
  - Notes: Official implementation inspected for method, retrieval-head identification, LongBench, NIAH, scoring, integration, dependency, release, and licensing evidence. Code was not executed.
- Source URL: https://sure-wshop.github.io/
  - Applies to: `2606.24467-whitepaper-review.md`
  - Notes: Official SuRE @ IJCAI 2026 page used to verify the future workshop date and its quantitative resource-efficiency remit.
- Source URL: https://openreview.net/forum?id=EytBpUGB1Z
  - Applies to: `2606.24467-whitepaper-review.md`
  - Notes: Primary Retrieval Heads record used to vet conceptual provenance.
- Source URL: https://aclanthology.org/2023.acl-long.499/
  - Applies to: `2606.24467-whitepaper-review.md`
  - Notes: Primary ACL Anthology record used to verify LongBench’s multi-task evaluation scope.
- Source URL: https://github.com/gkamradt/LLMTest_NeedleInAHaystack
  - Applies to: `2606.24467-whitepaper-review.md`
  - Notes: Primary NIAH repository used to verify benchmark purpose and limitations.
- Source URL: https://arxiv.org/abs/2606.31145
  - Applies to: `README.md` and `2606.24467-whitepaper-review.md`
  - Notes: Canonical SeKV record used as a directly relevant reconstructive KV-cache alternative.
- Authors from the canonical arXiv record:
  - Xiaolin Lin — https://arxiv.org/search/cs?query=Lin%2C+X&searchtype=author
  - Jingcun Wang — https://arxiv.org/search/cs?query=Wang%2C+J&searchtype=author
  - Olga Kondrateva — https://arxiv.org/search/cs?query=Kondrateva%2C+O&searchtype=author
  - Yiyu Shi — https://arxiv.org/search/cs?query=Shi%2C+Y&searchtype=author
  - Bing Li — https://arxiv.org/search/cs?query=Li%2C+B&searchtype=author
  - Grace Li Zhang — https://arxiv.org/search/cs?query=Zhang%2C+G&searchtype=author
  - Applies to: `README.md` and `2606.24467-whitepaper-review.md`
  - Notes: Complete author attribution from the canonical record; profile links are arXiv author searches supplied by the locally verified provenance record. All source documents were verified locally and withheld from this repository.
