# DEP-A-20260812-Cache Aware Prompts

#artificial-intelligence #prompt-compression #prompt-caching #LLM-APIs #cost-modeling #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.15516v1, *Cache-Aware Prompt Compression:A Two-Tier Cost Model for LLM API Caching*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.15516-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.15516-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Don’t Break the Cache (Lumer et al., 2026 ) evaluates three caching strategies on the DeepResearch benchmark for long-horizon agentic tasks but does not propose a cost model. We show that under realistic, measured cache hit rates ρ ​ ( N , | P | ) \rho(N,|P|) , the literature’s implicit assumption ρ = 1.0 \rho=1.0 misstates the cost-quality landscape in three concrete ways: (1) Anthropic’s cache has a two-tier architecture with a sharp size threshold near 3,500 tokens, below which ρ < 1 \rho<1 ; (2) at high compression ratios ( r ≥ 6 r\geq 6 ), query-aware compression actually beats naïve cache-only — the inverse of conventional wisdom; (3) at all 16 (doc-size × \times ratio) configurations tested on LongBench-v2, a simple Cache-Aware Prompt Compression ( CAPC ) that combines query- agnostic compression with caching strictly dominates the literature’s baselines. Prior work touching CAPC ’s design space falls into five threads: empirical characterization of prompt caching, prompt compression methods, cost-aware model routing, agent and reasoning budget control, and the small but growing body of industry guidance on cache-aware prompt construction.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat cache-aware prompt compression as a two-tier economic controller: bind every cost estimate to the provider policy and observed hit process, preserve task quality beside billed tokens, and disable compression when cache thresholds or pricing drift beyond the calibrated model.

## Associated DEP Records

- [DEP-A-20260714-LCLM Context Compression](../../Series%20001/DEP-A-20260714-LCLM%20Context%20Compression/README.md) - direct learned context and semantic-compression context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260802-Coding Agent Context](../../Series%20001/DEP-A-20260802-Coding%20Agent%20Context/README.md) - direct repository-scale coding-agent and verification context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.15516v1
  - Applies to: `2607.15516-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.15516v1
  - Applies to: `2607.15516-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.15516v1
  - Applies to: `2607.15516-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.15516
  - Applies to: `2607.15516-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Yan Song
  - arXiv author search: https://arxiv.org/search/?query=Yan%20Song&searchtype=author
  - Applies to: the reviewed paper and `2607.15516-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
