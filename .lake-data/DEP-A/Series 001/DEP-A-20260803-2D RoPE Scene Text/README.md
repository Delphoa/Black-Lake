# DEP-A-20260803-2D RoPE Scene Text

#artificial-intelligence #scene-text-recognition #rotary-embeddings #transformers #document-analysis #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.13458v1, *2D Rotary Position Embedding for Scene Text Recognition with Transformers*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.13458-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.13458-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Deep learning has driven STR forward, with architectures evolving from CNN-RNN hybrid models [ 38 , 39 ] to attention-based encoder-decoder frameworks [ 9 , 7 ] and, more recently, Transformer-based approaches [ 3 , 15 , 47 ] ; see [ 1 ] for a recent survey of Transformers in text recognition. Our main contributions are: We adapt axial 2D Rotary Position Embedding to the anisotropic, encoder-decoder setting of scene text recognition, via a text-aspect-ratio-matched row/column dimension split and an extension of the rotary coupling into decoder cross-attention—both absent from prior vision-only 2D-RoPE formulations and both validated as the best-performing choice in our ablations. Describe the issue below: Abstract 1 Introduction 2.1 Scene Text Recognition 2.2 Positional Encoding in Transformers 3.1 Preliminary: Rotary Position Embedding 3.2 2D Rotary Position Embedding 3.3.1 Overall Architecture 3.3.2 2D-RoPE in Self-Attention 3.3.3 Frequency Base Selection 3.3.4 Cross-Attention Positional Encoding 4.1 Datasets 4.2 Implementation Details 4.3 Comparison with State-of-the-Art 4.4.1 Effect of Positional Encoding Type 4.4.2 2D-RoPE Design Choices 4.5 Qualitative Analysis 5 Discussion 6 Conclusion References [1] \fnm Zobeir \sur Raisi.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat 2D Rotary Position Embedding for Scene Text Recognition with Transformers as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.13458v1
  - Applies to: `2607.13458-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.13458v1
  - Applies to: `2607.13458-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.13458v1
  - Applies to: `2607.13458-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.13458
  - Applies to: `2607.13458-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Zobeir Raisi
  - arXiv author search: https://arxiv.org/search/?query=Zobeir%20Raisi&searchtype=author
  - Applies to: the reviewed paper and `2607.13458-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
