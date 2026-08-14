# DEP-A-20260815-MoA Decode Kernel

#artificial-intelligence #attention #KV-cache #OpenACC #GPU-kernels #array-algebra

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.19456v1, *MoA-Structured Decode Attention DNF Derivation, KV-Cache Accumulation, GQA/MQA, and OpenACC Kernel*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.19456-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.19456-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Describe the issue below: Abstract 1.1 Background 1.2 Contributions 1.3 Notation and Terminology 2 Decode DNF 3 Python Implementation 4.1 ONF Stride Arithmetic 4.2 Dimension Lifting and Hardware-Coalescing Proof 4.3 OpenACC Annotations 4.4 Verification 5.1 Cache Append Expression 5.2 Combined Per-Step Cost 5.3 Python Implementation 5.4 Verification 6.1 Psi-Selection Expression 6.2 Dimension Lifting 6.3 Python Implementation 6.4 Verification and Traffic 7 Summary and Relationship to Training Kernel 8 Conclusion References This paper shows that the same DNF, with the query-row index i ′ i^{\prime} fixed to the current decode step, yields four inference artifacts. C/OpenACC GPU kernel (§ 4 ): ONF γ \gamma stride arithmetic gives coalesced memory access; the coalescing criterion is stated as a γ \gamma -difference condition. Standard PyTorch KV-cache uses torch.cat to grow the cache at each step, materialising K ⊤ K^{\top} at each attention call: Listing 4: Standard autoregressive decode ( pytorch_reference.py : std_kvcache_decode ).

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat MoA-Structured Decode Attention DNF Derivation, KV-Cache Accumulation, GQA/MQA, and OpenACC Kernel as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260812-KVBuffer Serving](../DEP-A-20260812-KVBuffer%20Serving/README.md) - direct decode-time KV movement and serving context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.19456v1
  - Applies to: `2607.19456-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.19456v1
  - Applies to: `2607.19456-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.19456v1
  - Applies to: `2607.19456-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.19456
  - Applies to: `2607.19456-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Lenore Mulin
  - arXiv author search: https://arxiv.org/search/?query=Lenore%20Mulin&searchtype=author
  - Applies to: the reviewed paper and `2607.19456-whitepaper-review.md`.
- Author: Gaetan Hains
  - arXiv author search: https://arxiv.org/search/?query=Gaetan%20Hains&searchtype=author
  - Applies to: the reviewed paper and `2607.19456-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
