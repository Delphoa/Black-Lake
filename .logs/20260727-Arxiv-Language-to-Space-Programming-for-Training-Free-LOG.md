# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260727-ADBD50D5`
- Deployment item ID: `BLAD-2200-20260727-ADBD50D5-P03`
- Public-safe date: 2026-07-27
- Paper: *Language-to-Space Programming for Training-Free 3D Visual Grounding*
- Identifier: `arXiv:2502.01401`; DOI: `10.48550/arXiv.2502.01401`
- URL: https://arxiv.org/abs/2502.01401

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 72,018 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Language-to-Space-Programming-for-Training-Free` slug; the 24-hour marker cutoff was 2026-07-26.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 3,731,850 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 21; sampled text inspection: true.
- Full-paper HTML: 872,139 bytes, 79,461 body characters, 106 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260727-Arxiv-Language-to-Space-Programming-for-Training-Free-LOG.md`
- `.reports/BL-Arxiv-Language-to-Space-Programming-for-Training-Free-20260727/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260727-Language-to-Space/README.md`
- `.lake-data/DEP-E/DEP-E-20260727-Language-to-Space/language_to_space_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-MIRA One Touch/mira_one_touch_manuscript.md` - One-Touch Instruction Routing; overlap: constrained, retrieval, recommendation.
2. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` - OViP Preference - DEP-E; overlap: preference, vision-language.
3. `.lake-data/DEP-E/DEP-E-20260726-ManipulationNet An/manipulationnet_an_manuscript.md` - ManipulationNet An - DEP-E; overlap: challenges, robot.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
