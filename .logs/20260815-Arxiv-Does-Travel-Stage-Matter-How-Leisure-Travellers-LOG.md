# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260815-A0637DE9`
- Deployment item ID: `BLAD-2200-20260815-A0637DE9-P09`
- Public-safe date: 2026-08-15
- Paper: *Does Travel Stage Matter? How Leisure Travellers Perceive Their Privacy Attitudes Towards Personal Data Sharing Before, During, and After Travel*
- Identifier: `arXiv:2603.01992`; DOI: `10.48550/arXiv.2603.01992`
- URL: https://arxiv.org/abs/2603.01992

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 31,095 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Does-Travel-Stage-Matter-How-Leisure-Travellers` slug; the 24-hour marker cutoff was 2026-08-14.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 358,193 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 18; sampled text inspection: true.
- Full-paper HTML: 584,718 bytes, 96,566 body characters, 85 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260815-Arxiv-Does-Travel-Stage-Matter-How-Leisure-Travellers-LOG.md`
- `.reports/BL-Arxiv-Does-Travel-Stage-Matter-How-Leisure-Travellers-20260815/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260815-Does Travel Stage Matter/README.md`
- `.lake-data/DEP-E/DEP-E-20260815-Does Travel Stage Matter/does_travel_stage_matter_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260728-CanCal Towards Real-time/cancal_towards_real_time_manuscript.md` - CanCal Towards Real-time - DEP-E; overlap: towards, during, privacy, does.
2. `.lake-data/DEP-E/DEP-E-20260730-RLHF-V Towards/rlhf_v_towards_manuscript.md` - RLHF-V Towards - DEP-E; overlap: towards, how, privacy, does.
3. `.lake-data/DEP-E/DEP-E-20260809-Discriminative and/discriminative_and_manuscript.md` - Discriminative and - DEP-E; overlap: towards, how, privacy, does.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
