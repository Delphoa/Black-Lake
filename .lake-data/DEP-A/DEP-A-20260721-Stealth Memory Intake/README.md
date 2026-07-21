# DEP-A-20260721-Stealth Memory Intake

#agent-security #persistent-memory #memory-poisoning #email-agents #provenance #authorization #archival-intake #whitepaper-review

Public deposition date: 2026-07-21. This DEP-A is a new, public-safe archival intake derived by reviewing `.lake-data/DEP-E/DEP-E-20260721-Stealth Memory Injection` at source commit `b7d91fc501abb299db8aa54405a8bd893c667ad9`. The paired task indicator is `BL-DEPPAIR-20260721-3B5798D0`.

## Contents

- `README.md`
  - Classification, inventory, review boundary, one-way provenance, associations, and attribution.
- `2607.05189-whitepaper-review.md`
  - Whitepaper-grade full-paper review covering source integrity, technical reconstruction, WhisperBench, MemGhost, quantitative results, claim vetting, external context, defensive re-conceptualization, limitations, hypotheses, governance, replication, and complete table/figure coverage.

## Summary of Items

The review treats the complete, pinned DEP-E record and the version-matched arXiv v1 paper as its evidence objects. It separates paper-reported evidence, directly inspected source facts, reviewer inference, and proposed defensive mechanisms. It does not claim independent reproduction.

The durable finding is that persistent-agent memory is an authorization boundary. A record derived from untrusted correspondence should not acquire future action authority merely because a language model extracted or summarized it. Defensible systems need provenance-bearing writes, quarantine, user-visible memory diffs, independent approval for sensitive changes, action-time evidence checks, and complete revocation lineage.

## Insights and Relevance

This package preserves the paper's strongest controlled results together with their denominators, runtime and endpoint boundaries, baseline asymmetries, reproducibility gaps, and editorial inconsistencies. It intentionally excludes concrete malicious messages and payload-construction instructions.

Passing the review methodology supports auditability, observability, and traceable lineage. It does not certify security, privacy, correctness, production readiness, or regulatory compliance.

## Provenance Pair

- Paired task indicator: `BL-DEPPAIR-20260721-3B5798D0`
- Direction: `DEP-E -> DEP-A`
- Source DEP-E: `.lake-data/DEP-E/DEP-E-20260721-Stealth Memory Injection`
- Source commit: `b7d91fc501abb299db8aa54405a8bd893c667ad9`
- Source action: review-only
- Source DEP modified: no
- Files moved: no
- Existing files copied into DEP-A: no
- New derived data generated: yes
- DEP-A intake status: complete only after validation and repository submission
- DEP-A deposition status: complete only after validation and repository submission
- This one-way pair does not reclassify, transfer, supersede, or mutate the DEP-E.

## Associated DEP Records

- [DEP-A-20260717-FARMA Reasoning Poison](../DEP-A-20260717-FARMA%20Reasoning%20Poison/README.md) - related forged-reasoning and memory-provenance review.
- [DEP-E-20260718-Memory Defense Layers](../../DEP-E/DEP-E-20260718-Memory%20Defense%20Layers/README.md) - related architecture-layer defense analysis.
- [DEP-E-20260711-Agent Memory Forensics](../../DEP-E/DEP-E-20260711-Agent%20Memory%20Forensics/README.md) - related persistent-memory forensic analysis.

## Attribution Block

- Source DEP-E repository URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260721-Stealth%20Memory%20Injection
  - Item: complete source record `.lake-data/DEP-E/DEP-E-20260721-Stealth Memory Injection` at `b7d91fc501abb299db8aa54405a8bd893c667ad9`.
  - Notes: reviewed in place; no source DEP file was moved, copied, renamed, deleted, reclassified, or modified by this DEP-A run.
- Canonical arXiv record: https://arxiv.org/abs/2607.05189v1
  - Item: title, authors, submitted date, subjects, abstract, and version identity.
  - Notes: primary source; no source document was uploaded.
- Canonical PDF: https://arxiv.org/pdf/2607.05189v1
  - Item: complete 25-page paper used for the full-paper review.
  - Notes: verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.05189v1
  - Item: structured full text, equations, tables, figures, appendices, and references.
  - Notes: verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.05189
  - Item: canonical persistent identifier.
  - Notes: applies to the paper and generated review.
- Author: Yechao Zhang
  - arXiv author search: https://arxiv.org/search/?query=Yechao%20Zhang&searchtype=author
  - Applies to: reviewed paper and generated review.
- Author: Shiqian Zhao
  - arXiv author search: https://arxiv.org/search/?query=Shiqian%20Zhao&searchtype=author
  - Applies to: reviewed paper and generated review.
- Author: Jiawen Zhang
  - arXiv author search: https://arxiv.org/search/?query=Jiawen%20Zhang&searchtype=author
  - Applies to: reviewed paper and generated review.
- Author: Jie Zhang
  - arXiv author search: https://arxiv.org/search/?query=Jie%20Zhang&searchtype=author
  - Applies to: reviewed paper and generated review.
- Author: Gelei Deng
  - arXiv author search: https://arxiv.org/search/?query=Gelei%20Deng&searchtype=author
  - Applies to: reviewed paper and generated review.
- Author: Xiaogeng Liu
  - arXiv author search: https://arxiv.org/search/?query=Xiaogeng%20Liu&searchtype=author
  - Applies to: reviewed paper and generated review.
- Author: Chaowei Xiao
  - arXiv author search: https://arxiv.org/search/?query=Chaowei%20Xiao&searchtype=author
  - Applies to: reviewed paper and generated review.
- Author: Tianwei Zhang
  - arXiv author search: https://arxiv.org/search/?query=Tianwei%20Zhang&searchtype=author
  - Applies to: reviewed paper and generated review.
- Generated review: `2607.05189-whitepaper-review.md`
  - Item: new public-safe whitepaper-grade archival review.
  - Notes: original derived prose; validated before submission; source documents and private processing evidence were not uploaded.
