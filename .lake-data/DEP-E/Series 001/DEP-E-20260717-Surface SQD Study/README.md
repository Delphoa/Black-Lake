# DEP-E-20260717-Surface SQD Study

#quantum-computing #quantum-chemistry #materials-science #battery-research #sample-based-diagonalization #active-space #evidence-review

- Deposition date: 2026-07-17
- DEP class: DEP-E
- Subject title: Surface Reaction SQD Review
- Source DEP: Black-Lake-Data/.lake-data/DEP-20260624-Tech Intel 2338
- Expanded source: arXiv:2503.10923v2; DOI:10.1038/s41598-026-58228-0

## Contents

- `README.md`
  - DEP inventory, classification, source attribution, and downstream review context.
- `surface-sqd-study.md`
  - Schema-complete manuscript research artifact expanding the prior abstract-level SQD finding with full-paper methods, results, limitations, and replication planning.

## Summary of Items

`README.md` records the DEP-E class, selected source DEP, exact deposited files, primary-source locators, and final attribution required by the live repository standard.

`surface-sqd-study.md` reviews the lithium-oxygen surface-reaction workflow that combines DFT, density-difference and CCSD-natural-orbital active-space selection, LUCJ hardware sampling, SQD, and single-excitation Ext-SQD. It preserves reported circuit and invalid-sample statistics, distinguishes real-hardware feasibility from quantum-advantage claims, documents the classical diagonalization bottleneck, and records public scale tensions without inventing a resolution.

## Insights and Relevance

This deposit turns one related-reading node from the earlier broad `Tech Intel 2338` artifact into a focused evidence record. The most consequential relationship is that quantum-hardware scale cannot be assessed independently of classical preparation and post-processing: the active-space selector determines the modeled problem, most raw samples violate the required particle sector, Ext-SQD expands the recovered subspace classically, and the stated scaling bottleneck moves to classical diagonalization. The artifact adds direct semantic links to the local-embedding, SQD, Ext-SQD, and LUCJ method lineage for future review.

No external source file is included. Research-paper source payloads remain outside the public repository; only generated analysis, public URLs, and repository-relative provenance are deposited.

## Attribution Block

- Source repository path: Black-Lake-Data/.lake-data/DEP-20260624-Tech Intel 2338
  - Applies to: `surface-sqd-study.md`
  - Notes: Selected source DEP and prior Report-Mark lineage for this iterative review.
- Source URL: https://arxiv.org/abs/2503.10923
  - Applies to: `surface-sqd-study.md`
  - Notes: Canonical arXiv record for title, authors, version history, abstract, and publication linkage.
- Source URL: https://arxiv.org/html/2503.10923
  - Applies to: `surface-sqd-study.md`
  - Notes: Full-paper HTML inspected for methods, figures/tables, results, limitations, declarations, and references.
- Source URL: https://doi.org/10.1038/s41598-026-58228-0
  - Applies to: `surface-sqd-study.md`
  - Notes: Scientific Reports publication record, DOI, dates, authorship, abstract, and CC BY 4.0 license.
- Source URL: https://doi.org/10.1038/s41534-023-00753-1
  - Applies to: `surface-sqd-study.md`
  - Notes: Local-embedding methodological predecessor identified through the primary paper.
- Source URL: https://arxiv.org/abs/2405.05068
  - Applies to: `surface-sqd-study.md`
  - Notes: SQD method neighbor identified through the primary paper.
- Source URL: https://arxiv.org/abs/2411.00468
  - Applies to: `surface-sqd-study.md`
  - Notes: Ext-SQD method neighbor identified through the primary paper.
- Source URL: https://doi.org/10.1039/D3SC02516K
  - Applies to: `surface-sqd-study.md`
  - Notes: LUCJ state-preparation method identified through the primary paper.
