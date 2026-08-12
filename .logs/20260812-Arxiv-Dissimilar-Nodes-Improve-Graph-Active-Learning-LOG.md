# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260812-9483C5E4`
- Deployment item ID: `BLAD-2200-20260812-9483C5E4-P02`
- Public-safe date: 2026-08-12
- Paper: *Dissimilar Nodes Improve Graph Active Learning*
- Identifier: `arXiv:2212.01968`; DOI: `10.48550/arXiv.2212.01968`
- URL: https://arxiv.org/abs/2212.01968

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 22,835 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Dissimilar-Nodes-Improve-Graph-Active-Learning` slug; the 24-hour marker cutoff was 2026-08-11.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 482,639 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 168,692 bytes, 41,923 body characters, 47 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260812-Arxiv-Dissimilar-Nodes-Improve-Graph-Active-Learning-LOG.md`
- `.reports/BL-Arxiv-Dissimilar-Nodes-Improve-Graph-Active-Learning-20260812/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260812-Dissimilar Nodes Improve/README.md`
- `.lake-data/DEP-E/DEP-E-20260812-Dissimilar Nodes Improve/dissimilar_nodes_improve_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260728-Constrained Bayesian/constrained_bayesian_manuscript.md` - Constrained Bayesian - DEP-E; overlap: active, improve.
2. `.lake-data/DEP-E/DEP-E-20260801-APRIL Active Partial/april_active_partial_manuscript.md` - APRIL Active Partial - DEP-E; overlap: active.
3. `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md` - Medical Diff VQA - DEP-E; overlap: graph, nodes, improve.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
