# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P57`
- Public-safe date: 2026-08-19
- Paper: *TaDA: Training-free recipe for Decoding with Adaptive KV Cache Compression and Mean-centering*
- Identifier: `arXiv:2506.04642`; DOI: `10.48550/arXiv.2506.04642`
- URL: https://arxiv.org/abs/2506.04642

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 68,055 on draw 8.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: kv cache.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `TaDA-Training-free-recipe-for-Decoding-with` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 6; source-gate exclusions: 0; reselections: 7.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 321,612 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 9; sampled text inspection: true.
- Full-paper HTML: 156,057 bytes, 38,230 body characters, 43 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-TaDA-Training-free-recipe-for-Decoding-with-LOG.md`
- `.reports/BL-Arxiv-TaDA-Training-free-recipe-for-Decoding-with-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-TaDA Training-free recipe/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-TaDA Training-free recipe/tada_training_free_recipe_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260727-Language-to-Space/language_to_space_manuscript.md` - Language-to-Space - DEP-E; overlap: training-free, cache.
2. `.lake-data/DEP-E/DEP-E-20260818-VFM-Loc Zero-Shot/vfm_loc_zero_shot_manuscript.md` - VFM-Loc Zero-Shot - DEP-E; overlap: training-free, cache.
3. `.lake-data/DEP-E/DEP-E-20260719-MIRA One Touch/mira_one_touch_manuscript.md` - One-Touch Instruction Routing; overlap: decoding, cache.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
