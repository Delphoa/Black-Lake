# DEP-A-20260811-MemMachine Ground Truth

#artificial-intelligence #agent-memory #personalization #episodic-memory #retrieval #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2604.04853v1, *MemMachine: A Ground-Truth-Preserving Memory System for Personalized AI Agents*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2604.04853-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2604.04853-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: MemMachine achieves 0.9169 on LoCoMo with gpt-4.1-mini, among the strongest published results for open memory frameworks and above reported Mem0, Zep, Memobase, LangMem, and OpenAI baseline scores. Retrieval-based systems (MemMachine, Mem0, Zep) search for relevant memories each turn, which enables access to arbitrarily large memory stores but invalidates prompt caches and adds latency. We present MemMachine, an open-source memory system that combines short-term memory, long-term episodic memory, and profile memory in a ground-truth-preserving architecture that stores raw conversational episodes and minimizes routine LLM-based extraction.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Operate ground-truth-preserving agent memory as a consented evidence store: retain full episodic provenance, retrieval expansions, query-routing decisions, profile mutations, deletions, and user corrections, while keeping a no-memory path for sensitive, stale, or weakly supported personalization.

## Associated DEP Records

- [DEP-A-20260717-Agent Memory Systems](../DEP-A-20260717-Agent%20Memory%20Systems/README.md) - direct agent-memory lifecycle and systems context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260719-Agent Memory Benchmark](../DEP-A-20260719-Agent%20Memory%20Benchmark/README.md) - direct memory-agent benchmarking and evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2604.04853v1
  - Applies to: `2604.04853-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2604.04853v1
  - Applies to: `2604.04853-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2604.04853v1
  - Applies to: `2604.04853-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2604.04853
  - Applies to: `2604.04853-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/MemMachine/MemMachine
  - Applies to: reproducibility context in `2604.04853-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Shu Wang
  - arXiv author search: https://arxiv.org/search/?query=Shu%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2604.04853-whitepaper-review.md`.
- Author: Edwin Yu
  - arXiv author search: https://arxiv.org/search/?query=Edwin%20Yu&searchtype=author
  - Applies to: the reviewed paper and `2604.04853-whitepaper-review.md`.
- Author: Oscar Love
  - arXiv author search: https://arxiv.org/search/?query=Oscar%20Love&searchtype=author
  - Applies to: the reviewed paper and `2604.04853-whitepaper-review.md`.
- Author: Tom Zhang
  - arXiv author search: https://arxiv.org/search/?query=Tom%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2604.04853-whitepaper-review.md`.
- Author: Tom Wong
  - arXiv author search: https://arxiv.org/search/?query=Tom%20Wong&searchtype=author
  - Applies to: the reviewed paper and `2604.04853-whitepaper-review.md`.
- Author: Steve Scargall
  - arXiv author search: https://arxiv.org/search/?query=Steve%20Scargall&searchtype=author
  - Applies to: the reviewed paper and `2604.04853-whitepaper-review.md`.
- Author: Charles Fan
  - arXiv author search: https://arxiv.org/search/?query=Charles%20Fan&searchtype=author
  - Applies to: the reviewed paper and `2604.04853-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
