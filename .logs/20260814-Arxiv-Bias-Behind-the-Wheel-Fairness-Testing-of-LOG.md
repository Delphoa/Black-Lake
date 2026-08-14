# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260814-24737ACA`
- Deployment item ID: `BLAD-2200-20260814-24737ACA-P01`
- Public-safe date: 2026-08-14
- Paper: *Bias Behind the Wheel: Fairness Testing of Autonomous Driving Systems*
- Identifier: `arXiv:2308.02935`; DOI: `10.48550/arXiv.2308.02935`
- URL: https://arxiv.org/abs/2308.02935

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 68,864 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Bias-Behind-the-Wheel-Fairness-Testing-of` slug; the 24-hour marker cutoff was 2026-08-13.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,521,079 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 24; sampled text inspection: true.
- Full-paper HTML: 450,070 bytes, 93,912 body characters, 77 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260814-Arxiv-Bias-Behind-the-Wheel-Fairness-Testing-of-LOG.md`
- `.reports/BL-Arxiv-Bias-Behind-the-Wheel-Fairness-Testing-of-20260814/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260814-Bias Behind the Wheel/README.md`
- `.lake-data/DEP-E/DEP-E-20260814-Bias Behind the Wheel/bias_behind_the_wheel_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260718-Stable Diffusion Depth/stable_diffusion_depth_manuscript.md` - Stable Diffusion Depth - DEP-E; overlap: driving, behind, bias, systems, autonomous.
2. `.lake-data/DEP-E/DEP-E-20260803-ADReFT Adaptive Decision/adreft_adaptive_decision_manuscript.md` - ADReFT Adaptive Decision - DEP-E; overlap: driving, autonomous, systems, testing.
3. `.lake-data/DEP-E/DEP-E-20260805-Light the Night A/light_the_night_a_manuscript.md` - Light the Night A - DEP-E; overlap: driving, autonomous, systems, testing.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
