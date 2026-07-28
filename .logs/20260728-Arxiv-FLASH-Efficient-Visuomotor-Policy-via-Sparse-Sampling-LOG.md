# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260728-EB036F17`
- Deployment item ID: `BLAD-2200-20260728-EB036F17-P09`
- Public-safe date: 2026-07-28
- Paper: *FLASH: Efficient Visuomotor Policy via Sparse Sampling*
- Identifier: `arXiv:2605.15492`; DOI: `10.48550/arXiv.2605.15492`
- URL: https://arxiv.org/abs/2605.15492

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75825 PDFs and 75822 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 14494.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant deposited identifiers, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `FLASH-Efficient-Visuomotor-Policy-via-Sparse-Sampling` slug; the 24-hour marker cutoff was 2026-07-27.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 9348303 bytes with valid `%PDF-` header and trailing `%%EOF`; page markers: 24.
- Full-paper HTML: 283593 bytes, 53058 body characters, 53 headings, and 4 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260728-Arxiv-FLASH-Efficient-Visuomotor-Policy-via-Sparse-Sampling-LOG.md`
- `.reports/BL-Arxiv-FLASH-Efficient-Visuomotor-Policy-via-Sparse-Sampling-20260728/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260728-FLASH Efficient/README.md`
- `.lake-data/DEP-E/DEP-E-20260728-FLASH Efficient/flash_efficient_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-Semantic Skill MoE/semantic_skill_moe_manuscript.md` - Semantic Skill MoE Policies; overlap: action, all, high.
2. `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/favla_fast_slow_manuscript.md` - FAVLA Fast-Slow - DEP-E; overlap: all, experiments, high.
3. `.lake-data/DEP-E/DEP-E-20260726-ManipulationNet An/manipulationnet_an_manuscript.md` - ManipulationNet An - DEP-E; overlap: accurate, control, directly.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
