# Arxiv DEP Log: Willmore Loop Groups

- Public date marker: 2026-07-25.
- Selected paper: *Willmore surfaces in spheres via loop groups I: generic cases and some examples*.
- Stable identifiers: arXiv:1301.2756v4; DOI:10.48550/arXiv.1301.2756.
- Canonical record: https://arxiv.org/abs/1301.2756.

## Selection

- Method: `rg --files -g "*.pdf"` enumerated the private source archive. Each unique PDF parent directory was one paper unit; normalized arXiv identifiers came from the folder and PDF names, with nearby metadata inspected for the selected unit.
- Counts: 75,780 PDFs; 75,777 paper units; 324 prior-identifier matches excluded; 185 identifier-incomplete units withheld; 75,268 eligible units.
- Draw: PowerShell `Get-Random` selected zero-based eligible index 48,133 from the sorted fixed eligible pool. The first frozen-pool draw was accepted; duplicate reselections: 0.
- Dedup: the arXiv ID, DOI, normalized title, `willmore-loop-groups` slug, repository artifacts, automation memory, relevant Black-Lake-Data entries, and preceding-24-hour markers were checked. No owning Arxiv DEP deposit or recent same-paper marker was found.

## Source Integrity

- Initial state: partial. The preserved 580,177-byte PDF passed the 10 KB minimum, `%PDF-` header, trailing `%%EOF`, and 47-page parser check; full-paper HTML was missing.
- Repair: the valid PDF was preserved. A bounded local-only repair collected metadata HTML and a validated ar5iv full-paper HTML fallback, then refreshed the local README, provenance record, machine-readable summary, and verification report.
- Final state: complete. The full-paper HTML is 6,514,846 bytes with 300,514 body characters, a document marker, 171 heading/section markers, and seven paper-structure terms. Metadata HTML is 42,751 bytes. No partial files remain.
- Source policy: PDF, metadata HTML, full-paper HTML, repair records, and any local review material remain private and local. No source file or `.source/` directory is included in this repository change.

## Outputs

- `.logs/20260725-Arxiv-Willmore-Loop-Groups-LOG.md`
- `.reports/BL-Arxiv-Willmore-Loop-Groups-20260725/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260725-Willmore Loop Groups/README.md`
- `.lake-data/DEP-E/DEP-E-20260725-Willmore Loop Groups/willmore_loop_groups_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Which singularities in the non-compact Iwasawa factorization are removable in the reconstructed Willmore surface, and which represent genuine geometric degeneration?
2. Can the normalized-potential construction be implemented with interval or symbolic checks that distinguish a valid conformal Gauss map from a harmonic map that does not reconstruct to an immersion?
3. How do the follow-up classifications of Willmore two-spheres constrain the explicit non-S-Willmore example and the broader moduli problem?

## Challenges

1. The central results are theorem-driven and were not formally verified, so the deposit reports proof structure rather than a correctness certificate.
2. The non-compact Iwasawa decomposition is only local on open cells; a naïve numerical construction can cross a cell boundary and produce misleading singular frames.
3. No official implementation, executable examples, or reproducible numerical manifest was identified in the inspected primary sources.

## Outcome

Source review and public-artifact validation completed. Repository and Slack submission status are recorded after remote verification.
