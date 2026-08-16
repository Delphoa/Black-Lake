# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260816-7EAAB41B`
- Deployment item ID: `BLAD-2200-20260816-7EAAB41B-P09`
- Public-safe date: 2026-08-16
- Paper: *Get Your Embedding Space in Order: Domain-Adaptive Regression for Forest Monitoring*
- Identifier: `arXiv:2405.00514`; DOI: `10.48550/arXiv.2405.00514`
- URL: https://arxiv.org/abs/2405.00514

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 41,665 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Get-Your-Embedding-Space-in-Order-Domain` slug; the 24-hour marker cutoff was 2026-08-15.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 10,366,893 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 21; sampled text inspection: true.
- Full-paper HTML: 328,355 bytes, 72,870 body characters, 70 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260816-Arxiv-Get-Your-Embedding-Space-in-Order-Domain-LOG.md`
- `.reports/BL-Arxiv-Get-Your-Embedding-Space-in-Order-Domain-20260816/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260816-Get Your Embedding Space/README.md`
- `.lake-data/DEP-E/DEP-E-20260816-Get Your Embedding Space/get_your_embedding_space_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260801-CrossNER Adapt/crossner_domain_adaptation_manuscript.md` - CrossNER - DEP-E; overlap: domain-adaptive, order, monitoring.
2. `.lake-data/DEP-E/DEP-E-20260730-Drag Your GAN Interactive/drag_your_gan_interactive_manuscript.md` - Drag Your GAN Interactive - DEP-E; overlap: your, monitoring.
3. `.lake-data/DEP-E/DEP-E-20260709-SANE Embeddings/sane_embeddings_manuscript.md` - SANE Embeddings - DEP-E; overlap: embedding, get, regression, space.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
