# Arxiv DEP Log: CuraLight

- Public date marker: 2026-07-24.
- Selected paper: *CuraLight: Debate-Guided Data Curation for LLM-Centered Traffic Signal Control*.
- Stable identifiers: arXiv:2604.05663v2; DOI 10.48550/arXiv.2604.05663.
- Canonical records: https://arxiv.org/abs/2604.05663 and https://doi.org/10.48550/arXiv.2604.05663.

## Selection

- Method: `rg --files -g "*.pdf"` enumerated the private archive; each unique PDF parent directory was one paper unit. Normalized arXiv identifiers were reconciled against Black Lake `.logs`, `.reports`, `.lake-data`, this automation's memory, and relevant Black-Lake-Data entries.
- Counts: 75,780 PDFs; 75,777 paper units; 268 previously used identifier matches excluded; 185 identifier-incomplete units withheld; 75,324 eligible units.
- Draw: PowerShell `Get-Random` selected zero-based eligible index 12,989 from the sorted fixed pool. A preliminary diagnostic draw was discarded before eligibility was frozen because its identifier derivation was incomplete; the corrected full-pool draw was accepted with zero duplicate reselections.
- Dedup: exact arXiv ID, DOI, normalized title, `CuraLight` slug, owning-artifact, automation-memory, related-repository, and preceding-24-hour scans found no prior Arxiv DEP deposit or recent same-paper marker. A related-repository author inventory row was metadata only and did not own a DEP.

## Source Integrity

- Initial state: partial. The existing 7,295,610-byte PDF passed the 10 KB minimum, `%PDF-` header, trailing `%%EOF`, and six-page parser checks; full-paper HTML was missing.
- Repair: preserved the valid PDF and collected broker-paced metadata HTML plus official arXiv full-paper HTML. The local README, attribution record, machine-readable summary, acquisition receipt, and verification report were updated.
- Final state: complete. Full-paper HTML is 188,114 bytes with 34,193 body characters, a document marker, 46 heading/section markers, and six paper-structure terms. Metadata HTML is 43,015 bytes. No partial files remain.
- Optional source package: not collected because the TeX endpoint redirected to a route rejected by the archive broker. This does not affect the PDF-plus-full-paper-HTML completion gate.
- Source policy: every PDF, HTML page, metadata record, receipt, verification file, and review render remains private and local. No source document or `.source/` directory is included in this repository change.

## Outputs

- `.logs/20260724-Arxiv-CuraLight-LOG.md`
- `.reports/BL-Arxiv-CuraLight-20260724/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260724-CuraLight Review/README.md`
- `.lake-data/DEP-E/DEP-E-20260724-CuraLight Review/curalight_review_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Do the reported gains persist across repeated seeds, confidence intervals, unseen demand regimes, and traffic incidents rather than only the seven fixed SUMO traces?
2. How do the RL critic and LLM preference judge behave when they disagree systematically, and what calibration or abstention rule prevents a biased feedback loop?
3. Can the deliberation ensemble meet real controller latency, safety, fallback, and operator-audit requirements on physical intersections?

## Challenges

1. The evaluation is simulation-only, and the inspected paper does not report uncertainty intervals, significance tests, or a road-deployment safety case.
2. Reproduction remains incomplete because exact prompts, judge-model identities, training-data counts, key mixture weights, seeds, and a locked environment were not established.
3. Textual rationales and hidden debate improve inspectability but do not prove faithful causal explanations; runtime evidence retention and disagreement governance remain open.

## Outcome

Source review and public-artifact validation completed. Repository and Slack submission status are recorded in the automation result after remote verification.
