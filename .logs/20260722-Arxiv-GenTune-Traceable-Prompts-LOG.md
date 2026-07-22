# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260722-A5461BD0`
- Deployment item ID: `BLAD-2200-20260722-A5461BD0-P10`
- Public-safe date: 2026-07-22
- Paper: *GenTune: Toward Traceable Prompts to Improve Controllability of Image Refinement in Environment Design*
- Identifier: `arXiv:2508.15227`; DOI: `10.1145/3746059.3747774`
- URL: https://arxiv.org/abs/2508.15227

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,780 PDFs and 75,777 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 2,945 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, the public dedup index, automation memory, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `GenTune-Traceable-Prompts` slug; the 24-hour marker cutoff was 2026-07-21.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded archive repair.
- PDF: 28,038,018 bytes with a valid `%PDF-` header and trailing `%%EOF`.
- Full-paper HTML: 265,685 bytes, 107,072 body characters, 2 document markers, 94 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260722-Arxiv-GenTune-Traceable-Prompts-LOG.md`
- `.reports/BL-Arxiv-GenTune-Traceable-Prompts-20260722/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260722-GenTune Traceable Prompts/README.md`
- `.lake-data/DEP-E/DEP-E-20260722-GenTune Traceable Prompts/gentune_traceable_prompts_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md`
2. `.lake-data/DEP-E/DEP-E-20260716-UAV Visual Localization/uav_visual_localization_manuscript.md`
3. `.lake-data/DEP-E/DEP-E-20260719-CLOVER Test Benchmark/clover_test_benchmark_manuscript.md`

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
