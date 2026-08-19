# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P124`
- Public-safe date: 2026-08-19
- Paper: *HiP-AD: Hierarchical and Multi-Granularity Planning with Deformable Attention for Autonomous Driving in a Single Decoder*
- Identifier: `arXiv:2503.08612`; DOI: `10.48550/arXiv.2503.08612`
- URL: https://arxiv.org/abs/2503.08612

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 52,271 on draw 5.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: planning.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `HiP-AD-Hierarchical-and-Multi-Granularity` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 4; source-gate exclusions: 0; reselections: 4.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 20,079,891 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 17; sampled text inspection: true.
- Full-paper HTML: 309,355 bytes, 65,652 body characters, 59 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-HiP-AD-Hierarchical-and-Multi-Granularity-LOG.md`
- `.reports/BL-Arxiv-HiP-AD-Hierarchical-and-Multi-Granularity-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-HiP-AD Hierarchical and/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-HiP-AD Hierarchical and/hip_ad_hierarchical_and_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md` - Device Tuning MTL - DEP-E; overlap: decoder, attention, single, autonomous, planning.
2. `.lake-data/DEP-E/DEP-E-20260718-Stable Diffusion Depth/stable_diffusion_depth_manuscript.md` - Stable Diffusion Depth - DEP-E; overlap: driving, decoder, attention, single, autonomous.
3. `.lake-data/DEP-E/DEP-E-20260805-Light the Night A/light_the_night_a_manuscript.md` - Light the Night A - DEP-E; overlap: driving, autonomous, attention, planning.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
