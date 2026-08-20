# DEP-A-20260722-UltraQuant KV4

#artificial-intelligence #KV-cache #quantization #agent-serving #FP4 #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.20474v2, *UltraQuant: 4-bit KV Caching for Context-Heavy Agents*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.20474-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.20474-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: UltraQuant studies a 4-bit KV-cache path for multi-round agents. It begins from TurboQuant-style rotation and calibrated codebooks, then replaces lookup-table dequantization with FP4 micro-tensors, UE8M0 block scales, FP8 queries, and CDNA4 scaled-MFMA instructions so dequantization occurs inside matrix multiplication. Boundary layers retain BF16 KV state.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Deploy a pressure-aware KV codec that remains on FP8 or BF16 until measured residency predicts a benefit, then enables FP4 by layer with per-benchmark quality guards and reversible cache promotion when confidence drops.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.20474v2
  - Applies to: `2606.20474-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.20474v2
  - Applies to: `2606.20474-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.20474v2
  - Applies to: `2606.20474-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.20474
  - Applies to: `2606.20474-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Inesh Chakrabarti
  - arXiv author search: https://arxiv.org/search/?query=Inesh%20Chakrabarti&searchtype=author
  - Applies to: the reviewed paper and `2606.20474-whitepaper-review.md`.
- Author: David Limpus
  - arXiv author search: https://arxiv.org/search/?query=David%20Limpus&searchtype=author
  - Applies to: the reviewed paper and `2606.20474-whitepaper-review.md`.
- Author: Aditi Ghai Rana
  - arXiv author search: https://arxiv.org/search/?query=Aditi%20Ghai%20Rana&searchtype=author
  - Applies to: the reviewed paper and `2606.20474-whitepaper-review.md`.
- Author: Bowen Bao
  - arXiv author search: https://arxiv.org/search/?query=Bowen%20Bao&searchtype=author
  - Applies to: the reviewed paper and `2606.20474-whitepaper-review.md`.
- Author: Spandan Tiwari
  - arXiv author search: https://arxiv.org/search/?query=Spandan%20Tiwari&searchtype=author
  - Applies to: the reviewed paper and `2606.20474-whitepaper-review.md`.
- Author: Thiago Crepaldi
  - arXiv author search: https://arxiv.org/search/?query=Thiago%20Crepaldi&searchtype=author
  - Applies to: the reviewed paper and `2606.20474-whitepaper-review.md`.
- Author: Ashish Sirasao
  - arXiv author search: https://arxiv.org/search/?query=Ashish%20Sirasao&searchtype=author
  - Applies to: the reviewed paper and `2606.20474-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
