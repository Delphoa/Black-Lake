# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P408`
- Public-safe date: 2026-08-19
- Paper: *Just Say What You Want: Only-prompting Self-rewarding Online Preference Optimization*
- Identifier: `arXiv:2409.17534`; DOI: `10.48550/arXiv.2409.17534`
- URL: https://arxiv.org/abs/2409.17534

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 63,669 on draw 55.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: optimization.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Just-Say-What-You-Want-Only-prompting` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 9; focus exclusions: 45; source-gate exclusions: 0; reselections: 54.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,335,848 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 13; sampled text inspection: true.
- Full-paper HTML: 187,154 bytes, 47,499 body characters, 65 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Just-Say-What-You-Want-Only-prompting-LOG.md`
- `.reports/BL-Arxiv-Just-Say-What-You-Want-Only-prompting-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Just Say What You Want/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Just Say What You Want/just_say_what_you_want_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260813-Adapt as You Say Online/adapt_as_you_say_online_manuscript.md` - Adapt as You Say Online - DEP-E; overlap: say, you, online.
2. `.lake-data/DEP-E/DEP-E-20260818-OffSeeker Online/offseeker_online_manuscript.md` - OffSeeker Online - DEP-E; overlap: you, online, say.
3. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` - OViP Preference - DEP-E; overlap: preference, online, optimization.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
