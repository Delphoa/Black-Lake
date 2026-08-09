# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260809-2E4CB30E`
- Deployment item ID: `BLAD-2200-20260809-2E4CB30E-P02`
- Public-safe date: 2026-08-09
- Paper: *Streaming Transformer-based Acoustic Models Using Self-attention with Augmented Memory*
- Identifier: `arXiv:2005.08042`; DOI: `10.48550/arXiv.2005.08042`
- URL: https://arxiv.org/abs/2005.08042

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 1,144 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Streaming-Transformer-based-Acoustic-Models` slug; the 24-hour marker cutoff was 2026-08-08.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 396,695 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 5; sampled text inspection: true.
- Full-paper HTML: 230,633 bytes, 33,146 body characters, 35 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260809-Arxiv-Streaming-Transformer-based-Acoustic-Models-LOG.md`
- `.reports/BL-Arxiv-Streaming-Transformer-based-Acoustic-Models-20260809/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260809-Streaming/README.md`
- `.lake-data/DEP-E/DEP-E-20260809-Streaming/streaming_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260801-RawBMamba/rawbmamba_manuscript.md` - RawBMamba Review - DEP-E; overlap: streaming, self-attention, acoustic, memory.
2. `.lake-data/DEP-E/DEP-E-20260731-Lattice Spoken LM/lattice_spoken_lm_manuscript.md` - Lattice Spoken LM - DEP-E; overlap: transformer-based, streaming, pruning, memory.
3. `.lake-data/DEP-E/DEP-E-20260711-Telecom AI Roadmap/telecom_ai_roadmap_manuscript.md` - Telecom AI Roadmap - DEP-E; overlap: transformer-based, quantization, pruning, compression, memory.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
