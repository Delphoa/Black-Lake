# DEP-E-20260721-Stealth Memory Injection

#agent-security #persistent-memory #memory-poisoning #email-agents #provenance #evaluation #defensive-research #reproducibility

Public deposition context: the user explicitly selected arXiv:2607.05189v1 for a complete DEP-E review. A previously downloaded, integrity-checked paper bundle was reused rather than downloaded again. The complete PDF, full-paper HTML, abstract record, and source archive remain outside this repository.

## Contents

- `README.md` - deposition context, inventory, source boundary, associations, and attribution.
- `stealth_memory_trust_manuscript.md` - source-grounded manuscript covering the threat model, WhisperBench, MemGhost, experimental evidence, limitations, defensive implications, and reproducibility gaps.

The corresponding public processing records are:

- `.logs/20260721-Arxiv-Stealth-Memory-Injection-LOG.md`
- `.reports/BL-Arxiv-Stealth-Memory-Injection-20260721/Report-Mark.md`

No PDF, HTML, TeX source, extracted text, prompt payload, credential, private trace, or local machine path is included.

## Summary of Items

### `README.md`

Defines the DEP-E boundary and provides canonical public provenance for the reviewed arXiv version.

### `stealth_memory_trust_manuscript.md`

Reconstructs the paper's one-shot, cross-session memory-injection threat; the 108-case WhisperBench evaluation; the environment and objective proxies used by MemGhost; supervised and group-relative policy training; reported transfer and defense-evasion results; metric and baseline qualifications; and a defensive architecture based on provenance, write authority, quarantine, retrieval policy, and action authorization.

## Insights and Relevance

The paper's durable contribution is to separate four events that agent systems often collapse: accepting untrusted content, writing a memory, exposing evidence to the user, and allowing the memory to influence a later action. Its reported results show that a system may appear normal at ingestion while retaining attacker-controlled state for another session. The operational implication for Black Lake is that memory must be treated as an authorization-bearing security boundary, not merely a retrieval-quality feature.

The review does not reproduce attack prompts or give instructions for constructing covert email payloads. It focuses on measurable state transitions, evaluation validity, defensive controls, and incident evidence.

## Associated DEP Records

- [DEP-A-20260717-FARMA Reasoning Poison](../../DEP-A/DEP-A-20260717-FARMA%20Reasoning%20Poison/README.md) - forged-reasoning attacks and provenance-aware memory gating.
- [DEP-E-20260718-Memory Defense Layers](../DEP-E-20260718-Memory%20Defense%20Layers/README.md) - architecture-layer defenses, memory authority, and evaluation validity.
- [DEP-E-20260711-Agent Memory Forensics](../DEP-E-20260711-Agent%20Memory%20Forensics/README.md) - trace evidence and forensic analysis of poisoned persistent state.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.05189v1
  - Applies to: `stealth_memory_trust_manuscript.md` and this README.
  - Notes: stable metadata for the reviewed v1 paper.
- Canonical PDF: https://arxiv.org/pdf/2607.05189v1
  - Applies to: `stealth_memory_trust_manuscript.md`.
  - Notes: complete 25-page PDF verified locally and withheld from the repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.05189v1
  - Applies to: `stealth_memory_trust_manuscript.md`.
  - Notes: complete article rendering inspected and withheld from the repository.
- DOI: https://doi.org/10.48550/arXiv.2607.05189
  - Applies to: all generated artifacts in this DEP-E package.
  - Notes: canonical arXiv DOI resolver.
- Authors: Yechao Zhang; Shiqian Zhao; Jiawen Zhang; Jie Zhang; Gelei Deng; Xiaogeng Liu; Chaowei Xiao; Tianwei Zhang.
  - Applies to: the reviewed paper and all generated summaries.
  - Notes: author order follows the canonical arXiv v1 record.
- Related DEP records: the three repository-relative links under `Associated DEP Records`.
  - Applies to: synthesis and implementation context only.
  - Notes: related records are not substitutes for the primary paper.
- Source boundary: all source documents, extraction caches, validators, manifests, and machine context remained local and were not uploaded.
