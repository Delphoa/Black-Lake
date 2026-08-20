# DEP-A-20260814-Variable Width Models

#artificial-intelligence #transformers #model-scaling #variable-width #KV-cache #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.18246v1, *Variable-Width Transformers*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.18246-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.18246-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Across these settings, we find that × \times -shaped models (wide in early and late layers but narrower in the middle) outperform parameter-matched constant-width transformers. Figure 2 : Comparing variable-width transformers with different shapes, each sweeping over multiple hyperparameter choices. > <formers consistently outperform constant-width transformers on perplexity-based tasks, and the 2B > <former wins on most natural language understanding tasks.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Interpret variable width as depth-wise capacity allocation rather than a new attention primitive: compare parameter-, FLOP-, and loss-matched profiles, trace information through residual resizing, and falsify the bottleneck thesis with alternative nonuniform schedules.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.18246v1
  - Applies to: `2606.18246-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.18246v1
  - Applies to: `2606.18246-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.18246v1
  - Applies to: `2606.18246-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.18246
  - Applies to: `2606.18246-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/ZhaofengWu/variable-width-transformers
  - Applies to: reproducibility context in `2606.18246-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Zhaofeng Wu
  - arXiv author search: https://arxiv.org/search/?query=Zhaofeng%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2606.18246-whitepaper-review.md`.
- Author: Oliver Sieberling
  - arXiv author search: https://arxiv.org/search/?query=Oliver%20Sieberling&searchtype=author
  - Applies to: the reviewed paper and `2606.18246-whitepaper-review.md`.
- Author: Shawn Tan
  - arXiv author search: https://arxiv.org/search/?query=Shawn%20Tan&searchtype=author
  - Applies to: the reviewed paper and `2606.18246-whitepaper-review.md`.
- Author: Rameswar Panda
  - arXiv author search: https://arxiv.org/search/?query=Rameswar%20Panda&searchtype=author
  - Applies to: the reviewed paper and `2606.18246-whitepaper-review.md`.
- Author: Yury Polyanskiy
  - arXiv author search: https://arxiv.org/search/?query=Yury%20Polyanskiy&searchtype=author
  - Applies to: the reviewed paper and `2606.18246-whitepaper-review.md`.
- Author: Yoon Kim
  - arXiv author search: https://arxiv.org/search/?query=Yoon%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2606.18246-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
