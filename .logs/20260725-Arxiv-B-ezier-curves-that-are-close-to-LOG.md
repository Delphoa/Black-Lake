# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260725-FF48EE13`
- Deployment item ID: `BLAD-2200-20260725-FF48EE13-P10`
- Public-safe date: 2026-07-25
- Paper: *B\'ezier curves that are close to elastica*
- Identifier: `arXiv:1710.09192`; DOI: `10.48550/arXiv.1710.09192`
- URL: https://arxiv.org/abs/1710.09192

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 63,047 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `B-ezier-curves-that-are-close-to` slug; the 24-hour marker cutoff was 2026-07-24.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,139,411 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 13; sampled text inspection: true.
- Full-paper HTML: 573,564 bytes, 51,431 body characters, 46 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260725-Arxiv-B-ezier-curves-that-are-close-to-LOG.md`
- `.reports/BL-Arxiv-B-ezier-curves-that-are-close-to-20260725/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260725-B ezier curves that are/README.md`
- `.lake-data/DEP-E/DEP-E-20260725-B ezier curves that are/b_ezier_curves_that_are_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260720-VG Navigable Space/vg_navigable_space_manuscript.md` - VG Navigable Space Review - DEP-E; overlap: navigable, navigation.
2. `.lake-data/DEP-E/DEP-E-20260722-GenTune Traceable Prompts/gentune_traceable_prompts_manuscript.md` - GenTune Traceable Prompts Review - DEP-E; overlap: environment, design.
3. `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/favla_fast_slow_manuscript.md` - FAVLA Fast-Slow - DEP-E; overlap: robotic, control.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
