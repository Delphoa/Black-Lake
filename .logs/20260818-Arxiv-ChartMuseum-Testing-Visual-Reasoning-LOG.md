# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-50A35360`
- Deployment item ID: `BLAD-2200-20260818-50A35360-P04`
- Public-safe date: 2026-08-18
- Paper: *ChartMuseum: Testing Visual Reasoning Capabilities of Large Vision-Language Models*
- Identifier: `arXiv:2505.13444`; DOI: `10.48550/arXiv.2505.13444`
- URL: https://arxiv.org/abs/2505.13444

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 11,241 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `ChartMuseum-Testing-Visual-Reasoning` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 28,802,142 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 49; sampled text inspection: true.
- Full-paper HTML: 512,064 bytes, 113,927 body characters, 112 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-ChartMuseum-Testing-Visual-Reasoning-LOG.md`
- `.reports/BL-Arxiv-ChartMuseum-Testing-Visual-Reasoning-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-ChartMuseum Testing/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-ChartMuseum Testing/chartmuseum_testing_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` - OViP Preference - DEP-E; overlap: vision-language, visual.
2. `.lake-data/DEP-E/DEP-E-20260818-RL of Thoughts Navigating/rl_of_thoughts_navigating_manuscript.md` - RL of Thoughts Navigating - DEP-E; overlap: reasoning, capabilities, testing.
3. `.lake-data/DEP-E/DEP-E-20260714-ComfyUI R1/comfyui_r1_manuscript.md` - ComfyUI-R1 Workflow - DEP-E; overlap: reasoning, visual, testing.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
