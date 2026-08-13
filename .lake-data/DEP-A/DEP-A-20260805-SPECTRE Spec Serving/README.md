# DEP-A-20260805-SPECTRE Spec Serving

#artificial-intelligence #LLM-serving #speculative-decoding #parallel-decoding #resource-efficiency #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.08151v2, *SPECTRE: Hybrid Ordinary-Parallel Speculative Serving for Resource-Efficient LLM Inference*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.08151-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.08151-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We present SPECTRE , a hybrid ordinary-parallel speculative serving framework for remote draft-target deployment as shown in Figure 3 . Describe the issue below: 1]Jincheng Xie 2 Yawen Ling 2 Qi Xiao 2 Feiyu Zhang 1 Zhongyi Huang 2 Wen Hu ⋆ 3 Yu Zheng ⋆ 1]Tsinghua University 2 AI Infra Team at JDT 3 JD iCity, JD Technology, JD Intelligent Cities Research ]xiejc22@mails.tsinghua.edu.cn {lingyawen1, xiaoqi.31, zhangfeiyu.17}@jd.com zhongyih@tsinghua.edu.cn msyuzheng@outlook.com huwen.31@jd.com *]Corresponding Author SPECTRE: Hybrid Ordinary-Parallel Speculative Serving for Resource-Efficient LLM Inference Figure 2 illustrates the difference between ordinary and parallel speculative decoding. We propose SPECTRE (Parallel SPEC ulative Decoding with a Multi- T enant RE mote Drafter), a serving framework that reuses underutilized tail-model services as remote drafters for heavily loaded large-model services through speculative decoding.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Operate hybrid speculative serving as adaptive branch-width control: record draft provenance, ordinary and parallel acceptance, memory pressure, queue state, and fallback, then test tail latency and energy at equal output quality across workload and model shifts.

## Associated DEP Records

- [DEP-A-20260804-KernelFlume Serving](../DEP-A-20260804-KernelFlume%20Serving/README.md) - direct LLM-serving latency and systems-efficiency context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.08151v2
  - Applies to: `2605.08151-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.08151v2
  - Applies to: `2605.08151-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.08151v2
  - Applies to: `2605.08151-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.08151
  - Applies to: `2605.08151-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/sgl-project/sglang/pull/22272
  - Applies to: reproducibility context in `2605.08151-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://huggingface.co/AngelSlim/Qwen3-32B_eagle3
  - Applies to: reproducibility context in `2605.08151-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://huggingface.co/lmsys/Qwen3-235B-A22B-EAGLE3
  - Applies to: reproducibility context in `2605.08151-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Jincheng Xie
  - arXiv author search: https://arxiv.org/search/?query=Jincheng%20Xie&searchtype=author
  - Applies to: the reviewed paper and `2605.08151-whitepaper-review.md`.
- Author: Yawen Ling
  - arXiv author search: https://arxiv.org/search/?query=Yawen%20Ling&searchtype=author
  - Applies to: the reviewed paper and `2605.08151-whitepaper-review.md`.
- Author: Qi Xiao
  - arXiv author search: https://arxiv.org/search/?query=Qi%20Xiao&searchtype=author
  - Applies to: the reviewed paper and `2605.08151-whitepaper-review.md`.
- Author: Feiyu Zhang
  - arXiv author search: https://arxiv.org/search/?query=Feiyu%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2605.08151-whitepaper-review.md`.
- Author: Zhongyi Huang
  - arXiv author search: https://arxiv.org/search/?query=Zhongyi%20Huang&searchtype=author
  - Applies to: the reviewed paper and `2605.08151-whitepaper-review.md`.
- Author: Wen Hu
  - arXiv author search: https://arxiv.org/search/?query=Wen%20Hu&searchtype=author
  - Applies to: the reviewed paper and `2605.08151-whitepaper-review.md`.
- Author: Yu Zheng
  - arXiv author search: https://arxiv.org/search/?query=Yu%20Zheng&searchtype=author
  - Applies to: the reviewed paper and `2605.08151-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
