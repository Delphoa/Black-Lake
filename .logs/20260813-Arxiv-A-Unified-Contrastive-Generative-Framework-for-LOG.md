# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260813-F994AA5E`
- Deployment item ID: `BLAD-2200-20260813-F994AA5E-P02`
- Public-safe date: 2026-08-13
- Paper: *A Unified Contrastive-Generative Framework for Time Series Classification*
- Identifier: `arXiv:2508.09451`; DOI: `10.48550/arXiv.2508.09451`
- URL: https://arxiv.org/abs/2508.09451

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 62,873 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `A-Unified-Contrastive-Generative-Framework-for` slug; the 24-hour marker cutoff was 2026-08-12.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,441,255 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 10; sampled text inspection: true.
- Full-paper HTML: 252,714 bytes, 60,146 body characters, 79 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260813-Arxiv-A-Unified-Contrastive-Generative-Framework-for-LOG.md`
- `.reports/BL-Arxiv-A-Unified-Contrastive-Generative-Framework-for-20260813/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260813-A Unified/README.md`
- `.lake-data/DEP-E/DEP-E-20260813-A Unified/a_unified_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260729-Decentralized Attention/decentralized_attention_manuscript.md` - Decentralized Attention - DEP-E; overlap: series, time.
2. `.lake-data/DEP-E/DEP-E-20260811-PA-RNet/pa_rnet_manuscript.md` - PA-RNet - DEP-E; overlap: series, time.
3. `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` - HERMES World Model - DEP-E; overlap: unified, time.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
