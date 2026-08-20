# DEP-A-20260715-Prompt Compression Wild

#prompt-compression #llm-inference #latency #gpu-memory #long-context #information-retrieval #benchmarking #whitepaper-review

This archival DEP-A preserves a public-safe, whitepaper-grade review of arXiv:2604.02985v1, “Prompt Compression in the Wild: Measuring Latency, Rate Adherence, and Quality for Faster LLM Inference.” The complete PDF and full-paper HTML were verified from a local research archive. Those source documents, private cache ledgers, coverage matrices, and validator reports remain local and are not deposited here.

## Contents

- `README.md` — classification, inventory, provenance, relationships, and attribution for this DEP-A.
- `2604.02985-whitepaper-review.md` — validated technical reconstruction, quantitative audit, external primary-source vetting, independent re-conceptualization, coverage ledger, and replication agenda.

## Summary of Items

### `2604.02985-whitepaper-review.md`

The review reconstructs more than 30,000 compression/inference experiments across compressor variants, models, serving stacks, hardware, lengths, ratios, and task families. It separates compressor overhead from prefill/decoding, audits quality failures and target-rate adherence, and records the profiler link as unresolved rather than inventing an artifact URL.

## Insights and Relevance

The durable result is a break-even methodology: compression should be an abstaining workload-specific policy, not a default token-reduction step. Optimized serving, commercial APIs, structured tasks, short prompts, and long outputs can erase or reverse nominal gains.

## Associated DEP Records

The [LCLM Context Compression DEP](../DEP-A-20260714-LCLM%20Context%20Compression/README.md) is directly relevant learned-compressor context. The [Hybrid Graph Compression DEP](../DEP-A-20260715-Hybrid%20Graph%20Compression/README.md) is a training-free extractive alternative. Neither is the same paper; together they provide comparison points for the systems break-even and quality-risk findings. No same-paper DEP was verified.

## Attribution Block

- Source URL: https://arxiv.org/abs/2604.02985v1
  - Applies to: `2604.02985-whitepaper-review.md`
  - Notes: Canonical arXiv v1 record and complete paper metadata.
- Source URL: https://arxiv.org/pdf/2604.02985v1
  - Applies to: `2604.02985-whitepaper-review.md`
  - Notes: Canonical public PDF locator; the source was verified locally and withheld from the repository.
- Source URL: https://arxiv.org/html/2604.02985v1
  - Applies to: `2604.02985-whitepaper-review.md`
  - Notes: Canonical public full-paper HTML locator; the source was verified locally and withheld from the repository.
- Source URL: https://doi.org/10.48550/arXiv.2604.02985
  - Applies to: `2604.02985-whitepaper-review.md`
  - Notes: Canonical arXiv DOI.
- Source URL: https://github.com/microsoft/LLMLingua
  - Applies to: `2604.02985-whitepaper-review.md`
  - Notes: Official implementation of the evaluated LLMLingua family; it is precursor software, not a verified repository for this paper's claimed profiler.
- Author: Cornelius Kummer
  - arXiv author search: https://arxiv.org/search/?query=Cornelius%20Kummer&searchtype=author
  - Applies to: the reviewed paper and `2604.02985-whitepaper-review.md`.
- Author: Lena Jurkschat
  - arXiv author search: https://arxiv.org/search/?query=Lena%20Jurkschat&searchtype=author
  - Applies to: the reviewed paper and `2604.02985-whitepaper-review.md`.
- Author: Michael Färber
  - arXiv author search: https://arxiv.org/search/?query=Michael%20F%C3%A4rber&searchtype=author
  - Applies to: the reviewed paper and `2604.02985-whitepaper-review.md`.
- Author: Sahar Vahdati
  - arXiv author search: https://arxiv.org/search/?query=Sahar%20Vahdati&searchtype=author
  - Applies to: the reviewed paper and `2604.02985-whitepaper-review.md`.
