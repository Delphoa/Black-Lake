# DEP-A-20260801-Long Context TTT

#artificial-intelligence #test-time-training #long-context #language-models #adaptation #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.09415v1, *Self-Guided Test-Time Training for Long-Context LLMs*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.09415-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.09415-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: This suggests that the central bottleneck of long-context TTT is not the adaptation mechanism itself, but rather test-time training-data quality . We propose Self-Guided TTT (S-TTT), a simple and effective framework that uses the LLM itself to select question-relevant evidence spans for test-time training, avoiding the expensive computational cost of full-context training and mitigating the severe noise of random span sampling. A broad line of work addresses long-context limitations by extending usable context windows ( peng2024yarn ; chen2024longlora ) , improving prefill or attention efficiency ( jiang2024minference ) , compressing prompts ( jiang2024longllmlingua ) , retrieving external evidence ( lewis2020rag ; zhang2025qrhead ) , or analyzing and steering attention behavior at inference time ( wu2024retrievalhead ; zhang2025qrhead ; ye_dysco_2026 ) .

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Constrain self-guided test-time training to a reversible adaptation envelope: retain the self-supervised signal, update steps, parameter delta, held-out degradation checks, and rollback trigger, then test whether long-context gains reflect task learning rather than leakage, memorization, or prompt-specific overfitting.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.09415v1
  - Applies to: `2607.09415-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.09415v1
  - Applies to: `2607.09415-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.09415v1
  - Applies to: `2607.09415-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.09415
  - Applies to: `2607.09415-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Xinyu Zhu
  - arXiv author search: https://arxiv.org/search/?query=Xinyu%20Zhu&searchtype=author
  - Applies to: the reviewed paper and `2607.09415-whitepaper-review.md`.
- Author: Zhe Xu
  - arXiv author search: https://arxiv.org/search/?query=Zhe%20Xu&searchtype=author
  - Applies to: the reviewed paper and `2607.09415-whitepaper-review.md`.
- Author: Xiaohan Wei
  - arXiv author search: https://arxiv.org/search/?query=Xiaohan%20Wei&searchtype=author
  - Applies to: the reviewed paper and `2607.09415-whitepaper-review.md`.
- Author: Yunchen Pu
  - arXiv author search: https://arxiv.org/search/?query=Yunchen%20Pu&searchtype=author
  - Applies to: the reviewed paper and `2607.09415-whitepaper-review.md`.
- Author: Fei Tian
  - arXiv author search: https://arxiv.org/search/?query=Fei%20Tian&searchtype=author
  - Applies to: the reviewed paper and `2607.09415-whitepaper-review.md`.
- Author: Chonglin Sun
  - arXiv author search: https://arxiv.org/search/?query=Chonglin%20Sun&searchtype=author
  - Applies to: the reviewed paper and `2607.09415-whitepaper-review.md`.
- Author: Kaushik Rangadurai
  - arXiv author search: https://arxiv.org/search/?query=Kaushik%20Rangadurai&searchtype=author
  - Applies to: the reviewed paper and `2607.09415-whitepaper-review.md`.
- Author: Hua Zhi
  - arXiv author search: https://arxiv.org/search/?query=Hua%20Zhi&searchtype=author
  - Applies to: the reviewed paper and `2607.09415-whitepaper-review.md`.
- Author: Frank Shyu
  - arXiv author search: https://arxiv.org/search/?query=Frank%20Shyu&searchtype=author
  - Applies to: the reviewed paper and `2607.09415-whitepaper-review.md`.
- Author: Sandeep Pandey
  - arXiv author search: https://arxiv.org/search/?query=Sandeep%20Pandey&searchtype=author
  - Applies to: the reviewed paper and `2607.09415-whitepaper-review.md`.
- Author: Luke Simon
  - arXiv author search: https://arxiv.org/search/?query=Luke%20Simon&searchtype=author
  - Applies to: the reviewed paper and `2607.09415-whitepaper-review.md`.
- Author: Yu Meng
  - arXiv author search: https://arxiv.org/search/?query=Yu%20Meng&searchtype=author
  - Applies to: the reviewed paper and `2607.09415-whitepaper-review.md`.
- Author: Xi Liu
  - arXiv author search: https://arxiv.org/search/?query=Xi%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.09415-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
