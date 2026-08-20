# DEP-A-20260816-OTRO Tokenizer Privacy

#artificial-intelligence #tokenization #ORAM #confidential-computing #side-channels #LLM-serving

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.17358v2, *OTRO: Oblivious Tokenization Path with Square-Root ORAM*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.17358-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.17358-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Describe the issue below: Abstract 1.1 OTRO : Efficient and Oblivious Tokenization Path 2.1 Trusted Execution Environment 2.2 LLM Tokenization 2.3 Oblivious Random Access Memory 3.1 Threat Model 3.2 Case Study: Leakage in BPE Tokenizer 4 Prompt Reconstruction on Intel TDX 5.1 OTRO Overview 5.2 SqrtORAM Pool Access 5.3 Chunked Tokenization 5.4 Detokenization 6 Security Analysis 7.1 Experimental Setup and Implementation 7.2 Offline Tuning for CPU-GPU Overlap 7.3 Time-To-First-Token Latency 7.4 System Level Cost 7.5 Residual Leakage Quantification 8 Related Work 9 Conclusion References A Security Analysis In this work, we propose OTRO , an efficient and secure Oblivious Tokenization Path tailored to confidential LLM serving. Our evaluation shows that OTRO only limits TTFT overhead to at most 4.5% and adds less than 0.5 GB of memory, significantly outperforming PathORAM and naive SqrtORAM baselines. In this section, we introduce OTRO , an efficient and oblivious tokenization pathway built on top of SqrtORAM and tailored to BPE tokenizers in LLM inference serving.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat OTRO: Oblivious Tokenization Path with Square-Root ORAM as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260726-Pi RAG Oblivious](../../Series%20001/DEP-A-20260726-Pi%20RAG%20Oblivious/README.md) - direct access-pattern-oblivious retrieval and privacy context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.17358v2
  - Applies to: `2606.17358-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.17358v2
  - Applies to: `2606.17358-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.17358v2
  - Applies to: `2606.17358-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.17358
  - Applies to: `2606.17358-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Jonghyun Lee
  - arXiv author search: https://arxiv.org/search/?query=Jonghyun%20Lee&searchtype=author
  - Applies to: the reviewed paper and `2606.17358-whitepaper-review.md`.
- Author: Yongqin Wang
  - arXiv author search: https://arxiv.org/search/?query=Yongqin%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.17358-whitepaper-review.md`.
- Author: Rachit Rajat
  - arXiv author search: https://arxiv.org/search/?query=Rachit%20Rajat&searchtype=author
  - Applies to: the reviewed paper and `2606.17358-whitepaper-review.md`.
- Author: Daniel Wong
  - arXiv author search: https://arxiv.org/search/?query=Daniel%20Wong&searchtype=author
  - Applies to: the reviewed paper and `2606.17358-whitepaper-review.md`.
- Author: Mengyuan Li
  - arXiv author search: https://arxiv.org/search/?query=Mengyuan%20Li&searchtype=author
  - Applies to: the reviewed paper and `2606.17358-whitepaper-review.md`.
- Author: Murali Annavaram
  - arXiv author search: https://arxiv.org/search/?query=Murali%20Annavaram&searchtype=author
  - Applies to: the reviewed paper and `2606.17358-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
