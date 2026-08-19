# DEP-A-20260819-Detecting Route Flip Is

#artificial-intelligence #arXiv #paper-review #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.11212v1, *Detecting a Route Flip Is Easier Than Knowing Whether to Fix It: Causal Route-Mediated Damage in Quantized Mixture-of-Experts*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.11212-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.11212-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: On DeepSeek-MoE-16B ( N = 384 N{=}384 , dose-matched), route-mediated damage decomposes into harmful ( + 0.2036 +0.2036 [ + 0.199 , + 0.208 ] [+0.199,+0.208] ) and beneficial ( − 0.1819 -0.1819 [ − 0.186 , − 0.178 ] [-0.186,-0.178] ) flip components that near-cancel ( cancellation 90.2 % 90.2\% ), and the oracle harm sign is not predictable from local router statistics (combined sign-AUC 0.507 0.507 , within the | AUC − 0.5 | ≤ 0.05 |\mathrm{AUC}-0.5|\leq 0.05 band). We study one deployment-origin disturbance—4-bit KV-cache quantization [ 12 , 23 ] under a protected BF16 gate (router weights and arithmetic in BF16, reading a quantized upstream hidden state)—and ask what damage flows through the routing decision, and whether that damage can be detected or repaired from signals available at inference. [empirical, pilot] Detecting a flip is not knowing whether to fix it.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat Detecting a Route Flip Is Easier Than Knowing Whether to Fix It: Causal Route-Mediated Damage in Quantized Mixture-of-Experts as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.11212v1
  - Applies to: `2608.11212-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.11212v1
  - Applies to: `2608.11212-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.11212v1
  - Applies to: `2608.11212-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2608.11212
  - Applies to: `2608.11212-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Parvel Gu
  - arXiv author search: https://arxiv.org/search/?query=Parvel%20Gu&searchtype=author
  - Applies to: the reviewed paper and `2608.11212-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
