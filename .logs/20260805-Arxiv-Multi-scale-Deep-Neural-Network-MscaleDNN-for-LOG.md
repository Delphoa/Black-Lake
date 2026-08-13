# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260805-6C10E207`
- Deployment item ID: `BLAD-2200-20260805-6C10E207-P02`
- Public-safe date: 2026-08-05
- Paper: *Multi-scale Deep Neural Network (MscaleDNN) for Solving Poisson-Boltzmann Equation in Complex Domains*
- Identifier: `arXiv:2007.11207`; DOI: `10.4208/cicp.OA-2020-0179`
- URL: https://arxiv.org/abs/2007.11207

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 6,822 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Multi-scale-Deep-Neural-Network-MscaleDNN-for` slug; the 24-hour marker cutoff was 2026-08-04.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 3,513,314 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 34; sampled text inspection: true.
- Full-paper HTML: 1,368,935 bytes, 81,699 body characters, 74 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260805-Arxiv-Multi-scale-Deep-Neural-Network-MscaleDNN-for-LOG.md`
- `.reports/BL-Arxiv-Multi-scale-Deep-Neural-Network-MscaleDNN-for-20260805/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260805-Multi-scale Deep Neural/README.md`
- `.lake-data/DEP-E/DEP-E-20260805-Multi-scale Deep Neural/multi_scale_deep_neural_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260723-Schwarz Neural Inference/schwarz_neural_inference_manuscript.md` - Schwarz Neural Inference - DEP-E; overlap: solving, equation, complex, neural, domains.
2. `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` - Physical Data - DEP-E; overlap: equation, complex, neural, domains, network.
3. `.lake-data/DEP-E/DEP-E-20260801-Dehomogenized 3D Topology/dehomogenized_3d_topology_manuscript.md` - 3D Dehomogenization - DEP-E; overlap: multi-scale, equation, domains.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
