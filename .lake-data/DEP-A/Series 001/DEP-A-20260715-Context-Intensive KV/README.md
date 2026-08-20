# DEP-A-20260715-Context-Intensive KV

#kv-cache #offloading #long-context #quantization #inference-systems #gpu-memory #benchmarking #whitepaper-review

This archival DEP-A preserves a public-safe, whitepaper-grade review of arXiv:2604.08426v4, “KV Cache Offloading for Context-Intensive Tasks.” The complete PDF and full-paper HTML were verified from the local research archive. Those source documents, the private cache ledger, coverage matrix, and validator report remain local and are not deposited here.

## Contents

- `README.md` — classification, inventory, provenance, relationships, and attribution for this DEP-A.
- `2604.08426-whitepaper-review.md` — validated technical reconstruction, quantitative audit, external primary-source vetting, independent re-conceptualization, coverage ledger, and replication agenda.

## Summary of Items

### `2604.08426-whitepaper-review.md`

The review reconstructs context intensity, Text2JSON, ShadowKV’s low-rank and grouped-landmark failure modes, YAKV’s direct quantized per-token selection, accuracy-versus-transfer results, throughput mechanism, hardware disclosures, and every appendix experiment. It identifies an H100/H200 label inconsistency that should be clarified in reproduction.

## Insights and Relevance

The durable lesson is that offloading is repeated approximate retrieval and must be evaluated by required evidence accesses, not context length alone. The review recommends quality-versus-transfer service curves, field-level error decomposition, exact hardware provenance, adaptive budgets, shadow full-attention tests, and high-fidelity fallbacks.

## Associated DEP Records

The [SpectrumKV Transfer DEP](../DEP-A-20260714-SpectrumKV%20Transfer/README.md) is directly corresponding conceptual work on KV transfer and precision. It is not the same paper: SpectrumKV studies mixed-precision transfer for disaggregated serving, while this paper studies host-memory offloading under context-intensive workloads. No same-paper DEP was found.

## Attribution Block

- Source URL: https://arxiv.org/abs/2604.08426v4
  - Applies to: `2604.08426-whitepaper-review.md`
  - Notes: Canonical arXiv v4 record for the reviewed paper; complete author list appears below.
- Source URL: https://arxiv.org/pdf/2604.08426v4
  - Applies to: `2604.08426-whitepaper-review.md`
  - Notes: Canonical public PDF locator. The complete source was verified locally and withheld from the repository.
- Source URL: https://arxiv.org/html/2604.08426v4
  - Applies to: `2604.08426-whitepaper-review.md`
  - Notes: Canonical public full-paper HTML locator. The complete source was verified locally and withheld from the repository.
- Source URL: https://doi.org/10.48550/arXiv.2604.08426
  - Applies to: `2604.08426-whitepaper-review.md`
  - Notes: Canonical arXiv DOI for the reviewed paper.
- Source URL: https://github.com/yandex-research/context-intensive-kv-offloading
  - Applies to: `2604.08426-whitepaper-review.md`
  - Notes: Official work-in-progress implementation and Text2JSON repository used for artifact vetting; no performance reproduction is claimed.
- Author: Andrey Bocharnikov
  - arXiv author search: https://arxiv.org/search/?query=Andrey%20Bocharnikov&searchtype=author
  - Applies to: the reviewed paper and `2604.08426-whitepaper-review.md`.
- Author: Ivan Ermakov
  - arXiv author search: https://arxiv.org/search/?query=Ivan%20Ermakov&searchtype=author
  - Applies to: the reviewed paper and `2604.08426-whitepaper-review.md`.
- Author: Denis Kuznedelev
  - arXiv author search: https://arxiv.org/search/?query=Denis%20Kuznedelev&searchtype=author
  - Applies to: the reviewed paper and `2604.08426-whitepaper-review.md`.
- Author: Vyacheslav Zhdanovskiy
  - arXiv author search: https://arxiv.org/search/?query=Vyacheslav%20Zhdanovskiy&searchtype=author
  - Applies to: the reviewed paper and `2604.08426-whitepaper-review.md`.
- Author: Yegor Yershov
  - arXiv author search: https://arxiv.org/search/?query=Yegor%20Yershov&searchtype=author
  - Applies to: the reviewed paper and `2604.08426-whitepaper-review.md`.
