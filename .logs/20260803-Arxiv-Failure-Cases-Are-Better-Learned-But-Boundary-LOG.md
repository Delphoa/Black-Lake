# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260803-11C1283E`
- Deployment item ID: `BLAD-2200-20260803-11C1283E-P02`
- Public-safe date: 2026-08-03
- Paper: *Failure Cases Are Better Learned But Boundary Says Sorry: Facilitating Smooth Perception Change for Accuracy-Robustness Trade-Off in Adversarial Training*
- Identifier: `arXiv:2508.02186`; DOI: `10.48550/arXiv.2508.02186`
- URL: https://arxiv.org/abs/2508.02186

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 40,314 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Failure-Cases-Are-Better-Learned-But-Boundary` slug; the 24-hour marker cutoff was 2026-08-02.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,343,776 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 14; sampled text inspection: true.
- Full-paper HTML: 384,596 bytes, 90,603 body characters, 59 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260803-Arxiv-Failure-Cases-Are-Better-Learned-But-Boundary-LOG.md`
- `.reports/BL-Arxiv-Failure-Cases-Are-Better-Learned-But-Boundary-20260803/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260803-Failure Cases Are Better/README.md`
- `.lake-data/DEP-E/DEP-E-20260803-Failure Cases Are Better/failure_cases_are_better_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-XPRINT Traffic Privacy/xprint_traffic_privacy_manuscript.md` - XPRINT Traffic Privacy - DEP-E; overlap: trade-off, defense, attack, security, says.
2. `.lake-data/DEP-E/DEP-E-20260721-Feature Denoising/feature_denoising_manuscript.md` - Feature Denoising - DEP-E; overlap: trade-off, defense, attack, adversarial, learned.
3. `.lake-data/DEP-E/DEP-E-20260716-PIArena Evaluation/piarena_evaluation_manuscript.md` - PIArena Evaluation - DEP-E; overlap: trade-off, defense, attack, security, adversarial.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
