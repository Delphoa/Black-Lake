# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260813-F994AA5E`
- Deployment item ID: `BLAD-2200-20260813-F994AA5E-P01`
- Public-safe date: 2026-08-13
- Paper: *Controllable Dynamic Appearance for Neural 3D Portraits*
- Identifier: `arXiv:2309.11009`; DOI: `10.48550/arXiv.2309.11009`
- URL: https://arxiv.org/abs/2309.11009

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 36,584 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Controllable-Dynamic-Appearance-for-Neural-3D` slug; the 24-hour marker cutoff was 2026-08-12.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 48,835,335 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 17; sampled text inspection: true.
- Full-paper HTML: 320,692 bytes, 70,662 body characters, 80 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260813-Arxiv-Controllable-Dynamic-Appearance-for-Neural-3D-LOG.md`
- `.reports/BL-Arxiv-Controllable-Dynamic-Appearance-for-Neural-3D-20260813/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260813-Controllable Dynamic/README.md`
- `.lake-data/DEP-E/DEP-E-20260813-Controllable Dynamic/controllable_dynamic_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md` - Self-Learned IDC - DEP-E; overlap: dynamic, neural.
2. `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` - DMNN Conditional Paths - DEP-E; overlap: dynamic, neural.
3. `.lake-data/DEP-E/DEP-E-20260722-4DContrast Contrastive/4dcontrast_contrastive_manuscript.md` - 4DContrast Contrastive Review - DEP-E; overlap: dynamic.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
