# DEP-A-20260819-Graph Native Bitemporal M

#artificial-intelligence #arXiv #paper-review #memory #agents #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.26520v1, *A Graph-Native Bitemporal Memory Store for Conversational AI Agents*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.26520-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.26520-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Describe the issue below: Abstract I Introduction II-A Agent Memory Paradigms II-B Vector Databases II-C Graph-Based Retrieval II-D Temporal Databases III-A Data Model III-B Bitemporal Model Current-state retrieval Historical retrieval IV-A Technology Stack IV-B Agent Tool-Use Loop IV-C Storing User Messages Only IV-D Automatic Edge Construction IV-E Legacy Data Migration V-A Benchmark and Protocol V-B Results V-C Single-Session User Statements V-D Single-Session Assistant and Preference Types V-E Temporal Reasoning and the Dilution Effect V-F Knowledge Update V-G Multi-Session VI-A Summary VI-B Future Directions References Prior work generally divides LLM agent memory into three categories: parametric memory stored in model weights, in-context memory maintained within the prompt window, and retrieval-augmented memory that pulls information from external storage [ 2 ] . This design works well for user-centered memory retrieval, but it also means the system cannot answer questions about what the assistant previously said, since those responses are not stored. In this project we implemented a conversational memory store on Neo4j that combines vector-based similarity search with a bitemporal data model and automatic graph linking.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat A Graph-Native Bitemporal Memory Store for Conversational AI Agents as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260717-Agent Memory Systems](../../Series%20001/DEP-A-20260717-Agent%20Memory%20Systems/README.md) - foundation for agent-memory architecture and evaluation. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.26520v1
  - Applies to: `2607.26520-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.26520v1
  - Applies to: `2607.26520-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.26520v1
  - Applies to: `2607.26520-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.26520
  - Applies to: `2607.26520-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Alp Niksarli
  - arXiv author search: https://arxiv.org/search/?query=Alp%20Niksarli&searchtype=author
  - Applies to: the reviewed paper and `2607.26520-whitepaper-review.md`.
- Author: Gopesh Baheti
  - arXiv author search: https://arxiv.org/search/?query=Gopesh%20Baheti&searchtype=author
  - Applies to: the reviewed paper and `2607.26520-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
