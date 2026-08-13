# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260813-F994AA5E`
- Deployment item ID: `BLAD-2200-20260813-F994AA5E-P09`
- Public-safe date: 2026-08-13
- Paper: *Beyond Line-of-Sight: Cooperative Localization Using Vision and V2X Communication*
- Identifier: `arXiv:2507.20772`; DOI: `10.48550/arXiv.2507.20772`
- URL: https://arxiv.org/abs/2507.20772

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 4,164 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Beyond-Line-of-Sight-Cooperative-Localization` slug; the 24-hour marker cutoff was 2026-08-12.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,591,967 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 8; sampled text inspection: true.
- Full-paper HTML: 290,175 bytes, 55,609 body characters, 56 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260813-Arxiv-Beyond-Line-of-Sight-Cooperative-Localization-LOG.md`
- `.reports/BL-Arxiv-Beyond-Line-of-Sight-Cooperative-Localization-20260813/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260813-Beyond Line-of-Sight/README.md`
- `.lake-data/DEP-E/DEP-E-20260813-Beyond Line-of-Sight/beyond_line_of_sight_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260803-Empirical Study on/empirical_study_on_manuscript.md` - Empirical Study on - DEP-E; overlap: cooperative.
2. `.lake-data/DEP-E/DEP-E-20260805-UAV-Assisted Cooperative/uav_assisted_cooperative_manuscript.md` - UAV-Assisted Cooperative - DEP-E; overlap: cooperative.
3. `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md` - Multi-Point ISAC - DEP-E; overlap: communication, cooperative.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
