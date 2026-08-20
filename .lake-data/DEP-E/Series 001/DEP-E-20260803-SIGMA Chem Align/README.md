# DEP-E-20260803-SIGMA Chem Align

#chemistry #molecular-generation #SMILES #contrastive-learning #graph-invariance #beam-search #research-review

Public-safe review of SIGMA, a source-grounded preprint review about structure-invariant alignment for autoregressive molecular language models and isomorphic beam search. Original paper files were inspected locally and withheld; this DEP contains generated Markdown and public locators only.

## Contents

- `README.md` - public-safe context, inventory, relevance, and attribution.
- `sigma_chem_align_manuscript.md` - schema-complete manuscript review with evidence ledger, limitations, implementation paths, exercises, and source references.

## Summary of Items

The manuscript reconstructs SIGMA's problem framing, functional-equivalence view construction, token-level contrastive objective, projection-decoupled architecture, IsoBeam decoder, ZINC-250k and PMO evaluation, reported metrics, reproducibility boundary, and safe implementation implications. It preserves author-reported results as claims rather than independent reproduction.

The local source unit passed the complete-paper gate before review: the full PDF and full-paper HTML were present and structurally validated. No repair was needed. Source documents, extracted text, caches, and other original files remain local and were not deposited.

## Insights and Relevance

SIGMA makes a useful separation between syntactic variation and structural identity: the training objective aligns equivalent token trajectories, while IsoBeam spends decoding capacity on distinct structure identifiers. The practical value is promising for research benchmarking, but evidence remains bounded by one ZINC-250k setup, three-run PMO summaries, proxy metrics, incomplete external validation, the cost and edge cases of partial-molecule structure checks, and the absence of a public implementation at review time. FGBench Chemistry, Graph Alignment, and Equivariant Contrastive provide concrete neighboring evidence for structure-aware benchmarks, graph alignment, and invariance-aware contrastive evaluation.

## Attribution Block

- Source URL: https://arxiv.org/abs/2603.25062
  - Applies to: `README.md` and `sigma_chem_align_manuscript.md`.
  - Notes: Canonical title, authors, submission record, abstract, version, subjects, and public paper locators.
- Source URL: https://arxiv.org/pdf/2603.25062
  - Applies to: `sigma_chem_align_manuscript.md`.
  - Notes: Public equivalent of the complete PDF inspected locally; the source file was withheld.
- Source URL: https://arxiv.org/html/2603.25062
  - Applies to: `sigma_chem_align_manuscript.md`.
  - Notes: Official full-paper HTML inspected locally; the source file was withheld.
- Source URL: https://doi.org/10.48550/arXiv.2603.25062
  - Applies to: `README.md` and `sigma_chem_align_manuscript.md`.
  - Notes: Persistent arXiv DOI.
- Source URL: https://www.xinyuwang1209.com/publications/
  - Applies to: `sigma_chem_align_manuscript.md`.
  - Notes: Author-maintained publication listing and release-context cross-check.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260716-FGBench%20Chemistry/fgbench_chemistry_manuscript.md
  - Applies to: `sigma_chem_align_manuscript.md`.
  - Notes: Related DEP for functional-group molecular reasoning benchmarks and chemistry-specific evaluation controls.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260722-Graph%20Alignment/graph_alignment_manuscript.md
  - Applies to: `sigma_chem_align_manuscript.md`.
  - Notes: Related DEP for graph alignment, uniformity, and representation-level evaluation.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260721-Equivariant%20Contrastive/equivariant_contrastive_manuscript.md
  - Applies to: `sigma_chem_align_manuscript.md`.
  - Notes: Related DEP for equivariant and contrastive invariance mechanisms.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md` and `sigma_chem_align_manuscript.md`.
  - Notes: Live repository authority for processed artifacts, source locality, DEP classes, and attribution.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `README.md` and `sigma_chem_align_manuscript.md`.
  - Notes: Live companion-repository authority used for related DEP and dedup context.
- Source handling: No PDF, HTML, source archive, extracted text, cache, private path, or `.source/` file was uploaded, committed, or attached.
