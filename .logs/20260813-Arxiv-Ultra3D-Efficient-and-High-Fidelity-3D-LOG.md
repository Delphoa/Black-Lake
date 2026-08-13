# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260813-F994AA5E`
- Deployment item ID: `BLAD-2200-20260813-F994AA5E-P06`
- Public-safe date: 2026-08-13
- Paper: *Ultra3D: Efficient and High-Fidelity 3D Generation with Part Attention*
- Identifier: `arXiv:2507.17745`; DOI: `10.48550/arXiv.2507.17745`
- URL: https://arxiv.org/abs/2507.17745

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 42,740 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Ultra3D-Efficient-and-High-Fidelity-3D` slug; the 24-hour marker cutoff was 2026-08-12.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 32,619,920 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 17; sampled text inspection: true.
- Full-paper HTML: 154,877 bytes, 60,524 body characters, 46 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260813-Arxiv-Ultra3D-Efficient-and-High-Fidelity-3D-LOG.md`
- `.reports/BL-Arxiv-Ultra3D-Efficient-and-High-Fidelity-3D-20260813/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260813-Ultra3D Efficient and/README.md`
- `.lake-data/DEP-E/DEP-E-20260813-Ultra3D Efficient and/ultra3d_efficient_and_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` - AFIDAF Vision - DEP-E; overlap: attention, part.
2. `.lake-data/DEP-E/DEP-E-20260719-MiNet CTR Transfer/minet_ctr_manuscript.md` - Mixed-Interest CTR Transfer; overlap: attention.
3. `.lake-data/DEP-E/DEP-E-20260729-Decentralized Attention/decentralized_attention_manuscript.md` - Decentralized Attention - DEP-E; overlap: attention.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
