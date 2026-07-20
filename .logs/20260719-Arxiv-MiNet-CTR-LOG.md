# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260719-7D93E819`
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P07`
- Public-safe run date: 2026-07-19
- Outcome: reviewed replacement validated and prepared for submission
- Selected paper: *MiNet: Mixed Interest Network for Cross-Domain Click-Through Rate Prediction*
- Stable identifier: `arXiv:2008.02974v1`
- Canonical URL: https://arxiv.org/abs/2008.02974

## Random Selection

- Method: `rg --files -g "*.pdf"`, unique PDF-parent units, uniform PowerShell `Get-Random` index.
- Refreshed pool: 75,790 PDFs across 75,777 paper units.
- First draw: index 64,910, arXiv:2102.13303; rejected at the complete-source gate after bounded repair because fallback HTML was a conversion notice.
- Replacement draw: index 42,352; selection accepted. The job exclusion set prevented reuse of the rejected unit and six completed papers.
- Duplicate exclusions: 0; source-gate rejections: 1; reselections: 1.

## Deduplication and Reselection

- Scanned Black Lake logs, reports, DEP-E artifacts/indexes, this automation memory, relevant Black-Lake-Data records, and the current-job set.
- Keys: arXiv ID, DOI, normalized title, `MiNet-CTR` slug, prior cron markers, and markers on or after cutoff date 2026-07-18.
- Accepted paper had no prior or current-job match.

## Source Integrity

- Initial classification: partial; valid PDF present, full-paper HTML absent.
- One bounded repair used approved ar5iv full-paper HTML after official HTML was unavailable and retrieved official metadata.
- PDF: 2,269,189 bytes; `%PDF-` and trailing `%%EOF` passed.
- Full-paper HTML: 506,059 bytes; 72,409 body characters; document marker; 30 headings; five structure terms; no rejected payload pattern.
- Cache: `cached`; PDF and HTML extraction succeeded; unexpected partials: 0.
- Final state: complete. All source and cache files remain local.

## Public Outputs

- `.logs/20260719-Arxiv-MiNet-CTR-LOG.md`
- `.reports/BL-Arxiv-MiNet-CTR-20260719/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260719-MiNet CTR Transfer/README.md`
- `.lake-data/DEP-E/DEP-E-20260719-MiNet CTR Transfer/minet_ctr_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` - preference signals, feedback loops, and balanced evaluation.
2. `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` - input-dependent routing and runtime evidence.
3. `.lake-data/DEP-E/DEP-E-20260716-XPRINT Traffic Privacy/xprint_traffic_privacy_manuscript.md` - behavioral side channels and privacy-minimized measurement.

## Submission Gate

- Allowlist: generated Markdown plus required publication-index Markdown and dedup JSON.
- `.source/`: not created. Source-document upload: none.
- Private paths, exact local timestamps, timezone labels, and user/machine context are withheld.
