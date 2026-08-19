# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P118`
- Public-safe date: 2026-08-19
- Paper: *Investigating Rumor News Using Agreement-Aware Search*
- Identifier: `arXiv:1802.07398`; DOI: `10.1145/3269206.3272020`
- URL: https://arxiv.org/abs/1802.07398

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 4,630 on draw 8.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: search.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Investigating-Rumor-News-Using-Agreement-Aware` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 7; source-gate exclusions: 0; reselections: 7.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,969,688 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 10; sampled text inspection: true.
- Full-paper HTML: 211,970 bytes, 55,925 body characters, 61 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Investigating-Rumor-News-Using-Agreement-Aware-LOG.md`
- `.reports/BL-Arxiv-Investigating-Rumor-News-Using-Agreement-Aware-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Investigating Rumor News/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Investigating Rumor News/investigating_rumor_news_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260802-COVID Fake News/covid_fake_news_manuscript.md` - COVID Fake News - DEP-E; overlap: news, rumor, search.
2. `.lake-data/DEP-E/DEP-E-20260802-Fantastic Semantics and/fantastic_semantics_and_manuscript.md` - Fantastic Semantics and - DEP-E; overlap: investigating, search.
3. `.lake-data/DEP-E/DEP-E-20260818-Lower Quantity Higher/lower_quantity_higher_manuscript.md` - Lower Quantity Higher - DEP-E; overlap: news, investigating.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
