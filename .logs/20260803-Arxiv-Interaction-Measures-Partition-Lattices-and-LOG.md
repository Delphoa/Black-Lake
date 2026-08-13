# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260803-11C1283E`
- Deployment item ID: `BLAD-2200-20260803-11C1283E-P04`
- Public-safe date: 2026-08-03
- Paper: *Interaction Measures, Partition Lattices and Kernel Tests for High-Order Interactions*
- Identifier: `arXiv:2306.00904`; DOI: `10.48550/arXiv.2306.00904`
- URL: https://arxiv.org/abs/2306.00904

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 75,267 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Interaction-Measures-Partition-Lattices-and` slug; the 24-hour marker cutoff was 2026-08-02.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 6,809,164 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 22; sampled text inspection: true.
- Full-paper HTML: 1,363,170 bytes, 101,269 body characters, 99 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260803-Arxiv-Interaction-Measures-Partition-Lattices-and-LOG.md`
- `.reports/BL-Arxiv-Interaction-Measures-Partition-Lattices-and-20260803/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260803-Interaction Measures/README.md`
- `.lake-data/DEP-E/DEP-E-20260803-Interaction Measures/interaction_measures_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260720-VaTD Canonical/vatd_canonical_manuscript.md` - VaTD Canonical - DEP-E; overlap: lattices, partition, interactions, tests.
2. `.lake-data/DEP-E/DEP-E-20260717-Moran Spectra/moran_spectra_manuscript.md` - Moran Spectra - DEP-E; overlap: lattices, partition, measures, tests.
3. `.lake-data/DEP-E/DEP-E-20260718-SpOctA Accelerator/spocta_accelerator_manuscript.md` - SpOctA Accelerator - DEP-E; overlap: partition, kernel, measures, tests.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
