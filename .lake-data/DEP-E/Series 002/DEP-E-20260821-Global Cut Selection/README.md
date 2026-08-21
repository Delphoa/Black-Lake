# DEP-E-20260821-Global Cut Selection

**Classification:** DEP-E
**Subject tags:** artificial intelligence; mixed-integer programming; branch-and-cut; global cut selection; graph neural networks; reinforcement learning; solver control; search-tree optimization; research synthesis
**Deposition date:** 2026-08-21 (UTC)
**Source policy:** Public URLs and derived Markdown only. The reviewed PDF and full-paper HTML were verified locally and withheld; no original source file was uploaded.

## Contents

- `README.md` — this DEP inventory and public attribution record.
- `gcs_global_cut_manuscript.md` — schema-complete manuscript research document for arXiv:2503.15847.

## Summary of Items

- **`README.md`:** States the classification, public-safe deposition context, contents, relevance, and attribution needed to interpret the DEP without access to local source files.
- **`gcs_global_cut_manuscript.md`:** Records source metadata, evidence ledger, research summary, methodology, limitations, implementation ideas, three exercise paths, an MVP product concept, and exactly three related Black Lake DEP entries.

## Insights and Relevance

This DEP reviews Global Cut Selection (GCS), a graph-and-reinforcement-learning approach to selecting and ordering cuts from global branch-and-cut context. It complements the job log at `.logs/20260821-Arxiv-GCS-Global-Cut-LOG.md`, which records the operational selection, integrity, and validation checkpoints, and the detailed Report-Mark at `.reports/BL-Arxiv-GCS-Global-Cut-20260821/Report-Mark.md`, which contains the deeper synthesis and implementation mock-ups.

The manuscript connects GCS with three existing DEP-E entries: heterogeneous graph-attention solver state, reinforcement learning for coupled optimization, and tree-search feedback. The combined relevance is a bounded solver-control pattern: encode structured state, model action interactions, measure downstream outcomes, and preserve a deterministic fallback when global context is too costly or uncertain.

## Attribution Block

- Selected paper: [arXiv:2503.15847](https://arxiv.org/abs/2503.15847), [full-paper HTML](https://arxiv.org/html/2503.15847), [PDF](https://arxiv.org/pdf/2503.15847), and [DOI](https://doi.org/10.48550/arXiv.2503.15847). The original source files were verified locally and withheld from this public DEP.
- Related DEP: [HGATSolver A](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260819-HGATSolver%20A).
- Related DEP: [Joint Optimization of](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20002/DEP-E-20260819-Joint%20Optimization%20of).
- Related DEP: [Monte Carlo Tree Search](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20002/DEP-E-20260819-Monte%20Carlo%20Tree%20Search).
- Repository authority: [Delphoa/Black-Lake](https://github.com/Delphoa/Black-Lake) README and live `.lake-data` README were consulted for the canonical DEP layout and public-output rules.
