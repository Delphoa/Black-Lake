# DEP-A-20260803-Revelio Memory Safety

#artificial-intelligence #software-security #memory-safety #coding-agents #vulnerability-detection #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.22263v1, *Revelio: Cost-Efficient Agentic Memory Safety Vulnerability Detection For Repository-Scale Codebases*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.22263-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.22263-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Figure 1: Overall workflow of Revelio for end-to-end agentic memory safety vulnerability detection. Based on this insight, we design Revelio , an end-to-end agentic framework for detecting memory safety vulnerabilities in repository-scale C/C++ codebases. This paper presents Revelio , a cost-efficient end-to-end agentic framework for memory-safety vulnerability discovery.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat LLM-generated vulnerability hypotheses as untrusted proposals that become findings only after an executable proof and sanitizer confirmation; retain code revision, prompt trace, proof input, crash, triage, and disclosure state, and never equate benchmark yield with complete repository safety.

## Associated DEP Records

- [DEP-A-20260802-Coding Agent Context](../DEP-A-20260802-Coding%20Agent%20Context/README.md) - direct repository-scale coding-agent and verification context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.22263v1
  - Applies to: `2606.22263-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.22263v1
  - Applies to: `2606.22263-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.22263v1
  - Applies to: `2606.22263-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.22263
  - Applies to: `2606.22263-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/trailofbits/buttercup
  - Applies to: reproducibility context in `2606.22263-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Yiwei Hou
  - arXiv author search: https://arxiv.org/search/?query=Yiwei%20Hou&searchtype=author
  - Applies to: the reviewed paper and `2606.22263-whitepaper-review.md`.
- Author: Hao Wang
  - arXiv author search: https://arxiv.org/search/?query=Hao%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.22263-whitepaper-review.md`.
- Author: Muxi Lyu
  - arXiv author search: https://arxiv.org/search/?query=Muxi%20Lyu&searchtype=author
  - Applies to: the reviewed paper and `2606.22263-whitepaper-review.md`.
- Author: Marius Momeu
  - arXiv author search: https://arxiv.org/search/?query=Marius%20Momeu&searchtype=author
  - Applies to: the reviewed paper and `2606.22263-whitepaper-review.md`.
- Author: Eric Nguyen
  - arXiv author search: https://arxiv.org/search/?query=Eric%20Nguyen&searchtype=author
  - Applies to: the reviewed paper and `2606.22263-whitepaper-review.md`.
- Author: Taige Yang
  - arXiv author search: https://arxiv.org/search/?query=Taige%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2606.22263-whitepaper-review.md`.
- Author: Koushik Sen
  - arXiv author search: https://arxiv.org/search/?query=Koushik%20Sen&searchtype=author
  - Applies to: the reviewed paper and `2606.22263-whitepaper-review.md`.
- Author: Dawn Song
  - arXiv author search: https://arxiv.org/search/?query=Dawn%20Song&searchtype=author
  - Applies to: the reviewed paper and `2606.22263-whitepaper-review.md`.
- Author: David Wagner
  - arXiv author search: https://arxiv.org/search/?query=David%20Wagner&searchtype=author
  - Applies to: the reviewed paper and `2606.22263-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
