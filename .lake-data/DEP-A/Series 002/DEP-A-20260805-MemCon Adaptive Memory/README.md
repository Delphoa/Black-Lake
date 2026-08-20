# DEP-A-20260805-MemCon Adaptive Memory

#artificial-intelligence #agent-memory #online-learning #adaptive-control #contextual-bandits #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.13591v1, *Memory as a Controlled Process: Learned Adaptive Memory Management for LLM Agents*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.13591-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.13591-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We use three architecturally distinct agent runners, each sharing identical task loaders, tools, and evaluation protocol so that the only varying factor across baselines is the memory system: Lobster , a single-agent minimalist runner that talks to the OpenAI-compatible chat API directly; LangGraph [ 3 ] , a graph-structured multi-agent workflow built on LangChain; and Microsoft Agent-Framework , a pipeline-based multi-agent system. We evaluate MemCon across 6 benchmarks covering both interactive decision-making (ALFWorld [ 42 ] , PDDL planning, ScienceWorld [ 49 ] ) and knowledge / web / tool-use QA (TriviaQA [ 17 ] , WebWalkerQA [ 54 ] , GAIA [ 32 ] ); 3 agent frameworks (Lobster, LangGraph [ 3 ] , Microsoft Agent-Framework); 3 LLM backbones (GPT-4.1-mini, Claude Sonnet-4, DeepSeek-V3.2); and compare against 9 strong memory baselines spanning vector retrieval (MetaGPT [ 15 ] , MemoryBank [ 64 ] ), skill libraries (Voyager [ 47 ] ), trajectory summarization (ChatDev [ 37 ] ), generative re-ranking (Generative [ 36 ] , ExperienceBank), insight-based learning (OAgents [ 38 ] ), graph-based hierarchical memory (G-Memory [ 60 ] ), and latent-token memory (LatentMem [ 34 ] ). We formalize agent memory management as a Memory MDP and.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Memory as a Controlled Process: Learned Adaptive Memory Management for LLM Agents as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260717-Agent Memory Systems](../../Series%20001/DEP-A-20260717-Agent%20Memory%20Systems/README.md) - direct agent-memory systems and lifecycle context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260719-Agent Memory Benchmark](../../Series%20001/DEP-A-20260719-Agent%20Memory%20Benchmark/README.md) - direct agent-memory benchmark and evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.13591v1
  - Applies to: `2607.13591-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.13591v1
  - Applies to: `2607.13591-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.13591v1
  - Applies to: `2607.13591-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.13591
  - Applies to: `2607.13591-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/ericjiang18/MemCon/
  - Applies to: reproducibility context in `2607.13591-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Eric Hanchen Jiang
  - arXiv author search: https://arxiv.org/search/?query=Eric%20Hanchen%20Jiang&searchtype=author
  - Applies to: the reviewed paper and `2607.13591-whitepaper-review.md`.
- Author: Zhi Zhang
  - arXiv author search: https://arxiv.org/search/?query=Zhi%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.13591-whitepaper-review.md`.
- Author: Yuchen Wu
  - arXiv author search: https://arxiv.org/search/?query=Yuchen%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2607.13591-whitepaper-review.md`.
- Author: Levina Li
  - arXiv author search: https://arxiv.org/search/?query=Levina%20Li&searchtype=author
  - Applies to: the reviewed paper and `2607.13591-whitepaper-review.md`.
- Author: Dong Liu
  - arXiv author search: https://arxiv.org/search/?query=Dong%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.13591-whitepaper-review.md`.
- Author: Xiao Liang
  - arXiv author search: https://arxiv.org/search/?query=Xiao%20Liang&searchtype=author
  - Applies to: the reviewed paper and `2607.13591-whitepaper-review.md`.
- Author: Rui Sun
  - arXiv author search: https://arxiv.org/search/?query=Rui%20Sun&searchtype=author
  - Applies to: the reviewed paper and `2607.13591-whitepaper-review.md`.
- Author: Yubei Li
  - arXiv author search: https://arxiv.org/search/?query=Yubei%20Li&searchtype=author
  - Applies to: the reviewed paper and `2607.13591-whitepaper-review.md`.
- Author: Edward Sun
  - arXiv author search: https://arxiv.org/search/?query=Edward%20Sun&searchtype=author
  - Applies to: the reviewed paper and `2607.13591-whitepaper-review.md`.
- Author: Haozheng Luo
  - arXiv author search: https://arxiv.org/search/?query=Haozheng%20Luo&searchtype=author
  - Applies to: the reviewed paper and `2607.13591-whitepaper-review.md`.
- Author: Zhaolu Kang
  - arXiv author search: https://arxiv.org/search/?query=Zhaolu%20Kang&searchtype=author
  - Applies to: the reviewed paper and `2607.13591-whitepaper-review.md`.
- Author: Aylin Caliskan
  - arXiv author search: https://arxiv.org/search/?query=Aylin%20Caliskan&searchtype=author
  - Applies to: the reviewed paper and `2607.13591-whitepaper-review.md`.
- Author: Kai-Wei Chang
  - arXiv author search: https://arxiv.org/search/?query=Kai-Wei%20Chang&searchtype=author
  - Applies to: the reviewed paper and `2607.13591-whitepaper-review.md`.
- Author: Ying Nian Wu
  - arXiv author search: https://arxiv.org/search/?query=Ying%20Nian%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2607.13591-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
