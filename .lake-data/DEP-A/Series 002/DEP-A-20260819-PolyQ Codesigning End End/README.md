# DEP-A-20260819-PolyQ Codesigning End End

#artificial-intelligence #arXiv #paper-review #model-compression #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.14618v1, *PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.14618-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.14618-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We present PolyQ , a CPU-oriented framework for deployable activation-aware channel-wise mixed-precision inference. We propose an intra-layer quantization method over a CPU-aligned {2,3,4,8,16}-bit palette, guided by activation-aware saliency, enabling saliency-matched bit allocation and fine-grained fractional-bit budget adaptation across diverse deployment targets. We show that PolyQ improves perplexity by 2.4–32.1% over prior methods at a 3b target, realizes fractional budgets within 0.045b of target after SIMD-optimized quanta matching, reduces activation reorder traffic by up to 70.8% over prior layout policies, and keeps end-to-end latency within 5.8% of an optimized LUT backend with less than 2% energy/token overhead.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.14618v1
  - Applies to: `2607.14618-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.14618v1
  - Applies to: `2607.14618-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.14618v1
  - Applies to: `2607.14618-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.14618
  - Applies to: `2607.14618-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Hyunwoo Oh
  - arXiv author search: https://arxiv.org/search/?query=Hyunwoo%20Oh&searchtype=author
  - Applies to: the reviewed paper and `2607.14618-whitepaper-review.md`.
- Author: Suyeon Jang
  - arXiv author search: https://arxiv.org/search/?query=Suyeon%20Jang&searchtype=author
  - Applies to: the reviewed paper and `2607.14618-whitepaper-review.md`.
- Author: Hanning Chen
  - arXiv author search: https://arxiv.org/search/?query=Hanning%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2607.14618-whitepaper-review.md`.
- Author: KyungIn Nam
  - arXiv author search: https://arxiv.org/search/?query=KyungIn%20Nam&searchtype=author
  - Applies to: the reviewed paper and `2607.14618-whitepaper-review.md`.
- Author: Sanggeon Yun
  - arXiv author search: https://arxiv.org/search/?query=Sanggeon%20Yun&searchtype=author
  - Applies to: the reviewed paper and `2607.14618-whitepaper-review.md`.
- Author: Ryozo Masukawa
  - arXiv author search: https://arxiv.org/search/?query=Ryozo%20Masukawa&searchtype=author
  - Applies to: the reviewed paper and `2607.14618-whitepaper-review.md`.
- Author: Mohsen Imani
  - arXiv author search: https://arxiv.org/search/?query=Mohsen%20Imani&searchtype=author
  - Applies to: the reviewed paper and `2607.14618-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
