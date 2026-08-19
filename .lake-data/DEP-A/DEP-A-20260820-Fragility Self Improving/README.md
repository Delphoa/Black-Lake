# DEP-A-20260820-Fragility Self Improving

#artificial-intelligence #arXiv #paper-review #RAG #agents #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.18066v1, *On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.18066-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.18066-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: To better understand this fragility, we manually investigate the memories written by the agents, and identify environment and task underspecification during memory generation as potential drivers for the large variance and degraded performance. While shuffled task orders create challenges for models to learn, we expect the overall success rate to be maintained at the same level as the no-memory baseline in these challenging settings; however, we see that performance often goes worse, raising concerns on the reliability of these self-improving methods in real-world settings. To understand the amplified variance and the unexpected performance drop when shuffled orders are used, we manually inspect the agent’s memory produced by the RBank method, where we identify underspecification as a potential cause of these issues.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.18066v1
  - Applies to: `2608.18066-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.18066v1
  - Applies to: `2608.18066-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.18066v1
  - Applies to: `2608.18066-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2608.18066
  - Applies to: `2608.18066-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/SalesforceAIResearch/self-improve-fragility
  - Applies to: reproducibility context in `2608.18066-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://huggingface.co/datasets/Salesforce/self-improve-fragility
  - Applies to: reproducibility context in `2608.18066-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Qinyuan Ye
  - arXiv author search: https://arxiv.org/search/?query=Qinyuan%20Ye&searchtype=author
  - Applies to: the reviewed paper and `2608.18066-whitepaper-review.md`.
- Author: Yu Li
  - arXiv author search: https://arxiv.org/search/?query=Yu%20Li&searchtype=author
  - Applies to: the reviewed paper and `2608.18066-whitepaper-review.md`.
- Author: Yada Pruksachatkun
  - arXiv author search: https://arxiv.org/search/?query=Yada%20Pruksachatkun&searchtype=author
  - Applies to: the reviewed paper and `2608.18066-whitepaper-review.md`.
- Author: Jiaxin Zhang
  - arXiv author search: https://arxiv.org/search/?query=Jiaxin%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2608.18066-whitepaper-review.md`.
- Author: Chien-Sheng Wu
  - arXiv author search: https://arxiv.org/search/?query=Chien-Sheng%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2608.18066-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
