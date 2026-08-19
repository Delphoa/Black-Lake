# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P73`
- Public-safe date: 2026-08-19
- Paper: *ReFreeKV: Towards Threshold-Free KV Cache Compression*
- Identifier: `arXiv:2502.16886`; DOI: `10.48550/arXiv.2502.16886`
- URL: https://arxiv.org/abs/2502.16886

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 14,691 on draw 52.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: kv cache.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `ReFreeKV-Towards-Threshold-Free-KV-Cache` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 51; source-gate exclusions: 0; reselections: 51.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 417,794 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 16; sampled text inspection: true.
- Full-paper HTML: 393,452 bytes, 71,433 body characters, 98 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-ReFreeKV-Towards-Threshold-Free-KV-Cache-LOG.md`
- `.reports/BL-Arxiv-ReFreeKV-Towards-Threshold-Free-KV-Cache-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-ReFreeKV Towards/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-ReFreeKV Towards/refreekv_towards_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260730-RLHF-V Towards/rlhf_v_towards_manuscript.md` - RLHF-V Towards - DEP-E; overlap: towards, cache.
2. `.lake-data/DEP-E/DEP-E-20260809-Discriminative and/discriminative_and_manuscript.md` - Discriminative and - DEP-E; overlap: towards, cache.
3. `.lake-data/DEP-E/DEP-E-20260815-Does Travel Stage Matter/does_travel_stage_matter_manuscript.md` - Does Travel Stage Matter - DEP-E; overlap: towards, cache.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
