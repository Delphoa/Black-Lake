# DEP-A-20260818-Requential Coding Pushing

#artificial-intelligence #arXiv #paper-review #model-compression #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.11883v1, *Requential Coding: Pushing the Limits of Model Compression with Self-Generated Training Data*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.11883-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.11883-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: At a high level, requential coding changes prequential coding (Section 2 ) in one way: rather than training on a pre-existing dataset, the student trains on data it itself generates, and the code records only the small amount of information a stronger teacher model contributes by deciding which of the self-generated samples are worth training on. Alternatively, prequential coding [ 2 , 1 ] codes a model through its training data, compressed using the training process itself, but the code grows linearly with dataset size as it must encode the exact dataset encountered regardless of how much information the model extracts. Since prequential coding simultaneously encodes both the model and its training data, a commonly used heuristic for isolating the information stored in the final model P T P_{T} alone is L heuristic ​ ( P T ) = ∑ t = 0 T − 1 log ⁡ 1 / P t ​ ( X t ) − log ⁡ 1 / P T ​ ( X t ) , L_{\mathrm{heuristic}}(P_{T})=\sum_{t=0}^{T-1}\log 1/P_{t}(X_{t})-\log 1/P_{T}(X_{t}), i.e., subtracting the compressed size of the data X 0 : T − 1 X_{0:T-1} given P T P_{T} from the combined code length for both P T P_{T} and X 0 : T − 1 X_{0:T-1} [ 1 , 6 , 47 , 52 , 8 , 7 ] .

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Requential Coding: Pushing the Limits of Model Compression with Self-Generated Training Data as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.11883v1
  - Applies to: `2607.11883-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.11883v1
  - Applies to: `2607.11883-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.11883v1
  - Applies to: `2607.11883-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.11883
  - Applies to: `2607.11883-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/shikaiqiu/requential-coding
  - Applies to: reproducibility context in `2607.11883-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Shikai Qiu
  - arXiv author search: https://arxiv.org/search/?query=Shikai%20Qiu&searchtype=author
  - Applies to: the reviewed paper and `2607.11883-whitepaper-review.md`.
- Author: Marc Finzi
  - arXiv author search: https://arxiv.org/search/?query=Marc%20Finzi&searchtype=author
  - Applies to: the reviewed paper and `2607.11883-whitepaper-review.md`.
- Author: Yujia Zheng
  - arXiv author search: https://arxiv.org/search/?query=Yujia%20Zheng&searchtype=author
  - Applies to: the reviewed paper and `2607.11883-whitepaper-review.md`.
- Author: Kun Zhang
  - arXiv author search: https://arxiv.org/search/?query=Kun%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.11883-whitepaper-review.md`.
- Author: Andrew Gordon Wilson
  - arXiv author search: https://arxiv.org/search/?query=Andrew%20Gordon%20Wilson&searchtype=author
  - Applies to: the reviewed paper and `2607.11883-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
