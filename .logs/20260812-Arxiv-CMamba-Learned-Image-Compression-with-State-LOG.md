# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260812-9483C5E4`
- Deployment item ID: `BLAD-2200-20260812-9483C5E4-P08`
- Public-safe date: 2026-08-12
- Paper: *CMamba: Learned Image Compression with State Space Models*
- Identifier: `arXiv:2502.04988`; DOI: `10.48550/arXiv.2502.04988`
- URL: https://arxiv.org/abs/2502.04988

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 10,701 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `CMamba-Learned-Image-Compression-with-State` slug; the 24-hour marker cutoff was 2026-08-11.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,505,103 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 10; sampled text inspection: true.
- Full-paper HTML: 263,603 bytes, 59,148 body characters, 45 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260812-Arxiv-CMamba-Learned-Image-Compression-with-State-LOG.md`
- `.reports/BL-Arxiv-CMamba-Learned-Image-Compression-with-State-20260812/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260812-CMamba Learned Image/README.md`
- `.lake-data/DEP-E/DEP-E-20260812-CMamba Learned Image/cmamba_learned_image_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260804-Conceptual Compression/conceptual_compression_manuscript.md` - Conceptual Comp - DEP-E; overlap: compression, image, learned, state.
2. `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` - CAP Compression - DEP-E; overlap: compression, space, learned, image, state.
3. `.lake-data/DEP-E/DEP-E-20260708-ConMax Reasoning/conmax_reasoning_manuscript.md` - ConMax - DEP-E; overlap: compression, image, state.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
