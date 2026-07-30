# DEP-A-20260731-Hidden Decoding

#artificial-intelligence #language-models #hidden-decoding #inference-scaling #latent-computation #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.08186v1, *Hidden Decoding at Scale: Latent Computation Scaling for Large Language Models*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.08186-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.08186-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Consistent with this, looped models have stayed small: the largest is the 40B dense LoopCoder, trained without pipeline parallelism [ yang2026iquestcoderv1technicalreport ] , while other looped language models remain at a few billion parameters [ geiping2025latent_recurrent , zhu2025ouro ] . In this work, we propose a sequence-length scaling method named Hidden Decoding , which improves the capability of frontier-scale LLMs through continued pretraining (CPT). This efficiency is what makes Hidden Decoding practical to train at the scale of MoE models with over 100B parameters, a regime not reached by prior looped or length-scaling methods.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Expose sequential hidden decoding as a bounded inference mode whose extra latent streams carry explicit compute budgets, early-exit criteria, uncertainty monitoring, and a standard autoregressive fallback when hidden-stream agreement degrades.

## Associated DEP Records

- [DEP-A-20260714-GRC Latent Registers](../DEP-A-20260714-GRC%20Latent%20Registers/README.md) - direct latent-representation, compressed-context, and inference context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.08186v1
  - Applies to: `2607.08186-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.08186v1
  - Applies to: `2607.08186-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.08186v1
  - Applies to: `2607.08186-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.08186
  - Applies to: `2607.08186-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/Tencent/Sequential-Hidden-Decoding
  - Applies to: reproducibility context in `2607.08186-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://huggingface.co/collections/tencent/sequential-hidden-decoding
  - Applies to: reproducibility context in `2607.08186-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Aiwei Liu
  - arXiv author search: https://arxiv.org/search/?query=Aiwei%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Cheng Shi
  - arXiv author search: https://arxiv.org/search/?query=Cheng%20Shi&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Chuhan Wu
  - arXiv author search: https://arxiv.org/search/?query=Chuhan%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Ci Lei
  - arXiv author search: https://arxiv.org/search/?query=Ci%20Lei&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Di Lu
  - arXiv author search: https://arxiv.org/search/?query=Di%20Lu&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Donald He
  - arXiv author search: https://arxiv.org/search/?query=Donald%20He&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Fan Zhang
  - arXiv author search: https://arxiv.org/search/?query=Fan%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Fanhao Kong
  - arXiv author search: https://arxiv.org/search/?query=Fanhao%20Kong&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Feifei Zhang
  - arXiv author search: https://arxiv.org/search/?query=Feifei%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Guan Wang
  - arXiv author search: https://arxiv.org/search/?query=Guan%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Haicheng Wang
  - arXiv author search: https://arxiv.org/search/?query=Haicheng%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Haoyu Liu
  - arXiv author search: https://arxiv.org/search/?query=Haoyu%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Houjin Yu
  - arXiv author search: https://arxiv.org/search/?query=Houjin%20Yu&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Jiachen Ding
  - arXiv author search: https://arxiv.org/search/?query=Jiachen%20Ding&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Jiayi Feng
  - arXiv author search: https://arxiv.org/search/?query=Jiayi%20Feng&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Jie Zhou
  - arXiv author search: https://arxiv.org/search/?query=Jie%20Zhou&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Jijun Chi
  - arXiv author search: https://arxiv.org/search/?query=Jijun%20Chi&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Jindi Shi
  - arXiv author search: https://arxiv.org/search/?query=Jindi%20Shi&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Jing Lei
  - arXiv author search: https://arxiv.org/search/?query=Jing%20Lei&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Junjie Zhang
  - arXiv author search: https://arxiv.org/search/?query=Junjie%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Laiyi Li
  - arXiv author search: https://arxiv.org/search/?query=Laiyi%20Li&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Le Tian
  - arXiv author search: https://arxiv.org/search/?query=Le%20Tian&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Linhao Zhang
  - arXiv author search: https://arxiv.org/search/?query=Linhao%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Miao Fan
  - arXiv author search: https://arxiv.org/search/?query=Miao%20Fan&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Sijun Zhang
  - arXiv author search: https://arxiv.org/search/?query=Sijun%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Wei Jia
  - arXiv author search: https://arxiv.org/search/?query=Wei%20Jia&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Weiwei Shi
  - arXiv author search: https://arxiv.org/search/?query=Weiwei%20Shi&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Wenhan Li
  - arXiv author search: https://arxiv.org/search/?query=Wenhan%20Li&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Wentao Zhao
  - arXiv author search: https://arxiv.org/search/?query=Wentao%20Zhao&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Wenteng Liang
  - arXiv author search: https://arxiv.org/search/?query=Wenteng%20Liang&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Xiao Zhou
  - arXiv author search: https://arxiv.org/search/?query=Xiao%20Zhou&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Xiaojin Zhou
  - arXiv author search: https://arxiv.org/search/?query=Xiaojin%20Zhou&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Xihuai Wang
  - arXiv author search: https://arxiv.org/search/?query=Xihuai%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Xinyu Gao
  - arXiv author search: https://arxiv.org/search/?query=Xinyu%20Gao&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Xuanliang Wang
  - arXiv author search: https://arxiv.org/search/?query=Xuanliang%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Xuyang Ao
  - arXiv author search: https://arxiv.org/search/?query=Xuyang%20Ao&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Yang Yu
  - arXiv author search: https://arxiv.org/search/?query=Yang%20Yu&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Yangxiu You
  - arXiv author search: https://arxiv.org/search/?query=Yangxiu%20You&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Yinuo Zhao
  - arXiv author search: https://arxiv.org/search/?query=Yinuo%20Zhao&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Yufei Kuang
  - arXiv author search: https://arxiv.org/search/?query=Yufei%20Kuang&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Yufei Wang
  - arXiv author search: https://arxiv.org/search/?query=Yufei%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Yuan Liu
  - arXiv author search: https://arxiv.org/search/?query=Yuan%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Yuwen Chen
  - arXiv author search: https://arxiv.org/search/?query=Yuwen%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Zhencong Tian
  - arXiv author search: https://arxiv.org/search/?query=Zhencong%20Tian&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Zhongyin Zhao
  - arXiv author search: https://arxiv.org/search/?query=Zhongyin%20Zhao&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Zilin Yu
  - arXiv author search: https://arxiv.org/search/?query=Zilin%20Yu&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Author: Zitao Wang
  - arXiv author search: https://arxiv.org/search/?query=Zitao%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.08186-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
