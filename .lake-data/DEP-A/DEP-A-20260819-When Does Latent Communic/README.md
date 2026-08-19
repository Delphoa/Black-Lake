# DEP-A-20260819-When Does Latent Communic

#artificial-intelligence #arXiv #paper-review #KV-cache #agents #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.04893v1, *When Does Latent Communication Pay? A Causal Audit of Relayed KV Caches in Multi-Agent LLMs*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.04893-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.04893-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The relayed object is the KV cache, the per-layer attention key–value tensors a transformer accumulates as it processes a sequence, and recent systems attribute their reported gains to this “latent communication” ( Zou et al. The audit bounds the example-pairing value of delivered relays; it issues no latent-versus-text verdict, and the calibrated cells rule out the reading that relayed caches carry nothing. Within a natural cell the 500 examples are a deterministically selected, frozen subset, identical across seeds and arms; the derangement is likewise frozen — a within-batch cyclic shift of complete cache rows, the same assignment in every seed and arm — and the sender-side pipeline (prompt prefill and latent-state recycling) involves no token sampling, so the relayed caches and the donor assignment are common to all seeds.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat When Does Latent Communication Pay? A Causal Audit of Relayed KV Caches in Multi-Agent LLMs as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.04893v1
  - Applies to: `2608.04893-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.04893v1
  - Applies to: `2608.04893-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.04893v1
  - Applies to: `2608.04893-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2608.04893
  - Applies to: `2608.04893-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Jiaming Cheng
  - arXiv author search: https://arxiv.org/search/?query=Jiaming%20Cheng&searchtype=author
  - Applies to: the reviewed paper and `2608.04893-whitepaper-review.md`.
- Author: Subhransu Das
  - arXiv author search: https://arxiv.org/search/?query=Subhransu%20Das&searchtype=author
  - Applies to: the reviewed paper and `2608.04893-whitepaper-review.md`.
- Author: Rajiv Ramnath
  - arXiv author search: https://arxiv.org/search/?query=Rajiv%20Ramnath&searchtype=author
  - Applies to: the reviewed paper and `2608.04893-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
