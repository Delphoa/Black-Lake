# DEP-A-20260813-Extremum Stack Memory

#information-theory #sequence-models #rate-independence #online-algorithms #memory #theory

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.05245v2, *The Extremum Stack as Optimal Memory for Rate-Independent Sequence Models: Information-Theoretic Foundations and Online Complexity*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.05245-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.05245-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: PAL [ 8 ] replaces the KV-cache with the extremum stack, reducing memory to O ​ ( k ⋅ d model ) O(k\cdot d_{\mathrm{model}}) for rate-independent tasks. The reduction of a Preisach output to the surviving extremum sequence (the “memory curve” or staircase interface) is classical; what has been missing is a converse: a proof that nothing but the stack matters for any computable rate-independent functional, together with quantitative minimality guarantees. Replacing the KV-cache in a Preisach attention architecture [ 8 ] with the extremum stack reduces memory from O ​ ( n ⋅ d model ) O(n\cdot d_{\mathrm{model}}) to O ​ ( k ⋅ d model ) O(k\cdot d_{\mathrm{model}}) .

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Use the extremum stack as a minimal sufficient event log for rate-independent controllers: retain the turning-point sequence, verify invariance under monotone reparameterization, and compare its online complexity with any proposed bounded-memory substitute.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.05245v2
  - Applies to: `2606.05245-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.05245v2
  - Applies to: `2606.05245-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.05245v2
  - Applies to: `2606.05245-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.05245
  - Applies to: `2606.05245-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Piotr Frydrych
  - arXiv author search: https://arxiv.org/search/?query=Piotr%20Frydrych&searchtype=author
  - Applies to: the reviewed paper and `2606.05245-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
