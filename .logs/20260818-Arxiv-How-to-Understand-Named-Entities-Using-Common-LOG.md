# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-D85F5742`
- Deployment item ID: `BLAD-2200-20260818-D85F5742-P30`
- Public-safe date: 2026-08-18
- Paper: *How to Understand Named Entities: Using Common Sense for News Captioning*
- Identifier: `arXiv:2403.06520`; DOI: `10.48550/arXiv.2403.06520`
- URL: https://arxiv.org/abs/2403.06520

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 1,729 on draw 2.

## Research Focus Eligibility

- One-time focus: No one-time topic focus was requested..
- Matched categories: unrestricted.
- Matched title/abstract terms or phrases: not applicable.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `How-to-Understand-Named-Entities-Using-Common` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; focus exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,311,851 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 14; sampled text inspection: true.
- Full-paper HTML: 322,964 bytes, 84,559 body characters, 59 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-How-to-Understand-Named-Entities-Using-Common-LOG.md`
- `.reports/BL-Arxiv-How-to-Understand-Named-Entities-Using-Common-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-How to Understand Named/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-How to Understand Named/how_to_understand_named_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260802-COVID Fake News/covid_fake_news_manuscript.md` - COVID Fake News - DEP-E; overlap: news, named, how.
2. `.lake-data/DEP-E/DEP-E-20260801-CrossNER Adapt/crossner_domain_adaptation_manuscript.md` - CrossNER - DEP-E; overlap: named, entities.
3. `.lake-data/DEP-E/DEP-E-20260804-Forget FOLTR/forget_foltr_manuscript.md` - FOLTR Unlearning - DEP-E; overlap: how, sense.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
