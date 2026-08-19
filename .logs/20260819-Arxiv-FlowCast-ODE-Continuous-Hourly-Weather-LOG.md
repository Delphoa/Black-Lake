# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P135`
- Public-safe date: 2026-08-19
- Paper: *FlowCast-ODE: Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Solver*
- Identifier: `arXiv:2509.14775`; DOI: `10.48550/arXiv.2509.14775`
- URL: https://arxiv.org/abs/2509.14775

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 70,688 on draw 9.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: solver.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `FlowCast-ODE-Continuous-Hourly-Weather` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 7; source-gate exclusions: 0; reselections: 8.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 4,315,737 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 26; sampled text inspection: true.
- Full-paper HTML: 226,424 bytes, 66,275 body characters, 80 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-FlowCast-ODE-Continuous-Hourly-Weather-LOG.md`
- `.reports/BL-Arxiv-FlowCast-ODE-Continuous-Hourly-Weather-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-FlowCast-ODE Continuous/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-FlowCast-ODE Continuous/flowcast_ode_continuous_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-PIS A Generalized/pis_a_generalized_manuscript.md` - PIS A Generalized - DEP-E; overlap: solver, flow, matching.
2. `.lake-data/DEP-E/DEP-E-20260819-Fast Block Linear System/fast_block_linear_system_manuscript.md` - Fast Block Linear System - DEP-E; overlap: solver, dynamic, matching.
3. `.lake-data/DEP-E/DEP-E-20260811-PA-RNet/pa_rnet_manuscript.md` - PA-RNet - DEP-E; overlap: forecasting, matching.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
