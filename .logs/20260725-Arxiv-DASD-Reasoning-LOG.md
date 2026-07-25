# Arxiv DEP Log: DASD Reasoning

- Public date marker: 2026-07-25.
- Selected paper: *Distribution-Aligned Sequence Distillation for Superior Long-CoT Reasoning*.
- Stable identifiers: arXiv:2601.09088; DOI:10.48550/arXiv.2601.09088.
- Canonical record: https://arxiv.org/abs/2601.09088.

## Selection

- Method: `rg --files -g "*.pdf"` enumerated the private archive. Each unique PDF parent directory was a paper unit; the selected unit's filename and nearby README supplied the normalized arXiv ID and title.
- Candidate count: 75,780 PDFs collapsed to 75,777 unique parent-paper units.
- Random draw: PowerShell `Get-Random` selected zero-based index 56,517 from the sorted fixed parent-unit list. The first draw was accepted.
- Exclusions and reselections: 0 duplicate exclusions encountered; 0 reselections.
- Dedup validation: searched the public dedup index, Black Lake `.logs`, `.reports`, `.lake-data`, automation memory, relevant Black-Lake-Data entries, title, DOI, arXiv ID, slug, and same-paper markers within 24 hours. No owning Arxiv DEP artifact or recent marker was found.

## Source Integrity

- Initial state: partial. The existing 1,036,676-byte PDF passed the 10 KB minimum, `%PDF-` header, and trailing `%%EOF` checks, but full-paper HTML was absent.
- Repair: a bounded local-only companion-bundle repair retained the valid PDF and added verified full-paper HTML, metadata HTML, and the TeX source package. The local README, provenance record, machine-readable summary, and verification report were refreshed.
- Final state: complete. The full-paper HTML is 251,282 bytes with 81,512 body characters, a document marker, 65 heading/section markers, and six paper-structure terms. No partial files remained.
- Source policy: PDF, HTML, source package, cache, extracted text, provenance, and rendered pages remain local. No source file or `.source/` directory is included in this repository change.

## Outputs

- `.logs/20260725-Arxiv-DASD-Reasoning-LOG.md`
- `.logs/20260725-Arxiv-DASD-Reasoning-PHASE-LOG.md`
- `.reports/BL-Arxiv-DASD-Reasoning-20260725/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260725-DASD Reasoning/README.md`
- `.lake-data/DEP-E/DEP-E-20260725-DASD Reasoning/dasd_reasoning_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. Do the gains attributed to divergence-aware sampling persist under independent data filtering, compute budgets, and repeated random seeds?
2. How sensitive is mixed-policy distillation to prefix truncation, quality filters, and teacher-model revision across domains other than the reported benchmarks?
3. Can the released 4B model, data recipe, and configuration reproduce the reported table under an independently frozen evaluation manifest?

## Challenges

1. The paper's benchmark results and ablations were inspected but not independently reproduced.
2. `pdftotext` was unavailable; the cache used the successful `pypdf` fallback alongside full-paper HTML and TeX extraction.
3. The public release describes model and data resources, but their compute, license, dataset, and configuration requirements were not executed or independently audited in this run.

## Outcome

Source-first review, local integrity repair, cache extraction, related-DEP synthesis, and public-artifact validation are complete. Repository and Slack submission status are appended after remote verification.
