# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260810-B3B6846E`
- Deployment item ID: `BLAD-2200-20260810-B3B6846E-P07`
- Public-safe date: 2026-08-10
- Paper: *FES-FM: Free Energy Surface Sampling via Reduced Flow Matching*
- Identifier: `arXiv:2605.00337`; DOI: `10.48550/arXiv.2605.00337`
- URL: https://arxiv.org/abs/2605.00337

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 53,363 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Free-Energy-Surface-Sampling-via-Reduced-Flow` slug; the 24-hour marker cutoff was 2026-08-09.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,311,551 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 22; sampled text inspection: true.
- Full-paper HTML: 485,791 bytes, 85,470 body characters, 87 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260810-Arxiv-Free-Energy-Surface-Sampling-via-Reduced-Flow-LOG.md`
- `.reports/BL-Arxiv-Free-Energy-Surface-Sampling-via-Reduced-Flow-20260810/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260810-Free Energy Surface/README.md`
- `.lake-data/DEP-E/DEP-E-20260810-Free Energy Surface/free_energy_surface_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260801-High-Order Langevin/high_order_langevin_manuscript.md` - High-Order Langevin - DEP-E; overlap: distribution sampling, diffusion dynamics, accelerated MCMC.
2. `.lake-data/DEP-E/DEP-E-20260803-SIGMA Chem Align/sigma_chem_align_manuscript.md` - SIGMA Chem Align - DEP-E; overlap: molecular structure, invariant representation, chemical systems.
3. `.lake-data/DEP-E/DEP-E-20260716-FGBench Chemistry/fgbench_chemistry_manuscript.md` - FGBench Chemistry - DEP-E; overlap: molecular properties, chemical reasoning, benchmark evaluation.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
