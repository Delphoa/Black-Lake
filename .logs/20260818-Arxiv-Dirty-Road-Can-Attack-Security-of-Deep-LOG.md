# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-D85F5742`
- Deployment item ID: `BLAD-2200-20260818-D85F5742-P05`
- Public-safe date: 2026-08-18
- Paper: *Dirty Road Can Attack: Security of Deep Learning based Automated Lane Centering under Physical-World Attack*
- Identifier: `arXiv:2009.06701`; DOI: `10.48550/arXiv.2009.06701`
- URL: https://arxiv.org/abs/2009.06701

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 7,759 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Dirty-Road-Can-Attack-Security-of-Deep` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 1; source-gate exclusions: 0; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 24,245,117 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 29; sampled text inspection: true.
- Full-paper HTML: 561,396 bytes, 162,288 body characters, 112 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-Dirty-Road-Can-Attack-Security-of-Deep-LOG.md`
- `.reports/BL-Arxiv-Dirty-Road-Can-Attack-Security-of-Deep-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-Dirty Road Can Attack/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-Dirty Road Can Attack/dirty_road_can_attack_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Stereo Lane Detection/stereo_lane_detection_manuscript.md` - Stereo Lane Detection - DEP-E; overlap: lane, road, under.
2. `.lake-data/DEP-E/DEP-E-20260809-From Similarity to/from_similarity_to_manuscript.md` - From Similarity to - DEP-E; overlap: attack, security, under.
3. `.lake-data/DEP-E/DEP-E-20260810-DexMimicGen Automated/dexmimicgen_automated_manuscript.md` - DexMimicGen Automated - DEP-E; overlap: automated, under.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
