# DEP-A-20260814-SWE Pruner Pro

#artificial-intelligence #coding-agents #context-pruning #hidden-representations #SWE-bench #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.18213v1, *SWE-Pruner Pro: The Coder LLM Already Knows What to Prune*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.18213-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.18213-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We propose SWE-Pruner Pro, a lightweight head that reads the pruning signal directly from the backbone with a learned length-aware embedding and a per-sample balanced focal loss. For pruner-vs-pruner comparison on the SWE-QA family and Oolong (Table 1 ), we run six prior pruners under the matched configuration, swapping only the pruning module: LLMLingua2 [ pan2024llmlingua ] , Selective Context [ li2023compressing ] , RAG (sliding-window retrieval with bge-reranker-v2-m3 2 2 2 https://huggingface.co/BAAI/bge-reranker-v2-m3 ), Self-Prune (the same agent backbone re-prompted on each r t r_{t} with our line-keep labelling prompt), LongCodeZip [ shi2025longcodezip ] (coarse-only function-level perplexity ranking), and SWE-Pruner [ swepruner2026 ] , the closest prior task-specific pruner. Token-level pruners score tokens by self-information or perplexity and drop the lowest-ranking ones [ jiang2023llmlingua , jiang2024longllmlingua , li2023compressing , fang2025attentionrag ] ; retrieval-based shorteners replace verbatim content with retrieved or aggregated snippets [ lewis2020retrieval , cheng2024xrag , cheng2026resolving , shi2026reasoning , zhang2023repocoder , lai2026transformers ] .

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Use the coder model's hidden states as a calibrated context-retention signal: preserve line labels, length features, pruned tool output, and resolution outcomes, and restore full context when uncertainty or repository shift makes the pruning head unreliable.

## Associated DEP Records

- [DEP-A-20260802-Coding Agent Context](../DEP-A-20260802-Coding%20Agent%20Context/README.md) - direct repository-scale coding-agent and verification context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260714-LCLM Context Compression](../DEP-A-20260714-LCLM%20Context%20Compression/README.md) - direct learned context and semantic-compression context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.18213v1
  - Applies to: `2607.18213-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.18213v1
  - Applies to: `2607.18213-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.18213v1
  - Applies to: `2607.18213-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.18213
  - Applies to: `2607.18213-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/Ayanami1314/swe-pruner-pro
  - Applies to: reproducibility context in `2607.18213-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Yuhang Wang
  - arXiv author search: https://arxiv.org/search/?query=Yuhang%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.18213-whitepaper-review.md`.
- Author: Yuling Shi
  - arXiv author search: https://arxiv.org/search/?query=Yuling%20Shi&searchtype=author
  - Applies to: the reviewed paper and `2607.18213-whitepaper-review.md`.
- Author: Shaoqiu Zhang
  - arXiv author search: https://arxiv.org/search/?query=Shaoqiu%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.18213-whitepaper-review.md`.
- Author: Jialiang Liang
  - arXiv author search: https://arxiv.org/search/?query=Jialiang%20Liang&searchtype=author
  - Applies to: the reviewed paper and `2607.18213-whitepaper-review.md`.
- Author: Shilin He
  - arXiv author search: https://arxiv.org/search/?query=Shilin%20He&searchtype=author
  - Applies to: the reviewed paper and `2607.18213-whitepaper-review.md`.
- Author: Siyu Ye
  - arXiv author search: https://arxiv.org/search/?query=Siyu%20Ye&searchtype=author
  - Applies to: the reviewed paper and `2607.18213-whitepaper-review.md`.
- Author: Yuting Chen
  - arXiv author search: https://arxiv.org/search/?query=Yuting%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2607.18213-whitepaper-review.md`.
- Author: Kai Cai
  - arXiv author search: https://arxiv.org/search/?query=Kai%20Cai&searchtype=author
  - Applies to: the reviewed paper and `2607.18213-whitepaper-review.md`.
- Author: Xiaodong Gu
  - arXiv author search: https://arxiv.org/search/?query=Xiaodong%20Gu&searchtype=author
  - Applies to: the reviewed paper and `2607.18213-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
